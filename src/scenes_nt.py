"""Scenes for the Nỏ thần story (Cổ Loa, An Dương Vương, Mỵ Châu, Trọng Thủy). Every scene is its own composition; characters come from chars.py."""
import math
from PIL import Image, ImageDraw, ImageFilter
import story2 as S, story3 as X, chars as C
from story2 import layer, grad, fill_wave, W, H, PAD, CREAM, RED, GOLD, INK, GREEN, EDGE
from scenes_hk2 import L, waves, stars, sway, bob, _peasant

EARTH = "#6b4a2e"


def sky(c0, c1, sun=None):
    bg = grad(c0, c1).convert("RGBA")
    if sun: x, y, r, col = sun; ImageDraw.Draw(bg).ellipse((x - r, y - r, x + r, y + r), fill=col)
    return bg


def ground(y, col, amp=14): return L(lambda d: fill_wave(d, y, amp, 240, y / 300, col), 8, 6)


def wall(d, x0, x1, top, base, col, edge="#3a2a1c", step=70):
    d.rectangle((x0, top, x1, base), fill=col, outline=edge)
    for x in range(int(x0), int(x1 - step * .6), step): d.rectangle((x, top - 26, x + step * .6, top), fill=col, outline=edge)


def flame(d, x, y, s=1.0):
    d.polygon([(x - 40 * s, y), (x - 20 * s, y - 90 * s), (x - 4 * s, y - 50 * s), (x + 14 * s, y - 130 * s), (x + 30 * s, y - 60 * s), (x + 44 * s, y)], fill="#e8532a")
    d.polygon([(x - 22 * s, y), (x, y - 70 * s), (x + 10 * s, y - 38 * s), (x + 24 * s, y)], fill=GOLD)


def gate(d, cx, base, s=1.0, wall_col="#8a6a48"):
    d.rectangle((cx - 150 * s, base - 150 * s, cx + 150 * s, base), fill=wall_col, outline="#3a2a1c"); d.polygon([(cx - 80 * s, base), (cx - 80 * s, base - 90 * s), (cx, base - 125 * s), (cx + 80 * s, base - 90 * s), (cx + 80 * s, base)], fill=INK)
    d.rectangle((cx - 120 * s, base - 260 * s, cx + 120 * s, base - 150 * s), fill=CREAM, outline="#3a2a1c"); d.polygon([(cx - 150 * s, base - 260 * s), (cx + 150 * s, base - 260 * s), (cx + 90 * s, base - 340 * s), (cx - 90 * s, base - 340 * s)], fill=RED)


def coloa_night():
    bg = X._night_bg().convert("RGBA")
    far = L(lambda d: (wall(d, -20, 1100, 1010, 1130, "#5a4632"), [d.ellipse((x - 9, 980 - 9, x + 9, 980 + 9), fill=GOLD) for x in range(80, 1060, 160)]), 6, 4)
    near = L(lambda d: (wall(d, -20, 1100, 1150, 1290, "#7a5c3a"), gate(d, 540, 1290, 1.0), [C.soldier_au(d, x, 1150, .55) for x in (120, 300, 780, 960)]), 8, 6)
    return bg.convert("RGB"), [(0.3, S.cached("hill3", X.hill_far), None), (0.5, far, None), (0.8, near, None), (0.9, waves(1300, ["#2c6f88", "#1f5670", "#18445a"], dy=(0, 120, 260)), None)]


def crossbow_fire():
    bg = sky((60, 24, 46), (230, 110, 70), (780, 760, 150, (255, 206, 130, 255)))

    def arrows(d):
        for i, a in enumerate((-.5, -.36, -.22, -.08, .06, .2)):
            x0, y0 = 480, 1130; x1, y1 = x0 + 760 * math.cos(a - .35), y0 + 760 * math.sin(a - .35) - 120 * (i % 3)
            d.line([(x0, y0), (x1, y1)], fill="#efe6c8", width=7); d.polygon([(x1 + 22 * math.cos(a - .35), y1 + 22 * math.sin(a - .35)), (x1 - 8 * math.cos(a - .35) + 13 * math.sin(a - .35), y1 - 8 * math.sin(a - .35) - 13 * math.cos(a - .35)), (x1 - 8 * math.cos(a - .35) - 13 * math.sin(a - .35), y1 - 8 * math.sin(a - .35) + 13 * math.cos(a - .35))], fill=GOLD)
    wl = L(lambda d: (wall(d, -20, 1100, 1560, 1920, "#7a5c3a"), C.crossbow(d, 360, 1470, 1.6, arrow=False), C.king(d, 800, 1560, 2.2)), 10, 8)
    return bg.convert("RGB"), [(0.3, ground(1200, "#3a1a2a"), None), (0.7, L(arrows, 4, 3), None), (1.0, wl, None), (0, "glow", S.sword_glow(300, 1500, 220))]


