# ICON FORMULAS — Site

Precision clinical wellness e-commerce prototype for [iconformulas.com](https://iconformulas.com).

White editorial layout (clinical / photo-based), cobalt accent, Inter + Cormorant Garamond.

## Structure

```
index.html          Home
shop.html           Collection (6 formulas)
product-*.html      Product pages
css/styles.css      Design tokens (primitive → semantic → component)
design-tokens.json  Token source of truth
assets/gen/         Scene photography (seedream 5 pro edit, real bottle refs)
assets/products/    Product packshots
js/main.js          FAQ accordion, mobile nav, gallery
```

## Formulas

| SKU | Goal | Dose |
|---|---|---|
| Zinc Bisglycinate | Daily essentials | 25 mg |
| Iron Bisglycinate | Energy & recovery | 36 mg |
| Magtein® Magnesium L-Threonate | Brain & focus | 2,000 mg |
| Magnesium Bisglycinate 200 mg | Daily essentials | 200 mg |
| Magnesium Bisglycinate 225 mg | Energy & recovery | 225 mg |
| Vitamin K2 MK-7 | Bones & balance | 120 mcg |

## Preview

Open `index.html` locally, or:

```bash
python -m http.server 8765 --bind 127.0.0.1
```

## Disclaimer

These statements have not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease.
