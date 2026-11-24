"""Scenes for the GTA 6 news explainer: paper-cut drawings (own interpretation of the game's look: sunset, palms, neon, the two leads, a stylised VI logo). No text in the drawings."""
import math
import story2 as S
from story2 import grad, W, H, GOLD, INK
from scenes_hk2 import L, sway, bob
import chars_nv as N
from chars_st import _p, _eyes

PINK, TEAL, GRN, RED_, ORG = "#ff5d8f", "#2ec4b6", "#3fae5a", "#d6403a", "#ff9a3c"


def _bg(c0=(20, 14, 48), c1=(70, 40, 100)): return grad(c0, c1).convert("RGBA")


def _q(d, cx, cy, s, col="#f2f2ee"):
    d.arc((cx - 90 * s, cy - 150 * s, cx + 90 * s, cy - 10 * s), 200, 380, fill=col, width=int(44 * s)); d.line([(cx + 80 * s, cy - 60 * s), (cx, cy + 40 * s), (cx, cy + 80 * s)], fill=col, width=int(44 * s)); d.ellipse((cx - 26 * s, cy + 120 * s, cx + 26 * s, cy + 172 * s), fill=col)


def _bill(d, x, y, w=300, h=130):
    d.rectangle((x, y, x + w, y + h), fill="#5cc06a", outline="#1f6a30", width=5); d.ellipse((x + w / 2 - h * .3, y + h * .2, x + w / 2 + h * .3, y + h * .8), fill="#8ae09a", outline="#1f6a30", width=4)


def _stack(d, cx, base, n, w=300):
    for i in range(n): _bill(d, cx - w / 2 + (i % 2) * 8, base - (i + 1) * 36, w, 110)


def _coin(d, cx, cy, r): d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GOLD, outline="#8a6a10", width=6); d.ellipse((cx - r * .62, cy - r * .62, cx + r * .62, cy + r * .62), outline="#c89a20", width=5)


def _sil(d, cx, base, s, col="#2a2d38"):
    d.polygon([(cx - 50 * s, base), (cx - 36 * s, base - 150 * s), (cx + 36 * s, base - 150 * s), (cx + 50 * s, base)], fill=col); d.ellipse((cx - 28 * s, base - 215 * s, cx + 28 * s, base - 150 * s), fill=col)


def _palm(d, x, base, h, lean=0, col="#2a1a2a"):
    top = (x + lean, base - h); d.line([(x, base), top], fill=col, width=int(h * .05) + 8)
    for a in (-170, -130, -90, -50, -10, 190, 230):
        ex, ey = top[0] + h * .36 * math.cos(math.radians(a)), top[1] + h * .22 * math.sin(math.radians(a)) + h * .1
        d.polygon([top, (ex - 18, ey - 24), (ex + 18, ey + 24)], fill=col)


def _vi(d, cx, cy, s):
    """Stylised 'VI' logo: a pink-to-orange V and I, drawn as polygons."""
    d.polygon([(cx - 210 * s, cy - 150 * s), (cx - 120 * s, cy - 150 * s), (cx - 40 * s, cy + 90 * s), (cx + 40 * s, cy - 150 * s), (cx + 130 * s, cy - 150 * s), (cx - 40 * s, cy + 190 * s)], fill=PINK, outline="#7a1a4a")
    d.polygon([(cx - 120 * s, cy - 150 * s), (cx - 60 * s, cy - 150 * s), (cx - 10 * s, cy), (cx - 70 * s, cy)], fill=ORG)
    d.rectangle((cx + 160 * s, cy - 150 * s, cx + 250 * s, cy + 190 * s), fill=PINK, outline="#7a1a4a"); d.rectangle((cx + 160 * s, cy - 150 * s, cx + 250 * s, cy - 40 * s), fill=ORG)


