"""More Hoan Kiem scenes: every shot gets its own composition (characters/props are reused, whole scenes are not)."""
import math
from PIL import Image, ImageDraw, ImageFilter
import story2 as S, story3 as X
from story2 import layer, grad, fill_wave, W, H, PAD, WW, CREAM, RED, GOLD, INK, GREEN, EDGE
L = layer
TEAL = ["#3b8aa0", "#2c6f88", "#1f5670"]
sway = lambda a, f=1.2: (lambda t: (a * math.sin(t * f), 0))
bob = lambda a, f=1.6: (lambda t: (0, a * math.sin(t * f)))


def waves(y0, cols=TEAL, dy=(0, 150, 330), amp=12):
    return L(lambda d: [fill_wave(d, y0 + o, amp, 70 + 10 * i, i, c) for i, (o, c) in enumerate(zip(dy, cols))], 8, 6)


def stars(n, seed=3, ymax=900):
    import random; r = random.Random(seed); pts = [(r.uniform(0, W), r.uniform(60, ymax), r.uniform(2, 5)) for _ in range(n)]
    return L(lambda d: [d.ellipse((x - s, y - s, x + s, y + s), fill=(255, 250, 220, 230)) for x, y, s in pts], 0, 0)


def swordlake():
    bg = X._night_bg().convert("RGBA"); sw = L(lambda d: None); sw.alpha_composite(S.sword_rgba(420), (PAD + 480, 470))
    refl = L(lambda d: None); refl.alpha_composite(S.sword_rgba(420).transpose(Image.FLIP_TOP_BOTTOM), (PAD + 480, 1200)); refl.putalpha(refl.split()[3].point(lambda v: int(v * .35)))
    return bg.convert("RGB"), [(0.4, S.cached("hill3", X.hill_far), None), *X.lake_layers(), (0, "glow", S.sword_glow(540, 760, 250)), (0.9, sw, bob(14, 1.3)), (0.9, refl, bob(-8, 1.3))]


def weak():
    bg = grad((44, 42, 66), (120, 96, 104)).convert("RGBA")

    def fig(d):
        fill_wave(d, 1330, 14, 200, .4, "#2a2230")
        for x, b, s in ((250, 1340, 1.5), (560, 1380, 1.8), (850, 1340, 1.4)): X.person(d, x, b, s)
        d.line((560 + 90, 1380 - 20, 700, 640), fill="#2a1020", width=10); d.polygon([(700, 650), (800, 700), (730, 720), (790, 780), (700, 770)], fill="#7a2a2a")  # torn flag
    far = L(lambda d: fill_wave(d, 1100, 30, 220, 2, "#3a3144"), 6, 4)
    return bg.convert("RGB"), [(0.3, far, None), (1.0, L(fig, 10, 8), None)]


def camp():
    bg = grad((12, 16, 38), (42, 34, 62)).convert("RGBA")

    def tents(d):
        for x, b, w in ((180, 1170, 300), (880, 1170, 280)): d.polygon([(x - w / 2, b), (x, b - w * .75), (x + w / 2, b)], fill=CREAM, outline=EDGE); d.polygon([(x - 28, b), (x, b - w * .5), (x + 28, b)], fill=INK)
    def fire(d):
        d.line((420, 1330, 660, 1290), fill="#4a2410", width=22); d.line((430, 1290, 650, 1330), fill="#5a2c14", width=22)
        d.polygon([(470, 1300), (520, 1160), (545, 1230), (585, 1120), (620, 1230), (660, 1300)], fill=RED); d.polygon([(500, 1300), (540, 1210), (575, 1170), (610, 1300)], fill=GOLD)
    def men(d):
        fill_wave(d, 1360, 12, 220, .3, "#1a2a22"); X.person(d, 250, 1420, 1.9); X.person(d, 860, 1420, 1.9)
        d.line((860 - 70, 1300, 860 - 150, 1130), fill="#dfe6ea", width=12)  # the blade he shows
    return bg.convert("RGB"), [(0.3, stars(40), None), (0.6, L(tents, 8, 6), None), (0, "glow", S.sword_glow(540, 1250, 300)), (0.9, L(fire, 6, 4), lambda t: (0, 5 * math.sin(t * 9))), (1.0, L(men, 10, 8), None), (0, "sparkle", None)]


