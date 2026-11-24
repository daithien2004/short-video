"""Scenes for the Nvidia CEO news explainer: paper-cut icons and simple characters, no text in the drawings."""
import math
import story2 as S, story3 as X, chars_nv as N
from story2 import grad, fill_wave, W, H, CREAM, RED, GOLD, INK, EDGE
from scenes_hk2 import L, sway, bob

GN = N.GREEN_NV
NAVY0, NAVY1 = (14, 20, 44), (44, 60, 96)


def _bg(c0=NAVY0, c1=NAVY1): return grad(c0, c1).convert("RGBA")


def _table(d, y=1500):
    d.polygon([(-60, y), (W + 60, y), (W + 60, H), (-60, H)], fill="#5a3e2a", outline="#2a1a10"); d.polygon([(-60, y), (W + 60, y), (W + 60, y + 40), (-60, y + 40)], fill="#7a5a3a")


def _q(d, cx, cy, s, col="#f2f2ee"):
    d.arc((cx - 90 * s, cy - 150 * s, cx + 90 * s, cy - 10 * s), 200, 380, fill=col, width=int(44 * s)); d.line([(cx + 80 * s, cy - 60 * s), (cx, cy + 40 * s), (cx, cy + 80 * s)], fill=col, width=int(44 * s)); d.ellipse((cx - 26 * s, cy + 120 * s, cx + 26 * s, cy + 172 * s), fill=col)


# ---------- 1 ----------
def chip():
    bg = _bg((6, 24, 20), (30, 70, 40))
    pl = L(lambda d: (N.chip(d, 540, 900, 520), [d.line([(540 + dx, 900 + dy), (540 + dx * 2.2, 900 + dy * 2.2)], fill=GN, width=8) for dx, dy in ((-300, -300), (300, -300), (-300, 300), (300, 300), (0, -340), (0, 340), (-340, 0), (340, 0))]), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 520)), (1.0, pl, bob(6, 1.2)), (0, "sparkle", None)]


def press():
    bg = _bg()
    pl = L(lambda d: (N.doc(d, 180, 560, 900, 1360, 9, redact=(2, 3, 5)), d.rectangle((180, 560, 900, 640), fill=GN), d.ellipse((760, 1180, 1000, 1420), fill="#f4f4ee", outline="#8a8e9a", width=8), d.line([(880, 1300), (880, 1220)], fill="#16161a", width=10), d.line([(880, 1300), (930, 1330)], fill="#16161a", width=10)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 440)), (1.0, pl, bob(5, 1.1))]


def chair():
    bg = _bg((10, 12, 28), (36, 40, 70))
    pl = L(lambda d: (_table(d, 1560), [N.chair(d, x, 1700, 1.0, "#3a3a44") for x in (140, 940)], N.chair(d, 540, 1640, 2.6)), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 460)), (1.0, pl, None)]


# ---------- 2 ----------
def letter():
    bg = _bg((30, 30, 50), (90, 70, 90))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#3a3a44"), N.huang(d, 300, 1700, 3.4), d.polygon([(600, 900), (1000, 820), (1030, 1260), (630, 1340)], fill="#f4f4ee", outline="#8a8e9a"), [d.line([(660, 980 + i * 60), (960, 920 + i * 60)], fill="#b8bcc4", width=10) for i in range(5)]), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 420)), (1.0, pl, bob(3, 1.2))]


def inquiry():
    bg = _bg((14, 30, 40), (40, 80, 80))
    pl = L(lambda d: (d.polygon([(160, 1000), (460, 1000), (500, 940), (920, 940), (920, 1500), (160, 1500)], fill="#c8a45a", outline="#6a4a1a"), N.doc(d, 220, 1040, 860, 1440, 6), d.ellipse((520, 520, 960, 960), fill=(190, 230, 240, 120), outline="#c8ccd4", width=28), d.line([(880, 920), (1040, 1180)], fill="#c8ccd4", width=48)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(740, 740, 380)), (1.0, pl, sway(8, 1.0))]