def lucia(d, cx, base, s):
    """One of the two leads (own simplified paper-cut): long dark wavy hair, tan skin, orange top, blue jeans."""
    p = _p(cx, base, s)
    d.rectangle((*p(-24, -52), *p(-4, 0)), fill="#2a4a8a"); d.rectangle((*p(4, -52), *p(24, 0)), fill="#2a4a8a")
    d.polygon([p(-34, -230), p(-48, -150), p(-40, -90), p(40, -90), p(48, -150), p(34, -230)], fill="#3a2418")
    d.polygon([p(-44, -52), p(-34, -150), p(34, -150), p(44, -52)], fill=ORG, outline="#a05a10")
    d.ellipse((*p(-28, -214), *p(28, -148)), fill="#c8845a"); _eyes(d, p, -190); d.arc((*p(-10, -176), *p(10, -160)), 20, 160, fill="#7a2a2a", width=max(int(3 * s), 2))
    d.polygon([p(-30, -206), p(-26, -234), p(0, -244), p(26, -234), p(30, -206), p(14, -216), p(-14, -216)], fill="#3a2418")


def jason(d, cx, base, s):
    """The other lead (own simplified paper-cut): cap, short dark hair, white tank top, jeans."""
    p = _p(cx, base, s)
    d.rectangle((*p(-24, -62), *p(-4, 0)), fill="#3a4a6a"); d.rectangle((*p(4, -62), *p(24, 0)), fill="#3a4a6a")
    d.polygon([p(-50, -62), p(-40, -152), p(40, -152), p(50, -62)], fill="#f4f4ee", outline="#8a8e9a"); d.polygon([p(-56, -150), p(-40, -152), p(-44, -100), p(-62, -104)], fill="#c8845a"); d.polygon([p(56, -150), p(40, -152), p(44, -100), p(62, -104)], fill="#c8845a")
    d.ellipse((*p(-28, -214), *p(28, -148)), fill="#d49a70"); _eyes(d, p, -190); d.line([p(-10, -170), p(10, -170)], fill="#7a2a2a", width=max(int(3 * s), 2))
    d.polygon([p(-32, -200), p(-30, -224), p(0, -232), p(30, -224), p(32, -200)], fill=TEAL); d.polygon([p(-32, -204), p(-60, -198), p(-32, -190)], fill="#1a8a80")


def _car(d, cx, base, s):
    d.polygon([(cx - 330 * s, base - 60 * s), (cx - 270 * s, base - 140 * s), (cx - 100 * s, base - 150 * s), (cx - 20 * s, base - 215 * s), (cx + 120 * s, base - 215 * s), (cx + 190 * s, base - 150 * s), (cx + 330 * s, base - 130 * s), (cx + 350 * s, base - 60 * s)], fill=PINK, outline="#7a1a4a")
    d.polygon([(cx - 10 * s, base - 150 * s), (cx + 20 * s, base - 200 * s), (cx + 110 * s, base - 200 * s), (cx + 160 * s, base - 150 * s)], fill="#9ad8e8")
    for dx in (-190, 210): d.ellipse((cx + dx * s - 62 * s, base - 120 * s, cx + dx * s + 62 * s, base + 4 * s), fill="#16161a"); d.ellipse((cx + dx * s - 28 * s, base - 86 * s, cx + dx * s + 28 * s, base - 30 * s), fill="#c8ccd4")