def netcatch():
    bg = grad((24, 96, 120), (6, 34, 58)).convert("RGBA")

    def net(d):
        for i in range(-3, 14): d.line((60 + i * 90, 380, 300 + i * 90, 1180), fill=(235, 225, 190, 230), width=5); d.line((900 - i * 90 + 150, 380, 660 - i * 90 + 150, 1180), fill=(235, 225, 190, 230), width=5)
        d.polygon([(40, 380), (1040, 380), (900, 1220), (180, 1220)], outline=CREAM)
        for x, y, c in ((300, 1000, "#e8a05a"), (700, 900, "#d9784a"), (520, 1100, "#f0c070"), (820, 1080, "#e8a05a")): d.ellipse((x - 44, y - 22, x + 44, y + 22), fill=c); d.polygon([(x + 40, y), (x + 80, y - 26), (x + 80, y + 26)], fill=c)
    bl = L(lambda d: None); bl.alpha_composite(S.sword_rgba(300).rotate(68, expand=True, resample=Image.BICUBIC), (PAD + 330, 650))
    man = L(lambda d: (d.polygon([(-100, 1920), (1180, 1920), (1180, 1700), (-100, 1700)], fill="#7a3b1d"), X.person(d, 250, 1700, 2.4)), 10, 8)
    return bg.convert("RGB"), [(0.4, L(net, 4, 3), sway(14, 1.0)), (0, "glow", S.sword_glow(560, 840, 230)), (0.8, bl, sway(10, 1.0)), (1.0, man, bob(6, 1.1))]


def join():
    bg = grad((20, 14, 52), (60, 36, 96)).convert("RGBA"); sw = S.sword_rgba(420); top, bot = sw.crop((0, 0, 120, 440)), sw.crop((0, 440, 120, 570))
    a = L(lambda d: None); a.alpha_composite(top, (PAD + 480, 460)); b = L(lambda d: None); b.alpha_composite(bot, (PAD + 480, 900))
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 900, 220)), (0.9, a, lambda t: (0, -420 * (1 - min(t / 2.2, 1)) ** 2)), (0.9, b, lambda t: (0, 420 * (1 - min(t / 2.2, 1)) ** 2)), (0, "sparkle", None)]


def lakeshore():
    bg = grad((54, 30, 74), (240, 156, 92)).convert("RGBA"); ImageDraw.Draw(bg).ellipse((540 - 200, 1010 - 200, 540 + 200, 1010 + 200), fill=(255, 226, 150, 255))
    col = L(lambda d: [d.rectangle((540 - w, 1080 + i * 40, 540 + w, 1100 + i * 40), fill=(255, 220, 140, 150)) for i, w in enumerate((150, 120, 100, 80, 60, 40))], 0, 0)
    shore = L(lambda d: (fill_wave(d, 1360, 20, 260, .6, "#2a1a30"), X.person(d, 300, 1420, 2.7)), 12, 10)
    sw = L(lambda d: None); sw.alpha_composite(S.sword_rgba(330).rotate(-8, expand=True, resample=Image.BICUBIC), (PAD + 400, 780))
    return bg.convert("RGB"), [(0.3, S.mountain(1060, 40, 100, 1, "#3a2040", False), None), (0.8, waves(1080, ["#d9885a", "#9a5a6a", "#523a66"]), None), (0.9, col, bob(3, 2)), (1.0, shore, None), (1.0, sw, bob(6, 1.2))]


def offer():
    bg = X._night_bg().convert("RGBA"); bl = L(lambda d: None); bl.alpha_composite(S.sword_rgba(300).rotate(-8, expand=True, resample=Image.BICUBIC), (PAD + 400, 520))
    boat = L(lambda d: (X.boat(d, 380, 1180, 1.7), X.person(d, 360, 1190, 2.1)), 10, 8)
    tur = L(lambda d: X.turtle(d, 900, 1270, .75), 10, 8)
    return bg.convert("RGB"), [(0.4, S.cached("hill3", X.hill_far), None), (0.6, tur, bob(8, 1.4)), (0, "glow", S.sword_glow(500, 700, 230)), (0.9, boat, bob(9, 1.8)), (0.9, bl, bob(9, 1.8)), *X.lake_layers()[1:]]


