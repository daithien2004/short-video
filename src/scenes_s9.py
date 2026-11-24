"""Scenes for scam_job (việc nhẹ lương cao, dụ dỗ thiếu niên đi làm xa). Prefix s9_.
Ink style, black outlines, pastel bg (86% white mix). No text in images. No rounded_rectangle."""
import math
import story2 as S
from story2 import W, H, GOLD, grad
from scenes_hk2 import L, bob, sway
from scenes_ink import InkD, ink_figure, lighten_scene
from scenes_sc3 import (coin, bill, qmark, bubble, floor, room, bankhall, screen,
                        avatar, zoom, figure, shadow, _padlock, _cross)

def zoom(*a, **k): pass  # no connector lines from hands to screens (looked like stray grey strokes)


def room(d, v=0): floor(d, 1560, "#d9cdb8", "#c9bba4")  # plain floor only, no window/decor


PINK, TEAL, RED_, ORG, GRN, BLU = "#ff5d8f", "#2ec4b6", "#d6403a", "#ff9a3c", "#3fae5a", "#3a6ac8"
INK = "#14121a"
DARK0, DARK1 = (40, 48, 60), (70, 84, 100)  # night: dark but still lightened for black outlines


def _bg(c0=(24, 22, 52), c1=(70, 60, 110)):
    return grad(c0, c1).convert("RGBA")


def scene(fn, c0=(24, 22, 52), c1=(70, 60, 110), anim=None, k=None):
    bg = _bg(c0, c1).convert("RGB")
    res = (bg, [(1.0, L(lambda d: fn(InkD(d)), 12, 10), anim or bob(4, 1.1))])
    return lighten_scene(res, k)


def night_scene(fn, anim=None):
    # darker base, slightly less whitening so night reads but black outlines still visible
    return scene(fn, DARK0, DARK1, anim, k=0.78)


# ================= Đoạn 1 =================
def calendar():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        # paper calendar
        d.rectangle((180, 420, 900, 1180), fill="#f4f4ee", outline=INK, width=8)
        d.rectangle((180, 420, 900, 560), fill=RED_, outline=INK, width=8)
        # grid
        for i in range(1, 6):
            y = 560 + i * 124
            d.line([(220, y), (860, y)], fill="#c8ccd4", width=4)
        for i in range(1, 7):
            x = 180 + i * 103
            d.line([(x, 560), (x, 1180)], fill="#c8ccd4", width=4)
        # circled day (no number)
        d.ellipse((560, 820, 700, 960), outline=RED_, width=10)
    return scene(draw, (30, 30, 50), (80, 80, 110))


def hills_village():
    def draw(d):
        # low hills and a few highland houses
        d.polygon([(0, 1280), (200, 980), (420, 1120), (640, 900), (860, 1060), (1080, 920), (1080, 1920), (0, 1920)], fill="#7a9a72")
        d.polygon([(0, 1400), (260, 1160), (520, 1300), (780, 1100), (1080, 1260), (1080, 1920), (0, 1920)], fill="#5f8358")
        for x, y, w, h in ((180, 1220, 120, 90), (360, 1280, 130, 95), (620, 1180, 120, 90), (800, 1240, 110, 85)):
            d.polygon([(x - 10, y), (x + w / 2, y - 55), (x + w + 10, y)], fill="#8a5a3a", outline=INK, width=5)
            d.rectangle((x, y, x + w, y + h), fill="#e8dcc8", outline=INK, width=5)
            d.rectangle((x + w * 0.4, y + h * 0.45, x + w * 0.6, y + h), fill="#5a3a2a")
        # winding path
        d.line([(540, 1500), (480, 1400), (560, 1320)], fill="#d9cdb8", width=18)
    return scene(draw, (70, 120, 170), (140, 170, 200))


def danang_map():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        # same village cluster small in center
        for x, y, w, h in ((420, 980, 90, 70), (540, 1010, 95, 75), (660, 990, 85, 65)):
            d.polygon([(x - 8, y), (x + w / 2, y - 40), (x + w + 8, y)], fill="#8a5a3a", outline=INK, width=4)
            d.rectangle((x, y, x + w, y + h), fill="#e8dcc8", outline=INK, width=4)
        # soft arc around it like a small map boundary, no text
        d.arc((260, 760, 820, 1320), 20, 340, fill=BLU, width=10)
        d.arc((290, 790, 790, 1290), 30, 330, fill="#8ab4d8", width=6)
    return scene(draw, (50, 90, 130), (120, 150, 180))


def two_girls_phone():
    def draw(d):
        room(d, 0)
        figure(d, 350, 1740, 3.2, "girl", "calm", "down")
        figure(d, 700, 1740, 3.2, "girl2", "calm", "phone")
    return scene(draw, (30, 30, 60), (80, 80, 120))


def stranger_lure_mountain():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        # far mountain
        d.polygon([(560, 560), (760, 340), (980, 560)], fill="#8a9ab0", outline=INK, width=6)
        shadow(d, 260, 1680, 3.0)
        # arm pointing to mountain
        figure(d, 820, 1740, 2.4, "girl", "worried", "down")
    return scene(draw, (40, 50, 80), (90, 100, 140))


def salary_bills():
    def draw(d):
        room(d, 1)
        figure(d, 260, 1740, 3.2, "girl", "happy", "down")
        x0, y0, x1, y1 = 520, 420, 1000, 1380
        screen(d, x0, y0, x1, y1, GRN)
        zoom(d, (340, 1200), (390, 1180), x0, y0 + 500)
        for i in range(4):
            bill(d, x0 + 70, y0 + 520 - i * 55, 300, 100)
    return scene(draw, (30, 40, 50), (80, 100, 110))


def tip_coins():
    def draw(d):
        room(d, 2)
        figure(d, 540, 1740, 3.4, "girl", "happy", "down")
        # coins falling into open hand area
        for i, (cx, cy) in enumerate(((420, 1180), (520, 1120), (620, 1180), (560, 1240), (480, 1280))):
            coin(d, cx, cy, 34)
    return scene(draw, (40, 40, 60), (90, 90, 120))


# ================= Đoạn 2 =================
def two_girls_young():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 380, 1700, 3.2, "girl", "calm", "down")
        figure(d, 700, 1700, 3.2, "girl2", "calm", "down")
    return scene(draw, (40, 40, 70), (90, 90, 130))


