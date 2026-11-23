"""Short video maker (Vietnamese): script -> VieNeu voice -> Commons photos (Ken Burns) -> word subs -> 9:16 MP4.
Script file: first line "# Title" (shown on screen, not spoken), then one line per beat: "image keywords | spoken text".
Run UI:  python shorts.py              (http://localhost:8000)
Run CLI: python shorts.py script.txt
"""
import json, os, re, subprocess, sys, tempfile, time, urllib.error, urllib.parse, urllib.request
import numpy as np

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
OUT, IMG = os.path.join(HERE, "out"), os.path.join(HERE, "assets", "img")
SR = 48000  # VieNeu v3 Turbo sample rate
GAP = 0.25  # seconds of silence between beats
WORDS_PER_CAPTION = 3
OK_LICENSES = re.compile(r"^(public domain|cc0|cc by \d|no restrictions|pd)", re.I)  # no BY-SA on purpose
_tts = None


def speak(text):
    global _tts
    if _tts is None:
        from vieneu import Vieneu
        _tts = Vieneu()  # default voice: Hai Dang (male)
    a = np.asarray(_tts.infer(text), dtype=np.float32)
    loud = np.flatnonzero(abs(a) > 0.02)  # trim TTS lead/tail silence so word timing matches
    return a[max(loud[0] - int(0.05 * SR), 0):loud[-1] + int(0.1 * SR)] if len(loud) else a


def get(req, timeout=60):
    for i in range(5):  # Wikimedia rate-limits bursts (429): back off and retry
        try:
            return urllib.request.urlopen(req, timeout=timeout).read()
        except urllib.error.HTTPError as e:
            if e.code != 429 or i == 4:
                raise
            time.sleep(4 * (i + 1))


def commons(q):
    """Return (path, credit) of a usable photo for keywords q, cached in assets/img."""
    os.makedirs(IMG, exist_ok=True)
    slug = re.sub(r"\W+", "_", q.lower()).strip("_")
    meta = os.path.join(IMG, slug + ".json")
    if os.path.exists(meta):
        m = json.load(open(meta, encoding="utf-8"))
        if os.path.exists(m["path"]):
            return m["path"], m["credit"]
    p = dict(action="query", format="json", generator="search", gsrsearch=q + " filetype:bitmap", gsrnamespace=6,
             gsrlimit=20, prop="imageinfo", iiprop="url|size|extmetadata", iiurlwidth=1920)
    req = urllib.request.Request("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(p),
                                 headers={"User-Agent": "shorts-maker/0.1"})
    pages = json.loads(get(req, 30)).get("query", {}).get("pages", {}).values()
    cands = []
    for pg in pages:
        i = pg["imageinfo"][0]
        lic = i["extmetadata"].get("LicenseShortName", {}).get("value", "")
        if OK_LICENSES.match(lic) and i["width"] >= 1000 and "/thumb/" in i.get("thumburl", "") and pg["title"].lower().endswith((".jpg", ".jpeg")):
            artist = re.sub("<[^>]+>", "", i["extmetadata"].get("Artist", {}).get("value", "")).strip()
            pd = lic.lower().startswith(("public", "cc0", "no ", "pd"))
            cands.append((not pd, pg["index"], i["thumburl"], f"{pg['title']} - {artist} - {lic} - {i['descriptionurl']}"))
    if not cands:
        return None, None
    cands.sort()
    _, _, url, credit = cands[0]
    path = os.path.join(IMG, slug + ".jpg")
    open(path, "wb").write(get(urllib.request.Request(url, headers={"User-Agent": "shorts-maker/0.1"})))
    time.sleep(1.5)
    json.dump({"path": path, "credit": credit}, open(meta, "w", encoding="utf-8"), ensure_ascii=False)
    return path, credit