def dawnlake():
    bg = grad((255, 226, 176), (160, 208, 222)).convert("RGBA"); ImageDraw.Draw(bg).ellipse((340 - 200, 880 - 200, 340 + 200, 880 + 200), fill=(255, 246, 220, 255))

    def bridge(d):
        d.ellipse((120, 1080, 720, 1160), fill="#2f6a4a")
        d.polygon([(40, 1250), (200, 1130), (520, 1130), (680, 1250), (640, 1250), (500, 1160), (220, 1160), (80, 1250)], fill=RED)
        for x in range(90, 640, 55): d.line((x, 1250 - abs(x - 360) * .35, x, 1170 - abs(x - 360) * .32), fill="#8e2018", width=7)
        d.rectangle((700, 1000, 900, 1130), fill=CREAM); d.polygon([(670, 1000), (930, 1000), (860, 920), (740, 920)], fill=RED); d.rectangle((740, 1060, 860, 1130), fill=INK)
    return bg.convert("RGB"), [(0.3, S.mountain(1080, 30, 110, 2, "#9ec7b8", False), None), (0.7, L(bridge, 8, 6), None), (0.9, waves(1210, ["#7fc0d0", "#5aa6bd", "#3f87a3"]), None), (0, "glow", S.sword_glow(340, 900, 300))]


def kimquy():
    bg = grad((34, 18, 74), (124, 64, 150)).convert("RGBA")
    tur = L(lambda d: X.turtle(d, 620, 1180, 1.7), 14, 12)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(620, 1000, 340)), (0.8, tur, bob(10, 1.0)), (0.5, waves(1300, ["#4a3a8a", "#3a2c74", "#2a2060"]), None), (0, "sparkle", None)]


def winter():
    bg = grad((176, 190, 202), (118, 138, 154)).convert("RGBA"); ImageDraw.Draw(bg).ellipse((760 - 90, 560 - 90, 760 + 90, 560 + 90), fill=(238, 240, 236, 255))
    def tree(d):
        d.polygon([(190, 1230), (220, 780), (260, 780), (290, 1230)], fill="#4a4038")
        for i in range(30): x = 120 + i * 9 + (i % 5) * 14; d.line([(240, 800), (x, 960 + (i % 4) * 40), (x - 10, 1120 + (i % 6) * 30)], fill="#6a6258", width=4)
    return bg.convert("RGB"), [(0.3, S.mountain(1040, 20, 120, 4, "#a8b6c0", False), None), (0.9, waves(1150, ["#7e98aa", "#6a8498", "#587084"]), None), (1.0, L(tree, 8, 6), sway(5, .8))]


def oldturtle():
    bg = grad((70, 86, 84), (24, 40, 44)).convert("RGBA")

    def t(d):
        c, s = (640, 1130), 1.7; p = lambda dx, dy: (c[0] + dx * s, c[1] + dy * s)
        d.polygon([p(200 * math.cos(math.radians(a)), -130 * math.sin(math.radians(a))) for a in range(0, 181, 6)], fill="#68784a"); d.ellipse((*p(-215, -20), *p(215, 30)), fill="#4a5a38")
        for gx, gy in ((-110, -56), (0, -78), (110, -56)): d.regular_polygon((c[0] + gx * s, c[1] + gy * s, 40 * s), 6, fill="#56663c")
        for gx, gy, r in ((-60, -100, 16), (70, -108, 12), (130, -70, 14)): d.ellipse((c[0] + (gx - r) * s, c[1] + (gy - r) * s, c[0] + (gx + r) * s, c[1] + (gy + r) * s), fill="#7f9660")
        d.ellipse((*p(-340, -90), *p(-205, 10)), fill="#7f8c5a"); d.ellipse((*p(-318, -66), *p(-292, -40)), fill=INK); d.polygon([p(-170, 8), p(-250, 70), p(-190, 96), p(-110, 30)], fill="#4a5a38")
    return bg.convert("RGB"), [(0.4, waves(1320, ["#3a5058", "#2c4048", "#1e3038"]), None), (0.9, L(t, 12, 10), bob(10, 0.9)), (1.0, waves(1420, ["#486068", "#3a525a", "#2c424a"], dy=(0, 120, 260)), None)]