def fall():
    bg = sky((24, 10, 20), (170, 50, 40))

    def burn(d):
        gate(d, 540, 1380, 1.6, "#5a3a28"); [flame(d, x, y, s) for x, y, s in ((300, 1200, 1.6), (800, 1250, 1.8), (540, 1040, 1.3), (180, 1380, 1.2), (930, 1380, 1.4))]
        d.line((650, 1050, 700, 760), fill="#2a1a14", width=10); d.polygon([(700, 765), (820, 800), (740, 840), (816, 880), (700, 870)], fill="#3a2a30")
    sm = L(lambda d: [d.ellipse((x - r, y - r, x + r, y + r), fill=(70, 60, 64, 200)) for x, y, r in ((460, 760, 90), (560, 620, 120), (680, 500, 150), (800, 380, 160))], 0, 0)
    foes = L(lambda d: (fill_wave(d, 1560, 14, 240, .7, "#1a0a10"), [C.soldier_bac(d, x, b, s_) for x, b, s_ in ((250, 1600, 1.5), (560, 1640, 1.8), (900, 1600, 1.4))]), 10, 8)
    return bg.convert("RGB"), [(0.6, L(burn, 8, 6), bob(3, 6)), (0.5, sm, lambda t: (0, -30 * (t % 3))), (0, "glow", S.sword_glow(540, 1200, 360)), (1.0, foes, None), (0, "sparkle", None)]


def king_build():
    bg = sky((150, 200, 230), (250, 236, 200), (240, 560, 110, (255, 248, 220, 255)))
    half = L(lambda d: (wall(d, -20, 560, 1180, 1330, "#9a7a52"), [d.rectangle((x, 1100, x + 130, 1180), fill="#b08a5a", outline="#3a2a1c") for x in (60, 250)]), 8, 6)
    ppl = L(lambda d: (fill_wave(d, 1480, 14, 240, .4, "#8a6a42"), C.king(d, 800, 1620, 2.4), [_peasant(d, x, 1660 + (i % 2) * 30, 1.3, 1) for i, x in enumerate((180, 430))]), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1090, 30, 110, 2, "#a4c8a8", False), None), (0.6, half, None), (1.0, ppl, sway(4, 1.1))]


def wall_collapse():
    bg = sky((84, 84, 98), (170, 160, 150))

    def bricks(d):
        for i, (x, y, a) in enumerate(((300, 1260, 0), (470, 1240, 8), (640, 1280, -10), (400, 1160, 20), (560, 1120, -15), (740, 1180, 30), (260, 1100, -25))):
            c, s_ = math.cos(math.radians(a)), math.sin(math.radians(a)); pts = [(x + dx * c - dy * s_, y + dx * s_ + dy * c) for dx, dy in ((-70, -32), (70, -32), (70, 32), (-70, 32))]; d.polygon(pts, fill="#b08a5a", outline="#3a2a1c")
    dust = L(lambda d: [d.ellipse((x - r, y - r, x + r, y + r), fill=(200, 190, 176, 150)) for x, y, r in ((300, 1280, 120), (560, 1160, 150), (780, 1240, 110))], 0, 0)
    pl = L(lambda d: (fill_wave(d, 1500, 14, 240, .5, "#5a4632"), C.king(d, 220, 1660, 2.2), [C.soldier_au(d, x, 1660, 1.5) for x in (880,)]), 10, 8)
    return bg.convert("RGB"), [(0.6, L(bricks, 8, 6), lambda t: (0, 6 * math.sin(t * 7))), (0.5, dust, lambda t: (0, -18 * (t % 2))), (1.0, pl, None)]


