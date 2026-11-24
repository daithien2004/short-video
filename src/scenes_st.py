"""Scenes for Son Tinh - Thuy Tinh. Every scene is its own composition; characters come from chars_st.py / chars_tg.py (king_hung)."""
import math, random
from PIL import Image, ImageDraw
import story2 as S, story3 as X, chars_st as G, chars_tg as K
from story2 import layer, grad, fill_wave, W, H, PAD, CREAM, RED, GOLD, INK, GREEN, EDGE
from scenes_hk2 import L, waves, stars, sway, bob, _peasant, _paddy
from scenes_nt import sky, ground, flame, gate
from scenes_tg import _hut

SEA = ["#3b8aa0", "#2c6f88", "#1f5670"]
DEEP = ["#2a5a8a", "#1f4672", "#16345a"]


def _foam(d, pts, r=26): [d.ellipse((x - r, y - r * .5, x + r, y + r * .5), fill=(255, 255, 255, 230)) for x, y in pts]


def _rain(n=40, seed=5, col=(220, 235, 250, 170)):
    r = random.Random(seed); pts = [(r.uniform(0, W), r.uniform(0, H)) for _ in range(n)]
    return L(lambda d: [d.line([(x, y), (x - 24, y + 80)], fill=col, width=5) for x, y in pts], 0, 0)


def _bolt(d, x, y, col="#fff3a0"):
    d.polygon([(x, y), (x + 60, y + 200), (x + 14, y + 200), (x + 80, y + 440), (x - 40, y + 230), (x + 8, y + 230), (x - 30, y + 60)], fill=col, outline="#e8a020")


def _clouds(d, pts, col):
    for x, y, r in pts: d.ellipse((x - r, y - r * .6, x + r, y + r * .6), fill=col)


def _mtn(d, x, base, w, h, col="#5a8a5a", snow=False):
    d.polygon([(x - w, base), (x, base - h), (x + w, base)], fill=col, outline="#2f5a34"); d.polygon([(x, base - h), (x + w, base), (x + w * .3, base)], fill="#2f5a34")
    if snow: d.polygon([(x, base - h), (x - w * .16, base - h * .8), (x + w * .16, base - h * .8)], fill="#f4f4ee")


def _hall(d, col="#8e1f24"):
    d.rectangle((0, 1560, W, H), fill="#7a5a36"); d.rectangle((0, 540, W, 1560), fill="#d8b86a")
    for x in (120, 960): d.rectangle((x - 40, 480, x + 40, 1560), fill=col, outline="#4a1014"); d.rectangle((x - 56, 440, x + 56, 490), fill=GOLD)
    d.polygon([(0, 540), (W, 540), (W - 120, 400), (120, 400)], fill=col)


# ---------- scene 1 ----------
def palace():
    bg = grad((246, 218, 170), (214, 170, 110)).convert("RGBA")
    hall = L(lambda d: (_hall(d), d.rectangle((300, 1080, 780, 1560), fill="#a8421e", outline="#4a1014"), d.rectangle((260, 1500, 820, 1580), fill=GOLD)), 8, 6)
    pl = L(lambda d: (K.king_hung(d, 400, 1500, 2.5), G.mi_nuong(d, 700, 1580, 2.5)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 380)), (0.5, hall, None), (1.0, pl, bob(2, 1.0))]


def mi_nuong():
    bg = sky((255, 214, 216), (250, 240, 226), (860, 360, 110, (255, 248, 230, 255)))
    lot = L(lambda d: (fill_wave(d, 1500, 12, 240, .4, "#7ac0b0"), [(d.ellipse((x - 150, 1560 - y, x + 150, 1650 - y), fill="#3f9a6a"), [d.polygon([(x, 1560 - y), (x + 36 * k, 1480 - y - 30 * abs(k)), (x + 90 * k, 1560 - y)], fill="#f8a8c0", outline="#c8688a") for k in (-1.4, -.7, 0, .7, 1.4)]) for x, y in ((180, 0), (900, 40), (520, 150))]), 8, 6)
    pl = L(lambda d: G.mi_nuong(d, 540, 1600, 3.8), 10, 8)
    pet = L(lambda d: [d.ellipse((x - 14, y - 8, x + 14, y + 8), fill="#ffd0dc") for x, y in ((200, 500), (420, 760), (700, 580), (880, 900), (300, 1000))], 0, 0)
    return bg.convert("RGB"), [(0.3, S.mountain(1000, 40, 120, 1, "#c8d8c0", False), None), (0.7, lot, None), (1.0, pl, bob(2, 1.0)), (0.9, pet, lambda t: (-30 * (t % 3), 60 * (t % 3)))]


