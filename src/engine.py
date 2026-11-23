"""Cached, per-scene video engine. Voice cached per phrase, video cached per scene clip (key = content hash + art-code version),
scenes render in parallel in a process pool, final = ffmpeg concat (no re-encode) + mixed audio.
Durations are quantised to 1/15 s so every scene is independent of the others (editing one never invalidates its neighbours' clips)."""
import io, os, sys, json, math, random, time, hashlib, contextlib, subprocess, tempfile, threading, numpy as np, soundfile as sf
from concurrent.futures import ProcessPoolExecutor
from PIL import Image
import shorts
from tulinh2 import phrases

SRC = os.path.dirname(os.path.abspath(__file__)); HERE = os.path.dirname(SRC)  # SRC = code, HERE = project root (assets, cache, projects, exports, previews)
if SRC not in sys.path: sys.path.insert(0, SRC)
os.chdir(HERE)  # some art modules write/read paths relative to the root
CACHE = os.path.join(HERE, "cache"); OUT = os.path.join(HERE, "out"); EXPORTS = os.path.join(HERE, "exports"); PREVIEWS = os.path.join(HERE, "previews")
for d in ("tts", "clips", "audio", "still", "preview"): os.makedirs(os.path.join(CACHE, d), exist_ok=True)
os.makedirs(OUT, exist_ok=True)
SR, RATE, Q, TEAR, XF, SHOT_XF = shorts.SR, 1.12, 1 / 15, 0.3, 0.25, 0.3
MODES = {"draft": dict(fps=15, scale=0.5), "final": dict(fps=30, scale=1.0)}
CODE = ("engine.py", "build.py", "scenes_hk.py", "scenes_hk2.py", "opening_frames.py", "animate.py", "story2.py", "story3.py", "tulinh.py", "tulinh2.py", "tulinh3.py")
_tts_lock = threading.Lock()


def code_version():
    h = hashlib.sha1()
    for f in CODE:
        p = os.path.join(SRC, f)
        if os.path.exists(p): s = os.stat(p); h.update(f"{f}{s.st_mtime_ns}{s.st_size}".encode())
    return h.hexdigest()[:12]


def sha(o): return hashlib.sha1(json.dumps(o, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:20]


# ---------------------------------------------------------------- voice
def _fast(a, rate):
    with tempfile.TemporaryDirectory() as d:
        i, o = os.path.join(d, "i.wav"), os.path.join(d, "o.wav"); sf.write(i, a, SR)
        subprocess.run([shorts.FFMPEG, "-y", "-i", i, "-af", f"atempo={rate}", o], capture_output=True, check=True); return sf.read(o, dtype="float32")[0]


def _rawpath(ph): return os.path.join(CACHE, "tts", "raw_" + sha([ph, "haidang"]) + ".npy")


def voice(ph, gen=True, rate=RATE):
    """Raw TTS is cached once per phrase; the speed-up is a cheap ffmpeg pass cached per rate (so the speed slider costs ~nothing)."""
    raw, fast = _rawpath(ph), os.path.join(CACHE, "tts", f"{rate}_" + sha([ph, "haidang"]) + ".npy")
    if os.path.exists(fast): return np.load(fast)
    if not os.path.exists(raw):
        if not gen: return None
        with _tts_lock:
            if not os.path.exists(raw): np.save(raw, shorts.speak(ph))
    a = _fast(np.load(raw), rate); np.save(fast, a); return a


def missing_phrases(text): return [ph for ph in phrases(text) if not os.path.exists(_rawpath(ph))]


def unit(text, gen=True, lead=0.0, min_len=0.0, tail=0.0, rate=RATE):
    """Audio + quantised duration + 2-word caption chunks (times relative to the unit start)."""
    t, pieces, words, starts = lead, [np.zeros(int(lead * SR), np.float32)], [], []
    for ph in phrases(text):
        starts.append(t); a = voice(ph, gen, rate)
        if a is None: return None
        d = len(a) / SR; words += shorts.spread(ph, t, t + d)
        pause = 0.12 if ph[-1] in ".?!" else 0.04; pieces += [a, np.zeros(int(pause * SR), np.float32)]; t += d + pause
    dur = math.ceil(max(t + tail, min_len) / Q - 1e-9) * Q; pieces.append(np.zeros(max(int(dur * SR) - sum(len(x) for x in pieces), 0), np.float32))
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) == 2 or w[3]: chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    return dict(audio=np.concatenate(pieces)[:int(dur * SR)], dur=dur, starts=starts, chunks=[(c[0][0], c[-1][1], " ".join(w[2] for w in c)) for c in chunks])


