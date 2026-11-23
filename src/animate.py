"""Animated paper-cut preview: layers parallax, turtle rises on cue, mist, fireflies, voice + word captions. Pure code."""
import math, random, subprocess, sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageFont
import shorts

W, H, PAD, FPS = 1080, 1920, 70, 30
WW = W + 2 * PAD
NAVY, CREAM, RED, GOLD, GREEN, INK = "#1d3557", "#f4ead2", "#c8372d", "#f2b632", "#3f7d58", "#14213d"
random.seed(4)


class D:  # ImageDraw proxy: shifts x by PAD so layers are wider than the screen (room to slide)
    def __init__(s, d): s.d = d
    def _sh(s, xy):
        if isinstance(xy[0], (tuple, list)): return [(x + PAD, y) for x, y in xy]
        return [v + PAD if i % 2 == 0 else v for i, v in enumerate(xy)]
    def polygon(s, xy, **k): s.d.polygon(s._sh(xy), **k)
    def ellipse(s, xy, **k): s.d.ellipse(s._sh(xy), **k)
    def rectangle(s, xy, **k): s.d.rectangle(s._sh(xy), **k)
    def line(s, xy, **k): s.d.line(s._sh(xy), **k)
    def arc(s, xy, a, b, **k): s.d.arc(s._sh(xy), a, b, **k)
    def pieslice(s, xy, a, b, **k): s.d.pieslice(s._sh(xy), a, b, **k)
    def regular_polygon(s, bb, n, **k): s.d.regular_polygon((bb[0] + PAD, bb[1], bb[2]), n, **k)


def layer(fn, shadow=14, off=10):
    im = Image.new("RGBA", (WW, H), (0, 0, 0, 0)); fn(D(ImageDraw.Draw(im)))
    sh = Image.new("RGBA", (WW, H), (0, 0, 0, 0)); sh.putalpha(im.split()[3].point(lambda a: int(a * 0.55)))
    sh = ImageChops.offset(sh, 0, off).filter(ImageFilter.GaussianBlur(shadow))
    return Image.alpha_composite(sh, im)


def wave(y0, amp, freq, ph=0, step=6):
    return [(x, y0 + amp * math.sin(x / freq + ph)) for x in range(-PAD - 10, W + PAD + 10, step)]


def fill_wave(d, y0, amp, freq, ph, color):
    d.polygon(wave(y0, amp, freq, ph) + [(W + PAD + 10, H), (-PAD - 10, H)], fill=color)