def never_far():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        # road leading away
        d.polygon([(460, 1560), (620, 1560), (580, 900), (500, 900)], fill="#b8bcc4", outline=INK, width=5)
        figure(d, 360, 1700, 3.0, "girl", "worried", "down")
        figure(d, 660, 1700, 3.0, "girl2", "worried", "down")
        # hands holding backpack straps implied by small bags
        for x in (310, 610):
            d.rectangle((x, 1540, x + 85, 1635), fill=BLU, outline=INK, width=6)
    return scene(draw, (50, 60, 90), (110, 120, 150))


def easy_job_promise():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        shadow(d, 540, 1700, 3.3)
        # open palms gesture
    return scene(draw, (30, 30, 60), (80, 80, 120))


def no_degree():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        shadow(d, 360, 1700, 3.0)
        # paper pushed away, falling
        d.rectangle((680, 980, 900, 1160), fill="#f4f4ee", outline=INK, width=6)
        d.line([(720, 1020), (860, 1020)], fill="#c8ccd4", width=8)
        d.line([(720, 1070), (830, 1070)], fill="#c8ccd4", width=8)
    return scene(draw, (30, 30, 60), (80, 80, 120))


def just_get_in_car():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        # car with open door, step
        d.rectangle((420, 1180, 980, 1500), fill="#5a6a84", outline=INK, width=8)
        d.rectangle((460, 1220, 640, 1340), fill="#cfe8f4", outline=INK, width=6)
        d.rectangle((680, 1220, 860, 1340), fill="#cfe8f4", outline=INK, width=6)
        d.ellipse((500, 1470, 580, 1550), fill="#2a2a2a", outline=INK, width=6)
        d.ellipse((820, 1470, 900, 1550), fill="#2a2a2a", outline=INK, width=6)
        # open door
        d.polygon([(420, 1200), (280, 1260), (280, 1500), (420, 1500)], fill="#4a5a74", outline=INK, width=7)
        d.rectangle((300, 1500, 420, 1540), fill="#8a8e9a", outline=INK, width=5)
    return scene(draw, (40, 50, 80), (90, 100, 140))


def picked_up_there():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        # car with scammer pointing to seat
        d.rectangle((420, 1180, 980, 1500), fill="#5a6a84", outline=INK, width=8)
        d.rectangle((460, 1220, 640, 1340), fill="#cfe8f4", outline=INK, width=6)
        d.rectangle((680, 1220, 860, 1340), fill="#cfe8f4", outline=INK, width=6)
        d.ellipse((500, 1470, 580, 1550), fill="#2a2a2a", outline=INK, width=6)
        d.ellipse((820, 1470, 900, 1550), fill="#2a2a2a", outline=INK, width=6)
        shadow(d, 250, 1700, 2.8)
    return scene(draw, (40, 50, 80), (90, 100, 140))


def family_unaware():
    def draw(d):
        # dark room
        floor(d, 1560, "#6a7484", "#5a6474")
        # window no silhouette
        d.rectangle((680, 360, 960, 700), fill="#3a4454", outline=INK, width=8)
        d.line([(820, 360), (820, 700)], fill=INK, width=6)
        d.line([(680, 530), (960, 530)], fill=INK, width=6)
        # phone buzzing on table
        d.rectangle((220, 1320, 520, 1420), fill="#8a6a3a", outline=INK, width=6)
        d.rectangle((320, 1220, 420, 1360), fill="#8fe0f4", outline=INK, width=6)
        # vibration lines
        for x in (290, 450):
            d.line([(x, 1200), (x - 20, 1170)], fill=GOLD, width=6)
            d.line([(x, 1240), (x - 20, 1210)], fill=GOLD, width=6)
    return night_scene(draw)


# ================= Đoạn 3 =================
def build_trust():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        shadow(d, 540, 1700, 3.3)
        # hands clasped at chest
        d.rectangle((460, 1220, 620, 1320), fill="#2d2848", outline=INK, width=6)
    return scene(draw, (30, 30, 60), (80, 80, 120))


def car_booked():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        shadow(d, 280, 1700, 2.8)
        # small car on palm
        d.rectangle((500, 1100, 700, 1200), fill="#5a6a84", outline=INK, width=6)
        d.rectangle((520, 1120, 580, 1160), fill="#cfe8f4", outline=INK, width=4)
        d.rectangle((620, 1120, 680, 1160), fill="#cfe8f4", outline=INK, width=4)
        d.ellipse((530, 1190, 560, 1220), fill="#2a2a2a", outline=INK, width=4)
        d.ellipse((640, 1190, 670, 1220), fill="#2a2a2a", outline=INK, width=4)
    return scene(draw, (30, 40, 70), (80, 90, 130))


def car_arrives():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        # gate
        d.rectangle((120, 980, 160, 1560), fill="#8a6a3a", outline=INK, width=6)
        d.rectangle((320, 980, 360, 1560), fill="#8a6a3a", outline=INK, width=6)
        d.rectangle((120, 980, 360, 1020), fill="#8a6a3a", outline=INK, width=6)
        # car with headlights
        d.rectangle((520, 1220, 980, 1500), fill="#5a6a84", outline=INK, width=8)
        d.rectangle((540, 1260, 640, 1360), fill="#fff3b8", outline=INK, width=5)
        d.rectangle((860, 1260, 960, 1360), fill="#fff3b8", outline=INK, width=5)
        d.ellipse((600, 1470, 680, 1550), fill="#2a2a2a", outline=INK, width=6)
        d.ellipse((820, 1470, 900, 1550), fill="#2a2a2a", outline=INK, width=6)
    return scene(draw, (40, 50, 80), (90, 100, 140))


def girls_excited():
    def draw(d):
        room(d, 1)
        figure(d, 360, 1740, 3.2, "girl", "happy", "down")
        figure(d, 700, 1740, 3.2, "girl2", "happy", "down")
        bubble(d, 620, 680, 980, 840, "#f4f4ee", ((760, 840), (740, 920), (820, 840)))
    return scene(draw, (40, 40, 70), (90, 90, 130))


def get_in_car():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        d.rectangle((520, 1180, 1020, 1500), fill="#5a6a84", outline=INK, width=8)
        d.rectangle((560, 1220, 740, 1340), fill="#cfe8f4", outline=INK, width=6)
        d.rectangle((780, 1220, 960, 1340), fill="#cfe8f4", outline=INK, width=6)
        d.ellipse((600, 1470, 680, 1550), fill="#2a2a2a", outline=INK, width=6)
        d.ellipse((860, 1470, 940, 1550), fill="#2a2a2a", outline=INK, width=6)
        d.polygon([(520, 1200), (380, 1260), (380, 1500), (520, 1500)], fill="#4a5a74", outline=INK, width=7)
        figure(d, 280, 1700, 2.8, "girl", "calm", "down")
        figure(d, 170, 1700, 2.6, "girl2", "calm", "down")
    return scene(draw, (40, 50, 80), (90, 100, 140))