def plan(sc, gen=True):
    """Units for cover + every scene; None entries when voice is missing and gen=False."""
    n = len(sc["scenes"])
    r = sc.get("speed", RATE); cover = unit(sc["hook"], gen, lead=0.2, min_len=1.6, rate=r)
    us = [unit(s["text"], gen, tail=0.6 if i == n - 1 else 0, rate=r) for i, s in enumerate(sc["scenes"])]
    return cover, us


# ---------------------------------------------------------------- tasks
def desc(s, u=None):
    d = {"scene": s["scene"], "mood": s.get("mood"), "mascot": bool(s.get("mascot")), "cam": s.get("cam"), "at": s.get("at"), "fx": s.get("fx")}
    if s.get("shots") and u:  # extra shots: switch visual at the start of phrase x["at"], resolved to seconds from the voice timing
        n = len(u["starts"]); d["shots"] = sorted(({"t": round(u["starts"][min(x["at"], n - 1)], 2), "scene": x["scene"], "mood": x.get("mood"), "fx": x.get("fx")} for x in s["shots"]), key=lambda x: x["t"])
    return d


def make_task(sc, k, cover, us, mode, at=None):
    """k = -1 for cover. Returns picklable task dict, or None if voice missing."""
    m = MODES[mode]; scs = sc["scenes"]
    if k < 0:
        if cover is None or us[0] is None: return None
        T = dict(kind="cover", title=sc["title"], dur=cover["dur"], desc0=desc(scs[0], us[0]), dur0=us[0]["dur"], bg=sc.get("cover", scs[0]["scene"]))
    else:
        u = us[k]
        if u is None or (k > 0 and us[k - 1] is None): return None
        T = dict(kind="scene", desc=desc(scs[k], u), dur=u["dur"], chunks=u["chunks"], text=scs[k]["text"], prev=({"desc": desc(scs[k - 1], us[k - 1]), "dur": us[k - 1]["dur"]} if k > 0 else None))
    T.update(fps=m["fps"], scale=m["scale"], at=at); return T


def clip_path(T, mode): return os.path.join(CACHE, "clips", f"{mode}_{sha([T, code_version()])}.mp4")


# ---------------------------------------------------------------- workers (run in pool processes)
_C = {}


def _ctx():
    if not _C:
        with contextlib.redirect_stdout(io.StringIO()):
            import build as B
        _C.update(B=B, reg=B.scenes_hk.registry(), glow=B.A.sprite_glow(), mist=B.Image.new("RGBA", (10, 10)), data={}, spr={}, cb={})
    return _C


def warm(): _ctx(); return os.getpid()


def _raw1(d, lt, dur):
    c = _ctx(); B = c["B"]
    if d["scene"] not in c["data"]:
        c["data"][d["scene"]] = c["reg"][d["scene"]]()
        while len(c["data"]) > 6: c["data"].pop(next(iter(c["data"])))  # every scene is ~50 MB of layers: keep a small LRU, not all of them
    s = {"data": c["data"][d["scene"]], "ripple": d["scene"] in ("returned", "ripple")}
    if "fireflies" in (d.get("fx") or []): r = random.Random(7); s["fly"] = [(r.uniform(0, B.W), r.uniform(800, 1600), r.uniform(0, 6.28), r.uniform(.5, 1.2)) for _ in range(18)]
    im = _camera(B.S2.frame(s, max(lt, 0), dur, c["glow"], c["mist"]).convert("RGBA"), d, lt, dur)
    return B.tint(im, *B.MOOD[d["mood"]]) if d.get("mood") else im


