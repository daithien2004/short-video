"""Scenes for Mai An Tiem. Every scene is its own composition; characters come from chars_ma.py / chars_tg.py (king_hung)."""
import math, random
import story2 as S, story3 as X, chars_ma as M, chars_tg as K
from story2 import layer, grad, fill_wave, W, H, PAD, CREAM, RED, GOLD, INK, GREEN, EDGE
from scenes_hk2 import L, waves, stars, sway, bob, _peasant
from scenes_nt import sky, ground
from scenes_st import _mtn, _clouds, _rain, _foam, _hall, SEA, DEEP

SAND = "#e8d49a"


def _sea(y, n=3, cols=SEA, amp=14): return L(lambda d: [fill_wave(d, y + 110 * i, amp, 110, i, c) for i, c in enumerate(cols[:n])], 8, 6)


def _island(d, cx, base, w, col=SAND): d.polygon([(cx - w, base + 60), (cx - w * .7, base - 30), (cx - w * .2, base - 60), (cx + w * .3, base - 50), (cx + w * .8, base - 20), (cx + w, base + 60)], fill=col, outline="#a8905a")


def _palm(d, x, base, h=420, lean=40):
    d.polygon([(x - 14, base), (x + 14, base), (x + 8 + lean, base - h), (x - 8 + lean, base - h)], fill="#8a6a3a", outline="#5a3e26")
    for a in (-150, -110, -70, -30): r = math.radians(a); d.polygon([(x + lean, base - h), (x + lean + 150 * math.cos(r), base - h + 90 * math.sin(r) + 50), (x + lean + 60 * math.cos(r + .5), base - h + 20)], fill="#3f9a4a", outline="#1f5a28")


def _slice(d, x, y, s=1.0, ang=0):
    pts = [(x - 40 * s, y), (x + 40 * s, y), (x, y + 60 * s)]; d.polygon(pts, fill="#e8403a", outline="#3f9a4a"); d.line([(x - 40 * s, y), (x + 40 * s, y)], fill="#3f9a4a", width=max(int(8 * s), 3))
    for dx in (-14, 8): d.ellipse((x + dx * s - 3, y + 14 * s, x + dx * s + 3, y + 22 * s), fill="#16121a")


# ---------- 1 ----------
def court():
    bg = grad((246, 218, 170), (214, 170, 110)).convert("RGBA")
    hall = L(lambda d: (_hall(d), d.rectangle((560, 1100, 1000, 1560), fill="#a8421e", outline="#4a1014")), 8, 6)
    chest = L(lambda d: (d.rectangle((60, 1500, 300, 1620), fill="#8a5a2a", outline=EDGE), d.polygon([(60, 1500), (300, 1500), (270, 1440), (90, 1440)], fill=GOLD, outline=EDGE)), 8, 6)
    pl = L(lambda d: (K.king_hung(d, 760, 1560, 2.4), M.an_tiem(d, 330, 1620, 2.5)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 380)), (0.5, hall, None), (0.8, chest, None), (1.0, pl, bob(2, 1.0))]


def home():
    bg = grad((255, 230, 180), (230, 190, 130)).convert("RGBA")
    rm = L(lambda d: (d.rectangle((0, 1560, W, H), fill="#7a5a36"), d.rectangle((0, 560, W, 1560), fill="#d8b86a"), [d.rectangle((x - 34, 500, x + 34, 1560), fill="#8e1f24", outline="#4a1014") for x in (90, 990)],
                      d.rectangle((140, 1360, 440, 1560), fill="#8a5a2a", outline=EDGE), [d.ellipse((190 + i * 70, 1320 - (i % 2) * 20, 250 + i * 70, 1380), fill=GOLD, outline="#8a6a20") for i in range(3)],
                      d.polygon([(620, 1560), (680, 1380), (860, 1380), (920, 1560)], fill="#efe0b4", outline=EDGE), d.rectangle((640, 1200, 700, 1560), fill="#c8372d"), d.rectangle((720, 1240, 780, 1560), fill="#2f6a8a"), d.rectangle((800, 1220, 860, 1560), fill="#e8a030")), 8, 6)
    pl = L(lambda d: (M.an_tiem(d, 540, 1700, 2.0), M.vo(d, 380, 1720, 1.9), M.con(d, 700, 1720, 1.7)), 10, 8)
    return bg.convert("RGB"), [(0.6, rm, None), (1.0, pl, bob(2, 1.2))]