def night_departure():
    def draw(d):
        d.rectangle((0, 1560, W, H), fill="#3a4250")
        # moon
        d.ellipse((820, 180, 940, 300), fill="#f4f0c8", outline=INK, width=5)
        # road curve
        d.polygon([(0, 1560), (1080, 1560), (760, 1200), (560, 1200)], fill="#4a5260", outline=INK, width=5)
        # car
        d.rectangle((430, 1280, 760, 1460), fill="#5a6a84", outline=INK, width=7)
        d.rectangle((460, 1310, 560, 1380), fill="#fff3b8", outline=INK, width=4)
        d.rectangle((630, 1310, 730, 1380), fill="#fff3b8", outline=INK, width=4)
        d.ellipse((500, 1440, 560, 1500), fill="#2a2a2a", outline=INK, width=5)
        d.ellipse((630, 1440, 690, 1500), fill="#2a2a2a", outline=INK, width=5)
        # street lights
        for x in (120, 320):
            d.line([(x, 1560), (x, 1100)], fill="#8a8e9a", width=8)
            d.ellipse((x - 20, 1080, x + 20, 1120), fill="#ffe8a0", outline=INK, width=4)
    return night_scene(draw)


# ================= Đoạn 4 =================
def leaving_danang():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        for x, y in ((120, 1280), (260, 1320)):
            d.polygon([(x - 8, y), (x + 45, y - 35), (x + 98, y)], fill="#8a5a3a", outline=INK, width=4)
            d.rectangle((x, y, x + 90, y + 70), fill="#e8dcc8", outline=INK, width=4)
        d.rectangle((620, 1300, 940, 1470), fill="#5a6a84", outline=INK, width=7)
        d.ellipse((690, 1450, 750, 1510), fill="#2a2a2a", outline=INK, width=5)
        d.ellipse((810, 1450, 870, 1510), fill="#2a2a2a", outline=INK, width=5)
        d.line([(560, 1420), (360, 1440), (200, 1460)], fill="#c8ccd4", width=10)
    return scene(draw, (50, 70, 100), (110, 130, 160))


def toward_bac_kan():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        d.polygon([(440, 1560), (640, 1560), (590, 900), (490, 900)], fill="#b8bcc4", outline=INK, width=5)
        d.polygon([(820, 420), (980, 280), (1040, 420)], fill="#8a9ab0", outline=INK, width=6)
        d.line([(760, 740), (920, 560)], fill="#8a9ab0", width=12)
        d.polygon([(920, 560), (890, 590), (940, 590)], fill="#8a9ab0", outline=INK)
    return scene(draw, (50, 70, 110), (110, 130, 170))


def quang_tri_marker():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        d.rectangle((380, 980, 420, 1560), fill="#8a8e9a", outline=INK, width=6)
        d.rectangle((660, 980, 700, 1560), fill="#8a8e9a", outline=INK, width=6)
        d.rectangle((340, 980, 460, 1040), fill="#f4f4ee", outline=INK, width=6)
        d.rectangle((620, 980, 740, 1040), fill="#f4f4ee", outline=INK, width=6)
        d.polygon([(460, 1560), (620, 1560), (600, 1040), (480, 1040)], fill="#b8bcc4", outline=INK, width=5)
    return scene(draw, (50, 70, 110), (110, 130, 170))


def police_stop():
    def draw(d):
        floor(d, 1560, "#6a7484", "#5a6474")
        d.rectangle((360, 1240, 860, 1480), fill="#5a6a84", outline=INK, width=7)
        d.rectangle((400, 1275, 520, 1360), fill="#cfe8f4", outline=INK, width=5)
        d.rectangle((700, 1275, 820, 1360), fill="#cfe8f4", outline=INK, width=5)
        d.ellipse((450, 1460, 520, 1530), fill="#2a2a2a", outline=INK, width=5)
        d.ellipse((700, 1460, 770, 1530), fill="#2a2a2a", outline=INK, width=5)
        figure(d, 220, 1700, 3.0, "officer", "stern", "down")
        ink_figure(InkD(d), 500, 1410, 0.9, "girl2", "worried")
        ink_figure(InkD(d), 620, 1410, 0.9, "girl2", "worried")
    return night_scene(draw)


def night_dark():
    def draw(d):
        floor(d, 1560, "#6a7484", "#5a6474")
        d.ellipse((820, 220, 920, 320), fill="#f4f0c8", outline=INK, width=5)
        d.rectangle((360, 1280, 820, 1480), fill="#5a6a84", outline=INK, width=7)
        d.ellipse((450, 1460, 520, 1530), fill="#2a2a2a", outline=INK, width=5)
        d.ellipse((660, 1460, 730, 1530), fill="#2a2a2a", outline=INK, width=5)
    return night_scene(draw)


# ================= Đoạn 5 =================
def officer_approach():
    def draw(d):
        floor(d, 1560, "#6a7484", "#5a6474")
        d.rectangle((460, 1240, 940, 1480), fill="#5a6a84", outline=INK, width=7)
        d.rectangle((500, 1275, 620, 1360), fill="#cfe8f4", outline=INK, width=5)
        d.ellipse((550, 1460, 620, 1530), fill="#2a2a2a", outline=INK, width=5)
        d.ellipse((780, 1460, 850, 1530), fill="#2a2a2a", outline=INK, width=5)
        figure(d, 260, 1700, 3.0, "officer", "calm", "down")
    return night_scene(draw)


def escort_night():
    def draw(d):
        floor(d, 1560, "#6a7484", "#5a6474")
        d.ellipse((820, 220, 920, 320), fill="#f4f0c8", outline=INK, width=5)
        figure(d, 280, 1720, 2.8, "girl", "worried", "down")
        figure(d, 470, 1720, 2.8, "girl2", "worried", "down")
        figure(d, 740, 1720, 3.0, "officer", "calm", "down")
        d.polygon([(240, 1720), (320, 1720), (420, 1840), (300, 1840)], fill="#2f3744")
        d.polygon([(430, 1720), (510, 1720), (610, 1840), (490, 1840)], fill="#2f3744")
    return night_scene(draw)