def kimquy_rise():
    bg = sky((40, 22, 80), (200, 150, 90))
    tur = L(lambda d: X.turtle(d, 800, 1260, 1.35), 14, 12); pl = L(lambda d: (fill_wave(d, 1400, 12, 240, .3, "#3a2a40"), C.king(d, 160, 1640, 2.0)), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(800, 1100, 380)), (0.8, tur, lambda t: (0, 240 * (1 - min(t / 1.4, 1)) ** 2)), (1.0, pl, None), (0, "sparkle", None)]


def claw():
    bg = sky((255, 214, 150), (240, 150, 120))
    tur = L(lambda d: (X.turtle(d, 470, 1320, 1.1), d.polygon([(640, 1290), (740, 1210), (800, 1230), (730, 1320)], fill="#d99a1c")), 12, 10)
    hands = L(lambda d: (fill_wave(d, 1480, 12, 240, .3, "#6a4a40"), C.king(d, 940, 1640, 2.3)), 10, 8)
    cl = L(lambda d: d.polygon([(780, 1170), (840, 1190), (850, 1260), (820, 1290), (790, 1230)], fill=GOLD, outline=EDGE), 6, 4)
    return bg.convert("RGB"), [(0.9, tur, bob(5, 1.2)), (0, "glow", S.sword_glow(815, 1230, 200)), (0.9, cl, bob(8, 2)), (1.0, hands, None), (0, "sparkle", None)]


def trigger():
    bg = grad((12, 34, 44), (30, 80, 90)).convert("RGBA")
    xb = L(lambda d: C.crossbow(d, 520, 1000, 3.0, arrow=False), 14, 12)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(500, 1130, 260)), (0.9, xb, bob(6, 1.3)), (0, "sparkle", None)]


def north():
    bg = sky((30, 14, 52), (120, 60, 110), (800, 700, 130, (210, 190, 240, 255)))
    mt = L(lambda d: fill_wave(d, 1100, 80, 300, 1.5, "#3a2458"), 6, 4)
    pl = L(lambda d: (fill_wave(d, 1500, 14, 240, .8, "#1c0e2c"), C.zhao(d, 540, 1640, 2.6), [C.soldier_bac(d, x, 1660, 1.5) for x in (150, 940)]), 10, 8)
    return bg.convert("RGB"), [(0.3, mt, None), (1.0, pl, None)]


def defeat():
    bg = sky((90, 40, 50), (200, 130, 100))
    run = L(lambda d: (fill_wave(d, 1400, 14, 240, .2, "#4a2a30"), [C.soldier_bac(d, x, b, s_) for x, b, s_ in ((200, 1560, 1.6), (480, 1620, 1.9), (780, 1570, 1.5))]), 10, 8)
    ar = L(lambda d: [(d.line([(x, y), (x - 110, y - 40)], fill="#efe6c8", width=6), d.polygon([(x, y), (x - 24, y - 16), (x - 20, y + 4)], fill=GOLD)) for x, y in ((900, 520), (720, 430), (980, 700), (620, 640))], 2, 2)
    return bg.convert("RGB"), [(0.3, S.mountain(1150, 30, 110, 3, "#6a3a40", False), None), (0.9, ar, lambda t: (-80 * (t % 1.5), 28 * (t % 1.5))), (1.0, run, bob(6, 5))]


def scheme():
    bg = grad((18, 10, 30), (60, 34, 70)).convert("RGBA")
    pl = L(lambda d: (d.rectangle((0, 1500, 1080, 1920), fill="#2a1a2a"), C.zhao(d, 340, 1640, 2.4), C.prince(d, 780, 1640, 2.4), d.rectangle((420, 1380, 700, 1420), fill="#6a4a2a"), d.rectangle((470, 1340, 650, 1380), fill=CREAM, outline=EDGE)), 10, 8)
    can = L(lambda d: (d.rectangle((530, 1300, 560, 1340), fill=CREAM), flame(d, 545, 1300, .5)), 4, 3)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(545, 1250, 380)), (1.0, pl, None), (1.0, can, bob(3, 9))]