def family():
    bg = sky((255, 214, 216), (200, 232, 200), (860, 340, 110, (255, 248, 230, 255)))
    gr = L(lambda d: (fill_wave(d, 1480, 14, 240, .4, "#6aa44e"), [d.ellipse((x - 26, y - 20, x + 26, y + 20), fill=c) for x, y, c in ((120, 1560, "#f2b632"), (260, 1620, "#e8a0b8"), (900, 1580, "#f2b632"), (990, 1640, "#e8a0b8"), (700, 1700, "#fff"))]), 8, 6)
    pl = L(lambda d: (M.vo(d, 270, 1720, 2.8), M.an_tiem(d, 560, 1720, 3.1), M.con(d, 840, 1720, 2.6)), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1000, 40, 120, 1, "#c8d8c0", False), None), (0.7, gr, None), (1.0, pl, bob(3, 1.0))]


# ---------- 2 ----------
def boast():
    bg = grad((255, 200, 140), (230, 120, 80)).convert("RGBA")
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#7a5a36"), M.an_tiem(d, 540, 1700, 3.9), d.line([(640, 1180), (760, 960)], fill="#e8c8a0", width=30)), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 900, 440)), (1.0, pl, bob(2, 1.4)), (0, "sparkle", None)]


def informer():
    bg = grad((30, 24, 50), (80, 50, 70)).convert("RGBA")
    pil = L(lambda d: (d.rectangle((0, 400, 300, H), fill="#6a1a24", outline="#2a0a10"), d.rectangle((260, 400, 340, H), fill=GOLD)), 8, 6)
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#3a2a2a"), M.courtier(d, 700, 1720, 3.7)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(760, 900, 360)), (0.6, pil, None), (1.0, pl, bob(2, .9))]


def tell_king():
    bg = grad((70, 30, 40), (170, 90, 60)).convert("RGBA")
    rm = L(lambda d: (_hall(d, "#6a1a24"), d.rectangle((520, 1100, 1000, 1560), fill="#a8421e", outline="#4a1014")), 8, 6)
    pl = L(lambda d: (K.king_hung(d, 780, 1560, 2.5), M.courtier(d, 230, 1680, 2.4)), 10, 8)
    return bg.convert("RGB"), [(0.5, rm, None), (0, "glow", S.sword_glow(780, 800, 360)), (1.0, pl, bob(2, 1.0))]


# ---------- 3 ----------
def angry_king():
    bg = grad((40, 10, 30), (180, 40, 40)).convert("RGBA")
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#3a1418"), K.king_hung(d, 540, 1700, 3.9)), 10, 8)
    sp = L(lambda d: [d.polygon([(x, y), (x + 40, y - 120), (x + 80, y)], fill="#e8402a") for x, y in ((100, 700), (880, 760), (60, 1100), (940, 1160))], 0, 0)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 900, 460)), (0.5, sp, bob(10, 3.0)), (1.0, pl, bob(2, 3.0))]


def exile_boat():
    bg = sky((250, 200, 170), (200, 220, 230), (200, 500, 110, (255, 244, 214, 255)))
    sh = L(lambda d: (fill_wave(d, 1380, 12, 240, .4, "#8a6a3a"), M.hut(d, 40, 1380, 200, 120)), 8, 6)
    bt = L(lambda d: (M.boat(d, 600, 1480, 1.8), M.an_tiem(d, 520, 1440, 1.1), M.vo(d, 640, 1440, 1.0), M.con(d, 740, 1440, 1.0)), 10, 8)
    return bg.convert("RGB"), [(0.4, sh, None), (0.7, _sea(1400), sway(10, 1.0)), (1.0, bt, bob(6, 1.2)), (0.9, _sea(1600, 2, DEEP), sway(14, 1.2))]


