#!/usr/bin/env python3
"""Turn the Claude Design export into a plain scrolling web deck.

Why this exists: the export needs the design-tool runtime to render, and that
runtime shows one slide at a time with a thumbnail rail. On a phone there is
nothing to scroll. So we let the runtime render once in headless Chrome, take
the finished DOM, and keep only the deck's own stylesheet and its seven
slides. The output has no JavaScript framework and no rail. Every word and
every pixel of the slides is the designer's; only the container changed.

Run: python3 build.py     (needs Google Chrome and a free port)
"""
import http.server, os, re, socketserver, subprocess, threading, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'source')
OUT = os.path.join(ROOT, 'web', 'deck', 'index.html')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
PORT = 8931

def render():
    """Serve source/ and let Chrome resolve the templating for us."""
    os.chdir(SRC)
    h = http.server.SimpleHTTPRequestHandler
    srv = socketserver.TCPServer(('127.0.0.1', PORT), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    url = 'http://127.0.0.1:%d/EverGuard-Partnership-Deck.current.dc.html' % PORT
    dom = subprocess.run([CHROME, '--headless=new', '--disable-gpu',
                          '--virtual-time-budget=9000', '--dump-dom', url],
                         capture_output=True, text=True).stdout
    srv.shutdown()
    return dom

LAYOUT = """
/* Layout added by build.py. The slides are authored at 1920x1080, so each one
   sits in a 16:9 frame and is scaled to the frame's width. Scaling instead of
   reflowing keeps the design exactly as drawn at every size, including phones,
   and the page scrolls normally. */
html,body{margin:0;padding:0;background:#141414;overflow-x:hidden}
deck-stage{display:block;max-width:1600px;margin:0 auto;padding:18px 18px 40px}
.frame{position:relative;width:100%;aspect-ratio:16/9;overflow:hidden;
  border:1px solid rgba(236,236,236,.10);border-radius:3px;margin:0 0 18px;background:#191919}
.frame > .slide{position:absolute;top:0;left:0;width:1920px;height:1080px;
  box-sizing:border-box;transform-origin:0 0;transform:scale(var(--s,1))}
/* The export assumes a 1920x1080 box including its own padding. Without this
   the padding is added outside the width and the right edge clips. */
.frame > .slide *{box-sizing:border-box}
.deck-end{color:rgba(236,236,236,.52);font:600 12px/1.6 Montserrat,system-ui,sans-serif;
  letter-spacing:.08em;text-transform:uppercase;text-align:center;padding:6px 0 14px}
/* The deck ends by moving her on, not by stopping. Same exit pattern as every
   other section: the next thing in the story, then home. */
.exit{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;padding:0 0 34px}
/* Montserrat, not Orbitron: a display face at 11px with wide tracking is what
   makes small interface text tiring to read. */
.exit a{display:inline-flex;align-items:center;justify-content:center;min-height:46px;
  padding:13px 22px;border-radius:3px;text-decoration:none;border:1px solid;
  font-family:Montserrat,system-ui,sans-serif;font-weight:700;font-size:11.5px;
  letter-spacing:.09em;text-transform:uppercase}
.exit a.go{background:#ff6a00;border-color:#ff6a00;color:#141414;font-weight:700}
.exit a.go:hover{background:#ff8a33}
.exit a.home{background:transparent;border-color:rgba(236,236,236,.18);color:rgba(236,236,236,.84)}
.exit a.home:hover{border-color:#ff6a00;color:#ff6a00}
/* Joey cut the top-left corner motif: its diagonal ran against the angle of
   the right-hand rules and the page-number slashes. As of the 14 Sep export the
   markup no longer contains it at all, so this rule is now only a guard in case
   a later export brings it back. */
.frame > .slide .slash{display:none !important}
@media (max-width:700px){ deck-stage{padding:10px 10px 28px} .frame{margin-bottom:10px} }
@media print{
  html,body{background:#fff}
  deck-stage{max-width:none;margin:0;padding:0}
  .frame{border:0;border-radius:0;margin:0;page-break-after:always;break-after:page}
  .deck-end{display:none}
}
"""

SCALE_JS = """
// Fit each 1920px slide to its frame. One listener, no dependencies.
(function(){
  var frames = document.querySelectorAll('.frame');
  function fit(){
    for (var i=0;i<frames.length;i++){
      frames[i].style.setProperty('--s', frames[i].clientWidth/1920);
    }
  }
  fit();
  addEventListener('resize', fit);
  addEventListener('orientationchange', fit);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
})();
"""

def main():
    dom = render()
    if '<deck-stage' not in dom:
        sys.exit('render failed: no deck-stage in the DOM')

    head = dom[:dom.find('</head>')]
    fonts = re.search(r'<link[^>]*fonts\.googleapis[^>]*>', head)
    deck_css = re.search(r'<style data-dc-tpl="3">(.*?)</style>', head, re.S)
    if not deck_css:
        sys.exit('render failed: the deck stylesheet was not found')

    body = dom[dom.find('<deck-stage'):dom.find('</deck-stage>')]
    slides = re.findall(r'<section [^>]*class="slide[^"]*".*?</section>', body, re.S)
    if len(slides) < 5:
        sys.exit('render failed: found %d slides' % len(slides))

    title = re.search(r'<title>(.*?)</title>', head, re.S)
    title = title.group(1).strip() if title else 'EverGuard'

    frames = '\n'.join('<div class="frame">%s</div>' % s for s in slides)
    out = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="robots" content="noindex, nofollow, noarchive">\n'
        '<title>%s</title>\n%s\n<style>%s</style>\n<style>%s</style>\n</head>\n'
        '<body>\n<deck-stage>\n%s\n<div class="deck-end">End &middot; EverGuard</div>\n'
        '<div class="exit"><a class="go" href="../agreement/">The agreement</a>'
        '<a class="home" href="../">Home</a></div>\n'
        '</deck-stage>\n<script>%s</script>\n</body>\n</html>\n'
    ) % (title, fonts.group(0) if fonts else '', deck_css.group(1), LAYOUT, frames, SCALE_JS)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)
    print('built %s  (%d slides, %d bytes)' % (OUT, len(slides), len(out)))

if __name__ == '__main__':
    main()