def _deco(d, x, w, top, base, c="#241446", edge=TEAL):
    d.rectangle((x, top, x + w, base), fill=c); d.rectangle((x + w * .12, top - 40, x + w * .88, top), fill=c); d.line([(x, top), (x + w, top)], fill=edge, width=8)
    for i in range(int((base - top) // 90)): d.rectangle((x + w * .2, top + 30 + i * 90, x + w * .8, top + 46 + i * 90), fill=(255, 120, 150) if i % 2 else (90, 220, 220))


def _screen(d, x0, y0, x1, y1, col="#0e1a2a"):
    d.rectangle((x0, y0, x1, y1), fill=col, outline="#8a8e9a", width=8)


# ---------- cover ----------
def city():
    bg = grad((50, 12, 90), (255, 130, 100)).convert("RGBA")
    pl = L(lambda d: (d.ellipse((220, 540, 860, 1180), fill="#ffd36a"), [d.rectangle((220, 760 + k * 66, 860, 780 + k * 66 + 14 + k * 6), fill=(255, 130, 120, 255)) for k in range(5)],
                      _deco(d, 0, 170, 1180, 1700), _deco(d, 150, 130, 1000, 1700, edge=PINK), _deco(d, 270, 160, 1240, 1700), _deco(d, 760, 150, 1100, 1700, edge=PINK), _deco(d, 900, 180, 1280, 1700),
                      d.rectangle((0, 1640, W, H), fill="#160a30"), [d.rectangle((x, 1790, x + 120, 1806), fill="#ffd36a") for x in range(40, 1080, 240)], _palm(d, 110, 1720, 760, 50), _palm(d, 980, 1720, 640, -60), _car(d, 540, 1760, 0.8), _vi(d, 540, 330, 0.9)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 860, 520)), (1.0, pl, bob(4, 1.2))]


# ---------- 1: cost, 13 years, delay ----------
def money():
    bg = _bg((6, 30, 28), (20, 80, 60))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#10382c"), [(_screen(d, x - 130, 1300, x + 130, 1440), d.polygon([(x - 110, 1420), (x - 70, 1340), (x - 20, 1400), (x + 40, 1320), (x + 110, 1420)], fill=TEAL), d.rectangle((x - 150, 1440, x + 150, 1480), fill="#5a3e2a"), d.rectangle((x - 130, 1480, x - 110, 1640), fill="#3a2a1a"), d.rectangle((x + 110, 1480, x + 130, 1640), fill="#3a2a1a")) for x in (210, 540, 870)],
                      [N.suit(d, x, 1300, 1.7, c, t) for x, c, t in ((210, "#6a6e7a", "#2f6a8a"), (540, "#7a4a4a", "#d6403a"), (870, "#4a6a5a", "#c8a43a"))],
                      [_bill(d, 120 + i * 140, 380 + (i % 3) * 120 + i * 8, 190, 86) for i in range(7)], d.polygon([(420, 300), (660, 300), (700, 150), (380, 150)], fill="#c8a45a", outline="#6a4a1a"), d.ellipse((330, 280, 750, 640), fill="#c8a45a", outline="#6a4a1a", width=8), d.line([(540, 360), (540, 560)], fill="#5a3e1a", width=18), d.arc((470, 380, 610, 480), 90, 360, fill="#5a3e1a", width=18), d.arc((470, 450, 610, 560), 270, 450, fill="#5a3e1a", width=18)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 460)), (1.0, pl, bob(4, 1.1))]


def clock():
    bg = _bg((24, 20, 60), (60, 50, 110))
    pl = L(lambda d: ([d.rectangle((140 + i * 38, 700 + i * 28, 740 + i * 38, 1300 + i * 28), fill="#f4f4ee" if i % 2 else "#e4e6ea", outline="#8a8e9a", width=4) for i in range(12, -1, -1)], d.rectangle((140, 700, 740, 860), fill=PINK), [d.ellipse((x - 18, 660, x + 18, 740), fill="#8a8e9a") for x in (260, 440, 620)],
                      [d.rectangle((190 + c * 90, 900 + r * 90, 260 + c * 90, 970 + r * 90), fill="#e4e6ea") for r in range(3) for c in range(6)], d.polygon([(700, 560), (1020, 420), (980, 700), (860, 640)], fill="#f4f4ee", outline="#8a8e9a"), d.line([(720, 600), (990, 480)], fill="#b8bcc4", width=8)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 960, 420)), (1.0, pl, sway(4, 1.0))]


