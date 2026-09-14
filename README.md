# EverGuard proposal site

Private proposal for **Chris Calderon**. Keenan Miller Technology Solutions and
Joe CXO.

> **This repository is public.** Anything committed here can be read by anyone
> who finds it, including search engines. Client details and pricing are
> already in the deck files, which is a deliberate choice by Joey so Keenan can
> read the work without a GitHub account. Do not add anything else that would
> hurt if a stranger read it: no contracts, no signed agreements, no bank or
> payment details, no personal contact information, and no credentials. The
> site's access code lives in a Netlify environment variable and must never be
> committed.

Live: **https://everguard-proposal.netlify.app**, behind a shared access code
checked at the edge, so the site serves nothing without it. Ask Joey for the
code. Nothing has been sent to the client yet.

## Three pieces

| | Piece | Status |
|---|---|---|
| 01 | **The deck** | Live at `/deck/`. |
| 02 | **The agreement** | Scope and terms, the version that goes to a lawyer. Not drafted. |
| 03 | **The demo** | Live at `/demo/`. EVERGUARD // ROLL CALL: five beats, the fleet livery flip with a contrast readout, the uniform spec, a live Oahu map and dispatch ticker. |

All three are wired to cards on `web/index.html`.

The demo ships with the design runtime (`support.js`) because its interactions
depend on it, unlike the deck, which is flattened by `build.py`. Three things
were changed in the hosted copy and are marked in the file: the close button
pointed at `#partnership`, an anchor that does not exist anywhere in the page,
and now returns to the proposal hub; the hover-only instruction became
"explore the markers" because this opens on phones; and the fixed HUD blocks
were given room at narrow widths, where the top-left readout collided with the
clock and the build label collided with the sound toggle. The design file in
`source/` is untouched.

## Layout

- `web/` is what deploys. `netlify.toml` publishes it.
- `web/index.html` is the hub page.
- `web/deck/` is the deck. It is the Claude Design export served as is, with one
  added line of CSS that hides the design-tool thumbnail rail so it presents
  full bleed.
- `source/` holds the original exports. `EverGuard-Partnership-Deck.current.dc.html`
  is the one to work from. `Partnership-Deck.older.dc.html` is an earlier
  version, kept only so nobody edits the wrong file.
- `assets/` holds the three images the deck uses.

A responsive rebuild is in progress on a `web-build` branch.

## House rules

- **Brand is EVERGUARD.** Never any other name for it.
- Orange `#FF6A00` and `#CC4E00`. Black `#1A1A1A`, charcoal `#2E2E2E`, bone
  `#E6E6E6`. Headers Orbitron Bold, body Montserrat Regular.
- Thin orange line icons. One real camera or operations photo per slide,
  maximum. No sunset heroes, no stock person with a coffee cup.
- Nothing is published, linked, or sent to the client without Joey's yes on the
  exact final version.
- The two current image placeholders are sunset stock and want replacing with
  real camera or site stills. Drop them in `assets/` and swap the references.

## Working on it

No build step. Open `web/index.html` in a browser, or serve the folder:

```
cd web && python3 -m http.server 8899
```

Deploys are manual and Joey runs them.
