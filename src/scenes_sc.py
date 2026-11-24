"""Scenes for the 'scam story' genre (first story: the lucky-wheel scam, Tuyên Quang, Nov 2026). Paper-cut people and props, no text, no real faces."""
import math
import story2 as S
from story2 import grad, W, H, GOLD
from scenes_hk2 import L, sway, bob
import chars_nv as N
from chars_st import _p, _eyes

PINK, TEAL, RED_, ORG, GRN = "#ff5d8f", "#2ec4b6", "#d6403a", "#ff9a3c", "#3fae5a"


def _bg(c0=(24, 22, 52), c1=(70, 60, 110)): return grad(c0, c1).convert("RGBA")


def _coin(d, cx, cy, r): d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GOLD, outline="#8a6a10", width=6); d.ellipse((cx - r * .62, cy - r * .62, cx + r * .62, cy + r * .62), outline="#c89a20", width=5)


def _bill(d, x, y, w=300, h=130):
    d.rectangle((x, y, x + w, y + h), fill="#5cc06a", outline="#1f6a30", width=5); d.ellipse((x + w / 2 - h * .3, y + h * .2, x + w / 2 + h * .3, y + h * .8), fill="#8ae09a", outline="#1f6a30", width=4)


def _q(d, cx, cy, s, col="#f2f2ee"):
    d.arc((cx - 90 * s, cy - 150 * s, cx + 90 * s, cy - 10 * s), 200, 380, fill=col, width=int(44 * s)); d.line([(cx + 80 * s, cy - 60 * s), (cx, cy + 40 * s), (cx, cy + 80 * s)], fill=col, width=int(44 * s)); d.ellipse((cx - 26 * s, cy + 120 * s, cx + 26 * s, cy + 172 * s), fill=col)


def _bubble(d, x0, y0, x1, y1, fill="#f4f4ee", tail=None):
    d.rectangle((x0, y0, x1, y1), fill=fill, outline="#8a8e9a", width=5)
    if tail: d.polygon([tail[0], tail[1], tail[2]], fill=fill, outline="#8a8e9a")


def person(d, cx, base, s, top, bot, hair, skin="#e0b080", worried=False, cap=None, skirt=False):
    p = _p(cx, base, s)
    if skirt: d.polygon([p(-56, -52), p(-34, -150), p(34, -150), p(56, -52)], fill=bot)
    else: d.rectangle((*p(-24, -66), *p(-4, 0)), fill=bot); d.rectangle((*p(4, -66), *p(24, 0)), fill=bot)
    if skirt: d.rectangle((*p(-20, -52), *p(-6, 0)), fill=skin); d.rectangle((*p(6, -52), *p(20, 0)), fill=skin)
    d.polygon([p(-50, -62), p(-38, -152), p(38, -152), p(50, -62)], fill=top, outline="#2a2d38")
    d.ellipse((*p(-28, -216), *p(28, -148)), fill=skin); _eyes(d, p, -190)
    if worried: d.arc((*p(-10, -168), *p(10, -154)), 200, 340, fill="#7a2a2a", width=max(int(3 * s), 2)); d.line([p(-22, -204), p(-8, -208)], fill="#3a2a2a", width=max(int(3 * s), 2)); d.line([p(22, -204), p(8, -208)], fill="#3a2a2a", width=max(int(3 * s), 2))
    else: d.arc((*p(-10, -176), *p(10, -160)), 20, 160, fill="#7a2a2a", width=max(int(3 * s), 2))
    if cap: d.polygon([p(-32, -200), p(-30, -228), p(0, -238), p(30, -228), p(32, -200), p(44, -196), p(-44, -196)], fill=cap); d.rectangle((*p(-34, -204), *p(34, -196)), fill="#16161a")
    else:
        d.polygon([p(-30, -202), p(-26, -230), p(0, -240), p(26, -230), p(30, -202), p(16, -214), p(-16, -214)], fill=hair)
        if skirt: d.ellipse((*p(-14, -252), *p(14, -226)), fill=hair)


def woman(d, cx, base, s, worried=False): person(d, cx, base, s, "#e87a9a", "#3a4a6a", "#2a1a14", "#e0b080", worried, None, True)
def teller(d, cx, base, s): person(d, cx, base, s, "#2a6ac8", "#2a2d38", "#2a1a14", "#d49a70")
def officer(d, cx, base, s): person(d, cx, base, s, "#3a6a4a", "#2a3a2a", "#2a1a14", "#d49a70", False, "#3a6a4a")


def _phone(d, x0, y0, x1, y1):
    d.rectangle((x0, y0, x1, y1), fill="#16161a", outline="#8a8e9a", width=8)
    d.rectangle((x0 + 30, y0 + 70, x1 - 30, y1 - 70), fill="#eef2f8")