def king_pick():
    bg = grad((70, 40, 60), (160, 90, 70)).convert("RGBA")
    room = L(lambda d: (d.rectangle((0, 1600, W, H), fill="#5a3a26"), d.rectangle((380, 1380, 700, 1620), fill="#8a5a2a", outline=EDGE), d.rectangle((420, 1330, 660, 1390), fill="#efe0b4", outline=EDGE)), 8, 6)
    bub = L(lambda d: (d.ellipse((150, 380, 930, 1000), fill="#fff4e0", outline=EDGE, width=6), [d.ellipse((x - r, y - r, x + r, y + r), fill="#fff4e0", outline=EDGE, width=5) for x, y, r in ((300, 1100, 36), (240, 1190, 22))],
                      d.polygon([(330, 880), (350, 720), (420, 700), (440, 880)], fill="#3a2a3a"), d.ellipse((335, 620, 435, 720), fill="#3a2a3a"), d.polygon([(640, 880), (660, 720), (730, 700), (750, 880)], fill="#3a2a3a"), d.ellipse((645, 620, 745, 720), fill="#3a2a3a"), d.ellipse((520, 560, 580, 620), fill=RED), d.ellipse((540, 580, 600, 640), fill=RED), d.polygon([(500, 590), (560, 700), (620, 590)], fill=RED)), 6, 4)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1200, 360)), (0.5, room, None), (0.8, bub, bob(6, 1.0)), (1.0, L(lambda d: K.king_hung(d, 300, 1620, 2.7), 10, 8), None)]


# ---------- scene 2 ----------
def suitors_arrive():
    bg = sky((250, 230, 190), (200, 220, 220), (540, 420, 100, (255, 246, 220, 255)))
    left = L(lambda d: (_mtn(d, 120, 1500, 380, 560, "#6a9a5a"), _mtn(d, 400, 1500, 300, 380, "#5a8a50")), 8, 6)
    right = L(lambda d: [fill_wave(d, 1480 + 80 * i, 14, 150, i, c) for i, c in enumerate(SEA)], 8, 6)
    pal = L(lambda d: (d.rectangle((420, 1180, 660, 1480), fill="#d8b86a", outline=EDGE), d.polygon([(380, 1190), (700, 1190), (640, 1050), (440, 1050)], fill=RED), d.rectangle((500, 1320, 580, 1480), fill=INK)), 8, 6)
    pl = L(lambda d: (G.son_tinh(d, 190, 1700, 2.3), G.thuy_tinh(d, 900, 1700, 2.3)), 10, 8)
    return bg.convert("RGB"), [(0.3, left, None), (0.5, right, sway(4, .8)), (0.8, pal, None), (1.0, pl, bob(3, 1.4))]


def son_tinh():
    bg = sky((255, 206, 150), (200, 220, 230), (800, 420, 120, (255, 244, 210, 255)))
    pk = L(lambda d: (_mtn(d, 220, 1300, 380, 760, "#7a9a7a", True), _mtn(d, 600, 1300, 460, 960, "#5a8a60", True), _mtn(d, 940, 1300, 360, 640, "#7a9a7a", True)), 10, 8)
    mist = L(lambda d: _clouds(d, ((200, 1200, 220), (700, 1260, 260), (950, 1160, 180)), (255, 255, 255, 150)), 0, 0)
    pl = L(lambda d: (fill_wave(d, 1500, 12, 240, .4, "#4f8a4a"), G.son_tinh(d, 540, 1700, 3.6)), 10, 8)
    return bg.convert("RGB"), [(0.3, pk, None), (0.5, mist, lambda t: (30 * math.sin(t * .6), 0)), (1.0, pl, bob(2, 1.0))]


def thuy_tinh():
    bg = grad((18, 40, 80), (50, 120, 150)).convert("RGBA")
    pl = L(lambda d: (G.thuy_tinh(d, 540, 1640, 3.6), [fill_wave(d, 1500 + 90 * i, 16, 120, i, c) for i, c in enumerate(DEEP)]), 10, 8)
    cl = L(lambda d: _clouds(d, ((200, 360, 200), (800, 300, 240), (540, 520, 180)), (36, 70, 110, 220)), 0, 0)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 420)), (0.3, cl, lambda t: (20 * math.sin(t * .5), 0)), (1.0, pl, bob(2, 1.2)), (0, "sparkle", None)]


