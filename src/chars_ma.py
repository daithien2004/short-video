"""Characters for Mai An Tiem. Each has its own look. (d, cx, base, s): feet at (cx, base), height ~232*s unless noted."""
import math
from story2 import RED, GOLD, INK, EDGE
from chars_st import _p, _eyes, SKIN


def an_tiem(d, cx, base, s, hoe=False):
    """Mai An Tiem: young man, deep-teal tunic, orange sash, black topknot with a small bronze pin."""
    p = _p(cx, base, s)
    if hoe: d.line([p(62, 6), p(86, -250)], fill="#6a4a2a", width=max(int(8 * s), 3)); d.polygon([p(70, -250), p(130, -270), p(120, -226), p(86, -236)], fill="#8a8f9a", outline="#4a4e58")
    d.rectangle((*p(-24, -52), *p(-6, 0)), fill="#3a3028"); d.rectangle((*p(6, -52), *p(24, 0)), fill="#3a3028")
    d.polygon([p(-54, -40), p(-36, -150), p(36, -150), p(54, -40)], fill="#1f7a86", outline="#124850"); d.rectangle((*p(-46, -86), *p(46, -68)), fill="#e8802a")
    d.ellipse((*p(-30, -216), *p(30, -146)), fill=SKIN); _eyes(d, p, -192); d.line([p(-10, -168), p(10, -168)], fill="#8a4a3a", width=max(int(3 * s), 2))
    d.polygon([p(-32, -200), p(32, -200), p(26, -226), p(0, -236), p(-26, -226)], fill="#16121a"); d.ellipse((*p(-14, -262), *p(14, -230)), fill="#16121a"); d.line([p(-22, -246), p(22, -252)], fill="#c8902a", width=max(int(5 * s), 2))


def vo(d, cx, base, s, hat=False):
    """An Tiem's wife: saffron-yellow tunic, brown apron, hair in a low bun with a wooden pin (optional conical hat)."""
    p = _p(cx, base, s)
    d.polygon([p(-56, 0), p(-30, -142), p(30, -142), p(56, 0)], fill="#e8a030", outline="#a86a10"); d.polygon([p(-34, -96), p(34, -96), p(44, 0), p(-44, 0)], fill="#8a5a3a")
    d.ellipse((*p(-30, -212), *p(30, -146)), fill=SKIN); _eyes(d, p, -190); d.ellipse((*p(-24, -170), *p(-12, -162)), fill="#f0a8a8"); d.ellipse((*p(12, -170), *p(24, -162)), fill="#f0a8a8")
    d.polygon([p(-32, -206), p(32, -206), p(30, -178), p(0, -196), p(-30, -178)], fill="#3a2418"); d.ellipse((*p(-18, -236), *p(18, -202)), fill="#3a2418"); d.line([p(-26, -224), p(26, -214)], fill="#d8b86a", width=max(int(4 * s), 2))
    if hat: d.polygon([p(-86, -196), p(86, -196), p(0, -290)], fill="#d8b86a", outline="#8a6a30")


def con(d, cx, base, s):
    """The child (about 130*s tall): red tunic, round head, one tuft of hair on top."""
    p = _p(cx, base, s)
    d.rectangle((*p(-14, -30), *p(-4, 0)), fill=SKIN); d.rectangle((*p(4, -30), *p(14, 0)), fill=SKIN)
    d.polygon([p(-24, -26), p(-18, -84), p(18, -84), p(24, -26)], fill="#c8372d", outline="#7a2018")
    d.ellipse((*p(-30, -136), *p(30, -78)), fill=SKIN); d.ellipse((*p(-12, -114), *p(-4, -104)), fill="#2b2420"); d.ellipse((*p(4, -114), *p(12, -104)), fill="#2b2420"); d.ellipse((*p(-22, -100), *p(-12, -92)), fill="#f0a8a8"); d.ellipse((*p(12, -100), *p(22, -92)), fill="#f0a8a8")
    d.polygon([p(-4, -134), p(0, -160), p(8, -134)], fill="#16121a")


def courtier(d, cx, base, s):
    """Sly courtier: dusky-purple robe, tall black winged hat, thin moustache, narrow eyes."""
    p = _p(cx, base, s)
    d.polygon([p(-54, 0), p(-32, -142), p(32, -142), p(54, 0)], fill="#6a4a7a", outline="#3a2848"); d.polygon([p(-32, -142), p(0, -114), p(32, -142)], fill="#d8c8e0"); d.rectangle((*p(-42, -80), *p(42, -64)), fill="#c8a8d8")
    d.ellipse((*p(-28, -208), *p(28, -144)), fill="#e6c6a0"); d.line([p(-16, -186), p(-6, -182)], fill="#16121a", width=max(int(4 * s), 2)); d.line([p(6, -182), p(16, -186)], fill="#16121a", width=max(int(4 * s), 2))
    d.polygon([p(-18, -166), p(0, -160), p(18, -166), p(10, -158), p(-10, -158)], fill="#16121a")
    d.polygon([p(-30, -206), p(30, -206), p(24, -246), p(-24, -246)], fill="#16121a"); d.polygon([p(-30, -230), p(-80, -250), p(-34, -214)], fill="#16121a"); d.polygon([p(30, -230), p(80, -250), p(34, -214)], fill="#16121a")


