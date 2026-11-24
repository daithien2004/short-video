"""Scenes for the Thánh Gióng story. Every scene is its own composition; characters come from chars_tg.py / chars.py."""
import math
from PIL import Image, ImageDraw
import story2 as S, story3 as X, chars as C, chars_tg as G
from story2 import layer, grad, fill_wave, W, H, PAD, CREAM, RED, GOLD, INK, GREEN, EDGE
from scenes_hk2 import L, waves, sway, bob, _peasant, _paddy
from scenes_nt import sky, ground, wall, flame

THATCH, WOOD = "#d8b86a", "#6a4a2a"


def _hut(d, x, base, w=260, h=150):
    d.rectangle((x, base - h, x + w, base), fill="#a8793c", outline="#5a3e26"); d.polygon([(x - 40, base - h + 6), (x + w + 40, base - h + 6), (x + w - 30, base - h - 120), (x + 30, base - h - 120)], fill=THATCH, outline="#8a6a30")
    d.rectangle((x + w * .4, base - h * .7, x + w * .6, base), fill=INK)


def _smoke(d, pts, col=(70, 60, 64, 190)):
    for x, y, r in pts: d.ellipse((x - r, y - r, x + r, y + r), fill=col)


def _rays_bg(c0, c1): return grad(c0, c1).convert("RGBA")


def village():
    bg = sky((255, 226, 176), (170, 210, 200), (300, 520, 110, (255, 246, 220, 255)))
    grove = L(lambda d: [G.bamboo(d, x, 1200, h, lean=l) for x, h, l in ((70, 520, 10), (150, 640, -14), (940, 600, 12), (1020, 500, -10))], 6, 4)
    hut = L(lambda d: (_hut(d, 330, 1200), _hut(d, 700, 1230, 230, 130)), 8, 6)
    pl = L(lambda d: (fill_wave(d, 1450, 12, 240, .4, "#6aa44e"), _peasant(d, 380, 1640, 1.5, 0, "#c8372d"), _peasant(d, 760, 1660, 1.7, 0, "#2f6a8a")), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1060, 40, 110, 2, "#a4c8a8", False), None), (0.5, grove, sway(5, .8)), (0.7, hut, None), (0.8, _paddy(1250, ["#9fd078", "#86bc62", "#6aa44e", "#549040"]), None), (1.0, pl, sway(4, 1.0))]


def boy_lying():
    bg = grad((60, 40, 30), (150, 100, 60)).convert("RGBA")
    room = L(lambda d: (d.rectangle((0, 1560, 1080, 1920), fill="#7a5a36"), d.polygon([(120, 0), (520, 0), (820, 1500), (240, 1500)], fill=(255, 226, 150, 60))), 0, 0)
    pl = L(lambda d: (G.boy_lying(d, 640, 1640, 1.8), G.mother(d, 220, 1700, 2.2), d.ellipse((900, 1560, 1020, 1660), fill="#8a4a2a", outline="#4a2a14")), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(500, 700, 360)), (0.4, room, None), (1.0, pl, bob(2, 1.0))]


def giant_shadow():
    bg = sky((40, 26, 70), (240, 150, 100), (540, 1000, 200, (255, 214, 140, 255)))
    sil = L(lambda d: (d.polygon([(380, 1300), (400, 1000), (360, 760), (430, 560), (500, 520), (560, 440), (600, 380), (620, 440), (680, 520), (740, 700), (700, 1000), (720, 1300)], fill="#1a0e22"),
                       d.ellipse((470, 380, 600, 520), fill="#1a0e22"), d.polygon([(500, 390), (540, 270), (590, 390)], fill="#1a0e22"), d.polygon([(760, 1100), (800, 560), (820, 560), (790, 1100)], fill="#1a0e22")), 0, 0)
    pl = L(lambda d: (fill_wave(d, 1220, 30, 260, .3, "#2a1a30"), _hut(d, 120, 1300, 240, 130), _hut(d, 760, 1330, 220, 120), fill_wave(d, 1360, 14, 240, .8, "#1a1020")), 10, 8)
    return bg.convert("RGB"), [(0.2, sil, None), (1.0, pl, None)]


