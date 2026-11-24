"""Characters for Son Tinh - Thuy Tinh. Each has its own look. (d, cx, base, s): feet at (cx, base), height ~232*s unless noted."""
import math
from story2 import RED, GOLD, INK, EDGE
import chars as C

SKIN = "#f3dcb4"


def _p(cx, base, s): return lambda dx, dy: (cx + dx * s, base + dy * s)


def _eyes(d, p, y=-190, col="#2b2420"):
    d.ellipse((*p(-13, y), *p(-5, y + 8)), fill=col); d.ellipse((*p(5, y), *p(13, y + 8)), fill=col)


def son_tinh(d, cx, base, s, staff=True):
    """Mountain god: long white hair and beard, mossy green cape, brown tunic, grey stone shoulder pads, stone crown, stone-headed staff."""
    p = _p(cx, base, s)
    if staff:
        d.line([p(66, 6), p(72, -330)], fill="#6a4a2a", width=max(int(8 * s), 3)); d.polygon([p(50, -330), p(94, -330), p(104, -372), p(74, -402), p(44, -372)], fill="#9a9a96", outline="#5a5a56")
    d.polygon([p(-78, -150), p(-96, 8), p(96, 8), p(78, -150)], fill="#2f6a3a")
    d.rectangle((*p(-30, -50), *p(-6, 0)), fill="#6a4a2a"); d.rectangle((*p(6, -50), *p(30, 0)), fill="#6a4a2a")
    d.polygon([p(-52, -56), p(-38, -150), p(38, -150), p(52, -56)], fill="#8a6a3a", outline="#5a3e26"); d.rectangle((*p(-46, -78), *p(46, -62)), fill="#4f9a4a")
    d.ellipse((*p(-70, -172), *p(-28, -132)), fill="#9a9a96", outline="#5a5a56"); d.ellipse((*p(28, -172), *p(70, -132)), fill="#9a9a96", outline="#5a5a56")
    d.ellipse((*p(-42, -226), *p(42, -140)), fill="#f2f2ec"); d.ellipse((*p(-28, -212), *p(28, -148)), fill="#e8c8a0"); d.polygon([p(-24, -170), p(24, -170), p(14, -110), p(0, -100), p(-14, -110)], fill="#f2f2ec")
    _eyes(d, p, -196)
    d.polygon([p(-34, -222), p(34, -222), p(40, -250), p(20, -240), p(0, -278), p(-20, -240), p(-40, -250)], fill="#9a9a96", outline="#5a5a56"); d.polygon([p(-34, -222), p(34, -222), p(30, -230), p(-30, -230)], fill="#4f9a4a")


def thuy_tinh(d, cx, base, s, trident=True):
    """Sea god: pale blue skin, long dark-blue hair, coral crown, deep-blue wave robe, teal cape, golden trident."""
    p = _p(cx, base, s)
    if trident:
        d.line([p(-70, 6), p(-76, -340)], fill=GOLD, width=max(int(8 * s), 3)); d.polygon([p(-104, -330), p(-48, -330), p(-52, -392), p(-62, -350), p(-76, -410), p(-90, -350), p(-100, -392)], fill=GOLD, outline="#8a6a20")
    d.polygon([p(-76, -150), p(-100, 8), p(100, 8), p(76, -150)], fill="#2c8aa0")
    d.ellipse((*p(-46, -230), *p(46, -110)), fill="#14284a"); d.polygon([p(-46, -170), p(-60, -40), p(-20, -110)], fill="#14284a"); d.polygon([p(46, -170), p(60, -40), p(20, -110)], fill="#14284a")
    d.polygon([p(-56, 0), p(-36, -150), p(36, -150), p(56, 0)], fill="#1f4e8a", outline="#14284a")
    for i, y in enumerate((-120, -90, -60, -30)): d.arc((*p(-30 + i % 2 * 14, y), *p(14 + i % 2 * 14, y + 26)), 200, 340, fill="#8ac8e8", width=max(int(4 * s), 2))
    d.rectangle((*p(-40, -80), *p(40, -66)), fill="#e8603a")
    d.ellipse((*p(-28, -212), *p(28, -148)), fill="#bcd8e4"); _eyes(d, p, -192, "#14284a"); d.line([p(-10, -166), p(10, -166)], fill="#4a7a96", width=max(int(3 * s), 2))
    d.polygon([p(-30, -208), p(30, -208), p(36, -246), p(18, -228), p(0, -266), p(-18, -228), p(-36, -246)], fill="#e8603a", outline="#8a2a18")