def delay():
    bg = _bg((30, 24, 56), (80, 56, 100))
    pl = L(lambda d: (d.rectangle((120, 540, 960, 1380), fill="#f4f4ee", outline="#8a8e9a"), d.rectangle((120, 540, 960, 700), fill=PINK), [d.ellipse((x - 20, 500, x + 20, 580), fill="#8a8e9a") for x in (300, 540, 780)],
                      [d.rectangle((160 + c * 114, 740 + r * 110, 250 + c * 114, 830 + r * 110), fill="#e4e6ea") for r in range(5) for c in range(7)], d.ellipse((140, 960, 270, 1090), outline=GRN, width=14),
                      d.arc((200, 780, 560, 1060), 200, 340, fill=RED_, width=16), d.polygon([(556, 900), (600, 960), (520, 960)], fill=RED_), d.arc((480, 780, 840, 1060), 200, 340, fill=RED_, width=16), d.polygon([(836, 900), (880, 960), (800, 960)], fill=RED_),
                      d.line([(640, 1180), (760, 1300)], fill=RED_, width=18), d.line([(760, 1180), (640, 1300)], fill=RED_, width=18)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 960, 460)), (1.0, pl, bob(5, 1.1))]


# ---------- 2: waiting ----------
def queue():
    bg = _bg((10, 14, 40), (50, 40, 90))
    pl = L(lambda d: (d.ellipse((780, 180, 940, 340), fill="#f4f4ee"), d.rectangle((0, 1560, W, H), fill="#1a2238"), d.rectangle((40, 560, 1040, 1560), fill="#2a2d48", outline="#0e1630", width=6), d.polygon([(40, 560), (1040, 560), (1000, 700), (80, 700)], fill=PINK),
                      [d.rectangle((40 + i * 142, 570, 40 + i * 142 + 71, 700), fill=(255, 255, 255, 70)) for i in range(0, 7, 2)], d.rectangle((120, 780, 960, 1400), fill="#ffd36a", outline="#8a6a10", width=8),
                      [d.rectangle((160 + i * 160, 820, 260 + i * 160, 1000), fill=c, outline="#16161a", width=4) for i, c in enumerate(("#3a6ac8", PINK, "#3aa86a", ORG, "#8a3ac8"))],
                      [(_sil(d, 90 + i * 130, 1700 + (i % 2) * 20, 1.5 + (i % 3) * .12, c), d.rectangle((90 + i * 130 - 14, 1700 + (i % 2) * 20 - 330, 90 + i * 130 + 14, 1700 + (i % 2) * 20 - 270), fill="#f4f4ee")) for i, c in enumerate(("#3a2d48", "#2a3a58", "#483a2d", "#2a4838", "#4a2d3a", "#2a2d38", "#38284a", "#2d3a4a"))]), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1000, 440)), (1.0, pl, bob(3, 1.0))]


def chart():
    bg = _bg((10, 30, 40), (30, 80, 90))
    pl = L(lambda d: (d.rectangle((90, 520, 760, 1300), fill="#f4f4ee", outline="#8a8e9a", width=10), d.line([(150, 1220), (700, 1220)], fill="#16161a", width=8), [d.rectangle((170 + i * 66, 1220 - (90 + i * 85), 220 + i * 66, 1220), fill=TEAL) for i in range(8)], d.line([(180, 1100), (700, 640)], fill=ORG, width=14), d.polygon([(700, 590), (770, 650), (690, 690)], fill=ORG),
                      d.rectangle((0, 1640, W, H), fill="#10303a"), N.suit(d, 880, 1700, 2.6, "#6a6e7a", "#2f6a8a"), d.line([(800, 1330), (720, 1050)], fill="#16161a", width=16)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1000, 440)), (1.0, pl, bob(4, 1.1))]


# ---------- 3: launch ----------
def shelf():
    bg = _bg((30, 14, 60), (90, 40, 110))
    def art(d):
        d.rectangle((300, 520, 780, 1240), fill="#ff9a6a", outline="#16161a", width=10); d.rectangle((300, 520, 780, 820), fill="#ff5d8f"); d.ellipse((440, 700, 640, 900), fill="#ffd36a"); d.rectangle((300, 1000, 780, 1240), fill="#241446")
        _palm(d, 350, 1000, 360, 20, "#16102a"); _palm(d, 740, 1000, 300, -20, "#16102a"); _vi(d, 540, 640, 0.38); _car(d, 540, 1180, 0.4)
    pl = L(lambda d: (d.rectangle((40, 1330, 1040, 1380), fill="#5a3e2a"), [d.rectangle((60 + i * 170, 1190, 210 + i * 170, 1330), fill=c, outline="#16161a", width=4) for i, c in enumerate(("#3a6ac8", "#c8453a", "#3aa86a", "#c8a43a", "#8a3ac8", "#3ac8c8"))], art(d), d.rectangle((40, 1700, 1040, 1750), fill="#5a3e2a"), [d.rectangle((60 + i * 170, 1560, 210 + i * 170, 1700), fill="#3a6ac8", outline="#16161a", width=4) for i in range(6)]), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 860, 480)), (1.0, pl, bob(5, 1.1)), (0, "sparkle", None)]