def power():
    bg = grad((150, 190, 150), (60, 120, 160)).convert("RGBA")
    mt = L(lambda d: (d.polygon([(0, 0), (W // 2 + 60, 0), (W // 2 - 60, H), (0, H)], fill="#9acb8a"), [G.hill(d, x, 1700, w, h) for x, w, h in ((130, 250, 520), (400, 200, 380))]), 6, 4)
    sea = L(lambda d: (d.polygon([(W // 2 + 60, 0), (W, 0), (W, H), (W // 2 - 60, H)], fill="#2c6f88"), [fill_wave(d, 900 + 160 * i, 20, 100, i, c) for i, c in enumerate(SEA)]), 6, 4)
    pl = L(lambda d: (G.son_tinh(d, 250, 1700, 2.4), G.thuy_tinh(d, 840, 1700, 2.4)), 10, 8)
    return bg.convert("RGB"), [(0.3, mt, None), (0.4, sea, sway(8, 1.2)), (1.0, pl, bob(3, 1.0)), (0, "sparkle", None)]


# ---------- scene 3 ----------
def king_dilemma():
    bg = grad((30, 24, 50), (90, 50, 70)).convert("RGBA")
    room = L(lambda d: (_hall(d, "#6a1a24"), [(d.line([(x, 560), (x, 700)], fill="#3a2a1c", width=6), d.ellipse((x - 40, 700, x + 40, 800), fill="#e8402a", outline=GOLD)) for x in (300, 780)]), 8, 6)
    pl = L(lambda d: (K.king_hung(d, 540, 1560, 2.4), G.son_tinh(d, 150, 1640, 2.0, staff=False), G.thuy_tinh(d, 930, 1640, 2.0, trident=False)), 10, 8)
    return bg.convert("RGB"), [(0.5, room, None), (0, "glow", S.sword_glow(540, 800, 380)), (1.0, pl, bob(2, 1.0))]


def _gift_bg(c0, c1): return grad(c0, c1).convert("RGBA")


def gift_elephant():
    bg = sky((255, 224, 170), (190, 220, 190), (200, 360, 100, (255, 246, 220, 255)))
    pl = L(lambda d: (fill_wave(d, 1460, 12, 240, .4, "#6aa44e"), G.elephant(d, 470, 1580, 2.2), d.polygon([(420, 1260), (520, 1260), (540, 1340), (400, 1340)], fill=RED, outline=GOLD)), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1060, 40, 110, 2, "#a4c8a8", False), None), (1.0, pl, bob(3, 1.0)), (0, "sparkle", None)]


def gift_rooster():
    bg = grad((255, 214, 150), (240, 170, 120)).convert("RGBA")
    pl = L(lambda d: (fill_wave(d, 1560, 12, 240, .4, "#8a6a3a"), G.rooster(d, 600, 1640, 3.2), [d.polygon([(x, 1560), (x + 20, 1500), (x + 40, 1560)], fill="#6aa44e") for x in (80, 140, 880, 940)]), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(500, 1100, 380)), (1.0, pl, bob(4, 1.6)), (0, "sparkle", None)]


def gift_horse():
    bg = sky((170, 214, 236), (240, 240, 210), (900, 300, 100, (255, 248, 220, 255)))
    pl = L(lambda d: (fill_wave(d, 1500, 12, 240, .4, "#7ab05a"), G.horse9(d, 440, 1640, 2.0)), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1000, 40, 110, 3, "#b8d4b0", False), None), (0.8, _paddy(1250, ["#9fd078", "#86bc62", "#6aa44e"], 3), None), (1.0, pl, bob(3, 1.2))]


# ---------- scene 4 ----------
def dawn_gifts():
    bg = sky((250, 150, 110), (255, 226, 176), (200, 640, 140, (255, 240, 200, 255)))
    road = L(lambda d: (fill_wave(d, 1500, 10, 240, .4, "#a8793c"), d.rectangle((760, 1000, 1040, 1500), fill="#d8b86a", outline=EDGE), d.polygon([(730, 1010), (1070, 1010), (1000, 880), (800, 880)], fill=RED)), 8, 6)
    pl = L(lambda d: (G.son_tinh(d, 150, 1640, 1.7), G.elephant(d, 480, 1620, 1.0), G.rooster(d, 700, 1620, 1.0), G.horse9(d, 940, 1620, 0.9)), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0.3, S.mountain(1080, 40, 110, 2, "#c88a6a", False), None), (0.7, road, None), (1.0, pl, bob(3, 2.0))]


def wedding():
    bg = grad((120, 24, 36), (214, 130, 60)).convert("RGBA")
    room = L(lambda d: (_hall(d, "#a8241e"), [d.ellipse((x - 46, 620, x + 46, 740), fill="#e8402a", outline=GOLD) for x in (230, 540, 850)], [d.line([(x, 560), (x, 620)], fill=GOLD, width=5) for x in (230, 540, 850)]), 8, 6)
    pl = L(lambda d: (K.king_hung(d, 540, 1560, 2.4), G.mi_nuong(d, 170, 1620, 2.5), G.son_tinh(d, 890, 1620, 2.1)), 10, 8)
    return bg.convert("RGB"), [(0.5, room, None), (0, "glow", S.sword_glow(540, 900, 380)), (1.0, pl, bob(2, 1.0)), (0, "sparkle", None)]


def to_mountain():
    bg = sky((255, 170, 120), (230, 190, 200), (820, 460, 120, (255, 234, 190, 255)))
    mt = L(lambda d: (d.polygon([(-60, H), (80, 1000), (260, 700), (430, 480), (560, 440), (680, 520), (900, 900), (1140, H)], fill="#5a8a5a", outline="#2f5a34"), d.polygon([(560, 440), (680, 520), (900, 900), (1140, H), (700, H)], fill="#3f7040"), d.line([(120, 1650), (320, 1400), (260, 1180), (470, 960), (440, 780)], fill="#d8c08a", width=30)), 10, 8)
    mist = L(lambda d: _clouds(d, ((300, 1100, 200), (800, 1300, 240), (560, 800, 180)), (255, 255, 255, 140)), 0, 0)
    pl = L(lambda d: (G.son_tinh(d, 330, 1440, 0.9), G.mi_nuong(d, 430, 1330, 0.9)), 10, 8)
    return bg.convert("RGB"), [(0.3, mt, None), (0.6, mist, lambda t: (40 * math.sin(t * .5), 0)), (1.0, pl, None)]


# ---------- scene 5 ----------
def late_arrival():
    bg = grad((60, 70, 110), (190, 120, 100)).convert("RGBA")
    pal = L(lambda d: (d.rectangle((0, 1560, W, H), fill="#5a4a3a"), gate(d, 760, 1560, 1.7)), 8, 6)
    pl = L(lambda d: (G.thuy_tinh(d, 250, 1700, 2.4), G.cua_tuong(d, 480, 1700, 1.8), G.tom_binh(d, 100, 1720, 1.6), d.rectangle((420, 1480, 560, 1560), fill="#8a5a2a", outline=EDGE)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(760, 1300, 360)), (0.6, pal, None), (1.0, pl, bob(2, 1.2))]


def angry():
    bg = grad((30, 14, 40), (150, 40, 50)).convert("RGBA")
    sk = L(lambda d: (_clouds(d, ((220, 300, 240), (800, 240, 260), (540, 460, 200)), (30, 20, 50, 235)), _bolt(d, 150, 480), _bolt(d, 860, 520)), 0, 0)
    pl = L(lambda d: (G.thuy_tinh(d, 540, 1700, 4.0, trident=False),), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 460)), (0.3, sk, None), (1.0, pl, bob(2, 3.0)), (0, "sparkle", None)]


def summon():
    bg = grad((20, 30, 60), (70, 100, 130)).convert("RGBA")
    cl = L(lambda d: _clouds(d, ((200, 260, 260), (700, 200, 300), (980, 380, 220), (440, 480, 220)), (24, 34, 60, 240)), 0, 0)
    sea = L(lambda d: (fill_wave(d, 1100, 90, 110, .6, "#2c6f88"), fill_wave(d, 1300, 70, 90, 1.4, "#1f5670"), fill_wave(d, 1500, 40, 80, 2.2, "#16345a")), 8, 6)
    top = L(lambda d: (d.polygon([(300, 1500), (540, 1000), (780, 1500)], fill="#2c6f88"), G.thuy_tinh(d, 540, 1040, 1.9)), 10, 8)
    return bg.convert("RGB"), [(0.3, cl, lambda t: (-20 * (t % 4), 0)), (0.7, sea, sway(12, 1.4)), (1.0, top, bob(4, 1.5)), (0.9, _rain(60), lambda t: (-40 * (t % 1), 160 * (t % 1)))]


# ---------- scene 6 ----------
def flood_fields():
    bg = grad((130, 140, 150), (190, 190, 180)).convert("RGBA")
    fld = L(lambda d: (d.rectangle((0, 1150, W, H), fill="#7ab0c0"), [d.line([(x, 1150 + (x % 90)), (x + 8, 1090 + (x % 90))], fill="#6aa44e", width=6) for x in range(20, W, 46)], [fill_wave(d, 1400 + 110 * i, 18, 120, i, c) for i, c in enumerate(("#8ac0d0", "#6aa8bc", "#4a88a0"))]), 8, 6)
    pl = L(lambda d: (d.line([(160, 1700), (160, 1320)], fill="#5a3e26", width=10), d.polygon([(100, 1320), (220, 1320), (160, 1250)], fill="#d8b86a"), d.rectangle((560, 1540, 760, 1580), fill="#8a5a2a")), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1050, 40, 110, 2, "#9aaa98", False), None), (0.7, fld, sway(6, 1.0)), (1.0, pl, None), (0.9, _rain(40, 7), lambda t: (-40 * (t % 1), 160 * (t % 1)))]


