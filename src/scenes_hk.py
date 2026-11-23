"""Scene registry for the Hoan Kiem script: reuse story3 scenes + 3 new ones (banners, fisher, banyan)."""
import math
from PIL import Image, ImageDraw, ImageFilter
import story2 as S, story3 as X
from story2 import layer, grad, fill_wave, W, H, PAD, WW, CREAM, RED, GOLD, INK, GREEN, EDGE


def banners():
    bg = grad((40, 20, 50), (214, 108, 70)).convert("RGBA"); ImageDraw.Draw(bg).ellipse((300 - 230, 1010 - 230, 300 + 230, 1010 + 230), fill=(255, 214, 130, 255))

    def flags(d):
        for x in (120, 360, 800, 980):
            d.line((x, 760, x, 1140), fill="#2a1020", width=8); d.polygon([(x, 770), (x + 135, 800), (x + 20, 818), (x + 140, 836), (x, 846)], fill=RED if x % 2 else GOLD)

    def hill(d): fill_wave(d, 1190, 40, 120, .5, "#2a1020"); X.person(d, 640, 1180, 2.0)
    return bg.convert("RGB"), [(0.3, S.mountain(1060, 50, 80, 2, "#4a1a2a", True), None), (0.6, layer(flags, 6, 4), lambda t: (6 * math.sin(t * 3), 0)), (1.0, layer(hill, 10, 8), None)]


def fisher():
    b = layer(lambda d: (X.boat(d, 300, 1150, 1.3), X.person(d, 285, 1156, 1.3)), 10, 8)
    bl = layer(lambda d: None); sw = S.sword_rgba(300).rotate(18, expand=True, resample=Image.BICUBIC); bl.alpha_composite(sw, (PAD + 640, 880))
    return X.night([(0.9, b, lambda t: (0, 8 * math.sin(t * 2.2))), (0, "glow", S.sword_glow(760, 1050, 190)), (0.9, bl, lambda t: (0, 330 * (1 - min(t / 1.6, 1) ** .6)))])


def banyan():
    bg = grad((22, 30, 52), (84, 74, 74)).convert("RGBA")

    def tree(d):
        d.polygon([(400, 1250), (440, 800), (500, 560), (560, 560), (620, 800), (660, 1250)], fill="#4a2e1c")
        for cx, cy, r in ((420, 520, 200), (700, 480, 190), (560, 380, 210), (300, 640, 150), (820, 640, 160), (540, 600, 190)): d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GREEN)
        for cx, cy, r in ((700, 430, 90), (380, 560, 80), (560, 330, 90)): d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="#4f9468")
        d.rectangle((592, 586, 612, 650), fill=GOLD); d.rectangle((574, 580, 630, 592), fill=GOLD)  # the hilt in the branches

    def ground(d): fill_wave(d, 1260, 24, 140, .3, "#243824"); X.person(d, 800, 1250, 1.7)
    return bg.convert("RGB"), [(0.8, layer(tree, 10, 8), None), (0, "glow", S.sword_glow(602, 620, 150)), (1.0, layer(ground, 10, 8), None)]


def army():
    """Rows of small figures with spears and flags on dusk hills (nghia quan)."""
    bg = grad((26, 22, 58), (200, 96, 84)).convert("RGBA"); ImageDraw.Draw(bg).ellipse((780 - 190, 930 - 190, 780 + 190, 930 + 190), fill=(255, 206, 130, 255))

    def row(base, s, n, col, gap):
        def f(d):
            fill_wave(d, base + 8, 14, 170, base / 300, col)
            for i in range(n):
                x = 80 + i * gap + (gap / 2 if base % 2 else 0); X.person(d, x, base, s)
                d.line((x + 60 * s, base - 30 * s, x + 60 * s, base - 330 * s), fill="#2a1020", width=max(int(7 * s), 3))
                d.polygon([(x + 60 * s, base - 330 * s), (x + 52 * s, base - 300 * s), (x + 68 * s, base - 300 * s)], fill="#dfe6ea")
        return f
    def flags(d):
        for x in (210, 560, 900):
            d.line((x, 700, x, 1080), fill="#2a1020", width=9); d.polygon([(x, 710), (x + 150, 740), (x + 20, 760), (x + 150, 780), (x, 790)], fill=RED if x != 560 else GOLD)
    return bg.convert("RGB"), [(0.3, S.mountain(1010, 50, 80, 2, "#4a1a2a", True), None), (0.5, layer(row(1130, .55, 8, "#34182c", 150), 8, 6), None), (0.6, layer(flags, 6, 4), lambda t: (8 * math.sin(t * 3), 0)),
                               (0.8, layer(row(1250, .85, 5, "#241222", 230), 10, 8), None), (1.0, layer(row(1400, 1.2, 4, "#160c18", 330), 12, 10), None)]


