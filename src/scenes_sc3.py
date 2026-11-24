"""Detailed pass for the scam-story scenes: people with arms, hands, brows and moods; real backgrounds (room, bank hall, street, underwater); phone insets that show the screen being talked about.
Same scene names as scenes_sc / scenes_sc2 (this file overrides them in the registry)."""
import math
import story2 as S
from story2 import W, H, GOLD, grad
from scenes_hk2 import L, sway, bob
import chars_nv as N
from chars_st import _p, _eyes
from scenes_ink import ink_figure, lighten_scene, InkD

PINK, TEAL, RED_, ORG, GRN, BLU = "#ff5d8f", "#2ec4b6", "#d6403a", "#ff9a3c", "#3fae5a", "#3a6ac8"


def _bg(c0=(24, 22, 52), c1=(70, 60, 110)): return grad(c0, c1).convert("RGBA")


def coin(d, cx, cy, r): d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GOLD, outline="#8a6a10", width=6); d.ellipse((cx - r * .62, cy - r * .62, cx + r * .62, cy + r * .62), outline="#c89a20", width=5); d.line([(cx - r * .12, cy - r * .35), (cx - r * .12, cy + r * .35)], fill="#c89a20", width=max(int(r * .12), 3))


def bill(d, x, y, w=300, h=110):
    d.rectangle((x, y, x + w, y + h), fill="#5cc06a", outline="#1f6a30", width=5); d.ellipse((x + w / 2 - h * .3, y + h * .2, x + w / 2 + h * .3, y + h * .8), fill="#8ae09a", outline="#1f6a30", width=4); d.rectangle((x + 12, y + 12, x + 40, y + 34), outline="#1f6a30", width=3)


def qmark(d, cx, cy, s, col="#f2f2ee"):
    d.arc((cx - 90 * s, cy - 150 * s, cx + 90 * s, cy - 10 * s), 200, 380, fill=col, width=int(44 * s)); d.line([(cx + 80 * s, cy - 60 * s), (cx, cy + 40 * s), (cx, cy + 80 * s)], fill=col, width=int(44 * s)); d.ellipse((cx - 26 * s, cy + 120 * s, cx + 26 * s, cy + 172 * s), fill=col)


def bubble(d, x0, y0, x1, y1, fill="#f4f4ee", tail=None):
    d.rectangle((x0, y0, x1, y1), fill=fill, outline="#8a8e9a", width=5)
    if tail: d.polygon(list(tail), fill=fill, outline="#8a8e9a")


# ---------------- backgrounds ----------------
def floor(d, y=1560, c="#2a2036", c2="#3a2e4a"):
    d.rectangle((0, y, W, H), fill=c); d.rectangle((0, y - 24, W, y + 8), fill=c2)


def window(d, x, y, w, h):
    d.rectangle((x, y, x + w, y + h), fill="#bfdcf2", outline="#8a7a6a", width=8); d.line([(x + w / 2, y), (x + w / 2, y + h)], fill="#8a7a6a", width=6); d.ellipse((x + w * .6, y + h * .14, x + w * .82, y + h * .14 + w * .22), fill="#fff3b8")


def pic(d, x, y, w, h):
    d.rectangle((x, y, x + w, y + h), fill="#e8d8b0", outline="#6a4a2a", width=10); d.polygon([(x + 14, y + h - 14), (x + w * .35, y + h * .35), (x + w * .55, y + h * .6), (x + w * .75, y + h * .3), (x + w - 14, y + h - 14)], fill="#5a8a6a"); d.ellipse((x + w * .65, y + 22, x + w * .65 + 40, y + 62), fill="#e8b84a")


def lamp(d, x, base):
    d.polygon([(x - 150, base - 560), (x + 150, base - 560), (x + 330, base), (x - 330, base)], fill=(255, 226, 140, 40))
    d.rectangle((x - 8, base - 520, x + 8, base), fill="#6a5a4a"); d.polygon([(x - 90, base - 520), (x + 90, base - 520), (x + 60, base - 620), (x - 60, base - 620)], fill="#e8c860", outline="#8a6a2a"); d.ellipse((x - 70, base - 20, x + 70, base + 6), fill="#4a3a2a")


def plant(d, x, base, s=1.0):
    d.polygon([(x - 60 * s, base - 110 * s), (x + 60 * s, base - 110 * s), (x + 44 * s, base), (x - 44 * s, base)], fill="#a0522d", outline="#5a2a10")
    for a in (-110, -80, -50, -20, 200, 230): d.polygon([(x, base - 110 * s), (x + 150 * s * math.cos(math.radians(a)) - 14, base - 110 * s + 170 * s * math.sin(math.radians(a))), (x + 150 * s * math.cos(math.radians(a)) + 14, base - 110 * s + 170 * s * math.sin(math.radians(a)) + 20)], fill="#3a8a4a")


def room(d, v=0):
    floor(d, 1560, "#d9cdb8", "#c9bba4"); window(d, (60, 700, 380)[v % 3], 320, 280, 420)


def bankhall(d):
    d.rectangle((0, 1500, W, H), fill="#c4d2e0")
    for r in range(8):
        for c in range(12):
            if (r + c) % 2: d.rectangle((c * 90, 1500 + r * 52, c * 90 + 90, 1552 + r * 52), fill="#b4c4d6")
    d.rectangle((0, 300, W, 1500), fill="#d6e4f0"); d.rectangle((0, 300, W, 360), fill="#b8cadc")
    d.ellipse((470, 460, 610, 600), fill="#f4f4ee", outline="#8a8e9a", width=10); d.line([(540, 530), (540, 480)], fill="#16161a", width=8); d.line([(540, 530), (580, 550)], fill="#d6403a", width=6)


