"""Scenes for the GTA 6 leak story (paper-cut, own drawings, no text in the art)."""
import math
from PIL import Image, ImageDraw, ImageFilter
import story2 as S
from story2 import grad, W, H, GOLD, INK, CREAM
from scenes_hk2 import L, sway, bob
from scenes_g6 import lucia, jason, _car, _palm, _vi, _deco
from chars_nv import suit

PINK, TEAL, GRN, RED_, ORG = "#ff5d8f", "#2ec4b6", "#3fae5a", "#d6403a", "#ff9a3c"


def _bg(c0=(10, 10, 26), c1=(42, 22, 60)): return grad(c0, c1).convert("RGBA")


def _glow(cx, cy, r, col=(255, 215, 90, 110)):
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)
    return g.filter(ImageFilter.GaussianBlur(70))


def _star(d, cx, cy, r, col=GOLD, out="#8a6a10"):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5; rr = r if i % 2 == 0 else r * .42
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, fill=col, outline=out)


def _card(d, x, y, w, h, c="#2a2d48"):
    d.rectangle((x, y, x + w, y + h), fill=c, outline="#0a0a14", width=6)
    d.rectangle((x + 12, y + 12, x + w - 12, y + h * .58), fill="#0e2a3a")
    d.ellipse((x + w * .28, y + h * .18, x + w * .62, y + h * .44), fill="#ffd36a")
    d.polygon([(x + w * .10, y + h * .56), (x + w * .34, y + h * .44), (x + w * .24, y + h * .58)], fill=TEAL)
    d.polygon([(x + w * .44, y + h * .56), (x + w * .68, y + h * .44), (x + w * .58, y + h * .58)], fill=PINK)
    d.polygon([(x + w * .44, y + h * .74), (x + w * .44, y + h * .90), (x + w * .58, y + h * .82)], fill="#f4f4ee")


def _teen(d, cx, base, s, col="#1a1c2a", hood="#242838"):
    d.rectangle((cx - 52 * s, base - 44 * s, cx - 12 * s, base), fill="#12131c")
    d.rectangle((cx + 12 * s, base - 44 * s, cx + 52 * s, base), fill="#12131c")
    d.polygon([(cx - 72 * s, base - 30 * s), (cx - 58 * s, base - 210 * s), (cx - 30 * s, base - 250 * s), (cx + 30 * s, base - 250 * s), (cx + 58 * s, base - 210 * s), (cx + 72 * s, base - 30 * s)], fill=col)
    d.rectangle((cx - 98 * s, base - 226 * s, cx - 60 * s, base - 96 * s), fill="#2f3a2a", outline="#1a2418", width=4)
    d.ellipse((cx - 54 * s, base - 336 * s, cx + 54 * s, base - 218 * s), fill=hood)
    d.ellipse((cx - 36 * s, base - 316 * s, cx + 36 * s, base - 238 * s), fill="#0a0b12")
    d.arc((cx - 60 * s, base - 348 * s, cx + 60 * s, base - 236 * s), 190, 350, fill=GOLD, width=max(int(9 * s), 3))
    d.ellipse((cx - 70 * s, base - 300 * s, cx - 42 * s, base - 254 * s), fill=GOLD)
    d.ellipse((cx + 42 * s, base - 300 * s, cx + 70 * s, base - 254 * s), fill=GOLD)


def _guard(d, cx, base, s, col="#2a3140"):
    d.rectangle((cx - 46 * s, base - 40 * s, cx - 10 * s, base), fill="#12131c")
    d.rectangle((cx + 10 * s, base - 40 * s, cx + 46 * s, base), fill="#12131c")
    d.polygon([(cx - 58 * s, base - 30 * s), (cx - 50 * s, base - 220 * s), (cx + 50 * s, base - 220 * s), (cx + 58 * s, base - 30 * s)], fill=col)
    d.rectangle((cx - 50 * s, base - 194 * s, cx + 50 * s, base - 156 * s), fill="#141a26")
    d.ellipse((cx - 30 * s, base - 286 * s, cx + 30 * s, base - 224 * s), fill="#d8b48c")
    d.rectangle((cx - 38 * s, base - 298 * s, cx + 38 * s, base - 268 * s), fill="#1a2230")
    d.rectangle((cx - 42 * s, base - 286 * s, cx + 42 * s, base - 272 * s), fill="#1a2230")
    d.rectangle((cx - 12 * s, base - 190 * s, cx - 2 * s, base - 172 * s), fill=GOLD)


