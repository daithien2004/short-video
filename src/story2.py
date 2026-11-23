"""Polished paper-cut story: textured paper layers, bevel + light, better characters, paper clouds, slow push-in, caption groups break at punctuation."""
import math, random, subprocess, os, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops
import shorts, animate as A
from animate import D, wave, fill_wave, W, H, PAD, FPS

WW = W + 2 * PAD
INK, CREAM, RED, DRED, GOLD, EDGE, GREEN = "#14213d", "#f4ead2", "#c8372d", "#8e2018", "#f2b632", "#b9770e", "#3f7d58"
random.seed(7)
_FIB = None
CACHE = {}


def finish(im):
    """Paper feel: vertical light falloff, fibre noise, thin light edge on top-left borders."""
    global _FIB
    if _FIB is None: _FIB = (1 + np.random.default_rng(1).normal(0, 0.035, (H, WW))).astype(np.float32)
    a = np.asarray(im).astype(np.float32); lit = np.linspace(1.12, 0.86, H, dtype=np.float32)[:, None]
    a[..., :3] *= (lit * _FIB)[..., None]
    out = Image.fromarray(a.clip(0, 255).astype(np.uint8), "RGBA"); al = out.split()[3]
    hl = ImageChops.subtract(al, ImageChops.offset(al, 3, 3)).point(lambda v: int(v * 0.5))
    white = Image.new("RGBA", out.size, (255, 255, 255, 0)); white.putalpha(hl)
    return Image.alpha_composite(out, white)


def layer(fn, shadow=14, off=10):
    im = Image.new("RGBA", (WW, H), (0, 0, 0, 0)); fn(D(ImageDraw.Draw(im))); im = finish(im)
    sh = Image.new("RGBA", (WW, H), (0, 0, 0, 0)); sh.putalpha(im.split()[3].point(lambda a: int(a * 0.55)))
    return Image.alpha_composite(ImageChops.offset(sh, 0, off).filter(ImageFilter.GaussianBlur(shadow)), im)


def cached(k, fn):
    if k not in CACHE: CACHE[k] = fn()
    return CACHE[k]


def grad(c0, c1):
    im = Image.new("RGB", (W, H)); d = ImageDraw.Draw(im)
    for y in range(H): t = y / H; d.line((0, y, W, y), fill=tuple(int(a + (b - a) * t) for a, b in zip(c0, c1)))
    return im


def lens(d, x, y, l, w, ang, col):
    ca, sa = math.cos(ang), math.sin(ang); pts = [(x, y), (x + ca * l / 2 - sa * w, y + sa * l / 2 + ca * w), (x + ca * l, y + sa * l), (x + ca * l / 2 + sa * w, y + sa * l / 2 - ca * w)]
    d.polygon(pts, fill=col)


# ---------- characters ----------
def figure(d, cx, base, s=1.0, robe=RED, dark=DRED):
    p = lambda dx, dy: (cx + dx * s, base + dy * s)
    d.polygon([p(-60, 0), p(-34, -150), p(34, -150), p(60, 0)], fill=robe); d.polygon([p(16, -150), p(34, -150), p(60, 0), p(28, 0)], fill=dark)
    d.polygon([p(-54, -122), p(-32, -148), p(-8, -66), p(-42, -58)], fill=robe); d.polygon([p(54, -122), p(32, -148), p(8, -66), p(42, -58)], fill=dark)
    d.polygon([p(-18, -150), p(18, -150), p(0, -104)], fill=CREAM)
    d.polygon([p(-42, -84), p(42, -84), p(44, -66), p(-44, -66)], fill=GOLD); d.ellipse((p(-8, -82)[0], p(-8, -82)[1], p(8, -68)[0], p(8, -68)[1]), fill=RED)
    d.polygon([p(-61, -9), p(61, -9), p(62, 0), p(-62, 0)], fill=GOLD)
    d.ellipse((*p(-30, -212), *p(30, -146)), fill="#f3dcb4")
    d.polygon([p(-20, -176), p(20, -176), p(12, -134), p(0, -122), p(-12, -134)], fill="#2b2420")  # beard
    d.ellipse((*p(-14, -196), *p(-6, -188)), fill="#2b2420"); d.ellipse((*p(6, -196), *p(14, -188)), fill="#2b2420")
    d.line([p(-18, -202), p(-4, -199)], fill="#2b2420", width=max(2, int(4 * s))); d.line([p(4, -199), p(18, -202)], fill="#2b2420", width=max(2, int(4 * s)))
    d.polygon([p(-44, -214), p(44, -214), p(36, -234), p(-36, -234)], fill="#1b1b22")
    d.polygon([p(-86, -224), p(-44, -222), p(-44, -214), p(-84, -214)], fill="#1b1b22"); d.polygon([p(86, -224), p(44, -222), p(44, -214), p(84, -214)], fill="#1b1b22")
    d.rectangle((*p(-16, -258), *p(16, -230)), fill="#1b1b22")