def prince_arrive():
    bg = sky((150, 200, 230), (250, 236, 200), (900, 420, 100, (255, 248, 220, 255)))
    far = L(lambda d: (wall(d, 560, 1100, 1180, 1320, "#9a7a52"), gate(d, 800, 1320, .8)), 6, 4)
    rd = L(lambda d: (fill_wave(d, 1500, 14, 240, .6, "#8a6a42"), C.horse(d, 400, 1700, 1.3, "#e6dcc8"), C.prince(d, 410, 1530, 1.6), C.soldier_bac(d, 120, 1660, 1.2)), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1120, 30, 120, 2, "#a4c8a8", False), None), (0.6, far, None), (1.0, rd, bob(5, 3))]


def wedding():
    bg = grad((120, 24, 36), (200, 70, 50)).convert("RGBA")

    def hall(d):
        for x in (70, 1010): d.rectangle((x - 50, 200, x + 50, 1500), fill=RED, outline=EDGE)
        d.rectangle((0, 200, 1080, 280), fill=GOLD); d.rectangle((0, 1500, 1080, 1920), fill="#7a2a20")
        for x in (250, 540, 830): d.line((x, 280, x, 420), fill="#4a2410", width=5); d.ellipse((x - 50, 420, x + 50, 550), fill=RED, outline=EDGE)
    pl = L(lambda d: (C.princess(d, 380, 1640, 2.6), C.prince(d, 720, 1640, 2.6)), 10, 8)
    return bg.convert("RGB"), [(0.5, L(hall, 8, 6), None), (0, "glow", S.sword_glow(540, 800, 400)), (1.0, pl, bob(3, 1.5)), (0, "sparkle", None)]


def couple():
    bg = X._night_bg().convert("RGBA")
    pond = L(lambda d: [(d.ellipse((x - 90, y - 24, x + 90, y + 24), fill="#3f8a5e"), d.ellipse((x - 18, y - 30, x + 18, y - 6), fill="#f4a8c0")) for x, y in ((220, 1350), (560, 1420), (860, 1330), (420, 1500))], 4, 3)
    pl = L(lambda d: (fill_wave(d, 1300, 12, 240, .3, "#1a3a2a"), C.princess(d, 400, 1330, 2.0), C.prince(d, 700, 1330, 2.0)), 10, 8)
    return bg.convert("RGB"), [(0.4, S.cached("hill3", X.hill_far), None), (1.0, pl, bob(3, 1.2)), (0.8, waves(1340, ["#2c6f88", "#1f5670", "#18445a"], dy=(0, 120, 260)), None), (0.9, pond, bob(4, 1.0))]


def show():
    bg = grad((70, 36, 24), (150, 90, 50)).convert("RGBA")
    pl = L(lambda d: (d.rectangle((0, 1560, 1080, 1920), fill="#4a2a1a"), d.rectangle((270, 1380, 810, 1430), fill="#8a5a30"), C.crossbow(d, 540, 1330, 1.3, arrow=False), C.princess(d, 170, 1640, 2.3), C.prince(d, 910, 1640, 2.3)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1200, 360)), (1.0, pl, None)]


def swap():
    bg = grad((10, 8, 20), (40, 24, 44)).convert("RGBA")
    pl = L(lambda d: (d.rectangle((0, 1500, 1080, 1920), fill="#241624"), C.crossbow(d, 480, 1380, 2.0, arrow=False), d.polygon([(1080, 950), (1080, 1380), (930, 1300), (800, 1190), (790, 1120), (850, 1060), (950, 1000)], fill="#0c0810"), d.ellipse((760, 1050, 860, 1150), fill="#0c0810")), 10, 8)
    real = L(lambda d: d.polygon([(770, 1040), (830, 1035), (850, 1110), (815, 1140), (780, 1090)], fill=GOLD, outline=EDGE), 6, 4)
    can = L(lambda d: (d.rectangle((90, 1480, 130, 1560), fill=CREAM), flame(d, 110, 1480, .6)), 4, 3)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(110, 1440, 380)), (1.0, pl, None), (0, "glow", S.sword_glow(805, 1100, 140)), (1.0, real, bob(6, 2)), (1.0, can, bob(3, 9))]