def _house(d, x, base, w, h, wall, roof):
    d.rectangle((x, base - h, x + w, base), fill=wall); d.polygon([(x - 14, base - h), (x + w + 14, base - h), (x + w - 14, base - h - 46), (x + 14, base - h - 46)], fill=roof); d.rectangle((x + w * .4, base - h * .55, x + w * .6, base), fill=INK)


def hanoi():
    """Old Hanoi morning: tiled houses along the bank, willow, Turtle Tower on the lake."""
    bg = grad((252, 206, 140), (120, 176, 196)).convert("RGBA"); ImageDraw.Draw(bg).ellipse((230 - 120, 640 - 120, 230 + 120, 640 + 120), fill=(255, 244, 214, 255))

    def houses(d):
        for i, (x, w, h, roof) in enumerate(((20, 130, 130, "#a8402e"), (690, 140, 150, "#8e2018"), (850, 170, 120, "#a8402e"))): _house(d, x, 1050, w, h, CREAM, roof)
    def willow(d):
        d.polygon([(800, 1130), (830, 800), (870, 800), (900, 1130)], fill="#4a2e1c"); d.ellipse((650, 600, 1050, 860), fill=GREEN)
        for i in range(22): x = 670 + i * 17; d.line([(x, 800), (x - 12 + (i % 3) * 8, 960), (x - 4, 1090 - (i % 4) * 30)], fill="#5aa87a", width=6)
    lake = layer(lambda d: [fill_wave(d, 1090 + dy, 12, 70 + 10 * i, i, c) for i, (dy, c) in enumerate(((0, "#3b8aa0"), (150, "#2c6f88"), (330, "#1f5670")))], 8, 6)
    return bg.convert("RGB"), [(0.3, layer(houses, 6, 4), None), (0.6, X.tower_layer(), None), (0.9, lake, None), (1.0, layer(willow, 10, 8), lambda t: (5 * math.sin(t * 1.2), 0))]


def underwater():
    bg = grad((18, 84, 108), (4, 22, 44)).convert("RGBA"); rays = Image.new("RGBA", (W, H), (0, 0, 0, 0)); rd = ImageDraw.Draw(rays)
    for x in (120, 380, 640, 900): rd.polygon([(x, 0), (x + 120, 0), (x + 330, H * .8), (x - 120, H * .8)], fill=(200, 240, 255, 34))
    bg = Image.alpha_composite(bg, rays.filter(ImageFilter.GaussianBlur(14)))
    weed = layer(lambda d: [d.polygon([(x - 14, 1920), (x + 8 * math.sin(i), 1500 - 60 * (i % 3)), (x + 14, 1920)], fill="#2f7a5a") for i, x in enumerate(range(40, 1100, 90))], 6, 4)
    bub = layer(lambda d: [d.ellipse((x - r, y - r, x + r, y + r), outline=(220, 245, 255, 200), width=4) for x, y, r in ((200, 1500, 20), (300, 1200, 12), (860, 1450, 24), (760, 1000, 14), (930, 700, 18), (130, 800, 16), (560, 1600, 14))], 2, 2)
    tur = layer(lambda d: X.turtle(d, 700, 1700, .9), 10, 8)
    bl = layer(lambda d: None); sw = S.sword_rgba(380).rotate(180, expand=True, resample=Image.BICUBIC); bl.alpha_composite(sw, (PAD + 480, 260))
    return bg.convert("RGB"), [(0.3, layer(lambda d: None), None), (0.6, tur, lambda t: (6 * math.sin(t), 0)), (0, "glow", S.sword_glow(540, 800, 260)), (0.9, bl, lambda t: (0, 40 + 420 * min(t / 4.0, 1))),
                               (0.8, weed, lambda t: (10 * math.sin(t * 1.4), 0)), (1.0, bub, lambda t: (0, -((t * 90) % 260)))]