def flood_houses():
    bg = grad((90, 100, 120), (170, 170, 170)).convert("RGBA")
    hs = L(lambda d: (_hut(d, 120, 1500, 340, 200), _hut(d, 620, 1560, 300, 180)), 8, 6)
    water = L(lambda d: [fill_wave(d, 1450 + 100 * i, 16, 120, i, c) for i, c in enumerate(("#6a98a8", "#4a7a90", "#2a5a78"))], 8, 6)
    pp = L(lambda d: (_peasant(d, 300, 1300, 1.0, 0, "#c8372d"), _peasant(d, 760, 1370, 1.0, 0, "#2f6a8a")), 10, 8)
    return bg.convert("RGB"), [(0.6, hs, None), (0.8, pp, bob(2, 1.5)), (1.0, water, sway(8, 1.2)), (0.9, _rain(50, 9), lambda t: (-40 * (t % 1), 160 * (t % 1)))]


def water_mountain():
    bg = grad((70, 70, 100), (150, 120, 120)).convert("RGBA")
    mt = L(lambda d: (_mtn(d, 540, 1380, 480, 980, "#5a8a5a", True), _mtn(d, 160, 1400, 220, 360, "#4f7a50")), 10, 8)
    sea = L(lambda d: (fill_wave(d, 1250, 50, 100, .6, "#2c6f88"), fill_wave(d, 1420, 60, 90, 1.4, "#1f5670"), fill_wave(d, 1600, 44, 80, 2.2, "#16345a"), _foam(d, [(150, 1250), (420, 1290), (760, 1230), (980, 1280), (300, 1440), (880, 1450)])), 8, 6)
    return bg.convert("RGB"), [(0.5, mt, None), (1.0, sea, sway(14, 1.4)), (0.9, _rain(50, 11), lambda t: (-40 * (t % 1), 160 * (t % 1)))]


