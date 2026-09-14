#!/bin/bash
# Regenerate the plain white PDF from web/agreement/print.html.
# print.html is the legal-looking version: same terms, no color, no interaction.
# Keep it in step with web/agreement/index.html by hand; the web page is the
# interactive one and the PDF is what goes to an attorney.
set -e
cd "$(dirname "$0")/web"
python3 -m http.server 8917 >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null' EXIT
sleep 1
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --no-pdf-header-footer --virtual-time-budget=6000 \
  --print-to-pdf="agreement/EverGuard-Partnership-Agreement.pdf" \
  http://127.0.0.1:8917/agreement/print.html 2>&1 | tail -1