# ---------------- people ----------------
BODYC = {"woman": "#ff6f91", "scammer": "#2b2644", "teller": "#3a8ad8", "officer": "#3e7a52"}
BADGEC = {"woman": "#7a4a6e", "scammer": "#5a4e8a", "teller": "#2f6aa0", "officer": "#2f6a4a"}
SKN, SKN2 = "#f0c090", "#e0aa78"


def _head(d, k, cx, cy, r, mood):
    if k == "woman":
        d.ellipse((cx - r * 1.05, cy - r * .9, cx + r * 1.05, cy + r * 1.1), fill="#2a1a14"); d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=SKN)
        d.polygon([(cx - r * 1.02, cy - r * .2), (cx - r * .7, cy - r * .95), (cx, cy - r * 1.08), (cx + r * .7, cy - r * .95), (cx + r * 1.02, cy - r * .2), (cx + r * .4, cy - r * .55), (cx - r * .4, cy - r * .55)], fill="#2a1a14")
        d.ellipse((cx - r * .38, cy - r * 1.62, cx + r * .38, cy - r * .92), fill="#2a1a14"); d.ellipse((cx - r * .85, cy + r * .2, cx - r * .5, cy + r * .42), fill="#f6a09a"); d.ellipse((cx + r * .5, cy + r * .2, cx + r * .85, cy + r * .42), fill="#f6a09a")
    elif k == "scammer":
        d.ellipse((cx - r * 1.2, cy - r * 1.15, cx + r * 1.2, cy + r * 1.15), fill="#2b2644", outline="#8a7ab8", width=max(int(r * .05), 3)); d.ellipse((cx - r * .82, cy - r * .7, cx + r * .82, cy + r * .85), fill="#08070c")
        [d.ellipse((cx + sx * r * .4 - r * .16, cy - r * .12, cx + sx * r * .4 + r * .16, cy + r * .2), fill="#f4f4ee") for sx in (-1, 1)]
        d.arc((cx - r * .34, cy + r * .2, cx + r * .34, cy + r * .66), 20, 160, fill="#f4f4ee", width=max(int(r * .09), 3))
        return
    elif k == "teller":
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=SKN); d.polygon([(cx - r * 1.02, cy - r * .1), (cx - r * .85, cy - r * .85), (cx, cy - r * 1.12), (cx + r * .85, cy - r * .85), (cx + r * 1.02, cy - r * .1), (cx + r * .5, cy - r * .5), (cx - r * .5, cy - r * .5)], fill="#3a2418")
    else:
        d.ellipse((cx - r, cy - r * .9, cx + r, cy + r * 1.05), fill=SKN2); d.polygon([(cx - r, cy - r * .5), (cx - r * .85, cy - r * 1.25), (cx, cy - r * 1.45), (cx + r * .85, cy - r * 1.25), (cx + r, cy - r * .5)], fill="#3e7a52")
        d.rectangle((cx - r * 1.2, cy - r * .62, cx + r * 1.2, cy - r * .42), fill="#1d1a26"); d.ellipse((cx - r * .22, cy - r * 1.18, cx + r * .22, cy - r * .74), fill="#f2c13a")
    w = max(int(r * .07), 3); ink = "#1d1a26"
    [d.ellipse((cx + sx * r * .42 - r * .12, cy + r * .02, cx + sx * r * .42 + r * .12, cy + r * .3), fill=ink) for sx in (-1, 1)]
    if mood == "worried":
        d.line([(cx - r * .7, cy - r * .12), (cx - r * .22, cy - r * .3)], fill=ink, width=w); d.line([(cx + r * .7, cy - r * .12), (cx + r * .22, cy - r * .3)], fill=ink, width=w); d.arc((cx - r * .22, cy + r * .5, cx + r * .22, cy + r * .78), 200, 340, fill=ink, width=w); d.polygon([(cx + r * .98, cy - r * .1), (cx + r * 1.12, cy + r * .3), (cx + r * .84, cy + r * .3)], fill="#6ec3f0")
    elif mood == "shock":
        d.line([(cx - r * .7, cy - r * .2), (cx - r * .22, cy - r * .12)], fill=ink, width=w); d.line([(cx + r * .7, cy - r * .2), (cx + r * .22, cy - r * .12)], fill=ink, width=w); d.ellipse((cx - r * .16, cy + r * .42, cx + r * .16, cy + r * .78), fill="#5a1a1a")
    elif mood == "stern":
        d.line([(cx - r * .7, cy - r * .2), (cx - r * .22, cy - r * .08)], fill=ink, width=w); d.line([(cx + r * .7, cy - r * .2), (cx + r * .22, cy - r * .08)], fill=ink, width=w); d.line([(cx - r * .22, cy + r * .58), (cx + r * .22, cy + r * .58)], fill=ink, width=w)
    else: d.arc((cx - r * .22, cy + r * .38, cx + r * .22, cy + r * .66), 20, 160, fill=ink, width=w)
    if k == "officer": d.rectangle((cx - r * .3, cy + r * .72, cx + r * .3, cy + r * .8), fill="#3a2418")