# ---------- 1 ----------
def phone():
    bg = _bg((22, 30, 60), (60, 90, 140))
    pl = L(lambda d: (_phone(d, 220, 380, 860, 1560), d.ellipse((290, 470, 380, 560), fill="#c8ccd4"), d.polygon([(280, 600), (290, 560), (380, 560), (390, 600)], fill="#c8ccd4"),
                      _bubble(d, 300, 640, 700, 780, "#dfe4ee"), _bubble(d, 380, 830, 780, 970, PINK), _bubble(d, 300, 1020, 640, 1160, "#dfe4ee"),
                      d.ellipse((420, 1230, 560, 1330), outline="#3a6ac8", width=18), d.ellipse((520, 1230, 660, 1330), outline="#3a6ac8", width=18)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 960, 440)), (1.0, pl, bob(4, 1.1))]


def wheel():
    bg = _bg((50, 14, 70), (140, 50, 110))
    cols = (RED_, GOLD, TEAL, "#6a8aff", PINK, ORG, GRN, "#b46aff")
    pl = L(lambda d: ([d.pieslice((140, 560, 940, 1360), k * 45, (k + 1) * 45, fill=c, outline="#f4f4ee", width=6) for k, c in enumerate(cols)], d.ellipse((470, 890, 610, 1030), fill="#f4f4ee", outline="#8a8e9a", width=8),
                      d.polygon([(540, 520), (590, 600), (490, 600)], fill="#f4f4ee", outline="#8a8e9a"), [d.ellipse((540 + 410 * math.cos(math.radians(k * 22.5)) - 12, 960 + 410 * math.sin(math.radians(k * 22.5)) - 12, 540 + 410 * math.cos(math.radians(k * 22.5)) + 12, 960 + 410 * math.sin(math.radians(k * 22.5)) + 12), fill=GOLD) for k in range(16)]), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 960, 480)), (1.0, pl, sway(6, 1.0)), (0, "sparkle", None)]


def pay():
    bg = _bg((30, 24, 50), (80, 60, 100))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#1a1a28"), woman(d, 230, 1740, 3.2, True), N.shadow_figure(d, 850, 1740, 3.2), [_coin(d, 400 + i * 80, 1080 - i * (4 - i) * 24, 44) for i in range(5)],
                      d.polygon([(700, 880), (770, 940), (690, 960)], fill=GOLD), d.rectangle((150, 1420, 290, 1560), fill="#16161a", outline="#8a8e9a", width=5)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1000, 420)), (1.0, pl, bob(4, 1.0))]


# ---------- 2 ----------
def gift():
    bg = _bg((26, 22, 40), (60, 50, 80))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#1a1a28"), d.rectangle((140, 1100, 600, 1560), fill=PINK, outline="#7a1a4a", width=8), d.polygon([(110, 1100), (630, 1100), (680, 980), (170, 920)], fill="#ff8aaa", outline="#7a1a4a"), d.rectangle((340, 1100, 400, 1560), fill=GOLD), d.rectangle((160, 1160, 580, 1520), fill="#2a1a30"),
                      _q(d, 370, 1360, 0.6, "#8a8e9a"), woman(d, 850, 1740, 3.2, True)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1100, 400)), (1.0, pl, bob(4, 1.0))]


def demand():
    bg = _bg((40, 14, 24), (110, 30, 50))
    pl = L(lambda d: (_phone(d, 80, 420, 520, 1260), _bubble(d, 120, 560, 480, 720, "#dfe4ee"), _bubble(d, 140, 800, 480, 960, RED_), d.rectangle((0, 1640, W, H), fill="#2a1018"), [_bill(d, 660 + (i % 2) * 10, 1560 - (i + 1) * 40, 340, 110) for i in range(14)],
                      d.polygon([(560, 900), (640, 860), (640, 940)], fill="#f4f4ee"), d.polygon([(800, 380), (860, 520), (740, 520)], fill="#f4f4ee"), d.rectangle((785, 530, 815, 600), fill="#f4f4ee")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(780, 1100, 440)), (1.0, pl, bob(5, 1.1))]


# ---------- 3 ----------
def bank():
    bg = _bg((20, 30, 60), (70, 100, 150))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#2a3a58"), d.polygon([(100, 760), (540, 480), (980, 760)], fill="#e8e6dc", outline="#8a8e9a", width=6), d.rectangle((100, 760, 980, 840), fill="#c8ccd4", outline="#8a8e9a", width=6), [d.rectangle((150 + i * 170, 840, 220 + i * 170, 1460), fill="#f4f2e8", outline="#8a8e9a", width=5) for i in range(6)],
                      d.rectangle((100, 1460, 980, 1520), fill="#c8ccd4"), d.rectangle((60, 1520, 1020, 1600), fill="#b8bcc4"), d.rectangle((420, 640, 660, 720), fill="#2a6ac8"), d.ellipse((490, 560, 590, 660), fill=GOLD)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 460)), (1.0, pl, bob(3, 1.0))]


