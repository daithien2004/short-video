"""More scenes for the scam story genre: one drawing per sentence so the picture shows what the voice says."""
import story2 as S
from story2 import W, H, GOLD
from scenes_hk2 import L, sway, bob
import chars_nv as N
from scenes_sc import _bg, _coin, _q, _bubble, _phone, woman, teller, officer, PINK, TEAL, RED_, ORG, GRN


def _avatar(d, cx, cy, r, col):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col, outline="#f4f4ee", width=5); d.ellipse((cx - r * .32, cy - r * .5, cx + r * .32, cy + r * .14), fill="#f4f4ee")
    d.polygon([(cx - r * .62, cy + r * .78), (cx - r * .5, cy + r * .2), (cx + r * .5, cy + r * .2), (cx + r * .62, cy + r * .78)], fill="#f4f4ee")


def group():
    bg = _bg((22, 30, 60), (60, 90, 150))
    cols = (PINK, TEAL, ORG, "#6a8aff", GRN, "#b46aff", RED_, GOLD, "#3aa8c8")
    pl = L(lambda d: (_phone(d, 180, 360, 900, 1600), d.rectangle((210, 430, 870, 540), fill="#3a6ac8"), [_avatar(d, 330 + (i % 3) * 210, 700 + (i // 3) * 230, 80, c) for i, c in enumerate(cols)],
                      d.rectangle((210, 1420, 870, 1530), fill="#dfe4ee", outline="#8a8e9a", width=4), d.line([(500, 1475), (580, 1475)], fill=TEAL, width=14), d.line([(540, 1435), (540, 1515)], fill=TEAL, width=14)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 960, 440)), (1.0, pl, bob(4, 1.1))]


def play():
    bg = _bg((50, 14, 70), (120, 40, 110))
    cols = (RED_, GOLD, TEAL, "#6a8aff", PINK, ORG, GRN, "#b46aff")
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#1a1028"), woman(d, 220, 1740, 3.3), _phone(d, 480, 520, 960, 1500), [d.pieslice((530, 700, 910, 1080), k * 45, (k + 1) * 45, fill=c, outline="#f4f4ee", width=4) for k, c in enumerate(cols)],
                      d.polygon([(720, 670), (750, 720), (690, 720)], fill="#f4f4ee"), d.rectangle((560, 1200, 880, 1320), fill=TEAL, outline="#0a4a44", width=5)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(700, 900, 420)), (1.0, pl, bob(4, 1.0)), (0, "sparkle", None)]


def repeat():
    bg = _bg((30, 24, 50), (80, 60, 100))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#1a1a28"),
                      [(_phone(d, 70 + i * 330, 560 + i * 60, 330 + i * 330, 1160 + i * 60), d.rectangle((100 + i * 330, 1000 + i * 60, 300 + i * 330, 1080 + i * 60), fill=TEAL), [_coin(d, 200 + i * 330, 820 + i * 60 - k * 90, 40) for k in range(2)]) for i in range(3)],
                      d.polygon([(380, 1560), (700, 1560), (760, 1380), (320, 1380)], fill="#c8a45a", outline="#6a4a1a", width=6), _coin(d, 540, 1470, 60)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1000, 440)), (1.0, pl, bob(4, 1.0))]


def check():
    bg = _bg((14, 30, 40), (40, 80, 80))
    pl = L(lambda d: (N.doc(d, 160, 560, 760, 1360, 8), d.rectangle((160, 560, 760, 650), fill="#3a6ac8"), d.ellipse((520, 880, 900, 1260), fill=(190, 230, 240, 110), outline="#c8ccd4", width=30), d.line([(860, 1220), (1020, 1440)], fill="#c8ccd4", width=56),
                      d.polygon([(250, 1480), (330, 1420), (330, 1540)], fill=GOLD), d.line([(330, 1480), (700, 1480)], fill=GOLD, width=20), _coin(d, 800, 1480, 60)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(640, 1000, 400)), (1.0, pl, bob(4, 1.0))]