def coloa():
    """Co Loa citadel: concentric earthen walls round a gate tower, moat ring, dusk sky."""
    bg = grad((38, 28, 78), (222, 132, 96)).convert("RGBA"); ImageDraw.Draw(bg).ellipse((540 - 150, 760 - 150, 540 + 150, 760 + 150), fill=(255, 226, 160, 255))

    def rings(d):
        for rx, col in ((540, "#2c7a8e"), (470, "#5a3c26"), (370, "#7a5330"), (270, "#95683a"), (170, "#b07f44")): d.ellipse((540 - rx, 1250 - rx * .3, 540 + rx, 1250 + rx * .3), fill=col, outline="#3a2414")
        d.ellipse((540 - 120, 1250 - 36, 540 + 120, 1250 + 36), fill=GREEN)
    def gate(d):
        d.rectangle((440, 1020, 640, 1250), fill=CREAM); d.polygon([(416, 1020), (664, 1020), (590, 940), (490, 940)], fill=RED); d.rectangle((470, 880, 610, 940), fill=CREAM); d.polygon([(450, 880), (630, 880), (540, 800), ], fill=RED)
        d.polygon([(500, 1250), (500, 1120), (540, 1090), (580, 1120), (580, 1250)], fill=INK)
        for x in (200, 880): d.line((x, 1180, x, 980), fill="#2a1020", width=8); d.polygon([(x, 990), (x + 90, 1010), (x, 1040)], fill=GOLD)
    return bg.convert("RGB"), [(0.3, S.mountain(1000, 40, 90, 1, "#3a2050", True), None), (0.8, layer(rings, 10, 8), None), (1.0, layer(gate, 10, 8), lambda t: (3 * math.sin(t), 0))]


def _foe(d, cx, base, s):
    p = lambda dx, dy: (cx + dx * s, base + dy * s)
    d.polygon([p(-55, 0), p(-32, -140), p(32, -140), p(55, 0)], fill="#2f4a78"); d.rectangle((*p(-40, -80), *p(40, -62)), fill="#9aa5b5")
    d.ellipse((*p(-30, -206), *p(30, -140)), fill="#e6d0a8"); d.polygon([p(-24, -160), p(24, -160), p(0, -136)], fill="#222"); d.ellipse((*p(-13, -190), *p(-5, -182)), fill="#222"); d.ellipse((*p(5, -190), *p(13, -182)), fill="#222")
    d.polygon([p(-40, -204), p(40, -204), p(0, -290)], fill="#3b3f48"); d.rectangle((*p(-44, -214), *p(44, -200)), fill="#6a707c")


def enemy():
    """Ming troops: blue robes, pointed helmets, dark flags on a blood-red dusk."""
    bg = grad((38, 14, 28), (150, 40, 44)).convert("RGBA"); ImageDraw.Draw(bg).ellipse((780 - 150, 930 - 150, 780 + 150, 930 + 150), fill=(232, 120, 90, 255))

    def row(base, s, n, col, gap):
        def f(d):
            fill_wave(d, base + 8, 12, 170, base / 300, col)
            for i in range(n): x = 90 + i * gap + (gap / 2 if base % 2 else 0); _foe(d, x, base, s); d.line((x - 62 * s, base - 20 * s, x - 62 * s, base - 320 * s), fill="#1a0c10", width=max(int(7 * s), 3))
        return f
    def flags(d):
        for x in (200, 560, 900): d.line((x, 690, x, 1080), fill="#1a0c10", width=9); d.polygon([(x, 700), (x + 160, 735), (x + 20, 765), (x + 160, 795), (x, 800)], fill="#262a36")
    return bg.convert("RGB"), [(0.3, S.mountain(1010, 50, 80, 2, "#2a0f18", True), None), (0.5, layer(row(1130, .55, 8, "#240c16", 150), 8, 6), None), (0.6, layer(flags, 6, 4), lambda t: (8 * math.sin(t * 3), 0)),
                               (0.8, layer(row(1250, .85, 5, "#1a0810", 230), 10, 8), None), (1.0, layer(row(1400, 1.2, 4, "#10050a", 330), 12, 10), None)]


