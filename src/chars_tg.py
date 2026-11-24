"""Characters for the Thánh Gióng story. Each has its own look. (d, cx, base, s): feet at (cx, base), height ~232*s unless noted."""
import math
from story2 import lens, CREAM, RED, GOLD, INK, EDGE, GREEN
import chars as C

SKIN = "#f3dcb4"


def _p(cx, base, s): return lambda dx, dy: (cx + dx * s, base + dy * s)


def _eyes(d, p, y=-190):
    d.ellipse((*p(-13, y), *p(-5, y + 8)), fill="#2b2420"); d.ellipse((*p(5, y), *p(13, y + 8)), fill="#2b2420")


def boy(d, cx, base, s):
    """Little boy (about 150*s tall): two hair buns, bare chest, red loincloth, round head."""
    p = _p(cx, base, s)
    d.rectangle((*p(-22, -10), *p(-6, 0)), fill=SKIN); d.rectangle((*p(6, -10), *p(22, 0)), fill=SKIN); d.rectangle((*p(-26, -76), *p(26, -14)), fill=SKIN); d.rectangle((*p(-28, -40), *p(28, -14)), fill=RED)
    d.ellipse((*p(-40, -176), *p(-18, -152)), fill="#16121a"); d.ellipse((*p(18, -176), *p(40, -152)), fill="#16121a"); d.ellipse((*p(-36, -156), *p(36, -76)), fill=SKIN)
    d.ellipse((*p(-16, -122), *p(-6, -110)), fill="#2b2420"); d.ellipse((*p(6, -122), *p(16, -110)), fill="#2b2420"); d.ellipse((*p(-26, -104), *p(-14, -96)), fill="#f0a8a8"); d.ellipse((*p(14, -104), *p(26, -96)), fill="#f0a8a8")


def boy_lying(d, cx, base, s):
    """The boy lying on his back on a straw mat, blanket over the body."""
    p = _p(cx, base, s)
    d.polygon([p(-200, 0), p(200, 0), p(180, -16), p(-180, -16)], fill="#c8a45a", outline="#8a6a30")
    d.ellipse((*p(-170, -86), *p(-90, -10)), fill=SKIN); d.ellipse((*p(-196, -76), *p(-170, -50)), fill="#16121a"); d.ellipse((*p(-160, -66), *p(-150, -56)), fill="#2b2420"); d.ellipse((*p(-130, -66), *p(-120, -56)), fill="#2b2420")
    d.polygon([p(-90, -14), p(-80, -66), p(160, -50), p(170, -14)], fill="#b8382d", outline="#7a2018")


def gion(d, cx, base, s, cape=True):
    """Gióng the warrior: iron-grey plate armour, red cape, helmet with a red plume."""
    p = _p(cx, base, s)
    if cape: d.polygon([p(-70, -150), p(-110, 10), p(110, 10), p(70, -150)], fill="#b8382d")
    d.rectangle((*p(-36, -50), *p(-6, 0)), fill="#4a505c"); d.rectangle((*p(6, -50), *p(36, 0)), fill="#4a505c")
    d.polygon([p(-58, -60), p(-40, -150), p(40, -150), p(58, -60)], fill="#9aa3b0", outline="#5a606c")
    for y in (-130, -108, -86): d.line([p(-44, y), p(44, y)], fill="#6a707c", width=max(int(5 * s), 2))
    d.rectangle((*p(-48, -70), *p(48, -56)), fill=GOLD); d.ellipse((*p(-78, -170), *p(-34, -130)), fill="#8a909c", outline="#5a606c"); d.ellipse((*p(34, -170), *p(78, -130)), fill="#8a909c", outline="#5a606c")
    d.ellipse((*p(-30, -216), *p(30, -150)), fill=SKIN); _eyes(d, p, -196); d.line([p(-14, -170), p(14, -170)], fill="#2b2420", width=max(int(4 * s), 2))
    d.polygon([p(-34, -196), p(34, -196), p(28, -250), p(0, -262), p(-28, -250)], fill="#7a828e", outline="#5a606c"); d.polygon([p(0, -262), p(-10, -296), p(14, -290)], fill=RED)


def mother(d, cx, base, s):
    """Gióng's mother: brown peasant dress, darker apron, head-scarf, kind lined face."""
    p = _p(cx, base, s)
    d.polygon([p(-56, 0), p(-30, -140), p(30, -140), p(56, 0)], fill="#8a5a3a"); d.polygon([p(-30, -90), p(30, -90), p(38, 0), p(-38, 0)], fill="#d8c8a0"); d.ellipse((*p(-30, -206), *p(30, -140)), fill=SKIN)
    _eyes(d, p); d.line([p(-8, -160), p(8, -160)], fill="#a05a4a", width=max(int(3 * s), 1)); d.line([p(-22, -176), p(-16, -172)], fill="#c8a880", width=2); d.line([p(22, -176), p(16, -172)], fill="#c8a880", width=2)
    d.polygon([p(-36, -196), p(36, -196), p(30, -226), p(0, -240), p(-30, -226)], fill="#5a3e2a"); d.polygon([p(30, -226), p(54, -214), p(36, -196)], fill="#5a3e2a")