def farewell():
    bg = sky((90, 60, 110), (250, 190, 130), (300, 980, 150, (255, 230, 170, 255)))
    pl = L(lambda d: (fill_wave(d, 1480, 14, 240, .5, "#5a4030"), gate(d, 200, 1480, 1.0), C.horse(d, 700, 1700, 1.4, "#e6dcc8", 1), C.prince(d, 700, 1520, 1.6), C.princess(d, 260, 1700, 2.0)), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1100, 30, 120, 2, "#7a4a6a", False), None), (1.0, pl, bob(3, 1.4))]


def feather_road():
    bg = X._night_bg().convert("RGBA")
    pl = L(lambda d: (fill_wave(d, 1220, 14, 240, .4, "#3a2e22"), d.polygon([(360, 1920), (720, 1920), (620, 1220), (460, 1220)], fill="#6a5a44"), [C.feather(d, x, y, sz, a) for x, y, sz, a in ((420, 1520, 1.6, .3), (640, 1640, 2.0, -.4), (520, 1360, 1.2, .8), (700, 1450, 1.4, 1.2), (400, 1760, 2.2, -.2), (580, 1260, 1.0, .2))]), 8, 6)
    return bg.convert("RGB"), [(0.4, S.cached("hill3", X.hill_far), None), (1.0, pl, bob(4, 1.2))]


def invasion():
    bg = sky((34, 20, 48), (150, 76, 80), (240, 860, 130, (232, 150, 110, 255)))

    def row(base, s_, n, col, gap):
        def f(d):
            fill_wave(d, base + 8, 12, 170, base / 300, col)
            for i in range(n): C.soldier_bac(d, 80 + i * gap + (gap / 2 if base % 2 else 0), base, s_)
        return f
    fl = L(lambda d: [(d.line((x, 650, x, 1060), fill="#1a0c10", width=9), d.polygon([(x, 660), (x + 150, 690), (x + 20, 720), (x + 150, 750), (x, 760)], fill="#262a36")) for x in (220, 560, 900)], 6, 4)
    return bg.convert("RGB"), [(0.3, S.mountain(1010, 50, 80, 2, "#2a1a2a", True), None), (0.5, L(row(1130, .55, 8, "#241420", 150), 8, 6), None), (0.6, fl, sway(8, 3)), (0.8, L(row(1260, .9, 5, "#1a1018", 230), 10, 8), None), (1.0, L(row(1420, 1.3, 4, "#10080e", 330), 12, 10), None)]


def xbow_fail():
    bg = grad((84, 84, 98), (150, 140, 134)).convert("RGBA")
    pl = L(lambda d: (fill_wave(d, 1520, 12, 240, .4, "#4a3e34"), C.crossbow(d, 600, 1480, 1.5, arrow=False), d.line((540, 1480, 720, 1680), fill="#d8d0b8", width=9), C.king(d, 220, 1660, 2.5)), 10, 8)
    dots = L(lambda d: [d.ellipse((x - 16, y - 16, x + 16, y + 16), fill="#2a2a34") for x, y in ((820, 900), (900, 960), (960, 880), (760, 960), (1000, 1000))], 0, 0)
    return bg.convert("RGB"), [(0.3, S.mountain(1100, 20, 120, 4, "#a8a49a", False), None), (0.5, dots, lambda t: (-60 * (t % 2), 0)), (1.0, pl, None)]


def flight():
    bg = sky((40, 12, 20), (190, 60, 40))
    city = L(lambda d: (fill_wave(d, 1100, 10, 240, .2, "#1a0a10"), wall(d, -20, 600, 1050, 1180, "#3a2018"), [flame(d, x, y, s_) for x, y, s_ in ((150, 1050, 1.5), (380, 1050, 1.8), (560, 1080, 1.3))]), 6, 4)
    rd = L(lambda d: (fill_wave(d, 1500, 14, 240, .6, "#2a1a14"), C.horse(d, 640, 1720, 1.6, "#7a4a2a", -1), C.king(d, 700, 1490, 1.0), C.princess(d, 590, 1490, 1.0)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(300, 1000, 420)), (0.5, city, None), (1.0, rd, bob(10, 6)), (0, "sparkle", None)]


