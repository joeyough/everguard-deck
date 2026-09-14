# Claude Design prompt: the EverGuard demo

Paste everything between the rules into Claude Design. Nothing above or below
the rules is part of the prompt.

---

Build a single-page interactive demo called **EVERGUARD // ROLL CALL**.

It is a marketing experience, not a slide deck. Think the vertical slice of a
video game: the first three minutes a studio shows to prove the whole thing is
real. It has a cold open, one hero interaction, and a close. It is short,
loud, and finished.

## Who it is for

Chris Calderon runs a security and monitoring operation on Oʻahu. She is
standing up her own brand, EverGuard, and taking delivery of a fleet of Toyota
RAV4s. Every vehicle is orange. She made one decision that the whole demo hangs
on: **she flipped the colors.** The truck is orange and the lettering is black,
so the words read hard against the paint instead of disappearing into it. She
also has uniforms coming. She has said she wants websites. This demo is the
answer to that, tailored to her, so the first thing she feels is that somebody
was listening.

## The through line

The orange RAV4 is the transition. It does not sit in a hero image. It enters
frame at speed, crosses, and its body wipes the screen into the next scene.
Every major beat is separated by a vehicle pass. That is the signature move.
Use it three times and never explain it.

## The five beats

**01 — COLD OPEN.** Black. A camera HUD boots: a reticle, a blinking REC dot,
`CAM 01 — HONOLULU` and a coordinate readout ticking. Grain and faint
scanlines. Two seconds of almost nothing. Then headlights bloom from the left
and the RAV4 rushes across with motion blur and speed lines, and the orange
body wipes the frame to beat 02.

**02 — THE FLIP.** The hero interaction. A large three-quarter RAV4 sits on a
dark stage under a slow rotating light sweep. A control strip lets the visitor
switch the livery live: lettering black on orange, which is hers and is the
default, against the ordinary way everyone else does it, white on white or
orange on white. The change animates. A short line appears when the flip is
selected: *"Black on orange. Readable at forty miles an hour and at night.
That was your call, not ours."* Let the visitor drag to rotate the vehicle a
little. Give the door panel a hover state that pops the EVERGUARD wordmark and
a unit number.

**03 — THE CREW.** Same treatment, one step smaller. The uniform: shirt,
patch, and plate carrier or polo option, with the same black-on-orange patch.
Toggle between day shift and night shift and watch the fabric and patch change
under the light. Small hover callouts: patch, radio, badge placement. Keep this
beat quick.

**04 — LIVE ISLAND.** A stylized dark map of Oʻahu with a thin orange
coastline. Patrol pins move slowly along routes. A dispatch ticker runs down
one edge with plausible, mundane entries: `UNIT 04 · ON SCENE · WAIKIKI`,
`CAM 12 · MOTION · KALIHI`, `UNIT 02 · CLEAR`. Nothing alarming, nothing fake
dramatic. A counter shows cameras online and units rolling. This is the beat
that says the brand is an operation, not a logo.

**05 — CLOSE.** One more vehicle pass wipes to a quiet end card: the EverGuard
wordmark, the line **"Stronger solutions, safer tomorrows."**, and a single
button reading *See the partnership*. Nothing else. No form, no pricing, no
contact fields.

## Game feel

This is the part that makes it a banger instead of a website.

- Boot it like a game: a two-second load bar labelled `VERTICAL SLICE — BUILD
  0.1` with the HUD assembling around it.
- Persistent HUD furniture on the edges: corner brackets, a frame counter, a
  live clock in Hawaii time, a small `REC` dot that never stops blinking.
- A sound toggle, off by default, in the corner. If sound is on: a low room
  tone, a whoosh on each vehicle pass, a soft click on every toggle. Never
  autoplay audio.
- Motion has weight. Things ease in fast and settle slow. Nothing bounces.
- A progress rail down the right edge showing the five beats, clickable.
- Scroll drives the beats on desktop and on phone. Also accept arrow keys,
  space, and swipe. Never trap the scroll.

## Non-negotiables

- **Everguard is the only name on it.** Never any other brand for this.
- Orange `#FF6A00` and `#CC4E00`. Black `#1A1A1A`, charcoal `#2E2E2E`, bone
  `#E6E6E6`. Orange is the accent and the vehicle, never a background wash.
- Headers **Orbitron Bold**, uppercase, wide letter spacing. Body **Montserrat
  Regular**. No third typeface.
- Thin orange line icons only. No filled icon sets, no emoji.
- **No Honolulu sunset heroes. No stock person holding a coffee cup. No
  palm-tree tropical framing. No "brighter tomorrows" as decoration.** The room
  is a cinematic black operations room. The only warmth on screen is the orange.
- No pricing, no tiers, no contact form, no fake testimonials, no fake logos of
  real companies.
- Everything self-contained: one page, no build step, no external libraries
  except the Google Fonts link. Generate the vehicle, the uniform, the map and
  the HUD as SVG and CSS rather than pulling stock photography.
- Respect `prefers-reduced-motion`: keep every beat and every control, replace
  the passes and parallax with cuts.
- It must work on a phone held vertically. That is how she will open it.

## What good looks like

Somebody opens it on their phone, the HUD boots, an orange RAV4 tears across
the screen, and they say "wait, that's my truck." Then they flip the lettering
themselves and see their own decision play back at them. That is the whole
point. Build for that ten seconds.

---

## Notes for Joey, not part of the prompt

- Claude Design will hand back a bundle. Send it over and it goes into
  `web/demo/` on this repo, wired to card 03 on the proposal page, behind the
  same access code.
- Keenan can take the same prompt to ChatGPT Astra afterwards. The style guide
  below is the thing to hand him so both passes stay on one rail.