def sword_rgba(L=420):
    im = Image.new("RGBA", (120, L + 150), (0, 0, 0, 0)); d = ImageDraw.Draw(im); cx = 60
    d.polygon([(cx - 15, L + 20), (cx + 15, L + 20), (cx + 11, 44), (cx, 0), (cx - 11, 44)], fill="#eef3f6", outline="#8fa4b3")
    d.polygon([(cx, 4), (cx + 11, 44), (cx + 15, L + 20), (cx + 2, L + 20)], fill="#c5d3dc"); d.line((cx, 40, cx, L), fill="#aebfcb", width=3)
    d.rectangle((cx - 46, L + 20, cx + 46, L + 38), fill=GOLD, outline=EDGE); d.rectangle((cx - 8, L + 38, cx + 8, L + 104), fill=RED)
    for k in range(4): d.line((cx - 8, L + 48 + k * 14, cx + 8, L + 56 + k * 14), fill=DRED, width=3)
    d.ellipse((cx - 17, L + 100, cx + 17, L + 134), fill=GOLD, outline=EDGE); d.line((cx, L + 134, cx - 10, L + 150), fill=RED, width=5)
    return im


def turtle_shape(d, cx, cy):
    dome = [(cx + 210 * math.cos(math.radians(a)), cy - 125 * math.sin(math.radians(a))) for a in range(0, 181, 6)]
    d.polygon(dome, fill=GOLD, outline=EDGE); d.ellipse((cx - 220, cy - 20, cx + 220, cy + 30), fill="#d99a1c", outline=EDGE, width=6)
    for gx, gy, r in ((-110, -52, 40), (0, -72, 46), (110, -52, 40), (-60, -108, 30), (60, -108, 30)): d.regular_polygon((cx + gx, cy + gy, r), 6, fill="#ffcf55", outline=EDGE, width=5)
    d.polygon([(cx - 170, cy + 4), (cx - 262, cy + 72), (cx - 196, cy + 96), (cx - 120, cy + 34)], fill="#d99a1c", outline=EDGE); d.polygon([(cx + 170, cy + 4), (cx + 250, cy + 70), (cx + 190, cy + 92), (cx + 110, cy + 30)], fill="#d99a1c", outline=EDGE)
    d.polygon([(cx - 200, cy - 20), (cx - 250, cy - 70), (cx - 300, cy - 40), (cx - 230, cy + 14)], fill=GOLD, outline=EDGE)
    d.ellipse((cx - 350, cy - 90, cx - 220, cy + 6), fill=GOLD, outline=EDGE, width=6); d.ellipse((cx - 330, cy - 70, cx - 306, cy - 44), fill="white"); d.ellipse((cx - 324, cy - 64, cx - 310, cy - 48), fill="#1a1008")
    d.arc((cx - 340, cy - 50, cx - 270, cy - 8), 15, 120, fill=EDGE, width=4)