def eye():
    bg = _bg((20, 10, 40), (60, 30, 80))
    pl = L(lambda d: (d.ellipse((190, 960, 890, 1660), fill="#2a6a9a", outline="#124a6a"), [d.arc((190, 960 + k * 60, 890, 1660 - k * 60), 0, 360, fill="#8ac0d8", width=6) for k in range(1, 6)], [d.arc((190 + k * 100, 960, 890 - k * 100, 1660), 0, 360, fill="#8ac0d8", width=6) for k in range(1, 4)],
                      d.polygon([(140, 680), (540, 520), (940, 680), (540, 840)], fill="#f4f4ee", outline="#8a8e9a"), d.ellipse((440, 590, 640, 790), fill="#c8372d"), d.ellipse((490, 640, 590, 740), fill="#16161a")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 700, 400)), (1.0, pl, bob(5, 1.0))]


# ---------- 3 ----------
def source():
    bg = _bg((20, 20, 30), (60, 60, 80))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#1a1a22"), N.shadow_figure(d, 460, 1700, 4.0), d.polygon([(560, 460), (1040, 460), (1040, 800), (700, 800), (620, 880), (640, 800), (560, 800)], fill=(200, 205, 215, 180), outline="#8a8e9a"), [d.line([(600, 540 + i * 70), (980 - i * 40, 540 + i * 70)], fill="#6a6e7a", width=22) for i in range(4)]), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(760, 620, 360)), (1.0, pl, bob(3, 0.9))]


def calendar():
    bg = _bg((24, 24, 48), (70, 50, 90))
    pl = L(lambda d: (d.rectangle((120, 540, 960, 1380), fill="#f4f4ee", outline="#8a8e9a"), d.rectangle((120, 540, 960, 700), fill="#c8372d"), [d.ellipse((x - 20, 500, x + 20, 580), fill="#8a8e9a") for x in (300, 540, 780)],
                      [d.rectangle((160 + c * 114, 740 + r * 110, 250 + c * 114, 830 + r * 110), fill="#e4e6ea") for r in range(5) for c in range(7)], d.rectangle((160 + 1 * 114, 740 + 2 * 110, 250 + 1 * 114, 830 + 2 * 110), fill=GN), d.rectangle((160 + 1 * 114, 740 + 3 * 110, 250 + 1 * 114, 830 + 3 * 110), fill=GN),
                      d.line([(205, 900), (560, 960), (205, 1010)], fill="#16161a", width=10)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 960, 460)), (1.0, pl, bob(5, 1.1))]


def vote():
    bg = _bg((30, 24, 20), (90, 60, 40))
    pl = L(lambda d: (d.rectangle((0, 1540, W, H), fill="#5a3e2a"), d.rectangle((200, 1100, 700, 1560), fill="#c8a45a", outline="#6a4a1a"), d.rectangle((300, 1100, 600, 1140), fill="#16161a"), d.polygon([(380, 1020), (520, 1020), (500, 1100), (400, 1100)], fill="#f4f4ee", outline="#8a8e9a"),
                      d.rectangle((640, 1420, 960, 1500), fill="#8a5a2a", outline="#4a2e12"), d.rectangle((660, 1360, 940, 1430), fill="#6a3e1a"), d.polygon([(780, 1360), (860, 1360), (860, 1180), (780, 1180)], fill="#8a5a2a"), d.rectangle((720, 1130, 920, 1220), fill="#6a3e1a", outline="#2a1a10")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1100, 400)), (1.0, pl, bob(4, 1.0))]