def crab_army():
    bg = grad((14, 30, 60), (60, 110, 140)).convert("RGBA")
    sea = L(lambda d: [fill_wave(d, 1100 + 150 * i, 24, 100, i, c) for i, c in enumerate(DEEP)], 8, 6)
    ar = L(lambda d: ([G.tom_binh(d, x, 1500 + (x % 3) * 20, 1.2) for x in (120, 340, 560, 780)], [G.cua_tuong(d, x, 1640, 1.4) for x in (230, 450, 670, 900)], [G.tom_binh(d, x, 1790, 1.7) for x in (160, 520, 880)]), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 600, 400)), (0.6, sea, sway(10, 1.0)), (1.0, ar, bob(4, 3.0))]


# ---------- scene 7 ----------
def son_calm():
    bg = grad((60, 50, 70), (150, 100, 90)).convert("RGBA")
    pl = L(lambda d: (G.son_tinh(d, 540, 1600, 3.9), [fill_wave(d, 1560 + 60 * i, 14, 110, i, c) for i, c in enumerate(("#2c6f88", "#1f5670"))]), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 420)), (0.3, S.mountain(1050, 50, 110, 4, "#4a5a6a", False), None), (1.0, pl, None), (0.9, _rain(40, 13), lambda t: (-40 * (t % 1), 160 * (t % 1)))]


def lift_hill():
    bg = grad((80, 70, 100), (200, 140, 110)).convert("RGBA")
    hl = L(lambda d: (G.hill(d, 540, 700, 330, 360, "#6a9a5a"), [d.polygon([(x, 700), (x + 14, 600), (x + 28, 700)], fill="#3f7d3a") for x in (440, 520, 600)]), 10, 8)
    pl = L(lambda d: (d.line([(420, 1180), (360, 720)], fill="#e8c8a0", width=26), d.line([(660, 1180), (720, 720)], fill="#e8c8a0", width=26), G.son_tinh(d, 540, 1640, 3.3, staff=False)), 10, 8)
    dust = L(lambda d: [d.ellipse((x - r, y - r * .6, x + r, y + r * .6), fill=(200, 170, 140, 170)) for x, y, r in ((200, 1640, 120), (860, 1650, 130))], 0, 0)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 700, 400)), (0.6, hl, bob(8, 1.2)), (1.0, pl, None), (0.9, dust, lambda t: (0, -10 * (t % 2)))]