def crowd():
    bg = grad((196, 206, 214), (150, 170, 184)).convert("RGBA")
    cols = ["#c8372d", "#2f6a8a", "#f2b632", "#4a7a58", "#8a4a8a", "#e0e0e0", "#d98a3a"]

    def folks(d):
        d.rectangle((0, 1330, 1080, 1400), fill="#7a7468"); d.rectangle((0, 1400, 1080, 1920), fill="#8a8478")
        for i, x in enumerate(range(80, 1040, 125)):
            h = 250 + (i % 3) * 40; b = 1560 + (i % 2) * 40; c = cols[i % len(cols)]
            d.polygon([(x - 50, b), (x - 36, b - h + 70), (x + 36, b - h + 70), (x + 50, b)], fill=c); d.ellipse((x - 32, b - h, x + 32, b - h + 64), fill="#2b2420")
    tower = L(lambda d: None); tower.alpha_composite(X.tower_layer().point(lambda v: int(v * .75)), (0, 0))
    return bg.convert("RGB"), [(0.3, S.mountain(1010, 20, 120, 2, "#b6c4cc", False), None), (0.7, tower, None), (0.9, waves(1100, ["#8aa6b8", "#7490a4", "#607c90"], dy=(0, 90, 190)), None), (1.0, L(folks, 8, 6), sway(3, 1.0))]


def incense():
    bg = grad((70, 76, 96), (150, 130, 130)).convert("RGBA")

    def steps(d):
        for i, y in enumerate((1180, 1300, 1420, 1540)): d.rectangle((0, y, 1080, y + 120), fill=("#7a766e", "#6a665e", "#5a564e", "#4a463e")[i], outline="#3a362e")
    def offer_(d):
        for x in (260, 540, 820):
            d.rectangle((x - 22, 1360, x + 22, 1520), fill=CREAM, outline=EDGE)
        for cx, cy in ((180, 1560), (400, 1580), (680, 1580), (900, 1560)):
            for k in range(7): a = k * .9; d.ellipse((cx + 38 * math.cos(a) - 28, cy + 24 * math.sin(a) - 28, cx + 38 * math.cos(a) + 28, cy + 24 * math.sin(a) + 28), fill=("#f4f0e0" if k % 2 else "#f2b632"))
            d.ellipse((cx - 24, cy - 24, cx + 24, cy + 24), fill="#d98a3a")
    def flames(d):
        for x in (260, 540, 820): d.polygon([(x - 14, 1360), (x, 1296), (x + 14, 1360)], fill=GOLD); d.polygon([(x - 6, 1360), (x, 1330), (x + 6, 1360)], fill=RED)
    tower = L(lambda d: None); tower.alpha_composite(X.tower_layer().point(lambda v: int(v * .6)), (0, 0))
    return bg.convert("RGB"), [(0.3, S.mountain(1010, 20, 120, 5, "#8a8aa0", False), None), (0.6, tower, None), (0.8, waves(1100, ["#6a7a94", "#586880", "#46566e"], dy=(0, 60, 130)), None), (1.0, L(steps, 8, 6), None), (0, "glow", S.sword_glow(540, 1330, 330)), (1.0, L(offer_, 6, 4), None), (1.0, L(flames, 2, 2), lambda t: (0, 3 * math.sin(t * 8)))]


REG = dict(swordlake=swordlake, weak=weak, camp=camp, netcatch=netcatch, join=join, lakeshore=lakeshore, offer=offer, dawnlake=dawnlake, kimquy=kimquy, winter=winter, oldturtle=oldturtle, crowd=crowd, incense=incense)


def _peasant(d, cx, base, s, bent=1, col="#6b4a2e"):
    p = lambda dx, dy: (cx + dx * s, base + dy * s); ln = 34 * bent
    d.polygon([p(-40, 0), p(-24 + ln, -130), p(24 + ln, -130), p(40, 0)], fill=col); d.ellipse((*p(ln - 30, -196), *p(ln + 30, -136)), fill="#f0d4a8"); d.polygon([p(ln - 76, -154), p(ln + 76, -154), p(ln, -262)], fill="#d8b86a")
    if bent: d.line([p(ln - 120, -176), p(ln + 120, -140)], fill="#4a2e1c", width=max(int(8 * s), 3)); [d.ellipse((*p(x - 38, y - 18), *p(x + 38, y + 44)), fill="#a8793c") for x, y in ((ln - 120, -176), (ln + 120, -140))]
    else: d.line([p(30, -110), p(86, -190)], fill=col, width=max(int(14 * s), 4))


