"""Simplified paper-cut story: few big flat shapes, one focal subject per scene, clean pill-style captions."""
import math, os, sys, tempfile, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import shorts, animate as A
import story2 as S
from story2 import layer, grad, wave, fill_wave, D, W, H, PAD, FPS, CREAM, RED, GOLD, EDGE, INK

NAVY, TEAL1, TEAL2, TEAL3 = "#1d3557", "#2a6f7f", "#235f6e", "#1b4f5e"
FONT = "C:/Windows/Fonts/seguibl.ttf"


# ---------- simple shapes (all scale with s) ----------
def person(d, cx, base, s):
    p = lambda dx, dy: (cx + dx * s, base + dy * s)
    d.polygon([p(-55, 0), p(-32, -140), p(32, -140), p(55, 0)], fill=RED)
    d.rectangle((*p(-40, -80), *p(40, -62)), fill=GOLD)
    d.ellipse((*p(-30, -206), *p(30, -140)), fill="#f3dcb4")
    d.polygon([p(-18, -168), p(18, -168), p(0, -128)], fill="#2b2420")
    d.ellipse((*p(-13, -190), *p(-5, -182)), fill="#2b2420"); d.ellipse((*p(5, -190), *p(13, -182)), fill="#2b2420")
    d.polygon([p(-44, -208), p(44, -208), p(34, -232), p(-34, -232)], fill="#1b1b22")
    d.polygon([p(-76, -222), p(-44, -220), p(-44, -208), p(-74, -208)], fill="#1b1b22"); d.polygon([p(76, -222), p(44, -220), p(44, -208), p(74, -208)], fill="#1b1b22")


def turtle(d, cx, cy, s):
    p = lambda dx, dy: (cx + dx * s, cy + dy * s)
    dome = [p(200 * math.cos(math.radians(a)), -120 * math.sin(math.radians(a))) for a in range(0, 181, 6)]
    d.polygon(dome, fill=GOLD); d.ellipse((*p(-210, -18), *p(210, 28)), fill="#d99a1c")
    for gx, gy in ((-100, -52), (0, -70), (100, -52)): d.regular_polygon((cx + gx * s, cy + gy * s, 38 * s), 6, fill="#ffcf55")
    d.polygon([p(-160, 6), p(-240, 66), p(-180, 90), p(-110, 30)], fill="#d99a1c")
    d.ellipse((*p(-330, -86), *p(-200, 8)), fill=GOLD); d.ellipse((*p(-308, -64), *p(-284, -40)), fill=INK)


def boat(d, cx, cy, s):
    p = lambda dx, dy: (cx + dx * s, cy + dy * s)
    d.polygon([p(-210, -36), p(-120, 60), p(120, 60), p(210, -36), p(110, -2), p(-110, -2)], fill="#7a3b1d"); d.rectangle((*p(-150, 6), *p(150, 20)), fill=CREAM)
    d.line([p(60, -60), p(200, 80)], fill="#4a2410", width=int(10 * s))


# ---------- layers ----------
def lake_layers(y0=1150):
    out = []
    for i, (dy, col) in enumerate(((0, TEAL1), (150, TEAL2), (320, TEAL3))):
        out.append((1.0 + 0.5 * i, layer(lambda d, y=y0 + dy, c=col, i=i: fill_wave(d, y, 10, 60 + 8 * i, i, c), 8, 6), None))
    return out