def footprint():
    bg = sky((150, 200, 230), (250, 236, 200), (900, 380, 100, (255, 248, 220, 255)))
    pr = L(lambda d: (d.ellipse((380, 1280, 880, 1760), fill="#8a6a46", outline="#5a3e26"), d.ellipse((430, 1330, 830, 1710), fill="#7a5a38"), [d.ellipse((x - r, y - r, x + r, y + r), fill="#8a6a46", outline="#5a3e26") for x, y, r in ((420, 1230, 50), (520, 1190, 56), (630, 1180, 56), (740, 1200, 52), (830, 1250, 44))]), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1100, 30, 120, 2, "#a4c8a8", False), None), (0.8, _paddy(1150, ["#9fd078", "#86bc62", "#6aa44e", "#549040"]), None), (1.0, pr, None), (1.0, L(lambda d: G.mother(d, 220, 1700, 2.5), 10, 8), bob(2, 1.0))]


def mother_foot():
    bg = grad((255, 214, 150), (240, 150, 120)).convert("RGBA")
    pr = L(lambda d: (d.ellipse((260, 1560, 960, 1840), fill="#8a6a46", outline="#5a3e26"), d.ellipse((330, 1600, 880, 1810), fill="#7a5a38")), 8, 6)
    ml = L(lambda d: (G.mother(d, 540, 1700, 3.4), d.ellipse((430, 1680, 560, 1760), fill=SKIN_FOOT)), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(560, 1720, 300)), (0.8, pr, None), (1.0, ml, bob(3, 1.2))]


SKIN_FOOT = "#f3dcb4"


def baby():
    bg = grad((14, 18, 44), (40, 34, 70)).convert("RGBA")
    pl = L(lambda d: (d.rectangle((0, 1620, 1080, 1920), fill="#5a3e26"), d.line([(160, 1000), (400, 1280), (700, 1280), (920, 1000)], fill="#c8a45a", width=14), d.polygon([(360, 1260), (700, 1260), (640, 1380), (420, 1380)], fill="#efe0b4", outline="#8a6a30"), d.ellipse((470, 1190, 590, 1300), fill=SKIN_FOOT), d.ellipse((500, 1230, 514, 1244), fill="#2b2420"), d.ellipse((540, 1230, 554, 1244), fill="#2b2420"), G.mother(d, 230, 1740, 2.4)), 10, 8)
    mn = L(lambda d: (d.rectangle((760, 220, 980, 520), fill="#1a1230", outline="#5a3e26"), d.ellipse((840, 280, 920, 360), fill="#f4ead2")), 4, 3)
    return bg.convert("RGB"), [(0.4, mn, None), (0, "glow", S.sword_glow(540, 1300, 300)), (1.0, pl, bob(3, 1.0))]


def invasion():
    bg = sky((40, 12, 20), (190, 60, 40))
    burn = L(lambda d: (_hut(d, 90, 1250, 240, 130), _hut(d, 700, 1260, 250, 140), [flame(d, x, y, s_) for x, y, s_ in ((200, 1160, 1.4), (820, 1160, 1.6), (460, 1240, 1.0))]), 8, 6)
    sm = L(lambda d: _smoke(d, ((220, 760, 90), (300, 620, 120), (840, 700, 100), (920, 560, 130))), 0, 0)
    foes = L(lambda d: (fill_wave(d, 1520, 14, 240, .5, "#1a0a10"), [G.soldier_an(d, x, b, s_) for x, b, s_ in ((200, 1620, 1.5), (520, 1660, 1.9), (860, 1620, 1.5))]), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1200, 420)), (0.6, L(burn.__class__ and (lambda d: None), 0, 0) if False else burn, bob(3, 6)), (0.5, sm, lambda t: (0, -30 * (t % 3))), (1.0, foes, None)]


def king_worry():
    bg = grad((20, 30, 70), (70, 60, 100)).convert("RGBA")
    hall = L(lambda d: ([d.rectangle((x - 46, 200, x + 46, 1500), fill="#8e1f24", outline=EDGE) for x in (70, 1010)], d.rectangle((0, 200, 1080, 270), fill=GOLD), d.rectangle((0, 1500, 1080, 1920), fill="#3a2a40")), 8, 6)
    pl = L(lambda d: (G.envoy(d, 190, 1660, 2.0), C.soldier_au(d, 900, 1660, 2.0), G.king_hung(d, 540, 1660, 2.8)), 10, 8)
    return bg.convert("RGB"), [(0.5, hall, None), (0, "glow", S.sword_glow(540, 800, 380)), (1.0, pl, bob(2, 1.1))]


