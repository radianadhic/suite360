#!/usr/bin/env python3
"""Generate product logo-lite SVGs + placeholder reporting pages for the Web Suite."""
import os

BASE = "/home/user/product"
os.makedirs(BASE, exist_ok=True)

SVG_HEAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" fill="none">\n'
SVG_TAIL = '</svg>\n'

LOGOS = {
"clarity_logo-lite.svg": """<defs><linearGradient id="g" x1="24" y1="24" x2="104" y2="104" gradientUnits="userSpaceOnUse"><stop stop-color="#e9d8ae"/><stop offset=".5" stop-color="#c6a15b"/><stop offset="1" stop-color="#a68540"/></linearGradient></defs>
<circle cx="64" cy="66" r="36" stroke="url(#g)" stroke-width="9"/>
<path d="M49 67l10 10 20-23" stroke="url(#g)" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M100 18v16M92 26h16" stroke="#e9d8ae" stroke-width="7" stroke-linecap="round"/>
""",
"orivo_logo-lite.svg": """<defs><linearGradient id="g" x1="28" y1="28" x2="100" y2="100" gradientUnits="userSpaceOnUse"><stop stop-color="#3ee6cf"/><stop offset="1" stop-color="#0c7f77"/></linearGradient></defs>
<circle cx="64" cy="64" r="17" fill="url(#g)"/>
<path d="M30 64a34 34 0 0 1 58-24" stroke="url(#g)" stroke-width="8" stroke-linecap="round"/>
<path d="M98 64a34 34 0 0 1-58 24" stroke="url(#g)" stroke-width="8" stroke-linecap="round"/>
<circle cx="88" cy="40" r="6" fill="#f08a0d"/>
<circle cx="40" cy="88" r="6" fill="#f08a0d"/>
""",
"originiq_logo-lite.svg": """<defs><linearGradient id="g" x1="28" y1="94" x2="100" y2="42" gradientUnits="userSpaceOnUse"><stop stop-color="#93b4fd"/><stop offset="1" stop-color="#2550eb"/></linearGradient></defs>
<path d="M28 94 56 66l20 14 24-36" stroke="url(#g)" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="28" cy="94" r="7" fill="#2550eb"/>
<circle cx="56" cy="66" r="7" fill="#4d73f0"/>
<circle cx="76" cy="80" r="7" fill="#4d73f0"/>
<circle cx="100" cy="42" r="10" fill="#fbbf24"/>
""",
"nara_logo-lite.svg": """<defs><linearGradient id="b" x1="30" y1="98" x2="70" y2="40" gradientUnits="userSpaceOnUse"><stop stop-color="#8fc4f2"/><stop offset="1" stop-color="#1b6fb8"/></linearGradient><linearGradient id="v" x1="64" y1="26" x2="94" y2="54" gradientUnits="userSpaceOnUse"><stop stop-color="#34d399"/><stop offset="1" stop-color="#0e9f6e"/></linearGradient></defs>
<path d="M30 98c20-4 28-24 34-46" stroke="url(#b)" stroke-width="9" stroke-linecap="round"/>
<circle cx="30" cy="98" r="6" fill="#8fc4f2"/>
<path d="M64 52c0-18 14-26 30-26 0 18-12 28-30 26Z" fill="url(#v)"/>
""",
"bariva_logo-lite.svg": """<defs><linearGradient id="g" x1="30" y1="20" x2="98" y2="108" gradientUnits="userSpaceOnUse"><stop stop-color="#7de9f7"/><stop offset="1" stop-color="#0891b2"/></linearGradient></defs>
<path d="M64 20 98 32v28c0 24-14 40-34 48-20-8-34-24-34-48V32L64 20Z" stroke="url(#g)" stroke-width="9" stroke-linejoin="round"/>
<path d="M45 62h10l6-12 8 24 6-12h10" stroke="#7de9f7" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
""",
"lims_logo-lite.svg": """<defs><linearGradient id="b" x1="64" y1="18" x2="64" y2="112" gradientUnits="userSpaceOnUse"><stop stop-color="#60a5fa"/><stop offset="1" stop-color="#1e40af"/></linearGradient><linearGradient id="g" x1="22" y1="86" x2="106" y2="86" gradientUnits="userSpaceOnUse"><stop stop-color="#f0d080"/><stop offset="1" stop-color="#d4a53a"/></linearGradient></defs>
<path d="M64 18C64 18 32 58 32 80a32 32 0 0 0 64 0C96 58 64 18 64 18Z" fill="url(#b)"/>
<path d="M22 86q10-10 20 0t20 0 20 0 20 0" stroke="url(#g)" stroke-width="7" stroke-linecap="round"/>
""",
"custovanta_logo-lite.svg": """<defs><linearGradient id="g" x1="30" y1="30" x2="98" y2="98" gradientUnits="userSpaceOnUse"><stop stop-color="#7ddcff"/><stop offset="1" stop-color="#0ea5e9"/></linearGradient></defs>
<rect x="30" y="30" width="68" height="68" rx="20" stroke="url(#g)" stroke-width="8"/>
<circle cx="64" cy="58" r="11" fill="#72f1c5"/>
<path d="M64 66 57 90h14L64 66Z" fill="#72f1c5"/>
""",
"narapro360_logo-lite.svg": """<defs><linearGradient id="b" x1="40" y1="38" x2="88" y2="94" gradientUnits="userSpaceOnUse"><stop stop-color="#60a5fa"/><stop offset="1" stop-color="#2563eb"/></linearGradient><linearGradient id="g" x1="18" y1="66" x2="110" y2="66" gradientUnits="userSpaceOnUse"><stop stop-color="#fbbf24"/><stop offset="1" stop-color="#f59e0b"/></linearGradient></defs>
<circle cx="64" cy="50" r="13" fill="url(#b)"/>
<path d="M40 94a24 24 0 0 1 48 0H40Z" fill="url(#b)"/>
<ellipse cx="64" cy="66" rx="46" ry="17" stroke="url(#g)" stroke-width="6" transform="rotate(-16 64 66)"/>
<circle cx="108" cy="53" r="6" fill="#fbbf24"/>
""",
"treasuryone_logo-lite.svg": """<defs><linearGradient id="g" x1="30" y1="26" x2="98" y2="100" gradientUnits="userSpaceOnUse"><stop stop-color="#f6d47c"/><stop offset="1" stop-color="#f2b33d"/></linearGradient><linearGradient id="t" x1="44" y1="60" x2="84" y2="88" gradientUnits="userSpaceOnUse"><stop stop-color="#35d0dd"/><stop offset="1" stop-color="#12a9b6"/></linearGradient></defs>
<path d="M30 48 64 26l34 22" stroke="url(#g)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M44 60v28M64 60v28M84 60v28" stroke="url(#t)" stroke-width="8" stroke-linecap="round"/>
<path d="M32 100h64" stroke="url(#g)" stroke-width="8" stroke-linecap="round"/>
""",
"orchevia_logo-lite.svg": """<defs><linearGradient id="g" x1="34" y1="34" x2="94" y2="94" gradientUnits="userSpaceOnUse"><stop stop-color="#e6cfa5"/><stop offset="1" stop-color="#b48b45"/></linearGradient></defs>
<path d="M64 64 34 34M64 64l30-30M64 64 34 94M64 64l30 30" stroke="url(#g)" stroke-width="6" stroke-linecap="round"/>
<circle cx="34" cy="34" r="8" stroke="url(#g)" stroke-width="6"/>
<circle cx="94" cy="34" r="8" stroke="url(#g)" stroke-width="6"/>
<circle cx="34" cy="94" r="8" stroke="url(#g)" stroke-width="6"/>
<circle cx="94" cy="94" r="8" stroke="url(#g)" stroke-width="6"/>
<circle cx="64" cy="64" r="11" fill="url(#g)"/>
""",
"pensia_logo-lite.svg": """<defs><linearGradient id="t" x1="30" y1="26" x2="80" y2="102" gradientUnits="userSpaceOnUse"><stop stop-color="#2dd4bf"/><stop offset="1" stop-color="#0e6b63"/></linearGradient><linearGradient id="g" x1="80" y1="52" x2="104" y2="76" gradientUnits="userSpaceOnUse"><stop stop-color="#e7c65a"/><stop offset="1" stop-color="#c9a227"/></linearGradient></defs>
<path d="M76 26A40 40 0 1 0 76 102 32 32 0 1 1 76 26Z" fill="url(#t)"/>
<path d="m92 52 4 8 8 4-8 4-4 8-4-8-8-4 8-4 4-8Z" fill="url(#g)"/>
""",
"aurea_logo-lite.svg": """<defs><linearGradient id="g" x1="26" y1="22" x2="102" y2="102" gradientUnits="userSpaceOnUse"><stop stop-color="#f4e9c8"/><stop offset=".55" stop-color="#c8a658"/><stop offset="1" stop-color="#a8883e"/></linearGradient></defs>
<path d="M64 22 102 42 64 62 26 42 64 22Z" fill="url(#g)"/>
<path d="M26 62l38 20 38-20" stroke="url(#g)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M26 82l38 20 38-20" stroke="url(#g)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
""",
"slika_logo-lite.svg": """<defs><linearGradient id="g" x1="32" y1="30" x2="96" y2="92" gradientUnits="userSpaceOnUse"><stop stop-color="#4fd1c5"/><stop offset="1" stop-color="#17a398"/></linearGradient></defs>
<rect x="32" y="42" width="64" height="50" rx="16" stroke="url(#g)" stroke-width="8"/>
<circle cx="52" cy="64" r="6" fill="#4fd1c5"/>
<circle cx="76" cy="64" r="6" fill="#4fd1c5"/>
<path d="M54 78q10 8 20 0" stroke="url(#g)" stroke-width="6" stroke-linecap="round"/>
<path d="M64 42V30" stroke="url(#g)" stroke-width="7" stroke-linecap="round"/>
<circle cx="64" cy="24" r="6" fill="url(#g)"/>
""",
}

