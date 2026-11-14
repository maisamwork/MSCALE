# MSCALE Tools

Free online tools website — fast, private, no sign-up. Everything runs client-side in your browser.

**Live:** https://maisamwork.github.io/MSCALE/ (after GitHub Pages is enabled)

## What's inside

- **19 fully working tools** — calculators (percentage, BMI, age, loan/EMI), text tools (word counter, case converter, duplicate line remover, reverse text), developer tools (JSON formatter, Base64, URL encoder, UUID generator), converters (units, timestamps), password generator, color converter, random number generator, dice roller, coin flipper.
- **12 category pages** with 1,800+ catalogued tools from a 27,131-tool research catalog (`data/tools-catalog.xlsx`), marked "coming soon" until built.
- **Live search** across the whole catalog on the homepage.
- Pure static HTML/CSS/JS — no build step, no dependencies, no tracking.

## Structure

```
index.html            homepage (search + categories + live tools)
category/*.html       category pages (12)
tools/*.html          working tool pages (19)
assets/               style.css, app.js (search), tools.js (tool logic)
data/catalog.json     1,800 catalogued tools (name, category, subcategory)
data/tools-catalog.xlsx  full research catalog: 27,131 unique tools from 29 sites
gen.py                regenerates all pages from the templates in this file
```

## Run locally

```bash
python3 -m http.server 8080
# open http://localhost:8080
```

or just open `index.html` in a browser.

## Adding a new tool

1. Add the tool's HTML to `TOOL_BODIES` in `gen.py` and its logic to `assets/tools.js`.
2. Add its slug/name/description to the `LIVE` list in `gen.py`.
3. Run `python3 gen.py` and commit the generated pages.