def _paddy(base, cols, n=4):
    return L(lambda d: [fill_wave(d, base + i * 70, 10, 120, i, c) for i, c in enumerate(cols[:n])], 6, 4)


def suffer():
    bg = grad((84, 84, 96), (156, 146, 134)).convert("RGBA")
    hut = L(lambda d: (d.rectangle((90, 1060, 330, 1200), fill="#6a4a2e"), d.polygon([(60, 1070), (360, 1070), (270, 930), (150, 930)], fill="#b08a48"), d.rectangle((190, 1110, 250, 1200), fill=INK)), 8, 6)
    ppl = L(lambda d: (fill_wave(d, 1330, 12, 240, .2, "#4a3a28"), [_peasant(d, x, b, sc_, 1) for x, b, sc_ in ((360, 1360, 1.5), (800, 1420, 1.7))]), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1040, 20, 110, 1, "#8c8a94", False), None), (0.6, hut, None), (0.7, _paddy(1150, ["#6f8a58", "#5c7a4a", "#4a6a3c", "#3a5a30"]), None), (1.0, ppl, sway(6, .9))]


def peace():
    bg = grad((255, 232, 176), (172, 214, 204)).convert("RGBA"); ImageDraw.Draw(bg).ellipse((780 - 130, 600 - 130, 780 + 130, 600 + 130), fill=(255, 248, 224, 255))
    hut = L(lambda d: (d.rectangle((90, 1060, 330, 1200), fill="#a8793c"), d.polygon([(60, 1070), (360, 1070), (270, 930), (150, 930)], fill="#d8b86a"), d.rectangle((190, 1110, 250, 1200), fill=INK)), 8, 6)
    ppl = L(lambda d: (fill_wave(d, 1360, 12, 240, .2, "#5a8a48"), [_peasant(d, x, b, sc_, 0, "#c8372d") for x, b, sc_ in ((380, 1400, 1.5), (780, 1440, 1.7))]), 10, 8)
    birds = L(lambda d: [d.line([(x - 40, y), (x, y - 22), (x + 40, y)], fill="#ffffff", width=6) for x, y in ((220, 560), (330, 500), (150, 460))], 0, 0)
    return bg.convert("RGB"), [(0.3, S.mountain(1040, 30, 120, 3, "#9cc8b4", False), None), (0.6, hut, None), (0.7, _paddy(1150, ["#9fd078", "#86bc62", "#6aa44e", "#549040"]), None), (0.4, birds, lambda t: (30 * math.sin(t * .5), 6 * math.sin(t * 2))), (1.0, ppl, sway(5, 1.1))]


def forest():
    bg = grad((8, 24, 30), (34, 64, 54)).convert("RGBA")

    def trees(d, xs, top, col, w):
        for x in xs: d.rectangle((x - w / 2, top, x + w / 2, 1500), fill=col); d.ellipse((x - 150, top - 160, x + 150, top + 110), fill=col)
    far = L(lambda d: trees(d, range(40, 1100, 180), 520, "#1c3e36", 40), 6, 4); mid = L(lambda d: trees(d, range(120, 1100, 260), 620, "#143028", 64), 8, 6)
    path = L(lambda d: (fill_wave(d, 1330, 14, 260, .5, "#1a2a20"), d.polygon([(380, 1920), (700, 1920), (620, 1330), (480, 1330)], fill="#6a5a3c"), X.person(d, 540, 1560, 1.5)), 10, 8)
    return bg.convert("RGB"), [(0.3, far, None), (0.6, mid, None), (1.0, path, bob(4, 2.4)), (0, "sparkle", None)]