def throne():
    bg = grad((92, 20, 34), (176, 70, 44)).convert("RGBA"); ImageDraw.Draw(bg).ellipse((540 - 330, 760 - 330, 540 + 330, 760 + 330), fill=(255, 206, 110, 255)); ImageDraw.Draw(bg).ellipse((540 - 250, 760 - 250, 540 + 250, 760 + 250), fill=(244, 170, 70, 255))

    def hall(d):
        for x in (60, 920): d.rectangle((x, 300, x + 100, 1500), fill=RED, outline=DRED if False else EDGE); d.rectangle((x - 20, 300, x + 120, 350), fill=GOLD); d.rectangle((x - 20, 1450, x + 120, 1500), fill=GOLD)
        d.polygon([(0, 300), (1080, 300), (1080, 220), (0, 220)], fill=GOLD)
    def dais(d):
        for i, (w, y) in enumerate(((640, 1150), (800, 1240), (960, 1330))): d.rectangle((540 - w / 2, y, 540 + w / 2, y + 90), fill=("#c8372d", "#a82a22", "#8a2018")[i], outline=EDGE)
        d.polygon([(380, 1150), (700, 1150), (660, 700), (420, 700)], fill=GOLD, outline=EDGE); d.ellipse((470, 740, 610, 880), fill=RED, outline=EDGE)
        X.person(d, 540, 1150, 2.4)
    def lamps(d):
        for x in (230, 540, 850):
            d.line((x, 220, x, 400), fill="#4a2410", width=5); d.ellipse((x - 46, 400, x + 46, 520), fill=RED, outline=EDGE); d.rectangle((x - 20, 396, x + 20, 410), fill=GOLD); d.line((x, 520, x, 600), fill=GOLD, width=6)
    return bg.convert("RGB"), [(0.4, layer(hall, 8, 6), None), (1.0, layer(dais, 12, 10), None), (0.8, layer(lamps, 6, 4), lambda t: (0, 8 * math.sin(t * 2)))]


def _rot(x, y, a): return x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a)


def _cloud(d, cx, cy, s, col):
    for dx, dy, r in ((-120, 10, 60), (-50, -30, 80), (40, -45, 90), (125, -5, 65), (190, 15, 45)): d.ellipse((cx + (dx - r) * s, cy + (dy - r) * s, cx + (dx + r) * s, cy + (dy + r) * s), fill=col)
    d.rectangle((cx - 190 * s, cy + 14 * s, cx + 230 * s, cy + 62 * s), fill=col)