for fname, body in LOGOS.items():
    with open(os.path.join(BASE, fname), "w") as f:
        f.write(SVG_HEAD + body + SVG_TAIL)
print("wrote", len(LOGOS), "logos")

PRODUCTS = [
    ("Clarity71", "Aplikasi PSAK 71", "clarity_logo-lite.svg", "clarity71_web_reporting.html", "#c6a15b"),
    ("Orivo", "Cash Management", "orivo_logo-lite.svg", "orivo_web_reporting.html", "#0fb6a6"),
    ("OriginIQ", "LOS / Loan Origination System", "originiq_logo-lite.svg", "originiq_web_reporting.html", "#5b7bff"),
    ("Nara", "Wealth Management", "nara_logo-lite.svg", "nara_web_reporting.html", "#4da3e8"),
    ("Bariva", "Fraud Risk Management", "bariva_logo-lite.svg", "bariva_web_reporting.html", "#22d3ee"),
    ("LiMS", "Liquidity Management", "lims_logo-lite.svg", "lims_web_reporting.html", "#d4a53a"),
    ("Custovanta", "Custodian System", "custovanta_logo-lite.svg", "custovanta_web_reporting.html", "#38bdf8"),
    ("NaraPro360", "Selling Agent", "narapro360_logo-lite.svg", "narapro360_web_reporting.html", "#f59e0b"),
    ("TreasuryOne", "Treasury System", "treasuryone_logo-lite.svg", "treasuryone_web_reporting.html", "#2cc4d0"),
    ("Orchevia", "Payment Hub", "orchevia_logo-lite.svg", "orchevia_web_reporting.html", "#c5a065"),
    ("Pensia", "DPLK Syariah", "pensia_logo-lite.svg", "pensia_web_reporting.html", "#2dd4bf"),
    ("Aurea", "Master Data Management", "aurea_logo-lite.svg", "aurea_web_reporting.html", "#c8a658"),
    ("Slika", "Slik OJK Robot Automation", "slika_logo-lite.svg", "slika_web_reporting.html", "#4fd1c5"),
]