def island_arrive():
    bg = sky((255, 220, 170), (190, 226, 230), (860, 420, 120, (255, 246, 220, 255)))
    isl = L(lambda d: (_island(d, 540, 1500, 700), _palm(d, 760, 1480, 480, 60)), 10, 8)
    pl = L(lambda d: (M.an_tiem(d, 400, 1600, 1.5), M.vo(d, 520, 1610, 1.4), M.con(d, 620, 1620, 1.3)), 10, 8)
    bt = L(lambda d: M.boat(d, 160, 1260, .8), 8, 6)
    return bg.convert("RGB"), [(0.5, _sea(1250, 2), sway(10, 1.0)), (0.6, bt, bob(4, 1.0)), (0.8, isl, None), (1.0, pl, bob(2, 1.4)), (0.9, _sea(1760, 2, DEEP), sway(10, 1.0))]


# ---------- 4 ----------
def island_empty():
    bg = sky((255, 190, 140), (190, 214, 236), (800, 500, 130, (255, 240, 200, 255)))
    isl = L(lambda d: (_island(d, 540, 1520, 420), _palm(d, 380, 1500, 300, 30)), 10, 8)
    tiny = L(lambda d: (M.an_tiem(d, 520, 1560, .55), M.vo(d, 600, 1565, .5), M.con(d, 660, 1570, .5)), 10, 8)
    return bg.convert("RGB"), [(0.4, _sea(1350, 3), sway(14, .8)), (0.8, isl, None), (1.0, tiny, None), (0.9, _sea(1700, 2, DEEP), sway(10, 1.0))]


def food_low():
    bg = grad((90, 70, 70), (170, 130, 100)).convert("RGBA")
    jar = L(lambda d: (d.rectangle((0, 1560, W, H), fill="#c8a870"), d.ellipse((260, 1100, 820, 1600), fill="#9a5a30", outline="#4a2a14"), d.ellipse((330, 1060, 750, 1180), fill="#3a1e10", outline="#4a2a14"), [d.ellipse((x - 8, y - 5, x + 8, y + 5), fill="#f2efe4") for x, y in ((470, 1130), (540, 1120), (610, 1135), (400, 1700), (700, 1690), (560, 1740))]), 10, 8)
    kid = L(lambda d: (M.con(d, 140, 1700, 2.2), M.vo(d, 940, 1720, 2.2)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1200, 380)), (0.9, jar, None), (1.0, kid, bob(2, .8))]


def resolve():
    bg = sky((255, 160, 110), (255, 226, 176), (540, 760, 160, (255, 240, 200, 255)))
    pl = L(lambda d: (fill_wave(d, 1560, 12, 240, .4, SAND), M.an_tiem(d, 460, 1700, 3.6)), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0.5, _sea(1180, 3), sway(10, 1.0)), (1.0, pl, bob(2, 1.0))]


# ---------- 5 ----------
def birds():
    bg = sky((255, 180, 120), (180, 206, 236), (200, 700, 140, (255, 240, 200, 255)))
    fl = L(lambda d: [M.gull(d, x, y, s_, 1, k % 2 == 0) for k, (x, y, s_) in enumerate(((700, 640, 2.4), (420, 820, 1.9), (880, 900, 1.6), (240, 600, 1.4), (560, 1060, 1.2), (150, 1000, 1.1)))], 6, 4)
    return bg.convert("RGB"), [(0.3, _clouds_layer(), lambda t: (-20 * (t % 4), 0)), (0.8, fl, lambda t: (30 * math.sin(t * .8), 14 * math.sin(t * 1.6))), (0.6, _sea(1500, 3), sway(10, 1.0))]


def _clouds_layer(): return L(lambda d: _clouds(d, ((200, 400, 200), (800, 300, 240), (560, 1200, 180)), (255, 255, 255, 150)), 0, 0)


def seeds():
    bg = sky((255, 200, 150), (200, 220, 236), (900, 360, 110, (255, 244, 214, 255)))
    sd = L(lambda d: [d.ellipse((x - 10, y - 16, x + 10, y + 16), fill="#16121a") for x, y in ((420, 760), (470, 940), (400, 1120), (520, 1300), (440, 1480))], 4, 3)
    sand = L(lambda d: (fill_wave(d, 1580, 16, 240, .4, SAND), [d.ellipse((x - 14, 1700 - y, x + 14, 1716 - y), fill="#16121a") for x, y in ((300, 0), (560, 30), (760, 10))]), 8, 6)
    return bg.convert("RGB"), [(0.5, _sea(1300, 2), sway(10, 1.0)), (1.0, L(lambda d: M.gull(d, 560, 560, 3.2, 1, True), 6, 4), bob(8, 2.0)), (0.9, sd, lambda t: (0, 40 * (t % 1.2))), (1.0, sand, None)]


