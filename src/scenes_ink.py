"""Ink style for people (thick black outline, pentagon head, short line eyes, flat fills) plus helpers to lighten dark scenes so the black outlines read."""
import os
from PIL import Image

INK = "#14121a"
SKIN, SKIN2 = "#ffe6dc", "#f5d2b4"


def ink_figure(d, cx, bottom, sc, kind="woman", mood="calm", prop=None):
    """Half-length character. Design box: 300 wide x 380 tall, centre x=150; sc = pixels per design unit; `bottom` = screen y of the cut bottom edge."""
    top = bottom - 380 * sc
    T = lambda x, y: (cx + x * sc, top + y * sc)
    w = max(int(5.2 * sc), 4)

    def poly(pts, fill): d.polygon([T(*p) for p in pts], fill=fill, outline=INK, width=w)
    def line(pts, ww=5.0, col=INK): d.line([T(*p) for p in pts], fill=col, width=max(int(ww * sc), 3))
    def blob(x0, y0, x1, y1, fill): d.ellipse((*T(x0, y0), *T(x1, y1)), fill=fill, outline=INK, width=w)
    def neck(skin): poly([(-15, 150), (15, 150), (20, 212), (-20, 212)], skin)

    def face(y, ink_col=INK):
        for sx in (-1, 1):
            x = sx * 22
            line([(x, y), (x, y + 30)], 5.2, ink_col)
            if mood == "worried": line([(x - 12, y - (10 if sx == -1 else 20)), (x + 12, y - (20 if sx == -1 else 10))], 4.6, ink_col)
            elif mood == "stern": line([(x - 12, y - (20 if sx == -1 else 10)), (x + 12, y - (10 if sx == -1 else 20))], 4.6, ink_col)
            elif mood == "shock": line([(x - 13, y - 24), (x + 13, y - 24)], 4.6, ink_col)
            else: line([(x - 13, y - 15), (x + 13, y - 15)], 4.6, ink_col)
        if mood == "worried": line([(-8, y + 50), (2, y + 44), (12, y + 50)], 4.6, ink_col); poly([(64, y - 4), (74, y + 18), (54, y + 18)], "#8fd0f0")
        elif mood == "shock": d.ellipse((*T(-8, y + 38), *T(8, y + 60)), fill="#4a1a1a", outline=INK, width=max(w - 2, 3))
        elif mood == "happy": d.arc((*T(-14, y + 34), *T(14, y + 56)), 15, 165, fill=ink_col, width=max(int(4.6 * sc), 3))
        elif mood == "stern": line([(-10, y + 46), (10, y + 46)], 4.6, ink_col)
        else: line([(-9, y + 42), (-3, y + 49), (11, y + 46)], 4.6, ink_col)

    if kind == "woman":
        HAIR, TOP = "#4a2a2a", "#e8607f"
        poly([(-100, 380), (-92, 224), (-40, 198), (40, 198), (92, 224), (100, 380)], TOP); poly([(-22, 194), (0, 224), (22, 194), (14, 190), (-14, 190)], "#fff6f2"); neck(SKIN)
        blob(-24, 28, 28, 78, HAIR); poly([(-58, 150), (-62, 76), (-20, 52), (40, 56), (62, 82), (58, 150), (46, 176), (-46, 176)], HAIR)
        poly([(-52, 78), (52, 74), (50, 160), (0, 188), (-52, 158)], SKIN)
        poly([(-54, 118), (-52, 80), (-6, 66), (46, 76), (52, 84), (50, 112), (20, 96), (-14, 92)], HAIR); face(126)
        if prop == "phone":
            poly([(-17, 290), (17, 290), (17, 350), (-17, 350)], "#8fe0f4"); blob(-36, 326, -8, 352, SKIN); blob(8, 326, 36, 352, SKIN)
        elif prop == "ear": poly([(56, 120), (74, 120), (74, 168), (56, 168)], "#8fe0f4")
    elif kind in ("girl", "girl2"):  # schoolgirl: white shirt, navy pinafore; girl = ponytail (orange tie), girl2 = bob with pink hairband
        HAIR, NAVY = "#1d1822", "#2f4a86"
        poly([(-100, 380), (-92, 230), (-44, 204), (44, 204), (92, 230), (100, 380)], "#ffffff"); neck(SKIN)
        poly([(-30, 200), (0, 252), (-48, 228)], "#ffffff"); poly([(30, 200), (0, 252), (48, 228)], "#ffffff"); poly([(-62, 380), (-58, 246), (0, 276), (58, 246), (62, 380)], NAVY)
        if kind == "girl":
            poly([(36, 66), (98, 92), (112, 206), (86, 240), (78, 150), (50, 108)], HAIR)
            poly([(-52, 78), (52, 74), (50, 160), (0, 188), (-52, 158)], SKIN)
            poly([(-56, 96), (-52, 62), (-6, 44), (48, 56), (56, 92), (30, 102), (-14, 84)], HAIR); blob(50, 64, 74, 86, "#ff9a3c")
        else:
            poly([(-64, 176), (-68, 70), (-10, 42), (50, 48), (68, 76), (64, 176), (40, 182), (-40, 182)], HAIR)
            poly([(-52, 84), (52, 80), (50, 160), (0, 188), (-52, 158)], SKIN)
            poly([(-54, 104), (-52, 70), (0, 58), (52, 68), (54, 104), (0, 96)], HAIR); poly([(-58, 64), (58, 60), (58, 76), (-58, 80)], "#ff7aa8")
        face(114)
        if prop == "phone":
            poly([(-17, 290), (17, 290), (17, 350), (-17, 350)], "#8fe0f4"); blob(-36, 326, -8, 352, SKIN); blob(8, 326, 36, 352, SKIN)
        elif prop == "ear": poly([(56, 120), (74, 120), (74, 168), (56, 168)], "#8fe0f4")
    elif kind == "teller":
        poly([(-104, 380), (-96, 230), (-44, 198), (44, 198), (96, 230), (104, 380)], "#ffffff")
        poly([(-30, 194), (-6, 228), (-36, 224), (-50, 202)], "#ffffff"); poly([(30, 194), (6, 228), (36, 224), (50, 202)], "#ffffff")
        poly([(-8, 224), (8, 224), (14, 380), (-14, 380)], "#7aa8c8"); blob(-12, 214, 12, 236, "#7aa8c8")
        poly([(36, 262), (74, 260), (76, 298), (56, 308), (38, 298)], "#ffffff"); line([(38, 274), (74, 272)], 4); neck(SKIN)
        poly([(-52, 74), (52, 70), (50, 156), (0, 184), (-52, 154)], SKIN)
        poly([(-56, 74), (-44, 36), (20, 28), (62, 52), (52, 84), (40, 74), (-10, 64), (-54, 94)], "#3a2418"); face(122)
        if prop == "ear": poly([(56, 110), (74, 110), (74, 158), (56, 158)], "#8fe0f4")
    elif kind == "officer":
        GR = "#4a8a5c"
        poly([(-104, 380), (-96, 230), (-44, 198), (44, 198), (96, 230), (104, 380)], GR); poly([(-30, 194), (0, 232), (30, 194)], "#e8e2c8"); poly([(30, 262), (56, 262), (56, 288), (30, 288)], "#f2c13a")
        poly([(-94, 232), (-52, 206), (-46, 224), (-88, 252)], "#f2c13a"); poly([(94, 232), (52, 206), (46, 224), (88, 252)], "#f2c13a"); neck(SKIN2)
        poly([(-52, 88), (52, 84), (50, 170), (0, 198), (-52, 168)], SKIN2)
        poly([(-60, 96), (-56, 46), (-6, 28), (50, 34), (60, 52), (58, 96)], GR); poly([(-78, 96), (78, 90), (74, 108), (-74, 112)], "#1c1a24"); blob(-12, 44, 14, 70, "#f2c13a"); face(134); line([(-22, 172), (22, 172)], 6)
        if prop == "ear": poly([(58, 124), (76, 124), (76, 172), (58, 172)], "#8fe0f4")
    else:  # scammer: dark hood, black face, white eyes and smile
        DK = "#2d2848"
        poly([(-104, 380), (-94, 228), (-44, 194), (44, 194), (94, 228), (104, 380)], DK); poly([(-74, 150), (-70, 56), (0, 26), (70, 56), (74, 150), (60, 214), (-60, 214)], DK)
        poly([(-46, 90), (46, 88), (44, 170), (0, 196), (-44, 170)], "#0a0910")
        for sx in (-1, 1): line([(sx * 20, 116), (sx * 20, 144)], 5.0, "#f4f4ee")
        d.arc((*T(-18, 150), *T(18, 176)), 20, 160, fill="#f4f4ee", width=max(int(4 * sc), 3))