def _bag(d, cx, base, s, col="#c8a45a"):
    d.polygon([(cx - 88 * s, base), (cx - 106 * s, base - 118 * s), (cx - 58 * s, base - 184 * s), (cx + 58 * s, base - 184 * s), (cx + 106 * s, base - 118 * s), (cx + 88 * s, base)], fill=col, outline="#6a4a1a", width=6)
    d.rectangle((cx - 34 * s, base - 224 * s, cx + 34 * s, base - 184 * s), fill="#a8863a", outline="#6a4a1a", width=4)
    d.ellipse((cx - 36 * s, base - 122 * s, cx + 36 * s, base - 50 * s), outline="#6a4a1a", width=5)
    d.line([(cx - 12 * s, base - 86 * s), (cx + 12 * s, base - 86 * s)], fill="#6a4a1a", width=5)


def _clock(d, cx, cy, r, frac=.82, col="#f4f4ee"):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col, outline="#3a3a4a", width=max(int(r * .09), 3))
    for i in range(12):
        a = i * math.pi / 6; rr = r * .76
        d.line([(cx + rr * math.cos(a), cy + rr * math.sin(a)), (cx + r * .9 * math.cos(a), cy + r * .9 * math.sin(a))], fill="#6a6e7a", width=max(int(r * .05), 2))
    d.line([(cx, cy), (cx + r * .48 * math.cos(-math.pi / 3), cy + r * .48 * math.sin(-math.pi / 3))], fill="#2a2d38", width=max(int(r * .08), 2))
    d.line([(cx, cy), (cx + r * .72 * math.cos(frac * 2 * math.pi), cy + r * .72 * math.sin(frac * 2 * math.pi))], fill=RED_, width=max(int(r * .06), 2))


def _ring(d, cx, cy, r, col=RED_):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=col, width=max(int(r * .09), 4))
    d.ellipse((cx - r * .55, cy - r * .55, cx + r * .55, cy + r * .55), outline=col, width=max(int(r * .06), 3))
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        d.line([(cx + dx * r * 1.28 - dy * 0, cy + dy * r * 1.28), (cx + dx * r * .7, cy + dy * r * .7)], fill=col, width=max(int(r * .07), 3))


def _trophy(d, cx, base, s):
    d.rectangle((cx - 78 * s, base - 26 * s, cx + 78 * s, base), fill="#8a6a3a", outline="#4a3412", width=6)
    d.rectangle((cx - 24 * s, base - 150 * s, cx + 24 * s, base - 26 * s), fill=GOLD, outline="#8a6a10", width=5)
    d.pieslice((cx - 120 * s, base - 340 * s, cx + 120 * s, base - 118 * s), 0, 180, fill=GOLD, outline="#8a6a10")
    d.rectangle((cx - 120 * s, base - 340 * s, cx + 120 * s, base - 286 * s), fill=GOLD, outline="#8a6a10", width=5)
    for sg in (-1, 1):
        d.arc((cx + sg * 130 * s - 58 * s, base - 316 * s, cx + sg * 130 * s + 58 * s, base - 210 * s), 90, 270, fill="#8a6a10", width=10)
    _star(d, cx, base - 232 * s, 48 * s, "#ffe08a", "#8a6a10")


def _camera(d, cx, cy, s, col="#1a1e2c"):
    d.rectangle((cx - 90 * s, cy - 50 * s, cx + 90 * s, cy + 60 * s), fill=col, outline="#0a0a12", width=5)
    d.rectangle((cx - 30 * s, cy - 92 * s, cx + 40 * s, cy - 50 * s), fill="#3a3f52")
    d.ellipse((cx - 104 * s, cy - 12 * s, cx - 40 * s, cy + 52 * s), fill="#0a0a12")
    d.ellipse((cx - 90 * s, cy + 2 * s, cx - 54 * s, cy + 38 * s), fill=TEAL)
    d.polygon([(cx + 62 * s, cy - 92 * s), (cx + 62 * s, cy - 150 * s), (cx + 70 * s, cy - 112 * s), (cx + 96 * s, cy - 100 * s), (cx + 70 * s, cy - 90 * s), (cx + 62 * s, cy - 56 * s)], fill="#ffe08a")


def _arm(d, y):
    d.polygon([(1080, y - 120), (940, y - 150), (800, y - 40), (820, y + 90), (1080, y + 140)], fill="#c8845a")
    d.polygon([(820, y - 40), (700, y - 74), (658, y + 8), (780, y + 70)], fill="#c8845a")
    d.line([(700, y - 58), (648, y - 44)], fill="#b07048", width=8)
    d.line([(706, y - 26), (650, y - 10)], fill="#b07048", width=8)


