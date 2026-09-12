# ============================================================
#  Suite360 — Web Suite (launcher 13 produk perbankan digital)
#  Image: static site di atas nginx alpine (ringan, ~20 MB)
#  Build : docker build -t suite360 .
#  Run   : docker run -d --name suite360 -p 8080:80 suite360
# ============================================================
FROM nginx:1.27-alpine

LABEL org.opencontainers.image.title="Suite360 Web Suite" \
      org.opencontainers.image.description="Layar launcher 13 produk perbankan digital dengan tema elegan" \
      org.opencontainers.image.vendor="radianadhic" \
      org.opencontainers.image.source="https://github.com/radianadhic/suite360"

# konfigurasi server (gzip + cache aset statis)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# hanya berkas situs yang masuk image
COPY index.html /usr/share/nginx/html/
COPY assets/    /usr/share/nginx/html/assets/
COPY product/   /usr/share/nginx/html/product/

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -q -O /dev/null http://127.0.0.1/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
