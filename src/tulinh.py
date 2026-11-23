"""Tu Linh list video, reference-inspired: flat outlined chibi creatures, colour per section, two-tier title,
small captions + gold fact line, creatures pop in with the narration. Pure code."""
import math, os, sys, tempfile, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import shorts

W, H, FPS = 1080, 1920, 30
DK = "#1c1230"
F_BLACK, F_BOLD = "C:/Windows/Fonts/seguibl.ttf", "C:/Windows/Fonts/segoeuib.ttf"
font = lambda p, s: ImageFont.truetype(p, s)


def thick(d, pts, w, col, ol=DK, olw=9):
    for ww, c in ((w + 2 * olw, ol), (w, col)):
        d.line(pts, fill=c, width=ww, joint="curve")
        for x, y in (pts[0], pts[-1]): d.ellipse((x - ww / 2, y - ww / 2, x + ww / 2, y + ww / 2), fill=c)


def eye(d, x, y, r, look=0):
    d.ellipse((x - r, y - r, x + r, y + r), fill="white", outline=DK, width=5); d.ellipse((x - r * .5 + look, y - r * .5, x + r * .5 + look, y + r * .5), fill=DK)
    d.ellipse((x - r * .1 + look, y - r * .45, x + r * .25 + look, y - r * .1), fill="white")


