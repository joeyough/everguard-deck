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

## Four doors

The landing page is the room, in story order. The console comes first on
purpose: a brochure being opened is not proof, so the product proves the paper.

| | Door | Where |
|---|---|---|
| 01 | **The console** | `/demo/` One night, one alert, one closed report. |
| 02 | **The team** | `/deck/` The partnership deck. |
| 03 | **The agreement** | `/agreement/` Terms, plus a plain PDF for an attorney. |
| 04 | **Next step** | On the landing page: reply to Keenan and book thirty minutes. |

## The console

`web/demo/index.html` is hand-built, no framework and no design runtime. It
plays a single incident: four cameras, motion on CAM 02, an analytics flag, an
operator verifying, a timestamped voice-down, the subject leaving, cleared
without dispatch, then an incident report with a timeline, evidence thumbnails
and one line a client could be sent. Play, pause and replay. Everything sits in
normal document flow, so there is no sticky stage and no scroll hijacking: the
previous build put fixed furniture over the picture and it collided on phones.

The earlier cinematic version, EVERGUARD // ROLL CALL, is kept at
`web/demo/film/` and is not linked from anywhere. It is worth keeping for the
HUD and the transitions, but a wrapped vehicle is packaging, not the product.

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