def ts(t):
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def make_ass(words, path, title, dur, cards=()):
    head = ("[Script Info]\nPlayResX: 1080\nPlayResY: 1920\n[V4+ Styles]\n"
            "Format: Name,Fontname,Fontsize,PrimaryColour,OutlineColour,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Bold\n"
            "Style: D,Arial,92,&H00FFFFFF,&H00000000,1,7,0,2,40,40,420,1\n"
            "Style: B,Arial,190,&H0000E5FF,&H00000000,1,10,0,5,40,40,0,1\n"
            "Style: T,Arial,66,&H0000E5FF,&H00000000,1,6,0,8,60,60,200,1\n[Events]\n"
            "Format: Layer,Start,End,Style,Text\n")
    ev = []
    if title:  # fixed headline + progress bar
        ev.append(f"Dialogue: 1,{ts(0)},{ts(dur)},T,{title.upper()}")
        ev.append(f"Dialogue: 1,{ts(0)},{ts(dur)},D,{{\\an7\\pos(0,1890)\\p1\\1c&H00E5FF&\\bord0\\fscx1"
                  f"\\t(0,{int(dur * 1000)},\\fscx100)}}m 0 0 l 1080 0 1080 16 0 16")
    for a, b, txt in cards:  # big pop-in text on card scenes
        ev.append(f"Dialogue: 2,{ts(a)},{ts(b)},B,{{\\fad(80,0)\\fscx60\\fscy60\\t(0,150,\\fscx100\\fscy100)}}{txt}")
    for i in range(0, len(words), WORDS_PER_CAPTION):
        g = words[i:i + WORDS_PER_CAPTION]
        for j, w in enumerate(g):  # one event per word, current word yellow
            nxt = g[j + 1][0] if j + 1 < len(g) else (words[i + WORDS_PER_CAPTION][0] if i + WORDS_PER_CAPTION < len(words) else w[1] + 0.3)
            txt = " ".join(("{\\c&H00E5FF&}%s{\\c&HFFFFFF&}" if k == j else "%s") % x[2].upper() for k, x in enumerate(g))
            ev.append(f"Dialogue: 0,{ts(w[0])},{ts(nxt)},D,{txt}")
    open(path, "w", encoding="utf-8").write(head + "\n".join(ev) + "\n")


def spread(text, t0, t1):
    """No word timestamps from VieNeu: split [t0,t1] across words by character count."""
    ws = text.split()
    wt = [len(w) + (3 if w[-1] in ",.?!" else 0) for w in ws]  # punctuation = tiny pause
    t, out = t0, []
    for w, x in zip(ws, wt):
        d = (t1 - t0) * x / sum(wt)
        out.append((t, t + d, w.strip(",.?!:") or w, w[-1] in ",.?!:"))
        t += d
    return out


def segment(img, dur, k, out, d, color="0x24243e"):
    n = max(int(dur * 30), 1)
    if img:
        z = f"1+0.12*on/{n}" if k % 2 == 0 else f"1.12-0.12*on/{n}"
        vf = (f"scale=1296:2304:force_original_aspect_ratio=increase,crop=1296:2304,"
              f"zoompan=z='{z}':d={n}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30")
        src = ["-loop", "1", "-i", img]
    else:
        vf, src = "null", ["-f", "lavfi", "-i", f"gradients=s=1080x1920:r=30:c0={color}:c1=0x1a1040:speed=0.02"]
    subprocess.run([FFMPEG, "-y", *src, "-vf", vf, "-frames:v", str(n), "-c:v", "libx264", "-preset", "veryfast",
                    "-pix_fmt", "yuv420p", out], cwd=d, check=True, capture_output=True)


