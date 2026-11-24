"""Studio: local web UI (React) for editing a script and re-rendering only what changed.  Run: python studio.py [script.json]  -> http://localhost:8765"""
import json, os, re, subprocess, sys, threading, time, mimetypes, urllib.parse
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
import engine as E

HERE = E.HERE
PROJ = os.path.join(HERE, "projects"); os.makedirs(PROJ, exist_ok=True)
SCENES = ["tower", "banners", "dragon", "fisher", "banyan", "sword", "victory", "boat", "turtle", "returned", "longquan", "army", "hanoi", "underwater", "coloa", "enemy", "throne", "swordlake", "weak", "camp", "netcatch", "join", "lakeshore", "offer", "dawnlake", "kimquy", "winter", "oldturtle", "crowd", "incense", "suffer", "peace", "forest", "hilt", "storm", "plea", "emblem", "scroll", "nt_coloa_night", "nt_crossbow_fire", "nt_fall", "nt_king_build", "nt_wall_collapse", "nt_kimquy_rise", "nt_claw", "nt_trigger", "nt_north", "nt_defeat", "nt_scheme", "nt_prince_arrive", "nt_wedding", "nt_couple", "nt_show", "nt_swap", "nt_farewell", "nt_feather_road", "nt_invasion", "nt_xbow_fail", "nt_flight", "nt_ride", "nt_chase", "nt_shore", "nt_turtle_sea", "nt_sword_silhouette", "nt_prayer", "nt_sea_part", "nt_search", "nt_well", "nt_pearl", "nt_dig", "nt_arrows", "nt_coloa_today", "nt_gem", "tg_village", "tg_boy_lying", "tg_giant_shadow", "tg_footprint", "tg_mother_foot", "tg_baby", "tg_invasion", "tg_king_worry", "tg_envoy_ride", "tg_envoy_arrive", "tg_boy_speaks", "tg_iron_gear", "tg_eating", "tg_growing", "tg_rice_baskets", "tg_gear_arrive", "tg_stretch", "tg_mount", "tg_horse_fire", "tg_battle", "tg_staff_break", "tg_bamboo", "tg_bamboo_swing", "tg_flee", "tg_soc_mountain", "tg_fly", "tg_king_title", "tg_temple", "tg_bamboo_gold", "tg_statue", "tg_festival", "tg_lanterns", "tg_edict", "tg_heritage", "st_palace", "st_mi_nuong", "st_king_pick", "st_suitors_arrive", "st_son_tinh", "st_thuy_tinh", "st_power", "st_king_dilemma", "st_gift_elephant", "st_gift_rooster", "st_gift_horse", "st_dawn_gifts", "st_wedding", "st_to_mountain", "st_late_arrival", "st_angry", "st_summon", "st_flood_fields", "st_flood_houses", "st_water_mountain", "st_crab_army", "st_son_calm", "st_lift_hill", "st_block_water", "st_hills_rise", "st_clash", "st_tired", "st_retreat", "st_vow", "st_every_year", "st_loses", "st_river_rise", "st_dike", "st_delta", "st_bavi", "st_temple", "st_temple", "ma_court", "ma_home", "ma_family", "ma_boast", "ma_informer", "ma_tell_king", "ma_angry_king", "ma_exile_boat", "ma_island_arrive", "ma_island_empty", "ma_food_low", "ma_resolve", "ma_birds", "ma_seeds", "ma_sowing", "ma_sprout", "ma_vines", "ma_cut", "ma_taste", "ma_harvest", "ma_ship", "ma_trade", "ma_rich_island", "ma_rumor", "ma_gift_king", "ma_king_eat", "ma_king_realize", "ma_royal_boat", "ma_return_home", "ma_seed_give", "ma_fields", "ma_ancestor", "ma_nga_son", "ma_temple", "nv_chip", "nv_press", "nv_chair", "nv_letter", "nv_inquiry", "nv_eye", "nv_source", "nv_calendar", "nv_vote", "nv_gov", "nv_shield", "nv_question", "nv_phone", "nv_trump", "nv_stamp", "nv_plane", "nv_letters", "nv_chip_china", "nv_chart_down", "nv_chart_up", "nv_gears", "nv_huang_back", "nv_december", "nv_boardroom", "nv_deal", "nv_mics", "nv_coins", "nv_scale"]
MOODS = [None, "kich", "huyen", "tram"]
JOB = {"running": False, "label": "", "msg": "", "done": 0, "total": 1, "error": None, "result": None, "t0": 0}
_jl = threading.Lock(); _sl = threading.Lock()