# ---------- cover ----------
def hotel():
    bg = _bg((8, 8, 20), (40, 18, 54))

    def room(d):
        for k in range(9): d.line([(0, 260 + k * 170), (W, 260 + k * 170)], fill="#1a1428", width=4)
        d.rectangle((30, 360, 150, 780), fill="#0c1224", outline="#2a2d48", width=8)
        for k in range(8): d.rectangle((38, 378 + k * 50, 142, 392 + k * 50), fill="#1a2440")
        d.ellipse((60, 320, 110, 370), fill="#e8e2c8")
        d.rectangle((0, 1520, W, H), fill="#140f20")
        d.rectangle((120, 1150, 960, 1190), fill="#0c0a14")
        d.rectangle((170, 430, 910, 1120), fill="#05050a", outline="#3a3a4a", width=12)
        d.rectangle((200, 462, 880, 1088), fill="#2a1040")
        d.rectangle((200, 462, 880, 700), fill="#ff7a90")
        d.ellipse((420, 520, 660, 760), fill="#ffd36a")
        for bx, bw, bt in ((225, 130, 800), (370, 150, 720), (540, 140, 780), (700, 130, 840)):
            d.rectangle((bx, bt, bx + bw, 1088), fill="#241446")
            for wy in range(bt + 30, 1060, 70):
                for wx in range(bx + 16, bx + bw - 24, 36):
                    d.rectangle((wx, wy, wx + 18, wy + 26), fill="#ffd36a" if (wx + wy) % 3 else "#3a2a5a")
        _car(d, 560, 1080, .34)
        d.rectangle((940, 1300, 1070, 1560), fill="#241a34")
        d.rectangle((975, 1180, 1035, 1300), fill="#3a2a4a")
        d.polygon([(950, 1180), (1060, 1180), (1022, 1120), (988, 1120)], fill="#c8a45a")
        d.rectangle((1002, 1128, 1022, 1184), fill="#ffd36a", outline="#8a6a10", width=3)
        d.polygon([(40, 1560), (60, 1380), (240, 1380), (270, 1560)], fill="#3a2d48", outline="#0a0a12", width=6)
        d.rectangle((128, 1352, 176, 1384), fill="#0a0a12")
        d.line([(70, 1440), (250, 1440)], fill="#241a34", width=6)
        cx = 560
        d.polygon([(cx - 200, H), (cx - 168, 1700), (cx - 110, 1600), (cx - 64, 1536), (cx + 64, 1536), (cx + 110, 1600), (cx + 168, 1700), (cx + 200, H)], fill="#0b0c12")
        d.ellipse((cx - 112, 1326, cx + 112, 1556), fill="#0b0c12")
        d.arc((cx - 112, 1326, cx + 112, 1556), 198, 342, fill="#4a4a5c", width=5)
        d.arc((cx - 126, 1306, cx + 126, 1566), 198, 342, fill=GOLD, width=9)
        d.ellipse((cx - 146, 1414, cx - 112, 1494), fill=GOLD, outline="#8a6a10", width=3)
        d.ellipse((cx + 112, 1414, cx + 146, 1494), fill=GOLD, outline="#8a6a10", width=3)
        d.line([(cx - 64, 1544), (cx - 34, 1624)], fill="#181a2a", width=6)
        d.line([(cx + 64, 1544), (cx + 34, 1624)], fill="#181a2a", width=6)
    return bg.convert("RGB"), [(0, "glow", _glow(540, 780, 380, (255, 150, 130, 70))), (1.0, L(room, 12, 8), bob(3, .9))]


# ---------- 1: the leak ----------
def leak():
    bg = _bg((22, 6, 20), (64, 14, 38))

    def room(d):
        d.rectangle((0, 1500, W, H), fill="#2a2038")
        d.ellipse((120, 1420, 380, 1600), fill="#3a3050")
        d.rectangle((250, 1050, 830, 1620), fill="#0a0a14", outline="#6a6e7a", width=10)
        d.rectangle((280, 1090, 800, 1580), fill="#122a3a")
        d.polygon([(490, 1240), (490, 1420), (640, 1330)], fill="#f4f4ee")
        d.rectangle((310, 1490, 770, 1510), fill="#3a4a5a"); d.rectangle((310, 1490, 500, 1510), fill=TEAL)
        cards = ((120, 300, "#3a2d48"), (300, 160, "#2a3a58"), (520, 80, "#483a2d"), (760, 200, "#2a4838"), (900, 420, "#4a2d3a"), (60, 560, "#38284a"), (330, 430, "#2d3a4a"), (620, 330, "#5a2a3a"), (850, 640, "#2d3a4a"), (120, 760, "#3a4a6a"))
        for x, y, c in cards: _card(d, x, y, 150, 230, c)
        for a in (245, 290, 335):
            d.line([(540, 1080), (540 - 250 * math.cos(math.radians(a)), 1080 - 250 * math.sin(math.radians(a)))], fill="#ffd36a", width=4)
    return bg.convert("RGB"), [(0, "glow", _glow(540, 900, 520, (255, 120, 150, 95))), (1.0, L(room, 12, 8), bob(4, 1.0)), (0, "sparkle", None)]