def portrait(d, cx, cy, r, k="woman", mood="calm", prop=None):
    """Round badge portrait: head and shoulders inside a circle with a white ring (the shared look of every person in the story)."""
    d.ellipse((cx - r - 12, cy - r - 12, cx + r + 12, cy + r + 12), fill="#f4f4ee"); d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=BADGEC[k])
    arc = [(cx + r * math.cos(math.radians(t)), cy + r * math.sin(math.radians(t))) for t in range(150, 29, -10)]
    top = [(cx + .75 * r, cy + .28 * r), (cx + .45 * r, cy + .17 * r), (cx + .2 * r, cy + .1 * r), (cx - .2 * r, cy + .1 * r), (cx - .45 * r, cy + .17 * r), (cx - .75 * r, cy + .28 * r)]
    d.polygon(arc + top, fill=BODYC[k])
    if k == "teller": d.polygon([(cx - .07 * r, cy + .16 * r), (cx + .07 * r, cy + .16 * r), (cx + .1 * r, cy + .6 * r), (cx, cy + .74 * r), (cx - .1 * r, cy + .6 * r)], fill="#e03a3a")
    if k == "officer": d.ellipse((cx + .34 * r, cy + .42 * r, cx + .56 * r, cy + .64 * r), fill="#f2c13a")
    if k != "scammer": d.rectangle((cx - .11 * r, cy + .15 * r, cx + .11 * r, cy + .42 * r), fill=SKN if k != "officer" else SKN2)
    _head(d, k, cx, cy - .12 * r, .5 * r, mood)
    if prop == "phone": d.rectangle((cx - .15 * r, cy + .52 * r, cx + .15 * r, cy + .97 * r), fill="#16161a"); d.rectangle((cx - .11 * r, cy + .57 * r, cx + .11 * r, cy + .95 * r), fill="#8fe0f4")
    if prop == "ear": d.rectangle((cx + .5 * r, cy - .28 * r, cx + .68 * r, cy + .14 * r), fill="#16161a"); d.rectangle((cx + .54 * r, cy - .22 * r, cx + .64 * r, cy + .08 * r), fill="#8fe0f4")


def figure(d, cx, base, s, kind="woman", mood="calm", pose="down"):
    """Ink-style half-length person (thick outline, pentagon head). Same signature as the old figure()."""
    prop = {"phone": "phone", "hold": "phone", "ear": "ear"}.get(pose)
    ink_figure(d, cx, base - 20, s * 0.78, kind, mood, prop)


def shadow(d, cx, base, s, col=None): figure(d, cx, base, s, "scammer", "calm", "down")


# ---------------- phone inset ----------------
def screen(d, x0, y0, x1, y1, bar="#3a6ac8"):
    d.rectangle((x0, y0, x1, y1), fill="#16161a", outline="#8a8e9a", width=8); d.rectangle((x0 + 22, y0 + 60, x1 - 22, y1 - 56), fill="#eef2f8"); d.rectangle((x0 + 22, y0 + 60, x1 - 22, y0 + 150), fill=bar); d.ellipse((x0 + (x1 - x0) / 2 - 10, y0 + 24, x0 + (x1 - x0) / 2 + 10, y0 + 44), fill="#3a3a44")
    return x0 + 22, y0 + 150, x1 - 22, y1 - 56


def avatar(d, cx, cy, r, col):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col, outline="#f4f4ee", width=5); d.ellipse((cx - r * .32, cy - r * .5, cx + r * .32, cy + r * .14), fill="#f4f4ee"); d.polygon([(cx - r * .62, cy + r * .78), (cx - r * .5, cy + r * .2), (cx + r * .5, cy + r * .2), (cx + r * .62, cy + r * .78)], fill="#f4f4ee")


def zoom(d, a, b, x, y): d.line([a, (x, y)], fill=(70, 70, 100, 140), width=6); d.line([b, (x, y + 120)], fill=(70, 70, 100, 140), width=6)


def scene(fn, c0=(24, 22, 52), c1=(70, 60, 110), glow=None, anim=None):
    bg = _bg(c0, c1).convert("RGB")
    return lighten_scene((bg, [(1.0, L(lambda d: fn(InkD(d)), 12, 10), anim or bob(4, 1.1))]))