def block_water():
    bg = grad((90, 100, 120), (180, 150, 130)).convert("RGBA")
    wl = L(lambda d: [G.hill(d, x, 1500, 200, h) for x, h in ((100, 520), (330, 640), (560, 560), (790, 680), (1010, 520))], 10, 8)
    sea = L(lambda d: (fill_wave(d, 1420, 80, 90, .6, "#2c6f88"), fill_wave(d, 1560, 50, 100, 1.4, "#1f5670"), _foam(d, [(80, 1400), (320, 1380), (560, 1410), (800, 1390), (1000, 1400)], 34)), 8, 6)
    return bg.convert("RGB"), [(0.3, S.mountain(900, 30, 100, 5, "#7a8a88", False), None), (0.6, wl, None), (1.0, sea, sway(20, 1.6)), (0.9, _rain(40, 15), lambda t: (-40 * (t % 1), 160 * (t % 1)))]


def hills_rise():
    bg = grad((120, 150, 170), (230, 220, 190)).convert("RGBA")
    hl = L(lambda d: (G.hill(d, 220, 1500, 250, 520, "#5a8a5a"), G.hill(d, 560, 1500, 280, 820, "#4f7a50"), G.hill(d, 900, 1500, 240, 1200, "#5a8a5a"), G.son_tinh(d, 900, 300, 0.8)), 10, 8)
    water = L(lambda d: (fill_wave(d, 1440, 20, 120, .6, "#3b8aa0"), [d.line([(0, y), (W, y)], fill=(255, 255, 255, 200), width=5) for y in (1240, 1020)], fill_wave(d, 1580, 20, 120, 1.4, "#2c6f88")), 8, 6)
    return bg.convert("RGB"), [(0.6, hl, None), (1.0, water, sway(10, 1.2))]


# ---------- scene 8 ----------
def clash():
    bg = grad((40, 20, 50), (200, 90, 70)).convert("RGBA")
    mid = L(lambda d: (_bolt(d, 500, 300), [d.polygon([(x, y), (x + 70, y - 50), (x + 120, y + 20), (x + 60, y + 70)], fill="#7a7a78", outline="#3a3a38") for x, y in ((400, 1000), (560, 1200), (440, 1400))], fill_wave(d, 1500, 60, 100, .8, "#2c6f88")), 8, 6)
    pl = L(lambda d: (G.son_tinh(d, 170, 1700, 2.6), G.thuy_tinh(d, 910, 1700, 2.6)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 700, 420)), (0.8, mid, sway(10, 2.0)), (1.0, pl, bob(5, 3.0)), (0, "sparkle", None)]


def tired():
    bg = grad((30, 30, 50), (80, 80, 100)).convert("RGBA")
    wv = L(lambda d: (fill_wave(d, 1500, 14, 240, .8, "#1f4672"), fill_wave(d, 1640, 10, 240, 1.6, "#16345a")), 8, 6)
    pl = L(lambda d: (G.thuy_tinh(d, 540, 1600, 3.0, trident=False), d.line([(760, 1620), (940, 1300)], fill=GOLD, width=14), d.polygon([(900, 1300), (980, 1300), (940, 1240)], fill=GOLD)), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1000, 40, 110, 3, "#2a3a4a", False), None), (1.0, pl, bob(2, .8)), (0.9, wv, sway(6, 1.0))]


def retreat():
    bg = sky((250, 170, 130), (255, 226, 176), (860, 500, 130, (255, 240, 200, 255)))
    sea = L(lambda d: [fill_wave(d, 1000 + 110 * i, 22, 110, i, c) for i, c in enumerate(SEA + ["#16345a"])], 8, 6)
    ar = L(lambda d: ([G.tom_binh(d, x, 1500, 1.0) for x in (200, 420)], [G.cua_tuong(d, x, 1560, 1.2) for x in (620, 820)], G.thuy_tinh(d, 940, 1480, 1.6, trident=False)), 10, 8)
    return bg.convert("RGB"), [(0.5, sea, sway(12, 1.0)), (1.0, ar, bob(3, 2.0))]


# ---------- scene 9 ----------
def vow():
    bg = grad((24, 10, 30), (120, 30, 40)).convert("RGBA")
    mt = L(lambda d: (_mtn(d, 800, 1300, 420, 900, "#1a1a2a"), _mtn(d, 1040, 1300, 260, 500, "#22223a")), 10, 8)
    pl = L(lambda d: (G.thuy_tinh(d, 340, 1560, 3.1), fill_wave(d, 1440, 24, 110, .6, "#16345a"), fill_wave(d, 1600, 30, 110, 1.4, "#0e2444")), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(300, 900, 380)), (0.3, mt, None), (1.0, pl, bob(2, 1.0)), (0.9, _rain(30, 17), lambda t: (-40 * (t % 1), 160 * (t % 1)))]