def envoy_ride():
    bg = sky((150, 200, 230), (250, 236, 200), (900, 380, 100, (255, 248, 220, 255)))
    rd = L(lambda d: (fill_wave(d, 1420, 14, 240, .5, "#8a6a42"), C.horse(d, 560, 1700, 1.6, "#7a4a2a"), G.envoy(d, 540, 1520, 1.3)), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1080, 30, 120, 2, "#a4c8a8", False), None), (0.8, _paddy(1150, ["#9fd078", "#86bc62", "#6aa44e", "#549040"]), None), (1.0, rd, bob(8, 6))]


def envoy_arrive():
    bg = sky((255, 226, 176), (170, 210, 200), (200, 480, 100, (255, 246, 220, 255)))
    hut = L(lambda d: (_hut(d, 500, 1330, 420, 230), d.rectangle((650, 1180, 760, 1330), fill="#2a1a10"), G.boy_lying(d, 705, 1330, .55)), 8, 6)
    pl = L(lambda d: (fill_wave(d, 1480, 12, 240, .4, "#6aa44e"), G.envoy(d, 200, 1680, 2.2), _peasant(d, 460, 1700, 1.4, 0, "#2f6a8a"), G.mother(d, 960, 1700, 2.0)), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1060, 40, 110, 2, "#a4c8a8", False), None), (0.7, hut, None), (1.0, pl, bob(2, 1.0))]


def boy_speaks():
    bg = grad((255, 224, 150), (240, 160, 90)).convert("RGBA")
    pl = L(lambda d: (d.rectangle((0, 1560, 1080, 1920), fill="#7a5a36"), G.mother(d, 190, 1700, 2.4), G.boy(d, 560, 1700, 3.2), G.envoy(d, 900, 1700, 2.2)), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(560, 1250, 340)), (1.0, pl, bob(3, 1.3)), (0, "sparkle", None)]


def iron_gear():
    bg = grad((40, 14, 14), (130, 50, 30)).convert("RGBA")
    pl = L(lambda d: (d.rectangle((0, 1540, 1080, 1920), fill="#2a1a14"), G.iron_horse(d, 420, 1700, 1.15, 1, False), G.staff(d, 850, 1700, 960, 1000, 22), d.line([(860, 1480), (860, 1700)], fill=WOOD, width=14),
                       d.polygon([(780, 1500), (940, 1500), (920, 1360), (800, 1360)], fill="#9aa3b0", outline="#5a606c"), d.ellipse((790, 1290, 930, 1380), fill="#8a909c", outline="#5a606c")), 12, 10)
    fg = L(lambda d: [flame(d, x, 1560, s_) for x, s_ in ((110, 1.8), (200, 1.2))], 4, 3)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(150, 1500, 420)), (1.0, pl, None), (0.9, fg, bob(4, 8)), (0, "sparkle", None)]


def eating():
    bg = grad((255, 236, 190), (230, 190, 130)).convert("RGBA")
    pl = L(lambda d: (d.rectangle((0, 1560, 1080, 1920), fill="#9a7444"), d.rectangle((120, 1480, 960, 1540), fill="#6a4a2a"),
                      [d.ellipse((x - 70, y - 40, x + 70, y + 40), fill="#f4f0e0", outline="#bbb099") for x, y in ((240, 1470), (380, 1470), (520, 1470), (660, 1470), (800, 1470), (310, 1400), (450, 1400), (590, 1400), (730, 1400), (380, 1330), (520, 1330), (660, 1330), (520, 1260))],
                      G.boy(d, 520, 1540, 2.0) if False else None, G.mother(d, 960, 1720, 2.2)), 10, 8)
    kid = L(lambda d: G.boy(d, 540, 1230, 2.6), 10, 8)
    return bg.convert("RGB"), [(1.0, kid, bob(3, 3)), (1.0, pl, None)]


def growing():
    bg = sky((255, 226, 176), (170, 210, 200), (900, 460, 100, (255, 246, 220, 255)))
    pl = L(lambda d: (fill_wave(d, 1480, 12, 240, .4, "#6aa44e"), _hut(d, 120, 1500, 280, 150), G.boy(d, 700, 1640, 5.0), [_peasant(d, x, 1700, 1.1, 0, c) for x, c in ((130, "#c8372d"), (330, "#2f6a8a"))]), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1080, 40, 110, 2, "#a4c8a8", False), None), (1.0, pl, sway(3, 1.0))]


