# -*- coding: utf-8 -*-
from pathlib import Path
import re

root = Path(r"C:\Users\USER\Documents\Icon_Formulas\site-prototype")

shop = root / "shop.html"
t = shop.read_text(encoding="utf-8")
repl = {
    "assets/products/zinc-front.png": "assets/gen/card-zinc.png",
    "assets/products/iron-front.png": "assets/gen/card-iron.png",
    "assets/products/magtein-front.png": "assets/gen/card-magtein.png",
    "assets/products/mg200-front.png": "assets/gen/card-mg225.png",
    "assets/products/mg225-front.png": "assets/gen/card-mg225.png",
    "assets/products/k2-front.png": "assets/gen/card-k2.png",
}
for a, b in repl.items():
    t = t.replace(a, b)
shop.write_text(t, encoding="utf-8")
print("shop updated")

for slug, scene in [
    ("product-zinc.html", "assets/gen/card-zinc.png"),
    ("product-iron.html", "assets/gen/card-iron.png"),
    ("product-magtein.html", "assets/gen/card-magtein.png"),
    ("product-mg-225.html", "assets/gen/card-mg225.png"),
    ("product-mg-200.html", "assets/gen/card-mg225.png"),
    ("product-k2.html", "assets/gen/card-k2.png"),
]:
    p = root / slug
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        'class="pdp-main">\n            <img id="main-image"',
        'class="pdp-main">\n            <img id="main-image" class="scene"',
        1,
    )
    t = re.sub(
        r'(id="main-image"[^>]*src=")[^"]+(")',
        r"\g<1>" + scene + r"\g<2>",
        t,
        count=1,
    )
    for a, b in repl.items():
        t = t.replace(a, b)
    p.write_text(t, encoding="utf-8")
    print("updated", slug)

print("done")