def footage():
    bg = _bg((16, 10, 34), (54, 20, 66))

    def scene(d):
        d.rectangle((90, 380, 990, 1300), fill="#05050a", outline="#3a3a4a", width=12)
        d.rectangle((120, 420, 960, 1260), fill="#301040")
        d.rectangle((120, 420, 960, 760), fill="#ff7a90")
        d.ellipse((420, 520, 660, 760), fill="#ffd36a")
        d.rectangle((120, 760, 960, 1260), fill="#241446")
        _deco(d, 30, 150, 900, 1300, edge=TEAL); _deco(d, 830, 160, 980, 1300, edge=PINK)
        _palm(d, 200, 1220, 360, 30, "#1a0f24"); _palm(d, 900, 1260, 300, -30, "#1a0f24")
        lucia(d, 430, 1220, 1.5); jason(d, 680, 1220, 1.5)
        d.polygon([(820, 470), (820, 570), (916, 520)], fill="#f4f4ee")
        d.rectangle((150, 1230, 930, 1248), fill="#6a6e7a"); d.rectangle((150, 1230, 420, 1248), fill=TEAL)
        for k in range(6): d.rectangle((120, 430 + k * 52, 960, 444 + k * 52), fill=(255, 255, 255, 18))
        d.ellipse((110, 1490, 310, 1700), fill="#0a0a12"); d.rectangle((50, 1650, 380, H), fill="#0a0a12")
    return bg.convert("RGB"), [(0, "glow", _glow(540, 840, 540, (255, 120, 150, 90))), (1.0, L(scene, 12, 8), sway(3, .8))]


# ---------- 2: the boy, the hotel ----------
def teen():
    bg = _bg((10, 12, 30), (36, 34, 60))

    def scene(d):
        d.rectangle((0, 1560, W, H), fill="#12162a")
        d.rectangle((760, 560, 1040, 1560), fill="#1a2036", outline="#2a3050", width=10)
        d.rectangle((790, 600, 1010, 1520), fill="#0e1428")
        d.ellipse((300, 1560, 640, 1660), fill="#0a0e1c")
        _teen(d, 430, 1560, 1.35)
        d.ellipse((452, 1204, 478, 1230), fill="#7ee0ff")
        d.ellipse((466, 1120, 540, 1194), fill=(126, 224, 255, 45))
    return bg.convert("RGB"), [(0, "glow", _glow(470, 1240, 280, (120, 200, 255, 90))), (1.0, L(scene, 12, 8), bob(3, .8))]


def guard():
    bg = _bg((6, 10, 24), (24, 32, 56))

    def scene(d):
        d.rectangle((0, 1520, W, H), fill="#0a0e1a")
        d.rectangle((60, 420, 1020, 1520), fill="#1c2238", outline="#2c3654", width=8)
        for r in range(4):
            for c in range(5):
                x = 100 + c * 180; y = 480 + r * 240; lit = (r * 5 + c) % 3 == 0
                d.rectangle((x, y, x + 140, y + 150), fill="#ffd36a" if lit else "#2a3450", outline="#101626", width=4)
        d.rectangle((300, 330, 780, 420), fill="#f4f4ee", outline="#8a8e9a", width=6)
        d.rectangle((380, 1180, 700, 1520), fill="#0e1424", outline="#3a4668", width=8)
        d.rectangle((330, 1130, 750, 1190), fill="#3a4668")
        d.rectangle((90, 560, 170, 610), fill="#0a0e18"); d.line([(130, 610), (110, 650)], fill="#0a0e18", width=7)
        d.rectangle((160, 1420, 300, 1560), fill="#3a2d48", outline="#0a0a12", width=6)
        d.rectangle((208, 1398, 252, 1424), fill="#0a0a12")
        _guard(d, 790, 1560, 1.7)
    return bg.convert("RGB"), [(0, "glow", _glow(540, 1300, 320, (255, 215, 120, 80))), (1.0, L(scene, 12, 8), bob(2, .7))]