def merchant(d, cx, base, s):
    """Sea merchant: sun-browned skin, red turban, brown vest over a white shirt, striped sash."""
    p = _p(cx, base, s)
    d.rectangle((*p(-24, -50), *p(-6, 0)), fill="#5a3e2a"); d.rectangle((*p(6, -50), *p(24, 0)), fill="#5a3e2a")
    d.polygon([p(-56, -44), p(-38, -150), p(38, -150), p(56, -44)], fill="#f2efe4", outline="#a89c84"); d.polygon([p(-52, -50), p(-38, -148), p(-14, -148), p(-14, -50)], fill="#7a4a2a"); d.polygon([p(52, -50), p(38, -148), p(14, -148), p(14, -50)], fill="#7a4a2a")
    for i, c in enumerate(("#c8372d", "#f2b632")): d.rectangle((*p(-50, -84 + i * 10), *p(50, -76 + i * 10)), fill=c)
    d.ellipse((*p(-30, -216), *p(30, -146)), fill="#c8905a"); _eyes(d, p, -190); d.line([p(-18, -198), p(-6, -200)], fill="#16121a", width=max(int(4 * s), 2)); d.line([p(6, -200), p(18, -198)], fill="#16121a", width=max(int(4 * s), 2))
    d.ellipse((*p(-36, -246), *p(36, -192)), fill="#c8372d", outline="#7a2018"); d.polygon([p(30, -226), p(64, -214), p(40, -200)], fill="#c8372d")


def gull(d, cx, cy, s, flip=1, up=True):
    """Seabird seen from the side with wings spread (about 130*s wide)."""
    f = lambda dx, dy: (cx + dx * s * flip, cy + dy * s)
    wy = -70 if up else 40
    d.polygon([f(-10, 0), f(-70, wy), f(-120, wy + 20), f(-60, 16)], fill="#d6dce4", outline="#8a929c"); d.polygon([f(-120, wy + 20), f(-70, wy), f(-96, wy + 6)], fill="#3a3a44")
    d.ellipse((min(f(-60, -18)[0], f(60, 18)[0]), cy - 18 * s, max(f(-60, -18)[0], f(60, 18)[0]), cy + 18 * s), fill="#f6f6f2", outline="#8a929c")
    d.polygon([f(56, -10), f(100, -4), f(56, 6)], fill="#f2a030"); d.ellipse((min(f(34, -12)[0], f(44, -4)[0]), cy - 12 * s, max(f(34, -12)[0], f(44, -4)[0]), cy - 4 * s), fill="#111")
    d.polygon([f(-60, 0), f(-104, 14), f(-60, 14)], fill="#d6dce4")


def melon(d, cx, cy, r, cut=False):
    """Watermelon: whole (green with dark stripes) or a cut half (red flesh, black seeds)."""
    if not cut:
        d.ellipse((cx - r * 1.2, cy - r, cx + r * 1.2, cy + r), fill="#3f9a4a", outline="#1f5a28")
        for k in (-0.7, -0.35, 0, 0.35, 0.7): d.arc((cx - r * 1.2 * abs(1 - abs(k) * .3), cy - r, cx + r * 1.2 * abs(1 - abs(k) * .3), cy + r), 250 + k * 40, 290 + k * 40, fill="#1f5a28", width=max(int(r * .12), 2))
    else:
        d.pieslice((cx - r * 1.2, cy - r * 1.2, cx + r * 1.2, cy + r * 1.2), 0, 180, fill="#3f9a4a", outline="#1f5a28"); d.pieslice((cx - r * 1.05, cy - r * 1.05, cx + r * 1.05, cy + r * 1.05), 0, 180, fill="#f2f2d8"); d.pieslice((cx - r * .92, cy - r * .92, cx + r * .92, cy + r * .92), 0, 180, fill="#e8403a")
        for k in range(-3, 4): d.ellipse((cx + k * r * .26 - 5, cy + r * .3 + (abs(k) % 2) * r * .16 - 8, cx + k * r * .26 + 5, cy + r * .3 + (abs(k) % 2) * r * .16 + 8), fill="#16121a")


def boat(d, cx, base, s, flip=1, sail="#f2efe4"):
    """Small sailing boat in profile (about 360*s wide): wooden hull, one sail."""
    f = lambda dx, dy: (cx + dx * s * flip, base + dy * s)
    d.polygon([f(-180, -50), f(180, -50), f(130, 0), f(-130, 0)], fill="#8a5a2a", outline="#4a2e12"); d.rectangle((min(f(-6, -300)[0], f(6, -50)[0]), base - 300 * s, max(f(-6, -300)[0], f(6, -50)[0]), base - 50 * s), fill="#5a3e26")
    d.polygon([f(10, -296), f(150, -80), f(10, -80)], fill=sail, outline="#a89c84"); d.polygon([f(-10, -270), f(-110, -80), f(-10, -80)], fill=sail, outline="#a89c84")


def hut(d, x, base, w=220, h=130):
    d.rectangle((x, base - h, x + w, base), fill="#a8793c", outline="#5a3e26"); d.polygon([(x - 30, base - h + 6), (x + w + 30, base - h + 6), (x + w - 30, base - h - 100), (x + 30, base - h - 100)], fill="#d8b86a", outline="#8a6a30"); d.rectangle((x + w * .4, base - h * .7, x + w * .6, base), fill=INK)