def build():
    L = []  # (name, speed, image)
    def add(name, speed, fn, **k): L.append([name, speed, layer(fn, **k)])
    add("hill1", 0.3, lambda d: fill_wave(d, 900, 60, 90, 1, "#27506b"))
    add("hill2", 0.5, lambda d: fill_wave(d, 960, 50, 70, 3, "#1f4258"))

    def tower(d):
        d.ellipse((230, 975, 620, 1075), fill="#2f6a4a")
        cx, base = 420, 1010
        tiers = [(190, 100), (150, 90), (112, 80)]
        for i, (w_, h_) in enumerate(tiers):
            top = base - sum(h for _, h in tiers[:i + 1])
            d.rectangle((cx - w_ // 2, top, cx + w_ // 2, top + h_), fill=CREAM)
            d.rectangle((cx - w_ // 2 - 12, top - 14, cx + w_ // 2 + 12, top + 4), fill=RED)
            for k in (-1, 0, 1) if i == 0 else (-1, 1):
                x = cx + k * w_ // 3.2
                d.polygon([(x - 16, top + h_), (x - 16, top + h_ - 40), (x, top + h_ - 62), (x + 16, top + h_ - 40), (x + 16, top + h_)], fill=INK)
        d.polygon([(cx - 50, base - 270), (cx, base - 335), (cx + 50, base - 270)], fill=RED)
    add("tower", 0.7, tower, shadow=10, off=8)

    def willow(d):
        for sx, sgn in ((-30, 1), (W + 30, -1)):
            for b in range(5):
                x0 = sx + sgn * b * 44
                pts = [(x0 + sgn * (28 * math.sin(t / 3.3 + b)), t * 22 + 40 * b % 120) for t in range(0, 38 + b * 4)]
                d.line(pts, fill=GREEN, width=6)
                for px, py in pts[3::2]: d.ellipse((px - 7, py - 3, px + 7, py + 3), fill="#5aa469")
        d.rectangle((-PAD, 0, W + PAD, 38), fill=GREEN)
    add("willow", 1.2, willow, shadow=8, off=6)

    def turtle(d):
        cx, cy = 600, 1150
        d.ellipse((cx - 190, cy - 105, cx + 190, cy + 105), fill=GOLD, outline="#b9770e", width=8)
        for gx in range(-120, 130, 80):
            for gy in (-45, 20):
                d.regular_polygon((cx + gx + (40 if gy == 20 else 0), cy + gy, 36), 6, outline="#b9770e", width=6)
        d.ellipse((cx - 300, cy - 40, cx - 150, cy + 50), fill=GOLD, outline="#b9770e", width=8)
        d.ellipse((cx - 255, cy - 15, cx - 235, cy + 5), fill=INK)
    L.append(["turtle", 0.9, layer(turtle, shadow=12, off=10)])

    add("w0", 1.0, lambda d: fill_wave(d, 1245, 14, 48, 0.5, "#2a6f7f"))
    for i, (y, c) in enumerate(((1320, "#235e6e"), (1430, "#1b4d5e"), (1560, "#143c4c"))):
        def w_(d, y=y, c=c, i=i):
            fill_wave(d, y, 16, 44 + 6 * i, i, c)
            for x in range(-PAD, W + PAD, 160): d.arc((x - 40, y + 30, x + 40, y + 70), 200, 340, fill=CREAM, width=4)
        add(f"w{i + 1}", 1.4 + 0.5 * i, w_, shadow=10, off=8)
    return L


def static_bg():
    bg = Image.new("RGB", (W, H)); d = ImageDraw.Draw(bg)
    for y in range(H):
        t = y / H; d.line((0, y, W, y), fill=(int(20 + 10 * t), int(33 + 30 * t), int(61 + 25 * t)))
    bg = bg.convert("RGBA")
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(glow).ellipse((620, 560, 920, 860), fill=(244, 234, 210, 110))
    bg = Image.alpha_composite(bg, glow.filter(ImageFilter.GaussianBlur(60)))
    ImageDraw.Draw(bg).ellipse((650, 590, 890, 830), fill=CREAM)
    return bg.convert("RGB")


def sprite_glow(r=18):
    s = Image.new("RGBA", (r * 6, r * 6), (0, 0, 0, 0)); ImageDraw.Draw(s).ellipse((r * 2, r * 2, r * 4, r * 4), fill=(255, 230, 120, 255))
    return s.filter(ImageFilter.GaussianBlur(r / 2))


F = lambda s: ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", s)
_cap = {}


def caption_img(words, cur):
    key = (tuple(words), cur)
    if key in _cap: return _cap[key]
    im = Image.new("RGBA", (W, 260), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = F(100)
    tw = [d.textlength(w, font=f) for w in words]; x = W / 2 - (sum(tw) + 28 * (len(words) - 1)) / 2 - 10
    for i, (w, wd) in enumerate(zip(words, tw)):
        fill = "#FFE500" if i == cur else "white"
        for dx in range(-8, 9, 2):
            for dy in range(-8, 9, 2):
                if dx * dx + dy * dy <= 64: d.text((x + dx, 130 + dy), w, font=f, fill="black", anchor="lm")
        d.text((x, 130), w, font=f, fill=fill, anchor="lm"); x += wd + 28
    _cap[key] = im
    return im


def title_img():
    im = Image.new("RGBA", (W, 260), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = F(84)
    for j, t in enumerate(("VÌ SAO GỌI LÀ", "HỒ HOÀN KIẾM?")):
        for dx in range(-7, 8, 2):
            for dy in range(-7, 8, 2):
                if dx * dx + dy * dy <= 49: d.text((W / 2 + dx, 70 + j * 100 + dy), t, font=f, fill="black", anchor="mm")
        d.text((W / 2, 70 + j * 100), t, font=f, fill="#FFE500", anchor="mm")
    return im


def main(lines, out):
    audio, words, t0, starts = [], [], 0.0, []
    for text in lines:
        a = shorts.speak(text); d = len(a) / shorts.SR
        words += shorts.spread(text, t0, t0 + d); starts.append(t0)
        audio += [a, np.zeros(int(shorts.GAP * shorts.SR), np.float32)]; t0 += d + shorts.GAP
    total = t0 + 0.6
    voice = np.concatenate(audio)
    rise_t = starts[-1] + 0.3  # turtle rises when the last line starts
    L, bg, glow = build(), static_bg(), sprite_glow()
    fly = [(random.uniform(0, W), random.uniform(1000, 1500), random.uniform(0, 6.28), random.uniform(.5, 1.2)) for _ in range(16)]
    mist = Image.new("RGBA", (W + 600, 300), (0, 0, 0, 0)); ImageDraw.Draw(mist).ellipse((0, 40, W + 600, 260), fill=(255, 255, 255, 55))
    mist = mist.filter(ImageFilter.GaussianBlur(50))
    title = title_img()
    grain = Image.effect_noise((W, H), 28).convert("L"); grain = Image.merge("RGBA", (grain, grain, grain, Image.new("L", (W, H), 20)))
    import soundfile as sf, tempfile
    wav = os.path.join(tempfile.gettempdir(), "prev.wav"); sf.write(wav, shorts.mix(voice, [], total), shorts.SR)
    p = subprocess.Popen([shorts.FFMPEG, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-i", wav, "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", out],
                         stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    for fr in range(int(total * FPS)):
        t = fr / FPS; im = bg.copy().convert("RGBA")
        sway = math.sin(2 * math.pi * t / 7)
        for name, sp, img in L:
            dx, dy = -PAD + sp * 16 * sway, 0
            if name == "willow": dx += 10 * math.sin(2 * math.pi * t / 3)
            if name == "turtle":
                k = min(max((t - rise_t) / 1.6, 0), 1); k = 1 - (1 - k) ** 3
                dy = (1 - k) * 190 + 6 * math.sin(2 * math.pi * t / 2.4)
            if name == "w0":  # mist drifts between tower and water, fireflies above it
                im.alpha_composite(mist, (int(-300 + (t * 22) % 300), 880))
            im.paste(img, (int(dx), int(dy)), img)
        for x, y, ph, s in fly:
            a = 0.5 + 0.5 * math.sin(t * 2 * s + ph)
            g = glow.copy(); g.putalpha(g.split()[3].point(lambda v, a=a: int(v * a)))
            im.paste(g, (int((x + 40 * math.sin(t * .6 * s + ph)) % W) - 54, int(y + 30 * math.cos(t * .5 * s + ph)) - 54), g)
        im.alpha_composite(grain)
        im.alpha_composite(title, (0, 230))
        cur = next((i for i, w in enumerate(words) if w[0] <= t < w[1] + 0.05), None)
        if cur is not None:
            g0 = cur // 3 * 3; grp = words[g0:g0 + 3]
            im.alpha_composite(caption_img([w[2].upper() for w in grp], cur - g0), (0, 1270))
        ImageDraw.Draw(im).rectangle((0, 1884, int(W * t / total), 1900), fill="#FFE500")
        p.stdin.write(im.convert("RGB").tobytes())
    p.stdin.close(); p.wait()
    return out


if __name__ == "__main__":
    print(main(["Thắng giặc xong, một ngày ông chèo thuyền trên hồ.", "Bỗng một con rùa vàng nổi lên, đòi lại thanh gươm."], "out/preview_papercut.mp4"))