def mix(voice, cuts, total):
    """voice + generated ambient pad + whoosh on every cut (all synthesized, no licensing)."""
    n = int(total * SR)
    out = np.zeros(n, np.float32)
    v = voice[:n]
    out[:len(v)] += v * (0.9 / max(float(abs(v).max()), 1e-6))
    t = np.arange(n) / SR
    pad = sum(np.sin(2 * np.pi * f * t) for f in (110, 164.81, 220, 261.63)) / 4 * (0.6 + 0.4 * np.sin(2 * np.pi * 0.1 * t))
    out += (0.06 * pad * np.minimum(1, (total - t))).astype(np.float32)
    L = int(0.4 * SR)
    w = np.convolve(np.random.default_rng(0).standard_normal(L), np.ones(40) / 40, "same")
    w = (w / abs(w).max() * np.sin(np.pi * np.linspace(0, 1, L)) ** 2 * 0.2).astype(np.float32)
    for c in cuts:
        i = max(int(c * SR) - L // 2, 0)
        seg = out[i:i + L]
        seg += w[:len(seg)]
    return np.clip(out, -1, 1)


CARD_COLORS = ["0x5b2a9d", "0x1a7f99", "0xb03060"]


def make(lines, name=None):
    """Beat = "kw1 / kw2 | text" (photos, cut evenly) or "=BIG TEXT | text" (generated card scene)."""
    title = lines[0][1:].strip() if lines and lines[0].startswith("#") else ""
    beats, kw = [], ""
    for l in lines:
        if not l.strip() or l.startswith("#"):
            continue
        k, _, t = l.partition("|") if "|" in l else (kw, "", l)
        kw = k.strip() or kw
        beats.append((kw, t.strip()))
    os.makedirs(OUT, exist_ok=True)
    name = name or time.strftime("%Y%m%d-%H%M%S")
    out, credits = os.path.join(OUT, name + ".mp4"), []
    audio, words, durs, t = [], [], [], 0.0
    for kw, text in beats:
        a = speak(text)
        d = len(a) / SR + GAP
        words += spread(text, t, t + d - GAP)
        audio += [a, np.zeros(int(GAP * SR), np.float32)]
        durs.append(d)
        t += d
    total = t + 0.4
    with tempfile.TemporaryDirectory() as d:
        segs, cards, cuts, t, nc = [], [], [], 0.0, 0
        for bi, ((kw, _), dur) in enumerate(zip(beats, durs)):
            dur += 0.4 if bi == len(beats) - 1 else 0
            if kw.startswith("="):
                parts = [None]
                cards.append((t, t + dur, kw[1:].strip()))
            else:
                parts = [p.strip() for p in kw.split("/")]
            for pi, p in enumerate(parts):
                img = None
                if p:
                    try:
                        img, cr = commons(p)
                        if cr and cr not in credits:
                            credits.append(cr)
                    except Exception as e:
                        print("image fail", p, e)
                name_s = f"s{len(segs)}.mp4"
                segment(img, dur / len(parts), len(segs), name_s, d, CARD_COLORS[nc % 3])
                nc += 0 if p else 1
                segs.append(name_s)
                if segs[1:] and (bi or pi):
                    cuts.append(t + dur / len(parts) * pi)
            t += dur
        import soundfile as sf
        sf.write(os.path.join(d, "a.wav"), mix(np.concatenate(audio), cuts, total), SR)
        make_ass(words, os.path.join(d, "s.ass"), title, total, cards)
        open(os.path.join(d, "list.txt"), "w").write("".join(f"file '{s}'\n" for s in segs))
        subprocess.run([FFMPEG, "-y", "-f", "concat", "-i", "list.txt", "-i", "a.wav", "-vf",
                        "drawbox=color=black@0.25:t=fill,ass=s.ass", "-t", f"{total:.2f}", "-c:v", "libx264",
                        "-preset", "veryfast", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", out],
                       cwd=d, check=True, capture_output=True)
    open(out[:-4] + ".credits.txt", "w", encoding="utf-8").write("Hinh anh: Wikimedia Commons\n" + "\n".join(credits) + "\n")
    return out


PAGE = """<meta charset=utf-8><title>Shorts</title><body style="font:16px sans-serif;max-width:640px;margin:2em auto">
<h3>Tao short video</h3><textarea id=t rows=12 style="width:100%" placeholder="# Tieu de&#10;tu khoa anh | cau thoai&#10;tu khoa anh | cau thoai"></textarea><br>
<button onclick=go()>Tao video</button> <span id=s></span><br><br><video id=p controls width=270></video>
<script>async function go(){s.textContent='dang tao...';let r=await fetch('/make',{method:'POST',headers:{'content-type':'application/json'},
body:JSON.stringify({lines:t.value.split('\\n')})});let j=await r.json();s.textContent=j.error||'xong';if(j.url)p.src=j.url}</script>"""

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(make(open(sys.argv[1], encoding="utf-8").read().splitlines()))
    else:
        import uvicorn
        from fastapi import FastAPI
        from fastapi.responses import HTMLResponse
        from fastapi.staticfiles import StaticFiles
        app = FastAPI()
        os.makedirs(OUT, exist_ok=True)
        app.mount("/out", StaticFiles(directory=OUT))

        @app.get("/", response_class=HTMLResponse)
        def index():
            return PAGE

        @app.post("/make")
        def mk(b: dict):
            try:
                return {"url": "/out/" + os.path.basename(make(b["lines"]))}
            except Exception as e:
                return {"error": str(getattr(e, "stderr", b"") or e)[-300:]}

        uvicorn.run(app, port=8000)