def call():
    bg = _bg((20, 40, 80), (60, 110, 170))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#2a3a58"), teller(d, 400, 1740, 3.6), d.polygon([(500, 960), (570, 930), (610, 1060), (540, 1090)], fill="#16161a", outline="#8a8e9a", width=4),
                      [d.arc((560 + k * 60, 800 - k * 50, 880 + k * 60, 1120 + k * 50), -50, 50, fill="#f4f4ee", width=18) for k in range(3)], officer(d, 880, 1740, 1.8)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 440)), (1.0, pl, bob(4, 1.0))]


def explain():
    bg = _bg((14, 34, 24), (40, 90, 60))
    def box(d, x, y, c): d.rectangle((x, y, x + 200, y + 150), fill=c, outline="#16161a", width=6)
    pl = L(lambda d: (d.rectangle((60, 420, 1020, 1180), fill="#f4f4ee", outline="#8a8e9a", width=10), box(d, 110, 560, "#dfe4ee"), box(d, 400, 560, GOLD), box(d, 690, 560, RED_), d.polygon([(330, 635), (390, 600), (390, 670)], fill="#16161a"), d.polygon([(620, 635), (680, 600), (680, 670)], fill="#16161a"),
                      d.line([(790, 760), (790, 980)], fill="#16161a", width=10), d.polygon([(790, 1040), (750, 960), (830, 960)], fill="#16161a"), d.line([(690, 1060), (890, 1140)], fill=RED_, width=24), d.line([(890, 1060), (690, 1140)], fill=RED_, width=24),
                      d.rectangle((0, 1640, W, H), fill="#10261a"), officer(d, 300, 1740, 3.4), d.line([(400, 1380), (640, 1180)], fill="#3a6a4a", width=24)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 440)), (1.0, pl, bob(4, 1.0))]


def mask():
    bg = _bg((20, 20, 34), (60, 50, 80))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#14141e"), N.shadow_figure(d, 540, 1740, 4.2), d.polygon([(330, 720), (350, 600), (540, 540), (730, 600), (750, 720), (840, 740), (240, 740)], fill="#3a6a4a", outline="#16161a", width=6), d.rectangle((330, 700, 750, 740), fill="#16161a"),
                      d.ellipse((380, 760, 700, 1000), fill="#f4f4ee", outline="#8a8e9a", width=6), d.ellipse((450, 840, 500, 890), fill="#16161a"), d.ellipse((580, 840, 630, 890), fill="#16161a"), d.arc((450, 880, 630, 960), 20, 160, fill="#16161a", width=10),
                      d.polygon([(540, 1180), (640, 1220), (640, 1330), (540, 1400), (440, 1330), (440, 1220)], fill="#2a6a4a", outline="#f4f4ee", width=6)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 440)), (1.0, pl, bob(3, 1.0))]


def badges():
    bg = _bg((26, 24, 44), (70, 60, 100))
    def card(d, x, y, icon): d.rectangle((x, y, x + 300, y + 520), fill="#f4f4ee", outline="#8a8e9a", width=8); d.rectangle((x, y, x + 300, y + 90), fill=RED_); icon(d, x + 150, y + 290)
    def shield_(d, cx, cy):
        d.polygon([(cx, cy - 120), (cx + 90, cy - 80), (cx + 90, cy + 20), (cx, cy + 120), (cx - 90, cy + 20), (cx - 90, cy - 80)], fill="#3a6a4a"); d.ellipse((cx - 36, cy - 36, cx + 36, cy + 36), fill=GOLD)
    def scales(d, cx, cy):
        d.line([(cx, cy - 110), (cx, cy + 110)], fill="#3a4a6a", width=14); d.line([(cx - 100, cy - 70), (cx + 100, cy - 70)], fill="#3a4a6a", width=14); d.pieslice((cx - 130, cy - 40, cx - 30, cy + 60), 0, 180, fill="#3a4a6a"); d.pieslice((cx + 30, cy - 40, cx + 130, cy + 60), 0, 180, fill="#3a4a6a")
    def seal(d, cx, cy): d.ellipse((cx - 100, cy - 100, cx + 100, cy + 100), fill=RED_, outline="#7a2018", width=8); d.ellipse((cx - 60, cy - 60, cx + 60, cy + 60), outline="#f4f4ee", width=8)
    pl = L(lambda d: (card(d, 60, 700, shield_), card(d, 390, 700, scales), card(d, 720, 700, seal), _q(d, 540, 1560, 0.9, "#f4f4ee")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 960, 440)), (1.0, pl, bob(4, 1.0))]


