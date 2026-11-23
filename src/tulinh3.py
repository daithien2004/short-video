"""Tu Linh v3: own look (sticker die-cut outlines + Dong Son drum motif + scalloped ground) and the mascot
peeking over the ground edge: intro (surprised, then ducks out) and question outro (thinking pose)."""
import math, os, re, sys, tempfile, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import shorts, tulinh as T, tulinh2 as T2
from tulinh import W, H, FPS, DK, F_BLACK, F_BOLD, font, spr, spaced, bg_img, ease_back
from tulinh2 import caption_sprite, with_alpha, ease_out, fact_layer, phrases, CAP_Y, FACT_Y

MASCOT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "mascot")
GROUND = 1250
SC = [dict(s) for s in T.SCENES]
SC[0].update(mode="pop", ground=GROUND, dots=None, mascot=dict(pose=0, t_in=0.1, t_out=1.9, h=720))
SC[0]["items"] = [("long", 270, 760, 0.5, 2.1), ("lan", 810, 760, 0.5, 2.6), ("quy", 270, 1030, 0.5, 3.1), ("phung", 810, 1030, 0.5, 3.6)]
SC[1].update(mode="rise", ground=1250, dots=0)
SC[2].update(mode="rise", ground=1195, dots=1)
SC[3].update(mode="pop", ground=GROUND, dots=None, mascot=dict(pose=1, t_in=0.3, t_out=None, h=520), q=True)
SC[3]["items"] = [("long", 180, 740, 0.4, 0.3), ("lan", 900, 740, 0.4, 0.7), ("quy", 180, 980, 0.4, 1.1), ("phung", 900, 980, 0.4, 1.5)]
BEATS = T.BEATS
_STK, _MASC, _MOTIF = {}, {}, {}


def sticker(img, r=15):
    """White die-cut outline + soft shadow around any RGBA sprite."""
    a = img.split()[3]; dil = a.filter(ImageFilter.GaussianBlur(r / 2)).point(lambda v: 255 if v > 8 else 0).filter(ImageFilter.GaussianBlur(1.2))
    white = Image.new("RGBA", img.size, (255, 255, 255, 255)); white.putalpha(dil)
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0)); sh.putalpha(dil.point(lambda v: int(v * 0.38))); sh = sh.filter(ImageFilter.GaussianBlur(9))
    from PIL import ImageChops
    sh = ImageChops.offset(sh, 0, 10)
    return Image.alpha_composite(Image.alpha_composite(sh, white), img)


def sprite_sticker(n):
    if n not in _STK: _STK[n] = sticker(spr(n))
    return _STK[n]


def mascot(pose, h):
    key = (pose, h)
    if key not in _MASC:
        im = Image.open(os.path.join(MASCOT_DIR, f"{pose}.png")).convert("RGBA")
        ref = Image.open(os.path.join(MASCOT_DIR, "0.png")).convert("RGBA").split()[3].getbbox(); s = h / (ref[3] - ref[1] - 26)  # h keeps its old meaning (pose-0 bbox height)
        im = im.crop((395, ref[1], 1125, 1005))  # one shared box for both poses: head centre ~x=760 -> centred; bottom drops the white sticker strip
        _MASC[key] = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    return _MASC[key]


def dongson(size=1500):
    if "m" in _MOTIF: return _MOTIF["m"]
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im); c = size // 2; col = (255, 244, 214, 40)
    for r, w in ((90, 8), (190, 6), (300, 10), (410, 6), (520, 8), (640, 6), (740, 10)): d.ellipse((c - r, c - r, c + r, c + r), outline=col, width=w)
    n = 36
    for i in range(n):  # zig-zag triangle band between rings
        a0, a1, am = 2 * math.pi * i / n, 2 * math.pi * (i + 1) / n, 2 * math.pi * (i + .5) / n
        d.polygon([(c + 195 * math.cos(a0), c + 195 * math.sin(a0)), (c + 295 * math.cos(am), c + 295 * math.sin(am)), (c + 195 * math.cos(a1), c + 195 * math.sin(a1))], fill=col)
    for i in range(48): a = 2 * math.pi * i / 48; d.ellipse((c + 585 * math.cos(a) - 11, c + 585 * math.sin(a) - 11, c + 585 * math.cos(a) + 11, c + 585 * math.sin(a) + 11), fill=col)
    pts = []
    for i in range(24): r = 80 if i % 2 == 0 else 34; a = math.pi * 2 * i / 24 - math.pi / 2; pts.append((c + r * math.cos(a), c + r * math.sin(a)))
    d.polygon(pts, fill=col); _MOTIF["m"] = im
    return im