def _raw(d, lt, dur):
    """Scene image; with d['shots'] the visual switches at each shot start (0.3 s dissolve), each shot animating from its own start."""
    if not d.get("shots"): return _raw1(d, lt, dur)
    seq = [(0.0, d)] + [(x["t"], {**d, "scene": x["scene"], "mood": x.get("mood"), "fx": x.get("fx"), "shots": None}) for x in d["shots"]]
    i = max(j for j, (t0, _) in enumerate(seq) if t0 <= lt or j == 0); t0 = seq[i][0]; t1 = seq[i + 1][0] if i + 1 < len(seq) else dur
    im = _raw1(seq[i][1], max(lt - t0, 0), t1 - t0)
    if i and lt - t0 < SHOT_XF:
        p0 = seq[i - 1][0]; im = Image.blend(_raw1(seq[i - 1][1], lt - p0, t0 - p0), im, max(lt - t0, 0) / SHOT_XF)
    return im


# camera presets: zoom start/end + centre start/end (pixels); "at" in the scene overrides the zoom centre
CAMS = {"zoomin": ([1.0, 1.4], None, None), "zoomout": ([1.4, 1.0], None, None), "panr": ([1.3, 1.3], (380, 960), (700, 960)), "panl": ([1.3, 1.3], (700, 960), (380, 960))}


def _camera(im, d, lt, dur):
    if d.get("cam") not in CAMS: return im
    z, a, b = CAMS[d["cam"]]; at = tuple(d.get("at") or (540, 960)); a, b = a or at, b or at
    u = min(max(lt / max(dur, 0.1), 0), 1); u = u * u * (3 - 2 * u); zz = z[0] + (z[1] - z[0]) * u
    cx, cy = a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u; w, h = 1080 / zz, 1920 / zz
    x0 = min(max(cx - w / 2, 0), 1080 - w); y0 = min(max(cy - h / 2, 0), 1920 - h)
    return im.crop((int(x0), int(y0), int(x0 + w), int(y0 + h))).resize((1080, 1920), Image.BILINEAR)


def _cover(T, t):
    """Cover: background keeps drifting; mascot rises from the bottom, holds, switches pose, sinks."""
    c = _ctx(); B = c["B"]; d0 = T["desc0"]; L1, L2 = T["title"]
    if T["bg"] not in c["cb"]: c["cb"][T["bg"]] = (c["reg"][T["bg"]](), B.S2.sword_glow(540, 1150, 380))
    data, gl = c["cb"][T["bg"]]
    u = min(max((t - 1.0) / 0.6, 0), 1); im = B.S2.frame({"data": data}, 1.0 + t, 5, c["glow"], c["mist"]).convert("RGBA"); im.alpha_composite(gl)
    B.title2(im, L1, L2, 1 - .55 * u, -50 * u)
    v = min(t / 0.45, 1); rise = 1250 * (1 - v) ** 3  # mascot slides up from below the frame (ease-out, no overshoot so its cut bottom never shows), holds, switches pose, then sinks
    B.mascot(im, 0 if t < 0.7 else 1, 1150, B.CX, int(300 * u + 260 * max(u - .5, 0) + rise) + 26, 0 if t < 0.7 else 2)
    if t > T["dur"] - TEAR: u = (t - (T["dur"] - TEAR)) / TEAR; im = B.torn_wipe(im, _raw(d0, 0, T["dur0"]), (B.W + 40) * (1 - u) - 60 * u)
    return im


def _scene(T, lt, st):
    c = _ctx(); B = c["B"]; d = T["desc"]; im = _raw(d, lt, T["dur"])
    if T["prev"] and lt < XF:
        if "pv" not in st: st["pv"] = _raw(T["prev"]["desc"], T["prev"]["dur"], T["prev"]["dur"])
        im = B.Image.blend(st["pv"], im, max(lt, 0) / XF)
    if d["mascot"] and lt < 1.8:
        if lt < 0.45: u = lt / 0.45; up = 1 + 2.2 * (u - 1) ** 3 + 1.2 * (u - 1) ** 2
        elif lt < 1.35: up = 1.0
        else: u = (lt - 1.35) / 0.45; up = 1 - u * u * (3 - 2 * u)
        B.mascot(im, 0, 760, 790, 60 + int(820 * (1 - up)), 4 * max(1 - up, 0))  # +60: the flat cut bottom stays below the frame even on the overshoot
    ch = [x for x in T["chunks"] if x[0] <= lt]
    if ch and lt < ch[-1][1] + 0.9:
        s0, _, txt = ch[-1]
        if txt not in c["spr"]: c["spr"][txt] = B.caption_sprite(txt)
        sp = c["spr"][txt]; kk = .85 + .15 * B.ease_out((lt - s0) / .1); pic = sp.resize((max(int(sp.width * kk), 2), max(int(sp.height * kk), 2)), B.Image.LANCZOS) if kk < .999 else sp
        im.alpha_composite(pic, (int(B.W / 2 - pic.width / 2), int(1345 - pic.height / 2)))
    return im