def rice_baskets():
    bg = sky((255, 214, 150), (190, 210, 170), (800, 500, 110, (255, 246, 220, 255)))
    pl = L(lambda d: (fill_wave(d, 1420, 12, 240, .4, "#b8a050"), _hut(d, 640, 1440, 340, 190), G.mother(d, 880, 1680, 2.2), [_peasant(d, x, b, 1.6, 1, c) for x, b, c in ((180, 1700, "#6b4a2e"), (440, 1740, "#5a4a3e"))]), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1080, 30, 120, 3, "#c8c890", False), None), (0.8, _paddy(1250, ["#e0c060", "#d0b050", "#c0a040", "#b09030"]), None), (1.0, pl, sway(4, 1.0))]


def gear_arrive():
    bg = sky((150, 200, 230), (250, 236, 200), (200, 480, 100, (255, 248, 220, 255)))

    def cart(d):
        d.rectangle((560, 1480, 1000, 1540), fill=WOOD, outline="#3a2414"); [d.ellipse((x - 60, 1500, x + 60, 1620), fill="#4a3220", outline="#2a1a10") for x in (640, 920)]
        G.staff(d, 640, 1470, 900, 1180, 20); d.polygon([(700, 1480), (860, 1480), (840, 1360), (720, 1360)], fill="#9aa3b0", outline="#5a606c"); d.ellipse((720, 1300, 840, 1380), fill="#8a909c", outline="#5a606c")
    pl = L(lambda d: (fill_wave(d, 1500, 12, 240, .4, "#8a6a42"), G.iron_horse(d, 250, 1700, .9, 1, False), G.envoy(d, 470, 1700, 1.5), _peasant(d, 130, 1680, 1.1, 0, "#c8372d")), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1090, 30, 120, 2, "#a4c8a8", False), None), (1.0, L(cart, 10, 8), bob(2, 2)), (1.0, pl, None)]


def stretch():
    bg = grad((255, 206, 140), (220, 120, 90)).convert("RGBA")
    clouds = L(lambda d: [d.ellipse((x - r, y - r * .5, x + r, y + r * .5), fill=(255, 240, 220, 200)) for x, y, r in ((200, 1100, 220), (860, 1300, 260), (500, 1500, 300))], 0, 0)
    pl = L(lambda d: (G.gion(d, 540, 1700, 5.4), [d.polygon([(x, y), (x + 70, y - 24), (x + 30, y + 22)], fill=THATCH) for x, y in ((150, 640), (860, 560), (240, 1020), (900, 980))]), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0.5, clouds, None), (0, "glow", S.sword_glow(540, 800, 420)), (1.0, pl, lambda t: (0, -30 * min(t / 1.2, 1))), (0, "sparkle", None)]


def mount():
    bg = sky((150, 200, 230), (250, 236, 200), (900, 380, 100, (255, 248, 220, 255)))
    pl = L(lambda d: (fill_wave(d, 1480, 12, 240, .4, "#8a6a42"), G.iron_horse(d, 500, 1700, 1.8, 1, False), G.gion(d, 540, 1360, 1.3), [d.ellipse((x - r, 1700 - r * .5, x + r, 1700 + r * .5), fill=(200, 180, 150, 150)) for x, r in ((200, 90), (320, 70), (760, 60))]), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1090, 30, 120, 2, "#a4c8a8", False), None), (1.0, pl, bob(4, 3))]


def horse_fire():
    bg = sky((90, 24, 30), (240, 130, 70), (260, 820, 150, (255, 214, 140, 255)))
    lines = L(lambda d: [d.line([(x, y), (x - 240, y)], fill=(255, 240, 220, 150), width=8) for x, y in ((420, 1180), (300, 1300), (460, 1440), (380, 1560))], 0, 0)
    pl = L(lambda d: (fill_wave(d, 1620, 14, 240, .5, "#2a1410"), G.iron_horse(d, 540, 1740, 1.8, 1, True), G.gion(d, 580, 1400, 1.3)), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1090, 30, 120, 2, "#5a2a30", False), None), (0.6, lines, lambda t: (-60 * (t % 1), 0)), (1.0, pl, bob(10, 7)), (0, "glow", S.sword_glow(900, 1160, 260))]


