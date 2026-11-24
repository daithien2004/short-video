"""Characters for the Nỏ thần story. Each character has its OWN look (never reuse one figure for several characters).
All take (d, cx, base, s): feet at (cx, base), height about 232*s, y grows downward."""
import math
import story3 as X
from story2 import lens, CREAM, RED, GOLD, INK, EDGE, GREEN

SKIN = "#f3dcb4"


def _p(cx, base, s): return lambda dx, dy: (cx + dx * s, base + dy * s)


def _face(d, p, eyes=True):
    d.ellipse((*p(-30, -206), *p(30, -140)), fill=SKIN)
    if eyes: d.ellipse((*p(-13, -190), *p(-5, -182)), fill="#2b2420"); d.ellipse((*p(5, -190), *p(13, -182)), fill="#2b2420")


def king(d, cx, base, s):
    """An Duong Vuong: old king, long white beard, gold robe with green hem and collar, winged gold crown."""
    p = _p(cx, base, s)
    d.polygon([p(-64, 0), p(-36, -140), p(36, -140), p(64, 0)], fill="#d9a62a"); d.rectangle((*p(-64, -18), *p(64, 0)), fill="#2f6a4a"); d.polygon([p(-36, -140), p(0, -108), p(36, -140)], fill="#2f6a4a")
    d.rectangle((*p(-44, -80), *p(44, -62)), fill="#2f6a4a"); _face(d, p)
    d.polygon([p(-27, -170), p(27, -170), p(32, -95), p(0, -56), p(-32, -95)], fill="#f4f0e6", outline="#c9c2b0")
    d.line([p(-22, -196), p(-6, -192)], fill="#f4f0e6", width=max(int(5 * s), 2)); d.line([p(6, -192), p(22, -196)], fill="#f4f0e6", width=max(int(5 * s), 2))
    d.rectangle((*p(-36, -228), *p(36, -206)), fill=GOLD, outline=EDGE); d.polygon([p(-36, -228), p(-22, -266), p(0, -240), p(22, -266), p(36, -228)], fill=GOLD, outline=EDGE)
    d.ellipse((*p(-8, -224), *p(8, -208)), fill=RED); d.polygon([p(-36, -222), p(-74, -240), p(-36, -208)], fill=GOLD); d.polygon([p(36, -222), p(74, -240), p(36, -208)], fill=GOLD)


def princess(d, cx, base, s):
    """My Chau: young princess, long black hair, pale pink dress, red sash, gold hairpin."""
    p = _p(cx, base, s)
    d.ellipse((*p(-46, -228), *p(46, -40)), fill="#16121a"); d.polygon([p(-58, 0), p(-26, -140), p(26, -140), p(58, 0)], fill="#f6d6dc", outline="#d9a8b2")
    d.rectangle((*p(-32, -102), *p(32, -84)), fill=RED); _face(d, p)
    d.polygon([p(-34, -210), p(34, -210), p(32, -176), p(0, -196), p(-32, -176)], fill="#16121a"); d.ellipse((*p(14, -226), *p(30, -210)), fill=GOLD); d.line([p(22, -218), p(40, -250)], fill=GOLD, width=max(int(5 * s), 2))
    d.ellipse((*p(-24, -166), *p(-12, -158)), fill="#f0a8a8"); d.ellipse((*p(12, -166), *p(24, -158)), fill="#f0a8a8")


def prince(d, cx, base, s):
    """Trong Thuy: northern prince, jade-teal robe, tall black scholar hat with side wings, thin moustache, no beard."""
    p = _p(cx, base, s)
    d.polygon([p(-56, 0), p(-32, -140), p(32, -140), p(56, 0)], fill="#2f8a8a"); d.polygon([p(-32, -140), p(0, -104), p(32, -140), p(14, -140), p(0, -120), p(-14, -140)], fill="#f2efe4")
    d.rectangle((*p(-42, -80), *p(42, -62)), fill="#c0c6cc"); _face(d, p); d.line([p(-14, -160), p(0, -156), p(14, -160)], fill="#2b2420", width=max(int(4 * s), 2))
    d.rectangle((*p(-26, -292), *p(26, -206)), fill="#1b1b22"); d.rectangle((*p(-70, -240), *p(-26, -230)), fill="#1b1b22"); d.rectangle((*p(26, -240), *p(70, -230)), fill="#1b1b22")


def zhao(d, cx, base, s):
    """Trieu Da: northern king, deep purple robe, black pointed beard, flat crown with hanging beads."""
    p = _p(cx, base, s)
    d.polygon([p(-62, 0), p(-36, -140), p(36, -140), p(62, 0)], fill="#4a2a6a"); d.rectangle((*p(-44, -80), *p(44, -62)), fill=GOLD); d.polygon([p(-36, -140), p(0, -108), p(36, -140)], fill="#8a5ab0")
    _face(d, p); d.polygon([p(-22, -166), p(22, -166), p(0, -96)], fill="#1b1b22"); d.line([p(-16, -172), p(0, -166), p(16, -172)], fill="#1b1b22", width=max(int(5 * s), 2))
    d.rectangle((*p(-30, -250), *p(30, -222)), fill="#1b1b22"); d.rectangle((*p(-52, -236), *p(52, -224)), fill="#2a2a34", outline=GOLD)
    for x in (-46, -30, 30, 46): d.line([p(x, -224), p(x, -196)], fill=GOLD, width=max(int(3 * s), 1))