def mi_nuong(d, cx, base, s):
    """Princess Mi Nuong: rose-pink dress, white sash, long black hair, white frangipani flowers in her hair."""
    p = _p(cx, base, s)
    d.ellipse((*p(-50, -230), *p(50, -50)), fill="#16121a"); d.polygon([p(-60, 0), p(-28, -140), p(28, -140), p(60, 0)], fill="#e8708a", outline="#a8405a")
    d.polygon([p(-26, -140), p(0, -100), p(26, -140)], fill="#fff4f0"); d.rectangle((*p(-34, -92), *p(34, -76)), fill="#fff4f0")
    d.ellipse((*p(-28, -212), *p(28, -148)), fill=SKIN); _eyes(d, p, -190); d.ellipse((*p(-24, -170), *p(-12, -162)), fill="#f0a8a8"); d.ellipse((*p(12, -170), *p(24, -162)), fill="#f0a8a8")
    d.polygon([p(-30, -206), p(30, -206), p(28, -178), p(0, -196), p(-28, -178)], fill="#16121a")
    for dx, dy in ((-22, -222), (0, -230), (22, -222)): d.ellipse((*p(dx - 12, dy - 10), *p(dx + 12, dy + 10)), fill="#ffffff", outline="#e8c8a0"); d.ellipse((*p(dx - 4, dy - 4), *p(dx + 4, dy + 4)), fill=GOLD)


def tom_binh(d, cx, base, s):
    """Shrimp soldier (about 120*s tall): orange curled body, long whiskers, tiny spear."""
    p = _p(cx, base, s)
    d.line([p(40, 0), p(52, -150)], fill="#6a4a2a", width=max(int(5 * s), 2)); d.polygon([p(52, -150), p(40, -126), p(64, -126)], fill="#cfd4da")
    d.ellipse((*p(-34, -86), *p(30, -10)), fill="#f26a3a", outline="#a83a1a"); d.polygon([p(-30, -34), p(-70, -6), p(-40, 8), p(-20, -10)], fill="#e8532a", outline="#a83a1a")
    d.ellipse((*p(-4, -118), *p(36, -76)), fill="#f26a3a", outline="#a83a1a"); d.ellipse((*p(14, -106), *p(24, -96)), fill="#111")
    d.line([p(30, -112), p(76, -150)], fill="#a83a1a", width=max(int(3 * s), 1)); d.line([p(30, -104), p(86, -120)], fill="#a83a1a", width=max(int(3 * s), 1))
    for x in (-18, -4, 10): d.line([p(x, -10), p(x - 6, 12)], fill="#a83a1a", width=max(int(3 * s), 1))


def cua_tuong(d, cx, base, s):
    """Crab general (about 100*s tall): wide red body, two raised claws, eye stalks, golden helmet."""
    p = _p(cx, base, s)
    for dx in (-1, 1):
        d.line([p(dx * 40, -50), p(dx * 90, -90)], fill="#a82a20", width=max(int(8 * s), 3)); d.polygon([p(dx * 90, -90), p(dx * 126, -140), p(dx * 70, -130), p(dx * 58, -104)], fill="#d8382d", outline="#8a1a14")
        for k in range(3): d.line([p(dx * (30 + k * 16), -20), p(dx * (66 + k * 22), 6)], fill="#a82a20", width=max(int(5 * s), 2))
    d.ellipse((*p(-62, -74), *p(62, 0)), fill="#d8382d", outline="#8a1a14")
    for dx in (-18, 18): d.line([p(dx, -70), p(dx, -96)], fill="#a82a20", width=max(int(4 * s), 2)); d.ellipse((*p(dx - 8, -108), *p(dx + 8, -92)), fill="#fff"); d.ellipse((*p(dx - 3, -104), *p(dx + 3, -96)), fill="#111")
    d.polygon([p(-34, -92), p(34, -92), p(26, -126), p(0, -140), p(-26, -126)], fill=GOLD, outline="#8a6a20")