def handover_family():
    def draw(d):
        floor(d, 1560, "#6a7888", "#5a6878")
        figure(d, 220, 1720, 3.0, "officer", "calm", "down")
        figure(d, 500, 1720, 2.6, "girl", "calm", "down")
        figure(d, 640, 1720, 2.6, "girl2", "calm", "down")
        figure(d, 900, 1720, 3.0, "girl2", "calm", "down")
    return night_scene(draw)


def safe_together():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 420, 1720, 3.2, "girl", "happy", "down")
        figure(d, 660, 1720, 3.2, "girl2", "happy", "down")
    return scene(draw, (40, 60, 80), (100, 130, 150))


def trip_stopped():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        d.ellipse((320, 1280, 560, 1520), fill="#e8e8e8", outline=INK, width=10)
        d.ellipse((380, 1340, 500, 1460), fill="#8a8e9a", outline=INK, width=8)
        d.line([(360, 1320), (520, 1480)], fill=RED_, width=14)
        d.rectangle((640, 1280, 1020, 1340), fill=RED_, outline=INK, width=6)
        d.rectangle((700, 1340, 740, 1560), fill="#8a8e9a", outline=INK, width=6)
        d.rectangle((920, 1340, 960, 1560), fill="#8a8e9a", outline=INK, width=6)
    return scene(draw, (40, 50, 80), (90, 110, 140))


# ================= Đoạn 6 =================
def officer_warning_lure():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 220, 1720, 3.0, "officer", "stern", "point")
        shadow(d, 760, 1720, 2.8)
        figure(d, 520, 1740, 2.4, "girl", "worried", "down")
    return scene(draw, (30, 40, 60), (80, 90, 120))


def forced_labor():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 760, 1720, 2.8, "girl", "worried", "down")
        # broom
        d.line([(700, 1200), (760, 1560)], fill="#8a6a3a", width=12)
        d.rectangle((660, 1500, 800, 1560), fill="#c8a45a", outline=INK, width=5)
        # coin stack bubble above scammer area
        bubble(d, 160, 520, 520, 760, "#f4f4ee", ((420, 760), (460, 860), (480, 760)))
        for i in range(4):
            coin(d, 280 + i * 50, 680 - i * 8, 28)
        shadow(d, 320, 1720, 2.4)
    return scene(draw, (30, 40, 60), (80, 90, 120))


def coercion():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        shadow(d, 360, 1720, 3.0)
        figure(d, 720, 1720, 3.0, "girl", "shock", "down")
    return scene(draw, (35, 30, 50), (90, 80, 110))


def trafficking():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        shadow(d, 360, 1720, 3.0)
        # two hands out, rope between
        d.line([(240, 1260), (480, 1260)], fill="#8a6a3a", width=12)
        figure(d, 760, 1720, 3.0, "girl", "worried", "down")
        # face turned away implied by pose; keep simple
    return scene(draw, (35, 30, 50), (90, 80, 110))


# ================= Đoạn 7 =================
def old_phones():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        for i, (x, y, w, h) in enumerate(((340, 1100, 180, 320), (420, 980, 190, 330), (500, 860, 200, 340))):
            d.rectangle((x, y, x + w, y + h), fill="#dfe4ee", outline=INK, width=6)
            d.rectangle((x + 14, y + 30, x + w - 14, y + h - 40), fill="#f4f4ee", outline=INK, width=4)
    return scene(draw, (30, 30, 50), (80, 80, 110))


def police_many_places():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 200, 1500, 2.2, "officer", "stern", "down")
        figure(d, 540, 1300, 2.2, "officer", "stern", "down")
        figure(d, 880, 1500, 2.2, "officer", "stern", "down")
        for x, y in ((200, 1080), (540, 880), (880, 1080)):
            d.line([(x, y), (x, y - 120)], fill=INK, width=12)
    return scene(draw, (30, 40, 60), (80, 90, 120))


def msg_facebook():
    def draw(d):
        room(d, 0)
        x0, y0, x1, y1 = 300, 420, 780, 1450
        screen(d, x0, y0, x1, y1, BLU)
        bubble(d, x0 + 40, y0 + 260, x1 - 80, y0 + 420, "#dfe4ee")
        bubble(d, x0 + 120, y0 + 500, x1 - 40, y0 + 660, "#cfe0ff")
    return scene(draw, (30, 40, 70), (80, 100, 140))


def msg_tiktok():
    def draw(d):
        room(d, 1)
        x0, y0, x1, y1 = 300, 420, 780, 1450
        screen(d, x0, y0, x1, y1, "#3a3a44")
        bubble(d, x0 + 40, y0 + 260, x1 - 80, y0 + 420, "#dfe4ee")
        bubble(d, x0 + 120, y0 + 500, x1 - 40, y0 + 660, "#f4d0e0")
        d.polygon([(x0 + 60, y0 + 420), (x0 + 30, y0 + 460), (x0 + 95, y0 + 420)], fill="#dfe4ee", outline="#8a8e9a")
    return scene(draw, (30, 30, 60), (80, 80, 120))


def msg_zalo():
    def draw(d):
        room(d, 2)
        x0, y0, x1, y1 = 300, 420, 780, 1450
        screen(d, x0, y0, x1, y1, "#4a8ad8")
        bubble(d, x0 + 40, y0 + 260, x1 - 80, y0 + 420, "#dfe4ee")
        bubble(d, x0 + 120, y0 + 500, x1 - 40, y0 + 660, "#d8ecff")
        d.ellipse((x0 + 48, y0 + 410, x0 + 78, y0 + 440), fill="#dfe4ee", outline="#8a8e9a")
    return scene(draw, (30, 50, 80), (80, 110, 150))


def target_young():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        shadow(d, 360, 1700, 2.8)
        figure(d, 740, 1700, 2.8, "girl", "worried", "down")
        # small backpack
        d.rectangle((690, 1540, 770, 1630), fill=BLU, outline=INK, width=6)
    return scene(draw, (30, 40, 60), (80, 90, 120))


def need_job():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 540, 1720, 3.2, "girl", "worried", "down")
        # folded paper in hand
        d.rectangle((620, 1320, 720, 1420), fill="#f4f4ee", outline=INK, width=6)
        d.line([(670, 1320), (670, 1420)], fill="#c8ccd4", width=4)
    return scene(draw, (30, 40, 60), (80, 90, 120))