def ride():
    bg = X._night_bg().convert("RGBA")
    fe = L(lambda d: [C.feather(d, 900 - i * 105, 1460 + (i % 3) * 36, 1.0, .3 + (i % 4) * .3) for i in range(8)], 4, 3)
    rd = L(lambda d: (fill_wave(d, 1400, 14, 240, .6, "#2a2418"), C.horse(d, 760, 1560, 1.1, "#7a4a2a", -1), C.king(d, 800, 1400, .75), C.princess(d, 720, 1400, .75)), 10, 8)
    return bg.convert("RGB"), [(0.4, S.cached("hill3", X.hill_far), None), (1.0, rd, bob(6, 6)), (0.9, fe, None)]


def chase():
    bg = sky((40, 22, 50), (190, 100, 80), (260, 800, 120, (255, 190, 130, 255)))
    fe = L(lambda d: [C.feather(d, 100 + i * 70, 1420 + (i % 3) * 30, .8, .3 + (i % 4) * .3) for i in range(11)], 4, 3)
    rd = L(lambda d: (fill_wave(d, 1360, 14, 240, .6, "#2a1c18"), [(C.horse(d, x, b, s_, "#3a2a2a", -1), C.soldier_bac(d, x + 20, b - 150 * s_, s_ * .85)) for x, b, s_ in ((700, 1700, 1.2), (980, 1640, 1.0))]), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1090, 30, 120, 2, "#4a2a40", True), None), (0.9, fe, None), (1.0, rd, bob(8, 7))]


def shore():
    bg = sky((60, 30, 70), (240, 130, 90), (600, 880, 160, (255, 214, 140, 255)))
    cl = L(lambda d: (d.polygon([(-20, 1920), (-20, 1180), (420, 1180), (560, 1300), (600, 1920)], fill="#3a2a2a"), C.horse(d, 280, 1180, 1.3, "#7a4a2a", 1), C.king(d, 330, 1020, .85), C.princess(d, 230, 1020, .85)), 10, 8)
    return bg.convert("RGB"), [(0.4, waves(1300, ["#d9885a", "#9a5a6a", "#523a66"], dy=(0, 120, 280), amp=24), sway(10, 1.2)), (1.0, cl, None)]


def turtle_sea():
    bg = X._night_bg().convert("RGBA")
    tur = L(lambda d: X.turtle(d, 690, 1250, 1.8), 14, 12)
    return bg.convert("RGB"), [(0.3, waves(1200, ["#2c6f88", "#1f5670", "#18445a"], dy=(0, 120, 260), amp=22), sway(8, 1.0)), (0, "glow", S.sword_glow(690, 1100, 420)), (0.9, tur, lambda t: (0, 160 * (1 - min(t / 1.2, 1)) ** 2)), (0.9, waves(1360, ["#2c6f88", "#1f5670", "#18445a"], dy=(0, 120, 260)), None), (0, "sparkle", None)]


def sword_silhouette():
    bg = grad((90, 14, 24), (230, 70, 50)).convert("RGBA"); sw = S.sword_rgba(420).rotate(-24, expand=True, resample=Image.BICUBIC)
    sl = L(lambda d: (d.polygon([(240, 1920), (330, 1560), (350, 1430), (470, 1400), (560, 1440), (600, 1560), (700, 1920)], fill="#120810"), d.ellipse((350, 1250, 480, 1400), fill="#120810"),
                      d.polygon([(350, 1260), (370, 1190), (410, 1230), (440, 1170), (470, 1230), (500, 1190), (480, 1260)], fill="#120810"),
                      d.polygon([(520, 1480), (600, 1450), (700, 1280), (650, 1240), (580, 1380)], fill="#120810"), d.ellipse((620, 1210, 720, 1300), fill="#120810")), 0, 0)
    ml = L(lambda d: None); ml.alpha_composite(sw, (PAD + 600, 700))
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (1.0, sl, None), (0.9, ml, bob(6, 1.5))]