def king_hung(d, cx, base, s):
    """Hung king: deep-red robe with gold trim, feather headdress in Dong Son style, short black beard."""
    p = _p(cx, base, s)
    d.polygon([p(-64, 0), p(-36, -140), p(36, -140), p(64, 0)], fill="#8e1f24"); d.polygon([p(-36, -140), p(0, -106), p(36, -140), p(24, -140), p(0, -122), p(-24, -140)], fill=GOLD); d.rectangle((*p(-46, -80), *p(46, -62)), fill=GOLD); d.rectangle((*p(-64, -14), *p(64, 0)), fill=GOLD)
    d.ellipse((*p(-30, -206), *p(30, -140)), fill=SKIN); _eyes(d, p); d.polygon([p(-18, -160), p(18, -160), p(12, -134), p(-12, -134)], fill="#1b1b22")
    d.rectangle((*p(-34, -226), *p(34, -208)), fill=GOLD, outline=EDGE)
    for i, (dx, col) in enumerate(((-52, "#2a7a9a"), (-26, "#c8372d"), (0, "#f2efe4"), (26, "#c8372d"), (52, "#2a7a9a"))): d.polygon([p(dx * .5, -226), p(dx - 10, -290 + abs(dx) * .5), p(dx + 10, -290 + abs(dx) * .5)], fill=col, outline="#5a4a3a")


def envoy(d, cx, base, s):
    """Royal envoy: green robe, black hat with a white feather, carries a red pennant."""
    p = _p(cx, base, s)
    d.line([p(60, 6), p(64, -330)], fill="#6a4a2a", width=max(int(6 * s), 3)); d.polygon([p(64, -330), p(150, -306), p(64, -278)], fill=RED)
    d.polygon([p(-54, 0), p(-32, -140), p(32, -140), p(54, 0)], fill="#3a7a4a"); d.polygon([p(-32, -140), p(0, -112), p(32, -140)], fill="#d8e8d0"); d.rectangle((*p(-42, -78), *p(42, -62)), fill="#e8d06a")
    d.ellipse((*p(-30, -206), *p(30, -140)), fill=SKIN); _eyes(d, p); d.polygon([p(-44, -204), p(44, -204), p(0, -252)], fill="#1b1b22"); d.line([p(0, -252), p(14, -296)], fill="#ffffff", width=max(int(5 * s), 2))


def soldier_an(d, cx, base, s):
    """An invader: maroon armour, horned helmet, thick moustache, curved blade."""
    p = _p(cx, base, s)
    d.line([p(52, -60), p(96, -200)], fill="#3a2a2a", width=max(int(8 * s), 3)); d.polygon([p(96, -200), p(130, -250), p(112, -176)], fill="#cfd4da")
    d.polygon([p(-56, 0), p(-34, -140), p(34, -140), p(56, 0)], fill="#7a2a2a"); d.rectangle((*p(-40, -90), *p(40, -72)), fill="#3a2a2a"); d.ellipse((*p(-30, -206), *p(30, -140)), fill="#e6c6a0")
    _eyes(d, p); d.polygon([p(-24, -164), p(24, -164), p(14, -152), p(-14, -152)], fill="#16121a")
    d.polygon([p(-34, -196), p(34, -196), p(26, -236), p(-26, -236)], fill="#3a2a2a"); d.polygon([p(-30, -226), p(-62, -276), p(-14, -236)], fill="#e8e0d0"); d.polygon([p(30, -226), p(62, -276), p(14, -236)], fill="#e8e0d0")


def iron_horse(d, cx, base, s, flip=1, fire=True):
    C.horse(d, cx, base, s, "#5a606c", flip)
    if fire:
        f = lambda dx, dy: (cx + dx * s * flip, base + dy * s)
        d.polygon([f(262, -214), f(380, -250), f(330, -214), f(420, -214), f(330, -196), f(262, -190)], fill="#e8532a"); d.polygon([f(262, -208), f(340, -222), f(310, -206), f(262, -196)], fill=GOLD)


def bamboo(d, x, base, h, col="#5a9a4a", leaf="#3f7d3a", lean=0):
    d.polygon([(x - 12, base), (x + 12, base), (x + 8 + lean, base - h), (x - 8 + lean, base - h)], fill=col, outline="#2f5a2a")
    for i in range(1, int(h // 120) + 1): y = base - i * 120; xx = x + lean * i * 120 / h; d.rectangle((xx - 15, y - 6, xx + 15, y + 6), fill="#2f5a2a")
    for k in range(4): y = base - h + k * 50; d.polygon([(x + lean, y), (x + lean + 90, y - 26), (x + lean + 20, y + 16)], fill=leaf); d.polygon([(x + lean, y + 10), (x + lean - 90, y - 16), (x + lean - 20, y + 26)], fill=leaf)


def staff(d, x0, y0, x1, y1, w=16, col="#6a707c"):
    d.line([(x0, y0), (x1, y1)], fill=col, width=w); d.line([(x0, y0), (x1, y1)], fill="#a8aeb8", width=max(w // 4, 2))
