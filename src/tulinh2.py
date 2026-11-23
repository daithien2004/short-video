"""Tu Linh v2: applies measurements from the reference video.
- captions: white, 1-2 words, ~0.5s, pop-in 0.1s, always on screen, ~70% height, no highlight
- gold fact line fades in ~2.4s after a section starts and stays
- voice: synthesised phrase by phrase, 0.45s pause after sentences / 0.3s after commas, loudness-normalised
- section characters rise from the ground edge, then nearly still; title fades in with progress dots"""
import math, os, re, sys, tempfile, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import shorts, tulinh as T
from tulinh import W, H, FPS, DK, F_BLACK, F_BOLD, font, spr, spaced, bg_img, ease_back

SC = [dict(s) for s in T.SCENES]
SC[0].update(mode="pop")
SC[1].update(mode="rise", ground=1250, dots=0)
SC[2].update(mode="rise", ground=1195, dots=1)
SC[3].update(mode="pop")
BEATS = T.BEATS
CAP_Y, FACT_Y = 1345, 1590
_capc = {}


def ground_img(y, c1):
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(g)
    col = tuple(int(c * 0.85) for c in c1) + (255,); d.rectangle((0, y, W, H), fill=col)
    d.rectangle((0, y, W, y + 8), fill=tuple(min(255, int(c * 1.7) + 25) for c in c1) + (255,)); d.line((0, y, W, y), fill=DK, width=6)
    return g


def caption_sprite(text):
    if text in _capc: return _capc[text]
    f = font(F_BLACK, 74); d0 = ImageDraw.Draw(Image.new("RGBA", (10, 10))); tw = d0.textlength(text, font=f)
    im = Image.new("RGBA", (int(tw) + 80, 150), (0, 0, 0, 0)); sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((im.width / 2, 80), text, font=f, fill=(0, 0, 0, 170), anchor="mm", stroke_width=9, stroke_fill=(0, 0, 0, 170))
    d = ImageDraw.Draw(im); d.text((im.width / 2, 75), text, font=f, fill="white", anchor="mm", stroke_width=8, stroke_fill=DK)
    out = Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(4)), im); _capc[text] = out
    return out