def need_money():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 540, 1720, 3.2, "girl", "worried", "down")
        # empty wallet
        d.rectangle((620, 1340, 760, 1440), fill="#8a5a3a", outline=INK, width=6)
        d.rectangle((640, 1360, 740, 1420), fill="#c8a45a", outline=INK, width=4)
    return scene(draw, (30, 40, 60), (80, 90, 120))


# ================= Đoạn 8 =================
def high_salary_sign():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 780, 1720, 3.0, "girl", "shock", "down")
        for i in range(5):
            coin(d, 260 + i * 60, 1320 - i * 20, 40)
        coin(d, 300, 1420, 36)
        coin(d, 420, 1440, 32)
    return scene(draw, (30, 40, 60), (80, 90, 120))


def no_degree_check():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        shadow(d, 320, 1720, 2.8)
        d.rectangle((700, 980, 920, 1200), fill="#f4f4ee", outline=INK, width=6)
        d.line([(740, 1040), (880, 1040)], fill="#c8ccd4", width=8)
        # pushed out of frame
        d.rectangle((940, 1040, 1040, 1220), fill="#f4f4ee", outline=INK, width=6)
    return scene(draw, (30, 40, 60), (80, 90, 120))


def no_experience_check():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        shadow(d, 360, 1720, 2.8)
        d.rectangle((640, 1120, 840, 1320), fill="#f4f4ee", outline=INK, width=6)
        d.line([(680, 1180), (800, 1180)], fill="#c8ccd4", width=8)
        d.rectangle((700, 1380, 860, 1540), fill="#f4f4ee", outline=INK, width=6)
    return scene(draw, (30, 40, 60), (80, 90, 120))


def but_book_car():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        shadow(d, 300, 1720, 2.8)
        # table and small car
        d.rectangle((460, 1320, 920, 1400), fill="#8a6a3a", outline=INK, width=6)
        d.rectangle((560, 1200, 760, 1300), fill="#5a6a84", outline=INK, width=6)
        d.rectangle((580, 1220, 640, 1260), fill="#cfe8f4", outline=INK, width=4)
        d.rectangle((680, 1220, 740, 1260), fill="#cfe8f4", outline=INK, width=4)
        d.ellipse((590, 1290, 620, 1320), fill="#2a2a2a", outline=INK, width=4)
        d.ellipse((700, 1290, 730, 1320), fill="#2a2a2a", outline=INK, width=4)
    return scene(draw, (30, 40, 60), (80, 90, 120))


def rush_now():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        shadow(d, 360, 1720, 3.0)
        # clock face no numbers
        d.ellipse((680, 520, 980, 820), fill="#f4f4ee", outline=INK, width=8)
        d.line([(830, 670), (830, 560)], fill=INK, width=10)
        d.line([(830, 670), (910, 720)], fill=RED_, width=8)
    return scene(draw, (35, 30, 50), (90, 80, 110))


def more_urgent():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        shadow(d, 540, 1720, 3.2)
        # leaning forward, waving hands (two hand lines)
        d.line([(420, 1240), (320, 1160)], fill="#8a8e9a", width=10)
        d.line([(660, 1240), (760, 1160)], fill="#8a8e9a", width=10)
    return scene(draw, (35, 30, 50), (90, 80, 110))


def must_stop():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 540, 1720, 3.4, "girl", "stern", "stop")
        # phone in other hand
        d.rectangle((660, 1320, 720, 1420), fill="#8fe0f4", outline=INK, width=5)
    return scene(draw, (30, 50, 70), (80, 110, 140))


# ================= Đoạn 9 =================
def police_advice():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 300, 1720, 3.2, "officer", "stern", "point")
        # blank board
        d.rectangle((560, 520, 980, 1100), fill="#f4f4ee", outline=INK, width=8)
        d.rectangle((560, 520, 980, 600), fill=BLU, outline=INK, width=8)
    return scene(draw, (30, 40, 70), (80, 100, 140))


def before_far_work():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        # doorway
        d.rectangle((200, 700, 520, 1560), fill="#e8dcc8", outline=INK, width=8)
        d.rectangle((240, 740, 480, 1560), fill="#c8d4e0", outline=INK, width=6)
        figure(d, 360, 1700, 2.8, "girl", "calm", "down")
        # bag
        d.rectangle((430, 1460, 500, 1560), fill=BLU, outline=INK, width=5)
    return scene(draw, (40, 50, 80), (90, 110, 140))


def check_with_family():
    def draw(d):
        room(d, 0)
        figure(d, 320, 1720, 3.0, "girl", "calm", "phone")
        figure(d, 760, 1720, 3.0, "girl2", "calm", "down")
    return scene(draw, (30, 40, 70), (80, 100, 140))


def dont_follow_stranger():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 360, 1720, 3.2, "girl", "stern", "stop")
        shadow(d, 760, 1720, 3.0)
    return scene(draw, (30, 40, 60), (80, 90, 120))


def dont_take_gifts():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 320, 1720, 3.2, "girl", "stern", "stop")
        # gift box and coins pushed back
        d.rectangle((620, 1320, 760, 1460), fill=PINK, outline=INK, width=6)
        d.line([(690, 1320), (690, 1460)], fill=GOLD, width=6)
        coin(d, 820, 1400, 30)
        coin(d, 860, 1440, 28)
    return scene(draw, (30, 40, 60), (80, 90, 120))


def pack_secretly():
    def draw(d):
        floor(d, 1560, "#6a7888", "#5a6878")
        figure(d, 540, 1720, 3.0, "girl", "worried", "down")
        # bag on floor, hand over mouth area suggested
        d.rectangle((640, 1480, 780, 1600), fill=BLU, outline=INK, width=6)
    return night_scene(draw)


def call_police():
    def draw(d):
        room(d, 2)
        figure(d, 360, 1720, 3.0, "girl", "calm", "phone")
        figure(d, 760, 1720, 3.0, "officer", "calm", "down")
    return scene(draw, (30, 50, 80), (80, 110, 150))


# ================= Đoạn 10 =================
def stopped_in_time():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        # officer hand blocking wheel
        figure(d, 260, 1720, 3.0, "officer", "stern", "stop")
        d.ellipse((520, 1340, 760, 1580), fill="#e8e8e8", outline=INK, width=10)
        d.ellipse((580, 1400, 700, 1520), fill="#8a8e9a", outline=INK, width=8)
        # two girls on step
        figure(d, 860, 1680, 2.2, "girl", "calm", "down")
        figure(d, 960, 1680, 2.2, "girl2", "calm", "down")
    return scene(draw, (40, 50, 80), (90, 110, 150))


