"""Build a video from a script JSON: cover (hook voice, title, mascot) -> paper tear -> scenes with white pop-in subs, moods, mascot cameo."""
import io, contextlib, os, sys, json, tempfile, subprocess, numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    import opening_frames as O
from opening_frames import *
import shorts, soundfile as sf, scenes_hk
from PIL import ImageEnhance
from tulinh2 import phrases, ease_out
FPS, CX, TEAR = 30, 548, 0.3
MOOD = {"kich": ((210, 40, 40), .30, .82), "huyen": ((130, 80, 210), .32, .95), "tram": ((90, 110, 150), .28, .80)}


def tint(im, col, k, br): return Image.blend(ImageEnhance.Brightness(im.convert("RGB")).enhance(br), Image.new("RGB", im.size, col), k).convert("RGBA")


def fast(a, r=1.08):
    i, o = os.path.join(tempfile.gettempdir(), "_i.wav"), os.path.join(tempfile.gettempdir(), "_o.wav"); sf.write(i, a, shorts.SR)
    subprocess.run([shorts.FFMPEG, "-y", "-i", i, "-af", f"atempo={r}", o], capture_output=True); return sf.read(o, dtype="float32")[0]


def say(text, t0, words, audio):
    for ph in phrases(text):
        a = fast(shorts.speak(ph)); d = len(a) / shorts.SR; words += shorts.spread(ph, t0, t0 + d)
        pause = 0.18 if ph[-1] in ".?!" else 0.06; audio += [a, np.zeros(int(pause * shorts.SR), np.float32)]; t0 += d + pause
    return t0


def title2(im, l1, l2, a=1.0, dy=0):
    L = Image.new("RGBA", (W, 700), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    for j, (t_, col) in enumerate(((l1, (255, 216, 77, 255)), (l2, (255, 255, 255, 255)))):
        sz = 152
        while d.textlength(t_, font=font(F_BLACK, sz)) > 900: sz -= 6
        f = font(F_BLACK, sz); xy = (W / 2, 150 + j * 190)
        d.text(xy, t_, font=f, fill="white", anchor="mm", stroke_width=32, stroke_fill="white"); d.text(xy, t_, font=f, fill=INK, anchor="mm", stroke_width=15, stroke_fill=INK); d.text(xy, t_, font=f, fill=col, anchor="mm")
    if a < 1: L.putalpha(L.split()[3].point(lambda v: int(v * a)))
    im.alpha_composite(L, (0, 160 + int(dy)))


def main(path):
    sc = json.load(open(path, encoding="utf8")); reg = scenes_hk.registry(); L1, L2 = sc["title"]
    glow, mist = A.sprite_glow(), Image.new("RGBA", (10, 10)); cache = {}

    def data(name):
        if name not in cache: cache[name] = reg[name]()
        return cache[name]
    cover_bg = S2.frame({"data": data(sc["scenes"][0]["scene"])}, 1.0, 5, glow, mist).convert("RGBA"); cover_bg.alpha_composite(S2.sword_glow(540, 1150, 380))

    def cover(t):
        u = min(max((t - 1.0) / 0.6, 0), 1); im = cover_bg.copy(); title2(im, L1, L2, 1 - .55 * u, -50 * u)
        mascot(im, 0 if t < 0.7 else 1, 1150, CX, int(300 * u + 260 * max(u - .5, 0)) + 16, 0 if t < 0.7 else 2); return im
    audio = [np.zeros(int(0.2 * shorts.SR), np.float32)]; hw = []; t = say(sc["hook"], 0.2, hw, audio)
    C = max(t, 1.6); audio.append(np.zeros(int(max(C - t, 0) * shorts.SR), np.float32)); t0 = C; words = []; ranges = []
    for s in sc["scenes"]: tb = t0; t0 = say(s["text"], t0, words, audio); ranges.append((tb, t0))
    total = t0 + 0.6; ranges[-1] = (ranges[-1][0], total)
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) == 2 or w[3]: chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    starts = [c[0][0] for c in chunks]; texts = [" ".join(w[2] for w in c) for c in chunks]; ends = [c[-1][1] for c in chunks]
    wav = os.path.join(tempfile.gettempdir(), "hk.wav"); sf.write(wav, shorts.mix(np.concatenate(audio), [C] + [r[0] for r in ranges[1:]], total), shorts.SR)
    p = subprocess.Popen([shorts.FFMPEG, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", wav, "-af", "acompressor=threshold=-26dB:ratio=3.5:attack=5:release=90:makeup=6,loudnorm=I=-16.5:TP=-1.5:LRA=7",
                          "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", sc["out"]], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    prev = {}

    def raw(k, tt):
        s = sc["scenes"][k]; lt = max(tt - ranges[k][0], 0); im = S2.frame({"data": data(s["scene"]), "ripple": s["scene"] in ("returned", "ripple")}, lt, ranges[k][1] - ranges[k][0], glow, mist).convert("RGBA")
        return tint(im, *MOOD[s["mood"]]) if s.get("mood") else im

    def scene_frame(k, tt):
        im = raw(k, tt); lt = tt - ranges[k][0]
        if lt < 0.25 and k > 0:
            if prev.get("k") != k - 1: prev.update(k=k - 1, im=raw(k - 1, ranges[k - 1][1]))
            im = Image.blend(prev["im"], im, max(lt, 0) / 0.25)
        return im
    for fr in range(int(total * FPS)):
        tt = fr / FPS; k = next((i for i, (a, b) in enumerate(ranges) if a <= tt < b), len(ranges) - 1)
        if tt < C:
            im = cover(tt)
            if tt > C - TEAR: u = (tt - (C - TEAR)) / TEAR; im = torn_wipe(im, scene_frame(0, ranges[0][0]), (W + 40) * (1 - u) - 60 * u)
        else:
            im = scene_frame(k, tt); s = sc["scenes"][k]
            if s.get("mascot"):
                lt = tt - ranges[k][0]
                if lt < 1.8:
                    if lt < 0.45: u = lt / 0.45; up = 1 + 2.2 * (u - 1) ** 3 + 1.2 * (u - 1) ** 2
                    elif lt < 1.35: up = 1.0
                    else: u = (lt - 1.35) / 0.45; up = 1 - u * u * (3 - 2 * u)
                    mascot(im, 0, 760, 790, int(820 * (1 - up)), 4 * (1 - up))
            ci = max((i for i, x in enumerate(starts) if x <= tt), default=None)
            if ci is not None and tt < ends[ci] + 0.9:
                sp = caption_sprite(texts[ci]); kk = .85 + .15 * ease_out((tt - starts[ci]) / .1); sz = (max(int(sp.width * kk), 2), max(int(sp.height * kk), 2)); pic = sp.resize(sz, Image.LANCZOS) if kk < .999 else sp
                im.alpha_composite(pic, (int(W / 2 - pic.width / 2), int(1345 - pic.height / 2)))
        p.stdin.write(im.convert("RGB").tobytes())
    p.stdin.close(); p.wait(); return sc["out"], total


if __name__ == "__main__": print(main(sys.argv[1] if len(sys.argv) > 1 else "hoan_kiem.json"))