def title_layer(sc, idx_dots):
    im = Image.new("RGBA", (W, 520), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.text((W / 2, 70), sc["main"], font=font(F_BLACK, 130), fill=sc["mc"], anchor="mm", stroke_width=9, stroke_fill=DK)
    spaced(d, (W / 2, 170), sc["sub"], font(F_BOLD, 38), sc["sc"], 5, stroke=5)
    if idx_dots is not None:
        for i in range(4):
            x = W / 2 + (i - 1.5) * 46; on = i == idx_dots; d.ellipse((x - 11, 222, x + 11, 244), fill="#ffd24d" if on else None, outline="#ffd24d" if on else sc["sc"], width=4)
    return im


def fact_layer(text):
    im = Image.new("RGBA", (W, 120), (0, 0, 0, 0)); spaced(ImageDraw.Draw(im), (W / 2, 60), text, font(F_BLACK, 52), "#ffd666", 7, stroke=6)
    return im


def with_alpha(layer, a):
    l = layer.copy(); l.putalpha(layer.split()[3].point(lambda v: int(v * a))); return l


def ease_out(u): u = min(max(u, 0), 1); return 1 - (1 - u) ** 3


def render(sc, t, bg, gnd, tl, fl, cap):
    im = bg.copy().convert("RGBA"); sec = sc.get("mode") == "rise"
    for n, x, y, s, t0 in sc["items"]:
        sp = spr(n)
        if sec:
            k = ease_out((t - t0) / 1.0)
            if k <= 0: continue
            sz = int(700 * s); pic = sp.resize((sz, sz), Image.LANCZOS); yy = y + (1 - k) * sz * 0.75 + 3 * math.sin(2 * math.pi * t / 2.8)
            im.paste(pic, (int(x - sz / 2), int(yy - sz / 2)), pic)
        else:
            k = ease_back((t - t0) / 0.4)
            if k <= 0: continue
            sz = max(int(700 * s * k), 2); pic = sp.resize((sz, sz), Image.LANCZOS); yy = y + 4 * math.sin(2 * math.pi * t / 2.8 + x)
            im.paste(pic, (int(x - sz / 2), int(yy - sz / 2)), pic)
            if sc.get("q") and t > t0 + 0.4:
                d = ImageDraw.Draw(im); qx, qy = x, y - 135; d.ellipse((qx - 36, qy - 36, qx + 36, qy + 36), fill="#ffd24d", outline=DK, width=6); d.text((qx, qy), "?", font=font(F_BLACK, 50), fill=DK, anchor="mm")
    if gnd is not None: im.alpha_composite(gnd)
    im.alpha_composite(with_alpha(tl, min(t / 0.2, 1)), (0, 200))
    if sc.get("q"):
        if t > 1.2:
            c = Image.new("RGBA", (W, 260), (0, 0, 0, 0)); cd = ImageDraw.Draw(c); cd.rounded_rectangle((90, 20, 990, 220), 36, fill=(20, 12, 40, 235), outline="#ffd24d", width=5)
            cd.ellipse((120, 70, 190, 140), fill="#ffd24d"); cd.text((155, 105), "?", font=font(F_BLACK, 56), fill=DK, anchor="mm")
            cd.text((220, 84), "Theo bạn, linh vật nào", font=font(F_BOLD, 46), fill="white", anchor="lm"); cd.text((220, 148), "quyền năng nhất?", font=font(F_BOLD, 46), fill="white", anchor="lm")
            im.alpha_composite(c, (0, 1420))
    elif sc["fact"] and t > 2.4:
        im.alpha_composite(with_alpha(fl, min((t - 2.4) / 0.3, 1)), (0, FACT_Y - 60))
    if cap:
        text, local = cap; spr_ = caption_sprite(text); k = 0.85 + 0.15 * ease_out(local / 0.1)
        sz = (max(int(spr_.width * k), 2), max(int(spr_.height * k), 2)); pic = spr_.resize(sz, Image.LANCZOS) if k < 0.999 else spr_
        im.alpha_composite(pic, (int(W / 2 - pic.width / 2), int(CAP_Y - pic.height / 2)))
    return im.convert("RGB")


def phrases(text): return [p.strip() for p in re.findall(r"[^.,?!:]+[.,?!:]?", text) if p.strip()]


def main(beats, out):
    audio, words, t0, ranges = [], [], 0.0, []
    for beat in beats:
        tb = t0
        for ph in phrases(beat):
            a = shorts.speak(ph); d = len(a) / shorts.SR; words += shorts.spread(ph, t0, t0 + d)
            pause = 0.28 if ph[-1] in ".?!" else 0.12; audio += [a, np.zeros(int(pause * shorts.SR), np.float32)]; t0 += d + pause
        ranges.append((tb, t0))
    total = t0 + 0.5; ranges[-1] = (ranges[-1][0], total)
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) == 2 or w[3]: chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    starts = [c[0][0] for c in chunks]; texts = [" ".join(w[2] for w in c) for c in chunks]; ends = [c[-1][1] for c in chunks]
    bgs = [bg_img(*sc["bg"]) for sc in SC]
    gnds = [ground_img(sc["ground"], sc["bg"][1]) if sc.get("ground") else None for sc in SC]
    tls = [title_layer(sc, sc.get("dots")) for sc in SC]; fls = [fact_layer(sc["fact"]) if sc["fact"] else None for sc in SC]
    import soundfile as sf
    wav = os.path.join(tempfile.gettempdir(), "tulinh2.wav"); sf.write(wav, shorts.mix(np.concatenate(audio), [r[0] for r in ranges[1:]], total), shorts.SR)
    p = subprocess.Popen([shorts.FFMPEG, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", wav, "-af", "acompressor=threshold=-26dB:ratio=3.5:attack=5:release=90:makeup=6,loudnorm=I=-16.5:TP=-1.5:LRA=7",
                          "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", out], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    for fr in range(int(total * FPS)):
        t = fr / FPS; k = next((i for i, (a, b) in enumerate(ranges) if a <= t < b), len(ranges) - 1)
        ci = max((i for i, s in enumerate(starts) if s <= t), default=None); cap = None
        if ci is not None and t < ends[ci] + 0.9: cap = (texts[ci], t - starts[ci])  # keep the chunk until the next one starts (always on screen)
        p.stdin.write(render(SC[k], t - ranges[k][0], bgs[k], gnds[k], tls[k], fls[k], cap).tobytes())
    p.stdin.close(); p.wait()
    return out, total


def stills(out):
    cells = []
    for i, sc in enumerate(SC):
        bg = bg_img(*sc["bg"]); g = ground_img(sc["ground"], sc["bg"][1]) if sc.get("ground") else None
        cells.append(render(sc, 4.5, bg, g, title_layer(sc, sc.get("dots")), fact_layer(sc["fact"]) if sc["fact"] else None, ("đầu tiên là", 0.3)).resize((270, 480)))
    s = Image.new("RGB", (270 * 4, 480), "#111")
    for i, c in enumerate(cells): s.paste(c, (i * 270, 0))
    s.save(out)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "still": stills("out/tulinh2_stills.png"); print("ok")
    else: print(main(BEATS, "out/tulinh2_preview.mp4"))