def one_thing():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        figure(d, 320, 1720, 3.2, "officer", "calm", "point")
        figure(d, 680, 1720, 2.6, "girl", "calm", "down")
        figure(d, 860, 1720, 2.6, "girl2", "calm", "down")
    return scene(draw, (30, 40, 70), (80, 100, 140))


def no_night_ride():
    def draw(d):
        floor(d, 1560, "#6a7484", "#5a6474")
        d.ellipse((820, 220, 920, 320), fill="#f4f0c8", outline=INK, width=5)
        # car with open door
        d.rectangle((520, 1240, 980, 1480), fill="#5a6a84", outline=INK, width=7)
        d.polygon([(520, 1260), (400, 1310), (400, 1480), (520, 1480)], fill="#4a5a74", outline=INK, width=6)
        d.ellipse((600, 1460, 670, 1530), fill="#2a2a2a", outline=INK, width=5)
        d.ellipse((820, 1460, 890, 1530), fill="#2a2a2a", outline=INK, width=5)
        figure(d, 260, 1720, 3.0, "girl", "stern", "stop")
    return night_scene(draw)


def call_family_safe():
    def draw(d):
        room(d, 0)
        figure(d, 360, 1720, 3.0, "girl", "calm", "ear")
        # guardian silhouette at door behind
        d.rectangle((760, 760, 980, 1560), fill="#d9cdb8", outline=INK, width=6)
        d.rectangle((800, 800, 940, 1520), fill="#b8c8d8", outline=INK, width=5)
        figure(d, 870, 1680, 2.6, "girl2", "calm", "down")
    return scene(draw, (40, 50, 80), (100, 120, 150))


def road_blocked():
    def draw(d):
        floor(d, 1560, "#d9cdb8", "#c9bba4")
        # long road fading
        d.polygon([(420, 1560), (660, 1560), (580, 700), (500, 700)], fill="#b8bcc4", outline=INK, width=5)
        # barrier before feet
        d.rectangle((360, 1360, 720, 1410), fill=RED_, outline=INK, width=6)
        d.rectangle((420, 1410, 450, 1560), fill="#8a8e9a", outline=INK, width=5)
        d.rectangle((630, 1410, 660, 1560), fill="#8a8e9a", outline=INK, width=5)
        figure(d, 540, 1700, 2.8, "girl", "calm", "down")
    return scene(draw, (40, 50, 80), (100, 120, 150))


REG = {
    "s9_calendar": calendar,
    "s9_hills_village": hills_village,
    "s9_danang_map": danang_map,
    "s9_two_girls_phone": two_girls_phone,
    "s9_stranger_lure_mountain": stranger_lure_mountain,
    "s9_salary_bills": salary_bills,
    "s9_tip_coins": tip_coins,
    "s9_two_girls_young": two_girls_young,
    "s9_never_far": never_far,
    "s9_easy_job_promise": easy_job_promise,
    "s9_no_degree": no_degree,
    "s9_just_get_in_car": just_get_in_car,
    "s9_picked_up_there": picked_up_there,
    "s9_family_unaware": family_unaware,
    "s9_build_trust": build_trust,
    "s9_car_booked": car_booked,
    "s9_car_arrives": car_arrives,
    "s9_girls_excited": girls_excited,
    "s9_get_in_car": get_in_car,
    "s9_night_departure": night_departure,
    "s9_leaving_danang": leaving_danang,
    "s9_toward_bac_kan": toward_bac_kan,
    "s9_quang_tri_marker": quang_tri_marker,
    "s9_police_stop": police_stop,
    "s9_night_dark": night_dark,
    "s9_officer_approach": officer_approach,
    "s9_escort_night": escort_night,
    "s9_handover_family": handover_family,
    "s9_safe_together": safe_together,
    "s9_trip_stopped": trip_stopped,
    "s9_officer_warning_lure": officer_warning_lure,
    "s9_forced_labor": forced_labor,
    "s9_coercion": coercion,
    "s9_trafficking": trafficking,
    "s9_old_phones": old_phones,
    "s9_police_many_places": police_many_places,
    "s9_msg_facebook": msg_facebook,
    "s9_msg_tiktok": msg_tiktok,
    "s9_msg_zalo": msg_zalo,
    "s9_target_young": target_young,
    "s9_need_job": need_job,
    "s9_need_money": need_money,
    "s9_high_salary_sign": high_salary_sign,
    "s9_no_degree_check": no_degree_check,
    "s9_no_experience_check": no_experience_check,
    "s9_but_book_car": but_book_car,
    "s9_rush_now": rush_now,
    "s9_more_urgent": more_urgent,
    "s9_must_stop": must_stop,
    "s9_police_advice": police_advice,
    "s9_before_far_work": before_far_work,
    "s9_check_with_family": check_with_family,
    "s9_dont_follow_stranger": dont_follow_stranger,
    "s9_dont_take_gifts": dont_take_gifts,
    "s9_pack_secretly": pack_secretly,
    "s9_call_police": call_police,
    "s9_stopped_in_time": stopped_in_time,
    "s9_one_thing": one_thing,
    "s9_no_night_ride": no_night_ride,
    "s9_call_family_safe": call_family_safe,
    "s9_road_blocked": road_blocked,
}


# ================= simplified redo: one big clear subject per frame =================
def _van(d, cx, base, s=1.0, lights=False, door=False):
    x0, x1, top = cx - 330 * s, cx + 330 * s, base - 330 * s
    d.polygon([(x0, base - 60 * s), (x0, top + 90 * s), (x0 + 120 * s, top + 90 * s), (x0 + 200 * s, top), (x1, top), (x1, base - 60 * s)], fill="#5a6a84")
    d.polygon([(x0 + 140 * s, top + 100 * s), (x0 + 205 * s, top + 30 * s), (x0 + 300 * s, top + 30 * s), (x0 + 300 * s, top + 100 * s)], fill="#cfe8f4")
    d.rectangle((x0 + 350 * s, top + 50 * s, x1 - 40 * s, top + 130 * s), fill="#cfe8f4")
    if door: d.polygon([(x0 + 330 * s, top + 150 * s), (x1 - 30 * s, top + 150 * s), (x1 - 30 * s, base - 70 * s), (x0 + 330 * s, base - 70 * s)], fill="#2a3446")
    if lights: d.ellipse((x0 - 10 * s, base - 200 * s, x0 + 70 * s, base - 130 * s), fill="#fff3b8")
    for wx in (x0 + 150 * s, x1 - 130 * s): d.ellipse((wx - 70 * s, base - 130 * s, wx + 70 * s, base + 10 * s), fill="#2a2a2a"); d.ellipse((wx - 26 * s, base - 86 * s, wx + 26 * s, base - 34 * s), fill="#c8ccd4")