def _frame(T, lt, st):
    im = _cover(T, lt) if T["kind"] == "cover" else _scene(T, lt, st)
    B = _ctx()["B"]
    if T["scale"] < 1: return im.convert("RGB").resize((int(B.W * T["scale"]), int(B.H * T["scale"])), B.Image.BILINEAR)
    return im.convert("RGB")


def render_task(T, out):
    """Encode one clip (atomic), or return PNG bytes when T['at'] is set."""
    fps, st = T["fps"], {}
    if T.get("at") is not None:
        buf = io.BytesIO(); _frame(T, min(T["at"], T["dur"] - 1e-3), st).save(buf, "PNG"); return buf.getvalue()
    if os.path.exists(out): return out
    n = round(T["dur"] * fps); B = _ctx()["B"]; w, h = int(B.W * T["scale"]), int(B.H * T["scale"]); draft = T["scale"] < 1
    tmp = out + ".part"
    p = subprocess.Popen([shorts.FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", str(fps), "-i", "-", "-c:v", "libx264", "-preset", "ultrafast" if draft else "veryfast",
                          "-crf", "30" if draft else "19", "-pix_fmt", "yuv420p", "-g", str(fps * 2), "-f", "mp4", tmp], stdin=subprocess.PIPE)
    for i in range(n): p.stdin.write(_frame(T, i / fps, st).tobytes())
    p.stdin.close(); p.wait(); os.replace(tmp, out); return out


# ---------------------------------------------------------------- pool
_pool = [None, None]


def pool():
    v = code_version()
    if _pool[0] is None or _pool[1] != v or getattr(_pool[0], "_broken", False):
        if _pool[0]: _pool[0].shutdown(wait=False, cancel_futures=True)
        _pool[0] = ProcessPoolExecutor(max_workers=max(2, min(6, (os.cpu_count() or 4) - 2))); _pool[1] = v
    return _pool[0]


def prewarm(): [pool().submit(warm) for _ in range(pool()._max_workers)]


def still(sc, k, t, mode="draft"):
    cover, us = plan(sc, gen=False); T = make_task(sc, k, cover, us, mode, at=float(t))
    if T is None: return None
    p = os.path.join(CACHE, "still", f"{mode}_{sha([T, code_version()])}.png")
    if not os.path.exists(p):
        data = pool().submit(render_task, T, "").result()
        with open(p, "wb") as f: f.write(data)
    return p


# ---------------------------------------------------------------- jobs
def _wav(name, arr):
    p = os.path.join(CACHE, "audio", name); sf.write(p, arr, SR); return p


def scene_audio(sc, k, cb=lambda *a: None):
    """Voice for one scene only (cheapest loop: edit the words, listen)."""
    cb("Tạo giọng", 0, 1); u = unit(sc["scenes"][k]["text"], rate=sc.get("speed", RATE)); cb("Xong", 1, 1)
    return _wav(f"scene_{sha([sc['scenes'][k]['text'], sc.get('speed', RATE)])}.wav", u["audio"]), u["dur"]


def status(sc):
    """Per-scene cache state for the UI."""
    cover, us = plan(sc, gen=False); res = []
    for k, s in enumerate(sc["scenes"]):
        r = {"tts": us[k] is not None, "dur": us[k]["dur"] if us[k] else None}
        for mode in MODES:
            T = make_task(sc, k, cover, us, mode); r[mode] = bool(T) and os.path.exists(clip_path(T, mode))
        res.append(r)
    c = {"tts": cover is not None, "dur": cover["dur"] if cover else None}
    for mode in MODES: T = make_task(sc, -1, cover, us, mode); c[mode] = bool(T) and os.path.exists(clip_path(T, mode))
    return {"cover": c, "scenes": res, "total": sum(r["dur"] or 0 for r in res) + (c["dur"] or 0)}