def prayer():
    bg = grad((14, 18, 52), (70, 54, 110)).convert("RGBA")
    pl = L(lambda d: C.princess(d, 540, 1700, 3.6), 10, 8)
    gems = L(lambda d: [d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 245, 232, 235)) for x, y, r in ((200, 700, 22), (860, 600, 28), (300, 1100, 16), (800, 1000, 20), (140, 1350, 26), (930, 1300, 18))], 6, 4)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 1000, 420)), (1.0, pl, bob(3, 1.2)), (0.8, gems, lambda t: (0, -20 * (t % 3)))]


def sea_part():
    bg = X._night_bg().convert("RGBA")

    def walls(d):
        d.polygon([(0, 1920), (0, 700), (360, 900), (440, 1920)], fill="#1f5670"); d.polygon([(1080, 1920), (1080, 700), (720, 900), (640, 1920)], fill="#2c6f88")
        d.polygon([(440, 1920), (360, 900), (720, 900), (640, 1920)], fill="#c8a870")
    tr = L(lambda d: (X.turtle(d, 540, 1500, .9), C.king(d, 560, 1380, .8)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 300)), (0.5, L(walls, 8, 6), None), (1.0, tr, bob(5, 1.3)), (0, "sparkle", None)]


def search():
    bg = sky((40, 44, 90), (170, 140, 150), (700, 760, 120, (240, 224, 220, 255)))
    pl = L(lambda d: (fill_wave(d, 1420, 12, 240, .3, "#c8a870"), C.prince(d, 500, 1640, 2.6), d.polygon([(640, 1600), (820, 1580), (880, 1650), (700, 1690)], fill="#f6d6dc", outline="#d9a8b2"), d.ellipse((720, 1560, 760, 1580), fill="#16121a")), 10, 8)
    return bg.convert("RGB"), [(0.4, waves(1180, ["#4a5a98", "#3a4a84", "#2a3a70"], dy=(0, 120, 260)), sway(8, 1.0)), (1.0, pl, bob(3, 1.0))]


def well():
    bg = X._night_bg().convert("RGBA")
    pl = L(lambda d: (fill_wave(d, 1300, 12, 240, .3, "#1a3a2a"), d.ellipse((220, 1380, 860, 1560), fill="#5a5a60", outline="#2a2a30"), d.ellipse((290, 1400, 790, 1520), fill="#0c1a2a"), d.ellipse((470, 1420, 620, 1490), fill="#f4ead2"), d.rectangle((230, 1470, 850, 1620), fill="#5a5a60"), d.polygon([(230, 1470), (230, 1620), (850, 1620), (850, 1470), (790, 1520), (290, 1520)], fill="#6a6a72")), 10, 8)
    return bg.convert("RGB"), [(0.4, S.cached("hill3", X.hill_far), None), (1.0, pl, None), (0, "sparkle", None)]


def pearl():
    bg = grad((10, 60, 80), (4, 24, 44)).convert("RGBA")
    sh = L(lambda d: (d.polygon([(220, 1250), (540, 1100), (860, 1250), (780, 1420), (300, 1420)], fill="#d8c8b8", outline="#8a7a6a"), d.polygon([(260, 1250), (540, 1180), (820, 1250), (780, 1310), (300, 1310)], fill="#efe4d4"), d.ellipse((440, 1130, 640, 1330), fill="#ffffff", outline="#cfd8e0")), 12, 10)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 1230, 340)), (0.9, sh, bob(5, 1.2)), (0, "sparkle", None)]


def gem():
    bg = X._night_bg().convert("RGBA")
    pr = L(lambda d: (d.ellipse((440, 880, 640, 1080), fill="#ffffff", outline="#cfd8e0"), d.ellipse((480, 920, 540, 970), fill="#f4f8ff")), 12, 10)
    return bg.convert("RGB"), [(0.3, waves(1300, ["#2c6f88", "#1f5670", "#18445a"], dy=(0, 120, 260), amp=18), sway(8, 1.0)), (0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 980, 360)), (0.9, pr, lambda t: (0, 120 * (1 - min(t / 1.6, 1)) ** 2 + 6 * math.sin(t * 2))), (0, "sparkle", None)]


