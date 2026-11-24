"""Assign shot cut points from real voice timing. Usage: python tools/autoshots.py <project>
Each scene may carry "seq": [scene names in order]; this sets scene=seq[0] and shots[] so every shot lasts 1..3.5 s."""
import sys, os, json, itertools
os.environ["PYTHONUTF8"] = "1"; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import engine as E
name = sys.argv[1]; path = f"projects/{name}/script.json"; sc = json.load(open(path, encoding="utf8")); cover, us = E.plan(sc, True)
def score(cuts, starts, dur):
    b = [0] + [starts[c] for c in cuts] + [dur]; seg = [y - x for x, y in zip(b, b[1:])]; m = sum(seg) / len(seg)
    return sum(100 * (1 - s) ** 2 if s < 1 else 100 * (s - 3.5) ** 2 if s > 3.5 else 0 for s in seg) + sum((s - m) ** 2 for s in seg)
for s, u in zip(sc["scenes"], us):
    seq = s.get("seq")
    if not seq: continue
    n = len(u["starts"]); k = len(seq) - 1
    if k <= 0: s["shots"] = []; continue
    best = min(itertools.combinations(range(1, n), min(k, n - 1)), key=lambda c: score(c, u["starts"], u["dur"]))
    s["scene"] = seq[0]; s["shots"] = [{"at": c, "scene": q} for c, q in zip(best, seq[1:])]
    b = [0] + [round(u["starts"][c], 1) for c in best] + [round(u["dur"], 1)]; print(seq[0], "phrases", n, "cuts", b)
json.dump(sc, open(path, "w", encoding="utf8"), ensure_ascii=False, indent=1)