def battle():
    bg = sky((60, 20, 30), (200, 90, 50))
    pl = L(lambda d: (fill_wave(d, 1580, 14, 240, .5, "#2a1410"), G.gion(d, 540, 1700, 3.0), G.staff(d, 640, 1500, 930, 760, 30),
                      [G.soldier_an(d, x, b, s_) for x, b, s_ in ((170, 1660, 1.5), (880, 1640, 1.3), (330, 1620, 1.1))]), 10, 8)
    dust = L(lambda d: [d.ellipse((x - r, y - r * .6, x + r, y + r * .6), fill=(200, 170, 140, 160)) for x, y, r in ((150, 1640, 120), (900, 1630, 110), (520, 1700, 160))], 0, 0)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1100, 400)), (1.0, pl, bob(5, 4)), (0.9, dust, lambda t: (0, -10 * (t % 2)))]


def staff_break():
    bg = grad((70, 20, 30), (210, 80, 50)).convert("RGBA")
    pl = L(lambda d: (fill_wave(d, 1620, 14, 240, .5, "#2a1410"), G.gion(d, 400, 1740, 2.8), G.staff(d, 520, 1560, 620, 1380, 30), G.staff(d, 780, 1000, 900, 780, 24), G.staff(d, 720, 1300, 830, 1130, 16),
                      d.polygon([(610, 1380), (650, 1340), (630, 1420)], fill="#a8aeb8"), [G.soldier_an(d, x, 1700, 1.8) for x in (840,)]), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(640, 1300, 260)), (1.0, pl, bob(4, 5)), (0, "sparkle", None)]


def bamboo():
    bg = sky((120, 170, 120), (230, 230, 170), (200, 420, 100, (255, 248, 220, 255)))
    pl = L(lambda d: (fill_wave(d, 1560, 12, 240, .4, "#5a8a40"), [G.bamboo(d, x, 1600, h, lean=l) for x, h, l in ((560, 1200, 60), (660, 1300, 90), (760, 1150, 70), (860, 1250, 110))],
                      G.gion(d, 280, 1720, 2.6), d.polygon([(520, 1600), (900, 1600), (860, 1680), (560, 1680)], fill="#5a3e26")), 10, 8)
    dirt = L(lambda d: [d.ellipse((x - r, y - r, x + r, y + r), fill="#6a4a2a") for x, y, r in ((520, 1520, 26), (900, 1540, 20), (700, 1480, 16), (820, 1500, 22))], 0, 0)
    return bg.convert("RGB"), [(0.3, S.mountain(1090, 30, 120, 2, "#7aaa7a", False), None), (1.0, pl, sway(6, 1.4)), (0.9, dirt, lambda t: (0, -14 * (t % 1)))]


def bamboo_swing():
    bg = sky((90, 40, 40), (230, 120, 70))
    stalk = L(lambda d: (d.line([(560, 1500), (1000, 640)], fill="#5a9a4a", width=34), [G.bamboo(d, 1000, 640, 1, lean=0) for _ in (0,)], [d.polygon([(x, y), (x + 100, y - 30), (x + 36, y + 26)], fill="#3f7d3a") for x, y in ((960, 700), (900, 800), (840, 900))]), 8, 6)
    pl = L(lambda d: (fill_wave(d, 1600, 14, 240, .5, "#2a1410"), G.gion(d, 380, 1740, 2.8), [G.soldier_an(d, x, 1700, 1.4) for x in (900,)]), 10, 8)
    fl = L(lambda d: [d.polygon([(x, y), (x + 80, y - 30), (x + 30, y + 24)], fill="#4f9a4a") for x, y in ((180, 700), (260, 540), (700, 520), (820, 440), (140, 900))], 0, 0)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(700, 1100, 360)), (1.0, pl, None), (0.9, stalk, lambda t: (-20 * math.sin(t * 5), 0)), (0.8, fl, lambda t: (-50 * (t % 1.2), 20 * (t % 1.2)))]


