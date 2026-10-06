# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(r"C:\Users\USER\Documents\Icon_Formulas\site-prototype")

products = [
    {
        "slug": "product-zinc.html",
        "tag": "Daily essentials / Formula 01",
        "tag_class": "",
        "title_serif": "Zinc Bisglycinate",
        "subtitle": "",
        "desc": "A highly bioavailable form of zinc for everyday immune, skin, and metabolic support. Chelated bisglycinate for gentle absorption.",
        "stats": [
            ("25 mg", "elemental zinc<br />per serving"),
            ("120", "capsules<br />40 servings"),
            ("1", "capsule daily<br />with food"),
        ],
        "tagline": "A named form. A transparent dose.",
        "why_title": "Why this form?",
        "why_body": "Zinc bisglycinate is a chelated form in which zinc is bound to two glycine molecules — chosen for absorption and gastrointestinal comfort compared with common zinc salts.",
        "glance": [
            ("01 / Form", "Zinc bisglycinate chelate."),
            ("02 / Dose", "25 mg elemental zinc per serving."),
            ("03 / Routine", "1 capsule daily with food."),
        ],
        "facts_title": "Supplement Facts",
        "serving": "Serving Size: 1 Capsule · Servings Per Container: 40",
        "facts_rows": [
            ('Zinc<span class="sub">as zinc bisglycinate chelate</span>', "25 mg<br />227%"),
        ],
        "other": "Other ingredients: Hypromellose (capsule), microcrystalline cellulose, vegetable stearate (plant source), silica.",
        "front": "assets/products/zinc-front.png",
        "facts_img": "assets/products/zinc-facts.png",
        "barcode": "assets/products/zinc-barcode.png",
        "related": [
            ("product-iron.html", "assets/products/iron-front.png", "MINERALS / FORMULA 02", "Iron Bisglycinate", "A well-tolerated form of iron for daily nutritional support."),
            ("product-mg-200.html", "assets/products/mg200-front.png", "MINERALS / FORMULA 04", "Magnesium Bisglycinate 200 mg", "Chelated magnesium for calm and muscle support."),
        ],
    },
    {
        "slug": "product-iron.html",
        "tag": "Energy & recovery / Formula 02",
        "tag_class": "",
        "title_serif": "Iron Bisglycinate",
        "subtitle": "",
        "desc": "A well-tolerated, highly bioavailable form of iron for daily nutritional support — without the harshness of common iron salts.",
        "stats": [
            ("36 mg", "elemental iron<br />per serving"),
            ("120", "capsules<br />120 servings"),
            ("1", "capsule daily<br />as directed"),
        ],
        "tagline": "Gentle iron. Clear milligrams.",
        "why_title": "Why this form?",
        "why_body": "Iron bisglycinate (ferrous bisglycinate chelate) is widely used for its absorption profile and digestive tolerance — a practical daily form when iron intake needs support.",
        "glance": [
            ("01 / Form", "Iron bisglycinate chelate."),
            ("02 / Dose", "36 mg elemental iron per serving."),
            ("03 / Routine", "1 capsule daily."),
        ],
        "facts_title": "Supplement Facts",
        "serving": "Serving Size: 1 Capsule · Servings Per Container: 120",
        "facts_rows": [
            ('Iron<span class="sub">as iron bisglycinate chelate</span>', "36 mg<br />200%"),
        ],
        "other": "Other ingredients: Hypromellose (capsule), microcrystalline cellulose, vegetable stearate (plant source), silica.",
        "front": "assets/products/iron-front.png",
        "facts_img": "assets/products/iron-facts.png",
        "barcode": "assets/products/iron-barcode.png",
        "related": [
            ("product-zinc.html", "assets/products/zinc-front.png", "MINERALS / FORMULA 01", "Zinc Bisglycinate", "A highly absorbable form of zinc for everyday support."),
            ("product-k2.html", "assets/products/k2-front.png", "VITAMINS / FORMULA 05", "Vitamin K2 MK-7", "Menaquinone-7 for calcium utilization and bone balance."),
        ],
    },
    {
        "slug": "product-magtein.html",
        "tag": "Brain & focus / Formula 06",
        "tag_class": "violet",
        "title_serif": "Magtein®",
        "subtitle": "Magnesium L-Threonate",
        "desc": "A focused magnesium form for your daily routine. Patented Magtein® is a distinct, well-researched form of magnesium L-threonate designed for high bioavailability.",
        "stats": [
            ("2,000 mg", "Magtein®<br />per daily serving"),
            ("144 mg", "elemental<br />magnesium"),
            ("90", "capsules<br />30 servings"),
        ],
        "tagline": "A named form. A transparent dose.",
        "why_title": "Why this form?",
        "why_body": "Magtein® is a patented form of magnesium L-threonate — a distinct, well-researched form of magnesium designed for high bioavailability and cognitive support routines.",
        "glance": [
            ("01 / Form", "Magtein® magnesium L-threonate."),
            ("02 / Dose", "2,000 mg Magtein®, providing 144 mg elemental magnesium."),
            ("03 / Routine", "3 capsules daily."),
        ],
        "facts_title": "Supplement Facts",
        "serving": "Serving Size: 3 Capsules · Servings Per Container: 30",
        "facts_rows": [
            ('Magnesium<span class="sub">as magnesium L-threonate from Magtein®</span>', "144 mg<br />34%"),
            ("Magtein® magnesium L-threonate", "2,000 mg<br />†"),
        ],
        "other": "Other ingredients: Hypromellose (capsule), microcrystalline cellulose, vegetable stearate (plant source), silica.",
        "front": "assets/products/magtein-front.png",
        "facts_img": "assets/products/magtein-facts.png",
        "barcode": "assets/products/magtein-barcode.png",
        "related": [
            ("product-zinc.html", "assets/products/zinc-front.png", "MINERALS / FORMULA 01", "Zinc Bisglycinate", "A highly absorbable form of zinc for everyday support."),
            ("product-iron.html", "assets/products/iron-front.png", "MINERALS / FORMULA 02", "Iron Bisglycinate", "A well-tolerated form of iron for daily nutritional support."),
        ],
    },
    {
        "slug": "product-mg-200.html",
        "tag": "Daily essentials / Formula 03",
        "tag_class": "",
        "title_serif": "Magnesium Bisglycinate",
        "subtitle": "200 mg",
        "desc": "Chelated magnesium bisglycinate for calm, muscle function, and everyday mineral support — at a clear 200 mg dose.",
        "stats": [
            ("200 mg", "magnesium<br />per serving"),
            ("120", "capsules<br />servings vary"),
            ("2", "capsules daily<br />typical routine"),
        ],
        "tagline": "Chelated magnesium. Honest milligrams.",
        "why_title": "Why this form?",
        "why_body": "Magnesium bisglycinate is magnesium bound to glycine — a chelated form selected for absorption and gentleness compared with oxide forms.",
        "glance": [
            ("01 / Form", "Magnesium bisglycinate chelate."),
            ("02 / Dose", "200 mg magnesium per serving."),
            ("03 / Routine", "2 capsules daily, or as directed."),
        ],
        "facts_title": "Supplement Facts",
        "serving": "Serving Size: 2 Capsules · Servings Per Container: 60",
        "facts_rows": [
            ('Magnesium<span class="sub">as magnesium bisglycinate chelate</span>', "200 mg<br />48%"),
        ],
        "other": "Other ingredients: Hypromellose (capsule), microcrystalline cellulose, vegetable stearate (plant source), silica.",
        "front": "assets/products/mg200-front.png",
        "facts_img": "assets/products/mg200-facts.png",
        "barcode": "assets/products/mg225-barcode.png",
        "related": [
            ("product-mg-225.html", "assets/products/mg225-front.png", "MINERALS / FORMULA 04", "Magnesium Bisglycinate 225 mg", "Higher-potency magnesium bisglycinate."),
            ("product-magtein.html", "assets/products/magtein-front.png", "COGNITIVE / FORMULA 06", "Magtein® Magnesium L-Threonate", "Patented form designed for cognitive support."),
        ],
    },
    {
        "slug": "product-mg-225.html",
        "tag": "Energy & recovery / Formula 04",
        "tag_class": "",
        "title_serif": "Magnesium Bisglycinate",
        "subtitle": "225 mg",
        "desc": "Higher-potency magnesium bisglycinate when your routine needs more elemental magnesium — same chelated form, a stronger dose.",
        "stats": [
            ("225 mg", "magnesium<br />per serving"),
            ("120", "capsules<br />servings vary"),
            ("2", "capsules daily<br />typical routine"),
        ],
        "tagline": "Same form. A clearer higher dose.",
        "why_title": "Why this form?",
        "why_body": "Bisglycinate chelation supports absorption and digestive comfort — useful when you need a more meaningful elemental magnesium load without switching forms.",
        "glance": [
            ("01 / Form", "Magnesium bisglycinate chelate."),
            ("02 / Dose", "225 mg magnesium per serving."),
            ("03 / Routine", "2 capsules daily, or as directed."),
        ],
        "facts_title": "Supplement Facts",
        "serving": "Serving Size: 2 Capsules · Servings Per Container: 60",
        "facts_rows": [
            ('Magnesium<span class="sub">as magnesium bisglycinate chelate</span>', "225 mg<br />54%"),
        ],
        "other": "Other ingredients: Hypromellose (capsule), microcrystalline cellulose, vegetable stearate (plant source), silica.",
        "front": "assets/products/mg225-front.png",
        "facts_img": "assets/products/mg225-facts.png",
        "barcode": "assets/products/mg225-barcode.png",
        "related": [
            ("product-mg-200.html", "assets/products/mg200-front.png", "MINERALS / FORMULA 03", "Magnesium Bisglycinate 200 mg", "Everyday chelated magnesium support."),
            ("product-magtein.html", "assets/products/magtein-front.png", "COGNITIVE / FORMULA 06", "Magtein® Magnesium L-Threonate", "Patented form designed for cognitive support."),
        ],
    },
    {
        "slug": "product-k2.html",
        "tag": "Bones & balance / Formula 05",
        "tag_class": "",
        "title_serif": "Vitamin K2",
        "subtitle": "MK-7 120 mcg",
        "desc": "Menaquinone-7 (MK-7) for calcium utilization and lasting skeletal strength. A long-half-life K2 form with a clear 120 mcg dose.",
        "stats": [
            ("120 mcg", "vitamin K2<br />as MK-7"),
            ("120", "capsules<br />120 servings"),
            ("1", "capsule daily<br />with a meal"),
        ],
        "tagline": "Named MK-7. Measured micrograms.",
        "why_title": "Why this form?",
        "why_body": "MK-7 (menaquinone-7) is a longer-acting vitamin K2 form commonly chosen for daily calcium-metabolism and bone-support routines.",
        "glance": [
            ("01 / Form", "Vitamin K2 as MK-7 (menaquinone-7)."),
            ("02 / Dose", "120 mcg per serving."),
            ("03 / Routine", "1 capsule daily with a meal."),
        ],
        "facts_title": "Supplement Facts",
        "serving": "Serving Size: 1 Capsule · Servings Per Container: 120",
        "facts_rows": [
            ('Vitamin K2<span class="sub">as menaquinone-7 (MK-7)</span>', "120 mcg<br />100%"),
        ],
        "other": "Other ingredients: Hypromellose (capsule), microcrystalline cellulose, vegetable stearate (plant source), silica.",
        "front": "assets/products/k2-front.png",
        "facts_img": "assets/products/k2-facts.png",
        "barcode": "assets/products/k2-barcode.png",
        "related": [
            ("product-mg-200.html", "assets/products/mg200-front.png", "MINERALS / FORMULA 03", "Magnesium Bisglycinate 200 mg", "Chelated magnesium for daily support."),
            ("product-zinc.html", "assets/products/zinc-front.png", "MINERALS / FORMULA 01", "Zinc Bisglycinate", "A highly absorbable form of zinc."),
        ],
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title_serif}{subtitle_html} — ICON FORMULAS</title>
  <meta name="description" content="{desc}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/styles.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a class="logo" href="index.html">ICON <span>FORMULAS</span></a>
      <nav class="nav" id="site-nav" aria-label="Primary">
        <a href="shop.html" aria-current="page">Formulas</a>
        <a href="index.html#standard">Our standard</a>
        <a href="index.html#quality">Quality</a>
        <a href="index.html#faq">FAQ</a>
      </nav>
      <div class="header-actions">
        <a class="btn btn-dark" href="shop.html">Shop collection</a>
        <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav"><span></span></button>
      </div>
    </div>
  </header>

  <main class="pdp">
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumb" style="padding-top: 22px;">
        <a href="index.html">Home</a>
        <span aria-hidden="true">/</span>
        <a href="shop.html">Formulas</a>
        <span aria-hidden="true">/</span>
        <span>{title_serif}</span>
      </nav>

      <div class="pdp-hero">
        <div class="pdp-gallery">
          <div class="pdp-main">
            <img id="main-image" src="{front}" alt="{title_serif} bottle" width="360" height="420" />
          </div>
          <div class="pdp-thumbs" role="tablist" aria-label="Product images">
            <button type="button" role="tab" aria-selected="true" data-full="{front}" title="Front">
              <img src="{front}" alt="Front label" width="80" height="80" />
            </button>
            <button type="button" role="tab" aria-selected="false" data-full="{facts_img}" title="Supplement Facts">
              <img src="{facts_img}" alt="Supplement Facts" width="80" height="80" />
            </button>
            <button type="button" role="tab" aria-selected="false" data-full="{barcode}" title="Barcode and warnings">
              <img src="{barcode}" alt="Barcode panel" width="80" height="80" />
            </button>
          </div>
        </div>

        <div class="pdp-info">
          <p class="eyebrow{tag_class}">{tag}</p>
          <h1>{title_serif}{subtitle_block}</h1>
          <p class="desc">{desc}</p>
          <div class="stat-row">
            {stats_html}
          </div>
          <p class="pdp-tagline">{tagline}</p>
          <div class="pdp-actions">
            <a class="btn btn-primary" href="shop.html">Add to cart</a>
            <a class="btn btn-ghost" href="shop.html">See all formulas</a>
          </div>
          <p class="pdp-note">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6l7-3z"/></svg>
            Made and quality tested in the USA with globally sourced ingredients.
          </p>
          <p class="muted" style="font-size: 12.5px; margin: 0;">Please consult your healthcare professional before use. These statements have not been evaluated by the FDA.</p>
        </div>
      </div>
    </div>

    <section class="pdp-why">
      <div class="container pdp-why-grid">
        <div>
          <p class="eyebrow eyebrow-muted">{tag}</p>
          <h2 class="h2">{why_title}</h2>
          <p class="lead">{why_body}</p>
        </div>
        <div style="background:#fff;border:1px solid var(--line);padding:22px;">
          <p class="eyebrow eyebrow-muted" style="margin-bottom: 8px;">A named form. A transparent approach.</p>
          <p class="serif-accent" style="font-size: 1.5rem; margin: 0; line-height: 1.3;">Form. Dose. Clarity.</p>
        </div>
      </div>
    </section>

    <div class="container">
      <div class="pdp-glance">
        {glance_html}
      </div>

      <div class="pdp-facts">
        <div class="pdp-main" style="aspect-ratio: 4/3;">
          <img src="{facts_img}" alt="Supplement Facts panel on bottle" width="360" height="270" />
        </div>
        <div class="label-facts">
          <h4>{facts_title}</h4>
          <p class="serving">{serving}</p>
          <table class="facts-table">
            <thead>
              <tr><th>Amount Per Serving</th><th>%DV</th></tr>
            </thead>
            <tbody>
              {facts_rows}
            </tbody>
          </table>
          <p class="muted" style="font-size: 12px; margin: 14px 0 10px;">† Daily Value (DV) not established. Please consult the actual product label for the most accurate and up-to-date information.</p>
          <p class="muted" style="font-size: 12.5px; margin: 0;">{other}</p>
        </div>
      </div>

      <section class="pdp-related">
        <h2>You may also like</h2>
        <div class="related-grid">
          {related_html}
        </div>
      </section>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-inner">
        <a class="logo" href="index.html">ICON <span>FORMULAS</span></a>
        <nav class="footer-nav" aria-label="Footer">
          <a href="shop.html">Formulas</a>
          <a href="index.html#standard">Our standard</a>
          <a href="index.html#quality">Quality</a>
          <a href="index.html#faq">FAQ</a>
        </nav>
        <p class="footer-note">Better nutrition. <em>A brighter you.</em></p>
      </div>
      <p class="footer-legal">These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease. Consult your healthcare professional before use.</p>
    </div>
  </footer>
  <script src="js/main.js"></script>
</body>
</html>
"""

for p in products:
    subtitle = p.get("subtitle") or ""
    subtitle_html = f" {subtitle}" if subtitle else ""
    subtitle_block = f'<div class="subtitle">{subtitle}</div>' if subtitle else ""
    tag_class = f" {p['tag_class']}" if p.get("tag_class") else ""
    stats_html = "\n            ".join(
        f'<div class="stat"><div class="value">{v}</div><div class="label">{l}</div></div>'
        for v, l in p["stats"]
    )
    glance_html = "\n        ".join(
        f'<article><div class="num">{n}</div><h3>{t}</h3></article>' for n, t in p["glance"]
    )
    facts_rows = "\n              ".join(
        f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in p["facts_rows"]
    )
    related_html = "\n          ".join(
        f'<a class="related-card" href="{href}"><img src="{img}" alt="{name}" width="90" height="110" /><div><p class="tag">{tag}</p><h3>{name}</h3><p class="muted" style="font-size:13px;margin:0 0 8px;">{blurb}</p><span class="link-arrow">Learn more</span></div></a>'
        for href, img, tag, name, blurb in p["related"]
    )
    html = TEMPLATE.format(
        title_serif=p["title_serif"],
        subtitle_html=subtitle_html,
        subtitle_block=subtitle_block,
        desc=p["desc"],
        tag=p["tag"],
        tag_class=tag_class,
        front=p["front"],
        facts_img=p["facts_img"],
        barcode=p["barcode"],
        stats_html=stats_html,
        tagline=p["tagline"],
        why_title=p["why_title"],
        why_body=p["why_body"],
        glance_html=glance_html,
        facts_title=p["facts_title"],
        serving=p["serving"],
        facts_rows=facts_rows,
        other=p["other"],
        related_html=related_html,
    )
    out = ROOT / p["slug"]
    out.write_text(html, encoding="utf-8")
    print("wrote", out.name)

print("done", len(products))