def score():
    bg = _bg((16, 30, 24), (40, 90, 60))
    pl = L(lambda d: (d.pieslice((120, 700, 960, 1540), 180, 360, fill="#2a3a2a", outline="#c8ccd4", width=10), d.pieslice((120, 700, 960, 1540), 180, 340, fill="#3fae5a"), d.pieslice((120, 700, 960, 1540), 340, 360, fill=GOLD), d.pieslice((260, 840, 820, 1400), 180, 360, fill="#10261a"),
                      d.line([(540, 1120), (860, 920)], fill="#f4f4ee", width=20), d.ellipse((500, 1080, 580, 1160), fill="#f4f4ee"),
                      [d.polygon([(190 + i * 175, 560), (206 + i * 175, 600), (250 + i * 175, 604), (216 + i * 175, 632), (228 + i * 175, 676), (190 + i * 175, 650), (152 + i * 175, 676), (164 + i * 175, 632), (130 + i * 175, 604), (174 + i * 175, 600)], fill=GOLD) for i in range(5)],
                      lucia(d, 200, 1760, 1.9), jason(d, 880, 1760, 1.9)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1000, 420)), (1.0, pl, bob(4, 1.0))]


# ---------- 4: stock ----------
def down():
    bg = _bg((40, 10, 16), (110, 30, 40))
    pl = L(lambda d: (_screen(d, 90, 480, 990, 1240, "#1a0a10"), d.line([(150, 1180), (150, 540)], fill="#c8ccd4", width=8), d.line([(150, 1180), (940, 1180)], fill="#c8ccd4", width=8), d.line([(190, 640), (360, 600), (480, 780), (620, 740), (780, 980), (920, 1080)], fill=RED_, width=18), d.polygon([(960, 1150), (800, 1120), (900, 1010)], fill=RED_),
                      d.rectangle((0, 1640, W, H), fill="#2a1018"), N.suit(d, 540, 1740, 2.7, "#6a6e7a", "#d6403a"), d.line([(430, 1280), (330, 1130)], fill="#6a6e7a", width=26), d.line([(650, 1280), (750, 1130)], fill="#6a6e7a", width=26)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 440)), (1.0, pl, bob(4, 1.1))]


def bet():
    bg = _bg((22, 16, 30), (60, 40, 70))
    pl = L(lambda d: (_screen(d, 140, 420, 940, 900, "#1a0a10"), d.line([(220, 560), (480, 640), (560, 760), (860, 840)], fill=RED_, width=16), d.polygon([(900, 830), (820, 820), (860, 760)], fill=RED_),
                      N.suit(d, 840, 1500, 2.3, "#3a3d48", "#6a6e7a"), d.rectangle((0, 1400, W, H), fill="#5a3e2a"), d.rectangle((0, 1400, W, 1440), fill="#7a5a3a"),
                      [[d.ellipse((cx - 100, 1520 - k * 32, cx + 100, 1568 - k * 32), fill=c, outline="#16161a", width=4) for k in range(n)] for cx, n, c in ((200, 5, RED_), (470, 9, "#2a2d38"), (720, 4, TEAL))]), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1000, 400)), (1.0, pl, bob(5, 1.1))]