def elephant(d, cx, base, s, flip=1):
    """Elephant with nine tusks, in profile facing right."""
    f = lambda dx, dy: (cx + dx * s * flip, base + dy * s)
    ell = lambda a, b, **k: d.ellipse((min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])), **k)
    rect = lambda a, b, **k: d.rectangle((min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])), **k)
    g = "#8a8f9a"
    for x in (-100, -50, 60, 110): rect(f(x - 22, -90), f(x + 22, 0), fill=g, outline="#5a5e68")
    ell(f(-150, -240), f(120, -60), fill=g, outline="#5a5e68"); ell(f(60, -260), f(190, -130), fill=g, outline="#5a5e68")
    d.polygon([f(150, -190), f(215, -150), f(222, -60), f(196, -60), f(190, -130), f(150, -150)], fill=g, outline="#5a5e68")
    ell(f(40, -220), f(110, -140), fill="#a0a5b0", outline="#5a5e68"); ell(f(150, -214), f(166, -198), fill="#111")
    for i in range(9): a = -0.6 + i * 0.15; d.polygon([f(176, -150), f(176 + 70 * math.cos(a) + 10, -140 - 70 * math.sin(a) + 30), f(176 + 74 * math.cos(a), -140 - 74 * math.sin(a) + 30)], fill="#f8f2dc", outline="#c8b88a")
    d.polygon([f(-150, -180), f(-190, -110), f(-170, -80), f(-140, -140)], fill=g)


def rooster(d, cx, base, s, flip=1):
    """Big rooster with nine spurs, in profile facing right."""
    f = lambda dx, dy: (cx + dx * s * flip, base + dy * s)
    ell = lambda a, b, **k: d.ellipse((min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])), **k)
    for i, col in enumerate(("#2a7a9a", "#c8372d", "#f2b632", "#2f9a5a", "#2a7a9a")): a = -0.2 + i * .35; d.polygon([f(-90, -150), f(-90 - 150 * math.cos(a), -150 - 160 * math.sin(a)), f(-70 - 150 * math.cos(a), -140 - 160 * math.sin(a))], fill=col)
    for x in (-10, 30): d.line([f(x, -80), f(x, 0)], fill="#d8a020", width=max(int(8 * s), 3))
    for i in range(9): d.polygon([f(-4 + (i % 3) * 18, -30 - (i // 3) * 22), f(-30 + (i % 3) * 18, -26 - (i // 3) * 22), f(-6 + (i % 3) * 18, -40 - (i // 3) * 22)], fill="#8a8a82")
    ell(f(-100, -170), f(70, -70), fill="#e8603a", outline="#8a2a18"); ell(f(30, -230), f(100, -150), fill="#e8603a", outline="#8a2a18")
    d.polygon([f(100, -198), f(140, -190), f(100, -178)], fill="#f2b632"); d.polygon([f(46, -232), f(60, -262), f(72, -236), f(86, -260), f(94, -230)], fill="#c8372d"); ell(f(74, -208), f(84, -198), fill="#111")
    d.polygon([f(-60, -140), f(10, -130), f(-20, -100)], fill="#c8372d")


def horse9(d, cx, base, s, flip=1):
    """Horse with a bright red mane (nine red hairs), facing right."""
    C.horse(d, cx, base, s, "#d8a050", flip)
    f = lambda dx, dy: (cx + dx * s * flip, base + dy * s)
    d.polygon([f(96, -160), f(172, -276), f(150, -280), f(70, -190)], fill="#c8372d")
    for i in range(9): x = 76 + i * 10; d.polygon([f(x, -200 - i * 8), f(x - 30, -214 - i * 8 - 14), f(x - 6, -190 - i * 8)], fill="#c8372d")


def hill(d, cx, base, w, h, col="#6a9a5a", edge="#3a6a34"):
    d.polygon([(cx - w, base), (cx - w * .5, base - h * .75), (cx, base - h), (cx + w * .5, base - h * .75), (cx + w, base)], fill=col, outline=edge)
    d.polygon([(cx, base - h), (cx + w * .5, base - h * .75), (cx + w, base), (cx + w * .2, base)], fill=edge)