def every_year():
    bg = grad((70, 80, 100), (150, 150, 150)).convert("RGBA")
    post = L(lambda d: (d.rectangle((460, 500, 620, 1700), fill="#8a5a2a", outline=EDGE), [d.line([(460, y), (540 if i % 2 else 600, y)], fill="#efe0b4", width=8) for i, y in enumerate(range(560, 1680, 70))]), 8, 6)
    wat = L(lambda d: (d.rectangle((0, 760, W, H), fill=(60, 120, 150, 200)), fill_wave(d, 760, 24, 100, .6, "#3b8aa0"), d.polygon([(380, 770), (460, 740), (380, 710)], fill=RED), d.line([(300, 740), (380, 740)], fill=RED, width=8)), 8, 6)
    cl = L(lambda d: _clouds(d, ((200, 260, 260), (800, 200, 300), (520, 420, 220)), (40, 50, 70, 235)), 0, 0)
    return bg.convert("RGB"), [(0.3, cl, lambda t: (20 * math.sin(t * .5), 0)), (0.8, post, None), (1.0, wat, sway(8, 1.2)), (0.9, _rain(60, 19), lambda t: (-40 * (t % 1), 160 * (t % 1)))]


def loses():
    bg = sky((170, 214, 236), (250, 236, 200), (200, 340, 100, (255, 248, 220, 255)))
    rb = L(lambda d: [d.arc((120 - 40 * i, 560 - 40 * i, 960 + 40 * i, 1400 + 40 * i), 180, 360, fill=c, width=26) for i, c in enumerate(("#e8532a", "#f2b632", "#6aa44e", "#3b8aa0"))], 0, 0)
    mt = L(lambda d: (_mtn(d, 300, 1450, 520, 880, "#5a8a5a", True), d.polygon([(-60, 1450), (W + 60, 1450), (W + 60, 1520), (-60, 1520)], fill="#3b8aa0"), G.son_tinh(d, 300, 640, 0.9)), 10, 8)
    ebb = L(lambda d: (fill_wave(d, 1560, 16, 120, .6, "#3b8aa0"), fill_wave(d, 1700, 16, 120, 1.4, "#2c6f88"), d.polygon([(760, 1560), (1100, 1380), (1100, 1560)], fill="#4a88a0")), 8, 6)
    return bg.convert("RGB"), [(0.3, rb, None), (0.6, mt, None), (1.0, ebb, sway(10, .8)), (0, "sparkle", None)]


# ---------- scene 10 ----------
def river_rise():
    bg = grad((120, 120, 130), (210, 190, 170)).convert("RGBA")
    rv = L(lambda d: (d.polygon([(0, 1100), (W, 900), (W, 1500), (0, 1700)], fill="#b0703a", outline="#6a3a1a"), fill_wave(d, 1250, 20, 100, 1.0, "#c88a50"), fill_wave(d, 1450, 20, 100, 2.0, "#a86a34")), 8, 6)
    bank = L(lambda d: (fill_wave(d, 1640, 10, 240, .4, "#6a9a4a"), _hut(d, 560, 1780, 240, 140), [_peasant(d, x, 1780, 1.0, 0, c) for x, c in ((200, "#c8372d"), (340, "#2f6a8a"))]), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(900, 30, 110, 5, "#9aa89a", False), None), (0.8, rv, sway(10, 1.0)), (1.0, bank, None), (0.9, _rain(50, 21), lambda t: (-40 * (t % 1), 160 * (t % 1)))]


def dike():
    bg = sky((255, 220, 170), (200, 220, 200), (860, 380, 110, (255, 246, 220, 255)))
    dk = L(lambda d: (d.polygon([(-60, 1500), (200, 1260), (880, 1260), (1140, 1500), (1140, H), (-60, H)], fill="#8a6a3a", outline="#5a3e26"), fill_wave(d, 1200, 10, 240, .4, "#6a9a4a"), [_peasant(d, x, 1560 + (x % 5), 1.3, 1, c) for x, c in ((260, "#c8372d"), (560, "#2f6a8a"), (860, "#6a8a3a"))]), 10, 8)
    soil = L(lambda d: [d.ellipse((x - 70, 1700, x + 70, 1780), fill="#6a4a2a") for x in (150, 540, 930)], 6, 4)
    return bg.convert("RGB"), [(0.3, S.mountain(1000, 40, 110, 2, "#a4c8a8", False), None), (1.0, dk, bob(2, 2.0)), (1.0, soil, None)]