def boat(cx, cy):
    def f(d):
        d.polygon([(cx - 215, cy - 40), (cx - 120, cy + 62), (cx + 120, cy + 62), (cx + 215, cy - 40), (cx + 110, cy - 4), (cx - 110, cy - 4)], fill="#7a3b1d")
        d.polygon([(cx - 110, cy - 4), (cx + 110, cy - 4), (cx + 120, cy + 62), (cx - 120, cy + 62)], fill="#8e4a26"); d.rectangle((cx - 150, cy + 6, cx + 150, cy + 20), fill=CREAM)
        for k in range(-3, 4): d.line((cx + k * 40, cy + 22, cx + k * 36, cy + 58), fill="#5e2d14", width=4)
        d.line((cx + 150, cy - 130, cx + 150, cy - 10), fill="#4a2410", width=8); d.ellipse((cx + 126, cy - 190, cx + 176, cy - 130), fill=GOLD, outline=EDGE, width=4); d.rectangle((cx + 138, cy - 196, cx + 164, cy - 186), fill=RED)
        figure(d, cx - 10, cy + 2, 1.05); d.line((cx + 50, cy - 70, cx + 200, cy + 80), fill="#4a2410", width=10); d.polygon([(cx + 190, cy + 70), (cx + 226, cy + 74), (cx + 206, cy + 100)], fill="#4a2410")
    return layer(f, shadow=10, off=8)


def turtle_layer(cx, with_sword=False):
    def f(d): turtle_shape(d, cx, 1150)
    im = layer(f, shadow=12, off=10)
    if with_sword: im.alpha_composite(sword_rgba(300).rotate(90, expand=True), (cx - 640 + PAD, 1150 - 30))
    return im


# ---------- environment ----------
def mountain(y, amp, freq, ph, col, pines=False):
    def f(d):
        d.polygon(wave(y, amp, freq, ph) + [(W + PAD + 10, H), (-PAD - 10, H)], fill=col)
        if pines:
            for x in range(-PAD, W + PAD, 64):
                yy = y + amp * math.sin(x / freq + ph); h = random.randint(50, 90)
                for k in range(3): d.polygon([(x - 22 + k * 3, yy - k * h * .28), (x, yy - h * (0.5 + k * .28)), (x + 22 - k * 3, yy - k * h * .28)], fill=col)
    return layer(f, shadow=8, off=6)


def clouds(y, col, n=4):
    def f(d):
        for i in range(n):
            x = -PAD + i * (WW / n) + random.randint(-30, 30); yy = y + random.randint(-30, 30)
            for dx, dy, r in ((0, 0, 70), (70, 14, 90), (160, 0, 70), (90, -30, 60)): d.ellipse((x + dx - r, yy + dy - r * .5, x + dx + r, yy + dy + r * .5), fill=col)
    return layer(f, shadow=6, off=5)


def waters(y0):
    L = [(1.0, layer(lambda d: fill_wave(d, y0, 14, 48, 0.5, "#2a6f7f")), None)]
    for i, (dy, c) in enumerate(((75, "#235e6e"), (185, "#1b4d5e"), (315, "#143c4c"))):
        def w_(d, y=y0 + dy, c=c, i=i):
            fill_wave(d, y, 16, 44 + 6 * i, i, c)
            for x in range(-PAD, W + PAD, 160): d.arc((x - 40, y + 30, x + 40, y + 70), 200, 340, fill=CREAM, width=4)
        L.append((1.4 + 0.5 * i, layer(w_, shadow=10, off=8), None))
    return L