def sowing():
    bg = sky((255, 220, 170), (200, 226, 220), (200, 380, 110, (255, 246, 220, 255)))
    pl = L(lambda d: (fill_wave(d, 1560, 12, 240, .4, SAND), [d.ellipse((x - 70, 1640, x + 70, 1700), fill="#8a6a3a") for x in (160, 540, 920)], M.an_tiem(d, 380, 1640, 2.9, hoe=True), M.vo(d, 760, 1650, 2.4, hat=True)), 10, 8)
    return bg.convert("RGB"), [(0.5, _sea(1250, 2), sway(10, 1.0)), (1.0, pl, bob(3, 1.5))]


# ---------- 6 ----------
def sprout():
    bg = grad((255, 236, 190), (210, 190, 130)).convert("RGBA")
    sp = L(lambda d: (fill_wave(d, 1200, 14, 240, .4, "#c8a870"), [(d.line([(x, 1500), (x, 1200 - h)], fill="#4f9a4a", width=18), d.polygon([(x, 1200 - h), (x - 90, 1160 - h), (x - 20, 1250 - h)], fill="#3f8a3a"), d.polygon([(x, 1200 - h), (x + 90, 1160 - h), (x + 20, 1250 - h)], fill="#3f8a3a")) for x, h in ((200, 40), (480, 200), (760, 120), (960, 20))], d.ellipse((60, 1480, 1020, 1760), fill="#8a6a3a")), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 900, 400)), (1.0, sp, sway(6, 1.4)), (0, "sparkle", None)]


def vines():
    bg = sky((200, 230, 240), (255, 246, 210), (860, 340, 110, (255, 248, 230, 255)))
    vn = L(lambda d: (fill_wave(d, 1400, 14, 240, .4, SAND), [d.line([(x0, 1500), (x0 + 200, 1560), (x0 + 380, 1500)], fill="#3f8a3a", width=14) for x0 in (-40, 300, 640)], [M.melon(d, x, y, r) for x, y, r in ((220, 1620, 110), (520, 1700, 130), (820, 1620, 100), (380, 1780, 90), (960, 1780, 80))], [d.polygon([(x, 1460), (x + 80, 1420), (x + 30, 1500)], fill="#3f8a3a") for x in (120, 420, 720)]), 10, 8)
    return bg.convert("RGB"), [(0.5, _sea(1150, 2), sway(10, 1.0)), (1.0, vn, sway(5, 1.2))]


def cut():
    bg = grad((255, 214, 170), (240, 150, 110)).convert("RGBA")
    pl = L(lambda d: (d.rectangle((0, 1560, W, H), fill="#c8a870"), M.melon(d, 540, 1100, 330, cut=True), d.polygon([(160, 1160), (260, 1100), (330, 1180), (200, 1260)], fill="#cfd4da", outline="#6a707c")), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 1000, 420)), (1.0, pl, bob(5, 1.2)), (0, "sparkle", None)]


def taste():
    bg = grad((255, 150, 110), (120, 60, 90)).convert("RGBA")
    pl = L(lambda d: (fill_wave(d, 1580, 12, 240, .4, "#8a6a3a"), M.vo(d, 230, 1720, 2.5), M.an_tiem(d, 540, 1720, 2.8), M.con(d, 850, 1720, 2.4), _slice(d, 380, 1380, 1.2), _slice(d, 690, 1330, 1.3), _slice(d, 980, 1450, 1.0)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1000, 400)), (1.0, pl, bob(3, 1.2)), (0, "sparkle", None)]