# ---------- 3: no computer, just the TV ----------
def nopc():
    bg = _bg((14, 12, 26), (36, 26, 52))

    def scene(d):
        d.rectangle((0, 1400, W, H), fill="#1a1428")
        d.rectangle((100, 1220, 980, 1290), fill="#5a3e2a", outline="#2a1c12", width=6)
        d.rectangle((160, 1290, 220, 1620), fill="#3a2a1a"); d.rectangle((860, 1290, 920, 1620), fill="#3a2a1a")
        d.rectangle((380, 1290, 700, 1320), fill="#2a2038"); d.line([(440, 1320), (440, 1540)], fill="#2a2038", width=16); d.line([(640, 1320), (640, 1540)], fill="#2a2038", width=16)
        d.line([(760, 1220), (760, 1090), (700, 1010)], fill="#0a0a12", width=10); d.rectangle((678, 950, 722, 1000), fill="#0a0a12")
        # ghost outline of the taken laptop
        x0, y0, x1, y1 = 280, 1040, 640, 1210
        for i in range(0, 101, 20):
            d.line([(x0 + (x1 - x0) * i / 100, y0), (x0 + (x1 - x0) * min(i + 10, 100) / 100, y0)], fill="#8a8e9a", width=3)
            d.line([(x0 + (x1 - x0) * i / 100, y1), (x0 + (x1 - x0) * min(i + 10, 100) / 100, y1)], fill="#8a8e9a", width=3)
        for i in range(0, 101, 20):
            d.line([(x0, y0 + (y1 - y0) * i / 100), (x0, y0 + (y1 - y0) * min(i + 10, 100) / 100)], fill="#8a8e9a", width=3)
            d.line([(x1, y0 + (y1 - y0) * i / 100), (x1, y0 + (y1 - y0) * min(i + 10, 100) / 100)], fill="#8a8e9a", width=3)
        d.rectangle((700, 1300, 900, 1410), fill="#4a3220", outline="#2a1c12", width=5)
        d.ellipse((774, 1336, 826, 1388), fill="#ffd36a", outline="#8a6a10", width=4)
        d.rectangle((794, 1352, 806, 1372), fill="#8a6a10")
        # laptop sealed in evidence bag, carried away
        d.polygon([(540, 470), (1000, 430), (1040, 1010), (580, 1050)], fill=(225, 232, 245, 52), outline="#c8ccd4", width=6)
        for i in range(8): d.line([(560 + i * 58, 452 - i * 5), (590 + i * 58, 448 - i * 5)], fill="#8a8e9a", width=3)
        d.ellipse((590, 930, 660, 1000), fill=(255, 215, 90, 55), outline="#c8a45a", width=4)
        d.rectangle((980, 330, 1080, 470), fill="#1a1e2c")
        d.polygon([(1000, 360), (1080, 340), (1080, 500), (1010, 500)], fill="#c8845a")
        d.ellipse((930, 430, 1020, 530), fill="#c8845a")
        for k in range(4): d.line([(944 + k * 18, 500), (950 + k * 18, 560)], fill="#b07048", width=7)
        d.rectangle((640, 620, 960, 880), fill="#2a2d38", outline="#0a0a12", width=8)
        d.rectangle((660, 650, 940, 720), fill="#0e2a3a")
        d.rectangle((610, 800, 780, 848), fill=(245, 245, 245, 60), outline="#8a8e9a", width=2)
        for i in range(7): d.line([(624 + i * 20, 812), (624 + i * 20, 836)], fill="#8a8e9a", width=3)
    return bg.convert("RGB"), [(0, "glow", _glow(520, 1080, 360, (200, 220, 255, 70))), (1.0, L(scene, 12, 8), bob(3, .7))]


def stick():
    bg = _bg((8, 16, 30), (26, 44, 60))

    def scene(d):
        d.rectangle((0, 1620, W, H), fill="#1a1428")
        d.rectangle((50, 380, 890, 1320), fill="#05050a", outline="#2a3444", width=12)
        d.rectangle((90, 420, 850, 1280), fill="#0c1a2a")
        _star(d, 470, 680, 120, GOLD)
        d.rectangle((240, 880, 700, 960), fill="#16283c", outline="#3a4a5a", width=4)
        d.rectangle((240, 1000, 700, 1080), fill="#16283c", outline="#3a4a5a", width=4)
        d.rectangle((320, 1140, 620, 1210), fill=TEAL)
        d.line([(872, 470), (930, 540)], fill="#0a0a12", width=10)
        d.rectangle((920, 520, 976, 790), fill="#ffd36a", outline="#8a6a10", width=6)
        d.rectangle((920, 560, 976, 584), fill="#1a1a22")
        d.ellipse((914, 760, 982, 830), fill="#1a1a22", outline="#0a0a12", width=4)
        for r in (80, 120, 160): d.arc((920 - r, 790 - r, 920 + r, 790 + r), 95, 175, fill=TEAL, width=6)
        d.rectangle((140, 1500, 700, 1620), fill="#2a2d38", outline="#0a0a12", width=6)
        for c in range(10):
            for r in range(3): d.rectangle((164 + c * 52, 1518 + r * 32, 200 + c * 52, 1538 + r * 32), fill="#4a4e5a")
        d.ellipse((800, 1500, 940, 1620), fill="#2a2d38", outline="#0a0a12", width=6); d.line([(870, 1530), (870, 1560)], fill="#4a4e5a", width=6)
    return bg.convert("RGB"), [(0, "glow", _glow(996, 690, 260, (255, 215, 90, 110))), (1.0, L(scene, 12, 8), bob(3, .9))]