def delta():
    bg = grad((200, 226, 200), (150, 200, 140)).convert("RGBA")
    pat = L(lambda d: ([d.polygon([(x, y), (x + 200, y + 20), (x + 220, y + 190), (x - 10, y + 170)], fill=c) for x, y, c in ((40, 300, "#9fd078"), (300, 280, "#c8d870"), (560, 320, "#86bc62"), (820, 290, "#d8e090"), (60, 560, "#c8d870"), (320, 600, "#9fd078"), (580, 560, "#d8e090"), (840, 580, "#86bc62"), (50, 860, "#86bc62"), (310, 880, "#d8e090"), (570, 850, "#9fd078"), (830, 880, "#c8d870"))],
                     d.line([(540, 0), (500, 400), (620, 800), (520, 1200), (640, 1600), (580, H)], fill="#b0703a", width=70), d.line([(500, 400), (200, 760), (160, 1200)], fill="#b0703a", width=36), d.line([(620, 800), (900, 1100), (940, 1500)], fill="#b0703a", width=36)), 8, 6)
    return bg.convert("RGB"), [(1.0, pat, None), (0, "sparkle", None)]


# ---------- scene 11 ----------
def bavi():
    bg = sky((255, 190, 150), (210, 220, 230), (200, 440, 120, (255, 240, 200, 255)))
    pk = L(lambda d: (_mtn(d, 220, 1400, 330, 760, "#6a8a8a", True), _mtn(d, 560, 1400, 420, 1020, "#4f7a60", True), _mtn(d, 890, 1400, 300, 700, "#6a8a8a", True)), 10, 8)
    mist = L(lambda d: _clouds(d, ((240, 1100, 260), (760, 1180, 300), (540, 900, 200)), (255, 255, 255, 170)), 0, 0)
    fl = L(lambda d: (fill_wave(d, 1560, 12, 240, .4, "#6aa44e"), fill_wave(d, 1700, 12, 240, 1.2, "#549040")), 8, 6)
    return bg.convert("RGB"), [(0.3, pk, None), (0.5, mist, lambda t: (30 * math.sin(t * .5), 0)), (1.0, fl, None)]


def st_temple():
    bg = grad((255, 226, 176), (200, 220, 200)).convert("RGBA")
    tp = L(lambda d: (d.polygon([(260, 1700), (820, 1700), (700, 1100), (380, 1100)], fill="#a09a8c", outline="#4a463e"), [d.line([(300 + i * 4, 1700 - i * 60), (780 - i * 4, 1700 - i * 60)], fill="#6a665a", width=6) for i in range(1, 9)],
                      d.rectangle((300, 800, 780, 1100), fill=CREAM, outline=EDGE), d.polygon([(220, 810), (860, 810), (740, 640), (340, 640)], fill=RED), d.polygon([(220, 810), (260, 850), (820, 850), (860, 810)], fill="#8e2018"), d.rectangle((480, 910, 600, 1100), fill=INK)), 10, 8)
    tr = L(lambda d: [(d.rectangle((x - 18, 1100, x + 18, 1700), fill="#5a3e26"), d.ellipse((x - 150, 860, x + 150, 1200), fill="#3f8a5e")) for x in (110, 970)], 8, 6)
    sm = L(lambda d: [d.ellipse((x - r, y - r, x + r, y + r), fill=(230, 230, 230, 150)) for x, y, r in ((540, 700, 50), (560, 580, 70), (540, 440, 90))], 0, 0)
    return bg.convert("RGB"), [(0.3, S.mountain(1000, 50, 110, 3, "#a4c8a8", False), None), (0.6, tr, sway(3, 1.0)), (0.8, tp, None), (0.5, sm, lambda t: (10 * math.sin(t), -20 * (t % 2))), (0, "sparkle", None)]


REG = {"st_" + k: v for k, v in dict(palace=palace, mi_nuong=mi_nuong, king_pick=king_pick, suitors_arrive=suitors_arrive, son_tinh=son_tinh, thuy_tinh=thuy_tinh, power=power, king_dilemma=king_dilemma,
          gift_elephant=gift_elephant, gift_rooster=gift_rooster, gift_horse=gift_horse, dawn_gifts=dawn_gifts, wedding=wedding, to_mountain=to_mountain, late_arrival=late_arrival, angry=angry, summon=summon,
          flood_fields=flood_fields, flood_houses=flood_houses, water_mountain=water_mountain, crab_army=crab_army, son_calm=son_calm, lift_hill=lift_hill, block_water=block_water, hills_rise=hills_rise,
          clash=clash, tired=tired, retreat=retreat, vow=vow, every_year=every_year, loses=loses, river_rise=river_rise, dike=dike, delta=delta, bavi=bavi, temple=st_temple).items()}