def counter():
    bg = _bg((24, 34, 60), (60, 90, 130))
    pl = L(lambda d: (teller(d, 760, 1560, 3.1), d.rectangle((0, 1300, W, 1480), fill="#8a6a3a", outline="#4a3a1a", width=6), d.rectangle((0, 1480, W, H), fill="#5a4a2a"), d.rectangle((0, 1180, W, 1300), fill=(190, 230, 240, 90), outline="#c8ccd4", width=5), woman(d, 250, 1780, 3.4, True), d.rectangle((560, 1240, 700, 1300), fill="#5cc06a", outline="#1f6a30", width=4)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 440)), (1.0, pl, bob(3, 1.0))]


# ---------- 4 ----------
def teller_ask():
    bg = _bg((20, 40, 80), (60, 110, 170))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#2a3a58"), teller(d, 540, 1740, 3.8), d.ellipse((160, 380, 920, 900), fill="#f4f4ee", outline="#8a8e9a", width=8), d.polygon([(480, 880), (540, 1020), (600, 880)], fill="#f4f4ee", outline="#8a8e9a"), _q(d, 540, 700, 1.1, "#2a6ac8"), _coin(d, 250, 480, 40), _coin(d, 830, 480, 40)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 800, 440)), (1.0, pl, bob(4, 1.0))]


def police():
    bg = _bg((14, 34, 24), (40, 90, 60))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#10261a"), officer(d, 300, 1740, 3.4), teller(d, 780, 1740, 3.4), woman(d, 540, 1740, 2.6, False), d.polygon([(540, 240), (700, 300), (700, 460), (540, 560), (380, 460), (380, 300)], fill="#2a6a4a", outline="#f4f4ee"), d.polygon([(540, 320), (572, 400), (656, 400), (588, 450), (614, 530), (540, 480), (466, 530), (492, 450), (424, 400), (508, 400)], fill=GOLD)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 440)), (1.0, pl, bob(4, 1.0))]


def stop():
    bg = _bg((40, 12, 20), (100, 30, 40))
    pl = L(lambda d: (_phone(d, 260, 600, 820, 1500), d.rectangle((330, 1180, 750, 1300), fill=TEAL, outline="#0a4a44", width=6), d.polygon([(540, 330), (700, 400), (770, 560), (700, 720), (540, 790), (380, 720), (310, 560), (380, 400)], fill=RED_, outline="#f4f4ee", width=10), d.rectangle((420, 540, 660, 600), fill="#f4f4ee")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 700, 440)), (1.0, pl, bob(5, 1.1))]


# ---------- 5 ----------
def bait():
    bg = _bg((10, 30, 50), (30, 90, 120))
    pl = L(lambda d: (d.rectangle((0, 1240, W, H), fill="#0e3a50"), d.line([(540, 0), (540, 900)], fill="#f4f4ee", width=8), d.arc((470, 880, 610, 1010), 0, 200, fill="#c8ccd4", width=14), _coin(d, 540, 1090, 70),
                      d.ellipse((120, 1380, 720, 1640), fill=PINK, outline="#7a1a4a", width=8), d.polygon([(700, 1510), (900, 1380), (900, 1640)], fill=PINK, outline="#7a1a4a"), d.ellipse((220, 1440, 270, 1490), fill="#f4f4ee"), d.ellipse((232, 1452, 258, 1478), fill="#16161a"), d.polygon([(120, 1480), (240, 1520), (120, 1560)], fill="#7a1a4a")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1100, 420)), (1.0, pl, sway(5, 1.0))]


def shield():
    bg = _bg((14, 34, 40), (40, 100, 100))
    pl = L(lambda d: (d.arc((330, 520, 750, 960), 180, 360, fill="#c8ccd4", width=60), d.line([(330, 740), (330, 880)], fill="#c8ccd4", width=60), d.line([(750, 740), (750, 880)], fill="#c8ccd4", width=60), d.rectangle((250, 840, 830, 1400), fill=GOLD, outline="#8a6a10", width=10), d.ellipse((490, 1020, 590, 1120), fill="#16161a"), d.rectangle((520, 1100, 560, 1240), fill="#16161a"),
                      d.line([(150, 1560), (260, 1660), (440, 1480)], fill=GRN, width=40)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1000, 440)), (1.0, pl, bob(4, 1.0))]


REG = {"sc_" + k: v for k, v in dict(phone=phone, wheel=wheel, pay=pay, gift=gift, demand=demand, bank=bank, counter=counter, teller=teller_ask, police=police, stop=stop, bait=bait, shield=shield).items()}