# ---------- 4: ultimatum, refusal ----------
def slack():
    bg = _bg((8, 24, 24), (18, 54, 50))

    def scene(d):
        d.rectangle((0, 1500, W, H), fill="#0e2422")
        d.rectangle((70, 420, 930, 1200), fill="#050a0a", outline="#2a4a46", width=10)
        d.rectangle((100, 450, 900, 1170), fill="#0e2422")
        d.rectangle((100, 450, 260, 1170), fill="#123230")
        for k in range(4): d.ellipse((140, 500 + k * 70, 180, 540 + k * 70), fill="#2a4a46")
        _star(d, 470, 530, 56, GOLD)
        d.rectangle((320, 640, 700, 730), fill="#2a4a46")
        d.rectangle((340, 780, 840, 870), fill="#1c3c38")
        d.rectangle((320, 920, 620, 1010), fill="#2a4a46")
        d.ellipse((860, 620, 890, 650), fill=RED_); d.ellipse((860, 760, 890, 790), fill=RED_)
        d.polygon([(880, 250), (1070, 320), (905, 390)], fill="#f4f4ee", outline="#6a6e7a")
        d.line([(905, 330), (1055, 322)], fill="#6a6e7a", width=4)
        d.polygon([(770, 1180), (1010, 1180), (890, 1350)], fill="#3a2a1a", outline="#8a6a10")
        d.polygon([(890, 1350), (770, 1500), (1010, 1500)], fill="#3a2a1a", outline="#8a6a10")
        d.polygon([(812, 1210), (968, 1210), (890, 1320)], fill=RED_)
        d.polygon([(806, 1474), (974, 1474), (890, 1400)], fill=RED_)
        d.line([(750, 1180), (1030, 1180)], fill="#8a6a10", width=12); d.line([(750, 1500), (1030, 1500)], fill="#8a6a10", width=12)
    return bg.convert("RGB"), [(0, "glow", _glow(540, 800, 480, (90, 220, 200, 70))), (1.0, L(scene, 12, 8), bob(3, .8))]


def refuse():
    bg = _bg((30, 8, 14), (76, 22, 30))

    def scene(d):
        d.rectangle((0, 1300, W, H), fill="#3a1c22")
        _star(d, 660, 600, 230, "#4a2d3a", "#7a1a4a")
        d.rectangle((780, 250, 1020, 620), fill="#0a0a14", outline="#6a6e7a", width=8)
        d.ellipse((900, 310, 968, 378), fill="#e8e2c8")
        d.line([(900, 330), (900, 620)], fill="#3a3a4a", width=5)
        for x, y, c in ((820, 300, "#3a2d48"), (900, 440, "#2a3a58"), (800, 520, "#483a2d")):
            _card(d, x, y, 90, 140, c)
        _bag(d, 470, 1300, 1.4)
        _arm(d, 980)
        d.ellipse((620, 900, 700, 980), fill=(255, 215, 90, 40))
    return bg.convert("RGB"), [(0, "glow", _glow(650, 700, 420, (255, 90, 110, 80))), (1.0, L(scene, 12, 8), sway(2, .7))]


# ---------- 5: cost, other targets ----------
def cost():
    bg = _bg((10, 26, 20), (30, 60, 44))

    def scene(d):
        d.rectangle((0, 1560, W, H), fill="#10261a")
        _star(d, 540, 300, 86, "#3a4a3a", "#1f6a30")
        d.line([(540, 420), (540, 1360)], fill="#8a6e3a", width=16)
        d.line([(220, 560), (860, 560)], fill="#8a6e3a", width=14)
        d.polygon([(540, 1360), (430, 1480), (650, 1480)], fill="#6a5228")
        d.arc((160, 560, 500, 700), 0, 180, fill="#c8a45a", width=10)
        d.arc((580, 560, 920, 700), 0, 180, fill="#c8a45a", width=10)
        for i in range(5): _bag(d, 250 + i * 38, 690 - i * 54, .34)
        for x, y in ((640, 686), (740, 686), (840, 686), (690, 600), (790, 600), (740, 500)): _clock(d, x, y, 44)
    return bg.convert("RGB"), [(0, "glow", _glow(540, 900, 440, (150, 220, 140, 80))), (1.0, L(scene, 12, 8), bob(2, .7))]


