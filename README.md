# suite360 — Web Suite (Suite All Application)

Layar launcher seluruh produk perbankan digital dalam satu halaman bergaya suite aplikasi modern: latar navy bergradasi dengan motif *guilloché*, grain, vignette, animasi cahaya (orb aurora, beam sweep, kelip bintang), dan 13 tile produk dengan logo serta keterangan masing‑masing.

**Live (GitHub Pages):** https://radianadhic.github.io/suite360/

## Produk

| # | Produk | Keterangan | Halaman |
|---|--------|------------|---------|
| 1 | Clarity71 | Aplikasi PSAK 71 | `product/clarity71_web_reporting.html` |
| 2 | Orivo | Cash Management | `product/orivo_web_reporting.html` |
| 3 | OriginIQ | LOS / Loan Origination System | `product/originiq_web_reporting.html` |
| 4 | Nara | Wealth Management | `product/nara_web_reporting.html` |
| 5 | Bariva | Fraud Risk Management | `product/bariva_web_reporting.html` |
| 6 | LiMS | Liquidity Management | `product/lims_web_reporting.html` |
| 7 | Custovanta | Custodian System | `product/custovanta_web_reporting.html` |
| 8 | NaraPro360 | Selling Agent | `product/narapro360_web_reporting.html` |
| 9 | TreasuryOne | Treasury System | `product/treasuryone_web_reporting.html` |
| 10 | Orchevia | Payment Hub | `product/orchevia_web_reporting.html` |
| 11 | Pensia | DPLK Syariah | `product/pensia_web_reporting.html` |
| 12 | Aurea | Master Data Management | `product/aurea_web_reporting.html` |
| 13 | Slika | Slik OJK Robot Automation | `product/slika_web_reporting.html` |

## Struktur repo

```
index.html                  Layar suite (launcher) + pencarian + animasi latar
assets/                     Aset raster root (logo-lite.png, favicon, apple-touch-icon)
product/*_logo-lite.svg     Mark "lite" tiap produk (gradien warna brand)
product/*_web_reporting.html  Halaman produk (salinan marketing, self-contained)
product/img/, product/frontend/  Aset yang direferensikan halaman produk
Dockerfile, nginx.conf      Image docker (nginx:1.27-alpine, gzip + cache)
.dockerignore               Context build ramping
make_assets.py              Skrip generator logo SVG + placeholder reporting
uploads/                    Sumber branding (halaman marketing asli)
```

## Menjalankan lokal

```bash
python3 -m http.server 8000
# buka http://localhost:8000
```

## Docker

```bash
docker build -t suite360 .
docker run -d --name suite360 -p 8080:80 suite360
# buka http://localhost:8080
```

## Catatan

- Halaman `product/` memakai path relatif (`../assets/`, `img/`, `frontend/`) sehingga berfungsi baik di root domain maupun di subpath GitHub Pages.
- Animasi latar otomatis nonaktif bagi pengguna `prefers-reduced-motion`.
- Pencarian: tekan `/` untuk fokus, `Esc` untuk menghapus.