def flee():
    bg = grad((236, 200, 170), (250, 236, 210)).convert("RGBA")
    run = L(lambda d: (fill_wave(d, 1480, 14, 240, .4, "#8a6a42"), [(G.soldier_an(d, x, b, s_), d.line([(x - 40 * s_, b - 190 * s_), (x - 90 * s_, b - 330 * s_)], fill="#3a2a2a", width=6)) for x, b, s_ in ((200, 1620, 1.5), (500, 1660, 1.7), (820, 1600, 1.3), (990, 1560, 1.0))]), 10, 8)
    ban = L(lambda d: [(d.line([(x, y), (x + 100, y + 200)], fill="#3a2a2a", width=8), d.polygon([(x + 100, y + 200), (x + 220, y + 240), (x + 130, y + 280)], fill=RED)) for x, y in ((120, 900), (700, 1000))], 4, 3)
    return bg.convert("RGB"), [(0.3, S.mountain(1090, 30, 120, 3, "#c8b898", False), None), (0.9, ban, None), (1.0, run, bob(6, 7))]


def soc_mountain():
    bg = sky((60, 30, 90), (250, 140, 90), (700, 760, 170, (255, 220, 150, 255)))
    pl = L(lambda d: (d.polygon([(-20, 1920), (-20, 1380), (260, 1100), (520, 960), (720, 1100), (1100, 1400), (1100, 1920)], fill="#4a3a52"), G.gion(d, 520, 980, 2.2, cape=True), C.horse(d, 880, 1130, .8, "#5a606c", -1),
                      d.polygon([(250, 1040), (330, 1000), (350, 1060), (270, 1080)], fill="#9aa3b0", outline="#5a606c"), d.ellipse((140, 1000, 230, 1070), fill="#8a909c", outline="#5a606c")), 10, 8)
    cl = L(lambda d: [d.ellipse((x - r, y - r * .4, x + r, y + r * .4), fill=(255, 230, 220, 200)) for x, y, r in ((200, 700, 200), (860, 560, 220), (540, 1500, 360))], 0, 0)
    return bg.convert("RGB"), [(0.4, cl, sway(20, .3)), (1.0, pl, None)]


def fly():
    bg = grad((120, 170, 230), (255, 226, 170)).convert("RGBA"); ImageDraw.Draw(bg).ellipse((780 - 130, 500 - 130, 780 + 130, 500 + 130), fill=(255, 248, 220, 255))
    cl = L(lambda d: [d.ellipse((x - r, y - r * .45, x + r, y + r * .45), fill=(255, 255, 255, 230)) for x, y, r in ((200, 1300, 260), (800, 1500, 320), (500, 1750, 380), (900, 800, 200))], 0, 0)
    grp = L(lambda d: (G.iron_horse(d, 480, 1100, 1.4, 1, True), G.gion(d, 520, 800, 1.1)), 10, 8).rotate(18, center=(540, 960), resample=Image.BICUBIC)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(780, 500, 300)), (0.4, cl, sway(30, .4)), (0.9, grp, lambda t: (60 * min(t / 2, 1), -120 * min(t / 2, 1))), (0, "sparkle", None)]


def king_title():
    bg = grad((120, 24, 36), (200, 120, 60)).convert("RGBA")
    hall = L(lambda d: ([d.rectangle((x - 46, 200, x + 46, 1500), fill=RED, outline=EDGE) for x in (70, 1010)], d.rectangle((0, 200, 1080, 270), fill=GOLD), d.rectangle((0, 1500, 1080, 1920), fill="#7a2a20")), 8, 6)
    pl = L(lambda d: (G.king_hung(d, 330, 1660, 2.8), G.envoy(d, 800, 1660, 2.5), d.rectangle((600, 1180, 700, 1300), fill=GOLD, outline=EDGE), d.rectangle((560, 1160, 740, 1190), fill="#efe0b4")), 10, 8)
    return bg.convert("RGB"), [(0.5, hall, None), (0, "glow", S.sword_glow(660, 1250, 320)), (1.0, pl, bob(2, 1.2)), (0, "sparkle", None)]