def hilt():
    bg = grad((10, 28, 22), (30, 66, 48)).convert("RGBA"); sw = S.sword_rgba(420).crop((0, 400, 120, 570)); big = sw.resize((sw.width * 3, sw.height * 3), Image.LANCZOS)
    hl = L(lambda d: None); hl.alpha_composite(big, (PAD + 540 - big.width // 2, 700))
    leaves = L(lambda d: [d.ellipse((x - r, y - r * .6, x + r, y + r * .6), fill=c) for x, y, r, c in ((120, 560, 200, "#1e5a3c"), (940, 520, 220, "#256a46"), (180, 1200, 230, "#1a4e34"), (900, 1260, 240, "#256a46"), (540, 360, 260, "#1e5a3c"), (540, 1500, 280, "#164430"))], 8, 6)
    return bg.convert("RGB"), [(0.5, leaves, sway(10, .7)), (0, "glow", S.sword_glow(540, 900, 330)), (0.8, hl, bob(6, 1.4)), (0, "sparkle", None)]


def storm():
    bg = grad((38, 10, 24), (150, 40, 40)).convert("RGBA")
    boat = L(lambda d: (X.boat(d, 480, 1290, 1.6), X.person(d, 460, 1300, 2.0)), 10, 8); boat = boat.rotate(9, center=(480, 1300), resample=Image.BICUBIC)
    return bg.convert("RGB"), [(0.3, waves(1100, ["#7a2a3a", "#5a2030", "#401624"], amp=46), sway(12, 1.4)), (0.9, boat, lambda t: (0, 22 * math.sin(t * 3))), (1.0, waves(1380, ["#4a1a2a", "#36101e", "#240a14"], dy=(0, 140, 300), amp=60), sway(18, 1.8))]


def plea():
    bg = X._night_bg().convert("RGBA")

    def head(d):
        d.polygon([(640, 1500), (700, 1160), (900, 1140), (1000, 1500)], fill="#d99a1c"); d.ellipse((560, 960, 1000, 1250), fill=GOLD, outline=EDGE); d.ellipse((620, 1040, 700, 1120), fill="white"); d.ellipse((636, 1058, 676, 1098), fill=INK)
        d.polygon([(560, 1150), (700, 1190), (700, 1220), (570, 1200)], fill="#b57a10")
    ring = L(lambda d: [d.arc((480 - r, 1090 - r, 480 + r, 1090 + r), 150, 210, fill=(255, 232, 150, 220), width=8) for r in (60, 120, 180)], 0, 0)
    boat = L(lambda d: (X.boat(d, 230, 1330, 1.0), X.person(d, 215, 1340, 1.3)), 8, 6)
    return bg.convert("RGB"), [(0.4, S.cached("hill3", X.hill_far), None), (0.8, L(head, 10, 8), bob(8, 1.2)), (0.9, ring, lambda t: (-24 * (t % 1.2), 0)), (0.9, boat, bob(8, 1.7)), *X.lake_layers()[1:]]


def emblem():
    bg = grad((255, 226, 170), (150, 196, 214)).convert("RGBA"); ImageDraw.Draw(bg).ellipse((540 - 160, 760 - 160, 540 + 160, 760 + 160), fill=(255, 246, 220, 255))
    tur = L(lambda d: X.turtle(d, 600, 1230, 1.2), 12, 10); sw = L(lambda d: None); sw.alpha_composite(S.sword_rgba(380), (PAD + 540, 690))
    return bg.convert("RGB"), [(0.5, waves(1280, ["#7fc0d0", "#5aa6bd", "#3f87a3"], dy=(0, 120, 260)), None), (0.9, tur, bob(8, 1.1)), (0, "glow", S.sword_glow(600, 900, 240)), (0.9, sw, bob(8, 1.1)), (0, "sparkle", None)]


def scroll():
    bg = grad((52, 30, 64), (160, 98, 84)).convert("RGBA")

    def sc_(d):
        d.rectangle((150, 640, 930, 1260), fill="#efe0b4", outline=EDGE); [d.ellipse((x - 34, 610, x + 34, 1290), fill="#c89a4a", outline=EDGE) for x in (150, 930)]
        for y in range(700, 1240, 46): d.line((250, y, 830, y), fill="#b8a478", width=5)
        d.line([(300, 900), (400, 800), (520, 880), (640, 780), (760, 860)], fill="#8e2018", width=12)  # brush-drawn dragon line
        X.turtle(d, 540, 1160, .42)
    return bg.convert("RGB"), [(0.5, L(sc_, 12, 10), bob(10, 1.0)), (0, "sparkle", None)]


REG.update(suffer=suffer, peace=peace, forest=forest, hilt=hilt, storm=storm, plea=plea, emblem=emblem, scroll=scroll)