# ================= 1: story =================
def group():
    def draw(d):
        room(d, 0); figure(d, 250, 1740, 3.4, "woman", "calm", "phone")
        x0, y0, x1, y1 = 520, 330, 1020, 1400; screen(d, x0, y0, x1, y1); zoom(d, (330, 1140), (380, 1120), x0, y0 + 600)
        d.rectangle((x0 + 40, y0 + 80, x0 + 330, y0 + 100), fill="#f4f4ee"); d.rectangle((x0 + 40, y0 + 115, x0 + 200, y0 + 128), fill="#c8d4f0")
        for i, c in enumerate((PINK, TEAL, ORG, "#6a8aff", GRN, "#b46aff", RED_, GOLD, "#3aa8c8")): avatar(d, x0 + 110 + (i % 3) * 140, y0 + 270 + (i // 3) * 200, 52, c); d.rectangle((x0 + 70 + (i % 3) * 140, y0 + 330 + (i // 3) * 200, x0 + 150 + (i % 3) * 140, y0 + 342 + (i // 3) * 200), fill="#b8bcc4")
        d.rectangle((x0 + 40, y1 - 190, x1 - 40, y1 - 100), fill=BLU); d.line([(x0 + 200, y1 - 145), (x0 + 300, y1 - 145)], fill="#f4f4ee", width=12); d.line([(x0 + 250, y1 - 175), (x0 + 250, y1 - 115)], fill="#f4f4ee", width=12)
    return scene(draw, (22, 30, 60), (60, 70, 120))


def phone():
    def draw(d):
        room(d, 1); figure(d, 250, 1740, 3.4, "woman", "happy", "phone")
        x0, y0, x1, y1 = 520, 330, 1020, 1400; screen(d, x0, y0, x1, y1, PINK); zoom(d, (330, 1140), (380, 1120), x0, y0 + 600); avatar(d, x0 + 80, y0 + 105, 30, "#3a4a6a")
        bubble(d, x0 + 40, y0 + 200, x0 + 330, y0 + 300, "#dfe4ee"); bubble(d, x0 + 150, y0 + 340, x1 - 40, y0 + 440, "#ffd0e0"); bubble(d, x0 + 40, y0 + 480, x0 + 350, y0 + 580, "#dfe4ee"); bubble(d, x0 + 120, y0 + 620, x1 - 40, y0 + 760, "#ffd0e0")
        d.ellipse((x0 + 190, y0 + 660, x0 + 290, y0 + 730), outline=BLU, width=14); d.ellipse((x0 + 260, y0 + 660, x0 + 360, y0 + 730), outline=BLU, width=14)
        d.rectangle((x0 + 40, y1 - 190, x1 - 40, y1 - 110), fill="#dfe4ee", outline="#8a8e9a", width=4)
    return scene(draw, (30, 24, 60), (90, 60, 120))


def wheel():
    cols = (RED_, GOLD, TEAL, "#6a8aff", PINK, ORG, GRN, "#b46aff")
    def draw(d):
        d.rectangle((0, 1640, W, H), fill="#d9cdb8"); d.polygon([(380, 1640), (700, 1640), (620, 1360), (460, 1360)], fill="#6a4a2a", outline="#2a1a10", width=6)
        [d.pieslice((120, 540, 960, 1380), k * 45, (k + 1) * 45, fill=c, outline="#f4f4ee", width=6) for k, c in enumerate(cols)]
        for k in range(8):
            a = math.radians(k * 45 + 22.5); cx, cy = 540 + 280 * math.cos(a), 960 + 280 * math.sin(a)
            if k % 2 == 0: coin(d, cx, cy, 44)
            else: d.rectangle((cx - 36, cy - 30, cx + 36, cy + 36), fill="#f4f4ee", outline="#16161a", width=4); d.rectangle((cx - 6, cy - 30, cx + 6, cy + 36), fill=RED_)
        d.ellipse((470, 890, 610, 1030), fill="#f4f4ee", outline="#8a8e9a", width=8); d.polygon([(540, 500), (600, 600), (480, 600)], fill="#f4f4ee", outline="#8a8e9a")
        [d.ellipse((540 + 440 * math.cos(math.radians(k * 22.5)) - 14, 960 + 440 * math.sin(math.radians(k * 22.5)) - 14, 540 + 440 * math.cos(math.radians(k * 22.5)) + 14, 960 + 440 * math.sin(math.radians(k * 22.5)) + 14), fill=GOLD if k % 2 else "#fff0a0") for k in range(16)]
    return scene(draw, (50, 14, 70), (140, 50, 110), (540, 960, 480), sway(5, 1.0))


def play():
    cols = (RED_, GOLD, TEAL, "#6a8aff", PINK, ORG, GRN, "#b46aff")
    def draw(d):
        room(d, 2); figure(d, 250, 1740, 3.4, "woman", "happy", "phone")
        x0, y0, x1, y1 = 520, 330, 1020, 1400; screen(d, x0, y0, x1, y1, "#b46aff"); zoom(d, (330, 1140), (380, 1120), x0, y0 + 600)
        [d.pieslice((x0 + 70, y0 + 240, x1 - 70, y0 + 660), k * 45, (k + 1) * 45, fill=c, outline="#f4f4ee", width=4) for k, c in enumerate(cols)]; d.polygon([((x0 + x1) / 2, y0 + 220), ((x0 + x1) / 2 + 30, y0 + 270), ((x0 + x1) / 2 - 30, y0 + 270)], fill="#16161a")
        d.rectangle((x0 + 90, y1 - 330, x1 - 90, y1 - 220), fill=TEAL, outline="#0a4a44", width=6); coin(d, x0 + 160, y0 + 110, 28)
    return scene(draw, (50, 14, 70), (120, 40, 110))


def pay():
    def draw(d):
        room(d, 0); figure(d, 230, 1740, 3.4, "woman", "worried", "phone")
        x0, y0, x1, y1 = 480, 300, 980, 1250; screen(d, x0, y0, x1, y1, TEAL); zoom(d, (310, 1140), (360, 1120), x0, y0 + 560)
        d.rectangle((x0 + 50, y0 + 200, x1 - 50, y0 + 320), fill="#dfe4ee", outline="#8a8e9a", width=4); [d.rectangle((x0 + 70 + i * 66, y0 + 236, x0 + 112 + i * 66, y0 + 290), fill="#16161a") for i in range(5)]
        d.rectangle((x0 + 50, y0 + 360, x1 - 50, y0 + 430), fill="#dfe4ee", outline="#8a8e9a", width=4); avatar(d, x0 + 100, y0 + 395, 24, "#3a4a6a"); d.rectangle((x0 + 90, y1 - 330, x1 - 90, y1 - 230), fill=GRN, outline="#1f6a30", width=6)
        shadow(d, 880, 1740, 2.5)
        for i in range(4): coin(d, 640 + i * 70, 1320 - i * (3 - i) * 26, 36)
        d.polygon([(900, 1260), (840, 1230), (846, 1310)], fill=GOLD)
    return scene(draw, (30, 24, 50), (80, 60, 100))


def repeat():
    def draw(d):
        room(d, 1)
        for i in range(3):
            x = 70 + i * 330; y = 420 + i * 70; screen(d, x, y, x + 280, y + 640, GRN); d.rectangle((x + 40, y + 250, x + 240, y + 330), fill="#dfe4ee"); d.line([(x + 90, y + 470), (x + 130, y + 510), (x + 200, y + 420)], fill=GRN, width=22); coin(d, x + 140, y - 50, 40)
        figure(d, 150, 1760, 2.2, "woman", "worried", "down"); d.polygon([(560, 1560), (940, 1560), (990, 1380), (510, 1380)], fill="#c8a45a", outline="#6a4a1a", width=6); [coin(d, 620 + i * 80, 1500 - (i % 2) * 18, 40) for i in range(4)]
        d.rectangle((560, 1000, 580, 1100), fill="#f4f4ee")
    return scene(draw, (30, 24, 50), (80, 60, 100))


def gift():
    def draw(d):
        room(d, 2); figure(d, 810, 1740, 3.3, "woman", "worried", "phone")
        d.rectangle((120, 1100, 580, 1560), fill=PINK, outline="#7a1a4a", width=8); d.polygon([(90, 1100), (610, 1100), (690, 960), (170, 900)], fill="#ff8aaa", outline="#7a1a4a"); d.rectangle((320, 1100, 380, 1560), fill=GOLD); d.rectangle((140, 1160, 560, 1520), fill="#2a1a30")
        qmark(d, 350, 1340, 0.6, "#8a8e9a"); [d.line([(150 + i * 70, 1200 + (i % 2) * 40), (210 + i * 70, 1240 + (i % 2) * 40)], fill="#8a8e9a", width=4) for i in range(5)]
        bubble(d, 620, 720, 1000, 860, "#dfe4ee", ((880, 860), (900, 930), (940, 860))); [d.ellipse((690 + i * 90, 770, 740 + i * 90, 820), fill="#8a8e9a") for i in range(3)]
    return scene(draw, (26, 22, 40), (60, 50, 80))


def demand():
    def draw(d):
        room(d, 1); figure(d, 230, 1740, 3.4, "woman", "shock", "raise")
        x0, y0, x1, y1 = 480, 320, 1000, 1360; screen(d, x0, y0, x1, y1, RED_); avatar(d, x0 + 80, y0 + 105, 30, "#3a4a6a")
        bubble(d, x0 + 40, y0 + 200, x1 - 40, y0 + 330, "#dfe4ee"); bubble(d, x0 + 40, y0 + 380, x1 - 40, y0 + 760, "#ffd8d4")
        [bill(d, x0 + 90 + (i % 2) * 8, y0 + 690 - (i + 1) * 36, 280, 90) for i in range(8)]; d.polygon([(x0 + 380, y0 + 420), (x0 + 430, y0 + 540), (x0 + 330, y0 + 540)], fill=RED_); d.rectangle((x0 + 372, y0 + 548, x0 + 388, y0 + 600), fill=RED_)
    return scene(draw, (40, 14, 24), (110, 30, 50))


def check():
    def draw(d):
        room(d, 0); d.rectangle((120, 520, 760, 1360), fill="#f4f4ee", outline="#8a8e9a", width=6); d.rectangle((120, 520, 760, 620), fill=BLU)
        [d.line([(170, 700 + i * 80), (700 - (i % 3) * 60, 700 + i * 80)], fill="#b8bcc4", width=14) for i in range(7)]; d.line([(170, 1100), (520, 1100)], fill="#16161a", width=18)
        d.ellipse((500, 800, 920, 1220), fill=(190, 230, 240, 110), outline="#c8ccd4", width=30); d.line([(870, 1170), (1030, 1400)], fill="#c8ccd4", width=56)
        d.rectangle((240, 1420, 460, 1520), fill=BLU, outline="#0e1630", width=6); d.rectangle((640, 1420, 860, 1520), fill=GRN, outline="#1f6a30", width=6); d.line([(470, 1470), (630, 1470)], fill=GOLD, width=16); d.polygon([(650, 1470), (610, 1430), (610, 1510)], fill=GOLD)
    return scene(draw, (14, 30, 40), (40, 80, 80))


# ================= bank =================
def bank():
    def draw(d):
        d.rectangle((0, 1640, W, H), fill="#c9d6e4"); d.rectangle((0, 1600, W, 1650), fill="#b4c4d6")
        d.polygon([(100, 760), (540, 480), (980, 760)], fill="#e8e6dc", outline="#8a8e9a", width=6); d.rectangle((100, 760, 980, 840), fill="#c8ccd4", outline="#8a8e9a", width=6)
        [d.rectangle((150 + i * 170, 840, 220 + i * 170, 1480), fill="#f4f2e8", outline="#8a8e9a", width=5) for i in range(6)]; d.rectangle((100, 1480, 980, 1540), fill="#c8ccd4"); d.rectangle((60, 1540, 1020, 1620), fill="#b8bcc4")
        d.rectangle((420, 640, 660, 720), fill=BLU); d.ellipse((490, 560, 590, 660), fill=GOLD); d.rectangle((420, 1080, 660, 1480), fill="#ffe8a0", outline="#8a8e9a", width=6); d.line([(540, 1080), (540, 1480)], fill="#8a8e9a", width=6)
        figure(d, 760, 1760, 1.9, "woman", "worried", "down"); figure(d, 340, 1760, 1.5, "officer", "calm", "down")
    return scene(draw, (20, 30, 60), (70, 100, 150), (540, 900, 460), bob(3, 1.0))


def counter():
    def draw(d):
        bankhall(d); figure(d, 760, 1540, 3.0, "teller", "calm", "down")
        d.rectangle((0, 1300, W, 1480), fill="#8a6a3a", outline="#4a3a1a", width=6); d.rectangle((0, 1480, W, H), fill="#5a4a2a"); d.rectangle((0, 1180, W, 1300), fill=(190, 230, 240, 90), outline="#c8ccd4", width=5)
        d.rectangle((560, 1240, 700, 1300), fill="#5cc06a", outline="#1f6a30", width=4); figure(d, 240, 1790, 3.4, "woman", "worried", "hold")
    return scene(draw, (24, 34, 60), (60, 90, 130), (540, 900, 440), bob(3, 1.0))


def teller():
    def draw(d):
        bankhall(d); figure(d, 540, 1790, 4.1, "teller", "worried", "hold")
        d.ellipse((130, 360, 950, 920), fill="#f4f4ee", outline="#8a8e9a", width=8); d.polygon([(480, 880), (540, 1010), (600, 880)], fill="#f4f4ee", outline="#8a8e9a"); qmark(d, 540, 680, 1.1, BLU); coin(d, 260, 540, 44); coin(d, 820, 540, 44)
    return scene(draw, (20, 40, 80), (60, 110, 170))


def call():
    def draw(d):
        bankhall(d); d.rectangle((0, 1300, W, 1480), fill="#8a6a3a", outline="#4a3a1a", width=6); d.rectangle((0, 1480, W, H), fill="#5a4a2a")
        figure(d, 400, 1540, 3.4, "teller", "calm", "ear"); [d.arc((640 + k * 70, 780 - k * 60, 960 + k * 70, 1100 + k * 60), -50, 50, fill="#f4f4ee", width=18) for k in range(3)]
        figure(d, 880, 1740, 1.8, "officer", "stern", "down"); figure(d, 130, 1790, 2.2, "woman", "worried", "down")
    return scene(draw, (20, 40, 80), (60, 110, 170))


def police():
    def draw(d):
        d.rectangle((0, 0, W, H), fill="#d4ead9"); d.rectangle((0, 1500, W, H), fill="#b8d4c0"); d.rectangle((60, 1160, 1020, 1240), fill="#8a6a3a", outline="#4a3a1a", width=6); d.rectangle((120, 1240, 160, 1560), fill="#6a4a2a"); d.rectangle((920, 1240, 960, 1560), fill="#6a4a2a")
        d.rectangle((340, 1040, 740, 1160), fill="#c8ccd4", outline="#6a6e7a", width=6); d.rectangle((360, 1050, 720, 1150), fill="#9ad8e8"); d.polygon([(380, 1160), (700, 1160), (740, 1220), (340, 1220)], fill="#8a8e9a")
        figure(d, 220, 1740, 3.2, "officer", "stern", "point"); figure(d, 860, 1740, 3.2, "teller", "calm", "down"); figure(d, 540, 1790, 2.4, "woman", "worried", "down")
        d.polygon([(540, 240), (700, 300), (700, 460), (540, 560), (380, 460), (380, 300)], fill="#2a6a4a", outline="#f4f4ee", width=6); d.ellipse((480, 340, 600, 460), fill=GOLD)
    return scene(draw, (14, 34, 24), (40, 90, 60))


def explain():
    def draw(d):
        d.rectangle((0, 1500, W, H), fill="#cfe6d6"); d.rectangle((50, 300, 1030, 1240), fill="#f4f4ee", outline="#8a8e9a", width=10)
        d.ellipse((100, 460, 260, 620), outline=BLU, width=20); d.ellipse((200, 460, 360, 620), outline=BLU, width=20)
        [d.pieslice((420, 440, 600, 620), k * 90, (k + 1) * 90, fill=c) for k, c in enumerate((RED_, GOLD, TEAL, PINK))]; coin(d, 760, 540, 80); d.polygon([(900, 460), (960, 580), (840, 580)], fill=RED_); d.rectangle((890, 590, 910, 620), fill=RED_)
        [d.polygon([(x, 540), (x - 40, 500), (x - 40, 580)], fill="#16161a") for x in (400, 650, 830)]
        d.line([(530, 700), (530, 920)], fill="#16161a", width=10); d.polygon([(530, 980), (490, 900), (570, 900)], fill="#16161a"); d.line([(430, 1010), (630, 1150)], fill=RED_, width=28); d.line([(630, 1010), (430, 1150)], fill=RED_, width=28)
        figure(d, 230, 1760, 3.4, "officer", "calm", "point")
    return scene(draw, (14, 34, 24), (40, 90, 60))


def stop():
    def draw(d):
        room(d, 1); figure(d, 240, 1740, 3.4, "woman", "calm", "stop")
        x0, y0, x1, y1 = 520, 520, 980, 1480; screen(d, x0, y0, x1, y1, TEAL); d.rectangle((x0 + 50, y0 + 220, x1 - 50, y0 + 320), fill="#dfe4ee", outline="#8a8e9a", width=4); d.rectangle((x0 + 70, y1 - 330, x1 - 70, y1 - 230), fill=GRN, outline="#1f6a30", width=6)
        d.polygon([(750, 260), (880, 310), (940, 440), (880, 570), (750, 620), (620, 570), (560, 440), (620, 310)], fill=RED_, outline="#f4f4ee", width=10); d.rectangle((650, 410, 850, 470), fill="#f4f4ee")
    return scene(draw, (40, 12, 20), (100, 30, 40))


# ================= pattern =================
def _fish(d, cx, cy, s, ang):
    """Minimal fish facing +x: body, tail, one fin, one eye, small open mouth. Ink outlines come from InkD."""
    c, sn = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    X = lambda x, y: (cx + s * (x * c - y * sn), cy + s * (x * sn + y * c))
    ell = lambda ex, ey, rx, ry, n=36: [X(ex + rx * math.cos(2 * math.pi * k / n), ey + ry * math.sin(2 * math.pi * k / n)) for k in range(n)]
    d.polygon([X(-.8, 0), X(-1.7, -.6), X(-1.7, .6)], fill="#ff5d8f")
    d.polygon([X(-.2, -.55), X(.15, -1.0), X(.5, -.5)], fill="#ff5d8f")
    d.polygon(ell(0, 0, 1.0, .66), fill="#ff7a9c")
    d.polygon([X(.85, -.2), X(1.2, 0), X(.85, .2)], fill="#8a1a3a")
    d.polygon(ell(.5, -.18, .18, .18, 24), fill="#ffffff"); d.polygon(ell(.55, -.18, .08, .08, 18), fill="#14121a", outline="#14121a", width=1)


def bait():
    def draw(d):
        d.rectangle((0, 1320, W, H), fill="#8ec8e0"); d.rectangle((0, 1320, W, 1352), fill="#6ab0d0")
        d.line([(540, 0), (540, 880)], fill="#14121a", width=8); d.arc((470, 860, 610, 990), 0, 200, fill="#14121a", width=14); coin(d, 540, 1090, 74)
        _fish(d, 380, 1250, 220, -34)
        d.arc((640, 1330, 840, 1390), 180, 360, fill="#f4fbff", width=8)
    return scene(draw, (10, 30, 50), (30, 90, 120), (540, 1100, 420), sway(5, 1.0))


def mask():
    def draw(d):
        figure_cx, sc, bottom = 540, 2.7, 1600
        ink_figure(d, figure_cx, bottom, sc, "scammer", "calm")
        top = bottom - 380 * sc
        d.polygon([(380, top + 30 * sc), (386, top - 70), (540, top - 130), (694, top - 70), (700, top + 30 * sc)], fill="#4a8a5c", outline="#14121a", width=14); d.polygon([(350, top + 24 * sc), (730, top + 16 * sc), (722, top + 50 * sc), (358, top + 58 * sc)], fill="#1c1a24", outline="#14121a", width=10); d.ellipse((500, top - 90, 580, top - 10), fill="#f2c13a", outline="#14121a", width=10)
        d.polygon([(540, 1180), (640, 1220), (640, 1330), (540, 1410), (440, 1330), (440, 1220)], fill="#4a8a5c", outline="#14121a", width=12); d.ellipse((500, 1250, 580, 1330), fill="#f2c13a", outline="#14121a", width=8)
    return scene(draw, (20, 20, 34), (60, 50, 80))


def fee():
    def draw(d):
        room(d, 2); figure(d, 260, 1740, 3.2, "woman", "worried", "point"); shadow(d, 800, 1740, 3.2)
        d.line([(700, 1280), (620, 1210)], fill="#2a2d38", width=30); d.ellipse((580, 1160, 640, 1220), fill="#2a2d38"); coin(d, 540, 1190, 52)
        d.polygon([(380, 640), (700, 640), (780, 760), (700, 880), (380, 880)], fill="#f4f4ee", outline="#8a8e9a", width=6); d.ellipse((410, 735, 470, 785), fill="#8a8e9a"); coin(d, 600, 760, 54)
    return scene(draw, (40, 24, 20), (110, 70, 50))


def verify():
    def draw(d):
        room(d, 0); figure(d, 300, 1740, 3.6, "woman", "calm", "ear")
        d.ellipse((560, 420, 1020, 860), fill="#f4f4ee", outline="#8a8e9a", width=8); d.polygon([(600, 800), (540, 960), (680, 840)], fill="#f4f4ee", outline="#8a8e9a"); d.rectangle((650, 620, 930, 700), fill=BLU); d.polygon([(660, 620), (790, 520), (920, 620)], fill="#e8e6dc", outline="#8a8e9a"); d.line([(690, 760), (750, 800), (860, 700)], fill=GRN, width=26)
    return scene(draw, (20, 40, 70), (70, 120, 170))


def rush():
    def draw(d):
        room(d, 1); figure(d, 240, 1740, 3.5, "woman", "worried", "raise")
        d.ellipse((520, 500, 1020, 1000), fill="#f4f4ee", outline="#8a8e9a", width=14); [d.line([(770 + 200 * math.cos(math.radians(k * 30)), 750 + 200 * math.sin(math.radians(k * 30))), (770 + 230 * math.cos(math.radians(k * 30)), 750 + 230 * math.sin(math.radians(k * 30)))], fill="#16161a", width=10) for k in range(12)]
        d.line([(770, 750), (770, 590)], fill="#16161a", width=18); d.line([(770, 750), (900, 820)], fill=RED_, width=14); [coin(d, 600 + i * 110, 1200 + (i % 2) * 70, 44) for i in range(4)]; d.polygon([(500, 1300), (580, 1260), (570, 1350)], fill=GOLD)
        [d.line([(x, 440), (x + 20, 380)], fill=RED_, width=10) for x in (560, 640, 720)]
    return scene(draw, (40, 24, 20), (110, 60, 50))


REG = {"sc_" + k: v for k, v in dict(group=group, phone=phone, wheel=wheel, play=play, pay=pay, repeat=repeat, gift=gift, demand=demand, check=check, bank=bank, counter=counter, teller=teller, call=call, police=police, explain=explain, stop=stop, bait=bait, mask=mask, fee=fee, verify=verify, rush=rush).items()}


def _padlock(d, cx, cy, s=1.0):
    d.arc((cx - 150 * s, cy - 330 * s, cx + 150 * s, cy - 30 * s), 180, 360, fill="#c8ccd4", width=int(54 * s)); d.line([(cx - 150 * s, cy - 180 * s), (cx - 150 * s, cy - 20 * s)], fill="#c8ccd4", width=int(54 * s)); d.line([(cx + 150 * s, cy - 180 * s), (cx + 150 * s, cy - 20 * s)], fill="#c8ccd4", width=int(54 * s))
    d.rectangle((cx - 230 * s, cy - 40 * s, cx + 230 * s, cy + 320 * s), fill=GOLD); d.ellipse((cx - 36 * s, cy + 80 * s, cx + 36 * s, cy + 152 * s), fill="#14121a"); d.rectangle((cx - 14 * s, cy + 130 * s, cx + 14 * s, cy + 240 * s), fill="#14121a")


def _cross(d, cx, cy, r, w=50): d.line([(cx - r, cy - r), (cx + r, cy + r)], fill=RED_, width=w); d.line([(cx + r, cy - r), (cx - r, cy + r)], fill=RED_, width=w)


def badges():
    def card(d, x, y, icon): d.rectangle((x, y, x + 300, y + 520), fill="#f4f4ee"); d.rectangle((x, y, x + 300, y + 90), fill=RED_); icon(d, x + 150, y + 300)
    def shield_(d, cx, cy): d.polygon([(cx, cy - 120), (cx + 90, cy - 80), (cx + 90, cy + 20), (cx, cy + 120), (cx - 90, cy + 20), (cx - 90, cy - 80)], fill="#3a6a4a"); d.ellipse((cx - 36, cy - 36, cx + 36, cy + 36), fill=GOLD)
    def scales(d, cx, cy): d.line([(cx, cy - 110), (cx, cy + 110)], fill="#3a4a6a", width=14); d.line([(cx - 100, cy - 70), (cx + 100, cy - 70)], fill="#3a4a6a", width=14); d.pieslice((cx - 130, cy - 40, cx - 30, cy + 60), 0, 180, fill="#3a4a6a"); d.pieslice((cx + 30, cy - 40, cx + 130, cy + 60), 0, 180, fill="#3a4a6a")
    def seal(d, cx, cy): d.ellipse((cx - 100, cy - 100, cx + 100, cy + 100), fill=RED_); d.ellipse((cx - 60, cy - 60, cx + 60, cy + 60), fill="#f4f4ee")
    def draw(d): floor(d, 1640, "#d9cdb8", "#c9bba4"); card(d, 60, 560, shield_); card(d, 390, 560, scales); card(d, 720, 560, seal); qmark(d, 540, 1500, 0.9, "#14121a")
    return scene(draw, (26, 24, 44), (70, 60, 100))


def freeze():
    def draw(d):
        floor(d, 1640, "#d9cdb8", "#c9bba4"); d.rectangle((140, 560, 940, 1080), fill=BLU); d.rectangle((140, 640, 940, 720), fill="#16161a"); d.ellipse((780, 820, 900, 940), fill=GOLD)
        _padlock(d, 540, 1180, 0.8)
    return scene(draw, (14, 30, 60), (60, 110, 170))


def otp():
    def draw(d):
        floor(d, 1640, "#d9cdb8", "#c9bba4"); x0, y0, x1, y1 = 200, 380, 880, 1500; screen(d, x0, y0, x1, y1, BLU)
        [d.rectangle((x0 + 40 + i * 90, 880, x0 + 110 + i * 90, 1000), fill="#dfe4ee") for i in range(6)]; [d.line([(x0 + 60 + i * 90, 940), (x0 + 90 + i * 90, 940)], fill="#14121a", width=10) for i in range(6)]
        _cross(d, 540, 940, 330, 54)
    return scene(draw, (40, 12, 20), (100, 30, 40))


def app():
    cols = (BLU, GRN, ORG, "#8a3ac8", TEAL, PINK, "#3aa8c8", GOLD, "#6a8aff")
    def draw(d):
        floor(d, 1640, "#d9cdb8", "#c9bba4"); x0, y0, x1, y1 = 180, 340, 900, 1600; screen(d, x0, y0, x1, y1, "#8a3ac8")
        [d.rectangle((250 + (i % 3) * 200, 640 + (i // 3) * 220, 400 + (i % 3) * 200, 790 + (i // 3) * 220), fill=c if i != 4 else "#16161a") for i, c in enumerate(cols)]
        d.polygon([(540, 1040), (680, 1290), (400, 1290)], fill=RED_); d.rectangle((526, 1110, 554, 1210), fill="#f4f4ee"); d.ellipse((526, 1228, 554, 1256), fill="#f4f4ee")
    return scene(draw, (30, 16, 40), (80, 40, 90))


def evidence():
    def draw(d):
        floor(d, 1640, "#d9cdb8", "#c9bba4"); d.rectangle((150, 1000, 930, 1560), fill="#c8a45a"); d.polygon([(150, 1000), (400, 1000), (450, 940), (930, 940), (930, 1000)], fill="#b8943a")
        d.rectangle((210, 640, 520, 1140), fill="#f4f4ee"); [d.line([(250, 720 + i * 80), (480, 720 + i * 80)], fill="#8a8e9a", width=10) for i in range(4)]
        bubble(d, 400, 440, 780, 620, "#dfe4ee"); bubble(d, 500, 660, 880, 840, PINK); d.rectangle((640, 960, 900, 1140), fill="#f4f4ee")
    return scene(draw, (22, 34, 40), (60, 90, 100))


def stats():
    def draw(d):
        floor(d, 1640, "#d9cdb8", "#c9bba4"); d.line([(110, 1500), (760, 1500)], fill="#14121a", width=12); d.line([(110, 1500), (110, 520)], fill="#14121a", width=12)
        [d.rectangle((150 + i * 120, 1500 - (300 + i * 150), 250 + i * 120, 1500), fill=TEAL) for i in range(5)]
        d.line([(160, 700), (700, 1100)], fill=RED_, width=18); d.polygon([(760, 1160), (620, 1140), (700, 1020)], fill=RED_)
        [[coin(d, 790 + c * 100 + (r % 2) * 50, 1600 - r * 56, 50) for c in range(2 - (r % 2) + 1)] for r in range(9)]
    return scene(draw, (14, 30, 40), (40, 80, 90))


def shield():
    def draw(d):
        floor(d, 1640, "#d9cdb8", "#c9bba4"); _padlock(d, 540, 820, 1.1); d.line([(260, 1560), (400, 1670), (660, 1440)], fill=GRN, width=60)
    return scene(draw, (14, 34, 40), (40, 100, 100))


def clock():
    def draw(d):
        floor(d, 1640, "#d9cdb8", "#c9bba4"); d.ellipse((190, 420, 890, 1120), fill="#f4f4ee")
        [d.line([(540 + 290 * math.cos(math.radians(k * 30)), 770 + 290 * math.sin(math.radians(k * 30))), (540 + 330 * math.cos(math.radians(k * 30)), 770 + 330 * math.sin(math.radians(k * 30)))], fill="#14121a", width=14) for k in range(12)]
        d.line([(540, 770), (540, 520)], fill="#14121a", width=22); d.line([(540, 770), (700, 860)], fill=RED_, width=18); [coin(d, 190 + i * 175, 1450 + (i % 2) * 60, 70) for i in range(5)]
    return scene(draw, (20, 20, 40), (60, 60, 100))


def pile():
    def draw(d):
        floor(d, 1640, "#d9cdb8", "#c9bba4")
        for r in range(7):
            for c in range(7 - r): coin(d, 540 + (c - (6 - r) / 2) * 150, 1560 - r * 120, 76)
        [bill(d, 90 + i * 270, 520 + (i % 2) * 120, 240, 100) for i in range(3)]
    return scene(draw, (20, 20, 40), (60, 60, 100))


REG.update({"sc_" + k: v for k, v in dict(badges=badges, freeze=freeze, otp=otp, app=app, evidence=evidence, stats=stats, shield=shield, clock=clock, pile=pile).items()})