# ---------- 7 ----------
def harvest():
    bg = sky((255, 224, 170), (190, 226, 220), (200, 380, 110, (255, 246, 220, 255)))
    pl = L(lambda d: (fill_wave(d, 1560, 12, 240, .4, SAND), [M.melon(d, 440 + (i % 4) * 150 - (i // 4) * 60, 1680 - (i // 4) * 120, 70) for i in range(10)], M.an_tiem(d, 180, 1700, 2.6)), 10, 8)
    return bg.convert("RGB"), [(0.5, _sea(1250, 2), sway(10, 1.0)), (1.0, pl, bob(2, 1.2))]


def ship():
    bg = sky((255, 210, 160), (190, 226, 236), (200, 420, 110, (255, 246, 220, 255)))
    pl = L(lambda d: (M.boat(d, 700, 1380, 2.0, -1, "#f2d6a0"), M.merchant(d, 640, 1360, .9)), 10, 8)
    sh = L(lambda d: (_island(d, 220, 1560, 380), [M.melon(d, 140 + 80 * i, 1620, 46) for i in range(3)]), 8, 6)
    return bg.convert("RGB"), [(0.5, _sea(1250, 2), sway(10, 1.0)), (1.0, pl, bob(6, 1.2)), (0.8, sh, None), (0.9, _sea(1700, 2, DEEP), sway(12, 1.0))]


def trade():
    bg = grad((255, 226, 176), (214, 170, 110)).convert("RGBA")
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill=SAND), d.rectangle((380, 1360, 700, 1440), fill="#8a5a2a", outline=EDGE), d.rectangle((420, 1440, 440, 1640), fill="#5a3e26"), d.rectangle((640, 1440, 660, 1640), fill="#5a3e26"),
                      M.an_tiem(d, 190, 1700, 2.6), M.merchant(d, 890, 1700, 2.6), M.melon(d, 460, 1320, 50), M.melon(d, 600, 1320, 50), d.polygon([(690, 1250), (770, 1250), (780, 1360), (680, 1360)], fill="#efe0b4", outline=EDGE)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 380)), (1.0, pl, bob(2, 1.2))]


def rich_island():
    bg = sky((255, 220, 170), (190, 226, 236), (860, 360, 110, (255, 246, 220, 255)))
    isl = L(lambda d: (_island(d, 540, 1480, 600, "#d8c47a"), M.hut(d, 220, 1500), M.hut(d, 560, 1520, 200, 120), [M.melon(d, 140 + 90 * i, 1640 + (i % 2) * 30, 50) for i in range(9)], _palm(d, 900, 1480, 380, 40)), 10, 8)
    bt = L(lambda d: (M.boat(d, 180, 1300, .8), M.boat(d, 880, 1260, .6, -1)), 8, 6)
    sm = L(lambda d: [d.ellipse((x - r, y - r, x + r, y + r), fill=(230, 230, 230, 140)) for x, y, r in ((320, 1200, 40), (330, 1120, 56), (320, 1020, 70))], 0, 0)
    return bg.convert("RGB"), [(0.5, _sea(1240, 2), sway(10, 1.0)), (0.6, bt, bob(4, 1.0)), (0.8, isl, None), (0.5, sm, lambda t: (10 * math.sin(t), -20 * (t % 2)))]


# ---------- 8 ----------
def rumor():
    bg = sky((255, 214, 170), (200, 226, 220), (860, 360, 110, (255, 246, 220, 255)))
    hb = L(lambda d: (d.rectangle((0, 1500, W, H), fill="#8a6a3a"), [d.rectangle((x, 1440, x + 14, 1620), fill="#5a3e26") for x in (60, 330, 760)], M.boat(d, 880, 1440, .9, -1)), 8, 6)
    pl = L(lambda d: (M.merchant(d, 240, 1740, 2.1), M.merchant(d, 560, 1760, 2.4), M.merchant(d, 880, 1740, 2.0), [M.melon(d, x, y, 50) for x, y in ((240, 1070), (560, 1010), (880, 1090))]), 10, 8)
    return bg.convert("RGB"), [(0.6, hb, None), (1.0, pl, bob(3, 1.6))]


def gift_king():
    bg = grad((70, 30, 40), (200, 130, 70)).convert("RGBA")
    rm = L(lambda d: (_hall(d, "#8e1f24"), d.rectangle((520, 1100, 1000, 1560), fill="#a8421e", outline="#4a1014")), 8, 6)
    pl = L(lambda d: (K.king_hung(d, 780, 1560, 2.5), M.merchant(d, 230, 1680, 2.3), d.rectangle((90, 1520, 380, 1560), fill=GOLD, outline="#8a6a20"), M.melon(d, 240, 1470, 70)), 10, 8)
    return bg.convert("RGB"), [(0.5, rm, None), (0, "glow", S.sword_glow(540, 800, 360)), (1.0, pl, bob(2, 1.0)), (0, "sparkle", None)]


def king_eat():
    bg = grad((255, 190, 130), (200, 100, 70)).convert("RGBA")
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#7a3a24"), K.king_hung(d, 520, 1700, 3.8), _slice(d, 760, 1100, 2.4)), 10, 8)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 900, 440)), (1.0, pl, bob(2, 1.2)), (0, "sparkle", None)]


# ---------- 9 ----------
def king_realize():
    bg = grad((30, 24, 60), (90, 60, 100)).convert("RGBA")
    bub = L(lambda d: (d.ellipse((120, 360, 960, 1020), fill="#e8f2fa", outline=EDGE, width=6), [d.ellipse((x - r, y - r, x + r, y + r), fill="#e8f2fa", outline=EDGE, width=5) for x, y, r in ((300, 1100, 36), (250, 1190, 22))],
                      _island(d, 540, 800, 300), _palm(d, 420, 780, 200, 20), M.an_tiem(d, 580, 790, .8), fill_wave(d, 900, 10, 240, .4, "#3b8aa0")), 6, 4)
    pl = L(lambda d: (d.rectangle((0, 1620, W, H), fill="#4a2a2a"), K.king_hung(d, 540, 1700, 3.0)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1200, 380)), (0.8, bub, bob(6, 1.0)), (1.0, pl, bob(2, 1.0))]