def targets():
    bg = _bg((10, 12, 34), (30, 26, 60))

    def scene(d):
        d.rectangle((0, 1580, W, H), fill="#0a0a12")
        _car(d, 250, 1500, .62)
        d.rectangle((450, 1030, 700, 1210), fill="#3a4a6a", outline="#0e1630", width=6)
        d.rectangle((472, 1052, 678, 1108), fill=GOLD)
        d.rectangle((472, 1130, 610, 1152), fill="#8aa0c8")
        d.line([(870, 1500), (870, 760)], fill="#6a6e7a", width=24)
        d.line([(790, 860), (950, 860)], fill="#6a6e7a", width=12)
        d.line([(810, 960), (930, 960)], fill="#6a6e7a", width=12)
        d.ellipse((844, 736, 896, 788), fill=RED_)
        _ring(d, 250, 1216, 166); _ring(d, 575, 1080, 150); _ring(d, 870, 830, 136)
    return bg.convert("RGB"), [(0, "glow", _glow(560, 1050, 520, (255, 90, 110, 70))), (1.0, L(scene, 12, 8), bob(3, .7))]


# ---------- 6: hospital, court, launch, after ----------
def hospital():
    bg = _bg((8, 22, 26), (20, 48, 50))

    def scene(d):
        d.rectangle((0, 1560, W, H), fill="#0e2426")
        d.rectangle((800, 500, 900, 600), fill="#c8372d"); d.rectangle((830, 470, 870, 630), fill="#c8372d"); d.rectangle((770, 530, 930, 570), fill="#c8372d")
        d.rectangle((110, 420, 520, 900), fill="#0a1420", outline="#2a4a46", width=8)
        for k in range(4): d.line([(150 + k * 100, 420), (150 + k * 100, 900)], fill="#2a4a46", width=8)
        d.ellipse((290, 500, 370, 580), fill="#e8e2c8")
        d.line([(560, 930), (560, 1560)], fill="#8a8e9a", width=10)
        d.rectangle((520, 860, 600, 930), fill="#c8e0e4", outline="#8a8e9a", width=3)
        d.line([(560, 930), (560, 1180)], fill="#8a8e9a", width=5)
        d.rectangle((100, 980, 220, 1240), fill="#6a6e7a")
        d.rectangle((90, 1200, 770, 1280), fill="#e8e6dc", outline="#8a8e9a", width=6)
        d.rectangle((90, 1280, 770, 1330), fill="#6a6e7a")
        d.rectangle((130, 1330, 170, 1560), fill="#4a4e5a"); d.rectangle((690, 1330, 730, 1560), fill="#4a4e5a")
        d.rectangle((130, 1140, 340, 1205), fill="#f4f0e4", outline="#b8b8b8", width=3)
        d.rectangle((300, 1170, 770, 1280), fill="#4a7a7a", outline="#2a4a4a", width=4)
        d.rectangle((300, 1170, 770, 1192), fill="#5a8a8a")
        d.ellipse((190, 1080, 300, 1180), fill="#e0b08a")
        d.pieslice((190, 1070, 300, 1160), 180, 360, fill="#2a2018")
        d.rectangle((780, 1490, 930, 1530), fill="#3a2a1a", outline="#1a1008", width=4)
        d.ellipse((780, 1466, 930, 1512), fill="#5a3e2a")
        d.line([(820, 1490), (950, 1350)], fill="#4a3018", width=22)
        d.rectangle((900, 1270, 1030, 1350), fill="#5a3a20", outline="#241408", width=6)
        d.line([(925, 1274), (925, 1346)], fill="#8a6a3a", width=8)
        d.line([(995, 1274), (995, 1346)], fill="#8a6a3a", width=8)
    return bg.convert("RGB"), [(0, "glow", _glow(540, 900, 420, (120, 210, 220, 80))), (1.0, L(scene, 12, 8), bob(2, .7))]


