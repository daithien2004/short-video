"""Characters and props for the Nvidia CEO news explainer (paper-cut, simple faces). (d, cx, base, s): feet at (cx, base), height ~232*s."""
import math
from story2 import RED, GOLD, INK, EDGE
from chars_st import _p, _eyes

GREEN_NV = "#76b900"


def huang(d, cx, base, s):
    """Jensen Huang (from the user's reference photo): silver-grey swept-back hair, thin half-rim glasses, slight smile, black leather jacket with a stand collar and silver zips, arms crossed, dark trousers."""
    p = _p(cx, base, s)
    d.polygon([p(-34, -84), p(-8, -84), p(-12, 0), p(-38, 0)], fill="#2a3040"); d.polygon([p(8, -84), p(34, -84), p(38, 0), p(12, 0)], fill="#2a3040"); d.rectangle((*p(-40, -8), *p(-8, 0)), fill="#16161a"); d.rectangle((*p(8, -8), *p(40, 0)), fill="#16161a")
    LT = "#16161a"; ED = "#05050a"; HL = "#3c3c46"  # black leather, edge, glossy highlight
    d.polygon([p(-58, -146), p(-44, -156), p(44, -156), p(58, -146), p(52, -84), p(40, -78), p(-40, -78), p(-52, -84)], fill=LT, outline=ED)  # fitted torso with sloped shoulders
    d.line([p(0, -150), p(0, -78)], fill="#c8ccd4", width=max(int(4 * s), 2)); d.polygon([p(-18, -168), p(18, -168), p(20, -148), p(-20, -148)], fill=LT, outline=ED); d.ellipse((*p(8, -162), *p(15, -155)), fill="#c8ccd4")  # zip, stand collar, snap
    for sx in (-1, 1): d.line([p(sx * 14, -126), p(sx * 40, -112)], fill="#c8ccd4", width=max(int(3 * s), 2))  # diagonal chest zip pockets
    d.polygon([p(-60, -148), p(-48, -152), p(-50, -106), p(-68, -110)], fill=LT, outline=ED); d.polygon([p(60, -148), p(48, -152), p(50, -106), p(68, -110)], fill=LT, outline=ED)  # upper arms
    d.polygon([p(-68, -122), p(-68, -100), p(48, -94), p(48, -116)], fill="#22222a", outline=ED); d.polygon([p(68, -114), p(68, -92), p(-46, -98), p(-46, -120)], fill="#1c1c22", outline=ED)  # forearms crossed over the chest
    d.line([p(-58, -146), p(-48, -112)], fill=HL, width=max(int(3 * s), 2)); d.line([p(58, -146), p(48, -112)], fill=HL, width=max(int(3 * s), 2)); d.line([p(-60, -112), p(40, -106)], fill=HL, width=max(int(2 * s), 1))  # leather shine
    d.ellipse((*p(40, -112), *p(60, -94)), fill="#e8c8a0")  # one hand tucked, fingers showing
    d.ellipse((*p(-30, -216), *p(30, -146)), fill="#e8c8a0"); _eyes(d, p, -192)
    for sx in (-1, 1): d.rectangle((*p(min(sx * 6, sx * 22), -198), *p(max(sx * 6, sx * 22), -184)), outline="#16161a", width=max(int(2 * s), 1))  # half-rim glasses
    d.line([p(-6, -192), p(6, -192)], fill="#16161a", width=max(int(2 * s), 1)); d.arc((*p(-12, -178), *p(12, -160)), 20, 160, fill="#7a4a3a", width=max(int(3 * s), 2))
    d.polygon([p(-32, -204), p(-30, -226), p(-14, -242), p(6, -246), p(26, -238), p(34, -220), p(30, -204), p(24, -214), p(0, -226), p(-20, -216)], fill="#c8ccd4", outline="#8a8e9a")


def trump(d, cx, base, s):
    """Donald Trump: navy suit, long red tie, golden swept hair, warm skin tone, neutral face."""
    p = _p(cx, base, s)
    d.rectangle((*p(-24, -52), *p(-4, 0)), fill="#14203a"); d.rectangle((*p(4, -52), *p(24, 0)), fill="#14203a")
    d.polygon([p(-60, -40), p(-40, -150), p(40, -150), p(60, -40)], fill="#1f2f5a", outline="#0e1630"); d.polygon([p(-16, -150), p(0, -100), p(16, -150)], fill="#f4f4f0")
    d.polygon([p(-6, -146), p(6, -146), p(10, -60), p(0, -46), p(-10, -60)], fill=RED, outline="#7a2018")
    d.ellipse((*p(-30, -216), *p(30, -146)), fill="#f0c090"); _eyes(d, p, -192); d.line([p(-10, -168), p(10, -168)], fill="#8a4a3a", width=max(int(3 * s), 2))
    d.polygon([p(-34, -196), p(34, -196), p(38, -232), p(10, -246), p(-30, -236)], fill="#e8c060"); d.polygon([p(-34, -222), p(-60, -214), p(-30, -200)], fill="#e8c060")