# ---------- 4 ----------
def gov():
    bg = _bg((20, 30, 60), (70, 90, 130))
    pl = L(lambda d: (N.capitol(d, 540, 1000, 900, 560), d.rectangle((300, 1360, 780, 1700), fill="#2a3f5a", outline="#0e1630"), [d.rectangle((330 + c * 100, 1390 + r * 100, 400 + c * 100, 1450 + r * 100), fill="#8ac0d8") for r in range(3) for c in range(4)], d.polygon([(540, 1100), (610, 1180), (570, 1180), (570, 1300), (510, 1300), (510, 1180), (470, 1180)], fill=GN)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 800, 400)), (1.0, pl, bob(4, 1.0))]


def shield():
    bg = _bg((6, 24, 20), (30, 70, 50))
    pl = L(lambda d: (N.chip(d, 760, 600, 240), d.polygon([(540, 760), (900, 860), (880, 1320), (540, 1640), (200, 1320), (180, 860)], fill=GN, outline="#3a6a00"), d.polygon([(540, 820), (840, 900), (820, 1300), (540, 1560), (260, 1300), (240, 900)], fill="#16161a"), d.line([(380, 1200), (500, 1320), (720, 1020)], fill="#f4f4ee", width=60)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1200, 480)), (1.0, pl, bob(5, 1.0)), (0, "sparkle", None)]


def question():
    bg = _bg((24, 20, 40), (80, 70, 100))
    pl = L(lambda d: (_table(d, 1560), N.suit(d, 200, 1700, 2.2), N.suit(d, 540, 1700, 2.2, "#4a5a6a", "#c8372d"), N.suit(d, 880, 1700, 2.2, "#6a5a4a", "#2f6a8a")), 10, 8)
    q = L(lambda d: _q(d, 540, 760, 2.4), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 760, 420)), (1.0, pl, bob(2, 1.0)), (0.9, q, bob(8, 1.4))]


# ---------- 5 ----------
def phone():
    bg = _bg((30, 30, 60), (90, 80, 130))
    pl = L(lambda d: (d.rectangle((280, 420, 800, 1500), fill="#16161a", outline="#05050a"), d.rectangle((310, 500, 770, 1420), fill="#2a3f7a"), d.rectangle((460, 450, 620, 470), fill="#3a3a44"),
                      d.polygon([(340, 640), (740, 640), (740, 1000), (560, 1000), (480, 1080), (500, 1000), (340, 1000)], fill="#f4f4ee"), [d.line([(380, 720 + i * 70), (700 - (i % 2) * 90, 720 + i * 70)], fill="#8a8e9a", width=26) for i in range(4)],
                      d.polygon([(340, 1100), (480, 1100), (440, 1200), (390, 1200)], fill=GN), d.polygon([(500, 1100), (640, 1100), (600, 1200), (550, 1200)], fill=GN)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 960, 460)), (1.0, pl, bob(6, 1.2))]


def trump_pod():
    bg = _bg((30, 40, 80), (80, 100, 150))
    pl = L(lambda d: (N.flag(d, 100, 520, 560, 340), d.line([(100, 520), (100, 1700)], fill="#8a8e9a", width=14), N.trump(d, 640, 1640, 3.4), d.polygon([(380, 1380), (900, 1380), (940, 1700), (340, 1700)], fill="#5a3e2a", outline="#2a1a10"), d.rectangle((380, 1380, 900, 1420), fill="#7a5a3a")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(640, 900, 440)), (1.0, pl, bob(3, 1.0))]


def stamp():
    bg = _bg((30, 24, 40), (80, 60, 90))
    pl = L(lambda d: (N.doc(d, 200, 520, 880, 1420, 9), d.polygon([(260, 900), (840, 780), (880, 960), (300, 1080)], outline="#c8372d", fill=None, width=22) if False else None, d.line([(260, 900), (840, 780), (880, 960), (300, 1080), (260, 900)], fill="#c8372d", width=24), d.line([(330, 960), (800, 860)], fill="#c8372d", width=14), d.line([(350, 1020), (820, 920)], fill="#c8372d", width=14)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 960, 440)), (1.0, pl, bob(4, 1.0))]