def projects(): return sorted(d for d in os.listdir(PROJ) if os.path.isfile(os.path.join(PROJ, d, "script.json")))


def proj(p):
    ok = projects(); return p if p in ok else (ok[0] if ok else None)


def spath(p): return os.path.join(PROJ, p, "script.json")


def load(p):
    with open(spath(p), encoding="utf8") as f: return json.load(f)


def save(p, sc):
    with _sl:
        with open(spath(p) + ".tmp", "w", encoding="utf8") as f: json.dump(sc, f, ensure_ascii=False, indent=1)
        os.replace(spath(p) + ".tmp", spath(p))


def exports(p):
    """Finals (exports/<p>/, newest first) and the preview (previews/<p>/) kept in separate folders."""
    ls = lambda d, kind: [{"name": os.path.relpath(f, HERE).replace("\\", "/"), "kind": kind, "size": os.path.getsize(f), "mtime": os.path.getmtime(f), "url": url(f)} for f in sorted((os.path.join(d, x) for x in os.listdir(d)), reverse=True) if f.endswith(".mp4")] if os.path.isdir(d) else []
    return ls(os.path.join(E.EXPORTS, p), "final") + ls(os.path.join(E.PREVIEWS, p), "draft")


def own_export(p, name):
    f = os.path.realpath(os.path.join(HERE, name))
    return f if any(f.startswith(os.path.realpath(os.path.join(d, p)) + os.sep) for d in (E.EXPORTS, E.PREVIEWS)) and os.path.isfile(f) else None


def create(name):
    name = re.sub(r"[^\w-]", "_", name.strip().lower())[:40].strip("_")
    if not name or name in projects(): return None
    os.makedirs(os.path.join(PROJ, name)); save(name, {"title": ["TIÊU ĐỀ", "DÒNG HAI"], "hook": "Câu mở đầu?", "cover": "tower", "speed": 1.12, "scenes": [{"scene": "tower", "text": "Viết lời đọc của cảnh đầu tiên ở đây."}]}); return name


def start(label, fn):
    with _jl:
        if JOB["running"]: return False
        JOB.update(running=True, label=label, msg="Bắt đầu", done=0, total=1, error=None, result=None, t0=time.time())

    def cb(m, d=0, t=1): JOB.update(msg=m, done=d, total=max(t, 1))

    def run():
        try: JOB["result"] = fn(cb)
        except Exception as e: JOB["error"] = f"{type(e).__name__}: {e}"
        finally: JOB["running"] = False
    threading.Thread(target=run, daemon=True).start(); return True