def _pin(d, cx, cy, s=1.0, col=RED_):
    d.polygon([(cx - 120 * s, cy - 60 * s), (cx + 120 * s, cy - 60 * s), (cx, cy + 190 * s)], fill=col); d.ellipse((cx - 150 * s, cy - 220 * s, cx + 150 * s, cy + 80 * s), fill=col); d.ellipse((cx - 55 * s, cy - 125 * s, cx + 55 * s, cy - 15 * s), fill="#f4f4ee")


def easy_job_promise():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690"); shadow(d, 400, 1740, 3.6)
        d.rectangle((560, 560, 1020, 900), fill="#f4f4ee"); d.polygon([(640, 900), (600, 1010), (730, 900)], fill="#f4f4ee")
        d.line([(650, 730), (740, 820), (930, 640)], fill=GRN, width=40)
    return scene(draw, (230, 200, 130), (240, 220, 160))


def just_get_in_car():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690"); x0, y0, x1, y1 = 250, 330, 830, 1330; screen(d, x0, y0, x1, y1, GRN)
        _van(d, 540, 960, 0.55, door=False); _pin(d, 540, 640, 0.5)
    return scene(draw, (230, 200, 130), (240, 220, 160))


def car_booked():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690"); figure(d, 260, 1740, 3.2, "scammer", "calm", "ear"); _van(d, 760, 1560, 0.78)
    return scene(draw, (230, 200, 130), (240, 220, 160))


def car_arrives():
    def draw(d):
        floor(d, 1560, "#d4d8e0", "#c4c8d0"); _van(d, 540, 1500, 1.4, lights=True)
    return scene(draw, (150, 170, 200), (190, 205, 230))


def quang_tri_marker():
    def draw(d):
        floor(d, 1640, "#3a4a60", "#2c3a50"); _pin(d, 540, 760, 2.0); _van(d, 540, 1520, 0.6)
    return night_scene(draw)


def get_in_car():
    def draw(d):
        floor(d, 1560, "#d4d8e0", "#c4c8d0"); _van(d, 790, 1560, 0.85, door=True)
        figure(d, 170, 1740, 2.6, "girl", "calm", "down"); figure(d, 400, 1760, 2.3, "girl2", "calm", "down")
    return scene(draw, (150, 170, 200), (190, 205, 230))


REG.update({"s9_easy_job_promise": easy_job_promise, "s9_just_get_in_car": just_get_in_car, "s9_car_booked": car_booked, "s9_car_arrives": car_arrives, "s9_quang_tri_marker": quang_tri_marker, "s9_get_in_car": get_in_car})


def trip_stopped():
    def draw(d):
        floor(d, 1560, "#d4d8e0", "#c4c8d0"); _van(d, 700, 1560, 0.85)
        d.polygon([(140, 520), (240, 420), (380, 420), (480, 520), (480, 660), (380, 760), (240, 760), (140, 660)], fill=RED_); d.rectangle((200, 570, 420, 620), fill="#f4f4ee")
        d.rectangle((290, 760, 330, 1560), fill="#c8ccd4")
    return scene(draw, (150, 170, 200), (190, 205, 230))


def forced_labor():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690"); figure(d, 540, 1740, 3.4, "girl", "worried", "down")
        for i, (x, y, w) in enumerate(((330, 1500, 420), (370, 1380, 340), (410, 1260, 260))): d.rectangle((x, y, x + w, y + 120), fill="#c8a45a"); d.line([(x + w / 2, y), (x + w / 2, y + 120)], fill="#8a6a1a", width=10)
    return scene(draw, (230, 200, 130), (240, 220, 160))


def but_book_car():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690"); shadow(d, 260, 1740, 3.2); _van(d, 770, 1560, 0.8)
    return scene(draw, (230, 200, 130), (240, 220, 160))


def stranger_lure_mountain():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690"); shadow(d, 300, 1740, 3.6)
        d.rectangle((520, 480, 1020, 860), fill="#f4f4ee"); d.polygon([(560, 840), (680, 520), (800, 840)], fill="#8a9ab0"); d.polygon([(720, 840), (860, 600), (1000, 840)], fill="#6a7a90"); d.ellipse((900, 520, 980, 600), fill=GOLD)
        d.polygon([(520, 860), (580, 860), (500, 940)], fill="#f4f4ee")
    return scene(draw, (230, 200, 130), (240, 220, 160))


REG.update({"s9_trip_stopped": trip_stopped, "s9_forced_labor": forced_labor, "s9_but_book_car": but_book_car, "s9_stranger_lure_mountain": stranger_lure_mountain})


def _stop(d, cx, cy, r=170):
    pts = [(cx + r * math.cos(math.radians(22.5 + 45 * i)), cy + r * math.sin(math.radians(22.5 + 45 * i))) for i in range(8)]
    d.polygon(pts, fill=RED_); d.rectangle((cx - r * .6, cy - r * .16, cx + r * .6, cy + r * .16), fill="#f4f4ee")


def high_salary_sign():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690")
        for i in range(5): bill(d, 250 + (i % 2) * 40, 1420 - i * 120, 580, 110)
        d.polygon([(540, 520), (700, 800), (380, 800)], fill=RED_); d.rectangle((526, 600, 554, 700), fill="#f4f4ee"); d.ellipse((526, 725, 554, 753), fill="#f4f4ee")
    return scene(draw, (230, 200, 130), (240, 220, 160))


def no_degree_check():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690"); d.rectangle((260, 700, 820, 1060), fill="#f4f4ee"); d.ellipse((430, 800, 650, 1020), fill=RED_); d.rectangle((350, 760, 730, 790), fill="#8a8e9a"); d.rectangle((350, 960, 730, 990), fill="#8a8e9a")
        _cross(d, 540, 880, 330, 60)
    return scene(draw, (230, 200, 130), (240, 220, 160))