def _dragon(d):
    """Paper-cut Long Quan: tapering gold body along an S-curve, red spikes, horned head with whiskers (head at the right)."""
    pts = []
    for i in range(61):
        s = i / 60; pts.append((70 + 690 * s, 640 + 130 * math.sin(s * 9.0) - 120 * s, 12 + 50 * min(s / 0.9, 1) ** .7))
    ang = lambda i: math.atan2(pts[min(i + 1, 60)][1] - pts[max(i - 1, 0)][1], pts[min(i + 1, 60)][0] - pts[max(i - 1, 0)][0])
    for i, (x, y, r) in enumerate(pts):  # outline pass, then fill pass, so the body reads as one shape
        d.ellipse((x - r - 6, y - r - 6, x + r + 6, y + r + 6), fill=EDGE)
    for i, (x, y, r) in enumerate(pts):
        d.ellipse((x - r, y - r, x + r, y + r), fill=GOLD)
    for i in range(4, 58, 3):  # belly scales + red spikes along the back
        x, y, r = pts[i]; a = ang(i); bx, by = _rot(0, r * .55, a); d.ellipse((x + bx - r * .5, y + by - r * .22, x + bx + r * .5, y + by + r * .22), fill="#ffe08a")
        sx, sy = _rot(0, -r, a); tx, ty = _rot(10, -r - 34 - r * .25, a); ux, uy = _rot(-10, -r, a); d.polygon([(x + ux, y + uy), (x + tx, y + ty), (x + sx + 20 * math.cos(a), y + sy + 20 * math.sin(a))], fill=RED)
    hx, hy, hr = pts[-1]; a = ang(60) + 0.1; P = lambda u, v: (hx + _rot(u, v, a)[0], hy + _rot(u, v, a)[1])
    d.polygon([P(-30, -hr * .9), P(120, -hr * .55), P(210, -hr * .2), P(215, hr * .25), P(120, hr * .6), P(-30, hr * 1.0)], fill=GOLD, outline=EDGE)  # head + snout
    d.polygon([P(120, hr * .5), P(215, hr * .3), P(180, hr * .95), P(60, hr * 1.1)], fill="#e0a128")  # jaw
    d.polygon([P(-10, -hr * .8), P(-120, -hr * 1.6), P(-60, -hr * .4)], fill=RED); d.polygon([P(20, -hr * .9), P(-50, -hr * 2.1), P(-10, -hr * .5)], fill=RED)  # mane
    d.line([P(50, -hr * .8), P(10, -hr * 2.0), P(60, -hr * 2.6)], fill=EDGE, width=11); d.line([P(90, -hr * .6), P(80, -hr * 1.6), P(130, -hr * 2.1)], fill=EDGE, width=9)  # horns
    ex, ey = P(112, -hr * .25); d.ellipse((ex - 18, ey - 18, ex + 18, ey + 18), fill="white"); d.ellipse((ex - 8, ey - 8, ex + 12, ey + 12), fill=INK)
    for k, dy in ((0, 0.1), (1, 0.45)): d.line([P(205, hr * dy), P(270, hr * (dy + .45)), P(340, hr * (dy + .15)), P(390, hr * (dy + .6))], fill="#fff0c0", width=6)  # whiskers
    nx, ny = P(204, hr * .02); d.ellipse((nx - 7, ny - 7, nx + 7, ny + 7), fill=INK)


def longquan():
    bg = grad((34, 20, 70), (176, 84, 96)).convert("RGBA"); gl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(gl).ellipse((140, 200, 940, 1000), fill=(255, 190, 110, 90)); bg = Image.alpha_composite(bg, gl.filter(ImageFilter.GaussianBlur(120)))
    far = layer(lambda d: [_cloud(d, x, y, s, "#8a5a8e") for x, y, s in ((200, 1250, 1.3), (760, 1420, 1.5), (540, 1050, 1.0))], 8, 6)
    dr = layer(_dragon, 12, 10)
    near = layer(lambda d: [_cloud(d, x, y, s, "#f4cfc0") for x, y, s in ((120, 1560, 1.6), (700, 1620, 1.8), (980, 1360, 1.0))], 10, 8)
    bl = layer(lambda d: None); sw = S.sword_rgba(380).rotate(180, expand=True, resample=Image.BICUBIC); bl.alpha_composite(sw, (PAD + 470, 760))
    return bg.convert("RGB"), [(0.3, far, lambda t: (22 * math.sin(t * .5), 0)), (0.7, dr, lambda t: (0, 14 * math.sin(t * 1.3))), (0, "glow", S.sword_glow(530, 1000, 230)),
                               (0.9, bl, lambda t: (0, -420 * (1 - min(t / 3.0, 1)) ** 2)), (1.0, near, lambda t: (-18 * math.sin(t * .4), 0))]


_X = None


def registry():
    global _X
    if _X is None: _X = X.build_scenes()
    mid = lambda i: _X[i]["mid"]
    import scenes_hk2
    return {**scenes_hk2.REG, "tower": mid(0), "victory": mid(1), "boat": mid(2), "turtle": mid(3), "sword": mid(4), "returned": mid(5), "dragon": mid(6), "banners": banners, "fisher": fisher, "banyan": banyan, "longquan": longquan, "army": army, "hanoi": hanoi, "underwater": underwater, "coloa": coloa, "enemy": enemy, "throne": throne, "ripple": mid(5)}