def royal_boat():
    bg = sky((255, 200, 150), (190, 220, 236), (860, 420, 120, (255, 244, 214, 255)))
    bt = L(lambda d: (M.boat(d, 520, 1500, 2.2, 1, "#c8372d"), d.line([(220, 1500), (220, 1200)], fill="#5a3e26", width=8), d.polygon([(220, 1200), (360, 1230), (220, 1280)], fill=GOLD)), 10, 8)
    far = L(lambda d: (_island(d, 900, 1190, 200), _palm(d, 920, 1180, 120, 10)), 8, 6)
    return bg.convert("RGB"), [(0.4, far, None), (0.6, _sea(1230, 2), sway(10, 1.0)), (1.0, bt, bob(6, 1.2)), (0.9, _sea(1700, 2, DEEP), sway(14, 1.2))]


def return_home():
    bg = grad((255, 214, 170), (240, 170, 110)).convert("RGBA")
    rm = L(lambda d: (_hall(d, "#a8241e"), [d.polygon([(100 + i * 12, 1560 + i * 14), (980 - i * 12, 1560 + i * 14), (980 - i * 12, 1574 + i * 14), (100 + i * 12, 1574 + i * 14)], fill="#c8a45a") for i in range(4)]), 8, 6)
    pl = L(lambda d: (K.king_hung(d, 800, 1560, 2.4), M.an_tiem(d, 380, 1660, 2.2), M.vo(d, 220, 1680, 2.0), M.con(d, 520, 1690, 1.9)), 10, 8)
    return bg.convert("RGB"), [(0.5, rm, None), (0, "glow", S.sword_glow(540, 900, 380)), (1.0, pl, bob(2, 1.0)), (0, "sparkle", None)]


# ---------- 10 ----------
def seed_give():
    bg = sky((255, 224, 170), (200, 226, 200), (200, 380, 110, (255, 246, 220, 255)))
    pl = L(lambda d: (fill_wave(d, 1560, 12, 240, .4, "#6aa44e"), M.an_tiem(d, 280, 1700, 2.8), _peasant(d, 700, 1700, 1.7, 0, "#2f6a8a"), _peasant(d, 940, 1720, 1.5, 0, "#c8372d"), d.ellipse((470, 1560, 590, 1660), fill="#efe0b4", outline=EDGE), d.line([(380, 1500), (560, 1560)], fill="#e8c8a0", width=26)), 10, 8)
    return bg.convert("RGB"), [(0.3, S.mountain(1060, 40, 110, 2, "#a4c8a8", False), None), (1.0, pl, bob(2, 1.2))]