def light(c, k=.86):
    return tuple(int(v + (255 - v) * k) for v in c[:3])


def lighten_scene(res, k=None):
    k = float(os.environ.get("INK_K", .86)) if k is None else k
    """Take (bg_image, layers) from a dark scene function and return a pastel version: bg blended with white, glow / sparkle layers dropped."""
    bg, layers = res
    bg = Image.blend(bg.convert("RGB"), Image.new("RGB", bg.size, (255, 255, 255)), k)
    return bg, [l for l in layers if l[1] not in ("glow", "sparkle")]


class InkD:
    """Draw proxy that gives every filled shape the same thick black outline as the people, so props and backgrounds match the characters.
    Width scales with the shape (3..8 px); translucent fills and tiny shapes are left alone."""
    def __init__(self, d): self._d = d

    def __getattr__(self, n): return getattr(self._d, n)

    @staticmethod
    def _box(xy):
        pts = list(xy)
        if pts and isinstance(pts[0], (tuple, list)): xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        else: xs, ys = pts[0::2], pts[1::2]
        return min(xs), min(ys), max(xs), max(ys)

    def _call(self, name, xy, args, k):
        fill = k.get("fill")
        solid = fill is not None and not (isinstance(fill, tuple) and len(fill) == 4 and fill[3] < 200)
        if solid and k.get("outline") != INK:
            x0, y0, x1, y1 = self._box(xy); sz = min(x1 - x0, y1 - y0)
            if sz >= 18: k["outline"] = INK; k["width"] = int(max(3, min(8, sz * .07)))
        return getattr(self._d, name)(xy, *args, **k)

    def polygon(self, xy, *a, **k): return self._call("polygon", xy, a, k)
    def ellipse(self, xy, *a, **k): return self._call("ellipse", xy, a, k)
    def rectangle(self, xy, *a, **k): return self._call("rectangle", xy, a, k)
    def pieslice(self, xy, *a, **k): return self._call("pieslice", xy, a, k)