def soldier_au(d, cx, base, s):
    """Au Lac soldier: brown leather armour, red headband, hair bun, spear."""
    p = _p(cx, base, s)
    d.line([p(52, -10), p(56, -330)], fill="#6a4a2a", width=max(int(7 * s), 3)); d.polygon([p(56, -330), p(48, -300), p(64, -300)], fill="#dfe6ea")
    d.polygon([p(-52, 0), p(-32, -140), p(32, -140), p(52, 0)], fill="#7a4a2a"); d.line([p(-30, -130), p(30, -60)], fill="#4a2a14", width=max(int(8 * s), 3)); d.line([p(30, -130), p(-30, -60)], fill="#4a2a14", width=max(int(8 * s), 3))
    d.ellipse((*p(-10, -232), *p(12, -206)), fill="#16121a"); _face(d, p); d.rectangle((*p(-31, -190), *p(31, -178)), fill=RED)


def soldier_bac(d, cx, base, s):
    """Northern soldier: grey armour, pointed helmet with red plume, spear."""
    p = _p(cx, base, s)
    d.line([p(-52, -10), p(-56, -330)], fill="#2a2a30", width=max(int(7 * s), 3)); d.polygon([p(-56, -330), p(-64, -300), p(-48, -300)], fill="#c8ccd2")
    d.polygon([p(-52, 0), p(-32, -140), p(32, -140), p(52, 0)], fill="#6a707c"); d.rectangle((*p(-36, -90), *p(36, -74)), fill="#3b3f48"); _face(d, p)
    d.polygon([p(-38, -198), p(38, -198), p(0, -292)], fill="#3b3f48"); d.rectangle((*p(-42, -204), *p(42, -194)), fill="#555a66"); d.polygon([p(0, -292), p(-9, -324), p(11, -320)], fill=RED)


def horse(d, cx, base, s, col="#8a5a3a", flip=1):
    """Horse in profile facing right (flip=-1 faces left)."""
    f = lambda dx, dy: (cx + dx * s * flip, base + dy * s); dark = "#2a1a12"
    ell = lambda a, b, **k: d.ellipse((min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])), **k)  # mirrored coordinates must stay ordered
    rect = lambda a, b, **k: d.rectangle((min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])), **k)
    d.polygon([f(-118, -150), f(-220, -96), f(-196, -56), f(-116, -110)], fill=dark)
    for x in (-100, -60, 70, 110): d.polygon([f(x - 14, -70), f(x + 14, -70), f(x + 10, 0), f(x - 10, 0)], fill=col); rect(f(x - 12, -8), f(x + 12, 0), fill=dark)
    ell(f(-140, -190), f(140, -50), fill=col)
    d.polygon([f(96, -160), f(180, -270), f(222, -246), f(150, -100)], fill=col); d.polygon([f(96, -160), f(172, -276), f(150, -280), f(70, -190)], fill=dark)
    d.polygon([f(176, -272), f(262, -222), f(254, -186), f(196, -206)], fill=col); d.polygon([f(190, -274), f(200, -306), f(212, -272)], fill=col); ell(f(204, -246), f(216, -234), fill="#111")


def crossbow(d, cx, cy, s, arrow=True):
    """Big crossbow seen from the side; gold 'claw' trigger. Shooting direction: right."""
    p = _p(cx, cy, s)
    d.rectangle((*p(-170, -14), *p(150, 16)), fill="#6a4a2a", outline="#3a2414"); d.rectangle((*p(100, -22), *p(160, 24)), fill="#8a5e36")
    d.line([p(140, -10), p(190, -150)], fill="#6a4a2a", width=max(int(20 * s), 4)); d.line([p(140, 12), p(190, 160)], fill="#6a4a2a", width=max(int(20 * s), 4))
    d.line([p(190, -150), p(-70, 0), p(190, 160)], fill="#efe6c8", width=max(int(5 * s), 2))
    d.polygon([p(-50, 16), p(-20, 16), p(-10, 56), p(-30, 66), p(-46, 40)], fill=GOLD, outline=EDGE)  # the claw trigger
    if arrow: d.line([p(-70, 0), p(230, 0)], fill="#d8d0b8", width=max(int(8 * s), 3)); d.polygon([p(230, -14), p(270, 0), p(230, 14)], fill="#c8872a")


def feather(d, x, y, s, ang=0.4):
    lens(d, x, y, 120 * s, 18 * s, ang, "#ffffff"); d.line([(x, y), (x + 120 * s * math.cos(ang), y + 120 * s * math.sin(ang))], fill="#d8d8d0", width=max(int(3 * s), 1))


ALL = (("An Dương Vương", king), ("Mỵ Châu", princess), ("Trọng Thủy", prince), ("Triệu Đà", zhao), ("Lính Âu Lạc", soldier_au), ("Lính phương Bắc", soldier_bac))