def url(p): return "/files/" + os.path.relpath(p, HERE).replace("\\", "/") + f"?v={int(os.path.getmtime(p))}"


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def send(self, code, body, ctype="application/json", extra=None):
        if isinstance(body, (dict, list)): body = json.dumps(body, ensure_ascii=False).encode()
        self.send_response(code); self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(body)))
        for k, v in (extra or {}).items(): self.send_header(k, v)
        self.end_headers(); self.wfile.write(body)

    def file(self, path, dl=False):
        full = os.path.realpath(os.path.join(HERE, path))
        if not full.startswith((os.path.join(HERE, "out"), os.path.join(HERE, "cache"), os.path.join(HERE, "static"), os.path.join(HERE, "exports"), os.path.join(HERE, "previews"))) or not os.path.isfile(full): return self.send(404, b"", "text/plain")
        size = os.path.getsize(full); ct = mimetypes.guess_type(full)[0] or "application/octet-stream"; a, b = 0, size - 1; code = 200; hdr = {"Accept-Ranges": "bytes"}
        if dl: hdr["Content-Disposition"] = f'attachment; filename="{os.path.basename(full)}"'
        rng = self.headers.get("Range")
        if rng and rng.startswith("bytes="):
            s, _, e = rng[6:].partition("-"); a = int(s) if s else 0; b = int(e) if e else size - 1; code = 206; hdr["Content-Range"] = f"bytes {a}-{b}/{size}"
        with open(full, "rb") as f: f.seek(a); data = f.read(b - a + 1)
        try: self.send(code, data, ct, hdr)
        except (ConnectionAbortedError, BrokenPipeError, ConnectionResetError): pass

    def do_GET(self):
        u = urllib.parse.urlparse(self.path); q = {k: v[0] for k, v in urllib.parse.parse_qs(u.query).items()}; p = proj(q.get("p"))
        try:
            if u.path == "/": return self.file("static/studio.html")
            if u.path.startswith("/files/"): return self.file(urllib.parse.unquote(u.path[7:]), "dl" in q)
            if u.path == "/api/script": return self.send(200, {"script": load(p), "scenes": SCENES, "moods": MOODS, "name": p, "projects": projects()})
            if u.path == "/api/state": return self.send(200, {"state": E.status(load(p)), "job": JOB, "videos": {m: url(f) for m in E.MODES if os.path.exists(f := os.path.join(E.PREVIEWS, p, f"{p}_{m}.mp4"))}})
            if u.path == "/api/job": return self.send(200, JOB)
            if u.path == "/api/exports": return self.send(200, {"items": exports(p)})
            if u.path == "/api/still":
                f = E.still(load(p), int(q["k"]), float(q.get("t", 2)), q.get("mode", "draft"))
                return self.send(200, {"url": url(f)} if f else {"url": None})
        except Exception as e: return self.send(500, {"error": f"{type(e).__name__}: {e}"})
        self.send(404, {"error": "not found"})

    def do_POST(self):
        u = urllib.parse.urlparse(self.path); p = proj(urllib.parse.parse_qs(u.query).get("p", [None])[0]); body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        try:
            if u.path == "/api/script": save(p, body); return self.send(200, {"ok": True})
            if u.path == "/api/new": n = create(body.get("name", "")); return self.send(200 if n else 409, {"name": n})
            if u.path in ("/api/export_delete", "/api/export_reveal"):
                f = own_export(p, body.get("name", ""))
                if not f: return self.send(404, {"error": "not found"})
                if u.path.endswith("delete"): os.remove(f)
                else: subprocess.Popen(["explorer", "/select,", f])
                return self.send(200, {"ok": True})
            sc = load(p)
            if u.path == "/api/render":
                mode = body.get("mode", "draft")
                ok = start(f"Dựng bản {'nháp' if mode == 'draft' else 'đầy đủ'}", lambda cb: (lambda r: {"video": url(r[0]), "total": r[1], "mode": mode})(E.render(sc, mode, p, cb)))
                return self.send(200 if ok else 409, {"ok": ok})
            if u.path == "/api/scene":
                k = int(body["k"]); ok = start(f"Xem cảnh {k + 1}", lambda cb: {"video": url(E.preview_scene(sc, k, cb)), "scene": k}); return self.send(200 if ok else 409, {"ok": ok})
            if u.path == "/api/audio":
                k = int(body["k"]); ok = start(f"Nghe cảnh {k + 1}", lambda cb: (lambda r: {"audio": url(r[0]), "scene": k})(E.scene_audio(sc, k, cb))); return self.send(200 if ok else 409, {"ok": ok})
        except Exception as e: return self.send(500, {"error": f"{type(e).__name__}: {e}"})
        self.send(404, {"error": "not found"})


if __name__ == "__main__":
    threading.Thread(target=E.prewarm, daemon=True).start()
    print("Studio: http://localhost:8765"); ThreadingHTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