def temple():
    bg = sky((255, 226, 176), (190, 210, 200), (900, 420, 110, (255, 246, 220, 255)))

    def tp(d):
        d.rectangle((260, 1080, 820, 1330), fill=CREAM, outline=EDGE); d.polygon([(190, 1090), (890, 1090), (770, 940), (310, 940)], fill=RED); d.polygon([(190, 1090), (230, 1130), (850, 1130), (890, 1090)], fill="#8e2018"); d.rectangle((470, 1180, 610, 1330), fill=INK)
        d.polygon([(350, 940), (730, 940), (620, 820), (460, 820)], fill=RED); d.rectangle((460, 780, 620, 820), fill=GOLD)
    pl = L(lambda d: (fill_wave(d, 1400, 12, 240, .4, "#6aa44e"), [d.rectangle((x - 18, 1130, x + 18, 1400), fill="#5a3e26") for x in (110, 970)], [d.ellipse((x - 120, 960, x + 120, 1200), fill="#3f8a5e") for x in (110, 970)], [_peasant(d, x, b, 1.1, 0, c) for x, b, c in ((380, 1600, "#c8372d"), (700, 1620, "#2f6a8a"))]), 10, 8)
    sm = L(lambda d: _smoke(d, ((540, 700, 60), (560, 580, 80), (540, 440, 100)), (230, 230, 230, 150)), 0, 0)
    return bg.convert("RGB"), [(0.3, S.mountain(1060, 30, 110, 2, "#a4d0b0", False), None), (0.7, L(tp, 8, 6), None), (0.5, sm, lambda t: (10 * math.sin(t), -20 * (t % 2))), (1.0, pl, sway(3, 1.0))]


def bamboo_gold():
    bg = grad((255, 230, 160), (240, 190, 100)).convert("RGBA")
    pl = L(lambda d: (fill_wave(d, 1560, 12, 240, .4, "#a89040"), [G.bamboo(d, x, 1600, h, "#d9b83a", "#b8962a", l) for x, h, l in ((120, 1500, 20), (280, 1300, -20), (460, 1500, 24), (640, 1350, -16), (820, 1550, 20), (980, 1300, -20))],
                      [d.ellipse((x - 26, y - 14, x + 26, y + 14), fill="#6a4a20") for x, y in ((200, 1300), (540, 1100), (900, 1200))]), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 900, 460)), (1.0, pl, sway(8, 1.2)), (0, "sparkle", None)]


def statue():
    bg = sky((255, 214, 150), (190, 200, 210), (800, 460, 120, (255, 246, 220, 255)))

    def st(d):
        d.rectangle((300, 1480, 780, 1620), fill="#8a8478", outline="#4a463e"); d.rectangle((360, 1380, 720, 1480), fill="#a09a8c", outline="#4a463e")
        G.gion(d, 540, 1380, 3.2)
    fl = L(lambda d: [d.ellipse((x - 30, y - 22, x + 30, y + 22), fill=c) for x, y, c in ((200, 1620, "#f2b632"), (290, 1650, "#e8a0b8"), (800, 1640, "#f2b632"), (890, 1620, "#e8a0b8"), (540, 1690, "#c8372d"))], 4, 3)
    return bg.convert("RGB"), [(0.3, S.mountain(1090, 40, 110, 2, "#a4c8a8", False), None), (0.7, L(st, 12, 10), None), (1.0, fl, None), (1.0, ground(1700, "#6aa44e", 10), None), (0, "sparkle", None)]


def edict():
    bg = grad((120, 24, 36), (214, 130, 60)).convert("RGBA")
    sc_ = L(lambda d: (d.rectangle((170, 620, 910, 1300), fill="#efe0b4", outline=EDGE), [d.ellipse((x - 34, 590, x + 34, 1330), fill="#c89a4a", outline=EDGE) for x in (170, 910)],
                       [d.line((280, y, 800, y), fill="#b8a478", width=5) for y in range(700, 1240, 52)], d.ellipse((440, 1020, 640, 1220), fill=RED, outline=EDGE), d.ellipse((480, 1060, 600, 1180), outline=GOLD, width=8)), 12, 10)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 1000, 420)), (0.8, sc_, bob(8, 1.1)), (0, "sparkle", None)]


def heritage():
    bg = grad((14, 16, 48), (60, 44, 90)).convert("RGBA")
    tp = L(lambda d: (d.rectangle((300, 1440, 780, 1600), fill="#2a1a2a", outline=EDGE), d.polygon([(230, 1450), (850, 1450), (740, 1300), (340, 1300)], fill="#5a1a22")), 8, 6)
    medal = L(lambda d: (d.ellipse((380, 700, 700, 1020), fill=GOLD, outline=EDGE), d.ellipse((420, 740, 660, 980), fill="#fff0b0", outline=EDGE), d.polygon([(x, y) for k in range(10) for x, y in ((540 + (96 if k % 2 == 0 else 40) * math.cos(k * math.pi / 5 - math.pi / 2), 860 + (96 if k % 2 == 0 else 40) * math.sin(k * math.pi / 5 - math.pi / 2)),)], fill=GOLD), d.polygon([(450, 1010), (520, 1010), (500, 1150), (440, 1110)], fill=RED), d.polygon([(560, 1010), (630, 1010), (640, 1110), (580, 1150)], fill=RED)), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 860, 420)), (0.8, medal, bob(8, 1.2)), (1.0, tp, None), (0, "sparkle", None)]