def fee():
    bg = _bg((40, 24, 20), (110, 70, 50))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#2a1a14"), woman(d, 230, 1740, 3.3, True), N.shadow_figure(d, 860, 1740, 3.3), d.line([(380, 1300), (500, 1240)], fill="#e0b080", width=30), _coin(d, 540, 1220, 56), d.line([(700, 1280), (620, 1230)], fill="#2a2d38", width=30),
                      d.polygon([(380, 640), (700, 640), (780, 760), (700, 880), (380, 880)], fill="#f4f4ee", outline="#8a8e9a", width=6), d.ellipse((410, 735, 470, 785), fill="#8a8e9a"), _coin(d, 600, 760, 54)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1000, 420)), (1.0, pl, bob(4, 1.0))]


def verify():
    bg = _bg((20, 40, 70), (70, 120, 170))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#2a3a58"), woman(d, 300, 1740, 3.6), d.polygon([(380, 1020), (450, 990), (490, 1100), (420, 1130)], fill="#16161a", outline="#8a8e9a", width=4),
                      d.ellipse((560, 420, 1020, 860), fill="#f4f4ee", outline="#8a8e9a", width=8), d.polygon([(600, 800), (540, 960), (680, 840)], fill="#f4f4ee", outline="#8a8e9a"), d.rectangle((650, 620, 930, 700), fill="#2a6ac8"), d.polygon([(660, 620), (790, 520), (920, 620)], fill="#e8e6dc", outline="#8a8e9a"),
                      d.line([(690, 760), (750, 800), (860, 700)], fill=GRN, width=26)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 440)), (1.0, pl, bob(4, 1.0))]


def evidence():
    bg = _bg((22, 34, 40), (60, 90, 100))
    pl = L(lambda d: (d.rectangle((0, 1560, W, H), fill="#2a3a40"), d.rectangle((150, 1000, 930, 1560), fill="#c8a45a", outline="#6a4a1a", width=8), d.polygon([(150, 1000), (400, 1000), (450, 940), (930, 940), (930, 1000)], fill="#b8943a"),
                      N.doc(d, 210, 640, 520, 1140, 5), _bubble(d, 400, 560, 780, 740, "#dfe4ee"), _bubble(d, 500, 780, 880, 940, PINK), d.rectangle((640, 960, 900, 1140), fill="#f4f4ee", outline="#8a8e9a", width=4), d.line([(670, 1010), (870, 1010)], fill="#8a8e9a", width=8), d.line([(670, 1060), (820, 1060)], fill="#8a8e9a", width=8)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1000, 440)), (1.0, pl, bob(4, 1.0))]


REG = {"sc_" + k: v for k, v in dict(group=group, play=play, repeat=repeat, check=check, call=call, explain=explain, mask=mask, badges=badges, fee=fee, verify=verify, evidence=evidence).items()}


# ---------- scenes added for the longer cut ----------
def stats():
    bg = _bg((14, 30, 40), (40, 80, 90))
    pl = L(lambda d: (d.line([(110, 1500), (700, 1500)], fill="#c8ccd4", width=10), d.line([(110, 1500), (110, 560)], fill="#c8ccd4", width=10), [d.rectangle((150 + i * 110, 1500 - (820 - i * 120), 230 + i * 110, 1500), fill=TEAL, outline="#0a4a44", width=4) for i in range(5)],
                      d.line([(160, 700), (640, 1180)], fill=RED_, width=14), d.polygon([(690, 1240), (560, 1210), (650, 1110)], fill=RED_), d.rectangle((0, 1640, W, H), fill="#10303a"),
                      [[_coin(d, 800 + c * 110 + (r % 2) * 55, 1620 - r * 62, 56) for c in range(2 - (r % 2) + 1)] for r in range(9)]), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1000, 440)), (1.0, pl, bob(4, 1.1))]