def ground_img(y, c1):
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(g); base = tuple(int(c * 0.85) for c in c1); light = tuple(min(255, int(c * 1.9) + 30) for c in c1)
    for x in range(-30, W + 60, 64): d.ellipse((x - 32, y - 20, x + 32, y + 20), fill=light + (255,))   # scalloped (wave) edge
    d.rectangle((0, y, W, H), fill=light + (255,)); d.rectangle((0, y + 14, W, H), fill=base + (255,))
    for x in range(-30, W + 60, 64): d.ellipse((x - 32, y - 6, x + 32, y + 34), fill=base + (255,))
    d.rectangle((0, y + 20, W, H), fill=base + (255,))
    return g


def title_layer(sc, idx_dots):
    im = Image.new("RGBA", (W, 520), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = font(F_BLACK, 130); xy = (W / 2, 80)
    d.text(xy, sc["main"], font=f, fill="white", anchor="mm", stroke_width=26, stroke_fill="white")     # die-cut sticker text
    d.text(xy, sc["main"], font=f, fill=DK, anchor="mm", stroke_width=11, stroke_fill=DK); d.text(xy, sc["main"], font=f, fill=sc["mc"], anchor="mm")
    spaced(d, (W / 2, 190), sc["sub"], font(F_BOLD, 38), "white", 5, stroke=7, sf=DK)
    if idx_dots is not None:
        for i in range(4):
            x = W / 2 + (i - 1.5) * 46; on = i == idx_dots; d.ellipse((x - 12, 240, x + 12, 264), fill="#ffd24d" if on else None, outline="white", width=4)
    return im


def render(sc, t, bg, gnd, tl, fl, cap):
    im = bg.copy().convert("RGBA"); sec = sc.get("mode") == "rise"
    mot = dongson().rotate(t * 2.5 + (sc["name"] == "quy") * 40, resample=Image.BILINEAR); im.paste(mot, (540 - 750, 790 - 750), mot)  # slowly turning Dong Son drum motif
    for n, x, y, s, t0 in sc["items"]:
        sp = sprite_sticker(n); tilt = 3 * math.sin(2 * math.pi * t / 3.2 + x)
        if sec:
            k = ease_out((t - t0) / 1.0)
            if k <= 0: continue
            sz = int(700 * s); pic = sp.resize((sz, sz), Image.LANCZOS); yy = y + (1 - k) * sz * 0.75 + 3 * math.sin(2 * math.pi * t / 2.8)
        else:
            k = ease_back((t - t0) / 0.4)
            if k <= 0: continue
            sz = max(int(700 * s * k), 2); pic = sp.resize((sz, sz), Image.LANCZOS); yy = y + 4 * math.sin(2 * math.pi * t / 2.8 + x)
        pic = pic.rotate(tilt, resample=Image.BILINEAR); im.paste(pic, (int(x - pic.width / 2), int(yy - pic.height / 2)), pic)
        if sc.get("q") and t > t0 + 0.4:
            d = ImageDraw.Draw(im); qx, qy = x, y - 130; d.ellipse((qx - 36, qy - 36, qx + 36, qy + 36), fill="#ffd24d", outline=DK, width=6); d.text((qx, qy), "?", font=font(F_BLACK, 50), fill=DK, anchor="mm")
    m = sc.get("mascot")
    if m:  # peeks over the ground edge, optional duck-out
        up = ease_back((t - m["t_in"]) / 0.45); down = ease_out((t - m["t_out"]) / 0.3) if m["t_out"] is not None else 0
        if up > 0 and down < 1:
            pic = mascot(m["pose"], m["h"]); off = (1 - min(up, 1.0)) * (pic.height + 40) + down * (pic.height + 40) - max(up - 1, 0) * 22
            ang = 2.5 * math.sin(2 * math.pi * (t - m["t_in"]) / 2.2); pad = Image.new("RGBA", (pic.width + 160, pic.height + 40), (0, 0, 0, 0)); pad.alpha_composite(pic, (80, 0))
            pad = pad.rotate(ang, center=(pad.width / 2, pad.height), resample=Image.BILINEAR); im.paste(pad, (int(m.get('cx', 540) - pad.width / 2), int(GROUND - pic.height + 30 + off)), pad)
    if gnd is not None: im.alpha_composite(gnd)
    im.alpha_composite(with_alpha(tl, min(t / 0.2, 1)), (0, 190))
    if sc.get("q"):
        if t > 1.2:
            c = Image.new("RGBA", (W, 260), (0, 0, 0, 0)); cd = ImageDraw.Draw(c); cd.rounded_rectangle((90, 20, 990, 220), 36, fill=(20, 12, 40, 235), outline="#ffd24d", width=5)
            cd.ellipse((120, 70, 190, 140), fill="#ffd24d"); cd.text((155, 105), "?", font=font(F_BLACK, 56), fill=DK, anchor="mm")
            cd.text((220, 84), "Theo bạn, linh vật nào", font=font(F_BOLD, 46), fill="white", anchor="lm"); cd.text((220, 148), "quyền năng nhất?", font=font(F_BOLD, 46), fill="white", anchor="lm")
            im.alpha_composite(c, (0, 1420))
    elif sc["fact"] and t > 2.4:
        im.alpha_composite(with_alpha(fl, min((t - 2.4) / 0.3, 1)), (0, FACT_Y - 60))
    if cap:
        text, local = cap; s_ = caption_sprite(text); k = 0.85 + 0.15 * ease_out(local / 0.1)
        pic = s_.resize((max(int(s_.width * k), 2), max(int(s_.height * k), 2)), Image.LANCZOS) if k < 0.999 else s_
        im.alpha_composite(pic, (int(W / 2 - pic.width / 2), int(CAP_Y - pic.height / 2)))
    return im.convert("RGB")


def assets():
    bgs = [bg_img(*sc["bg"]) for sc in SC]; gnds = [ground_img(sc["ground"], sc["bg"][1]) if sc.get("ground") else None for sc in SC]
    return bgs, gnds, [title_layer(sc, sc.get("dots")) for sc in SC], [fact_layer(sc["fact"]) if sc["fact"] else None for sc in SC]


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
    bgs, gnds, tls, fls = assets()
    import soundfile as sf
    wav = os.path.join(tempfile.gettempdir(), "tulinh3.wav"); sf.write(wav, shorts.mix(np.concatenate(audio), [r[0] for r in ranges[1:]], total), shorts.SR)
    p = subprocess.Popen([shorts.FFMPEG, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", wav, "-af",
                          "acompressor=threshold=-26dB:ratio=3.5:attack=5:release=90:makeup=6,loudnorm=I=-16.5:TP=-1.5:LRA=7", "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
                          "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", out], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    for fr in range(int(total * FPS)):
        t = fr / FPS; k = next((i for i, (a, b) in enumerate(ranges) if a <= t < b), len(ranges) - 1)
        ci = max((i for i, s in enumerate(starts) if s <= t), default=None); cap = None
        if ci is not None and t < ends[ci] + 0.9: cap = (texts[ci], t - starts[ci])
        p.stdin.write(render(SC[k], t - ranges[k][0], bgs[k], gnds[k], tls[k], fls[k], cap).tobytes())
    p.stdin.close(); p.wait()
    return out, total


def stills(out):
    bgs, gnds, tls, fls = assets(); cells = []
    for i, (sc, tt) in enumerate(zip(SC, (1.0, 4.5, 4.5, 3.0))):
        cells.append(render(sc, tt, bgs[i], gnds[i], tls[i], fls[i], ("đầu tiên là", 0.3)).resize((270, 480)))
    s = Image.new("RGB", (270 * 4, 480), "#111")
    for i, c in enumerate(cells): s.paste(c, (i * 270, 0))
    s.save(out)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "still": stills("out/tulinh3_stills.png"); print("ok")
    else: print(main(BEATS, "out/tulinh3_preview.mp4"))