def sprite(name):
    im = Image.new("RGBA", (700, 700), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if name == "long":  # dragon
        for k in range(8): a = math.radians(200 + k * 20); d.polygon([(350 + 120 * math.cos(a), 220 + 100 * math.sin(a)), (350 + 190 * math.cos(a + .1), 220 + 170 * math.sin(a + .1)), (350 + 120 * math.cos(a + .25), 220 + 100 * math.sin(a + .25))], fill="#ff7a3d", outline=DK, width=6)
        path = [(350, 330), (320, 400), (400, 470), (320, 540), (390, 610), (500, 630)]
        thick(d, path, 84, "#36b37e")
        for i, (x, y) in enumerate(path[1:-1]): d.polygon([(x - 50, y - 18), (x - 82, y), (x - 50, y + 22)], fill="#ff7a3d", outline=DK, width=5)
        d.polygon([(500, 600), (590, 580), (540, 640), (590, 690), (490, 660)], fill="#ff7a3d", outline=DK, width=6)
        for sx in (-1, 1):
            x0 = 350 + sx * 70; d.polygon([(x0 - sx * 14, 180), (x0 + sx * 44, 40), (x0 + sx * 18, 175)], fill="#ffd24d", outline=DK, width=6)
            thick(d, [(350 + sx * 60, 300), (350 + sx * 140, 340), (350 + sx * 190, 400)], 9, "#ffd24d", olw=5)
        d.ellipse((230, 140, 470, 340), fill="#36b37e", outline=DK, width=9); d.ellipse((270, 255, 430, 345), fill="#8be0b4", outline=DK, width=6)
        d.ellipse((322, 280, 336, 294), fill=DK); d.ellipse((364, 280, 378, 294), fill=DK); eye(d, 290, 205, 28); eye(d, 410, 205, 28)
        d.arc((320, 296, 380, 330), 20, 160, fill=DK, width=5)
    elif name == "quy":  # golden turtle
        d.rounded_rectangle((160, 500, 250, 610), 30, fill="#e0a21c", outline=DK, width=8); d.rounded_rectangle((450, 500, 540, 610), 30, fill="#e0a21c", outline=DK, width=8)
        dome = [(350 + 240 * math.cos(math.radians(a)), 470 - 220 * math.sin(math.radians(a))) for a in range(0, 181, 5)]
        d.polygon(dome, fill="#f2b632", outline=DK, width=10); d.ellipse((105, 450, 595, 520), fill="#d88f12", outline=DK, width=8)
        for gx, gy, r in ((-110, 350, 50), (0, 320, 56), (110, 350, 50), (-60, 410, 36), (60, 410, 36)): d.regular_polygon((350 + gx, gy, r), 6, fill="#ffd266", outline=DK, width=6)
        d.ellipse((40, 330, 230, 500), fill="#f2b632", outline=DK, width=9); eye(d, 110, 395, 26, -4); d.arc((60, 420, 150, 470), 20, 150, fill=DK, width=5)
        d.ellipse((70, 440, 100, 462), fill="#ff9aa8")
    elif name == "lan":  # qilin
        for x in (230, 400): d.rounded_rectangle((x, 470, x + 70, 620), 24, fill="#f08a3c", outline=DK, width=8)
        d.polygon([(500, 360), (620, 440), (560, 380), (640, 330), (520, 320)], fill="#e3402e", outline=DK, width=6)  # tail flame
        d.ellipse((190, 320, 530, 520), fill="#f08a3c", outline=DK, width=9)
        for k in range(4): d.polygon([(210 + k * 50, 300), (240 + k * 50, 230), (260 + k * 50, 310)], fill="#e3402e", outline=DK, width=6)  # mane flame
        d.ellipse((120, 200, 300, 370), fill="#f08a3c", outline=DK, width=9); d.polygon([(190, 215), (170, 120), (225, 205)], fill="#ffd24d", outline=DK, width=6)
        eye(d, 190, 285, 24); d.arc((150, 305, 230, 345), 20, 160, fill=DK, width=5); d.ellipse((140, 310, 168, 330), fill="#ff9aa8")
    elif name == "phung":  # phoenix
        for ang, col in ((20, "#3da8e0"), (50, "#36b37e"), (80, "#ffd24d")): d.ellipse((300, 400, 640, 480), fill=col, outline=DK, width=7) if False else None
        for ang, col in ((-10, "#3da8e0"), (15, "#36b37e"), (40, "#ffd24d")):
            leaf = Image.new("RGBA", (700, 700), (0, 0, 0, 0)); ld = ImageDraw.Draw(leaf); ld.ellipse((380, 440, 680, 520), fill=col, outline=DK, width=7)
            im.alpha_composite(leaf.rotate(ang, center=(350, 450), resample=Image.BICUBIC)); d = ImageDraw.Draw(im)
        d.ellipse((190, 300, 480, 560), fill="#ff5a4a", outline=DK, width=9); d.ellipse((280, 380, 440, 520), fill="#ff8a6a", outline=DK, width=7)
        d.ellipse((150, 200, 320, 360), fill="#ff5a4a", outline=DK, width=9)
        for k in range(3): d.polygon([(190 + k * 34, 215), (205 + k * 34, 120), (232 + k * 34, 210)], fill="#ffd24d", outline=DK, width=6)
        d.polygon([(150, 270), (80, 300), (150, 320)], fill="#ffd24d", outline=DK, width=6); eye(d, 215, 270, 24); d.rectangle((250, 560, 262, 640), fill=DK); d.rectangle((400, 560, 412, 640), fill=DK)
    return im


SPR = {}
def spr(n):
    if n not in SPR: SPR[n] = sprite(n)
    return SPR[n]


def ease_back(u):
    if u <= 0: return 0.0
    if u >= 1: return 1.0
    c1 = 2.2; c3 = c1 + 1; return 1 + c3 * (u - 1) ** 3 + c1 * (u - 1) ** 2


def bg_img(c0, c1, glow):
    im = Image.new("RGB", (W, H)); d = ImageDraw.Draw(im)
    for y in range(H): t = y / H; d.line((0, y, W, y), fill=tuple(int(a + (b - a) * t) for a, b in zip(c0, c1)))
    gl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(gl).ellipse((140, 500, 940, 1300), fill=glow + (90,))
    return Image.alpha_composite(im.convert("RGBA"), gl.filter(ImageFilter.GaussianBlur(120))).convert("RGB")


def spaced(d, xy, text, f, fill, sp=5, anchor="m", stroke=0, sf=DK):
    ws = [d.textlength(c, font=f) for c in text]; tot = sum(ws) + sp * (len(text) - 1); x = xy[0] - tot / 2
    for c, w in zip(text, ws): d.text((x, xy[1]), c, font=f, fill=fill, anchor="lm", stroke_width=stroke, stroke_fill=sf); x += w + sp


SCENES = [
    dict(name="intro", bg=((34, 22, 70), (14, 10, 34), (120, 70, 220)), main="TỨ LINH", mc="#e6e1f5", sub="4 LINH VẬT THIÊNG CỦA NGƯỜI VIỆT", sc="#b9b0d8", fact="LONG · LÂN · QUY · PHỤNG",
         items=[("long", 270, 800, 0.5, 0.8), ("lan", 810, 800, 0.5, 1.5), ("quy", 270, 1090, 0.5, 2.2), ("phung", 810, 1090, 0.5, 2.9)]),
    dict(name="long", bg=((130, 40, 20), (60, 14, 8), (255, 140, 40)), main="LONG", mc="#ffd24d", sub="RỒNG · BIỂU TƯỢNG QUYỀN UY", sc="#ffd9b0", fact="CON RỒNG CHÁU TIÊN", items=[("long", 540, 850, 1.12, 0.4)]),
    dict(name="quy", bg=((20, 70, 130), (8, 24, 60), (80, 170, 255)), main="QUY", mc="#ffe27a", sub="RÙA · TRƯỜNG THỌ & TRÍ TUỆ", sc="#bfe0ff", fact="RÙA VÀNG Ở HỒ GƯƠM", items=[("quy", 540, 880, 1.2, 0.4)]),
    dict(name="hoi", bg=((34, 22, 70), (14, 10, 34), (120, 70, 220)), main="CÂU HỎI", mc="#ffd24d", sub="CHO BẠN", sc="#b9b0d8", fact="", items=[("long", 270, 800, 0.5, 0.3), ("lan", 810, 800, 0.5, 0.7), ("quy", 270, 1090, 0.5, 1.1), ("phung", 810, 1090, 0.5, 1.5)], q=True),
]
BEATS = [
    "Người Việt có bốn con vật thiêng, gọi là Tứ Linh. Con nào quyền năng nhất?",
    "Đầu tiên là Long, con rồng. Rồng tượng trưng cho quyền uy, và làm mưa thuận gió hòa. Theo truyền thuyết, người Việt là con rồng cháu tiên.",
    "Thứ hai là Quy, con rùa. Rùa tượng trưng cho trường thọ và trí tuệ. Nhớ rùa vàng đòi gươm ở hồ Gươm không? Đó cũng là một Quy.",
    "Còn Lân và Phụng thì sao? Theo bạn, con nào mạnh nhất? Bình luận cho mình biết nhé.",
]


def render_frame(sc, t, bgs, cap, fact_alpha=True):
    im = bgs.copy().convert("RGBA")
    for n, x, y, s, t0 in sc["items"]:
        k = ease_back((t - t0) / 0.4)
        if k <= 0: continue
        sp = spr(n); z = s * k; sz = max(int(700 * z), 2); pic = sp.resize((sz, sz), Image.LANCZOS)
        bob = 8 * math.sin(2 * math.pi * t / 2.4 + x)
        im.alpha_composite(pic, (int(x - sz / 2), int(y - sz / 2 + bob))) if (int(x - sz / 2) >= 0 and int(y - sz / 2 + bob) >= 0 and int(x - sz / 2) + sz <= W and int(y - sz / 2 + bob) + sz <= H) else im.paste(pic, (int(x - sz / 2), int(y - sz / 2 + bob)), pic)
        if sc.get("q") and t > t0 + 0.4:
            d = ImageDraw.Draw(im); qx, qy = x, y - 190 * (s / 0.5) * 0.5 - 40; d.ellipse((qx - 36, qy - 36, qx + 36, qy + 36), fill="#ffd24d", outline=DK, width=6); d.text((qx, qy), "?", font=font(F_BLACK, 50), fill=DK, anchor="mm")
    d = ImageDraw.Draw(im); a = min(max(t / 0.35, 0), 1); dy = int((1 - a) * -30)
    d.text((W / 2, 250 + dy), sc["main"], font=font(F_BLACK, 130), fill=sc["mc"], anchor="mm", stroke_width=9, stroke_fill=DK)
    spaced(d, (W / 2, 350 + dy), sc["sub"], font(F_BOLD, 38), sc["sc"], 5, stroke=5)
    if sc.get("q"):
        c = Image.new("RGBA", (W, 260), (0, 0, 0, 0)); cd = ImageDraw.Draw(c); cd.rounded_rectangle((90, 20, 990, 220), 36, fill=(20, 12, 40, 235), outline="#ffd24d", width=5)
        cd.ellipse((120, 70, 190, 140), fill="#ffd24d"); cd.text((155, 105), "?", font=font(F_BLACK, 56), fill=DK, anchor="mm"); cd.text((220, 84), "Theo bạn, linh vật nào", font=font(F_BOLD, 46), fill="white", anchor="lm"); cd.text((220, 148), "quyền năng nhất?", font=font(F_BOLD, 46), fill="white", anchor="lm")
        if t > 1.2: im.alpha_composite(c, (0, 1330))
    elif sc["fact"] and t > 0.9:
        spaced(d, (W / 2, 1560), sc["fact"], font(F_BLACK, 52), "#ffd666", 7, stroke=6)
    if cap:
        words, cur = cap; f = font(F_BOLD, 74); ws = [d.textlength(w, font=f) for w in words]; x = W / 2 - (sum(ws) + 22 * (len(words) - 1)) / 2
        for i, (w, wd) in enumerate(zip(words, ws)):
            d.text((x, 1300), w, font=f, fill="#ffd24d" if i == cur else "white", anchor="lm", stroke_width=7, stroke_fill=DK); x += wd + 22
    return im.convert("RGB")


def main(beats, out):
    audio, words, t0, ranges = [], [], 0.0, []
    for text in beats:
        a = shorts.speak(text); dd = len(a) / shorts.SR
        words += shorts.spread(text, t0, t0 + dd); ranges.append((t0, t0 + dd + shorts.GAP))
        audio += [a, np.zeros(int(shorts.GAP * shorts.SR), np.float32)]; t0 += dd + shorts.GAP
    ranges[-1] = (ranges[-1][0], t0 + 0.8); total = t0 + 0.8
    groups, cur = [], []
    for i, w in enumerate(words):
        cur.append(i)
        if len(cur) == 3 or w[3]: groups.append(cur); cur = []
    if cur: groups.append(cur)
    gid = {i: g for g, idx in enumerate(groups) for i in idx}
    bgs = [bg_img(*sc["bg"]) for sc in SCENES]
    import soundfile as sf
    wav = os.path.join(tempfile.gettempdir(), "tulinh.wav"); sf.write(wav, shorts.mix(np.concatenate(audio), [r[0] for r in ranges[1:]], total), shorts.SR)
    p = subprocess.Popen([shorts.FFMPEG, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", wav, "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
                          "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", out], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    for fr in range(int(total * FPS)):
        t = fr / FPS; k = next((i for i, (a, b) in enumerate(ranges) if a <= t < b), len(ranges) - 1)
        ci = next((i for i, w in enumerate(words) if w[0] <= t < w[1] + 0.05), None); cap = None
        if ci is not None: idx = groups[gid[ci]]; cap = ([words[i][2] for i in idx], idx.index(ci))
        p.stdin.write(render_frame(SCENES[k], t - ranges[k][0], bgs[k], cap).tobytes())
    p.stdin.close(); p.wait()
    return out, total


def stills(out):
    cells = []
    for sc in SCENES:
        bg = bg_img(*sc["bg"]); cells.append(render_frame(sc, 5.0, bg, (["đầu", "tiên", "là"], 1)).resize((270, 480)))
    s = Image.new("RGB", (270 * 4, 480), "#111")
    for i, c in enumerate(cells): s.paste(c, (i * 270, 0))
    s.save(out)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "still": stills("out/tulinh_stills.png"); print("ok")
    else: print(main(BEATS, "out/tulinh_preview.mp4"))