# ---------- 6 ----------
def plane():
    bg = _bg((50, 90, 150), (190, 220, 240))
    cl = L(lambda d: [d.ellipse((x - r, y - r * .5, x + r, y + r * .5), fill=(255, 255, 255, 220)) for x, y, r in ((200, 1300, 220), (860, 1500, 260), (540, 700, 200))], 0, 0)
    pl = L(lambda d: (d.polygon([(120, 960), (800, 900), (980, 940), (800, 990), (120, 1000)], fill="#f4f4ee", outline="#8a8e9a"), d.polygon([(420, 940), (640, 600), (700, 620), (620, 940)], fill="#d4d8e0", outline="#8a8e9a"), d.polygon([(420, 990), (640, 1330), (700, 1310), (620, 990)], fill="#d4d8e0", outline="#8a8e9a"), d.polygon([(140, 960), (60, 780), (140, 780), (230, 950)], fill="#2a3f7a"), d.rectangle((760, 930, 940, 960), fill="#2a3f7a")), 12, 10)
    return bg.convert("RGB"), [(0.3, cl, lambda t: (-40 * (t % 4), 0)), (1.0, pl, bob(10, 1.1))]


def letters():
    bg = _bg((20, 30, 60), (70, 90, 130))
    pl = L(lambda d: (N.capitol(d, 400, 1500, 700, 440), [(d.rectangle((x, y, x + 300, y + 200), fill="#f4f4ee", outline="#8a8e9a"), d.polygon([(x, y), (x + 150, y + 110), (x + 300, y)], fill="#e4e6ea", outline="#8a8e9a")) for x, y in ((560, 560), (480, 880))], N.chip(d, 800, 1360, 200)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 420)), (1.0, pl, bob(5, 1.0))]


def chip_china():
    bg = _bg((14, 30, 60), (50, 80, 120))
    pl = L(lambda d: (d.polygon([(40, 900), (300, 780), (420, 900), (400, 1100), (200, 1180), (60, 1080)], fill="#3a7a5a", outline="#1a4a2a"), d.polygon([(640, 860), (900, 780), (1040, 900), (1000, 1100), (780, 1180), (640, 1020)], fill="#c8372d", outline="#7a2018"),
                      d.arc((200, 520, 880, 1080), 200, 340, fill=GN, width=24), d.polygon([(860, 800), (900, 880), (820, 880)], fill=GN), N.chip(d, 540, 640, 200)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 700, 380)), (1.0, pl, bob(4, 1.2))]


# ---------- 7 ----------
def chart_down():
    bg = _bg((40, 10, 20), (110, 30, 40))
    pl = L(lambda d: (d.rectangle((100, 520, 980, 1480), fill=(20, 20, 30, 230), outline="#8a8e9a"), [d.line([(100, 520 + i * 160), (980, 520 + i * 160)], fill="#3a3d48", width=4) for i in range(7)],
                      d.line([(140, 640), (280, 600), (380, 720), (500, 700), (600, 980), (700, 1060), (800, 1320), (940, 1400)], fill="#e8402a", width=22), [d.line([(x, y - 40), (x, y + 60)], fill="#e8402a", width=8) for x, y in ((280, 600), (500, 700), (700, 1060), (940, 1400))],
                      d.polygon([(900, 1500), (1000, 1500), (950, 1640)], fill="#e8402a")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 960, 460)), (1.0, pl, bob(5, 1.2))]


def chart_up():
    bg = _bg((6, 30, 20), (30, 100, 50))
    pl = L(lambda d: (d.rectangle((100, 520, 980, 1480), fill=(10, 24, 20, 230), outline="#8a8e9a"), [d.line([(100, 520 + i * 160), (980, 520 + i * 160)], fill="#2a4a3a", width=4) for i in range(7)],
                      d.line([(140, 1400), (300, 1380), (460, 1340), (560, 1320), (640, 900), (720, 680), (860, 620), (940, 600)], fill=GN, width=24), d.polygon([(940, 520), (1010, 640), (870, 640)], fill=GN)), 12, 10)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(760, 800, 460)), (1.0, pl, bob(6, 1.3)), (0, "sparkle", None)]


