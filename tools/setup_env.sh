#!/bin/bash
# One-time per container: tools the pipeline needs (Tesseract, LibreOffice Writer, Poppler, OpenJPEG, EPUBCheck 5.1.0, Pillow).
# Usage: tools/setup_env.sh [epubcheck_dir]   (default: /home/antigravity/.local/share/epubcheck)
#        tools/setup_env.sh --apt-https-only [apt_dir]   (only the mirror rewrite; used by the tests)
set -e

apt_https() {
  local d=${1:-/etc/apt}
  for f in "$d"/sources.list "$d"/sources.list.d/*.sources "$d"/sources.list.d/*.list; do
    if [ -f "$f" ]; then sed -E -i 's#http://(archive|security)\.ubuntu\.com#https://\1.ubuntu.com#g' "$f"; fi
  done
}
if [ "${1:-}" = "--apt-https-only" ]; then apt_https "${2:-}"; exit 0; fi

SUDO=""
if [ "$(id -u)" -ne 0 ] && command -v sudo >/dev/null 2>&1; then SUDO="sudo"; fi

NEED_APT=0
for bin in tesseract soffice pdftoppm opj_decompress; do
  if ! command -v "$bin" >/dev/null 2>&1; then NEED_APT=1; break; fi
done

if [ "$NEED_APT" -eq 1 ]; then
  $SUDO bash -c 'for f in /etc/apt/sources.list /etc/apt/sources.list.d/*.sources /etc/apt/sources.list.d/*.list; do [ -f "$f" ] && sed -E -i "s#http://(archive|security)\.ubuntu\.com#https://\1.ubuntu.com#g" "$f"; done; true'
  DEBIAN_FRONTEND=noninteractive timeout 600 $SUDO apt-get update -q >/dev/null 2>&1
  DEBIAN_FRONTEND=noninteractive $SUDO apt-get install -y -q --no-install-recommends \
    tesseract-ocr tesseract-ocr-eng libreoffice-writer poppler-utils libopenjp2-tools >/dev/null 2>&1
fi

D=${1:-/home/antigravity/.local/share/epubcheck}
if [ ! -f "$D/epubcheck-5.1.0/epubcheck.jar" ]; then
  mkdir -p "$D"
  curl -L -sS "https://github.com/w3c/epubcheck/releases/download/v5.1.0/epubcheck-5.1.0.zip" -o "$D/e.zip"
  unzip -q -o "$D/e.zip" -d "$D"
  rm -f "$D/e.zip"
fi

python3 -c "import PIL.Image" 2>/dev/null || python3 -m pip install -q Pillow
echo "ok: tesseract $(tesseract --version 2>&1 | head -1 | cut -d' ' -f2), epubcheck at $D/epubcheck-5.1.0/epubcheck.jar"