def trafficking():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690"); shadow(d, 250, 1740, 3.2); figure(d, 800, 1740, 3.0, "girl", "worried", "down")
        for i in range(3): bill(d, 360, 1180 + i * 100, 360, 90)
    return scene(draw, (230, 200, 130), (240, 220, 160))


def target_young():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690")
        for r, c in ((420, RED_), (300, "#f4f4ee"), (180, RED_), (70, "#f4f4ee")): d.ellipse((540 - r, 960 - r, 540 + r, 960 + r), fill=c)
        figure(d, 540, 1740, 3.2, "girl", "worried", "down")
    return scene(draw, (230, 200, 130), (240, 220, 160))


def must_stop():
    def draw(d):
        floor(d, 1560, "#d4d8e0", "#c4c8d0"); figure(d, 300, 1740, 3.4, "girl", "calm", "down"); _stop(d, 770, 860, 230); d.rectangle((755, 1090, 785, 1560), fill="#c8ccd4")
    return scene(draw, (150, 170, 200), (190, 205, 230))


def no_night_ride():
    def draw(d):
        floor(d, 1640, "#3a4a60", "#2c3a50"); _van(d, 540, 1500, 1.2, lights=True); _cross(d, 540, 1100, 300, 70)
        d.ellipse((800, 300, 960, 460), fill="#fff3b8")
    return night_scene(draw)


def dont_follow_stranger():
    def draw(d):
        floor(d, 1560, "#d4d8e0", "#c4c8d0"); figure(d, 250, 1740, 3.0, "girl", "calm", "down"); shadow(d, 800, 1740, 3.0); _cross(d, 800, 1050, 200, 50)
    return scene(draw, (150, 170, 200), (190, 205, 230))


REG.update({"s9_high_salary_sign": high_salary_sign, "s9_no_degree_check": no_degree_check, "s9_trafficking": trafficking, "s9_target_young": target_young, "s9_must_stop": must_stop, "s9_no_night_ride": no_night_ride, "s9_dont_follow_stranger": dont_follow_stranger})


def leaving_danang():
    def draw(d):
        floor(d, 1560, "#d4d8e0", "#c4c8d0"); _van(d, 620, 1560, 1.1)
        for x in (120, 280): d.polygon([(x - 10, 1300), (x + 60, 1230), (x + 130, 1300)], fill="#8a5a3a"); d.rectangle((x, 1300, x + 120, 1420), fill="#e8dcc8")
    return scene(draw, (150, 170, 200), (190, 205, 230))


def call_family_safe():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690"); figure(d, 290, 1740, 3.2, "girl", "calm", "ear"); figure(d, 790, 1740, 3.2, "girl2", "happy", "down")
    return scene(draw, (230, 200, 130), (240, 220, 160))


def stopped_in_time():
    def draw(d):
        floor(d, 1560, "#d4d8e0", "#c4c8d0"); figure(d, 220, 1740, 3.2, "officer", "calm", "down"); figure(d, 600, 1760, 2.6, "girl", "calm", "down"); figure(d, 880, 1760, 2.6, "girl2", "calm", "down")
        d.line([(400, 560), (500, 660), (700, 440)], fill=GRN, width=60)
    return scene(draw, (150, 170, 200), (190, 205, 230))


REG.update({"s9_leaving_danang": leaving_danang, "s9_call_family_safe": call_family_safe, "s9_stopped_in_time": stopped_in_time})


def get_in_car():
    def draw(d):
        floor(d, 1560, "#d4d8e0", "#c4c8d0"); _van(d, 820, 1560, 0.7, door=True)
        figure(d, 200, 1740, 2.4, "girl", "calm", "down"); figure(d, 440, 1760, 2.2, "girl2", "calm", "down")
    return scene(draw, (150, 170, 200), (190, 205, 230))


def handover_family():
    def draw(d):
        floor(d, 1560, "#6a7888", "#5a6878")
        figure(d, 160, 1720, 2.3, "officer", "calm", "down"); figure(d, 400, 1740, 2.0, "girl", "calm", "down"); figure(d, 580, 1740, 2.0, "girl2", "calm", "down"); figure(d, 850, 1720, 2.3, "woman", "happy", "down")
    return night_scene(draw)


def officer_warning_lure():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690"); shadow(d, 260, 1740, 3.0); figure(d, 780, 1740, 3.0, "girl", "worried", "down")
        d.polygon([(540, 460), (700, 760), (380, 760)], fill=RED_); d.rectangle((526, 540, 554, 650), fill="#f4f4ee"); d.ellipse((526, 676, 554, 704), fill="#f4f4ee")
    return scene(draw, (230, 200, 130), (240, 220, 160))


def old_phones():
    def draw(d):
        floor(d, 1560, "#d4d8e0", "#c4c8d0"); figure(d, 540, 1740, 3.4, "officer", "stern", "down")
        d.polygon([(540, 400), (700, 700), (380, 700)], fill=RED_); d.rectangle((526, 480, 554, 590), fill="#f4f4ee"); d.ellipse((526, 616, 554, 644), fill="#f4f4ee")
    return scene(draw, (150, 170, 200), (190, 205, 230))


def msg_facebook():
    def draw(d):
        floor(d, 1560, "#d4d8e0", "#c4c8d0")
        for i, c in enumerate(("#3a6ac8", "#16161a", "#2aa8e0")):
            y = 360 + i * 380; d.rectangle((300, y, 780, y + 320), fill=c); d.rectangle((360, y + 60, 720, y + 210), fill="#f4f4ee"); d.polygon([(400, y + 210), (400, y + 270), (470, y + 210)], fill="#f4f4ee")
    return scene(draw, (150, 170, 200), (190, 205, 230))


def no_degree_check():
    def draw(d):
        floor(d, 1560, "#e6d6a8", "#d8c690")
        d.polygon([(540, 620), (900, 780), (540, 940), (180, 780)], fill="#16161a"); d.rectangle((330, 880, 750, 1040), fill="#2a2a34"); d.line([(860, 800), (860, 1000)], fill=GOLD, width=14); d.ellipse((830, 990, 890, 1050), fill=GOLD)
        _cross(d, 540, 860, 360, 64)
    return scene(draw, (230, 200, 130), (240, 220, 160))


REG.update({"s9_get_in_car": get_in_car, "s9_handover_family": handover_family, "s9_officer_warning_lure": officer_warning_lure, "s9_old_phones": old_phones, "s9_msg_facebook": msg_facebook, "s9_no_degree_check": no_degree_check})