# ---------- 8 ----------
def _gear(d, cx, cy, r, col, teeth=10):
    pts = []
    for k in range(teeth * 2):
        a = k * math.pi / teeth; rr = r if k % 2 == 0 else r * .8; pts += [(cx + rr * math.cos(a - .12), cy + rr * math.sin(a - .12)), (cx + rr * math.cos(a + .12), cy + rr * math.sin(a + .12))]
    d.polygon(pts, fill=col, outline="#0a0a10"); d.ellipse((cx - r * .3, cy - r * .3, cx + r * .3, cy + r * .3), fill="#16161a")


def gears():
    bg = _bg((20, 24, 36), (60, 70, 90))
    pl = L(lambda d: (_gear(d, 380, 860, 300, "#8a8e9a"), _gear(d, 780, 1160, 220, "#6a7a9a", 8), _gear(d, 360, 1400, 160, "#c8a45a", 7), [d.polygon([(x, y), (x + 60, y + 100), (x - 60, y + 100)], fill=GN) for x, y in ((900, 560), (780, 540), (660, 560))]), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 420)), (1.0, pl, sway(6, 1.0))]


def huang_back():
    bg = _bg((10, 20, 30), (40, 70, 70))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#1a1a22"), N.chair(d, 700, 1700, 2.0, "#2a2a32"), N.huang(d, 420, 1700, 3.6), N.chip(d, 860, 1300, 180)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(500, 900, 420)), (1.0, pl, bob(3, 1.0))]


def december():
    bg = _bg((24, 30, 60), (80, 90, 130))
    pl = L(lambda d: (N.capitol(d, 540, 1120, 760, 420), d.rectangle((140, 1180, 940, 1700), fill="#f4f4ee", outline="#8a8e9a"), d.rectangle((140, 1180, 940, 1280), fill="#c8372d"),
                      [d.rectangle((170 + c * 110, 1320 + r * 70, 250 + c * 110, 1380 + r * 70), fill="#e4e6ea") for r in range(5) for c in range(7)], d.rectangle((170 + 0 * 110, 1320, 250, 1380), fill=GN), d.rectangle((170 + 2 * 110, 1320 + 0 * 70, 250 + 2 * 110, 1380), fill=GN),
                      d.rectangle((520, 1500, 540, 1700), fill="#8a8e9a"), d.ellipse((490, 1440, 570, 1520), fill="#16161a")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 420)), (1.0, pl, bob(4, 1.0))]



def boardroom():
    bg = _bg((20, 24, 44), (70, 80, 110))
    pl = L(lambda d: (_table(d, 1500), N.suit(d, 150, 1640, 2.0), N.suit(d, 400, 1660, 2.0, "#4a5a6a", "#c8372d"), N.suit(d, 680, 1660, 2.0, "#6a5a4a", "#2f6a8a"), N.suit(d, 940, 1640, 2.0, "#5a4a6a", GN),
                      d.rectangle((440, 1520, 640, 1640), fill="#c8a45a", outline="#6a4a1a"), d.polygon([(440, 1520), (510, 1520), (525, 1490), (640, 1490), (640, 1520)], fill="#d8b46a", outline="#6a4a1a")), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 800, 400)), (1.0, pl, bob(2, 1.0))]


def deal():
    bg = _bg((30, 24, 50), (90, 70, 110))
    pl = L(lambda d: (N.doc(d, 160, 520, 920, 1440, 8), d.line([(240, 1260), (420, 1220), (520, 1290), (640, 1230)], fill="#1f2f8a", width=10), d.line([(560, 1360), (860, 1360)], fill="#16161a", width=6),
                      d.polygon([(700, 1100), (740, 1080), (980, 1420), (940, 1440)], fill=GOLD, outline="#8a6a20"), d.polygon([(940, 1440), (980, 1420), (990, 1500)], fill="#16161a")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 440)), (1.0, pl, bob(5, 1.1))]