def tower_layer():
    def f(d):
        d.ellipse((130, 1090, 560, 1190), fill="#2f6a4a")
        cx = 345; tiers = [(230, 110), (180, 100), (130, 90)]
        for i, (w_, h_) in enumerate(tiers):
            top = 1130 - sum(h for _, h in tiers[:i + 1]); d.rectangle((cx - w_ // 2, top, cx + w_ // 2, top + h_), fill=CREAM)
            d.rectangle((cx - w_ // 2 - 18, top - 14, cx + w_ // 2 + 18, top + 4), fill=RED)
            x = cx; d.polygon([(x - 22, top + h_), (x - 22, top + h_ - 46), (x, top + h_ - 70), (x + 22, top + h_ - 46), (x + 22, top + h_)], fill=INK)
        d.polygon([(cx - 44, 1130 - 300 - 14), (cx, 1130 - 300 - 66), (cx + 44, 1130 - 300 - 14)], fill=RED)
    return layer(f, 8, 6)


def hill_far():
    return layer(lambda d: fill_wave(d, 1080, 36, 110, 1.5, "#1f4258"), 6, 4)


def night(mid, tower=False):
    bg = S.cached("n3bg", lambda: _night_bg())
    ls = [(0.4, S.cached("hill3", hill_far), None)] + ([(0.7, S.cached("tower3", tower_layer), None)] if tower else []) + mid + lake_layers()
    return bg, ls


def _night_bg():
    bg = grad((24, 42, 74), (38, 80, 108)).convert("RGBA")
    gl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(gl).ellipse((600, 460, 1000, 860), fill=(244, 234, 210, 100))
    bg = Image.alpha_composite(bg, gl.filter(ImageFilter.GaussianBlur(60))); ImageDraw.Draw(bg).ellipse((650, 510, 950, 810), fill=CREAM)
    return bg.convert("RGB")


def rays_simple():
    im = Image.new("RGBA", (1900, 1900), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for i in range(10):
        a0 = math.radians(i * 36); a1 = a0 + math.radians(12)
        d.polygon([(950, 950), (950 + 950 * math.cos(a0), 950 + 950 * math.sin(a0)), (950 + 950 * math.cos(a1), 950 + 950 * math.sin(a1))], fill=(255, 225, 130, 46))
    return im


def build_scenes():
    sc = []
    sc.append(dict(mid=lambda: night([], True)))
    def B():
        bg = grad((58, 30, 66), (240, 140, 80)).convert("RGBA"); d = ImageDraw.Draw(bg)
        d.ellipse((540 - 300, 1060 - 300, 540 + 300, 1060 + 300), fill=(255, 214, 120, 255))
        hill = layer(lambda d: (fill_wave(d, 1180, 30, 160, 0.5, "#2a1530"), person(d, 640, 1170, 2.3)), 8, 6)
        sw0 = S.sword_rgba(440).rotate(-14, expand=True, resample=Image.BICUBIC); sw = Image.new('RGBA', (sw0.width + 170, sw0.height), (0, 0, 0, 0)); sw.alpha_composite(sw0, (170, 0))  # shift the sword to the figure's hand side
        return bg.convert("RGB"), [(1.0, hill, None), (0, "sword", sw)]
    sc.append(dict(mid=B))
    sc.append(dict(mid=lambda: night([(0.9, layer(lambda d: (boat(d, 540, 1150, 1.5), person(d, 520, 1156, 1.5)), 10, 8), lambda t: (0, 8 * math.sin(t * 2.2)))])))
    def D_():
        b = layer(lambda d: (boat(d, 300, 1150, 1.3), person(d, 285, 1156, 1.3)), 10, 8)
        t = layer(lambda d: turtle(d, 760, 1120, 1.2), 10, 8)
        return night([(0.9, b, lambda t_: (0, 8 * math.sin(t_ * 2.2))), (0.9, t, lambda t_: (0, max(0, 200 - 200 * min(t_ / 1.3, 1) ** 0.5) + 6 * math.sin(t_ * 2.6)))])
    sc.append(dict(mid=D_))
    def E(): return grad((18, 24, 52), (44, 34, 78)), [(0, "rays", rays_simple()), (0, "glow", S.sword_glow(540, 900, 300)), (0, "swordc", S.sword_rgba(520))]
    sc.append(dict(mid=E))
    def F_():
        tl = layer(lambda d: turtle(d, 600, 1130, 1.3), 10, 8); sw = S.sword_rgba(300).rotate(90, expand=True); tl.alpha_composite(sw, (600 - 560 + PAD, 1130 - 30))
        return night([(0.9, tl, lambda t_: (0, 8 * math.sin(t_ * 2) + max(0, t_ - 1.0) * 130))])
    sc.append(dict(mid=F_, ripple=True))
    def Hs(): return grad((16, 28, 58), (28, 56, 84)), [(0, "glow", S.sword_glow(540, 900, 320)), (0, "spiral", S.spiral_img())]
    sc.append(dict(mid=Hs))
    sc.append(dict(mid=lambda: night([], True)))
    return sc


# ---------- captions / title ----------
def font(s): return ImageFont.truetype(FONT, s)


_cap = {}


def caption(words, cur):
    key = (tuple(words), cur)
    if key in _cap: return _cap[key]
    size = 92
    while True:
        f = font(size); d0 = ImageDraw.Draw(Image.new("RGBA", (10, 10))); ws = [d0.textlength(w, font=f) for w in words]
        if sum(ws) + 34 * (len(words) - 1) + 64 <= 900 or size <= 56: break
        size -= 4
    H_ = 200; im = Image.new("RGBA", (W, H_), (0, 0, 0, 0)); sh = Image.new("RGBA", (W, H_), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh); d = ImageDraw.Draw(im)
    x = W / 2 - (sum(ws) + 34 * (len(words) - 1)) / 2; cy = H_ // 2
    for i, (w, wd) in enumerate(zip(words, ws)):
        if i == cur:
            d.rounded_rectangle((x - 24, cy - size * 0.62, x + wd + 24, cy + size * 0.62), 30, fill=(255, 216, 77, 255)); d.text((x, cy), w, font=f, fill=(27, 27, 34, 255), anchor="lm")
        else:
            sd.text((x, cy + 5), w, font=f, fill=(0, 0, 0, 150), anchor="lm"); d.text((x, cy), w, font=f, fill=(255, 255, 255, 255), anchor="lm")
        x += wd + 34
    out = Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)), im); _cap[key] = out
    return out


def title_pill(text="Vì sao gọi là Hồ Hoàn Kiếm?"):
    f = font(54); d0 = ImageDraw.Draw(Image.new("RGBA", (10, 10))); tw = d0.textlength(text, font=f)
    im = Image.new("RGBA", (W, 140), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((W / 2 - tw / 2 - 40, 20, W / 2 + tw / 2 + 40, 120), 50, fill=(255, 216, 77, 255)); d.text((W / 2, 70), text, font=f, fill=(27, 27, 34, 255), anchor="mm")
    return im


def main(beats, out):
    audio, words, t0, ranges = [], [], 0.0, []
    for text in beats:
        a = shorts.speak(text); d = len(a) / shorts.SR
        words += shorts.spread(text, t0, t0 + d); ranges.append((t0, t0 + d + shorts.GAP))
        audio += [a, np.zeros(int(shorts.GAP * shorts.SR), np.float32)]; t0 += d + shorts.GAP
    ranges[-1] = (ranges[-1][0], t0 + 0.6); total = t0 + 0.6
    groups, cur = [], []
    for i, w in enumerate(words):
        cur.append(i)
        if len(cur) == 3 or w[3]: groups.append(cur); cur = []
    if cur: groups.append(cur)
    gid = {i: g for g, idx in enumerate(groups) for i in idx}
    scenes = build_scenes()
    for sc in scenes: sc["data"] = sc["mid"]()
    glow = A.sprite_glow(); mist = Image.new("RGBA", (10, 10)); title = title_pill()
    import soundfile as sf
    wav = os.path.join(tempfile.gettempdir(), "story3.wav"); sf.write(wav, shorts.mix(np.concatenate(audio), [r[0] for r in ranges[1:]], total), shorts.SR)
    p = subprocess.Popen([shorts.FFMPEG, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", wav, "-c:v", "libx264", "-preset", "veryfast",
                          "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", out], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    prev = None
    for fr in range(int(total * FPS)):
        t = fr / FPS; k = next((i for i, (a, b) in enumerate(ranges) if a <= t < b), len(ranges) - 1); lt = t - ranges[k][0]; dur = ranges[k][1] - ranges[k][0]
        im = S.frame(scenes[k], lt, dur, glow, mist)
        if lt < 0.25 and k > 0:
            if prev is None or prev[0] != k: pd = ranges[k - 1][1] - ranges[k - 1][0]; prev = (k, S.frame(scenes[k - 1], pd, pd, glow, mist))
            im = Image.blend(prev[1], im, lt / 0.25)
        im.alpha_composite(title, (0, 190))
        ci = next((i for i, w in enumerate(words) if w[0] <= t < w[1] + 0.05), None)
        if ci is not None:
            idx = groups[gid[ci]]; im.alpha_composite(caption([words[i][2] for i in idx], idx.index(ci)), (0, 1300))
        ImageDraw.Draw(im).rounded_rectangle((60, 1850, 60 + int((W - 120) * t / total), 1862), 6, fill=(255, 216, 77, 255))
        p.stdin.write(im.convert("RGB").tobytes())
    p.stdin.close(); p.wait()
    return out, total


def stills(out):
    scenes = build_scenes(); cells = []; glow = A.sprite_glow(); mist = Image.new("RGBA", (10, 10)); title = title_pill()
    for sc in scenes:
        sc["data"] = sc["mid"](); im = S.frame(sc, 1.6, 4, glow, mist); im.alpha_composite(title, (0, 190)); im.alpha_composite(caption(["trả", "cho", "ai?"], 1), (0, 1300)); cells.append(im.convert("RGB").resize((270, 480)))
    s = Image.new("RGB", (270 * 4, 480 * 2), "#111")
    for i, c in enumerate(cells): s.paste(c, ((i % 4) * 270, (i // 4) * 480))
    s.save(out)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "still": stills("out/story3_stills.png"); print("ok")
    else: print(main(S.BEATS, "out/story3_papercut.mp4"))
