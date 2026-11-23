"""Opening sequence idea: cover frame = first frame of the video. Big title is also the first caption; mascot big; then paper-tear into the story."""
import math, random
from PIL import Image, ImageDraw, ImageFilter, ImageChops
import animate as A, story2 as S2, story3 as X, tulinh3 as M
from tulinh2 import caption_sprite
from tulinh import font, F_BLACK, F_BOLD
W, H = 1080, 1920
random.seed(5)
scenes = X.build_scenes()
for sc in scenes: sc["data"] = sc["mid"]()
glow, mist = A.sprite_glow(), Image.new("RGBA", (10, 10))
base = lambda i, t: S2.frame(scenes[i], t, 5, glow, mist).convert("RGBA")
PAPER, INK = (244, 234, 210, 255), (20, 33, 61, 255)


def shadowed(layer, off=(0, 10), blur=10, a=110):
    sh = Image.new("RGBA", layer.size, (0, 0, 0, 0)); sh.putalpha(layer.split()[3].point(lambda v: int(v * a / 255))); return Image.alpha_composite(ImageChops.offset(sh, *off).filter(ImageFilter.GaussianBlur(blur)), layer)


def title(im, alpha=1.0, dy=0):
    L = Image.new("RGBA", (W, 700), (0, 0, 0, 0)); d = ImageDraw.Draw(L); f = font(F_BLACK, 152)
    for j, (t_, col) in enumerate((("TRẢ GƯƠM", (255, 216, 77, 255)), ("CHO AI?", (255, 255, 255, 255)))):
        xy = (W / 2, 150 + j * 190)
        d.text(xy, t_, font=f, fill="white", anchor="mm", stroke_width=32, stroke_fill="white"); d.text(xy, t_, font=f, fill=INK, anchor="mm", stroke_width=15, stroke_fill=INK); d.text(xy, t_, font=f, fill=col, anchor="mm")
    if alpha < 1: L.putalpha(L.split()[3].point(lambda v: int(v * alpha)))
    im.alpha_composite(L, (0, 160 + dy))


def mascot(im, pose, h, cx, sink=0, rot=0):
    m = M.mascot(pose, h); pad = Image.new("RGBA", (m.width + 120, m.height + 20), (0, 0, 0, 0)); pad.alpha_composite(m, (60, 0))
    if rot: pad = pad.rotate(rot, center=(pad.width / 2, pad.height), resample=Image.BILINEAR)
    im.alpha_composite(pad, (int(cx - pad.width / 2), int(H - m.height + 6 + sink)))


def torn_wipe(old, new, x):
    edge = [(x + 36 * math.sin(y / 70) + random.randint(-14, 14), y) for y in range(0, H + 40, 40)]
    mask = Image.new("L", (W, H), 0); ImageDraw.Draw(mask).polygon([(0, 0)] + edge + [(0, H)], fill=255); out = Image.composite(old, new, mask)
    strip = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(strip).polygon([(px + 4, py) for px, py in edge] + [(px + 40 + random.randint(-6, 6), py) for px, py in reversed(edge)], fill=PAPER)
    return Image.alpha_composite(out, shadowed(strip, (-8, 0), 14, 130))


def cover(t, pose, sink=0, a=1.0, dy=0, rot=0):
    """Rays + glow behind; the sword leans diagonally BEHIND the mascot's head (like a sword on the back); big mascot, eyes above the bottom UI zone."""
    bg, layers = scenes[4]["data"]; im = bg.copy().convert("RGBA")
    rays = next(l[2] for l in layers if l[1] == "rays").rotate(t * 9, resample=Image.BILINEAR); im.paste(rays, (540 - 950, 800 - 950), rays)
    im.alpha_composite(S2.sword_glow(540, 820, 330))
    sw = S2.sword_rgba(640); cv = Image.new("RGBA", (1500, 1500), (0, 0, 0, 0)); cv.alpha_composite(sw, (700 - 60, 700 - sw.height + 20)); cv = cv.rotate(-27, center=(700, 700), resample=Image.BICUBIC)
    im.alpha_composite(cv, (610 - 700, 1320 - 700 + int(10 * math.sin(t * 2))) if False else (610 - 700, 1320 - 700))
    title(im, a, dy); mascot(im, pose, 1150, 540, sink + 16, rot); return im


F0 = cover(0.0, 0)                                     # first frame = cover
F1 = cover(1.1, 1, 0, 1.0, 0, 2)                       # mascot switches to the thinking pose on "cho ai?"
F2 = cover(1.9, 1, 300, 0.45, -50, 2)                  # title lifts away, mascot sinks
S = base(0, 0.3); cap = caption_sprite("hà nội có một"); S.alpha_composite(cap, (int(W / 2 - cap.width / 2), int(1345 - cap.height / 2)))
F3 = torn_wipe(cover(2.2, 1, 560, 0.0, -90), S, 470)   # paper tear reveals scene 1
F0.convert("RGB").save("out/bia_mo_dau.png")
labels = ["0.0s  Khung đầu = ảnh bìa", "1.1s  Mascot đổi sang chống cằm", "1.9s  Chữ bay đi, mascot chìm", "2.3s  Xé giấy sang cảnh đầu"]
sheet = Image.new("RGB", (4 * 370 + 10, 690), "#111"); g = ImageDraw.Draw(sheet)
for i, (im, lab) in enumerate(zip((F0, F1, F2, F3), labels)): sheet.paste(im.convert("RGB").resize((360, 640)), (i * 370, 44)); g.text((i * 370 + 180, 22), lab, font=font(F_BOLD, 17), fill="white", anchor="mm")
sheet.save("out/mo_dau_4_frame.png"); print("ok")