def festival():
    bg = sky((150, 200, 230), (250, 236, 200), (900, 340, 100, (255, 248, 220, 255)))

    def flags(d):
        for i, (x, c) in enumerate(((120, RED), (300, GOLD), (480, "#2a7a9a"), (660, RED), (840, GOLD), (1000, "#2a7a9a"))): d.line([(x, 520), (x, 1500)], fill=WOOD, width=10); d.polygon([(x, 530), (x + 170, 580), (x + 20, 640), (x + 170, 700), (x, 740)], fill=c)
    def drum(d): d.ellipse((380, 1380, 700, 1560), fill="#8e2018", outline=EDGE); d.rectangle((380, 1450, 700, 1640), fill="#8e2018", outline=EDGE); d.ellipse((380, 1560, 700, 1700), fill="#8e2018", outline=EDGE); d.ellipse((400, 1400, 680, 1540), fill="#efe0b4", outline=EDGE)
    pl = L(lambda d: (fill_wave(d, 1500, 12, 240, .4, "#8a6a42"), [_peasant(d, x, 1740, 1.6, 0, c) for x, c in ((180, "#c8372d"), (880, "#2f6a8a"))]), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1100, 30, 120, 2, "#a4c8a8", False), None), (0.7, L(flags, 8, 6), sway(10, 2)), (1.0, L(drum, 8, 6), bob(4, 4)), (1.0, pl, bob(3, 3))]


def lanterns():
    bg = grad((12, 14, 40), (50, 36, 70)).convert("RGBA")

    def tl(d):
        d.rectangle((300, 1240, 780, 1420), fill="#2a1a2a", outline=EDGE); d.polygon([(230, 1250), (850, 1250), (740, 1100), (340, 1100)], fill="#5a1a22")
        for x in range(120, 1000, 110): d.line([(x, 560), (x + 55, 640)], fill=GOLD, width=3)
        for i, x in enumerate(range(100, 1000, 110)): y = 640 + (i % 2) * 60; d.ellipse((x - 36, y, x + 36, y + 90), fill=RED, outline=GOLD)
    bursts = L(lambda d: [d.polygon([(x + r * math.cos(a), y + r * math.sin(a)) for k in range(16) for a, r in ((k * math.pi / 8, 110), (k * math.pi / 8 + math.pi / 16, 44))], fill=col) for x, y, col in ((260, 360, "#f2b632"), (800, 280, "#e8532a"), (560, 460, "#fff0b0"))], 0, 0)
    return bg.convert("RGB"), [(0.3, stars(40, 5, 700) if False else L(lambda d: [d.ellipse((x - 3, y - 3, x + 3, y + 3), fill=(255, 250, 220, 220)) for x, y in ((90, 120), (300, 200), (600, 90), (900, 160), (1000, 320), (160, 420))], 0, 0), None), (0.5, bursts, bob(6, 2)), (0, "glow", S.sword_glow(540, 800, 420)), (0.8, L(tl, 8, 6), None), (1.0, ground(1560, "#1a1226"), None), (0, "sparkle", None)]


REG = {"tg_" + k: v for k, v in dict(village=village, boy_lying=boy_lying, giant_shadow=giant_shadow, footprint=footprint, mother_foot=mother_foot, baby=baby, invasion=invasion, king_worry=king_worry, envoy_ride=envoy_ride,
          envoy_arrive=envoy_arrive, boy_speaks=boy_speaks, iron_gear=iron_gear, eating=eating, growing=growing, rice_baskets=rice_baskets, gear_arrive=gear_arrive, stretch=stretch, mount=mount, horse_fire=horse_fire,
          battle=battle, staff_break=staff_break, bamboo=bamboo, bamboo_swing=bamboo_swing, flee=flee, soc_mountain=soc_mountain, fly=fly, king_title=king_title, temple=temple, bamboo_gold=bamboo_gold,
          festival=festival, edict=edict, heritage=heritage, statue=statue, lanterns=lanterns).items()}