TPL = """<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{name} — Reporting</title>
<style>
  :root {{ --accent: {accent}; }}
  * {{ margin: 0; box-sizing: border-box; }}
  body {{
    min-height: 100vh; display: grid; place-items: center;
    background: #161719 radial-gradient(900px 480px at 50% -10%, rgba(255,255,255,.05), transparent 70%);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #eef1f5; padding: 24px;
  }}
  .back {{
    position: fixed; top: 22px; left: 26px; color: #9aa3ae; text-decoration: none;
    font-size: .9rem; letter-spacing: .02em; transition: color .2s;
  }}
  .back:hover {{ color: #fff; }}
  .card {{
    width: min(560px, 92vw); text-align: center; padding: 56px 40px 48px;
    background: linear-gradient(165deg, #232529, #1a1c1f 55%, #141518);
    border: 1px solid rgba(255,255,255,.08); border-radius: 28px;
    box-shadow: 0 30px 80px rgba(0,0,0,.5), inset 0 1px 0 rgba(255,255,255,.07);
  }}
  img {{ width: 96px; height: 96px; filter: drop-shadow(0 10px 24px rgba(0,0,0,.45)); }}
  .badge {{
    display: inline-block; margin-top: 22px; padding: 6px 14px; border-radius: 999px;
    font-size: .68rem; font-weight: 700; letter-spacing: .28em;
    color: var(--accent); border: 1px solid color-mix(in srgb, var(--accent) 45%, transparent);
    background: color-mix(in srgb, var(--accent) 12%, transparent);
  }}
  h1 {{ margin-top: 16px; font-size: 1.7rem; font-weight: 650; letter-spacing: -.01em; }}
  .desc {{ margin-top: 8px; color: #98a1ac; font-size: .95rem; }}
  .note {{
    margin-top: 26px; padding: 14px 18px; border-radius: 14px; font-size: .85rem; line-height: 1.6;
    color: #aeb6c0; background: rgba(255,255,255,.04); border: 1px dashed rgba(255,255,255,.12);
  }}
</style>
</head>
<body>
<a class="back" href="../index.html">&larr; Kembali ke Suite</a>
<main class="card">
  <img src="{icon}" alt="Logo {name}"/>
  <div><span class="badge">REPORTING</span></div>
  <h1>{name}</h1>
  <p class="desc">{desc}</p>
  <p class="note">Halaman reporting <strong>{name}</strong> sedang disiapkan &mdash; ini placeholder bertema dari Web Suite. Ganti berkas ini dengan halaman reporting aslinya.</p>
</main>
</body>
</html>
"""

for name, desc, icon, link, accent in PRODUCTS:
    with open(os.path.join(BASE, link), "w") as f:
        f.write(TPL.format(name=name, desc=desc, icon=icon, accent=accent))
print("wrote", len(PRODUCTS), "placeholder reporting pages")
