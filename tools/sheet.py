import sys, os; sys.path.insert(0, "src"); os.environ["PYTHONUTF8"]="1"
import engine as E
from PIL import Image
c = E._ctx(); B = c["B"]; names = sys.argv[2:]; ims = []
for n in names:
    data = c["reg"][n](); im = B.S2.frame({"data": data}, 1.0, 5, c["glow"], c["mist"]).convert("RGB").resize((270, 480)); ims.append(im)
cols = 6; rows = -(-len(ims) // cols); sheet = Image.new("RGB", (270 * cols, 480 * rows), "white")
for i, im in enumerate(ims): sheet.paste(im, (270 * (i % cols), 480 * (i // cols)))
sheet.save(sys.argv[1]); print("ok", len(ims))