def fields():
    bg = sky((190, 226, 240), (255, 244, 210), (860, 320, 110, (255, 248, 230, 255)))
    fd = L(lambda d: [(fill_wave(d, 1100 + 150 * i, 12, 120, i, c), [M.melon(d, 80 + 180 * k + (i % 2) * 90, 1170 + 150 * i, 36 + 8 * i) for k in range(6)]) for i, c in enumerate(("#9fd078", "#86bc62", "#6aa44e", "#549040"))], 8, 6)
    return bg.convert("RGB"), [(0.3, S.mountain(1000, 40, 110, 4, "#b8d4b0", False), None), (1.0, fd, None), (1.0, L(lambda d: [_peasant(d, x, 1780, .9, 1, c) for x, c in ((200, "#c8372d"), (700, "#2f6a8a"))], 10, 8), None)]


def ancestor():
    bg = sky((255, 214, 150), (190, 200, 210), (800, 460, 120, (255, 246, 220, 255)))
    st = L(lambda d: (d.rectangle((300, 1480, 780, 1620), fill="#8a8478", outline="#4a463e"), d.rectangle((360, 1380, 720, 1480), fill="#a09a8c", outline="#4a463e"), M.an_tiem(d, 540, 1380, 3.2)), 12, 10)
    fl = L(lambda d: [M.melon(d, x, y, 50) for x, y in ((200, 1670), (860, 1680), (400, 1730), (700, 1740))], 6, 4)
    return bg.convert("RGB"), [(0.3, S.mountain(1090, 40, 110, 2, "#a4c8a8", False), None), (0.7, st, None), (1.0, fl, None), (1.0, ground(1700, "#6aa44e", 10), None), (0, "sparkle", None)]


# ---------- 11 ----------
def nga_son():
    bg = sky((255, 190, 150), (200, 220, 236), (860, 420, 120, (255, 240, 200, 255)))
    mt = L(lambda d: (_mtn(d, 300, 1380, 420, 760, "#5a8a60", True), _mtn(d, 680, 1380, 300, 480, "#7a9a7a")), 10, 8)
    bts = L(lambda d: (M.boat(d, 800, 1560, .7), M.boat(d, 300, 1620, .5, -1)), 8, 6)
    return bg.convert("RGB"), [(0.3, mt, None), (0.6, _sea(1420, 3), sway(10, 1.0)), (1.0, bts, bob(4, 1.0))]


def temple():
    bg = grad((255, 226, 176), (200, 220, 200)).convert("RGBA")

    def tp(d):
        d.polygon([(220, 1700), (860, 1700), (760, 1180), (320, 1180)], fill="#a09a8c", outline="#4a463e"); d.rectangle((300, 860, 780, 1180), fill=CREAM, outline=EDGE)
        d.polygon([(200, 870), (880, 870), (760, 700), (320, 700)], fill=RED); d.polygon([(200, 870), (240, 910), (840, 910), (880, 870)], fill="#8e2018"); d.rectangle((480, 960, 600, 1180), fill=INK)
        for x in (360, 720): d.rectangle((x - 16, 900, x + 16, 1180), fill="#8e1f24")
    tr = L(lambda d: [(d.rectangle((x - 16, 1100, x + 16, 1700), fill="#5a3e26"), d.ellipse((x - 140, 860, x + 140, 1200), fill="#3f8a5e")) for x in (100, 980)], 8, 6)
    pl = L(lambda d: ([M.melon(d, x, 1740, 56) for x in (320, 540, 760)], M.melon(d, 440, 1680, 40, cut=True)), 8, 6)
    return bg.convert("RGB"), [(0.3, S.mountain(1000, 50, 110, 3, "#a4c8a8", False), None), (0.6, tr, sway(3, 1.0)), (0.8, L(tp, 10, 8), None), (1.0, pl, None), (0, "sparkle", None)]


REG = {"ma_" + k: v for k, v in dict(court=court, home=home, family=family, boast=boast, informer=informer, tell_king=tell_king, angry_king=angry_king, exile_boat=exile_boat, island_arrive=island_arrive,
          island_empty=island_empty, food_low=food_low, resolve=resolve, birds=birds, seeds=seeds, sowing=sowing, sprout=sprout, vines=vines, cut=cut, taste=taste, harvest=harvest, ship=ship, trade=trade,
          rich_island=rich_island, rumor=rumor, gift_king=gift_king, king_eat=king_eat, king_realize=king_realize, royal_boat=royal_boat, return_home=return_home, seed_give=seed_give, fields=fields,
          ancestor=ancestor, nga_son=nga_son, temple=temple).items()}