# ---------- 5: the number ----------
def release():
    bg = _bg((14, 24, 50), (60, 70, 120))
    pl = L(lambda d: (d.rectangle((60, 700, 460, 1500), fill="#c8ccd4", outline="#6a6e7a", width=8), [d.rectangle((100 + c * 90, 760 + r * 110, 160 + c * 90, 840 + r * 110), fill="#ffd36a" if (r + c) % 3 else "#3a4a6a") for r in range(6) for c in range(4)], d.line([(260, 700), (260, 540)], fill="#6a6e7a", width=10), d.polygon([(260, 540), (400, 580), (260, 620)], fill=RED_),
                      d.rectangle((0, 1560, W, H), fill="#1a2238"), N.doc(d, 520, 620, 1000, 1360, 7, redact=(4,)), d.rectangle((520, 620, 1000, 700), fill=PINK), d.ellipse((780, 1160, 1040, 1420), fill="#c8372d", outline="#7a2018", width=8), d.ellipse((840, 1220, 980, 1360), outline="#f4f4ee", width=6)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(640, 940, 440)), (1.0, pl, bob(5, 1.1))]


def split():
    bg = _bg((16, 22, 50), (50, 70, 110))
    def shop(d, cx):
        d.rectangle((cx - 120, 1260, cx + 120, 1500), fill="#e8e6dc", outline="#8a8e9a", width=6); d.polygon([(cx - 140, 1260), (cx + 140, 1260), (cx + 110, 1190), (cx - 110, 1190)], fill=RED_); d.rectangle((cx - 40, 1360, cx + 40, 1500), fill="#5a3e2a")
    def console(d, cx):
        d.rectangle((cx - 110, 1330, cx + 110, 1500), fill="#2a2d38", outline="#05050a", width=6); d.ellipse((cx - 30, 1380, cx + 30, 1440), fill=TEAL); _pad_small(d, cx, 1260)
    def firm(d, cx):
        d.rectangle((cx - 90, 1180, cx + 90, 1500), fill="#3a4a6a", outline="#0e1630", width=6); [d.rectangle((cx - 60 + c * 70, 1220 + r * 90, cx - 20 + c * 70, 1270 + r * 90), fill="#ffd36a") for r in range(3) for c in range(2)]
    pl = L(lambda d: (_coin(d, 540, 700, 190), d.rectangle((530, 660, 550, 740), fill="#c89a20"), d.line([(430, 880), (260, 1130)], fill="#f4f4ee", width=40), d.polygon([(220, 1190), (300, 1120), (230, 1090)], fill="#f4f4ee"), d.line([(540, 900), (540, 1100)], fill="#f4f4ee", width=40), d.polygon([(540, 1170), (600, 1090), (480, 1090)], fill="#f4f4ee"), d.line([(650, 880), (830, 1130)], fill="#f4f4ee", width=12), d.polygon([(860, 1180), (860, 1090), (800, 1130)], fill="#f4f4ee"),
                      shop(d, 220), console(d, 540), firm(d, 860), d.rectangle((0, 1560, W, H), fill="#1a2238")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 960, 460)), (1.0, pl, bob(4, 1.0))]


def _pad_small(d, cx, cy):
    d.polygon([(cx - 70, cy - 20), (cx + 70, cy - 20), (cx + 100, cy + 40), (cx + 60, cy + 44), (cx + 30, cy + 10), (cx - 30, cy + 10), (cx - 60, cy + 44), (cx - 100, cy + 40)], fill="#e8e8f0", outline="#5a5e6a")


def big():
    bg = _bg((30, 20, 6), (110, 70, 20))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#3a2a0a"), [[_coin(d, 600 + c * 110 + (r % 2) * 55, 1610 - r * 62, 56) for c in range(4 - (r % 2))] for r in range(22)], N.suit(d, 190, 1700, 1.5, "#6a6e7a", "#2f6a8a"), d.polygon([(800, 160), (920, 320), (850, 320), (850, 420), (750, 420), (750, 320), (680, 320)], fill="#f4f4ee")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(760, 1100, 520)), (1.0, pl, bob(5, 1.0)), (0, "sparkle", None)]


REG = {"g6_" + k: v for k, v in dict(city=city, money=money, clock=clock, delay=delay, queue=queue, chart=chart, shelf=shelf, score=score, down=down, bet=bet, split=split, release=release, big=big).items()}