def mics():
    bg = _bg((26, 20, 44), (80, 60, 100))
    pl = L(lambda d: (d.rectangle((0, 1500, W, H), fill="#5a3e2a"), d.rectangle((0, 1500, W, 1540), fill="#7a5a3a"), [(d.rectangle((x - 8, 1180, x + 8, 1500), fill="#8a8e9a"), d.ellipse((x - 46, 1060, x + 46, 1190), fill="#c8ccd4", outline="#6a6e7a"), d.rectangle((x - 46, 1100, x + 46, 1120), fill="#6a6e7a")) for x in (220, 540, 860)],
                      d.rectangle((420, 1420, 660, 1500), fill="#8a5a2a", outline="#4a2e12"), d.rectangle((460, 1370, 620, 1430), fill="#6a3e1a")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1100, 420)), (1.0, pl, bob(3, 1.0))]


def coins():
    bg = _bg((30, 50, 20), (110, 130, 40))
    pl = L(lambda d: ([[d.ellipse((x - 120, 1600 - k * 56 - 40, x + 120, 1600 - k * 56 + 30), fill="#f2c24a", outline="#8a6a20") for k in range(n)] for x, n in ((220, 2), (540, 6), (860, 11))], d.polygon([(540, 460), (700, 640), (600, 640), (600, 820), (480, 820), (480, 640), (380, 640)], fill=GN, outline="#3a6a00")), 12, 10)
    return bg.convert("RGB"), [(0, "rays", X.rays_simple()), (0, "glow", S.sword_glow(540, 1100, 440)), (1.0, pl, bob(5, 1.2)), (0, "sparkle", None)]


def scale():
    bg = _bg((24, 24, 44), (80, 70, 100))
    pl = L(lambda d: (d.rectangle((520, 640, 560, 1640), fill="#8a8e9a"), d.polygon([(420, 1640), (660, 1640), (600, 1560), (480, 1560)], fill="#6a6e7a"), d.polygon([(200, 790), (860, 650), (860, 690), (200, 830)], fill="#c8a45a", outline="#6a4a1a"),
                      d.line([(200, 810), (120, 1100)], fill="#8a8e9a", width=8), d.line([(200, 810), (300, 1100)], fill="#8a8e9a", width=8), d.pieslice((100, 960, 320, 1180), 0, 180, fill="#c8a45a", outline="#6a4a1a"), [d.ellipse((130 + k * 40, 1070 - (k % 2) * 30, 190 + k * 40, 1110 - (k % 2) * 30), fill="#f2c24a", outline="#8a6a20") for k in range(4)],
                      d.line([(860, 670), (780, 640)], fill="#8a8e9a", width=8), d.line([(860, 670), (940, 640)], fill="#8a8e9a", width=8), d.pieslice((720, 520, 1000, 700), 0, 180, fill="#c8a45a", outline="#6a4a1a")), 12, 10)
    q = L(lambda d: _q(d, 860, 440, .9), 10, 8)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 420)), (1.0, pl, bob(4, 1.0)), (0.9, q, bob(6, 1.3))]


REG = {"nv_" + k: v for k, v in dict(chip=chip, press=press, chair=chair, letter=letter, inquiry=inquiry, eye=eye, source=source, calendar=calendar, vote=vote, gov=gov, shield=shield, question=question,
          phone=phone, trump=trump_pod, stamp=stamp, plane=plane, letters=letters, chip_china=chip_china, chart_down=chart_down, chart_up=chart_up, gears=gears, boardroom=boardroom, deal=deal, mics=mics, coins=coins, scale=scale, huang_back=huang_back, december=december).items()}