def court():
    bg = _bg((20, 24, 40), (52, 56, 78))

    def scene(d):
        d.rectangle((0, 1330, W, H), fill="#2a2e40")
        d.polygon([(180, 540), (900, 540), (780, 360), (300, 360)], fill="#3a3f52", outline="#1a1e2c", width=8)
        for i in range(4): d.rectangle((230 + i * 190, 560, 320 + i * 190, 1200), fill="#4a4f62", outline="#1a1e2c", width=6)
        d.rectangle((180, 500, 900, 560), fill="#4a4f62")
        d.rectangle((450, 920, 630, 1200), fill="#1a1428")
        d.rectangle((140, 1200, 940, 1260), fill="#5a5f72")
        d.rectangle((100, 1260, 980, 1330), fill="#4a4f62")
        _guard(d, 310, 1580, 1.5); _guard(d, 770, 1580, 1.5)
        suit(d, 540, 1580, 1.55, "#2a2d38", "#3a5a8a")
        _camera(d, 170, 1500, 1.0); _camera(d, 910, 1500, .95)
        d.rectangle((0, 1600, W, H), fill="#12141f")
    return bg.convert("RGB"), [(0, "glow", _glow(540, 1000, 430, (200, 210, 240, 60))), (1.0, L(scene, 12, 8), sway(2, .7))]


def launch():
    bg = _bg((30, 18, 6), (92, 52, 14))

    def scene(d):
        d.rectangle((0, 1580, W, H), fill="#3a2a0a")
        d.rectangle((300, 620, 720, 1420), fill="#ff9a6a", outline="#16161a", width=10)
        d.rectangle((300, 620, 720, 900), fill=PINK)
        d.ellipse((400, 720, 620, 940), fill="#ffd36a")
        d.rectangle((300, 1160, 720, 1420), fill="#241446")
        _vi(d, 510, 760, .40)
        _palm(d, 350, 1160, 250, 20, "#16102a"); _palm(d, 670, 1160, 210, -20, "#16102a")
        _trophy(d, 900, 1420, 1.1)
        for i, x in enumerate(range(50, 1050, 88)):
            d.ellipse((x, 210 + (i % 3) * 54, x + 44, 254 + (i % 3) * 54), fill=GOLD, outline="#8a6a10", width=4)
        for x, y in ((180, 420), (880, 380), (620, 260)): _star(d, x, y, 34, "#ffe08a", "#8a6a10")
    return bg.convert("RGB"), [(0, "glow", _glow(600, 900, 560, (255, 215, 120, 110))), (1.0, L(scene, 12, 8), bob(3, 1.0)), (0, "sparkle", None)]


def cell():
    bg = _bg((10, 14, 22), (24, 30, 40))

    def scene(d):
        for k in range(6): d.line([(0, 240 + k * 260), (W, 240 + k * 260)], fill="#161c26", width=4)
        d.rectangle((180, 380, 900, 1120), fill="#0c0f16", outline="#2a3240", width=18)
        d.rectangle((198, 398, 882, 820), fill="#1c3050")
        d.rectangle((198, 820, 882, 1080), fill="#c8703e")
        d.ellipse((690, 740, 850, 900), fill="#ffd08a")
        for i, (bx, bt) in enumerate(((230, 800), (310, 740), (390, 860), (470, 780), (560, 830), (650, 770), (740, 850), (820, 800))):
            d.rectangle((bx, bt, bx + 70, 1080), fill="#0e121c")
            for r in range(3):
                for c in range(2):
                    if (i + r + c) % 3: d.rectangle((bx + 12 + c * 30, bt + 18 + r * 34, bx + 22 + c * 30, bt + 28 + r * 34), fill="#e8b45a")
        for x0 in (330, 540, 750): d.rectangle((x0 - 12, 398, x0 + 12, 1102), fill="#0a0d14")
        d.rectangle((198, 700, 882, 722), fill="#0a0d14")
        d.rectangle((150, 1102, 930, 1132), fill="#2a3240")
        for gy in (540, 650, 760):
            for gx in range(4): d.line([(946 + gx * 22, gy), (946 + gx * 22, gy + 56)], fill="#5a6474", width=6)
            d.line([(944, gy + 48), (1006, gy + 10)], fill="#5a6474", width=6)
        d.ellipse((440, 850, 640, 1050), fill="#05070c")
        d.rectangle((515, 1010, 565, 1090), fill="#05070c")
        d.polygon([(430, 1070), (650, 1070), (730, 1260), (800, 1920), (280, 1920), (350, 1260)], fill="#05070c")
        d.arc((440, 850, 640, 1050), 200, 340, fill="#ffbe7a", width=6)
        d.line([(430, 1070), (392, 1170)], fill="#ffbe7a", width=5)
        d.line([(650, 1070), (688, 1170)], fill="#ffbe7a", width=5)
    return bg.convert("RGB"), [(0, "glow", _glow(540, 860, 460, (255, 170, 110, 80))), (1.0, L(scene, 14, 10), sway(1.2, .4))]


REG = {"g6h_" + k: v for k, v in dict(hotel=hotel, leak=leak, footage=footage, teen=teen, guard=guard, nopc=nopc, stick=stick, slack=slack, refuse=refuse, cost=cost, targets=targets, hospital=hospital, court=court, launch=launch, cell=cell).items()}