def tower():
    def f(d):
        d.ellipse((215, 975, 635, 1085), fill="#2f6a4a")
        for x in range(240, 620, 26): d.polygon([(x, 1005), (x + 8, 985), (x + 16, 1005)], fill="#4b9a6a")
        d.rectangle((310, 996, 540, 1016), fill="#d8ccb0")
        cx = 425; tiers = [(190, 96), (150, 86), (112, 76)]
        for i, (w_, h_) in enumerate(tiers):
            top = 1000 - sum(h for _, h in tiers[:i + 1]); d.rectangle((cx - w_ // 2, top, cx + w_ // 2, top + h_), fill=CREAM)
            d.polygon([(cx - w_ // 2 - 22, top + 6), (cx - w_ // 2 - 4, top - 16), (cx + w_ // 2 + 4, top - 16), (cx + w_ // 2 + 22, top + 6)], fill=RED)
            d.line((cx - w_ // 2 - 20, top + 6, cx + w_ // 2 + 20, top + 6), fill=GOLD, width=5)
            for k in ((-1, 0, 1) if i == 0 else (-1, 1)):
                x = cx + k * w_ // 3.2; d.polygon([(x - 16, top + h_), (x - 16, top + h_ - 40), (x, top + h_ - 62), (x + 16, top + h_ - 40), (x + 16, top + h_)], fill=INK)
        d.polygon([(cx - 36, 1000 - 262 - 16), (cx, 1000 - 262 - 70), (cx + 36, 1000 - 262 - 16)], fill=RED); d.line((cx, 1000 - 262 - 70, cx, 1000 - 262 - 100), fill=GOLD, width=5)
    return layer(f, shadow=10, off=8)


def willow():
    def f(d):
        for sx, sg in ((-20, 1), (W + 20, -1)):
            d.line([(sx + sg * k * 22, 28 + 16 * math.sin(k / 2)) for k in range(14)], fill="#4a3422", width=26)
            for b in range(10):
                x0 = sx + sg * (30 + b * 28); sh = ("#4f9a5f", "#3f7d58", "#66b07a")[b % 3]
                pts = [(x0 + sg * 16 * math.sin(t / 4 + b), 40 + t * 20) for t in range(0, 24 + (b % 4) * 9)]
                d.line(pts, fill=sh, width=4)
                for px, py in pts[2::2]: lens(d, px, py, 30, 6, math.pi / 2 + sg * 0.3, sh)
    return layer(f, shadow=8, off=6)


def night_base():
    def mk():
        bg = grad((18, 30, 58), (32, 66, 90)).convert("RGBA"); d = ImageDraw.Draw(bg)
        for _ in range(40): x, y = random.randint(0, W), random.randint(60, 700); r = random.randint(2, 5); d.polygon([(x, y - r * 2), (x + r, y), (x, y + r * 2), (x - r, y)], fill=(244, 234, 210, 220))
        gl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(gl).ellipse((600, 540, 940, 880), fill=(244, 234, 210, 110)); bg = Image.alpha_composite(bg, gl.filter(ImageFilter.GaussianBlur(60)))
        d = ImageDraw.Draw(bg); d.ellipse((650, 590, 890, 830), fill=CREAM)
        for cx_, cy_, r in ((720, 650, 22), (820, 720, 30), (770, 780, 16), (690, 740, 14)): d.ellipse((cx_ - r, cy_ - r, cx_ + r, cy_ + r), fill=(226, 214, 186, 255))
        return bg.convert("RGB"), {"cl1": (0.2, clouds(430, "#2e4a74")), "cl2": (0.35, clouds(560, "#37567f", 3)), "h1": (0.3, mountain(900, 60, 90, 1, "#27506b")),
                                   "h2": (0.5, mountain(960, 50, 70, 3, "#1f4258", True)), "tower": (0.7, tower()), "willow": (1.2, willow())}
    return cached("night", mk)


def night(mid, with_tower=True, with_willow=True):
    bg, L = night_base()
    ls = [(*L["cl1"], None), (*L["cl2"], None), (*L["h1"], None), (*L["h2"], None)] + ([(*L["tower"], None)] if with_tower else []) + [(0, "mist", None)] + list(mid)
    return bg, ls + ([(*L["willow"], None)] if with_willow else []) + waters(1245)


def spiral_img():
    im = Image.new("RGBA", (1000, 1000), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.line([(500 + (30 + 22 * a) * math.cos(a), 500 + (30 + 22 * a) * math.sin(a)) for a in np.arange(0, 21, 0.05)], fill=(242, 182, 50, 255), width=26, joint="curve")
    return im


def rays_img():
    im = Image.new("RGBA", (1900, 1900), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for i in range(14):
        a0 = math.radians(i * 360 / 14); a1 = a0 + math.radians(9)
        d.polygon([(950, 950), (950 + 950 * math.cos(a0), 950 + 950 * math.sin(a0)), (950 + 950 * math.cos(a1), 950 + 950 * math.sin(a1))], fill=(255, 220, 110, 60))
    return im


def sword_glow(cx, cy, r=260):
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 215, 90, 120)); return g.filter(ImageFilter.GaussianBlur(70))


def build_scenes():
    S = [dict(mid=lambda: night([]))]
    def B():
        bg = grad((52, 14, 36), (230, 132, 64)).convert("RGBA"); d = ImageDraw.Draw(bg)
        for r, c in ((300, (240, 150, 70, 90)), (240, (246, 176, 96, 140)), (190, (252, 205, 120, 220)), (140, (255, 226, 150, 255))): d.ellipse((300 - r, 1010 - r, 300 + r, 1010 + r), fill=c)
        far = mountain(1060, 50, 80, 2, "#4a1a2a", True)
        def banners(d):
            for x in (120, 330, 830, 980):
                d.line((x, 760, x, 1130), fill="#2a1020", width=8); d.polygon([(x, 770), (x + 135, 800), (x + 20, 818), (x + 140, 836), (x, 846)], fill=RED if x % 2 else GOLD)
            for x in range(60, 1020, 36):
                if 540 < x < 900: continue
                d.rectangle((x - 5, 1050, x + 5, 1110), fill="#2a1020"); d.ellipse((x - 9, 1030, x + 9, 1052), fill="#2a1020"); d.line((x + 12, 1000, x + 12, 1160), fill="#2a1020", width=4); d.polygon([(x + 6, 1000), (x + 12, 978), (x + 18, 1000)], fill="#2a1020")
        def hill(d):
            fill_wave(d, 1190, 40, 120, .5, "#2a1020"); figure(d, 700, 1175, 1.75)
            d.polygon([(700 + 40, 1175 - 255), (700 + 118, 1175 - 360), (700 + 140, 1175 - 340), (700 + 66, 1175 - 235)], fill=RED)  # raised sleeve
            d.ellipse((700 + 110, 1175 - 380, 700 + 150, 1175 - 340), fill="#f3dcb4")
        sw = sword_rgba(380).rotate(-14, expand=True, resample=Image.BICUBIC)
        return bg.convert("RGB"), [(0.2, clouds(500, "#c4603a"), None), (0.3, far, None), (0.6, layer(banners, 6, 4), lambda t: (6 * math.sin(t * 3), 0)), (1.0, layer(hill, 10, 8), None),
                                   (0, "sword", sw), (1.6, layer(lambda d: fill_wave(d, 1500, 50, 90, 1, "#1b0b16"), 8, 6), None)]
    S.append(dict(mid=B))
    S.append(dict(mid=lambda: night([(0.9, boat(540, 1190), lambda t: (0, 8 * math.sin(t * 2.2)))])))
    S.append(dict(mid=lambda: night([(0.9, boat(330, 1190), lambda t: (0, 8 * math.sin(t * 2.2))), (0.9, turtle_layer(760), lambda t: (0, max(0, 190 - 190 * min(t / 1.3, 1) ** 0.5) + 6 * math.sin(t * 2.6)))], False)))
    def E(): return grad((14, 20, 44), (40, 30, 70)), [(0, "rays", rays_img()), (0, "glow", sword_glow(540, 900)), (0, "swordc", sword_rgba(460)), (0, "sparkle", None)]
    S.append(dict(mid=E))
    S.append(dict(mid=lambda: night([(0.9, turtle_layer(600, True), lambda t: (0, 8 * math.sin(t * 2) + max(0, t - 1.0) * 130))]), ripple=True))
    def Hs(): return grad((12, 24, 48), (24, 52, 74)), [(0, "glow", sword_glow(540, 900, 300)), (0, "spiral", spiral_img())]
    S.append(dict(mid=Hs))
    S.append(dict(mid=lambda: night([])))
    return S


def frame(sc, t, dur, glow, mist):
    bg, layers = sc["data"]; im = bg.copy().convert("RGBA"); sway = math.sin(2 * math.pi * t / 7)
    for item in layers:
        sp, img, mo = item[0], item[1], (item[2] if len(item) > 2 else None)
        if isinstance(img, str):
            if img == "mist": im.alpha_composite(mist, (int(-300 + (t * 22) % 300), 880))
            elif img == "rays": rot = mo.rotate(t * 9, resample=Image.BILINEAR); im.paste(rot, (540 - 950, 900 - 950), rot)
            elif img == "glow": im.alpha_composite(mo)
            elif img == "spiral": rot = mo.rotate(-t * 7, resample=Image.BILINEAR); im.paste(rot, (40, 400), rot)
            elif img == "swordc": im.paste(mo, (540 - 60, int(900 - 240 + 14 * math.sin(t * 2))), mo)
            elif img == "sword": im.paste(mo, (int(560 + 8 * math.sin(t * 2)), 600), mo)
            elif img == "sparkle":
                d = ImageDraw.Draw(im)
                for k in range(12):
                    a = k * 0.52 + t * 0.3; r = 150 + 90 * ((k * 37) % 5) / 4; x, y = 540 + r * math.cos(a), 880 + r * 1.1 * math.sin(a); s = 8 + 10 * abs(math.sin(t * 3 + k))
                    d.polygon([(x, y - s * 2), (x + s * .6, y), (x, y + s * 2), (x - s * .6, y)], fill=(255, 245, 200, 230)); d.polygon([(x - s * 2, y), (x, y + s * .6), (x + s * 2, y), (x, y - s * .6)], fill=(255, 245, 200, 230))
            continue
        dx, dy = -PAD + sp * 16 * sway, 0
        if mo: mx, my = mo(t); dx += mx; dy += my
        im.paste(img, (int(dx), int(dy)), img)
    if "fly" in sc:
        for x, y, ph, s in sc["fly"]:
            a = 0.5 + 0.5 * math.sin(t * 2 * s + ph); g = glow.copy(); g.putalpha(g.split()[3].point(lambda v, a=a: int(v * a)))
            im.paste(g, (int((x + 40 * math.sin(t * .6 * s + ph)) % W) - 54, int(y + 30 * math.cos(t * .5 * s + ph)) - 54), g)
    if sc.get("ripple") and t > 1.0:
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
        for k in range(3):
            u = ((t - 1.0) * 0.8 + k / 3) % 1; r = 60 + 240 * u; od.ellipse((420 - r, 1250 - r * 0.25, 420 + r, 1250 + r * 0.25), outline=(244, 234, 210, int(200 * (1 - u))), width=5)
        im.alpha_composite(ov)
    z = 1 + 0.05 * min(t / max(dur, 0.1), 1)  # slow push-in
    zw, zh = int(W * z), int(H * z); big = im.convert("RGB").resize((zw, zh), Image.BILINEAR)
    return big.crop(((zw - W) // 2, (zh - H) // 2, (zw - W) // 2 + W, (zh - H) // 2 + H)).convert("RGBA")


def prepare():
    scenes = build_scenes()
    for sc in scenes:
        sc["data"] = sc["mid"](); sc["fly"] = [(random.uniform(0, W), random.uniform(1000, 1500), random.uniform(0, 6.28), random.uniform(.5, 1.2)) for _ in range(16)]
    mist = Image.new("RGBA", (W + 600, 300), (0, 0, 0, 0)); ImageDraw.Draw(mist).ellipse((0, 40, W + 600, 260), fill=(255, 255, 255, 55))
    return scenes, A.sprite_glow(), mist.filter(ImageFilter.GaussianBlur(50))


def stills(out):
    scenes, glow, mist = prepare(); cells = []
    for sc in scenes: cells.append(frame(sc, 1.6, 4, glow, mist).convert("RGB").resize((270, 480)))
    s = Image.new("RGB", (270 * 4, 480 * 2), "#111")
    for i, c in enumerate(cells): s.paste(c, ((i % 4) * 270, (i // 4) * 480))
    s.save(out)


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
    scenes, glow, mist = prepare(); title = A.title_img()
    g = Image.effect_noise((W, H), 28).convert("L"); grain = Image.merge("RGBA", (g, g, g, Image.new("L", (W, H), 20)))
    import soundfile as sf
    wav = os.path.join(tempfile.gettempdir(), "story2.wav"); sf.write(wav, shorts.mix(np.concatenate(audio), [r[0] for r in ranges[1:]], total), shorts.SR)
    p = subprocess.Popen([shorts.FFMPEG, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", wav, "-c:v", "libx264", "-preset", "veryfast",
                          "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", out], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    prev = None
    for fr in range(int(total * FPS)):
        t = fr / FPS; k = next((i for i, (a, b) in enumerate(ranges) if a <= t < b), len(ranges) - 1); lt = t - ranges[k][0]; dur = ranges[k][1] - ranges[k][0]
        im = frame(scenes[k], lt, dur, glow, mist)
        if lt < 0.25 and k > 0:
            if prev is None or prev[0] != k: pd = ranges[k - 1][1] - ranges[k - 1][0]; prev = (k, frame(scenes[k - 1], pd, pd, glow, mist))
            im = Image.blend(prev[1], im, lt / 0.25)
        im.alpha_composite(grain); im.alpha_composite(title, (0, 230))
        ci = next((i for i, w in enumerate(words) if w[0] <= t < w[1] + 0.05), None)
        if ci is not None:
            idx = groups[gid[ci]]; im.alpha_composite(A.caption_img([words[i][2].upper() for i in idx], idx.index(ci)), (0, 1270))
        ImageDraw.Draw(im).rectangle((0, 1884, int(W * t / total), 1900), fill="#FFE500")
        p.stdin.write(im.convert("RGB").tobytes())
    p.stdin.close(); p.wait()
    return out, total


BEATS = [
    "Hà Nội có một cái hồ, tên nghĩa là trả gươm. Trả cho ai?",
    "Truyền thuyết kể rằng, Lê Lợi có một thanh gươm thần, và dùng nó đánh đuổi quân Minh.",
    "Thắng giặc xong, một đêm trăng, ông chèo thuyền trên hồ.",
    "Bỗng mặt hồ nổi sóng. Một con rùa vàng ngoi lên, đòi lại thanh gươm.",
    "Lê Lợi hiểu ra: gươm chỉ mượn để cứu nước. Giặc đã hết, phải trả.",
    "Ông trao gươm. Rùa ngậm lấy, rồi lặn xuống đáy hồ.",
    "Người ta kể, rùa vàng ấy chính là thần Kim Quy, từng giúp An Dương Vương xây thành Cổ Loa.",
    "Từ đó, nơi này mang tên: trả gươm.",
]
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "still": stills("out/story2_stills.png"); print("ok")
    else: print(main(BEATS, "out/story2_papercut.mp4"))