def freeze():
    bg = _bg((14, 30, 60), (60, 110, 170))
    pl = L(lambda d: (d.rectangle((120, 700, 960, 1260), fill="#2a6ac8", outline="#0e1630", width=10), d.rectangle((120, 780, 960, 860), fill="#16161a"), d.rectangle((180, 1100, 520, 1160), fill="#c8ccd4"), d.rectangle((560, 1100, 700, 1160), fill="#c8ccd4"), d.ellipse((780, 1000, 900, 1120), fill=GOLD),
                      d.polygon([(100, 680), (400, 640), (360, 880), (110, 860)], fill=(190, 230, 250, 200), outline="#f4f4ee", width=6), d.polygon([(700, 1100), (980, 1060), (960, 1300), (720, 1280)], fill=(190, 230, 250, 200), outline="#f4f4ee", width=6),
                      d.line([(120, 1180), (960, 760)], fill="#c8ccd4", width=36), d.line([(120, 760), (960, 1180)], fill="#c8ccd4", width=36), d.rectangle((440, 940, 640, 1100), fill=GOLD, outline="#8a6a10", width=8), d.arc((470, 840, 610, 980), 180, 360, fill="#c8ccd4", width=26)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 980, 440)), (1.0, pl, bob(4, 1.0))]


def otp():
    bg = _bg((40, 12, 20), (100, 30, 40))
    pl = L(lambda d: (_phone(d, 220, 420, 860, 1500), d.rectangle((260, 520, 820, 700), fill="#3a6ac8"), [d.rectangle((270 + i * 92, 860, 340 + i * 92, 980), fill="#dfe4ee", outline="#16161a", width=5) for i in range(6)], [d.line([(290 + i * 92, 920), (320 + i * 92, 920)], fill="#16161a", width=10) for i in range(6)],
                      d.line([(160, 360), (920, 1560)], fill=RED_, width=50), d.line([(920, 360), (160, 1560)], fill=RED_, width=50)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 960, 440)), (1.0, pl, bob(4, 1.1))]


def app():
    bg = _bg((30, 16, 40), (80, 40, 90))
    cols = ("#3a6ac8", GRN, ORG, "#8a3ac8", TEAL, PINK, "#3aa8c8", GOLD, "#6a8aff")
    pl = L(lambda d: (_phone(d, 180, 360, 900, 1600), [d.rectangle((260 + (i % 3) * 190, 520 + (i // 3) * 200, 400 + (i % 3) * 190, 660 + (i // 3) * 200), fill=c if i != 4 else "#16161a", outline="#f4f4ee", width=5) for i, c in enumerate(cols)],
                      d.polygon([(540, 1010), (640, 1190), (440, 1190)], fill=RED_, outline="#f4f4ee", width=8), d.rectangle((530, 1060, 550, 1130), fill="#f4f4ee"), d.ellipse((530, 1148, 550, 1168), fill="#f4f4ee"), d.polygon([(620, 1300), (860, 1500), (800, 1560), (600, 1380)], fill="#f4f4ee", outline="#8a8e9a")), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 900, 440)), (1.0, pl, bob(4, 1.1))]


def rush():
    bg = _bg((40, 24, 20), (110, 60, 50))
    pl = L(lambda d: (d.rectangle((0, 1640, W, H), fill="#2a1a14"), woman(d, 260, 1740, 3.5, True), d.ellipse((500, 520, 1000, 1020), fill="#f4f4ee", outline="#8a8e9a", width=14), [d.line([(750 + 200 * __import__("math").cos(__import__("math").radians(k * 30)), 770 + 200 * __import__("math").sin(__import__("math").radians(k * 30))), (750 + 230 * __import__("math").cos(__import__("math").radians(k * 30)), 770 + 230 * __import__("math").sin(__import__("math").radians(k * 30)))], fill="#16161a", width=10) for k in range(12)],
                      d.line([(750, 770), (750, 610)], fill="#16161a", width=18), d.line([(750, 770), (880, 840)], fill=RED_, width=14), [_coin(d, 640 + i * 110, 1180 + (i % 2) * 70, 44) for i in range(4)], d.polygon([(520, 1330), (600, 1290), (590, 1380)], fill=GOLD)), 12, 10)
    return bg.convert("RGB"), [(0, "glow", S.sword_glow(540, 1000, 440)), (1.0, pl, bob(4, 1.0))]


REG.update({"sc_" + k: v for k, v in dict(stats=stats, freeze=freeze, otp=otp, app=app, rush=rush).items()})
