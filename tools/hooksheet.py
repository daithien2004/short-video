"""Preview every hook line of every project cover as strips (one column per project). Usage: python tools/hooksheet.py out/x.png proj1 proj2 ..."""
import sys, os, json, urllib.request, io
os.environ["PYTHONUTF8"] = "1"; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import engine as E
from PIL import Image
cols = []
for name in sys.argv[2:]:
    sc = json.load(open(f"projects/{name}/script.json", encoding="utf8")); cover, _ = E.plan(sc, False); lines = E.hook_lines(sc["hook"], hl=sc.get("hl")); strips = []
    for j, (tx, cl, wi) in enumerate(lines):
        t0 = 0.0 if j == 0 else max(cover["words"][min(wi, len(cover["words"]) - 1)][0] - 0.1, 0.0)
        u = json.load(urllib.request.urlopen(f"http://localhost:8765/api/still?p={name}&k=-1&t={t0 + .1:.2f}&mode=draft", timeout=600))["url"].split("?")[0]
        strips.append(Image.open(u.replace("/files/", "")).crop((0, 280, 540, 520)))
    col = Image.new("RGB", (540, 240 * len(strips))); [col.paste(s_, (0, 240 * i)) for i, s_ in enumerate(strips)]; cols.append(col)
H = max(c.height for c in cols); sheet = Image.new("RGB", (540 * len(cols), H), "white")
for i, c in enumerate(cols): sheet.paste(c, (540 * i, 0))
sheet.save(sys.argv[1]); print("ok", [c.height // 240 for c in cols])