def _render_clips(sc, cover, us, mode, cb, only=None):
    items = [(-1, make_task(sc, -1, cover, us, mode))] + [(k, make_task(sc, k, cover, us, mode)) for k in range(len(us))]
    items = [(k, T, clip_path(T, mode)) for k, T in items if only is None or k in only]
    todo = [x for x in items if not os.path.exists(x[2])]; cb(f"Vẽ {len(todo)}/{len(items)} clip (còn lại dùng bản lưu)", 0, max(len(todo), 1))
    fs = [pool().submit(render_task, T, p) for _, T, p in todo]
    for i, f in enumerate(fs): f.result(); cb(f"Vẽ clip {i + 1}/{len(todo)}", i + 1, len(todo))
    return {k: p for k, _, p in items}


def render(sc, mode="draft", name="video", cb=lambda *a: None):
    miss = sum(len(missing_phrases(s["text"])) for s in sc["scenes"]) + len(missing_phrases(sc["hook"]))
    if miss: cb(f"Tạo giọng ({miss} câu mới)", 0, miss)
    cover, us = plan(sc, gen=True)
    clips = _render_clips(sc, cover, us, mode, cb)
    cb("Ghép clip + trộn âm thanh", 1, 1)
    units = [cover] + us; voice_ = np.concatenate([u["audio"] for u in units]); total = sum(u["dur"] for u in units)
    cuts = list(np.cumsum([u["dur"] for u in units[:-1]]))
    wav = _wav(f"mix_{sha([name, mode])}.wav", shorts.mix(voice_, cuts, total))
    lst = os.path.join(CACHE, "audio", f"list_{mode}.txt")
    with open(lst, "w", encoding="utf8") as f: f.writelines(f"file '{clips[k].replace(chr(92), '/')}'\n" for k in [-1] + list(range(len(us))))
    if mode == "final": os.makedirs(os.path.join(EXPORTS, name), exist_ok=True); out = os.path.join(EXPORTS, name, f"{name}_{time.strftime('%Y%m%d_%H%M%S')}.mp4")  # finals are versioned, never overwritten
    else: os.makedirs(os.path.join(PREVIEWS, name), exist_ok=True); out = os.path.join(PREVIEWS, name, f"{name}_{mode}.mp4")  # previews live apart from finals
    subprocess.run([shorts.FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-i", wav, "-c:v", "copy", "-af", "acompressor=threshold=-26dB:ratio=3.5:attack=5:release=90:makeup=6,loudnorm=I=-16.5:TP=-1.5:LRA=7",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", out], check=True)
    return out, total


def preview_scene(sc, k, cb=lambda *a: None):
    miss = len(missing_phrases(sc["scenes"][k]["text"])) + (len(missing_phrases(sc["scenes"][k - 1]["text"])) if k else 0)
    if miss: cb("Tạo giọng", 0, miss)
    us = [None] * len(sc["scenes"])
    for j in (k - 1, k):
        if j >= 0: us[j] = unit(sc["scenes"][j]["text"], True, tail=0.6 if j == len(us) - 1 else 0, rate=sc.get("speed", RATE))
    T = make_task(sc, k, None, us, "draft"); p = clip_path(T, "draft"); cb("Vẽ cảnh", 0, 1); pool().submit(render_task, T, p).result()
    wav = _wav(f"scene_{sha([sc['scenes'][k]['text'], sc.get('speed', RATE)])}.wav", us[k]["audio"]); out = os.path.join(CACHE, "preview", f"scene_{sha([T, code_version()])}.mp4")
    if not os.path.exists(out): subprocess.run([shorts.FFMPEG, "-y", "-loglevel", "error", "-i", p, "-i", wav, "-c:v", "copy", "-c:a", "aac", "-shortest", out], check=True)
    return out
