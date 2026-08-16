# Vertus — hotel website (alpha)

Static multi-page site for the Vertus hotel. Plain HTML/CSS/JS — no framework,
no CMS, no build step. Open `index.html` in a browser, or serve locally:

```bash
python3 -m http.server 8080
# then visit http://localhost:8080
```

## Status: alpha

Structure and flow are complete; real photography is wired in. What's still
placeholder:

- **Facts** — every unknown fact is wrapped in a `<span class="tbd">` and shows
  with a yellow highlight (address, rates, contacts, policies). Search the
  HTML for `class="tbd"` to find them all.
- **Map** — still a labelled SVG until the address arrives.
- **Room type names** — Classic / Deluxe / Suite are assumed from the photos;
  rename once the official list is confirmed.

Drop new originals into `incoming/` (gitignored) and re-run
`python3 tools/process_photos.py` to refresh the WebPs.

The yellow alpha banner and `.tbd` styling are removed at beta.

## Structure

| File | Job |
|---|---|
| `index.html` | Home — hero, proof strip, featured rooms, amenities, gallery teaser, location, CTA |
| `rooms.html` | Rooms & Suites — one section per room type (3 assumed) |
| `dining.html` | Dining & Amenities |
| `gallery.html` | Full photo grid with lightbox |
| `contact.html` | Contact, map placeholder, booking enquiry form (`#enquiry`) |
| `about.html` | Hotel story — merges into Home if content is thin |
| `css/style.css` | Single shared stylesheet, mobile-first |
| `js/main.js` | Nav toggle, lightbox, form stub, reveal-on-scroll |
| `tools/make_placeholders.py` | Regenerates the placeholder SVGs |

## Wired for later phases

- `schema.org/Hotel` JSON-LD on the home page (TBD fields marked)
- Unique title/description + OpenGraph tags per page
- `sitemap.xml` / `robots.txt` on `vertushotelandsuites.com`
- Enquiry form is UI-only; connects to Netlify Forms or Formspree at Live phase

## Waiting on (plan §6)

High-res photos (exterior/dusk, lobby, each room type, dining, amenities) and
the facts list (exact name, address, contacts, room types + rates, check-in/out
times, amenities, policies, logo/brand colours, tagline, proof points).