def suit(d, cx, base, s, col="#6a6e7a", tie="#2f6a8a"):
    """Generic board member / lawmaker: plain suit, round head, simple face (no individual likeness)."""
    p = _p(cx, base, s)
    d.rectangle((*p(-24, -52), *p(-4, 0)), fill="#3a3d48"); d.rectangle((*p(4, -52), *p(24, 0)), fill="#3a3d48")
    d.polygon([p(-58, -40), p(-38, -150), p(38, -150), p(58, -40)], fill=col, outline="#3a3d48"); d.polygon([p(-14, -150), p(0, -104), p(14, -150)], fill="#f4f4f0"); d.polygon([p(-5, -146), p(5, -146), p(8, -74), p(0, -62), p(-8, -74)], fill=tie)
    d.ellipse((*p(-30, -216), *p(30, -146)), fill="#e6c6a0"); _eyes(d, p, -192); d.line([p(-10, -168), p(10, -168)], fill="#8a4a3a", width=max(int(3 * s), 2)); d.polygon([p(-30, -202), p(-24, -228), p(-6, -238), p(14, -234), p(28, -222), p(30, -202), p(18, -212), p(-18, -212)], fill="#4a4a52")


def shadow_figure(d, cx, base, s, col="#2a2d38"):
    """Anonymous source: flat dark silhouette, no face."""
    p = _p(cx, base, s)
    d.polygon([p(-60, 0), p(-44, -140), p(44, -140), p(60, 0)], fill=col); d.ellipse((*p(-32, -216), *p(32, -142)), fill=col)


def chip(d, cx, cy, w, col=GREEN_NV):
    h = w
    d.rectangle((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), fill="#1a1a22", outline="#05050a")
    for k in range(-3, 4):
        d.rectangle((cx + k * w * .13 - 6, cy - h / 2 - w * .1, cx + k * w * .13 + 6, cy - h / 2), fill="#c8ccd4"); d.rectangle((cx + k * w * .13 - 6, cy + h / 2, cx + k * w * .13 + 6, cy + h / 2 + w * .1), fill="#c8ccd4")
        d.rectangle((cx - w / 2 - w * .1, cy + k * h * .13 - 6, cx - w / 2, cy + k * h * .13 + 6), fill="#c8ccd4"); d.rectangle((cx + w / 2, cy + k * h * .13 - 6, cx + w / 2 + w * .1, cy + k * h * .13 + 6), fill="#c8ccd4")
    d.rectangle((cx - w * .32, cy - h * .32, cx + w * .32, cy + h * .32), fill=col); d.rectangle((cx - w * .2, cy - h * .2, cx + w * .2, cy + h * .2), fill="#1a1a22"); d.rectangle((cx - w * .1, cy - h * .1, cx + w * .1, cy + h * .1), fill=col)


def chair(d, cx, base, s, col="#2a2a32"):
    p = _p(cx, base, s)
    d.rectangle((*p(-70, -300), *p(70, -140)), fill=col, outline="#05050a"); d.polygon([p(-90, -140), p(90, -140), p(80, -90), p(-80, -90)], fill="#3a3a44", outline="#05050a")
    d.rectangle((*p(-8, -90), *p(8, -30)), fill="#8a8e9a"); d.polygon([p(-70, 0), p(-8, -30), p(8, -30), p(70, 0), p(50, 0), p(0, -20), p(-50, 0)], fill="#6a6e7a")


def doc(d, x0, y0, x1, y1, lines=6, redact=()):
    d.rectangle((x0, y0, x1, y1), fill="#f4f4ee", outline="#8a8e9a")
    h = (y1 - y0) / (lines + 1)
    for i in range(lines):
        y = y0 + h * (i + 1); d.line([(x0 + 24, y), (x1 - 24 - (i % 3) * 30, y)], fill="#16161a" if i in redact else "#b8bcc4", width=max(int(h * .35), 4))


def capitol(d, cx, base, w=900, h=520):
    d.rectangle((cx - w / 2, base - h * .35, cx + w / 2, base), fill="#e8e6dc", outline="#8a8e9a")
    for i in range(9): x = cx - w * .4 + i * w * .1; d.rectangle((x - 12, base - h * .35, x + 12, base), fill="#d4d2c6")
    d.polygon([(cx - w * .5, base - h * .35), (cx + w * .5, base - h * .35), (cx + w * .4, base - h * .5), (cx - w * .4, base - h * .5)], fill="#dcdacf", outline="#8a8e9a")
    d.rectangle((cx - w * .16, base - h * .72, cx + w * .16, base - h * .5), fill="#e8e6dc", outline="#8a8e9a"); d.pieslice((cx - w * .2, base - h * .95, cx + w * .2, base - h * .55), 180, 360, fill="#f4f2e8", outline="#8a8e9a"); d.rectangle((cx - 6, base - h * 1.04, cx + 6, base - h * .9), fill="#8a8e9a")


def flag(d, x, y, w, h):
    d.rectangle((x, y, x + w, y + h), fill="#f4f4f0", outline="#8a8e9a")
    for i in range(7): d.rectangle((x, y + i * h / 7, x + w, y + (i + .5) * h / 7), fill="#c8372d")
    d.rectangle((x, y, x + w * .42, y + h * 4 / 7), fill="#2a3f7a")
    for i in range(3):
        for j in range(4): d.ellipse((x + 8 + j * w * .1, y + 8 + i * h * .16, x + 14 + j * w * .1, y + 14 + i * h * .16), fill="#fff")