def _worker(d, cx, base, s):
    p = lambda dx, dy: (cx + dx * s, base + dy * s)
    d.polygon([p(-46, 0), p(-30, -130), p(30, -130), p(46, 0)], fill="#5a7a9a"); _head = (*p(-28, -196), *p(28, -136)); d.ellipse(_head, fill="#f0d4a8"); d.polygon([p(-34, -186), p(34, -186), p(26, -214), p(-26, -214)], fill="#6a5a44")
    d.line([p(50, -20), p(80, -180)], fill="#6a4a2a", width=max(int(8 * s), 3)); d.polygon([p(66, -180), p(100, -176), p(92, -140), p(72, -140)], fill="#9aa0a8")


def dig():
    bg = sky((150, 200, 230), (240, 236, 220), (200, 420, 100, (255, 248, 220, 255)))
    pl = L(lambda d: (d.rectangle((0, 1350, 1080, 1920), fill="#7a5a3a"), d.polygon([(200, 1350), (880, 1350), (780, 1700), (300, 1700)], fill="#5a3e26"), [_worker(d, x, b, 1.5) for x, b in ((340, 1700), (560, 1700), (780, 1700))], [d.ellipse((x - 60, 1300, x + 60, 1360), fill="#8a6a46") for x in (120, 960)]), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1220, 30, 120, 2, "#a4c8a8", False), None), (1.0, pl, bob(3, 3))]


def arrows():
    bg = grad((90, 62, 38), (40, 26, 18)).convert("RGBA")

    def heap(d):
        import random; r = random.Random(4)
        for i in range(60):
            x, y, a = r.uniform(120, 960), r.uniform(1000, 1700), r.uniform(0, 6.28); l_ = r.uniform(70, 110)
            pts = [(x, y), (x + l_ * math.cos(a) - 18 * math.sin(a), y + l_ * math.sin(a) + 18 * math.cos(a)), (x + l_ * math.cos(a) + 18 * math.sin(a), y + l_ * math.sin(a) - 18 * math.cos(a))]; d.polygon(pts, fill="#b8742c", outline="#6a3a14")
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1350, 460)), (0.9, L(heap, 8, 6), None), (0, "sparkle", None)]


def coloa_today():
    bg = sky((150, 210, 240), (250, 240, 214), (840, 380, 110, (255, 248, 220, 255)))
    mound = L(lambda d: (fill_wave(d, 1120, 50, 300, 1.2, "#6ab070"), fill_wave(d, 1300, 30, 260, 2.2, "#4f9a5e")), 8, 6)
    temple = L(lambda d: (d.rectangle((300, 1020, 780, 1250), fill=CREAM, outline=EDGE), d.polygon([(250, 1030), (830, 1030), (700, 900), (380, 900)], fill=RED), d.rectangle((480, 1110, 600, 1250), fill=INK), d.polygon([(250, 1030), (300, 1060), (780, 1060), (830, 1030)], fill="#8e2018"), [(d.rectangle((x - 20, 1180, x + 20, 1330), fill="#5a3e26"), d.ellipse((x - 90, 1060, x + 90, 1260), fill="#3f8a5e")) for x in (130, 950)]), 8, 6)
    return bg.convert("RGB"), [(0.3, S.mountain(1060, 30, 110, 2, "#a4d0b0", False), None), (0.6, mound, None), (0.9, temple, None), (1.0, ground(1560, "#4f9a5e", 10), None)]


REG = {"nt_" + k: v for k, v in dict(coloa_night=coloa_night, crossbow_fire=crossbow_fire, fall=fall, king_build=king_build, wall_collapse=wall_collapse, kimquy_rise=kimquy_rise, claw=claw, trigger=trigger, north=north,
          defeat=defeat, scheme=scheme, prince_arrive=prince_arrive, wedding=wedding, couple=couple, show=show, swap=swap, farewell=farewell, feather_road=feather_road, invasion=invasion, xbow_fail=xbow_fail,
          flight=flight, ride=ride, chase=chase, shore=shore, turtle_sea=turtle_sea, sword_silhouette=sword_silhouette, prayer=prayer, gem=gem, sea_part=sea_part, search=search, well=well, pearl=pearl, dig=dig,
          arrows=arrows, coloa_today=coloa_today).items()}
