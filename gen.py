import json, os, re
from openpyxl import load_workbook

ROOT = os.path.dirname(os.path.abspath(__file__))
import sys as _sys
_sys.path.insert(0, ROOT)
from content import CONTENT
from content.blog import BLOG_POSTS
DATA_XLSX = "/workspace/tools-catalog.xlsx"

BRAND = 'MSCALE<span>Tools</span>'

ICONS = {
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "arrow-down-up": '<path d="m3 16 4 4 4-4"/><path d="M7 20V4"/><path d="m21 8-4-4-4 4"/><path d="M17 4v16"/>',
    "calculators": '<rect width="16" height="20" x="4" y="2" rx="2"/><line x1="8" x2="16" y1="6" y2="6"/><line x1="16" x2="16" y1="14" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/><path d="M12 14h.01"/><path d="M16 14h.01"/><path d="M8 18h.01"/><path d="M12 18h.01"/>',
    "text-tools": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/>',
    "developer-tools": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "converters": '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/>',
    "security": '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "color-tools": '<path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"/>',
    "random-generators": '<path d="M2 18h1.4c1.3 0 2.5-.6 3.3-1.7l6.1-8.6c.8-1.1 2-1.7 3.3-1.7H22"/><path d="m18 2 4 4-4 4"/><path d="M2 6h1.9c1.5 0 2.9.9 3.6 2.2"/><path d="M22 18h-5.9c-1.3 0-2.6-.7-3.3-1.8l-.5-.8"/><path d="m18 14 4 4-4 4"/>',
    "pdf-tools": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/>',
    "image-tools": '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>',
    "seo-web-tools": '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>',
    "date-time-tools": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "finance-tools": '<rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/>',
    "zap": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    "gauge": '<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
    "braces": '<path d="M8 3H7a2 2 0 0 0-2 2v5a2 2 0 0 1-2 2 2 2 0 0 1 2 2v5c0 1.1.9 2 2 2h1"/><path d="M16 21h1a2 2 0 0 0 2-2v-5c0-1.1.9-2 2-2a2 2 0 0 1-2-2V5a2 2 0 0 0-2-2h-1"/>',
    "smartphone": '<rect width="14" height="20" x="5" y="2" rx="2"/><path d="M12 18h.01"/>',
    "book-open": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    "shield-check": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1 1 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',    "menu": '<line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="18" y2="18"/>',
    "arrow-right": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>',
    "moon": '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>',
}

INTROS = {
    "calculators": "Free online calculators for everyday math: percentages, loans, discounts, tips and more. Every calculator runs instantly in your browser \u2014 nothing is sent to a server.",
    "text-tools": "Clean up, transform and analyze text: count words, convert case, remove duplicates, sort lines and more. Paste, click, copy \u2014 your text never leaves your device.",
    "developer-tools": "Format, encode, decode and inspect data like JSON, JWT and CSV. Built for developers who want fast results without uploads or accounts.",
    "converters": "Convert between units, number systems and time formats instantly \u2014 length, weight, data size, temperature, timestamps and more.",
    "security": "Generate strong passwords and compute hashes safely. Everything is generated locally with cryptographically secure randomness.",
    "color-tools": "Pick, convert and explore colors \u2014 HEX, RGB and HSL conversion plus palette generation for designers and developers.",
    "random-generators": "Random numbers, dice and coin flips powered by your browser\u2019s random engine \u2014 perfect for games, draws and decisions.",
    "pdf-tools": "Merge, split and convert PDF files right in your browser. Tools coming soon.",
    "image-tools": "Resize, convert and optimize images without uploading them anywhere \u2014 processing happens on your own device.",
    "seo-web-tools": "Analyze and improve your website: meta tags, keywords and more. Tools coming soon.",
    "date-time-tools": "Work with dates and time \u2014 differences, timestamps and converters.",
    "finance-tools": "Practical finance calculators for loans, interest and taxes \u2014 clear results, no spreadsheets.",
}

def svg_icon(cat, cls="", color=None):
    style = f' style="color:{color}"' if color else ""
    return ('<svg class="' + cls + '"' + style + ' viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            + ICONS.get(cat, ICONS["wrench"]) + "</svg>")


CAT_HUES = {
    "calculators": "#ff9a3c", "text-tools": "#4cc3ff", "developer-tools": "#a78bfa",
    "converters": "#2dd4bf", "security": "#34d399", "color-tools": "#f472b6",
    "random-generators": "#fbbf24", "pdf-tools": "#f87171", "image-tools": "#e879f9",
    "seo-web-tools": "#22d3ee", "date-time-tools": "#60a5fa", "finance-tools": "#10b981",
    "wrench": "#ff7000",
}


def hue_of(cat_slug):
    return CAT_HUES.get(cat_slug, "#ff7000")
LIVE = [
    ("percentage-calculator", "Percentage Calculator", "Calculators", "Percent of a number, percentage change and more"),
    ("bmi-calculator", "BMI Calculator", "Calculators", "Body Mass Index with weight category"),
    ("age-calculator", "Age Calculator", "Calculators", "Exact age in years, months and days"),
    ("loan-emi-calculator", "Loan / EMI Calculator", "Calculators", "Monthly payment, total interest and total cost"),
    ("discount-calculator", "Discount Calculator", "Calculators", "Sale price, savings and final price with tax"),
    ("tip-calculator", "Tip Calculator", "Calculators", "Tip amount, total and per-person split"),
    ("word-counter", "Word Counter", "Text Tools", "Words, characters, sentences and reading time"),
    ("case-converter", "Case Converter", "Text Tools", "UPPER, lower, Title, camelCase, snake_case, kebab"),
    ("remove-duplicate-lines", "Remove Duplicate Lines", "Text Tools", "Deduplicate text lines, with case and trim options"),
    ("reverse-text", "Reverse Text", "Text Tools", "Reverse characters, words or lines"),
    ("find-and-replace", "Find and Replace", "Text Tools", "Replace text with case and regex options"),
    ("text-sorter", "Line Sorter", "Text Tools", "Sort lines A-Z, Z-A, by length or shuffle"),
    ("lorem-ipsum-generator", "Lorem Ipsum Generator", "Text Tools", "Placeholder text by paragraphs and sentences"),
    ("word-frequency-counter", "Word Frequency Counter", "Text Tools", "Top words with visual frequency bars"),
    ("json-formatter", "JSON Formatter", "Developer Tools", "Beautify, validate and minify JSON"),
    ("base64-encoder-decoder", "Base64 Encode / Decode", "Developer Tools", "UTF-8 safe Base64 conversion"),
    ("url-encoder-decoder", "URL Encoder / Decoder", "Developer Tools", "Percent-encode or decode URLs and text"),
    ("uuid-generator", "UUID Generator", "Developer Tools", "Generate v4 UUIDs in bulk"),
    ("hash-generator", "Hash Generator", "Developer Tools", "SHA-1, SHA-256 and SHA-512 hashes instantly"),
    ("jwt-decoder", "JWT Decoder", "Developer Tools", "Decode JWT header and payload, check expiry"),
    ("regex-tester", "Regex Tester", "Developer Tools", "Test regular expressions with live highlighting"),
    ("csv-to-json-converter", "CSV to JSON Converter", "Developer Tools", "Convert CSV or TSV to JSON, quote-aware"),
    ("html-encoder-decoder", "HTML Encoder / Decoder", "Developer Tools", "Escape or unescape HTML entities"),
    ("json-to-csv-converter", "JSON to CSV Converter", "Developer Tools", "Turn a JSON array into a clean CSV for spreadsheets"),
    ("unit-converter", "Unit Converter", "Converters", "Length, weight, data size and temperature"),
    ("timestamp-converter", "Timestamp Converter", "Converters", "Unix timestamp to date and back, live clock"),
    ("number-base-converter", "Number Base Converter", "Converters", "Binary, octal, decimal and hexadecimal"),
    ("roman-numeral-converter", "Roman Numeral Converter", "Converters", "Roman numerals to numbers and back"),
    ("password-generator", "Password Generator", "Security Tools", "Strong random passwords with entropy estimate"),
    ("color-converter", "Color Converter", "Color Tools", "HEX to RGB to HSL with live preview"),
    ("palette-generator", "Color Palette Generator", "Color Tools", "Shades and tints from any color, click to copy"),
    ("random-number-generator", "Random Number Generator", "Random Generators", "Random numbers in any range, unique option"),
    ("dice-roller", "Dice Roller", "Random Generators", "Roll up to 20 dice with any number of sides"),
    ("coin-flipper", "Coin Flipper", "Random Generators", "Flip one coin or a thousand, with counts"),
    ("pdf-merge", "PDF Merge", "PDF Tools", "Combine multiple PDFs into one, right in your browser"),
    ("pdf-split", "PDF Split", "PDF Tools", "Extract pages or ranges into a new PDF"),
    ("image-resizer", "Image Resizer", "Image Tools", "Resize and convert images in your browser"),
    ("image-compressor", "Image Compressor", "Image Tools", "Shrink JPG, PNG and WebP with a quality slider"),
    ("image-cropper", "Image Cropper", "Image Tools", "Crop images to exact pixels, locally and privately"),
    ("meta-tag-generator", "Meta Tag Generator", "SEO & Web Tools", "Full meta, Open Graph and Twitter tags with live previews"),
    ("keyword-density-checker", "Keyword Density Checker", "SEO & Web Tools", "One, two and three-word phrase density analysis"),
    ("xml-sitemap-generator", "XML Sitemap Generator", "SEO & Web Tools", "Build a valid sitemap.xml from your URL list"),
    ("slug-generator", "Slug Generator", "SEO & Web Tools", "Turn titles into clean URL slugs, with batch mode"),
    ("date-difference-calculator", "Date Difference Calculator", "Date & Time Tools", "Days, weeks, months and years between dates"),
    ("compound-interest-calculator", "Compound Interest Calculator", "Finance & Business", "Future value with contributions and compounding"),
    ("gst-vat-calculator", "GST / VAT Calculator", "Finance & Business", "Add or remove sales tax from any amount"),
    ("invoice-generator", "Invoice Generator", "Finance & Business", "Professional invoices with line items, tax and print to PDF"),
    ("qr-code-generator", "QR Code Generator", "Developer Tools", "Generate QR codes for links, text and Wi-Fi with size and error-correction control"),
    ("text-diff-checker", "Text Diff Checker", "Text Tools", "Compare two texts line by line with additions and removals highlighted"),
    ("markdown-previewer", "Markdown Previewer", "Developer Tools", "Render markdown live with copy-ready HTML output"),
    ("image-watermarker", "Image Watermarker", "Image Tools", "Stamp text watermarks with position, size and opacity control"),
    ("favicon-generator", "Favicon Generator", "Image Tools", "Create the full favicon size set from any logo, with link tags"),
    ("base64-image-encoder", "Base64 Image Encoder", "Developer Tools", "Convert images to data URIs with HTML and CSS snippets"),
    ("stopwatch-online", "Online Stopwatch", "Date & Time Tools", "Precise stopwatch with laps, splits and pause/resume"),
    ("countdown-timer", "Countdown Timer", "Date & Time Tools", "Live countdown to any date with progress bar"),
    ("password-strength-checker", "Password Strength Checker", "Security Tools", "Entropy, crack-time estimate and a fix-it checklist for any password"),
    ("cron-expression-explainer", "Cron Expression Explainer", "Developer Tools", "Translate cron schedules to plain English and see the next run times"),
    ("css-gradient-generator", "CSS Gradient Generator", "Color Tools", "Design linear gradients live with angle and colour control, copy-ready CSS"),
    ("box-shadow-generator", "Box Shadow Generator", "Color Tools", "Tune offset, blur, spread and colour with a live preview and copy-ready CSS"),
    ("text-to-speech", "Text to Speech", "Text Tools", "Read any text aloud with your device's voices, speed and pitch control"),
    ("typing-speed-test", "Typing Speed Test", "Text Tools", "Measure your words per minute and accuracy with a fresh word stream"),
    ("pomodoro-timer", "Pomodoro Timer", "Date & Time Tools", "Automatic 25/5 focus cycles with long breaks and a session counter"),
    ("url-parser", "URL Parser", "Developer Tools", "Break any URL into scheme, host, path, params and fragment"),
]

CAT_PAGES = {
    "calculators": ("Calculators", "\U0001F9EE", ["percentage-calculator", "bmi-calculator", "age-calculator", "loan-emi-calculator", "discount-calculator", "tip-calculator"], "Calculators"),
    "text-tools": ("Text Tools", "\U0001F4DD", ["word-counter", "case-converter", "remove-duplicate-lines", "reverse-text", "find-and-replace", "text-sorter", "lorem-ipsum-generator", "word-frequency-counter", "text-diff-checker", "text-to-speech", "typing-speed-test"], "Text Tools"),
    "developer-tools": ("Developer Tools", "\U0001F4BB", ["json-formatter", "base64-encoder-decoder", "url-encoder-decoder", "uuid-generator", "hash-generator", "jwt-decoder", "regex-tester", "csv-to-json-converter", "html-encoder-decoder", "json-to-csv-converter", "qr-code-generator", "markdown-previewer", "base64-image-encoder", "cron-expression-explainer", "url-parser"], "Developer Tools"),
    "converters": ("Converters", "\U0001F504", ["unit-converter", "timestamp-converter", "number-base-converter", "roman-numeral-converter"], "Converters (Units & Numbers)"),
    "security": ("Security Tools", "\U0001F512", ["password-generator", "password-strength-checker"], "Security & Encoding"),
    "color-tools": ("Color Tools", "\U0001F3A8", ["color-converter", "palette-generator", "css-gradient-generator", "box-shadow-generator"], "Color & Design Tools"),
    "random-generators": ("Random Generators", "\U0001F3B2", ["random-number-generator", "dice-roller", "coin-flipper"], "Random & Fun Generators"),
    "pdf-tools": ("PDF Tools", "\U0001F4C4", ["pdf-merge", "pdf-split"], "PDF Tools"),
    "image-tools": ("Image Tools", "\U0001F5BC\uFE0F", ["image-resizer", "image-compressor", "image-cropper", "image-watermarker", "favicon-generator"], "Image Tools"),
    "seo-web-tools": ("SEO & Web Tools", "\U0001F4C8", ["meta-tag-generator", "keyword-density-checker", "xml-sitemap-generator", "slug-generator"], "SEO & Web Tools"),
    "date-time-tools": ("Date & Time Tools", "\U0001F550", ["date-difference-calculator", "stopwatch-online", "countdown-timer", "pomodoro-timer"], "Date & Time Tools"),
    "finance-tools": ("Finance & Business", "\U0001F4B0", ["compound-interest-calculator", "gst-vat-calculator", "invoice-generator"], "Finance & Business"),
}

CATALOG_CATS = {
    "Calculators": "calculators",
    "Text Tools": "text-tools",
    "Developer Tools": "developer-tools",
    "Converters (Units & Numbers)": "converters",
    "Security & Encoding": "security",
    "Color & Design Tools": "color-tools",
    "Random & Fun Generators": "random-generators",
    "PDF Tools": "pdf-tools",
    "Image Tools": "image-tools",
    "SEO & Web Tools": "seo-web-tools",
    "Date & Time Tools": "date-time-tools",
    "Finance & Business": "finance-tools",
}

CAT_SLUG_BY_NAME = {v[0] if isinstance(v, tuple) else v: k for k, v in CAT_PAGES.items()}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def header(title, desc, depth="", extra_head="", og_image="", robots="", canonical=""):
    CHEV_D = '<svg class="dd-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>'
    cat_counts = {}
    for s, _, c, _ in LIVE:
        cs = CAT_SLUG_BY_NAME.get(c, "calculators")
        cat_counts[cs] = cat_counts.get(cs, 0) + 1
    mega_items = "".join(
        f"<a class='mega-item' href='{depth}{slug}/'><span class='icon-box' style='color:{hue_of(slug)};background:{hue_of(slug)}22'>{svg_icon(slug)}</span>"
        f"<span class='mega-txt'><b>{CAT_PAGES[slug][0]}</b><em>{cat_counts.get(slug, 0)} live tools</em></span></a>"
        for slug in CAT_PAGES
    )
    mega = (f"<div class='mega' role='menu' aria-label='Tool categories'><div class='mega-grid'>{mega_items}</div>"
            f"<div class='mega-foot'><span>{len(LIVE)} tools live &mdash; no sign-up, runs in your browser</span>"
            f"<a href='{depth}tools/'>Browse everything {svg_icon('arrow-right')}</a></div></div>")
    nav = (f'<a href="{depth}index.html">Home</a>'
           f'<div class="nav-dd"><a class="dd-top" href="{depth}tools/">Free Tools {CHEV_D}</a>{mega}</div>'
           f'<a href="{depth}blog/">Blog</a>')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}"/>
<link rel="icon" href="{depth}assets/favicon.svg" type="image/svg+xml"/>
<meta property="og:title" content="{esc(title)}"/>
<meta property="og:description" content="{esc(desc)}"/>
<meta property="og:type" content="website"/>
<meta property="og:site_name" content="MSCALE Tools"/>
<meta name="twitter:card" content="summary"/>
{f'<link rel="canonical" href="{canonical}"/>' if canonical else ''}
{f'<meta name="robots" content="{robots}"/>' if robots else ''}
{f'<meta property="og:image" content="{og_image}"/>' if og_image else ''}
{extra_head}
<script>document.documentElement.setAttribute("data-theme", (function(){{try{{return localStorage.getItem("mscale-theme")||"dark"}}catch(e){{return "dark"}}}})());</script>
<link rel="stylesheet" href="{depth}assets/style.css"/>
<script src="{depth}assets/live-tools.js" defer></script>
<script src="{depth}assets/app.js" defer></script>
<script src="{depth}assets/tools.js" defer></script>
</head>
<body>
<header class="site"><div class="container">
  <a class="brand" href="{depth}index.html"><span class="brand-tile">{svg_icon("wrench")}</span>MSCALE<span>Tools</span></a>
  <nav class="main" id="main-nav">{nav}<a class="nav-cta" href="{depth}tools/">All tools</a></nav>
  <div class="nav-actions">
    <button class="theme-toggle" id="theme-toggle" aria-label="Toggle dark or light theme">{svg_icon("sun", "ic-sun")}{svg_icon("moon", "ic-moon")}</button>
    <button class="nav-toggle" id="nav-toggle" aria-label="Open menu" aria-expanded="false">{svg_icon("menu")}</button>
  </div>
</div></header>
<main class="container">"""


def footer(depth):
    names_by_slug = {s: n for s, n, _, _ in LIVE}
    half = (len(CAT_PAGES) + 1) // 2
    slugs = list(CAT_PAGES.keys())
    cats1 = "".join(f'<a href="{depth}{slug}/">{CAT_PAGES[slug][0]}</a>' for slug in slugs[:half])
    cats2 = "".join(f'<a href="{depth}{slug}/">{CAT_PAGES[slug][0]}</a>' for slug in slugs[half:])
    popular = ["percentage-calculator", "word-counter", "json-formatter", "password-generator",
               "unit-converter", "image-resizer"]
    pop = "".join(f'<a href="{depth}tools/{s}.html">{names_by_slug[s]}</a>' for s in popular)
    return f"""</main>
<footer class="site"><div class="container">
  <div class="footer-grid">
    <div class="footer-brand">
      <a class="brand" href="{depth}index.html"><span class="brand-tile">{svg_icon("wrench")}</span>MSCALE<span>Tools</span></a>
      <p>Free online tools that run entirely in your browser \u2014 fast, private, no sign-up, no uploads. {len(LIVE)} tools live, more shipping weekly.</p>
      <a class="gh-link" href="https://github.com/maisamwork/MSCALE">{svg_icon("developer-tools", "", "#e6e9f0")}<span>github.com/maisamwork/MSCALE</span></a>
    </div>
    <div>
      <h4>Categories</h4>
      {cats1}
    </div>
    <div>
      <h4>&nbsp;</h4>
      {cats2}
    </div>
    <div>
      <h4>Popular tools</h4>
      {pop}
      <h4 class="gap-top">Resources</h4>
      <a href="{depth}blog/">Blog</a>
      <a href="{depth}tools/">All tools</a>
    </div>
  </div>
  <p class="copyright">&copy; 2026 MSCALE Tools. Every tool runs client-side in your browser \u2014 your data never leaves your device.</p>
</div></footer>
</body>
</html>"""


TOOL_BODIES = {

"password-strength-checker": """
<div class="panel">
  <label>Password to analyse</label>
  <div class="pw2-row">
    <input type="text" id="pw-in" oninput="pwCheck()" placeholder="Type a test password — nothing is sent anywhere" autocomplete="off">
    <button class="btn ghost" onclick="pw2Mask(this)">Hide</button>
  </div>
  <div class="pw-meter"><div id="pw-fill"></div></div>
  <div id="pw-stats" class="stat-row"></div>
  <label>Requirements</label>
  <div id="pw2-checks" class="pw2-checks"></div>
  <div id="pw-out" class="result"></div>
</div>
""",
"cron-expression-explainer": """
<div class="panel">
  <label>Quick presets</label>
  <div class="ir2-presets">
    <button type="button" class="ir2-preset" onclick="cr2Pre('* * * * *')">Every minute</button>
    <button type="button" class="ir2-preset" onclick="cr2Pre('*/15 * * * *')">Every 15 min</button>
    <button type="button" class="ir2-preset" onclick="cr2Pre('30 * * * *')">Hourly at :30</button>
    <button type="button" class="ir2-preset" onclick="cr2Pre('0 0 * * *')">Daily midnight</button>
    <button type="button" class="ir2-preset" onclick="cr2Pre('0 9 * * 1-5')">Weekdays 9 am</button>
    <button type="button" class="ir2-preset" onclick="cr2Pre('0 */6 * * *')">Every 6 hours</button>
    <button type="button" class="ir2-preset" onclick="cr2Pre('0 0 1 * *')">Monthly on the 1st</button>
    <button type="button" class="ir2-preset" onclick="cr2Pre('0 12 * * 6,0')">Weekends noon</button>
  </div>
  <label>Cron expression (5 fields)</label>
  <input id="cr-in" oninput="cronExplain()" placeholder="*/15 9-17 * * 1-5" autocomplete="off">
  <div id="cr2-sum" class="jf-stats" style="margin:10px 0"></div>
  <div id="cr-out" class="result"></div>
  <label>Next 5 runs (your local time)</label>
  <div id="cr-next" class="result"></div>
  <div class="row">
    <button class="btn ghost" onclick="copyText(document.getElementById('cr-in').value, this)">Copy expression</button>
  </div>
</div>
""",
"css-gradient-generator": """
<div class="panel">
  <label>Gradient type</label>
  <div class="lr2-types">
    <button type="button" class="lr2-type active" onclick="cg2Type(0,this)">Linear</button>
    <button type="button" class="lr2-type" onclick="cg2Type(1,this)">Radial</button>
    <button type="button" class="lr2-type" onclick="cg2Type(2,this)">Conic</button>
  </div>
  <label>Colour stops</label>
  <div id="cg2-stops"></div>
  <button class="btn ghost" onclick="cg2AddStop()">+ Add stop</button>
  <div id="cg2-ang-wrap" class="row" style="margin-top:12px">
    <div style="flex:1"><label>Angle: <span id="gr-angv">135</span>°</label><input type="range" id="gr-ang" min="0" max="360" value="135" oninput="grDraw()"></div>
  </div>
  <label>Presets</label>
  <div class="ir2-presets">
    <button type="button" class="ir2-preset" onclick="cg2Set(['#ff512f','#dd2476'],180)">Sunset</button>
    <button type="button" class="ir2-preset" onclick="cg2Set(['#2193b0','#6dd5ed'],90)">Ocean</button>
    <button type="button" class="ir2-preset" onclick="cg2Set(['#ff7000','#7c3aed'],135)">Ember</button>
    <button type="button" class="ir2-preset" onclick="cg2Set(['#00b09b','#96c93d'],120)">Mint</button>
    <button type="button" class="ir2-preset" onclick="cg2Set(['#ffecd2','#fcb69f'],45)">Peach</button>
    <button type="button" class="ir2-preset" onclick="cg2Set(['#e53935','#e35d5b','#f6d365'],110)">Volcano</button>
  </div>
  <div id="gr-prev" class="gr-prev"></div>
  <label>CSS</label>
  <textarea id="gr-out" readonly style="min-height:80px"></textarea>
  <div class="row">
    <button class="btn ghost" onclick="copyText(document.getElementById('gr-out').value, this)">Copy CSS</button>
    <button class="btn ghost" onclick="cg2Tail(this)">Copy Tailwind class</button>
    <button class="btn ghost" onclick="cg2Random()">Randomise</button>
  </div>
</div>
""",
"box-shadow-generator": """
<div class="panel">
  <label>Quick presets</label>
  <div class="ir2-presets">
    <button type="button" class="ir2-preset" onclick="bs2Pre(0,1,2,0,'#0f172a',10,0)">Subtle</button>
    <button type="button" class="ir2-preset" onclick="bs2Pre(0,4,12,-2,'#0f172a',18,0)">Card</button>
    <button type="button" class="ir2-preset" onclick="bs2Pre(0,18,40,-12,'#0f172a',25,0)">Floating</button>
    <button type="button" class="ir2-preset" onclick="bs2Pre(0,0,24,4,'#7c3aed',45,0)">Glow</button>
    <button type="button" class="ir2-preset" onclick="bs2Pre(6,6,0,0,'#111827',100,0)">Hard</button>
    <button type="button" class="ir2-preset" onclick="bs2Pre(0,2,6,0,'#0f172a',25,1)">Inset panel</button>
  </div>
  <label>Preview</label>
  <div class="bs-prev"><div id="bs-box"></div></div>
  <div class="row">
    <div><label>X offset: <span id="bs-xv">0</span>px</label><input type="range" id="bs-x" min="-40" max="40" value="0" oninput="bsDraw()"></div>
    <div><label>Y offset: <span id="bs-yv">10</span>px</label><input type="range" id="bs-y" min="-40" max="40" value="10" oninput="bsDraw()"></div>
  </div>
  <div class="row">
    <div><label>Blur: <span id="bs-blv">30</span>px</label><input type="range" id="bs-bl" min="0" max="100" value="30" oninput="bsDraw()"></div>
    <div><label>Spread: <span id="bs-spv">-8</span>px</label><input type="range" id="bs-sp" min="-30" max="40" value="-8" oninput="bsDraw()"></div>
  </div>
  <div class="row">
    <div><label>Shadow colour</label><input type="color" id="bs-color" value="#0f172a" oninput="bsDraw()"></div>
    <div><label>Opacity: <span id="bs-opv">55</span>%</label><input type="range" id="bs-op" min="0" max="100" value="55" oninput="bsDraw()"></div>
  </div>
  <label class="pg-switch"><input type="checkbox" id="bs-inset" onchange="bsDraw()"><span class="pg-track"></span> Inset shadow</label>
  <label>CSS</label>
  <textarea id="bs-out" readonly style="min-height:80px"></textarea>
  <div class="row">
    <button class="btn ghost" onclick="copyText(document.getElementById('bs-out').value, this)">Copy CSS</button>
  </div>
</div>
""",
"text-to-speech": """
<div class="panel">
  <label>Text to read aloud</label>
  <textarea id="tts-in" oninput="ttsStats()" placeholder="Type or paste anything&hellip;">MSCALE Tools runs entirely in your browser. Your text never leaves this page.</textarea>
  <div class="jf-stats" id="tts-stats"></div>
  <div class="row">
    <div><label>Voice</label><select id="tts-voice" onchange="ttsStats()"></select></div>
    <div><label>Speed: <span id="tts-ratev">1</span>&times;</label><input type="range" id="tts-rate" min="0.5" max="2" step="0.1" value="1" class="pg-slider" oninput="document.getElementById('tts-ratev').textContent=this.value; ttsStats()"></div>
    <div><label>Pitch: <span id="tts-pitchv">1</span></label><input type="range" id="tts-pitch" min="0.5" max="2" step="0.1" value="1" class="pg-slider" oninput="document.getElementById('tts-pitchv').textContent=this.value"></div>
  </div>
  <div class="row" style="margin-top:12px">
    <button class="btn" onclick="ttsPlay()">Speak</button>
    <button class="btn ghost" onclick="ttsPause()" id="tts-pause">Pause</button>
    <button class="btn ghost" onclick="ttsStop()">Stop</button>
    <button class="btn ghost" onclick="ttsSample()">Sample text</button>
  </div>
  <div id="tts-msg" class="result"></div>
</div>""",

"typing-speed-test": """
<div class="panel ty2">
  <div class="ty2-bar">
    <div class="ty2-durs">
      <button class="ty2-dur" data-sec="15" onclick="ty2Dur(15, this)">15s</button>
      <button class="ty2-dur active" data-sec="30" onclick="ty2Dur(30, this)">30s</button>
      <button class="ty2-dur" data-sec="60" onclick="ty2Dur(60, this)">60s</button>
    </div>
    <div class="ty2-timer" id="ty2-timer">30.0</div>
    <button class="btn ghost sm" onclick="ty2New()">[[ic zap]] Restart</button>
  </div>
  <div id="ty-words" class="ty-words ty2-words"></div>
  <input id="ty-in" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Click here and start typing&hellip;" oninput="tyInput()">
  <div id="ty2-live" class="ty2-live"></div>
  <div id="ty-stats" class="stat-row"></div>
  <p class="tool-note" id="ty2-best"></p>
</div>""",

"pomodoro-timer": """
<div class="panel">
  <div class="lr2-types">
    <button class="lr2-type active" onclick="poShow('focus', this)">Focus</button>
    <button class="lr2-type" onclick="poShow('short', this)">Short break</button>
    <button class="lr2-type" onclick="poShow('long', this)">Long break</button>
  </div>
  <div class="row" style="margin-top:12px">
    <div><label>Focus (min)</label><input type="number" id="po-focus-len" value="25" min="1" max="90" onchange="poSetLen()" /></div>
    <div><label>Short break (min)</label><input type="number" id="po-short-len" value="5" min="1" max="30" onchange="poSetLen()" /></div>
    <div><label>Long break (min)</label><input type="number" id="po-long-len" value="15" min="1" max="60" onchange="poSetLen()" /></div>
  </div>
  <div id="po-mode" class="tool-note" style="text-align:center">Focus session</div>
  <div id="po-display" class="big-time">25:00</div>
  <div class="wc-bar" style="margin:10px auto 4px;max-width:420px"><div class="wc-bar-fill" id="po-prog" style="width:0%"></div></div>
  <div class="row" style="margin-top:12px">
    <button class="btn" id="po-start" onclick="poToggle()">Start</button>
    <button class="btn ghost" onclick="poSkip()">Skip</button>
    <button class="btn ghost" onclick="poReset()">Reset</button>
    <label class="pg-switch" style="margin-left:auto"><input type="checkbox" id="po-sound" checked onchange="" /><span class="pg-track"></span> Sound</label>
  </div>
  <div id="po-count" class="result">Completed focus sessions: 0</div>
  <div class="jf-stats" id="po-dots" style="justify-content:center;margin-top:10px"></div>
</div>""",

"url-parser": """
<div class="panel up2">
  <label>URL to parse &mdash; updates live</label>
  <input id="up-in" oninput="urlParse()" value="https://user:pass@sub.example.com:8080/path/page?q=hello world&lang=en#section" autocomplete="off">
  <div class="jf-stats" id="up2-stats"></div>
  <div id="up-out" class="result" style="overflow:auto"></div>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="up2CopyJson(this)">Copy as JSON</button>
  </div>
</div>""",


"qr-code-generator": """
<div class="panel qr2">
  <div class="pg-tabs qr2-tabs">
    <button class="pg-tab active" onclick="qr2Type('text', this)">Text / URL</button>
    <button class="pg-tab" onclick="qr2Type('wifi', this)">WiFi</button>
    <button class="pg-tab" onclick="qr2Type('email', this)">Email</button>
    <button class="pg-tab" onclick="qr2Type('phone', this)">Phone</button>
    <button class="pg-tab" onclick="qr2Type('sms', this)">SMS</button>
  </div>
  <div id="qr2-fields"></div>
  <div class="qr2-opts">
    <div class="row">
      <div><label>Size</label>
        <select id="qr-size"><option value="200">200 px</option><option value="300" selected>300 px</option><option value="400">400 px</option><option value="500">500 px</option><option value="600">600 px</option></select></div>
      <div><label>Error correction</label>
        <select id="qr-ecc"><option value="L">L \u2014 smallest</option><option value="M" selected>M \u2014 balanced</option><option value="Q">Q \u2014 robust</option><option value="H">H \u2014 most robust</option></select></div>
      <div><label>Quiet zone</label>
        <select id="qr-margin"><option value="0">None</option><option value="4" selected>Standard (4)</option><option value="8">Wide (8)</option></select></div>
    </div>
    <div class="row qr2-colors">
      <div><label>Foreground</label><input type="color" id="qr-fg" value="#111827" oninput="qr2Gen()" /></div>
      <div><label>Background</label><input type="color" id="qr-bg" value="#ffffff" oninput="qr2Gen()" /></div>
    </div>
  </div>
  <div class="qr2-preview">
    <div id="qr-box" class="qr-box"></div>
    <p class="tool-note" id="qr2-status"></p>
    <div class="qr2-dl">
      <button class="btn" onclick="qr2Download()">Download PNG</button>
      <button class="btn ghost" onclick="qr2CopyData(this)">Copy QR data</button>
    </div>
  </div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>""",

"text-diff-checker": """
<div class="panel df2">
  <div class="row">
    <div style="flex:1;min-width:240px"><label>Original text</label>
      <textarea id="diff-a" oninput="df2Live()" style="min-height:170px" placeholder="Paste the original version\u2026"></textarea></div>
    <div style="flex:1;min-width:240px"><label>Changed text</label>
      <textarea id="diff-b" oninput="df2Live()" style="min-height:170px" placeholder="Paste the changed version\u2026"></textarea></div>
  </div>
  <div class="df2-opts">
    <div class="df2-modes">
      <button class="df2-mode active" id="df2-m-lines" onclick="df2SetMode('lines', this)">Line diff</button>
      <button class="df2-mode" id="df2-m-words" onclick="df2SetMode('words', this)">Word diff</button>
    </div>
    <label class="pg-switch"><input type="checkbox" id="df2-case" onchange="df2Run()" /><span class="pg-track"></span> Ignore case</label>
    <label class="pg-switch"><input type="checkbox" id="df2-ws" onchange="df2Run()" /><span class="pg-track"></span> Ignore extra whitespace</label>
  </div>
  <div class="df2-stats" id="df2-stats"></div>
  <div class="df2-sim"><div class="df2-sim-fill" id="df2-sim"></div></div>
  <div class="df2-legend"><span class="df2-l-add">+ added</span><span class="df2-l-del">&minus; removed</span><span class="df2-l-same">= unchanged</span></div>
  <div id="diff-out" class="diff-out df2-out"></div>
</div>""",

"markdown-previewer": """
<div class="panel">
  <label>View</label>
  <div class="lr2-types">
    <button type="button" class="lr2-type active" onclick="md2View(0,this)">Live preview</button>
    <button type="button" class="lr2-type" onclick="md2View(1,this)">HTML source</button>
  </div>
  <label>Insert at cursor</label>
  <div class="ir2-presets">
    <button type="button" class="ir2-preset" onclick="md2Wrap('**','**')">Bold</button>
    <button type="button" class="ir2-preset" onclick="md2Wrap('*','*')">Italic</button>
    <button type="button" class="ir2-preset" onclick="md2Wrap('`','`')">Code</button>
    <button type="button" class="ir2-preset" onclick="md2Wrap('[',' ](https://)')">Link</button>
    <button type="button" class="ir2-preset" onclick="md2Line('## ')">H2</button>
    <button type="button" class="ir2-preset" onclick="md2Line('- ')">Bullet</button>
    <button type="button" class="ir2-preset" onclick="md2Line('1. ')">Numbered</button>
    <button type="button" class="ir2-preset" onclick="md2Line('&gt; ')">Quote</button>
  </div>
  <div class="row">
    <div style="flex:1;min-width:240px"><label>Markdown input</label>
      <textarea id="md-in" oninput="mdRender();md2Stats()" style="min-height:280px" placeholder="# Heading&#10;&#10;Some **bold** and *italic* text with a [link](https://example.com)."></textarea></div>
    <div id="md2-prev-col" style="flex:1;min-width:240px"><label>Live preview</label>
      <div id="md-out" class="md-out"></div></div>
  </div>
  <div id="md2-stats" class="jf-stats" style="margin:12px 0"></div>
  <label>HTML source</label>
  <textarea id="md-html" readonly style="display:none;min-height:280px"></textarea>
  <div class="row">
    <button class="btn ghost" onclick="copyText('md-html')">Copy generated HTML</button>
    <button class="btn ghost" onclick="md2Download()">Download .html</button>
    <button class="btn ghost" onclick="md2Sample()">Sample</button>
    <button class="btn ghost" onclick="md2Clear()">Clear</button>
  </div>
</div>
""",
"image-watermarker": """
<div class="panel">
  <label>Choose an image</label>
  <input type="file" id="wm-file" accept="image/*" onchange="wmLoad()">
  <label>Watermark text</label>
  <input id="wm-text" value="\u00a9 Your Name" oninput="wmDraw()">
  <div class="row">
    <div><label>Position</label>
      <select id="wm-pos" onchange="wmDraw()">
        <option value="tl">Top left</option><option value="tc">Top center</option><option value="tr">Top right</option>
        <option value="ml">Middle left</option><option value="mc">Middle center</option><option value="mr">Middle right</option>
        <option value="bl">Bottom left</option><option value="bc">Bottom center</option><option value="br" selected>Bottom right</option>
      </select></div>
    <div><label>Size (%)</label><input type="number" id="wm-size" value="4" min="1" max="20" oninput="wmDraw()"></div>
  </div>
  <div class="row">
    <div><label>Opacity: <span id="wm-opv">35</span>%</label>
      <input type="range" id="wm-opacity" min="5" max="100" value="35" oninput="wmDraw()"></div>
    <div><label>Color</label><input type="color" id="wm-color" value="#ffffff" oninput="wmDraw()"></div>
  </div>
  <canvas id="wm-canvas" style="max-width:100%;border-radius:var(--r-md)"></canvas>
  <button class="btn" onclick="wmSave()">Download watermarked image</button>
</div>""",
"favicon-generator": """
<div class="panel">
  <label>Logo image (PNG, JPG, SVG or WebP)</label>
  <input type="file" id="fv-file" accept="image/*" onchange="fvGen()">
  <div class="row">
    <div><label>Background fill (used where the logo is transparent)</label><input type="color" id="fv-bg" value="#ffffff" oninput="fv2Redraw()"></div>
    <div class="fv2-tab-prev">
      <div class="fv2-tabshot"><img id="fv-tab" alt="Favicon preview at 32 px"><em>How it looks in a browser tab</em></div>
    </div>
  </div>
  <label>Generated sizes — download each and keep the file name</label>
  <div id="fv-previews" class="fv2-grid"></div>
  <label>Install snippets</label>
  <div class="uc2-cats jf-w100">
    <button type="button" class="uc2-cat active" onclick="fv2Tab(0,this)">HTML head tags</button>
    <button type="button" class="uc2-cat" onclick="fv2Tab(1,this)">site.webmanifest</button>
    <button type="button" class="uc2-cat" onclick="fv2Tab(2,this)">browserconfig.xml</button>
  </div>
  <textarea id="fv-tags" readonly style="min-height:170px"></textarea>
  <div class="row">
    <button class="btn ghost" onclick="copyText(document.getElementById('fv-tags').value, this)">Copy snippet</button>
  </div>
</div>
""",
"base64-image-encoder": """
<div class="panel">
  <div class="bi2-drop" id="bi2-drop" ondragover="bi2Drag(event)" ondragleave="bi2Undrag(event)" ondrop="bi2Drop(event)">
    <b>Drop an image here</b>
    <span>or</span>
    <label class="btn" style="margin:0">Choose file<input type="file" id="b64-file" accept="image/*" onchange="b64Enc()" style="display:none"></label>
  </div>
  <div class="row" style="align-items:flex-start">
    <div class="bi2-prev"><img id="bi2-img" alt="Preview of the uploaded image"></div>
    <div id="b64-info" class="jf-stats" style="margin:0;flex:1"></div>
  </div>
  <div id="bi2-warn" class="result"></div>
  <label>Data URI</label>
  <textarea id="b64-out" readonly style="min-height:120px"></textarea>
  <div class="row" style="flex-wrap:wrap">
    <button class="btn ghost" onclick="copyText('b64-out')">Copy data URI</button>
    <button class="btn ghost" onclick="copyText('b64-html')">Copy HTML img tag</button>
    <button class="btn ghost" onclick="copyText('b64-css')">Copy CSS background</button>
    <button class="btn ghost" onclick="bi2Txt()">Download .txt</button>
  </div>
  <textarea id="b64-html" style="display:none"></textarea>
  <textarea id="b64-css" style="display:none"></textarea>
</div>
""",
"stopwatch-online": """
<div class="panel">
  <div id="sw-display" class="big-time">00:00.00</div>
  <div id="sw-chips" class="jf-stats" style="justify-content:center;margin:8px 0 4px"></div>
  <div class="row">
    <button class="btn" id="sw-start" onclick="swStart()">Start</button>
    <button class="btn ghost" onclick="swLap()">Lap</button>
    <button class="btn ghost" onclick="swPause()">Pause</button>
    <button class="btn ghost" onclick="swReset()">Reset</button>
  </div>
  <label>Laps <span class="tool-note">shortcuts — Space starts/pauses, L records a lap</span></label>
  <div id="sw-laps"></div>
  <div id="sw2-export" class="row" style="display:none">
    <button class="btn ghost" onclick="sw2Copy(this)">Copy laps</button>
    <button class="btn ghost" onclick="sw2Csv()">Download CSV</button>
  </div>
</div>
""",
"countdown-timer": """
<div class="panel">
  <label>Quick presets</label>
  <div class="ir2-presets">
    <button type="button" class="ir2-preset" onclick="cd2PreMin(10)">+10 minutes</button>
    <button type="button" class="ir2-preset" onclick="cd2PreMin(60)">+1 hour</button>
    <button type="button" class="ir2-preset" onclick="cd2PreMin(180)">+3 hours</button>
    <button type="button" class="ir2-preset" onclick="cd2Tonight()">Tonight 6 pm</button>
    <button type="button" class="ir2-preset" onclick="cd2NY()">New Year</button>
  </div>
  <label>Event name (optional)</label>
  <input id="cd-name" placeholder="Product launch">
  <div class="row">
    <div><label>Date</label><input type="text" id="cd-date" readonly placeholder="Pick a date"></div>
    <div><label>Time</label><input type="text" id="cd-time" readonly placeholder="Pick a time"><input type="hidden" id="cd-time-val" value="09:00"></div>
  </div>
  <label class="pg-switch"><input type="checkbox" id="cd2-sound" checked><span class="pg-track"></span> Play a chime when time is up</label>
  <div class="row"><button class="btn" onclick="cdStart()">Start countdown</button></div>
  <div id="cd2-tstat" class="jf-stats" style="margin:12px 0"></div>
  <div id="cd-units" class="cd-units"></div>
  <div class="cd-bar"><div id="cd-fill"></div></div>
  <div id="cd-msg" class="result"></div>
</div>
""",
"json-to-csv-converter": """
<div class="panel jc2">
  <div class="uc2-cats jf-stats" id="jc2-delims">
    <span class="ir2-pl">CSV delimiter:</span>
    <button class="uc2-cat active" onclick="jc2Delim(',', this)">Comma</button>
    <button class="uc2-cat" onclick="jc2Delim(';', this)">Semicolon</button>
    <button class="uc2-cat" onclick="jc2Delim('tb', this)">Tab</button>
    <button class="uc2-cat" onclick="jc2Delim('|', this)">Pipe</button>
  </div>
  <label>JSON array of objects &mdash; converted live</label>
  <textarea id="j2c-in" oninput="jsonToCsv()" placeholder='[{"name": "Ada", "role": "Engineer"}]'>[{"name":"Ada","role":"Engineer","years":12},{"name":"Grace","role":"Admiral","years":30},{"name":"Linus","role":"Kernel","years":33}]</textarea>
  <div class="jf-stats" id="jc2-stats"></div>
  <label>CSV output</label>
  <textarea id="j2c-out" style="min-height:180px" readonly></textarea>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="jc2Copy(this)">Copy CSV</button>
    <button class="btn ghost" onclick="jc2Download()">Download .csv</button>
  </div>
</div>""",


"pdf-merge": """
<script src="https://cdn.jsdelivr.net/npm/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
<div class="panel">
  <div class="bi2-drop" id="pm2-drop" ondragover="bi2Drag(event)" ondragleave="bi2Undrag(event)" ondrop="pm2Drop(event)">
    <b>Drop PDF files here</b>
    <span>or</span>
    <label class="btn" style="margin:0">Choose files<input type="file" id="pm-files" accept="application/pdf" multiple style="display:none"></label>
  </div>
  <label>Merge order \u2014 reorder with \u2191/\u2193, remove with \u2715</label>
  <div id="pm-list" class="pm2-list"></div>
  <div id="pm2-stats" class="jf-stats" style="margin:10px 0"></div>
  <div class="row"><div><label>Output file name</label><input type="text" id="pm-name" value="merged.pdf" /></div></div>
  <div class="row">
    <button class="btn" onclick="pdfMerge()">Merge PDFs</button>
    <button class="btn ghost" onclick="pm2Clear()">Clear all</button>
  </div>
  <div id="pm-out" class="result">Drop two or more PDF files to merge.</div>
</div>
""",
"pdf-split": """
<script src="https://cdn.jsdelivr.net/npm/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
<div class="panel">
  <div class="bi2-drop" id="ps2-drop" ondragover="bi2Drag(event)" ondragleave="bi2Undrag(event)" ondrop="ps2Drop(event)">
    <b>Drop a PDF here</b>
    <span>or</span>
    <label class="btn" style="margin:0">Choose file<input type="file" id="ps-file" accept="application/pdf" style="display:none"></label>
  </div>
  <div id="ps2-stats" class="jf-stats" style="margin:12px 0"></div>
  <label>Mode</label>
  <div class="lr2-types">
    <button type="button" class="lr2-type active" onclick="ps2Mode(0,this)">Extract a range</button>
    <button type="button" class="lr2-type" onclick="ps2Mode(1,this)">Split every N pages</button>
  </div>
  <div id="ps2-range-wrap">
    <label>Pages to keep (e.g. 1-3,5,8-10) \u2014 blank keeps everything</label>
    <input type="text" id="ps-range" placeholder="1-3,5" oninput="ps2Check()">
  </div>
  <div id="ps2-n-wrap" style="display:none">
    <label>Pages per output file</label>
    <input type="number" id="ps-n" value="1" min="1" oninput="ps2Check()">
  </div>
  <div id="ps2-range-info" class="jf-stats" style="margin:10px 0"></div>
  <div class="row"><div><label>Output file name</label><input type="text" id="ps-name" value="extracted.pdf" /></div></div>
  <button class="btn" onclick="pdfSplit()">Extract pages</button>
  <div id="ps2-multi" style="margin:10px 0"></div>
  <div id="ps-out" class="result">Drop a PDF to begin.</div>
</div>
""",
"image-compressor": """
<div class="panel">
  <div class="bi2-drop" id="ic2-drop" ondragover="bi2Drag(event)" ondragleave="bi2Undrag(event)" ondrop="ic2Drop(event)">
    <b>Drop an image here</b>
    <span>or</span>
    <label class="btn" style="margin:0">Choose file<input type="file" id="ic-file" accept="image/*" style="display:none"></label>
  </div>
  <label>Output format</label>
  <div class="ir2-presets ic2-fmts">
    <button type="button" class="ir2-preset active" onclick="ic2Fmt('image/jpeg', this)">JPEG</button>
    <button type="button" class="ir2-preset" onclick="ic2Fmt('image/webp', this)">WebP</button>
    <button type="button" class="ir2-preset" onclick="ic2Fmt('image/png', this)">PNG</button>
  </div>
  <div class="row">
    <div><label>Quality: <span id="ic-qv">75</span>%</label><input type="range" id="ic-q" min="10" max="100" value="75" style="padding:0" oninput="document.getElementById('ic-qv').textContent=this.value;imgCompress()" /></div>
    <div><label>Max width (px, blank = original)</label><input type="number" id="ic-w" placeholder="original" oninput="imgCompress()" /></div>
  </div>
  <input type="hidden" id="ic-fmt" value="image/jpeg">
  <button class="btn" onclick="imgCompress()">Compress again</button>
  <div id="ic2-stats" class="jf-stats" style="margin:12px 0"></div>
  <div id="ic2-compare" class="row" style="display:none">
    <div class="bi2-prev"><img id="ic2-a" alt="Original image"><em>original \u00b7 <b id="ic2-asz"></b></em></div>
    <div class="bi2-prev"><img id="ic2-b" alt="Compressed image"><em>compressed \u00b7 <b id="ic2-bsz"></b> \u00b7 <span id="ic2-save"></span></em></div>
  </div>
  <div id="ic-out" class="result">Select an image to compress.</div>
  <a id="ic-dl" class="btn" style="display:none;margin-top:10px" download>Download compressed image</a>
</div>
""",
"image-cropper": """
<div class="panel">
  <div class="bi2-drop" id="icr2-drop" ondragover="bi2Drag(event)" ondragleave="bi2Undrag(event)" ondrop="icr2Drop(event)">
    <b>Drop an image here</b>
    <span>or</span>
    <label class="btn" style="margin:0">Choose file<input type="file" id="icr-file" accept="image/*" style="display:none"></label>
  </div>
  <div id="icr-dims" class="jf-stats" style="margin:10px 0"></div>
  <div class="icr2-wrap" id="icr2-wrap">
    <img id="icr-imgel" alt="Cropping preview \u2014 drag on the image to select an area" onmousedown="icr2Down(event)">
    <div id="icr-box" class="icr2-box"></div>
  </div>
  <label>Aspect presets</label>
  <div class="ir2-presets">
    <button type="button" class="ir2-preset" onclick="icr2Pre(0, this)">Free</button>
    <button type="button" class="ir2-preset" onclick="icr2Pre(1, this)">1:1</button>
    <button type="button" class="ir2-preset" onclick="icr2Pre(4 / 3, this)">4:3</button>
    <button type="button" class="ir2-preset" onclick="icr2Pre(16 / 9, this)">16:9</button>
    <button type="button" class="ir2-preset" onclick="icr2Pre(3 / 2, this)">3:2</button>
  </div>
  <div class="row">
    <div><label>X</label><input type="number" id="icr-x" value="0" oninput="icr2Draw()" /></div>
    <div><label>Y</label><input type="number" id="icr-y" value="0" oninput="icr2Draw()" /></div>
    <div><label>Width</label><input type="number" id="icr-w" placeholder="to edge" oninput="icr2Draw()" /></div>
    <div><label>Height</label><input type="number" id="icr-h" placeholder="to edge" oninput="icr2Draw()" /></div>
    <div><label>Output width</label><input type="number" id="icr-ow" placeholder="original" /></div>
  </div>
  <div class="row"><div><label>Format</label><select id="icr-fmt"><option value="image/png">PNG</option><option value="image/jpeg">JPEG</option></select></div></div>
  <button class="btn" onclick="imgCrop()">Apply crop</button>
  <div id="icr-out" class="result">Load an image, then drag on it or use the fields.</div>
  <img id="icr-preview" alt="Cropped result preview" style="max-width:100%;margin-top:12px;display:none;border-radius:8px" />
  <a id="icr-dl" class="btn" style="display:none;margin-top:10px" download>Download cropped image</a>
</div>
""",
"meta-tag-generator": """
<div class="panel">
  <div class="row">
    <div><label>Page title</label><input type="text" id="mt-title" placeholder="Best Coffee Grinders of 2025" oninput="metaGen()" /></div>
    <div><label>Author / brand</label><input type="text" id="mt-author" placeholder="Your Name" oninput="metaGen()" /></div>
  </div>
  <label>Meta description</label>
  <textarea id="mt-desc" style="min-height:80px" placeholder="A compelling 150-character summary of the page." oninput="metaGen()"></textarea>
  <div class="row">
    <div><label>Page URL</label><input type="text" id="mt-url" placeholder="https://example.com/page" oninput="metaGen()" /></div>
    <div><label>Social image URL</label><input type="text" id="mt-img" placeholder="https://example.com/card.jpg" oninput="metaGen()" /></div>
  </div>
  <div id="mt2-stats" class="jf-stats" style="margin:10px 0"></div>
  <label>Google search preview</label>
  <div class="result" id="mt-google" style="white-space:normal;font-family:Arial,sans-serif"></div>
  <label>Social share card preview</label>
  <div class="mt2-social" id="mt2-social"></div>
  <label>Generated tags</label>
  <div class="uc2-cats jf-w100">
    <button type="button" class="uc2-cat active" onclick="mt2Tab(3,this)">All tags</button>
    <button type="button" class="uc2-cat" onclick="mt2Tab(0,this)">Basic</button>
    <button type="button" class="uc2-cat" onclick="mt2Tab(1,this)">Open Graph</button>
    <button type="button" class="uc2-cat" onclick="mt2Tab(2,this)">Twitter</button>
  </div>
  <textarea id="mt-code" style="min-height:220px" readonly></textarea>
  <button class="btn" onclick="copyText('mt-code')">Copy tags</button>
</div>
""",
"keyword-density-checker": """
<div class="panel kd2">
  <label>Text to analyse &mdash; updates live</label>
  <textarea id="kd-in" oninput="kwDensity()" placeholder="Paste your article or page text here&hellip;"></textarea>
  <div class="lr2-types">
    <label class="pg-switch"><input type="checkbox" id="kd-stop" checked onchange="kwDensity()" /><span class="pg-track"></span> Hide common stop words</label>
    <span class="ir2-pl" style="margin-left:auto">Ideal density 0.5&ndash;2.5%</span>
  </div>
  <div class="jf-stats" id="kd2-stats"></div>
  <div id="kd-out" class="result" style="white-space:normal"></div>
</div>""",

"xml-sitemap-generator": """
<div class="panel">
  <label>Page URLs (one per line)</label>
  <textarea id="sm-urls" oninput="sitemapGen()" placeholder="https://example.com/&#10;https://example.com/about&#10;https://example.com/blog/post-1"></textarea>
  <label class="pg-switch"><input type="checkbox" id="sm-use-lastmod" checked onchange="sitemapGen()"><span class="pg-track"></span> Include &lt;lastmod&gt; entries</label>
  <div class="row">
    <div><label>Lastmod date</label><input type="text" id="sm-lastmod" readonly placeholder="Pick a date"></div>
    <div><label>Change frequency</label><select id="sm-freq" onchange="sitemapGen()"><option value="">omit</option><option value="daily">daily</option><option value="weekly" selected>weekly</option><option value="monthly">monthly</option><option value="yearly">yearly</option></select></div>
    <div><label>Priority (0.1\u20131.0)</label><input type="number" id="sm-prio" min="0.1" max="1" step="0.1" placeholder="omit" oninput="sitemapGen()" /></div>
  </div>
  <div id="sm2-stats" class="jf-stats" style="margin:10px 0"></div>
  <button class="btn" onclick="sitemapGen()">Generate sitemap</button>
  <label>sitemap.xml</label>
  <textarea id="sm-out" style="min-height:220px" readonly></textarea>
  <div class="row" style="flex-wrap:wrap">
    <button class="btn" onclick="copyText('sm-out')">Copy XML</button>
    <a id="sm-dl" class="btn" href="javascript:void(0)" download="sitemap.xml" style="display:none">Download sitemap.xml</a>
    <button class="btn ghost" onclick="sm2Robots(this)">Copy robots.txt line</button>
  </div>
  <div id="sm2-bad" class="result"></div>
</div>
""",
"slug-generator": """
<div class="panel">
  <label>Titles (one per line for batch mode)</label>
  <textarea id="sl-in" oninput="slugGen()" placeholder="10 Tips for Better Sleep&#10;Caf\u00e9 Culture in Z\u00fcrich&#10;How to Bake Sourdough"></textarea>
  <label>Separator</label>
  <div class="ir2-presets">
    <button type="button" class="ir2-preset active" onclick="sl2Sep('-', this)">Hyphen (-)</button>
    <button type="button" class="ir2-preset" onclick="sl2Sep('_', this)">Underscore (_)</button>
    <button type="button" class="ir2-preset" onclick="sl2Sep('.', this)">Dot (.)</button>
    <button type="button" class="ir2-preset" onclick="sl2Sep('', this)">None</button>
  </div>
  <div class="row" style="align-items:flex-end">
    <div><label>Max length (0 = unlimited)</label><input type="number" id="sl-len" value="0" min="0" oninput="slugGen()" /></div>
    <div id="sl2-stats" class="jf-stats" style="margin:0 0 4px"></div>
  </div>
  <label class="pg-switch"><input type="checkbox" id="sl-lower" checked onchange="slugGen()"><span class="pg-track"></span> Lowercase</label>
  <label class="pg-switch"><input type="checkbox" id="sl-stop" checked onchange="slugGen()"><span class="pg-track"></span> Remove stop words (a, the, of, to\u2026)</label>
  <div class="row">
    <button class="btn" onclick="slugGen()">Generate slugs</button>
    <button class="btn ghost" onclick="sl2Sample()">Sample</button>
  </div>
  <label>Slugs</label>
  <textarea id="sl-out" style="min-height:140px" readonly></textarea>
  <div class="row">
    <button class="btn ghost" onclick="copyText('sl-out')">Copy slugs</button>
    <button class="btn ghost" onclick="sl2Download()">Download .txt</button>
  </div>
</div>
""",
"invoice-generator": """
<div class="panel">
  <div class="row">
    <div><label>Your business name</label><input type="text" id="inv-from" placeholder="Acme Studio" oninput="invoiceRender()" /></div>
    <div><label>Your details</label><input type="text" id="inv-from2" placeholder="Address · email · phone" oninput="invoiceRender()" /></div>
  </div>
  <div class="row">
    <div><label>Client name</label><input type="text" id="inv-to" placeholder="Client Ltd" oninput="invoiceRender()" /></div>
    <div><label>Client details</label><input type="text" id="inv-to2" placeholder="Address" oninput="invoiceRender()" /></div>
  </div>
  <div class="row">
    <div><label>Invoice number</label><input type="text" id="inv-num" value="2025-001" oninput="invoiceRender()" /></div>
    <div><label>Issue date</label><input type="text" id="inv-date" readonly placeholder="Pick a date" oninput="invoiceRender()" /></div>
    <div><label>Due date</label><input type="text" id="inv-due" readonly placeholder="Pick a date" oninput="invoiceRender()" /></div>
    <div><label>Tax %</label><input type="number" id="inv-tax" value="0" min="0" oninput="invoiceRender()" /></div>
  </div>
  <label>Line items</label>
  <div id="inv-items"></div>
  <button class="btn ghost" onclick="invAddRow()">+ Add line item</button>
  <h3 style="margin:18px 0 6px">Preview</h3>
  <div id="inv-print" style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:22px"></div>
  <button class="btn" onclick="invPrint()">Print / Save PDF</button>
  <button class="btn ghost" onclick="invCopy(this)">Copy invoice text</button>
</div>""",
"percentage-calculator": """
<div class="panel pct2">
  <div class="pg-tabs pct2-tabs">
    <button class="pg-tab active" onclick="pct2Mode('of', this)">% of number</button>
    <button class="pg-tab" onclick="pct2Mode('iswhat', this)">X is what %</button>
    <button class="pg-tab" onclick="pct2Mode('change', this)">% change</button>
    <button class="pg-tab" onclick="pct2Mode('addsub', this)">Add / subtract %</button>
    <button class="pg-tab" onclick="pct2Mode('reverse', this)">Reverse %</button>
  </div>
  <div class="pct2-pane" id="pct2-p-of">
    <div class="row">
      <div><label>Percentage (%)</label><input type="number" id="pct2-of-p" value="15" oninput="pct2Run()" /></div>
      <div><label>Of number</label><input type="number" id="pct2-of-n" value="200" oninput="pct2Run()" /></div>
    </div>
  </div>
  <div class="pct2-pane" id="pct2-p-iswhat" style="display:none">
    <div class="row">
      <div><label>Value X</label><input type="number" id="pct2-iw-x" value="30" oninput="pct2Run()" /></div>
      <div><label>Is what % of Y</label><input type="number" id="pct2-iw-y" value="150" oninput="pct2Run()" /></div>
    </div>
  </div>
  <div class="pct2-pane" id="pct2-p-change" style="display:none">
    <div class="row">
      <div><label>From (old value)</label><input type="number" id="pct2-ch-a" value="80" oninput="pct2Run()" /></div>
      <div><label>To (new value)</label><input type="number" id="pct2-ch-b" value="100" oninput="pct2Run()" /></div>
    </div>
  </div>
  <div class="pct2-pane" id="pct2-p-addsub" style="display:none">
    <div class="row">
      <div><label>Number</label><input type="number" id="pct2-as-n" value="250" oninput="pct2Run()" /></div>
      <div><label>Percent (%)</label><input type="number" id="pct2-as-p" value="20" oninput="pct2Run()" /></div>
    </div>
    <div class="pct2-dir">
      <button class="pct2-dir-btn active" id="pct2-add" onclick="pct2Dir(true, this)">+ Add (e.g. tax)</button>
      <button class="pct2-dir-btn" id="pct2-sub" onclick="pct2Dir(false, this)">&minus; Subtract (e.g. discount)</button>
    </div>
  </div>
  <div class="pct2-pane" id="pct2-p-reverse" style="display:none">
    <div class="row">
      <div><label>Final amount</label><input type="number" id="pct2-rv-f" value="120" oninput="pct2Run()" /></div>
      <div><label>Percent added (%)</label><input type="number" id="pct2-rv-p" value="20" oninput="pct2Run()" /></div>
    </div>
    <p class="tool-note">Find the original number before a percentage was added &mdash; e.g. a price before VAT.</p>
  </div>
  <div class="pct2-result" id="pct2-big">&mdash;</div>
  <div class="pct2-steps" id="pct2-steps"></div>
  <div class="pct2-extra" id="pct2-extra"></div>
</div>""",

"bmi-calculator": """
<div class="panel bm2">
  <div class="lr2-types">
    <button class="lr2-type active" id="bm2-metric" onclick="bm2Units('metric', this)">Metric (kg / cm)</button>
    <button class="lr2-type" id="bm2-imperial" onclick="bm2Units('imperial', this)">Imperial (lb / ft+in)</button>
  </div>
  <div id="bm2-metric-pane">
    <div class="row">
      <div><label>Weight (kg)</label><input type="number" id="bmi-w" value="70" oninput="bmiCalc()" /></div>
      <div><label>Height (cm)</label><input type="number" id="bmi-h" value="175" oninput="bmiCalc()" /></div>
    </div>
  </div>
  <div id="bm2-imperial-pane" style="display:none">
    <div class="row">
      <div><label>Weight (lb)</label><input type="number" id="bm2-wlb" value="155" oninput="bmiCalc()" /></div>
      <div><label>Height</label><div class="row bm2-ft"><input type="number" id="bm2-ft" value="5" placeholder="ft" oninput="bmiCalc()" /><input type="number" id="bm2-in" value="9" placeholder="in" oninput="bmiCalc()" /></div></div>
    </div>
  </div>
  <div class="pct2-result" id="bmi-big">&mdash;</div>
  <div class="bm2-gauge">
    <div class="bm2-gauge-track"><div class="bm2-gauge-seg u1"></div><div class="bm2-gauge-seg u2"></div><div class="bm2-gauge-seg u3"></div><div class="bm2-gauge-seg u4"></div><div class="bm2-gauge-marker" id="bm2-marker"></div></div>
    <div class="bm2-gauge-labels"><span>15</span><span>18.5</span><span>25</span><span>30</span><span>40</span></div>
  </div>
  <div id="bmi-out" class="bm2-cat"></div>
  <div class="bm2-healthy" id="bm2-healthy"></div>
  <div class="lr2-actions" style="margin-top:10px"><button class="btn ghost" onclick="bm2Copy(this)">Copy result</button></div>
</div>""",

"age-calculator": """

<div class="panel ag2">
  <label>Date of birth</label>
  <input type="text" id="age-dob" readonly placeholder="Pick your date of birth" oninput="ageCalc()">
  <div class="row">
    <div><label>Compare with (defaults to today)</label><input type="text" id="ag2-on" readonly placeholder="Today" /></div>
    <div style="align-self:end"><button class="btn ghost" onclick="ag2Today()">Compare with today</button></div>
  </div>
  <div class="pct2-result" id="ag2-big">&mdash;</div>
  <div class="jf-stats" id="ag2-chips"></div>
  <table class="wc-table ag2-table"><tbody>
    <tr><th>Total months</th><td id="ag2-months">&mdash;</td></tr>
    <tr><th>Total weeks</th><td id="ag2-weeks">&mdash;</td></tr>
    <tr><th>Total days</th><td id="ag2-days">&mdash;</td></tr>
    <tr><th>Total hours</th><td id="ag2-hours">&mdash;</td></tr>
    <tr><th>Total minutes</th><td id="ag2-mins">&mdash;</td></tr>
    <tr><th>Next birthday in</th><td id="ag2-next">&mdash;</td></tr>
    <tr><th>Day of birth</th><td id="ag2-dow">&mdash;</td></tr>
  </tbody></table>
  <label>Milestones ahead</label>
  <div class="jf-stats" id="ag2-mile"></div>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="ag2Copy(this)">Copy summary</button>
  </div>
</div>
""",

"loan-emi-calculator": """

<div class="panel ln2">
  <div class="lr2-types" style="margin-bottom:10px">
    <button type="button" class="lr2-type" onclick="ln2Term(5)">5 years</button>
    <button type="button" class="lr2-type" onclick="ln2Term(10)">10 years</button>
    <button type="button" class="lr2-type" onclick="ln2Term(15)">15 years</button>
    <button type="button" class="lr2-type active" onclick="ln2Term(30)">30 years</button>
  </div>
  <div class="row">
    <div><label>Loan amount</label><input type="number" id="emi-p" value="250000" oninput="emiCalc()" /></div>
    <div><label>Interest rate (% / year)</label><input type="number" id="emi-r" value="7.5" step="0.01" oninput="emiCalc()" /></div>
    <div><label>Term (years)</label><input type="number" id="emi-n" value="30" oninput="emiCalc()" /></div>
    <div><label>Extra / month (prepay)</label><input type="number" id="emi-x" value="0" min="0" oninput="emiCalc()" /></div>
  </div>
  <div class="pct2-result" id="ln2-big">&mdash;</div>
  <div class="jf-stats" id="ln2-chips"></div>
  <div class="ci2-bars" id="ln2-bars"></div>
  <p class="tool-note" id="ln2-pay"></p>
  <div class="lr2-actions" style="margin:10px 0">
    <button class="btn ghost" onclick="ln2Csv()">Download full schedule (CSV)</button>
    <button class="btn ghost" onclick="ln2Copy(this)">Copy summary</button>
  </div>
  <p class="tool-note">Payment schedule (year by year &mdash; principal vs interest, includes prepayments)</p>
  <div class="uc2-table" id="ln2-table"></div>
</div>
""",

"word-counter": """
<div class="panel wc-pro">
  <div class="wc-toolbar">
    <span class="wc-live-dot"></span><span class="wc-live-txt">Live counting as you type</span>
    <span class="wc-tb-spacer"></span>
    <button class="btn ghost sm" onclick="wc2Sample()">Load sample</button>
    <button class="btn ghost sm" onclick="wc2Copy(this)">Copy text</button>
    <button class="btn ghost sm danger" onclick="wc2Clear()">Clear</button>
  </div>
  <textarea id="wc-in" oninput="wordCount()" placeholder="Start typing or paste your text here&hellip;"></textarea>
  <div class="wc-tiles" id="wc-tiles"></div>
  <div class="wc-cols">
    <div class="wc-col">
      <h3 class="wc-h">[[ic zap]] Keyword density</h3>
      <div class="wc-kw-opts">
        <label class="pg-switch"><input type="checkbox" id="wc-kw-stop" checked onchange="wordCount()" /><span class="pg-track"></span> Exclude common words</label>
        <label class="pg-switch"><input type="checkbox" id="wc-kw-2w" onchange="wordCount()" /><span class="pg-track"></span> 2-word phrases</label>
      </div>
      <div id="wc-kw" class="wc-kw"></div>
    </div>
    <div class="wc-col">
      <h3 class="wc-h">[[ic gauge]] Readability</h3>
      <div id="wc-read"></div>
      <h3 class="wc-h">[[ic smartphone]] Platform limits</h3>
      <div id="wc-social"></div>
    </div>
  </div>
  <p class="tool-note">Reference table &mdash; pages and time estimates for common document lengths (Letter &asymp; 250 words/page, A4 &asymp; 500 words/page):</p>
  <div id="wc-table" class="wc-table-wrap"></div>
</div>""",

"case-converter": """
<div class="panel cv2">
  <label>Enter your text</label>
  <textarea id="case-in" oninput="cv2Run()" placeholder="Type or paste text&hellip;">The quick brown fox jumps over the lazy dog</textarea>
  <div class="lr2-types" id="cv2-modes">
    <button class="lr2-type active" onclick="cv2Set('upper', this)">UPPER CASE</button>
    <button class="lr2-type" onclick="cv2Set('lower', this)">lowercase</button>
    <button class="lr2-type" onclick="cv2Set('title', this)">Title Case</button>
    <button class="lr2-type" onclick="cv2Set('sentence', this)">Sentence case</button>
    <button class="lr2-type" onclick="cv2Set('camel', this)">camelCase</button>
    <button class="lr2-type" onclick="cv2Set('pascal', this)">PascalCase</button>
    <button class="lr2-type" onclick="cv2Set('snake', this)">snake_case</button>
    <button class="lr2-type" onclick="cv2Set('kebab', this)">kebab-case</button>
  </div>
  <label>Result</label>
  <textarea id="cv2-out" readonly placeholder="Result appears here live&hellip;"></textarea>
  <div class="jf-stats" id="cv2-stats"></div>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="cv2Copy(this)">Copy result</button>
    <button class="btn ghost" onclick="cv2Swap()">Use result as input</button>
  </div>
</div>""",

"remove-duplicate-lines": """
<div class="panel dd2">
  <label>Lines &mdash; duplicates removed live</label>
  <textarea id="dd-in" oninput="dedupeLines()" placeholder="One item per line&hellip;">apple&#10;banana&#10;apple&#10;Apple&#10;cherry&#10;banana</textarea>
  <div class="lr2-types">
    <label class="pg-switch"><input type="checkbox" id="dd-case" onchange="dedupeLines()" /><span class="pg-track"></span> Ignore case</label>
    <label class="pg-switch"><input type="checkbox" id="dd-trim" checked onchange="dedupeLines()" /><span class="pg-track"></span> Trim whitespace</label>
    <label class="pg-switch"><input type="checkbox" id="dd2-noempty" checked onchange="dedupeLines()" /><span class="pg-track"></span> Remove empty lines</label>
    <label class="pg-switch"><input type="checkbox" id="dd2-sort" onchange="dedupeLines()" /><span class="pg-track"></span> Sort result A&ndash;Z</label>
  </div>
  <div class="jf-stats" id="dd2-stats"></div>
  <label>Clean result</label>
  <textarea id="dd2-out" readonly></textarea>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="dd2Copy(this)">Copy result</button>
    <button class="btn ghost" onclick="dd2Use()">Replace input</button>
  </div>
</div>""",

"reverse-text": """
<div class="panel rv2">
  <label>Text</label>
  <textarea id="rev-in" oninput="reverseText(RV2_MODE)" placeholder="Hello world">Hello world</textarea>
  <div class="lr2-types" id="rv2-modes">
    <button class="lr2-type active" onclick="reverseText('chars', this)">Characters</button>
    <button class="lr2-type" onclick="reverseText('words', this)">Words</button>
    <button class="lr2-type" onclick="reverseText('lines', this)">Lines</button>
    <button class="lr2-type" onclick="reverseText('each', this)">Each line reversed</button>
  </div>
  <div class="jf-stats" id="rv2-stats"></div>
  <label>Reversed</label>
  <textarea id="rev-out" readonly></textarea>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="rv2Copy(this)">Copy result</button>
    <button class="btn ghost" onclick="rv2Swap()">Use result as input</button>
  </div>
</div>""",

"json-formatter": """
<div class="panel jf-pro">
  <div class="jf-toolbar">
    <span class="jf-tb-label">[[ic braces]] JSON editor</span>
    <span class="jf-tb-spacer"></span>
    <button class="btn ghost sm" onclick="jf2Sample()">Sample</button>
    <button class="btn ghost sm" onclick="jf2Paste()">Paste</button>
    <button class="btn ghost sm danger" onclick="jf2Clear()">Clear</button>
  </div>
  <textarea id="json-in" oninput="jf2Live()" placeholder='{&quot;name&quot;:&quot;MSCALE&quot;,&quot;tools&quot;:100,&quot;live&quot;:true}'></textarea>
  <div class="jf-actions">
    <button class="btn" onclick="jf2Format(2)">Beautify (2)</button>
    <button class="btn ghost" onclick="jf2Format(4)">Beautify (4)</button>
    <button class="btn ghost" onclick="jf2Minify()">Minify</button>
    <button class="btn ghost" onclick="jf2Sort()">Sort keys A&ndash;Z</button>
  </div>
  <div id="json-err" class="error jf-err"></div>
  <div id="jf-stats" class="jf-stats"></div>
  <div class="jf-tabs">
    <button class="jf-tab active" id="jf-tab-out" onclick="jf2Tab('out')">Formatted</button>
    <button class="jf-tab" id="jf-tab-tree" onclick="jf2Tab('tree')">Tree view</button>
    <span class="jf-tb-spacer"></span>
    <button class="btn ghost sm" onclick="jf2Copy(this)">Copy</button>
    <button class="btn ghost sm" onclick="jf2Download()">Download .json</button>
  </div>
  <div id="json-out" class="result mono jf-out"></div>
  <div id="jf-tree" class="jf-tree" style="display:none"></div>
</div>""",

"base64-encoder-decoder": """
<div class="panel b64p">
  <div class="lr2-types">
    <button class="lr2-type active" id="b64-enc" onclick="b64Mode('enc')">Encode &rarr;</button>
    <button class="lr2-type" id="b64-dec" onclick="b64Mode('dec')">&larr; Decode</button>
    <span class="ir2-pl" style="margin-left:auto">URL-safe alphabet</span>
    <label class="pg-switch"><input type="checkbox" id="b64-urlsafe" onchange="b64Live()" /><span class="pg-track"></span></label>
  </div>
  <div class="b64-io">
    <div><label>Input</label><textarea id="b64-in" oninput="b64Live()" placeholder="Hello MSCALE"></textarea></div>
    <button class="btn ghost sm" onclick="b64Swap()" title="Move output back into input">&#8644;</button>
    <div><label>Output</label><textarea id="b64-out" readonly></textarea></div>
  </div>
  <div class="jf-stats" id="b64-stats"></div>
  <div id="b64-err" class="error" style="display:none"></div>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="b64Copy(this)">Copy output</button>
    <button class="btn ghost" onclick="b64Download()">Download .txt</button>
    <button class="btn ghost" onclick="b64Sample()">Sample</button>
  </div>
</div>""",

"url-encoder-decoder": """
<div class="panel ue2">
  <div class="lr2-types">
    <button class="lr2-type active" id="ue2-enc" onclick="ue2Mode('enc')">Encode &rarr;</button>
    <button class="lr2-type" id="ue2-dec" onclick="ue2Mode('dec')">&larr; Decode</button>
    <span class="ir2-pl" style="margin-left:auto">Keep URL structure</span>
    <label class="pg-switch"><input type="checkbox" id="ue2-uri" onchange="ue2Live()" /><span class="pg-track"></span></label>
  </div>
  <div class="b64-io">
    <div><label>Input</label><textarea id="url-in" oninput="ue2Live()" placeholder="https://example.com/search?q=hello world&num=10"></textarea></div>
    <button class="btn ghost sm" onclick="ue2Swap()" title="Move output back into input">&#8644;</button>
    <div><label>Output</label><textarea id="url-out" readonly></textarea></div>
  </div>
  <div class="jf-stats" id="ue2-stats"></div>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="ue2Copy(this)">Copy output</button>
    <button class="btn ghost" onclick="ue2Sample()">Sample URL</button>
  </div>
  <div id="ue2-err" class="error" style="display:none"></div>
</div>""",

"uuid-generator": """
<div class="panel uu2">
  <div class="row">
    <div><label>How many UUIDs?</label><input type="number" id="uuid-n" value="5" min="1" max="100" oninput="uuidGen()" /></div>
    <div class="uu2-note">Click any line to copy it</div>
  </div>
  <div class="lr2-types">
    <label class="pg-switch"><input type="checkbox" id="uu2-upper" onchange="uuidRegen()" /><span class="pg-track"></span> UPPERCASE</label>
    <label class="pg-switch"><input type="checkbox" id="uu2-nohyphen" onchange="uuidRegen()" /><span class="pg-track"></span> Remove hyphens</label>
    <label class="pg-switch"><input type="checkbox" id="uu2-braces" onchange="uuidRegen()" /><span class="pg-track"></span> Wrap in braces</label>
  </div>
  <label>Generated UUIDs (v4, cryptographically random)</label>
  <div id="uuid-out" class="result mono"></div>
  <div class="lr2-actions">
    <button class="btn" onclick="uuidGen()">Regenerate</button>
    <button class="btn ghost" onclick="uu2CopyAll(this)">Copy all</button>
  </div>
</div>""",

"unit-converter": """
<div class="panel uc2">
  <div class="uc2-cats" id="uc2-cats"></div>
  <div class="row uc2-row">
    <div class="uc2-val"><label>Value</label><input type="number" id="uc2-val" value="1" oninput="uc2Run()" /></div>
    <div class="uc2-from"><label>From</label><select id="uc2-from" onchange="uc2Run()"></select></div>
    <button class="uc2-swap" title="Swap units" onclick="uc2Swap()">[[ic arrow-right]]</button>
    <div class="uc2-to"><label>To</label><select id="uc2-to" onchange="uc2Run()"></select></div>
  </div>
  <div class="uc2-result" id="uc2-big">&mdash;</div>
  <p class="tool-note">Same value in every unit of this category:</p>
  <div id="uc2-table" class="uc2-table"></div>
  <div class="lr2-actions" style="margin-top:10px"><button class="btn ghost" onclick="uc2Copy(this)">Copy result</button></div>
</div>""",

"timestamp-converter": """
<div class="panel tm2">
  <div class="pct2-result" id="tm2-now">&mdash;</div>
  <p class="tool-note">Current Unix time (updates every second)</p>
  <div class="lr2-types">
    <button class="lr2-type active" id="tm2-s" onclick="tm2Unit('s')">Seconds</button>
    <button class="lr2-type" id="tm2-ms" onclick="tm2Unit('ms')">Milliseconds</button>
    <span style="flex:1"></span>
    <button class="btn ghost sm" onclick="tm2Now()">Use current time &rarr;</button>
    <button class="btn ghost sm" onclick="tm2Random()">Random</button>
  </div>
  <label>Unix timestamp &rarr; date</label>
  <input type="text" id="ts-in" value="1764000000" oninput="tm2Run()" placeholder="1735689600 or 1735689600000" />
  <div class="jf-stats" id="tm2-stats"></div>
  <table class="wc-table"><tbody>
    <tr><th>ISO 8601 (UTC)</th><td id="tm2-iso">&mdash;</td></tr>
    <tr><th>UTC string</th><td id="tm2-utc">&mdash;</td></tr>
    <tr><th>Local time</th><td id="tm2-local">&mdash;</td></tr>
    <tr><th>Day of week</th><td id="tm2-dow">&mdash;</td></tr>
    <tr><th>Relative</th><td id="tm2-rel">&mdash;</td></tr>
  </tbody></table>
  <label>Date &rarr; timestamp</label>
  <input type="datetime-local" id="ts-date" oninput="tm2Date()" />
  <div class="jf-stats" id="tm2-dstat"></div>
</div>""",

"password-generator": """
<div class="panel pg-panel">
  <div class="pg-tabs" id="pg-tabs">
    <button class="pg-tab active" data-mode="random" onclick="pgMode('random')">Random</button>
    <button class="pg-tab" data-mode="memorable" onclick="pgMode('memorable')">Memorable</button>
    <button class="pg-tab" data-mode="pin" onclick="pgMode('pin')">PIN</button>
  </div>
  <div class="pg-out-wrap">
    <div id="pg-out" class="pg-out" aria-live="polite">&middot;&middot;&middot;&middot;</div>
    <div class="pg-actions">
      <button class="btn" onclick="pgGen()">Regenerate</button>
      <button class="btn ghost" id="pg-copy" onclick="pgCopy()">Copy</button>
    </div>
  </div>
  <div class="pg-meter-row">
    <div class="pg-meter"><div id="pg-fill" class="pg-fill"></div></div>
    <div class="pg-meter-info"><b id="pg-label">&mdash;</b><span id="pg-entropy"></span></div>
  </div>
  <p id="pg-crack" class="pg-crack"></p>
  <div class="pg-slider">
    <label>Length: <b id="pg-len-val">16</b></label>
    <input type="range" id="pg-len" min="4" max="64" value="16" oninput="pgSlider()" />
    <div class="pg-range-marks"><span>4</span><span>64</span></div>
  </div>
  <div class="pg-toggles" id="pg-toggles">
    <label class="pg-switch"><input type="checkbox" id="pg-upper" checked onchange="pgGen()" /><span class="pg-track"></span>Uppercase <span class="pg-set">A-Z</span></label>
    <label class="pg-switch"><input type="checkbox" id="pg-lower" checked onchange="pgGen()" /><span class="pg-track"></span>Lowercase <span class="pg-set">a-z</span></label>
    <label class="pg-switch"><input type="checkbox" id="pg-digits" checked onchange="pgGen()" /><span class="pg-track"></span>Numbers <span class="pg-set">0-9</span></label>
    <label class="pg-switch"><input type="checkbox" id="pg-symbols" checked onchange="pgGen()" /><span class="pg-track"></span>Symbols <span class="pg-set">#$&amp;</span></label>
    <label class="pg-switch"><input type="checkbox" id="pg-ambig" onchange="pgGen()" /><span class="pg-track"></span>Avoid ambiguous <span class="pg-set">il1LoO0</span></label>
  </div>
  <button class="btn ghost" onclick="pgMulti()">Generate 5 alternatives</button>
  <div id="pg-multi" class="pg-multi"></div>
</div>""",
"color-converter": """

<div class="panel cc2">
  <div class="cc2-picker">
    <input type="color" id="col-cc" value="#ff7000" oninput="cc2FromPicker()" aria-label="Pick color" />
    <div class="cc2-picker-col">
      <label>Hex color</label>
      <input type="text" id="col-in" value="#ff7000" oninput="colorConvert()" placeholder="#ff7000" class="cc2-hex" />
      <div id="col-err" class="error"></div>
    </div>
    <button class="btn ghost sm" onclick="cc2Random()">Random</button>
  </div>
  <div class="cc2-preview-row">
    <div class="cc2-big" id="col-swatch"></div>
    <div class="cc2-big cc2-comp" id="cc2-comp" title="Complementary"></div>
  </div>
  <label>WCAG contrast</label>
  <div class="jf-stats" id="cc2-contrast"></div>
  <label>Tints &amp; shades (click to copy)</label>
  <div id="cc2-ramps" class="cc2-ramps"></div>
  <p class="tool-note">Click any value to copy:</p>
  <div id="col-out" class="cc2-fmts"></div>
</div>
""",
"random-number-generator": """
<div class="panel rn2">
  <div class="row">
    <div><label>Min</label><input type="number" id="rn-min" value="1" oninput="randNums()" /></div>
    <div><label>Max</label><input type="number" id="rn-max" value="100" oninput="randNums()" /></div>
    <div><label>How many</label><input type="number" id="rn-count" value="6" min="1" max="1000" oninput="randNums()" /></div>
  </div>
  <div class="lr2-types">
    <label class="pg-switch"><input type="checkbox" id="rn-unique" onchange="randNums()" /><span class="pg-track"></span> Unique only</label>
    <label class="pg-switch"><input type="checkbox" id="rn2-sort" onchange="rn2Render()" /><span class="pg-track"></span> Sort ascending</label>
    <label class="pg-switch"><input type="checkbox" id="rn2-justify" onchange="rn2Render()" /><span class="pg-track"></span> Zero-pad</label>
  </div>
  <div class="pct2-result" id="rn2-big">&mdash;</div>
  <p class="tool-note">All numbers</p>
  <div id="rn-out" class="result"></div>
  <div class="jf-stats" id="rn2-stats"></div>
  <div class="lr2-actions">
    <button class="btn" onclick="randNums()">Re-roll</button>
    <button class="btn ghost" onclick="rn2Copy(this)">Copy all</button>
  </div>
</div>""",

"dice-roller": """
<div class="panel dr2">
  <div class="row">
    <div><label>Number of dice</label><input type="number" id="dice-n" value="2" min="1" max="20" oninput="rollDice()" /></div>
    <div><label>Sides</label><select id="dice-sides" onchange="rollDice()"><option>4</option><option selected>6</option><option>8</option><option>10</option><option>12</option><option>20</option><option>100</option></select></div>
    <div><label>Modifier</label><input type="number" id="dr2-mod" value="0" oninput="rollDice()" /></div>
    <div style="align-self:end"><button class="btn" onclick="rollDice()">Roll</button></div>
  </div>
  <div class="pct2-result" id="dr2-big">&mdash;</div>
  <div id="dice-out" class="result"></div>
  <div class="jf-stats" id="dr2-stats"></div>
  <label>Recent rolls</label>
  <div id="dr2-hist" class="jf-stats" style="min-height:34px"></div>
  <div class="lr2-actions" style="margin-top:10px"><button class="btn ghost" onclick="dr2Copy(this)">Copy result</button></div>
</div>""",

"coin-flipper": """
<div class="panel cf2">
  <div class="row">
    <div><label>How many flips?</label><input type="number" id="coin-n" value="1" min="1" max="1000" oninput="flipCoin()" /></div>
    <div style="align-self:end"><button class="btn" onclick="flipCoin()">Flip coins</button></div>
  </div>
  <div class="pct2-result" id="cf2-big">&mdash;</div>
  <div class="ci2-bars" id="cf2-bars"></div>
  <div class="jf-stats" id="cf2-stats"></div>
  <label>History (newest first)</label>
  <div id="cf2-hist" class="jf-stats" style="min-height:34px"></div>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="cf2Copy(this)">Copy result</button>
    <button class="btn ghost" onclick="cf2Clear()">Clear history</button>
  </div>
</div>""",


"discount-calculator": """
<div class="panel dc2">
  <div class="row">
    <div><label>Original price</label><input type="number" id="disc-p" value="99.99" step="0.01" oninput="discountCalc()" /></div>
    <div><label>Discount (%)</label><input type="number" id="disc-off" value="25" oninput="discountCalc()" /></div>
    <div><label>Tax (%) &mdash; optional</label><input type="number" id="disc-tax" value="0" step="0.01" oninput="discountCalc()" /></div>
  </div>
  <div class="uc2-cats tx2-rates">
    <span class="ir2-pl">Quick discounts:</span>
    <button class="ir2-preset" onclick="dc2Pre(5)">5%</button>
    <button class="ir2-preset" onclick="dc2Pre(10)">10%</button>
    <button class="ir2-preset" onclick="dc2Pre(15)">15%</button>
    <button class="ir2-preset" onclick="dc2Pre(20)">20%</button>
    <button class="ir2-preset" onclick="dc2Pre(25)">25%</button>
    <button class="ir2-preset" onclick="dc2Pre(30)">30%</button>
    <button class="ir2-preset" onclick="dc2Pre(50)">50%</button>
  </div>
  <div class="pct2-result" id="dc2-big">&mdash;</div>
  <div class="ci2-bars" id="dc2-bars"></div>
  <p class="tool-note">Same product at every discount (with your tax rate applied)</p>
  <div class="uc2-table" id="dc2-table"></div>
</div>""",

"tip-calculator": """
<div class="panel tp2">
  <div class="row">
    <div><label>Bill amount</label><input type="number" id="tip-bill" value="64.50" step="0.01" oninput="tipCalc()" /></div>
    <div><label>Tip (%)</label><input type="number" id="tip-pct" value="15" oninput="tipCalc()" /></div>
    <div><label>Split between</label><input type="number" id="tip-people" value="1" min="1" oninput="tipCalc()" /></div>
  </div>
  <div class="uc2-cats tx2-rates">
    <span class="ir2-pl">Tip presets:</span>
    <button class="ir2-preset" onclick="tp2Rate(10)">10%</button>
    <button class="ir2-preset" onclick="tp2Rate(12)">12%</button>
    <button class="ir2-preset" onclick="tp2Rate(15)">15%</button>
    <button class="ir2-preset" onclick="tp2Rate(18)">18%</button>
    <button class="ir2-preset" onclick="tp2Rate(20)">20%</button>
    <button class="ir2-preset" onclick="tp2Rate(25)">25%</button>
  </div>
  <table class="wc-table tp2-table"><tbody>
    <tr><th>Tip amount</th><td id="tp2-tip">\u2014</td></tr>
    <tr><th>Total bill</th><td id="tp2-total">\u2014</td></tr>
    <tr><th>Per person \u2014 tip</th><td id="tp2-per-tip">\u2014</td></tr>
    <tr><th>Per person \u2014 total</th><td id="tp2-per-total">\u2014</td></tr>
  </tbody></table>
</div>""",

"compound-interest-calculator": """
<div class="panel ci2">
  <div class="row">
    <div><label>Initial amount</label><input type="number" id="ci-p" value="10000" oninput="ci2Live()" /></div>
    <div><label>Annual rate (%)</label><input type="number" id="ci-r" value="7" step="0.1" oninput="ci2Live()" /></div>
    <div><label>Years</label><input type="number" id="ci-t" value="10" oninput="ci2Live()" /></div>
  </div>
  <div class="row">
    <div><label>Compounds per year</label><select id="ci-n" onchange="ci2Live()"><option value="1">Yearly</option><option value="4">Quarterly</option><option value="12" selected>Monthly</option><option value="365">Daily</option></select></div>
    <div><label>Monthly contribution \u2014 optional</label><input type="number" id="ci-monthly" value="200" oninput="ci2Live()" /></div>
  </div>
  <div class="pct2-result" id="ci2-big">&mdash;</div>
  <div class="ci2-bars" id="ci2-bars"></div>
  <div class="uc2-cats tx2-rates"><span class="ir2-pl">Comparison of total by compounding frequency:</span><div id="ci2-freq" class="ci2-freq"></div></div>
  <p class="tool-note">Year-by-year growth</p>
  <div class="uc2-table" id="ci2-table"></div>
  <div class="lr2-actions" style="margin-top:10px"><button class="btn ghost" onclick="ci2Copy(this)">Copy result</button><button class="btn ghost" onclick="ci2Csv()">Export CSV</button></div>
</div>""",
"gst-vat-calculator": """
<div class="panel tx2">
  <div class="lr2-types">
    <button class="lr2-type active" id="tx2-add" onclick="tx2Dir('add', this)">Add tax (net \u2192 gross)</button>
    <button class="lr2-type" id="tx2-remove" onclick="tx2Dir('remove', this)">Remove tax (gross \u2192 net)</button>
  </div>
  <div class="row">
    <div><label id="tx2-amt-label">Net amount (before tax)</label><input type="number" id="tax-amt" value="1000" oninput="tx2Run()" /></div>
    <div><label>Tax rate (%)</label><input type="number" id="tax-rate" value="18" step="0.1" oninput="tx2Run()" /></div>
  </div>
  <div class="uc2-cats tx2-rates">
    <span class="ir2-pl">Common rates:</span>
    <button class="ir2-preset" onclick="tx2Rate(5)">5%</button>
    <button class="ir2-preset" onclick="tx2Rate(8)">8%</button>
    <button class="ir2-preset" onclick="tx2Rate(10)">10%</button>
    <button class="ir2-preset" onclick="tx2Rate(12)">12%</button>
    <button class="ir2-preset" onclick="tx2Rate(18)">18%</button>
    <button class="ir2-preset" onclick="tx2Rate(20)">20%</button>
    <button class="ir2-preset" onclick="tx2Rate(25)">25%</button>
  </div>
  <div class="pct2-result" id="tx2-big">&mdash;</div>
  <table class="wc-table tx2-table"><tbody>
    <tr><th>Base (net)</th><td id="tx2-net">\u2014</td></tr>
    <tr><th>Tax amount</th><td id="tx2-tax">\u2014</td></tr>
    <tr><th>Total (gross)</th><td id="tx2-gross">\u2014</td></tr>
  </tbody></table>
  <p class="tool-note">Works for GST, VAT, sales tax \u2014 any percentage-based tax.</p>
</div>""",
"date-difference-calculator": """
<div class="panel dd2">
  <div class="row">
    <div><label>Start date</label><input type="text" id="dd2-a" readonly placeholder="Pick start date" oninput="dateDiff()"></div>
    <div><label>End date</label><input type="text" id="dd2-b" readonly placeholder="Pick end date" oninput="dateDiff()"></div>
  </div>
  <div class="lr2-types">
    <label class="pg-switch"><input type="checkbox" id="dd2-inc" onchange="dateDiff()" /><span class="pg-track"></span> Include end date (day after shifts everything by 1)</label>
  </div>
  <div class="pct2-result" id="dd2-big">&mdash;</div>
  <div class="jf-stats" id="dd2-dowchips"></div>
  <table class="wc-table"><tbody>
    <tr><th>Calendar breakdown</th><td id="dd2-ymd">&mdash;</td></tr>
    <tr><th>Weeks + days</th><td id="dd2-wd">&mdash;</td></tr>
    <tr><th>Business days (Mon&ndash;Fri)</th><td id="dd2-biz">&mdash;</td></tr>
    <tr><th>Total hours</th><td id="dd2-hours">&mdash;</td></tr>
    <tr><th>Total minutes</th><td id="dd2-mins">&mdash;</td></tr>
  </tbody></table>
</div>""",

"find-and-replace": """
<div class="panel fr2">
  <label>Text</label>
  <textarea id="fr-in" oninput="fr2Run()" placeholder="Paste your text&hellip;">The old robot picked the old box. The old cat liked the old robot.</textarea>
  <div class="row">
    <div><label>Find</label><input type="text" id="fr-find" value="old" oninput="fr2Run()" placeholder="text to find" /></div>
    <div><label>Replace with</label><input type="text" id="fr-repl" value="new" oninput="fr2Run()" placeholder="replacement" /></div>
  </div>
  <div class="lr2-types">
    <label class="pg-switch"><input type="checkbox" id="fr-case" onchange="fr2Run()" /><span class="pg-track"></span> Case sensitive</label>
    <label class="pg-switch"><input type="checkbox" id="fr-regex" onchange="fr2Run()" /><span class="pg-track"></span> Regular expression</label>
  </div>
  <div class="jf-stats" id="fr2-stats"></div>
  <label>Preview &mdash; matches highlighted</label>
  <div id="fr2-preview" class="result mono fr2-prev"></div>
  <div class="lr2-actions">
    <button class="btn" onclick="fr2All(this)">Replace all</button>
    <button class="btn ghost" onclick="fr2Undo()">Undo replace</button>
    <button class="btn ghost" onclick="fr2Copy(this)">Copy text</button>
  </div>
</div>""",

"text-sorter": """
<div class="panel ts2">
  <label>Lines &mdash; sorted live, input never destroyed</label>
  <textarea id="sort-in" oninput="ts2Run()" placeholder="banana&#10;apple&#10;cherry">banana&#10;apple&#10;Cherry&#10;dragonfruit&#10;10&#10;2&#10;apple</textarea>
  <div class="lr2-types" id="ts2-modes">
    <button class="lr2-type active" onclick="ts2Mode('az', this)">A &rarr; Z</button>
    <button class="lr2-type" onclick="ts2Mode('za', this)">Z &rarr; A</button>
    <button class="lr2-type" onclick="ts2Mode('len', this)">Shortest first</button>
    <button class="lr2-type" onclick="ts2Mode('len2', this)">Longest first</button>
    <button class="lr2-type" onclick="ts2Mode('nat', this)">Natural 1 &lt; 2 &lt; 10</button>
    <button class="lr2-type" onclick="ts2Mode('rev', this)">Reverse</button>
    <button class="lr2-type" onclick="ts2Mode('shuffle', this)">Shuffle</button>
  </div>
  <div class="lr2-types">
    <label class="pg-switch"><input type="checkbox" id="ts2-ci" checked onchange="ts2Run()" /><span class="pg-track"></span> Ignore case</label>
    <label class="pg-switch"><input type="checkbox" id="ts2-noempty" checked onchange="ts2Run()" /><span class="pg-track"></span> Remove empty lines</label>
    <label class="pg-switch"><input type="checkbox" id="ts2-dedupe" onchange="ts2Run()" /><span class="pg-track"></span> Remove duplicates</label>
  </div>
  <div class="jf-stats" id="ts2-stats"></div>
  <label>Sorted result</label>
  <textarea id="ts2-out" readonly></textarea>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="ts2Copy(this)">Copy result</button>
    <button class="btn ghost" onclick="ts2Download()">Download .txt</button>
    <button class="btn ghost" onclick="ts2Use()">Use as input</button>
  </div>
</div>""",

"lorem-ipsum-generator": """
<div class="panel lr2">
  <div class="lr2-types">
    <button class="lr2-type active" id="lr2-t-paras" onclick="lr2Type('paras', this)">Paragraphs</button>
    <button class="lr2-type" id="lr2-t-sents" onclick="lr2Type('sents', this)">Sentences</button>
    <button class="lr2-type" id="lr2-t-words" onclick="lr2Type('words', this)">Words</button>
    <button class="lr2-type" id="lr2-t-lists" onclick="lr2Type('lists', this)">HTML lists</button>
  </div>
  <div class="row">
    <div><label id="lr2-n-label">Paragraphs</label><input type="number" id="lorem-n" value="3" min="1" max="50" oninput="lr2Live()" /></div>
    <div id="lr2-s-wrap"><label>Sentences per paragraph</label><input type="number" id="lorem-s" value="4" min="1" max="30" oninput="lr2Live()" /></div>
    <div id="lr2-start-wrap"><label class="lr2-opt"><input type="checkbox" id="lr2-start" checked onchange="lr2Gen()" style="width:auto" /> Start with &ldquo;Lorem ipsum dolor sit amet&rdquo;</label></div>
  </div>
  <div class="lr2-stats" id="lr2-stats"></div>
  <div id="lorem-out" class="result mono lr2-out"></div>
  <div class="lr2-actions">
    <button class="btn" onclick="lr2Gen()">Regenerate</button>
    <button class="btn ghost" onclick="lr2Copy(this)">Copy text</button>
    <button class="btn ghost" onclick="lr2CopyHtml(this)">Copy HTML</button>
    <button class="btn ghost" onclick="lr2Download()">Download .txt</button>
  </div>
</div>""",

"word-frequency-counter": """
<div class="panel wf2">
  <label>Text to analyze</label>
  <textarea id="wf-in" oninput="wordFreq()" placeholder="Paste an article, essay or any text&hellip;">Press the sample button and word frequency analysis begins immediately. The bar chart updates as you type, so you can find the words you rely on and vary them. Search engines reward varied vocabulary, and strong writing avoids repeating the same words in every sentence.</textarea>
  <div class="lr2-types" id="wf2-modes">
    <span class="ir2-pl">Show:</span>
    <button class="lr2-type active" id="wf2-top-10" onclick="wf2Top(10)">Top 10</button>
    <button class="lr2-type" id="wf2-top-25" onclick="wf2Top(25)">Top 25</button>
    <button class="lr2-type" id="wf2-top-50" onclick="wf2Top(50)">Top 50</button>
  </div>
  <div class="lr2-types">
    <label class="pg-switch"><input type="checkbox" id="wf2-stop" checked onchange="wordFreq()" /><span class="pg-track"></span> Exclude common words</label>
    <label class="pg-switch"><input type="checkbox" id="wf2-case" onchange="wordFreq()" /><span class="pg-track"></span> Case sensitive</label>
    <label class="pg-switch"><input type="checkbox" id="wf2-pairs" onchange="wordFreq()" /><span class="pg-track"></span> 2-word phrases</label>
  </div>
  <div class="jf-stats" id="wf2-stats"></div>
  <div id="wf-out" class="result"></div>
</div>""",

"hash-generator": """

<div class="panel hg2">
  <label>Text to hash &mdash; updates live, click any hash to copy</label>
  <textarea id="hash-in" oninput="hashGen()" placeholder="Type anything&hellip;">hello world</textarea>
  <div class="lr2-types">
    <label class="pg-switch"><input type="checkbox" id="hg2-s1" checked onchange="hashGen()" /><span class="pg-track"></span> SHA-1</label>
    <label class="pg-switch"><input type="checkbox" id="hg2-s256" checked onchange="hashGen()" /><span class="pg-track"></span> SHA-256</label>
    <label class="pg-switch"><input type="checkbox" id="hg2-s384" onchange="hashGen()" /><span class="pg-track"></span> SHA-384</label>
    <label class="pg-switch"><input type="checkbox" id="hg2-s512" checked onchange="hashGen()" /><span class="pg-track"></span> SHA-512</label>
  </div>
  <div id="hash-out" class="result mono"></div>

  <h3 style="margin:22px 0 4px;font-size:17px">Hash a file instead</h3>
  <p class="tool-note">Drop any file to get its checksums &mdash; ideal for verifying downloads. Files are hashed locally and never uploaded.</p>
  <div class="bi2-drop" id="hg2-drop" ondragover="bi2Drag(event)" ondragleave="bi2Undrag(event)" ondrop="hf2Drop(event)" onclick="hf2Pick()">
    <p><b>Drop a file here</b></p>
    <p class="tool-note">or click to choose one</p>
  </div>
  <input type="file" id="hg2-file" style="display:none" onchange="hf2File(this.files[0])">
  <div class="jf-stats" id="hg2-fstats"></div>
  <label>Verify against an expected checksum (optional)</label>
  <input id="hg2-expect" placeholder="Paste the SHA-256 the download page gave you&hellip;" oninput="hf2Check()">
  <div id="hg2-fout" class="result mono"></div>
</div>
""",

"jwt-decoder": """
<div class="panel jw2">
  <label>JWT token &mdash; decoded live in your browser</label>
  <textarea id="jwt-in" oninput="jwtDecode()" placeholder="eyJhbGciOi&hellip;">eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkphbmUgRG9lIiwicm9sZSI6ImFkbWluIiwiZXhwIjo0MTAyNDQ0ODAwfQ.sig_not_verified_locally</textarea>
  <div class="jf-stats" id="jw2-stats"></div>
  <div id="jwt-out" class="result mono"></div>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="jw2Copy(this)">Copy payload JSON</button>
    <button class="btn ghost" onclick="jw2Sample()">Load sample token</button>
  </div>
</div>""",

"regex-tester": """
<div class="panel re2">
  <div class="row">
    <div style="flex:2"><label>Pattern</label><input type="text" id="re-pattern" value="\\b\\w+@\\w+\\.\\w+\\b" oninput="regexTest()" /></div>
    <div><label>Flags</label><input type="text" id="re-flags" value="gi" oninput="regexTest()" /></div>
  </div>
  <div class="lr2-types" id="re2-presets">
    <span class="ir2-pl">Presets:</span>
    <button class="ir2-preset" onclick="re2Pre('email')">Email</button>
    <button class="ir2-preset" onclick="re2Pre('url')">URL</button>
    <button class="ir2-preset" onclick="re2Pre('date')">Date</button>
    <button class="ir2-preset" onclick="re2Pre('hex')">Hex color</button>
    <button class="ir2-preset" onclick="re2Pre('num')">Number</button>
    <button class="ir2-preset" onclick="re2Pre('ip')">IPv4</button>
  </div>
  <label>Test text</label>
  <textarea id="re-text" oninput="regexTest()" placeholder="Paste text to test against&hellip;">Contact jane@example.com or sales@mscale.tools. Site: https://mslace.vercel.app. Deadline 2026-01-15, alternative 15/01/2026. Colors #ff5733 and #0F0. Server 192.168.1.1 failed. Price: $129.99.</textarea>
  <div class="jf-stats" id="re2-stats"></div>
  <label>Highlighted matches</label>
  <div id="re-out" class="result"></div>
  <label>Matches with capture groups</label>
  <div id="re-groups" class="result mono"></div>
</div>""",

"csv-to-json-converter": """
<div class="panel cj2">
  <div class="uc2-cats jf-stats" id="cj2-delims">
    <span class="ir2-pl">Delimiter:</span>
    <button class="uc2-cat active" onclick="cj2Delim(',', this)">Comma</button>
    <button class="uc2-cat" onclick="cj2Delim(';', this)">Semicolon</button>
    <button class="uc2-cat" onclick="cj2Delim('tb', this)">Tab</button>
    <button class="uc2-cat" onclick="cj2Delim('|', this)">Pipe</button>
  </div>
  <div class="lr2-types">
    <label class="pg-switch"><input type="checkbox" id="cj2-header" checked onchange="csvToJson()" /><span class="pg-track"></span> First row is headers</label>
    <label class="pg-switch"><input type="checkbox" id="cj2-types" checked onchange="csvToJson()" /><span class="pg-track"></span> Detect numbers / booleans / null</label>
    <label class="pg-switch"><input type="checkbox" id="cj2-trim" checked onchange="csvToJson()" /><span class="pg-track"></span> Trim cells</label>
  </div>
  <label>CSV input</label>
  <textarea id="csv-in" oninput="csvToJson()" placeholder="name,age&#10;Alice,30&#10;Bob,25">name,age,active,score&#10;Alice,30,true,91.5&#10;Bob,25,false,88&#10;Carol,41,,95.2</textarea>
  <div class="jf-stats" id="cj2-stats"></div>
  <label>JSON output</label>
  <textarea id="csv-out" readonly></textarea>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="cj2Copy(this)">Copy JSON</button>
    <button class="btn ghost" onclick="cj2Download()">Download .json</button>
  </div>
</div>""",

"html-encoder-decoder": """
<div class="panel he2">
  <div class="lr2-types">
    <button class="lr2-type active" id="he2-enc" onclick="he2Mode('enc')">Encode &rarr;</button>
    <button class="lr2-type" id="he2-dec" onclick="he2Mode('dec')">&larr; Decode</button>
    <span class="ir2-pl" style="margin-left:auto">Escape quotes</span>
    <label class="pg-switch"><input type="checkbox" id="he2-quotes" checked onchange="he2Live()" /><span class="pg-track"></span></label>
  </div>
  <div class="b64-io">
    <div><label>Input</label><textarea id="henc-in" oninput="he2Live()" placeholder="&lt;div class=&quot;hello&quot;&gt;Hi &amp; bye&lt;/div&gt;"><div class="hello">Hi & bye</div></textarea></div>
    <button class="btn ghost sm" onclick="he2Swap()" title="Move output back into input">&#8644;</button>
    <div><label>Output</label><textarea id="henc-out" readonly></textarea></div>
  </div>
  <div class="jf-stats" id="he2-stats"></div>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="he2Copy(this)">Copy output</button>
  </div>
</div>""",

"number-base-converter": """
<div class="panel nb2">
  <div class="uc2-cats jf-stats" id="nb2-bases">
    <span class="ir2-pl">Input base:</span>
    <button class="uc2-cat" data-b="2" onclick="nb2Base(2, this)">BIN</button>
    <button class="uc2-cat" data-b="8" onclick="nb2Base(8, this)">OCT</button>
    <button class="uc2-cat active" data-b="10" onclick="nb2Base(10, this)">DEC</button>
    <button class="uc2-cat" data-b="16" onclick="nb2Base(16, this)">HEX</button>
    <button class="uc2-cat" data-b="36" onclick="nb2Base(36, this)">36</button>
  </div>
  <label>Number</label>
  <input type="text" id="nb-in" value="255" oninput="baseConvert()" placeholder="Enter in the selected base&hellip;" />
  <div class="jf-stats" id="nb2-stats"></div>
  <table class="wc-table"><tbody>
    <tr><th>Binary (base 2)</th><td id="nb2-b2" class="mono">&mdash;</td></tr>
    <tr><th>Octal (base 8)</th><td id="nb2-b8" class="mono">&mdash;</td></tr>
    <tr><th>Decimal (base 10)</th><td id="nb2-b10" class="mono">&mdash;</td></tr>
    <tr><th>Hex (base 16)</th><td id="nb2-b16" class="mono">&mdash;</td></tr>
    <tr><th>Base 32</th><td id="nb2-b32" class="mono">&mdash;</td></tr>
    <tr><th>Base 36</th><td id="nb2-b36" class="mono">&mdash;</td></tr>
  </tbody></table>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="nb2Copy()">Copy all conversions</button>
  </div>
</div>""",

"roman-numeral-converter": """
<div class="panel ro2">
  <label>Number (1&ndash;3999) or Roman numeral &mdash; converted live as you type</label>
  <input type="text" id="roman-in" value="2024" oninput="ro2Live()" placeholder="2024 or MMXXIV" />
  <div class="pct2-result" id="ro2-big">&mdash;</div>
  <div class="jf-stats" id="ro2-break"></div>
  <table class="wc-table ro2-table"><tbody>
    <tr><th>I</th><td>1</td><th>V</th><td>5</td></tr>
    <tr><th>X</th><td>10</td><th>L</th><td>50</th></tr>
    <tr><th>C</th><td>100</td><th>D</th><td>500</th></tr>
    <tr><th>M</th><td>1000</td><th colspan="2">largest: MMMCMXCIX = 3999</td></tr>
  </tbody></table>
  <div class="lr2-actions">
    <button class="btn ghost" onclick="ro2Copy(this)">Copy result</button>
  </div>
</div>""",

"image-resizer": """
<div class="panel ir2">
  <div class="ir2-drop" id="ir2-drop" onclick="document.getElementById('ir2-file').click()">
    [[ic image-tools]]
    <b>Drop an image here</b> or click to browse
    <span>Everything stays on your device \u2014 nothing is uploaded</span>
    <input type="file" id="ir2-file" accept="image/*" onchange="ir2Load()" />
  </div>
  <div id="ir2-controls" style="display:none">
    <div class="ir2-presets">
      <span class="ir2-pl">Quick scale:</span>
      <button class="ir2-preset" onclick="ir2Scale(25)">25%</button>
      <button class="ir2-preset" onclick="ir2Scale(50)">50%</button>
      <button class="ir2-preset" onclick="ir2Scale(75)">75%</button>
      <button class="ir2-preset" onclick="ir2Scale(100)">100%</button>
      <span class="ir2-pl">Sizes:</span>
      <button class="ir2-preset" onclick="ir2Fit(1920,1080)">1920\u00d71080</button>
      <button class="ir2-preset" onclick="ir2Fit(1200,675)">1200\u00d7675</button>
      <button class="ir2-preset" onclick="ir2Fit(1080,1080)">1080\u00d71080</button>
      <button class="ir2-preset" onclick="ir2Fit(800,600)">800\u00d7600</button>
      <button class="ir2-preset" onclick="ir2Fit(400,400)">400\u00d7400</button>
    </div>
    <div class="row">
      <div><label>Width (px)</label><input type="number" id="ir2-w" oninput="ir2OnW()" /></div>
      <div><label>Height (px)</label><input type="number" id="ir2-h" oninput="ir2OnH()" /></div>
      <div><label>Format</label><select id="ir2-fmt" onchange="ir2Apply()"><option value="jpeg">JPG</option><option value="png">PNG</option><option value="webp" selected>WebP</option></select></div>
      <div><label>Quality: <span id="ir2-qv">90</span>%</label><input type="range" id="ir2-q" min="10" max="100" value="90" class="pg-slider" oninput="ir2Q()" /></div>
    </div>
    <label class="pg-switch"><input type="checkbox" id="ir2-lock" checked onchange="ir2Apply()" /><span class="pg-track"></span> Lock aspect ratio</label>
    <div class="ir2-compare">
      <div class="ir2-side">
        <span class="ir2-tag">Before</span>
        <img id="ir2-before" alt="Original image" />
        <p class="ir2-meta" id="ir2-meta-a"></p>
      </div>
      <div class="ir2-arrow">\u2192</div>
      <div class="ir2-side">
        <span class="ir2-tag ir2-tag-after">After</span>
        <img id="ir2-preview" alt="Resized preview" />
        <p class="ir2-meta" id="ir2-meta-b"></p>
      </div>
    </div>
    <div class="ir2-actions">
      <button class="btn" onclick="ir2Apply()">Resize &amp; convert</button>
      <a id="ir2-download" class="btn" style="display:none" download>\u2193 Download</a>
    </div>
  </div>
</div>""",

"palette-generator": """
<div class="panel pg3">
  <div class="cc2-picker">
    <input type="color" id="pal-cc" value="#ff7000" oninput="pg2FromPicker()" aria-label="Pick base color" />
    <div class="cc2-picker-col">
      <label>Base color (hex)</label>
      <input type="text" id="pal-in" value="#ff7000" oninput="genPalette()" placeholder="#ff7000" class="cc2-hex" />
      <div id="pal-err" class="error"></div>
    </div>
    <button class="btn ghost sm" onclick="pg2Random()">Random</button>
  </div>
  <div class="pg3-modes">
    <button class="lr2-type active" id="pg2-m-shades" onclick="pg2Mode('shades', this)">Shades &amp; tints</button>
    <button class="lr2-type" id="pg2-m-comp" onclick="pg2Mode('comp', this)">Complementary</button>
    <button class="lr2-type" id="pg2-m-analog" onclick="pg2Mode('analog', this)">Analogous</button>
    <button class="lr2-type" id="pg2-m-triad" onclick="pg2Mode('triad', this)">Triadic</button>
    <button class="lr2-type" id="pg2-m-tetrad" onclick="pg2Mode('tetrad', this)">Tetradic</button>
    <button class="lr2-type" id="pg2-m-mono" onclick="pg2Mode('mono', this)">Monochromatic</button>
  </div>
  <p class="tool-note">Click a swatch to copy its hex:</p>
  <div id="pal-out" class="pal-row"></div>
  <div class="lr2-actions">
    <button class="btn ghost sm" onclick="pg2CopyCss(this)">Copy CSS variables</button>
    <button class="btn ghost sm" onclick="pg2CopyTailwind(this)">Copy Tailwind config</button>
  </div>
</div>""",
}


TOOL_DESC = {
    "password-strength-checker": "Check any password's real strength: entropy in bits, offline crack-time estimate and a fix-it checklist. Runs privately in your browser.",
    "cron-expression-explainer": "Translate any 5-field cron expression into plain English and see its next five run times before it surprises you in production.",
    "css-gradient-generator": "Design linear gradients with two colour pickers and an angle slider, live preview and copy-ready CSS output.",
    "box-shadow-generator": "Design CSS box shadows with sliders for offset, blur, spread, colour and opacity, live preview and copy-ready code.",
    "text-to-speech": "Read any text aloud with the voices installed on your device, with speed and pitch control. Private, free and unlimited.",
    "typing-speed-test": "Measure your typing speed and accuracy with a fresh random word stream, character-level feedback and instant WPM scoring.",
    "pomodoro-timer": "Run automatic 25/5 Pomodoro focus cycles with long breaks every fourth session and a completed-session counter.",
    "url-parser": "Break any URL into scheme, host, port, path, decoded query parameters and fragment using the browser's own URL engine.",
    "qr-code-generator": "Generate QR codes for URLs, text and Wi-Fi credentials with size and error-correction control. Download as PNG, free and private.",
    "text-diff-checker": "Compare two texts line by line and see every addition and removal highlighted. Private diff checking in your browser.",
    "markdown-previewer": "Render Markdown live as you type with a clean preview and copy-ready HTML output. Free, no signup.",
    "image-watermarker": "Add text watermarks to images with position, size, opacity and color control. Runs entirely in your browser.",
    "favicon-generator": "Create the complete favicon size set (16 to 512 px) from any logo, with ready-to-paste link tags.",
    "base64-image-encoder": "Convert images to Base64 data URIs with HTML img and CSS background snippets. Free and private.",
    "stopwatch-online": "Free online stopwatch with lap times, splits, pause and resume. Accurate timestamp-based timing.",
    "countdown-timer": "Count down to any date and time with a live days, hours, minutes and seconds display and progress bar.",
    "json-to-csv-converter": "Convert a JSON array of objects into a clean CSV for Excel or Google Sheets. Quote-aware, private and free, right in your browser.",
    "pdf-merge": "Merge two or more PDF files into one document in your browser. Private, free and no upload — files never leave your device.",
    "pdf-split": "Extract specific pages or page ranges from a PDF into a new file. Runs entirely in your browser with full quality preserved.",
    "image-compressor": "Compress JPG, PNG and WebP images in your browser with a quality slider and size preview. Free, private, no upload.",
    "image-cropper": "Crop images to exact pixel coordinates in your browser, with optional resize. Private, free and no watermarks.",
    "meta-tag-generator": "Generate complete meta, Open Graph and Twitter card tags with live Google and social previews for any page.",
    "keyword-density-checker": "Analyse keyword density in any text: top one, two and three-word phrases with counts and percentages, stopword filter included.",
    "xml-sitemap-generator": "Generate a valid sitemap.xml from your URL list with lastmod, changefreq and priority. Copy or download instantly.",
    "slug-generator": "Convert titles into clean, lowercase URL slugs with accent transliteration, stop-word removal and batch mode.",
    "invoice-generator": "Create professional invoices with line items, automatic tax and totals, then print or save as PDF. Free and private.",
    "percentage-calculator": "Free online percentage calculator: find X% of Y, what percent X is of Y, and percentage increase or decrease.",
    "bmi-calculator": "Calculate your Body Mass Index (BMI) instantly from weight and height, with WHO weight category.",
    "age-calculator": "Calculate your exact age in years, months and days from your date of birth.",
    "loan-emi-calculator": "Calculate monthly loan payments (EMI), total interest and total repayment.",
    "word-counter": "Count words, characters, sentences and paragraphs, plus estimated reading time.",
    "case-converter": "Convert text between UPPERCASE, lowercase, Title Case, Sentence case, camelCase, snake_case and kebab-case.",
    "remove-duplicate-lines": "Remove duplicate lines from any list or text, with case-insensitive and trim options.",
    "reverse-text": "Reverse the characters, words or lines of any text instantly.",
    "json-formatter": "Beautify, validate and minify JSON online. Format JSON with 2 or 4 spaces.",
    "base64-encoder-decoder": "Encode text to Base64 or decode Base64 to text. UTF-8 safe, runs in your browser.",
    "url-encoder-decoder": "URL-encode or decode text and query strings online.",
    "uuid-generator": "Generate random UUID v4 identifiers in bulk. Up to 100 at a time.",
    "unit-converter": "Convert between length, weight, data size and temperature units instantly.",
    "timestamp-converter": "Convert Unix timestamps to human dates and back, with a live epoch clock.",
    "password-generator": "Generate strong, random passwords locally in your browser with entropy estimate.",
    "color-converter": "Convert colors between HEX, RGB and HSL with a live preview swatch.",
    "random-number-generator": "Generate random numbers in any range, with optional unique values.",
    "dice-roller": "Roll up to 20 dice with 4 to 100 sides. Great for board games and D&D.",
    "coin-flipper": "Flip a coin online. One flip or hundreds, with heads/tails counts.",
    "discount-calculator": "Calculate sale price, savings and final price with optional sales tax.",
    "tip-calculator": "Calculate tip amount, total bill and per-person split for any tip percentage.",
    "compound-interest-calculator": "Calculate compound interest with contributions, yearly to daily compounding.",
    "gst-vat-calculator": "Add or remove GST, VAT or sales tax from any amount instantly.",
    "date-difference-calculator": "Find the exact duration between two dates in days, weeks, months and years.",
    "find-and-replace": "Find and replace text online with case sensitivity and regular expression support.",
    "text-sorter": "Sort text lines alphabetically, by length, or shuffle them randomly.",
    "lorem-ipsum-generator": "Generate Lorem Ipsum placeholder text by paragraphs and sentences.",
    "word-frequency-counter": "Analyze word frequency in any text with a visual bar chart of the top words.",
    "hash-generator": "Generate SHA-1, SHA-256 and SHA-512 hashes of any text instantly in your browser.",
    "jwt-decoder": "Decode JWT tokens to inspect the header and payload, with expiry checking.",
    "regex-tester": "Test regular expressions online with live match highlighting and capture groups.",
    "csv-to-json-converter": "Convert CSV or TSV data to JSON. Quote-aware parsing, runs entirely in your browser.",
    "html-encoder-decoder": "Escape text to HTML entities or decode HTML back to plain text.",
    "number-base-converter": "Convert numbers between binary, octal, decimal and hexadecimal.",
    "roman-numeral-converter": "Convert Roman numerals to numbers and numbers to Roman numerals.",
    "image-resizer": "Resize and convert images in your browser — nothing is uploaded to any server.",
    "palette-generator": "Generate tints and shades from any hex color. Click a swatch to copy.",
}

# ---- MEGA expansion: 101 new tools (engines live in assets/tools.js) ----
from content import MEGA as _MEGA
for _s, _m in _MEGA.items():
    LIVE.append((_s, _m["name"], _m["cat"], _m["short"]))
    TOOL_BODIES[_s] = _m["body"]
    TOOL_DESC[_s] = _m["desc"]
_MEGA_CATS = {}
for _s, _m in _MEGA.items():
    _MEGA_CATS.setdefault(_m["cat"], []).append(_s)
for _k, _v in CAT_PAGES.items():
    if _v[0] in _MEGA_CATS:
        CAT_PAGES[_k] = (_v[0], _v[1], _v[2] + _MEGA_CATS[_v[0]], _v[3])

def article_wordcount(c):
    texts = list(c["intro"]) + [c["how"][0]] + list(c["steps"]) + list(c["works"])
    texts += [f"{t} {b}" for t, b in c["examples"]]
    texts += list(c.get("mistakes", []))
    texts += list(c["tips"])
    texts += [f"{q} {a}" for q, a in c["faqs"]]
    return len(re.findall(r"[A-Za-z0-9'\u2019\-]+", " ".join(texts)))


def article_html(slug, name):
    c = CONTENT[slug]
    out = ['<div class="article">']
    out.append(f'<h2 class="section">What Is the {esc(name)}?</h2>')
    out += [f"<p>{esc(p)}</p>" for p in c["intro"]]
    out.append(f'<h2 class="section">How to Use the {esc(name)}</h2>')
    out.append(f"<p>{esc(c['how'][0])}</p>")
    out.append("<ol>" + "".join(f"<li>{esc(s)}</li>" for s in c["steps"]) + "</ol>")
    out.append(f'<h2 class="section">How the {esc(name)} Works</h2>')
    out += [f"<p>{esc(p)}</p>" for p in c["works"]]
    out.append('<h2 class="section">Examples and Practical Use Cases</h2>')
    for t, b in c["examples"]:
        out.append(f"<h3>{esc(t)}</h3><p>{esc(b)}</p>")
    if c.get("mistakes"):
        out.append('<h2 class="section">Common Mistakes to Avoid</h2>')
        out.append("<ul>" + "".join(f"<li>{esc(m)}</li>" for m in c["mistakes"]) + "</ul>")
    out.append('<h2 class="section">Tips, Benefits and Limitations</h2>')
    out.append("<ul>" + "".join(f"<li>{esc(t)}</li>" for t in c["tips"]) + "</ul>")
    out.append('<h2 class="section">Frequently Asked Questions</h2>')
    for q, a in c["faqs"]:
        out.append(f"<h3>{esc(q)}</h3><p>{esc(a)}</p>")
    out.append("</div>")
    return "\n".join(out)


def _slufigy(s):
    s = re.sub(r"[^a-z0-9\s-]", "", s.lower()).strip()
    return re.sub(r"[\s_]+", "-", s)


BASE_URL = "https://maisamwork.github.io/MSCALE/"


def full_blocks(post):
    """Base blocks enriched: quick answer + comparison table before the FAQ, conclusion + references after."""
    from content import blog_enriched_blocks
    pre, post_extra = blog_enriched_blocks(post["slug"])
    blocks = list(post["blocks"])
    faq_i = next((i for i, (k, _) in enumerate(blocks) if k == "faq"), len(blocks))
    return blocks[:faq_i] + pre + blocks[faq_i:] + post_extra


def _h2_ids(blocks):
    seen, out = {}, []
    for kind, val in blocks:
        if kind == "h2":
            base = _slufigy(val) or "sec"
            seen[base] = seen.get(base, 0) + 1
            out.append((base if seen[base] == 1 else f"{base}-{seen[base]}", val))
    return out


def blog_wordcount(post):
    texts = []
    for kind, val in full_blocks(post):
        if kind in ("p", "h2", "h3", "callout"):
            texts.append(val)
        elif kind in ("ul", "ol"):
            texts.extend(val)
        elif kind == "faq":
            texts.extend(f"{q} {a}" for q, a in val)
        elif kind == "table":
            texts.extend(str(h) for h in val["headers"])
            for row in val["rows"]:
                texts.extend(str(c) for c in row)
        elif kind == "refs":
            texts.extend(t for t, _ in val)
    return len(re.findall(r"[A-Za-z0-9'\u2019\-]+", " ".join(texts)))


def blog_blocks_html(post):
    out = []
    for kind, val in full_blocks(post):
        if kind == "p":
            out.append(f"<p>{esc(val)}</p>")
        elif kind == "h2":
            out.append(("H2", val))
        elif kind == "h3":
            out.append(f"<h3>{esc(val)}</h3>")
        elif kind in ("ul", "ol"):
            tag = "ul" if kind == "ul" else "ol"
            out.append(f"<{tag}>" + "".join(f"<li>{esc(i)}</li>" for i in val) + f"</{tag}>")
        elif kind == "table":
            head = "".join(f"<th>{esc(str(h))}</th>" for h in val["headers"])
            rows = "".join("<tr>" + "".join(f"<td>{esc(str(c))}</td>" for c in r) + "</tr>" for r in val["rows"])
            out.append(f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>')
        elif kind == "callout":
            out.append(f'<div class="quick-answer"><span class="qa-tag">Quick answer</span><p>{esc(val)}</p></div>')
        elif kind == "refs":
            lis = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{esc(t)}</a></li>' for t, u in val)
            out.append(f'<ul class="refs">{lis}</ul>')
        elif kind == "faq":
            out.append('<h2 class="section" id="faqs">Frequently Asked Questions</h2>')
            for q, a in val:
                out.append(f"<h3>{esc(q)}</h3><p>{esc(a)}</p>")
    # assign ids to h2s in a second pass
    ids = iter(_h2_ids(full_blocks(post)))
    final = []
    for chunk in out:
        if isinstance(chunk, tuple) and chunk[0] == "H2":
            hid, txt = next(ids)
            final.append(f'<h2 class="section" id="{hid}">{esc(txt)}</h2>')
        else:
            final.append(chunk)
    return "\n".join(final)


def build_blog_images():
    """Generate 16:9 featured images (1200/768/480, WebP + PNG) with the brand gradient."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Pillow not installed - skipping blog image generation")
        return False
    import os
    os.makedirs(f"{ROOT}/assets/blog", exist_ok=True)
    for post in BLOG_POSTS:
        slug, title = post["slug"], post["title"]
        for w in (1200, 768, 480):
            h = int(w * 675 / 1200)
            png, webp = f"{ROOT}/assets/blog/{slug}-{w}.png", f"{ROOT}/assets/blog/{slug}-{w}.webp"
            if os.path.exists(png) and os.path.exists(webp):
                continue
            img = Image.new("RGB", (w, h))
            dr = ImageDraw.Draw(img)
            top, bot = (26, 22, 38), (255, 122, 26)
            for y in range(h):
                t = y / h
                dr.line([(0, y), (w, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
            # subtle grid dots
            dot = max(1, w // 400)
            for gx in range(0, w, max(28, w // 24)):
                for gy in range(0, h, max(28, h // 12)):
                    dr.ellipse([gx, gy, gx + dot, gy + dot], fill=(255, 255, 255, 18))
            # brand chip
            pad = w // 24
            dr.rounded_rectangle([pad, pad, pad + w // 5, pad + h // 9], radius=h // 24, fill=(255, 122, 26))
            try:
                f_small = ImageFont.load_default(size=max(14, h // 18))
                f_big = ImageFont.load_default(size=max(22, h // 8))
            except TypeError:
                f_small = f_big = ImageFont.load_default()
            dr.text((pad + w // 90, pad + h // 40), "MSCALE Tools", font=f_small, fill=(255, 255, 255))
            # wrapped title
            words, lines, cur = title.split(), [], ""
            for wd in words:
                trial = (cur + " " + wd).strip()
                if f_big.getlength(trial) > w - 2 * pad and cur:
                    lines.append(cur)
                    cur = wd
                else:
                    cur = trial
            if cur:
                lines.append(cur)
            lines = lines[:3]
            ty = h / 2 - len(lines) * h / 12
            for ln in lines:
                dr.text((pad, ty), ln, font=f_big, fill=(255, 255, 255))
                ty += h / 6
            # bottom bar
            dr.rectangle([0, h - h // 14, w, h], fill=(255, 122, 26))
            img.save(png, optimize=True)
            try:
                img.save(webp, quality=82, method=6)
            except Exception:
                pass
    print("blog images: generated/verified", len(BLOG_POSTS) * 2, "files per size set")
    return True


def _post_picture(post, eager=False):
    from content import BLOG_META
    m = BLOG_META[post["slug"]]
    alt = esc(m["featured"]["alt"])
    sizes = "(max-width: 760px) 100vw, 760px"
    preload = ' fetchpriority="high"' if eager else ' loading="lazy"'
    return f"""<figure class="featured">
  <picture>
    <source type="image/webp" srcset="../assets/blog/{post['slug']}-480.webp 480w, ../assets/blog/{post['slug']}-768.webp 768w, ../assets/blog/{post['slug']}-1200.webp 1200w" sizes="{sizes}" />
    <img src="../assets/blog/{post['slug']}-1200.png" srcset="../assets/blog/{post['slug']}-480.png 480w, ../assets/blog/{post['slug']}-768.png 768w, ../assets/blog/{post['slug']}-1200.png 1200w" sizes="{sizes}" alt="{alt}" width="1200" height="675" decoding="async"{preload} />
  </picture>
  <figcaption>{esc(m['featured']['caption'])} <span class="img-credit">Image: {esc(m['featured']['credit'])}</span></figcaption>
</figure>"""


def blog_post_html(post):
    from content import BLOG_META
    m = BLOG_META[post["slug"]]
    seo = m["seo"]
    blocks = blog_blocks_html(post)
    toc = _h2_ids(full_blocks(post))
    words = blog_wordcount(post)
    reading = max(1, round(words / 200))
    canonical = f"{BASE_URL}blog/{post['slug']}.html"
    og_img = f"{BASE_URL}assets/blog/{post['slug']}-1200.png"
    sizes = "(max-width: 760px) 100vw, 760px"
    meta_desc = esc(seo["meta_desc"])
    extra_head = (
        f'<link rel="canonical" href="{canonical}"/>\n'
        f'<meta name="robots" content="{esc(seo.get("robots", "index, follow"))}"/>\n'
        f'<meta name="keywords" content="{esc(seo["focus_keyword"] + ", " + ", ".join(seo["secondary_keywords"]))}"/>\n'
        f'<meta property="og:title" content="{esc(seo["seo_title"])}"/>\n'
        f'<meta property="og:description" content="{meta_desc}"/>\n'
        f'<meta property="og:image" content="{og_img}"/>\n'
        f'<meta property="og:image:width" content="1200"/>\n'
        f'<meta property="og:image:height" content="675"/>\n'
        f'<meta property="og:url" content="{canonical}"/>\n'
        f'<meta property="og:type" content="article"/>\n'
        f'<meta name="twitter:card" content="summary_large_image"/>\n'
        f'<meta name="twitter:title" content="{esc(seo["seo_title"])}"/>\n'
        f'<meta name="twitter:description" content="{meta_desc}"/>\n'
        f'<meta name="twitter:image" content="{og_img}"/>\n'
        f'<link rel="preload" as="image" href="../assets/blog/{post["slug"]}-768.webp" imagesrcset="../assets/blog/{post["slug"]}-480.webp 480w, ../assets/blog/{post["slug"]}-768.webp 768w, ../assets/blog/{post["slug"]}-1200.webp 1200w" imagesizes="{sizes}"/>\n'
    )
    faq = next((v for k, v in full_blocks(post) if k == "faq"), [])
    schemas = [
        {"@context": "https://schema.org", "@type": "Article",
         "headline": seo["seo_title"], "description": seo["meta_desc"],
         "image": [f"{BASE_URL}assets/blog/{post['slug']}-1200.png"],
         "datePublished": m["date"], "dateModified": m["updated"],
         "inLanguage": "en",
         "author": {"@type": m["author"]["type"], "name": m["author"]["name"], "url": m["author"]["url"]},
         "publisher": {"@type": "Organization", "name": "MSCALE Tools",
                       "logo": {"@type": "ImageObject", "url": BASE_URL + "assets/favicon.svg"}},
         "mainEntityOfPage": {"@type": "WebPage", "@id": canonical}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList",
         "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": BASE_URL + "blog/"},
            {"@type": "ListItem", "position": 3, "name": post["title"], "item": canonical}]},
    ]
    if faq:
        schemas.append({"@context": "https://schema.org", "@type": "FAQPage",
                        "mainEntity": [{"@type": "Question", "name": q,
                                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    jsonld = "".join(f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in schemas)
    toc_html = "".join(f'<a href="#{hid}">{esc(txt)}</a>' for hid, txt in toc)
    author = m["author"]
    initials = "".join(w[0] for w in author["name"].split()[:2])
    other_posts = [p for p in BLOG_POSTS if p["slug"] != post["slug"]]
    rel_articles = "".join(
        f'<a class="side-link" href="{p["slug"]}.html"><b>{esc(p["title"])}</b><span>{max(1, round(blog_wordcount(p) / 200))} min read</span></a>'
        for p in other_posts
    )
    rel_tools = "".join(
        f'<a class="side-link" href="../tools/{s}.html"><b>{n}</b><span>{CAT_SLUG_BY_NAME.get(c, "")}</span></a>'
        for s, n, c, _ in LIVE if s in m.get("related_tools", [])[:3]
    )
    pop_articles = "".join(
        f'<a class="side-link" href="{p["slug"]}.html"><b>{esc(p["title"])}</b><span>{p["date"]}</span></a>'
        for p in BLOG_POSTS[:2]
    )
    return (
        header(f'{seo["seo_title"]} | MSCALE Tools Blog', seo["meta_desc"], "../", extra_head=extra_head)
        + f"""{jsonld}
<nav class="breadcrumb" aria-label="Breadcrumb">
<a href="../index.html">{svg_icon("wrench", "crumb-ic")}Home</a>
<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
<a href="../blog/">Blog</a>
<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
<span>{esc(post["title"])}</span>
</nav>
<div class="post-layout">
<article class="prose post-full">
  <div class="post-cats"><a class="chip chip-cat" href="../blog/">{esc(m["category"])}</a></div>
  <h1>{esc(post["title"])}</h1>
  <p class="post-lead">{esc(post["desc"])}</p>
  <div class="post-byline">
    <span class="avatar" aria-hidden="true">{initials}</span>
    <div>
      <b>{esc(author["name"])} <a class="byline-link" href="{author["url"]}">profile</a></b>
      <span class="post-dates">Published {m["date"]} &middot; Updated {m["updated"]} &middot; {reading} min read</span>
    </div>
  </div>
  {_post_picture(post, eager=True)}
  {blocks}
</article>
<aside class="post-side" aria-label="Article sidebar">
  <div class="side-box"><div class="side-title">On this page</div><nav class="toc">{toc_html}</nav></div>
  <div class="side-box"><div class="side-title">Related tools</div>{rel_tools}</div>
  <div class="side-box"><div class="side-title">Related articles</div>{rel_articles}</div>
  <div class="side-box"><div class="side-title">Popular articles</div>{pop_articles}</div>
  <div class="side-box side-news">
    <div class="side-title">Newsletter</div>
    <p>New tools and guides, straight to your inbox.</p>
    <form onsubmit="return nlSub(event)">
      <input type="email" required placeholder="you@email.com" />
      <button class="btn" type="submit">Subscribe</button>
    </form>
    <div id="nl-msg" class="tool-note"></div>
  </div>
</aside>
</div>
{ad_slot("post-bottom", "970 \u00d7 120")}
<section class="cat-sec"><h2 class="section">Try these tools</h2>
<div class="grid">{"".join(f'<a class="card" href="../tools/{s}.html"><div class="card-head">{svg_icon(CAT_SLUG_BY_NAME.get(c, "wrench"), "card-ic", hue_of(CAT_SLUG_BY_NAME.get(c, "wrench")))}<h3>{n}</h3></div><p>{d}</p><span class="tag live">LIVE</span></a>' for s, n, c, d in LIVE[:4])}</div></section>"""
        + footer("../")
    )


def blog_index_html():
    from content import BLOG_META
    cards = "".join(
        f"""<a class="card blog-card" href="{p['slug']}.html">
<figure class="blog-thumb"><img src="../assets/blog/{p['slug']}-768.webp" onerror="this.onerror=null;this.src='../assets/blog/{p['slug']}-768.png'" alt="{esc(BLOG_META[p['slug']]['featured']['alt'])}" width="768" height="432" loading="lazy" decoding="async" /></figure>
<div class="blog-card-body"><span class="chip chip-cat">{esc(BLOG_META[p['slug']]['category'])}</span>
<h3>{esc(p["title"])}</h3>
<p>{esc(p["desc"])}</p>
<span class="post-meta">{p["date"]} &middot; {max(1, round(blog_wordcount(p) / 200))} min read</span></div>
</a>"""
        for p in BLOG_POSTS
    )
    hero = BLOG_POSTS[0]
    hm = BLOG_META[hero["slug"]]
    return (
        header("Blog | MSCALE Tools", "Practical guides on word counts, password security, JSON, images and getting the most from online tools.", "../")
        + f"""<div class="tool-head"><div class="tool-title">""" + svg_icon("book-open", "tool-ic big") + f"""<h1>Blog</h1></div>
<p>Practical, in-depth guides from the MSCALE Tools team. Every article is a full read, no fluff.</p></div>
{ad_slot("blog-top", "970 \u00d7 120")}
<a class="blog-hero" href="{hero["slug"]}.html">
  {_post_picture(hero)}
  <div class="blog-hero-body">
    <span class="chip chip-cat">Featured &middot; {esc(hm["category"])}</span>
    <h2>{esc(hero["title"])}</h2>
    <p>{esc(hero["desc"])}</p>
    <span class="post-meta">{hm["date"]} &middot; {max(1, round(blog_wordcount(hero) / 200))} min read</span>
  </div>
</a>
<div class="blog-grid">""" + cards + "</div>" + footer("../")
    )


def gen_sitemap():
    import datetime
    from xml.dom import minidom
    urls = [""]
    for d in sorted(os.listdir(ROOT)):
        if os.path.isdir(f"{ROOT}/{d}") and os.path.exists(f"{ROOT}/{d}/index.html") and d not in ("assets", "data", "content", "blog", "tools", "__pycache__"):
            urls.append(f"{d}/")
    for f in sorted(os.listdir(f"{ROOT}/tools")):
        if f.endswith(".html") and f != "index.html":
            urls.append(f"tools/{f}")
    urls.append("tools/")
    urls.append("blog/")
    for f in sorted(os.listdir(f"{ROOT}/blog")):
        if f.endswith(".html") and f != "index.html":
            urls.append(f"blog/{f}")
    today = datetime.date.today().isoformat()
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        lines.append(f"<url><loc>{BASE_URL}{u}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq></url>")
    lines.append("</urlset>")
    with open(f"{ROOT}/sitemap.xml", "w") as f:
        f.write("\n".join(lines))
    minidom.parse(f"{ROOT}/sitemap.xml")
    print(f"sitemap: {len(urls)} URLs, XML valid")


def tools_index_html(catalog):
    live_names = {s: (n, d) for s, n, _, d in LIVE}
    cat_name = {slug: v[0] for slug, v in CAT_PAGES.items()}
    live_per, cat_per = {}, {}
    for s, n, c, d in LIVE:
        cs = CAT_SLUG_BY_NAME.get(c, "calculators")
        live_per[cs] = live_per.get(cs, 0) + 1
    for item in catalog:
        cat_per[item["c"]] = cat_per.get(item["c"], 0) + 1
    total_live = len(LIVE)
    total_catalog = len(catalog)
    side = f"""<button class="side-item active" data-cat="all"><span>Complete catalog</span><em>{total_live + total_catalog}</em></button>"""
    for slug in CAT_PAGES:
        n = live_per.get(slug, 0) + cat_per.get(slug, 0)
        side += (f"<button class='side-item' data-cat='{slug}'><span class='side-dot' style='background:{hue_of(slug)}'></span>"
                 f"<span>{cat_name[slug]}</span><em>{n}</em></button>")
    side += """<div class="side-note">Live tools work right now. Catalog tools are coming soon — new ones ship weekly.</div>"""
    side += """<div class="side-news">
      <div class="side-title">Newsletter</div>
      <p>New tools and guides, straight to your inbox. No spam, unsubscribe anytime.</p>
      <form onsubmit="return nlSub(event)">
        <input type="email" required placeholder="you@email.com">
        <button class="btn" type="submit">Subscribe</button>
      </form>
      <div id="nl-msg" class="tool-note"></div>
    </div>"""
    return (
        header(f"Explore {total_live + total_catalog}+ Free Online Tools | MSCALE Tools",
               f"Search and filter the full MSCALE toolbox: {total_live} live tools and {total_catalog} more coming soon. 100% private, no sign-up, everything runs in your browser.", "../")
        + f"""<nav class="breadcrumb" aria-label="Breadcrumb">
<a href="../index.html">{svg_icon("wrench", "crumb-ic")}Home</a>
<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
<span>All tools</span>
</nav>
<div class="tools-head">
  <h1>Explore {total_live + total_catalog}+ <em>free tools</em></h1>
  <p>Search and filter the most complete browser-based toolbox. 100% private, no sign-up, instant results.</p>
</div>
<div class="tools-stats">
  <span class="stat-chip"><b>{total_live}</b> tools live</span>
  <span class="stat-chip"><b>{len(CAT_PAGES)}</b> categories</span>
  <span class="stat-chip"><b>100%</b> free</span>
  <span class="stat-chip">No sign-up</span>
  <span class="stat-chip">Runs in your browser</span>
</div>
<div class="cat-chips" id="cat-chips">
  <span class="chips-label">Browse by category</span>
  <button class="chip active" data-cat="all"><span class="chip-ic" style="color:var(--accent)">{svg_icon("wrench")}</span>All</button>
  {"".join(f"<button class='chip' data-cat='{slug}'><span class='chip-ic' style='color:{hue_of(slug)}'>{svg_icon(slug)}</span>{cat_name[slug]}</button>" for slug in CAT_PAGES)}
</div>
{ad_slot("tools-top")}
<div class="tools-layout">
  <aside class="tools-side" id="tools-side">{side}</aside>
  <div class="tools-main">
    <div class="tools-controls">
      <div class="search-wrap big-search">
        {svg_icon("search", "search-ic")}
        <input id="tools-search" placeholder="Search {total_live + total_catalog:,} tools (e.g. 'word counter', 'password')" />
        <button id="tools-clear" class="search-clear" type="button" aria-label="Clear search">{svg_icon("x")}</button>
        <kbd class="search-kbd" aria-hidden="true">/</kbd>
      </div>
      <div class="sort-wrap">
        {svg_icon("arrow-down-up", "sort-ic")}
        <select id="tools-sort" aria-label="Sort tools">
          <option value="pop">Popular first</option>
          <option value="az">A to Z</option>
          <option value="za">Z to A</option>
        </select>
      </div>
    </div>
    <p id="tools-count" class="tools-count"></p>
    <div class="grid" id="tools-grid"></div>
    <div style="text-align:center;margin-top:22px"><button id="tools-more" class="btn ghost" style="display:none">Load more tools</button></div>
    {ad_slot("tools-feed", "970 × 160")}
    <div class="banner-cta">
      <div><b>Every tool you need right here in your browser.</b><span>Free, private, no sign-up — {total_live} tools live today.</span></div>
      <div class="banner-btns">
        <a class="btn" href="word-counter.html">Try Now</a>
        <a class="btn ghost" href="https://github.com/maisamwork/MSCALE/issues/new" target="_blank" rel="noopener">Submit a tool</a>
      </div>
    </div>
  </div>
</div>"""
        + footer("../")
    )


def tool_page(slug, name, cat, desc):
    cat_slug = CAT_SLUG_BY_NAME.get(cat, "calculators")
    body = re.sub(r"\[\[ic ([a-z0-9-]+)\]\]", lambda m: svg_icon(m.group(1), "ic-inline"), TOOL_BODIES[slug])
    related = [(s, n) for s, n, c, _ in LIVE if c == cat and s != slug][:4]
    rel_html = ""
    if related:
        rel_html = "<h2 class='section'>Related tools</h2><div class='grid'>" + "".join(
            f"<a class='card' href='../tools/{s}.html'><div class='card-head'>{svg_icon(cat_slug, 'card-ic', hue_of(cat_slug))}<h3>{n}</h3></div></a>"
            for s, n in related
        ) + "</div>"
    crumb = f"""<nav class="breadcrumb" aria-label="Breadcrumb">
<a href="../index.html">{svg_icon("wrench", "crumb-ic")}Home</a>
<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
<a href="../{cat_slug}/">{cat}</a>
<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
<span>{name}</span>
</nav>"""
    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": name,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "Web",
        "description": desc,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
    })
    article = article_html(slug, name)
    return (
        header(f"{name} — Free Online Tool | MSCALE Tools", desc, "../")
        + f"""<div class="tool-wrap">
{crumb}
<script type="application/ld+json">{jsonld}</script>
<div class="tool-head"><div class="tool-title">{svg_icon(cat_slug, "tool-ic")}<h1>{name}</h1></div><p>{desc}</p></div>
{body}
{ad_slot('tool-top', '970 × 120')}
{article}
{rel_html}
</div>"""
        + footer("../")
    )


def build_catalog():
    global CATALOG
    wb = load_workbook(DATA_XLSX, read_only=True)
    catalog = []
    ws = wb["All Tools"]
    for row in ws.iter_rows(min_row=2, values_only=True):
        name, cat, sub = row[0], row[1], row[2]
        target = CATALOG_CATS.get(cat)
        if not target:
            continue
        catalog.append({"n": name, "c": target, "s": sub or ""})
    per_cat = {}
    result = []
    for item in sorted(catalog, key=lambda x: x["n"].lower()):
        c = item["c"]
        if per_cat.get(c, 0) >= 150:
            continue
        per_cat[c] = per_cat.get(c, 0) + 1
        result.append(item)
    os.makedirs(f"{ROOT}/data", exist_ok=True)
    json.dump(result, open(f"{ROOT}/data/catalog.json", "w"), ensure_ascii=False)
    CATALOG = result
    return result

def ad_slot(key, size="728 × 90"):
    """Reusable ad placement slot. Swap the placeholder for real ad network code later."""
    return (
        f"<div class='ad-slot' data-ad-slot='{key}' aria-label='Advertisement'>"
        f"<span class='ad-tag'>Ad</span>"
        f"<div class='ad-ph'>{size} ad space — paste your ad network code here</div>"
        f"</div>"
    )


HERO_ILLO = """<svg class="hero-illo" viewBox="0 0 440 330" fill="none" aria-hidden="true">
  <defs>
    <linearGradient id="illo-o" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff7000"/><stop offset="1" stop-color="#ff9a3c"/></linearGradient>
    <linearGradient id="illo-v" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a78bfa"/><stop offset="1" stop-color="#7c3aed"/></linearGradient>
  </defs>
  <rect x="30" y="52" width="250" height="168" rx="16" fill="var(--card2)" stroke="var(--border2)"/>
  <rect x="46" y="68" width="218" height="136" rx="9" fill="var(--bg)"/>
  <rect x="66" y="150" width="24" height="42" rx="4" fill="url(#illo-o)" opacity=".55"/>
  <rect x="100" y="128" width="24" height="64" rx="4" fill="url(#illo-o)" opacity=".75"/>
  <rect x="134" y="108" width="24" height="84" rx="4" fill="url(#illo-o)"/>
  <polyline points="66,96 108,84 150,88 196,70 240,60" stroke="url(#illo-v)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="240" cy="60" r="4.5" fill="#a78bfa"/>
  <rect x="104" y="220" width="102" height="12" rx="6" fill="var(--border2)"/>
  <circle cx="348" cy="226" r="58" stroke="url(#illo-v)" stroke-width="3"/>
  <ellipse cx="348" cy="226" rx="26" ry="58" stroke="url(#illo-v)" stroke-width="2" opacity=".7"/>
  <path d="M292 210h112M292 242h112" stroke="url(#illo-v)" stroke-width="2" opacity=".7"/>
  <rect x="268" y="34" width="140" height="58" rx="12" fill="var(--card2)" stroke="var(--border2)"/>
  <circle cx="292" cy="63" r="11" fill="url(#illo-o)"/>
  <rect x="312" y="50" width="82" height="8" rx="4" fill="var(--border2)"/>
  <rect x="312" y="66" width="58" height="8" rx="4" fill="var(--border)" />
  <rect x="60" y="252" width="120" height="44" rx="10" fill="var(--card2)" stroke="var(--border2)"/>
  <circle cx="82" cy="274" r="9" fill="url(#illo-v)"/>
  <rect x="98" y="264" width="66" height="7" rx="3.5" fill="var(--border2)"/>
  <rect x="98" y="277" width="44" height="7" rx="3.5" fill="var(--border)"/>
</svg>"""


def index_page(catalog):
    cat_counts = {}
    for item in catalog:
        cat_counts[item["c"]] = cat_counts.get(item["c"], 0) + 1
    live_by_cat = {}
    for s, n, c, d in LIVE:
        cs = CAT_SLUG_BY_NAME.get(c, "calculators")
        live_by_cat.setdefault(cs, []).append((s, n))
    cat_cards = ""
    for slug, (name, _, _, _) in CAT_PAGES.items():
        n = len(live_by_cat.get(slug, []))
        cat_cards += (f"<a class='cat-card' href='{slug}/'><span class='icon-box' style='color:{hue_of(slug)};background:{hue_of(slug)}22'>{svg_icon(slug)}</span>"
                      f"<h3>{name}</h3><p><span class='cat-count'>{n} live tools</span><span class='cat-arrow'>{svg_icon('arrow-right')}</span></p></a>")
    popular_slugs = ["word-counter", "password-generator", "json-formatter", "case-converter"]
    live_by_slug = {s: (n, c, d) for s, n, c, d in LIVE}
    popular_cards = "".join(
        f"<a class='card pop-card' href='tools/{s}.html'><div class='card-head'>{svg_icon(CAT_SLUG_BY_NAME.get(live_by_slug[s][1], 'wrench'), 'card-ic', hue_of(CAT_SLUG_BY_NAME.get(live_by_slug[s][1], 'wrench')))}<h3>{live_by_slug[s][0]}</h3></div><p>{live_by_slug[s][2]}</p><span class='btn btn-sm'>Open Tool</span></a>"
        for s in popular_slugs if s in live_by_slug
    )
    featured_slugs = ["percentage-calculator", "json-formatter", "qr-code-generator", "password-generator",
                      "unit-converter", "color-converter", "image-resizer", "loan-emi-calculator"]
    featured_cards = "".join(
        f"<a class='card' href='tools/{s}.html'><div class='card-head'>{svg_icon(CAT_SLUG_BY_NAME.get(live_by_slug[s][1], 'wrench'), 'card-ic', hue_of(CAT_SLUG_BY_NAME.get(live_by_slug[s][1], 'wrench')))}<h3>{live_by_slug[s][0]}</h3></div><p>{live_by_slug[s][2]}</p><span class='tag'>LIVE</span></a>"
        for s in featured_slugs if s in live_by_slug
    )
    blog_cards = "".join(
        f"<a class='card blog-card' href='blog/{p['slug']}.html'><h3>{esc(p['title'])}</h3><p>{esc(p['desc'])}</p><span class='post-meta'>{p['date']}</span></a>"
        for p in BLOG_POSTS
    )
    total = len(catalog) + len(LIVE)
    return header("MSCALE Tools — Free Online Tools", "Discover better tools. Free online calculators, text tools, developer tools, converters and more. Fast, private, no sign-up.") + f"""
<div class="hero hero-new">
  <div class="hero-copy">
    <p class="hero-kicker">Software &bull; AI &bull; Digital Growth</p>
    <h1>Discover better tools. <em>Work smarter.</em> Grow faster.</h1>
    <p class="hero-sub">Practical software guides, free online tools and technology resources for businesses, creators and learners worldwide. Everything runs right in your browser.</p>
    <form class="hero-search" action="tools/" method="get" role="search">
      {svg_icon("search", "search-ic")}
      <input id="search" name="q" placeholder="Search tools, articles and guides&hellip;" />
      <button class="btn" type="submit">Search</button>
    </form>
    <div class="cta-row">
      <a class="btn" href="tools/">Explore Free Tools</a>
      <a class="btn ghost" href="blog/">Read the Blog</a>
    </div>
  </div>
  <div class="hero-art">{HERO_ILLO}</div>
</div>
{ad_slot("home-hero")}
<section class="features">
  <div class="feature"><span class="f-tile" style="color:#ff9a3c;background:rgba(255,154,60,.14)">{svg_icon("zap")}</span><div><b>Fast &amp; free</b><span>No sign-up, no limits</span></div></div>
  <div class="feature"><span class="f-tile" style="color:#34d399;background:rgba(52,211,153,.14)">{svg_icon("shield-check")}</span><div><b>100% private</b><span>Everything runs on your device</span></div></div>
  <div class="feature"><span class="f-tile" style="color:#60a5fa;background:rgba(96,165,250,.14)">{svg_icon("smartphone")}</span><div><b>Works anywhere</b><span>Desktop, tablet and mobile</span></div></div>
  <div class="feature"><span class="f-tile" style="color:#a78bfa;background:rgba(167,139,250,.14)">{svg_icon("converters")}</span><div><b>Always growing</b><span>New tools added regularly</span></div></div>
</section>
<div class="sec-head"><h2 class="section">Popular Free Tools</h2><a class="sec-link" href="tools/">View all tools {svg_icon("arrow-right")}</a></div>
<div class="grid">{popular_cards}</div>
{ad_slot("home-mid", "970 × 210")}
<div class="sec-head"><h2 class="section">Explore Categories</h2><a class="sec-link" href="tools/">View all categories {svg_icon("arrow-right")}</a></div>
<div class="cat-grid">{cat_cards}</div>
<div class="sec-head"><h2 class="section">Featured tools</h2><a class="sec-link" href="tools/">Browse everything {svg_icon("arrow-right")}</a></div>
<div class="grid">{featured_cards}</div>
{ad_slot("home-pre-blog")}
<h2 class="section">From the blog</h2>
<div class="blog-grid">{blog_cards}</div>
""" + footer("")


CAT_ABOUT = {
    "calculators": (
        "Calculators are the most-used category on MSCALE because they answer everyday questions in seconds. "
        "Whether you are checking a percentage increase on a price tag, working out a loan repayment, or splitting "
        "a restaurant bill, the tools in this section give you an instant answer without ads getting in the way or "
        "an account being required. Each calculator has been built with a single job in mind, so the interface stays "
        "clean and the result appears the moment you finish typing.",
        "Every calculator here runs entirely inside your browser. The numbers you enter are never transmitted to a "
        "server, stored in a database, or shared with third parties, which makes the tools safe to use for salary "
        "figures, loan amounts and other personal information. They also work on phones and tablets, so you can run "
        "a quick calculation while standing in a shop or reviewing a contract.",
        [
            "Check percentage change between two prices before negotiating a deal",
            "Estimate monthly EMI payments before speaking to a lender",
            "Work out discounts and sale prices during shopping seasons",
            "Calculate BMI and simple health metrics in seconds",
            "Compute compound interest to compare savings options",
        ],
    ),
    "text-tools": (
        "Text tools solve the small annoyances that interrupt writing every day: a paragraph pasted with inconsistent "
        "capitalisation, a list full of duplicate lines, or a document that must hit an exact word count. The tools in "
        "this category handle those jobs instantly. Paste your text, click once, and copy the cleaned result back — "
        "no formatting is lost and nothing is uploaded anywhere.",
        "Writers, students, marketers and developers all rely on these utilities. A content writer can verify that an "
        "article meets a 1,000-word requirement, a student can normalise the case of copied notes, and a developer can "
        "strip whitespace or sort lines before committing a config file. Because processing happens locally in your "
        "browser, even confidential drafts and private notes are safe to paste.",
        [
            "Count words, characters, sentences and reading time for essays and articles",
            "Convert text between UPPERCASE, lowercase, Title Case and Sentence case",
            "Remove duplicate lines and empty lines from lists and logs",
            "Sort lines alphabetically or reverse them",
            "Find and replace text across a whole document at once",
        ],
    ),
    "developer-tools": (
        "Developer tools on MSCALE are built for speed: format a broken JSON payload, decode a JWT to inspect its "
        "claims, convert CSV to JSON for a test fixture, or encode a string to Base64 for an API call. Each tool "
        "opens instantly, works offline once loaded, and shows clear errors when input is malformed instead of "
        "silently returning wrong results.",
        "Nothing you paste leaves your machine. That matters when you are working with tokens, internal API responses "
        "or customer data that must never be sent to an unknown server. The tools use the same parsing rules as modern "
        "browsers and runtimes, so formatted output matches what your application expects, and pretty-printed JSON is "
        "ready to paste straight into your editor.",
        [
            "Pretty-print and validate JSON from APIs and log files",
            "Decode JWTs to inspect header and payload claims",
            "Convert CSV data to JSON for tests and mock endpoints",
            "Encode and decode Base64, URL-encode and HTML-escape strings",
            "Generate UUIDs and inspect timestamps for debugging",
        ],
    ),
    "converters": (
        "Unit conversion is a daily necessity: a recipe in ounces, a laptop spec in inches, a file size in megabytes, "
        "or a timestamp in a log file that needs to become a readable date. The converters in this category handle "
        "those switches instantly and show precise results with sensible rounding, so you never have to search for a "
        "conversion formula again.",
        "All conversion logic runs locally using exact conversion factors, and results update as you type. The tools "
        "cover length, weight, temperature, data storage, number systems and time, and each one includes the most "
        "commonly needed targets by default instead of hiding them behind dropdowns. This makes them fast enough to "
        "use mid-conversation or while writing a report.",
        [
            "Convert length and distance between metric and imperial units",
            "Switch weight units for cooking, shipping and fitness",
            "Translate file sizes between bytes, KB, MB and GB",
            "Convert binary, decimal, hex and octal number systems",
            "Turn Unix timestamps into human-readable dates and back",
        ],
    ),
    "security": (
        "Security tools are the ones you hope you never need but should use weekly. The password generator creates "
        "long, random passwords using your browser's cryptographically secure random number generator, and the hash "
        "utilities let you verify file integrity without installing anything. Because generation happens on your own "
        "device, no password or hash input is ever transmitted, logged or stored.",
        "A strong password is long, unique and unpredictable — this category helps with all three. Generate a distinct "
        "password for every account, check that hash utilities produce the exact digest format your system expects, "
        "and avoid the common mistakes that make passwords crackable, such as dictionary words, personal dates and "
        "short lengths. The tools explain their output so you can make informed choices rather than clicking blindly.",
        [
            "Generate strong random passwords with custom length and character sets",
            "Create memorable passphrases for accounts you type often",
            "Compute MD5, SHA-1 and SHA-256 hashes to verify downloads",
            "Learn which password habits put accounts at risk",
            "Keep credentials private — everything runs on your device",
        ],
    ),
    "color-tools": (
        "Color tools turn a vague idea — \"that shade from the screenshot\" — into exact values you can hand to a "
        "designer or paste into CSS. Convert between HEX, RGB and HSL, build matching palettes, and grab tints and "
        "shades of a brand color in one click. Values are shown in every format simultaneously, so nothing is lost "
        "moving between design tools and code.",
        "Consistent color is what separates an amateur interface from a professional one. These tools help you keep "
        "hex codes consistent across a website, generate accessible darker variants for hover states, and translate "
        "a color picked from an image into the HSL values a design system expects. Everything updates live as you "
        "type or pick, and your color never leaves the browser.",
        [
            "Convert HEX to RGB and HSL and back again",
            "Build tints and shades for hover states and dark themes",
            "Generate matching palettes from a single brand color",
            "Copy CSS-ready values with one click",
            "Preview colors against light and dark backgrounds",
        ],
    ),
    "random-generators": (
        "Random generators handle the moments when a decision needs to be left to chance: picking a raffle winner, "
        "rolling dice for a board game, flipping a coin, or drawing a random number for a giveaway. The tools use "
        "your browser's random engine, so results are fair and cannot be predicted or influenced by anyone — "
        "including us.",
        "Fairness matters when randomness decides something people care about. These generators produce fresh results "
        "on every click, display them clearly, and never remember previous draws. Teachers use them to pick students, "
        "streamers use them for giveaways, and developers use them for quick test values. Because everything runs "
        "locally, the tools keep working even with no internet connection after the page loads.",
        [
            "Flip a coin for quick yes-or-no decisions",
            "Roll one or more dice with any number of sides",
            "Draw random numbers in any range for giveaways",
            "Pick a random item from a list of names or options",
            "Generate test data and sample values for development",
        ],
    ),
    "pdf-tools": (
        "PDF tools remove the friction from working with documents: merge several files into one before emailing them, "
        "split a long PDF into single chapters, or compress a scan so it fits an attachment limit. The tools in this "
        "category process files directly in your browser using modern PDF libraries, which means your documents are "
        "never uploaded to a server.",
        "That local processing is the key difference from most online PDF sites. Contracts, invoices, ID scans and "
        "medical documents stay on your device from start to finish. The workflow is deliberately simple — drop a "
        "file, choose an action, download the result — and output quality is preserved so text stays selectable and "
        "searchable after merging or splitting.",
        [
            "Merge multiple PDFs into a single ordered document",
            "Split a PDF by page ranges for sharing chapters",
            "Compress large scans to meet email attachment limits",
            "Keep text selectable — no rasterising or quality loss",
            "Process private documents without uploading them anywhere",
        ],
    ),
    "image-tools": (
        "Image tools cover the three jobs people need most often: resizing, converting and compressing. Resize a photo "
        "to exact dimensions for a profile picture, convert between PNG, JPG and WebP for a website, or shrink a large "
        "image so a page loads fast. All processing happens in your browser using canvas technology — files are never "
        "uploaded.",
        "Because the work happens locally, even large photos process in seconds and private images never leave your "
        "device. The tools expose the settings that matter — dimensions, format and quality — without burying them in "
        "menus, and they preserve aspect ratio by default so nothing comes out stretched. Results download instantly "
        "with sensible file names.",
        [
            "Resize images to exact pixel dimensions for profiles and thumbnails",
            "Convert between PNG, JPG and WebP formats",
            "Compress photos to reduce page weight and load faster",
            "Crop images to standard aspect ratios",
            "Optimise images without uploading them to any server",
        ],
    ),
    "seo-web-tools": (
        "SEO and web tools help you understand how a page looks to search engines and visitors before you publish it. "
        "Preview and validate meta titles and descriptions, check keyword density in a draft, and inspect the tags "
        "that control how snippets appear in search results. Catching these details early is far easier than "
        "discovering them after a page has been indexed.",
        "Search visibility is built from hundreds of small signals, but a handful of them matter most: a clear title "
        "tag, an accurate meta description, sensible heading structure and focused content. The tools in this category "
        "check exactly those elements and explain what good looks like, so you can fix issues yourself without an SEO "
        "audit. Everything analyses text you paste — no crawling, no account, no data collection.",
        [
            "Preview and validate meta titles and descriptions",
            "Check keyword density and stuffing in draft content",
            "Analyse heading structure for clarity and hierarchy",
            "Inspect how snippets appear in search results",
            "Audit pages before publishing, not after indexing",
        ],
    ),
    "date-time-tools": (
        "Date and time tools settle the questions that cause real mistakes: how many days between two dates, what a "
        "Unix timestamp means, what time it is for a colleague in another timezone, or how old someone is in exact "
        "years, months and days. The answers update instantly and account for leap years automatically.",
        "These tools are used for deadlines, contracts, travel planning and server logs. A countdown to a project due "
        "date, an age calculation for a form, or a timestamp conversion while debugging an API all take seconds. "
        "Because the calculations run in your browser with your local timezone respected by default, the results match "
        "what your calendar and your systems actually show.",
        [
            "Calculate the difference between two dates in days, months and years",
            "Convert Unix timestamps to readable dates and back",
            "Work out exact age in years, months and days",
            "Count down to deadlines, launches and events",
            "Check current time across timezones for scheduling",
        ],
    ),
    "finance-tools": (
        "Finance calculators turn vague money questions into concrete numbers: what a loan actually costs per month, "
        "how much interest compounds over five years, or what a salary works out to after tax. The tools in this "
        "category use standard financial formulas and show a clear breakdown, so you can compare options instead of "
        "guessing.",
        "The calculators are built for quick decision-making — comparing two loan offers, checking whether a "
        "subscription is worth it, or estimating savings growth. Inputs are plain numbers with no sign-up and no data "
        "collection, and results include the totals that matter: monthly payment, total interest and overall cost. "
        "They are estimates for planning, not financial advice, but they give you a solid number to work from.",
        [
            "Calculate loan EMI with interest breakdown",
            "Project compound interest on savings over time",
            "Work out take-home pay from gross salary",
            "Compare costs before accepting a credit offer",
            "Plan budgets with clear monthly totals",
        ],
    ),
}

CAT_POPULAR = {
    "calculators": ["percentage-calculator", "loan-emi-calculator", "age-calculator"],
    "text-tools": ["word-counter", "case-converter", "text-diff-checker"],
    "developer-tools": ["json-formatter", "slug-generator", "cron-expression-explainer"],
    "converters": ["unit-converter", "roman-numeral-converter", "binary-converter"],
    "security": ["password-generator", "password-strength-checker", "hash-generator"],
    "color-tools": ["color-converter", "css-gradient-generator", "color-palette-generator"],
    "random-generators": ["random-number-generator", "random-name-picker", "dice-roller"],
    "pdf-tools": ["pdf-merge", "pdf-split", "pdf-to-image"],
    "image-tools": ["image-resizer", "image-compressor", "image-cropper"],
    "seo-web-tools": ["meta-tag-generator", "xml-sitemap-generator", "keyword-density-checker"],
    "date-time-tools": ["date-difference", "countdown-timer", "stopwatch-online"],
    "finance-tools": ["invoice-generator", "compound-interest-pro", "roi-calculator"],
}

CAT_ADVANCED = {
    "calculators": [
        ("Chain calculations into workflows", "Run one calculator, carry its result into the next: compute a percentage change, feed it into the loan calculator as an extra payment, then check the break-even point of the decision. Each tool keeps its inputs, so a whole analysis takes under a minute."),
        ("Reverse any calculation", "Every formula here works in both directions. Know the payment you can afford but not the loan size, or the final grade but not the exam score needed? Enter what you have and read the missing number straight off the result panel."),
        ("Sanity-check quoted numbers", "Vendors and lenders quote rounded, optimistic figures. Recompute their numbers independently with exact inputs - the difference between their figure and yours is usually a fee or an assumption worth questioning."),
    ],
    "text-tools": [
        ("Audit content against hard limits", "Meta descriptions, tweets, ad headlines and abstracts all have exact character ceilings. Draft in the word counter, trim to the limit, then run the case converter and diff checker to polish the final version without leaving the browser."),
        ("Compare two versions line by line", "The diff checker is not just for code: paste two drafts of the same paragraph and see exactly which words changed. It is the fastest way to review an edit someone else made, or to check what a rewrite actually altered."),
        ("Normalize messy imported text", "Text pasted from PDFs and spreadsheets arrives with broken casing, doubled spaces and smart quotes. Run the cleanup and case tools in sequence to produce consistent, searchable text before publishing."),
    ],
    "developer-tools": [
        ("Validate API payloads before shipping", "Paste a real response into the JSON formatter to catch trailing commas, duplicate keys and silent unicode issues before your parser hits them in production. Format, inspect, then minify the corrected version for fixtures."),
        ("Generate production-ready identifiers", "Use the slug generator and hash tools to produce consistent URL slugs, cache keys and ids instead of hand-rolling transformations that drift between services and break routing."),
        ("Debug cron and encoding issues", "Paste a cron expression to see every next run time, and decode base64 payloads inline when an API returns opaque strings. Both run offline, so nothing leaves your machine during incident work."),
    ],
    "converters": [
        ("Read the reference table, not just the answer", "Every converter prints a table of nearby values around your result - use it when a recipe, spec or drawing needs several related conversions and you want them consistent in one glance."),
        ("Chain units through a common base", "For compound units like speed, price per weight or data transfer, convert to the base unit first, do the arithmetic, then convert back. The swap button makes the reverse check a single click."),
        ("Verify supplier and spec sheets", "Specs often mix metric and imperial. Convert every figure to one system before comparing products - a 10% advantage frequently disappears once units are honestly equalized."),
    ],
    "security": [
        ("Grade passwords before you reuse them", "Run candidate passwords through the strength checker to see crack-time estimates against modern hardware, then generate a replacement from the generator with length 16+ and copy it straight into your manager."),
        ("Use generated secrets as building blocks", "Generator output is ideal for Wi-Fi keys, dev API tokens and encryption passphrases. Generate, then store - never improve a random string by hand, because human edits destroy entropy."),
        ("Make security checks a habit, not a project", "A 30-second strength check on every new account beats an annual password purge. Pair the two tools: generate on signup, verify on audit."),
    ],
    "color-tools": [
        ("Build accessible palettes from one seed", "Start from your brand hex, generate tints and shades, then run the contrast checker on every text and background pair. You get a palette that is both coherent and WCAG-compliant in one pass."),
        ("Translate color between design and code", "Designers think in HSL, CSS wants hex or rgb. The converters keep both views in sync, so a request like 10% lighter becomes an exact lightness change instead of guesswork."),
        ("Extract and rebuild gradients", "Recreate a gradient you like by sampling its endpoints, converting them, then regenerating it with the gradient tool - adjusting the angle and stops until it matches."),
    ],
    "random-generators": [
        ("Run fair draws you can defend", "For giveaways, raffles and team splits, use the pickers and shufflers instead of drawing names by hand - the result is unbiased and you can rerun it publicly to show it is honest."),
        ("Sample realistic test data", "Random words, dates and country names make better demo datasets than typing test, test, test. Generate a batch, paste it into your spreadsheet or seed script, and your UI finally shows real-world variety."),
        ("Break decision deadlocks", "Yes/no, letter, dice - when a choice is truly symmetric, commit to randomness in advance and let the tool decide. It removes the bias that quietly favors the first option."),
    ],
    "pdf-tools": [
        ("Split, reorder and remerge without installs", "Break a 200-page PDF into chapters with the split tool, then merge the parts you need back into a clean handout. Everything happens client-side, so confidential documents never leave your device."),
        ("Prepare documents for signing", "Extract just the pages a counterparty needs, merge them into one file, and the signature packet is ready in minutes - no full document shared, no desktop software required."),
        ("Clean up scanned bundles", "Scanners produce bloated, unordered files. Split off blanks, merge in the right order, and the archive becomes smaller, ordered and actually usable."),
    ],
    "image-tools": [
        ("Hit exact upload limits in two passes", "Resize to the target dimensions first, then compress until the file fits under the platform cap. Resizing before compressing keeps far more quality than compressing a huge image alone."),
        ("Crop for the platform, not the camera", "Aspect ratios differ everywhere: 16:9 for thumbnails, 1:1 for avatars, 4:5 for feeds. Crop once per destination from the same source and every post looks native."),
        ("Batch-prepare page images", "Run every image for a page through resize and compression before upload - pages load visibly faster and you avoid the oversized hero image that quietly doubles load time."),
    ],
    "seo-web-tools": [
        ("Generate complete meta sets per page", "Produce title, description and keyword meta in one pass, paste them into your CMS, and keep every page within search-engine length limits instead of getting truncated in results."),
        ("Keep sitemaps honest", "Regenerate the XML sitemap whenever pages are added or removed and resubmit it in Search Console - crawl budget stops being wasted on URLs that no longer exist."),
        ("Check keyword balance before publishing", "Run the density checker on a draft to catch accidental stuffing and confirm the target term appears naturally - both over-use and total absence cost rankings."),
    ],
    "date-time-tools": [
        ("Plan across units without a calendar", "Add or subtract days from deadlines, count business days for contracts, and compute week numbers for reporting - all three agree because they share the same date engine."),
        ("Turn vague urgency into a number", "Use the countdown timer for public launch moments and the difference tool for how long you actually have - the pair gives the whole team the same visible deadline."),
        ("Time-box work precisely", "Stopwatch for measuring how long a task really takes, pomodoro for keeping focus sprints honest. Measured time is the input that makes every deadline estimate better."),
    ],
    "finance-tools": [
        ("Model a decision end to end", "Price a product with the break-even calculator, check the return with ROI, then project savings growth with compound interest - the three together answer whether it is viable and what it earns."),
        ("Compare offers on true cost", "Run competing loans through the amortization calculator and compare total interest, not monthly payment. The schedule shows exactly where a cheaper-looking offer costs more."),
        ("Turn bills into budget lines", "The electricity cost calculator converts any appliance into an annual figure; do that for your top five devices and your energy budget stops being a guess."),
    ],
}

def category_page(slug, name, icon, live_slugs, catalog_cat):
    live_names_by_slug = {s: (n, d) for s, n, _, d in LIVE}
    hue = hue_of(slug)
    tile = f"<span class='icon-box' style='color:{hue};background:{hue}22'>{svg_icon(slug)}</span>"
    pop_slugs = [s for s in CAT_POPULAR.get(slug, []) if s in live_names_by_slug]
    for s in live_slugs:
        if len(pop_slugs) >= 3:
            break
        if s not in pop_slugs:
            pop_slugs.append(s)
    pop_slugs = pop_slugs[:3]
    pop_tags = ["HOT", "POPULAR", "POPULAR"]
    pop_cards = "".join(
        f"<a class='card pop-feat' data-name='{esc(live_names_by_slug[s][0].lower())}' data-kind='live' href='../tools/{s}.html'>"
        f"<div class='card-head'>{tile}<h3>{live_names_by_slug[s][0]}</h3></div><p>{live_names_by_slug[s][1]}</p>"
        f"<div class='card-foot'><span class='hot-tag {t.lower()}'>{t}</span><span class='btn btn-sm'>Use Tool</span></div></a>"
        for s, t in zip(pop_slugs, pop_tags)
    )
    live_cards = "".join(
        f"<a class='card' data-name='{esc(live_names_by_slug[s][0].lower())}' data-kind='live' href='../tools/{s}.html'>"
        f"<div class='card-head'>{tile}<h3>{live_names_by_slug[s][0]}</h3></div>"
        f"<p>{live_names_by_slug[s][1]}</p><span class='tag live'>LIVE</span></a>"
        for s in live_slugs if s not in pop_slugs
    )
    live_names = {live_names_by_slug[s][0].lower() for s in live_slugs}
    coming = [(i["n"], i.get("s", "")) for i in CATALOG if i["c"] == slug and i["n"].lower() not in live_names][:120]
    coming_cards = "".join(
        f"<div class='card soon' data-name='{esc(n.lower())}' data-kind='soon'><div class='card-head'>{tile}<h3>{esc(n)}</h3></div>"
        f"<p>{esc(d)}</p><span class='tag'>coming soon</span></div>"
        for n, d in coming
    )
    intro = INTROS.get(slug, "")
    a1, a2, bullets = CAT_ABOUT.get(slug, ("", "", []))
    about_html = ""
    if a1:
        lis = "".join(f"<li>{esc(b)}</li>" for b in bullets)
        about_html = (
            f"<section class='about-sec'><h2 class='section'>About {esc(name)}</h2>"
            f"<p>{a1}</p><p>{a2}</p><ul>{lis}</ul></section>"
        )
    adv_items = CAT_ADVANCED.get(slug, [])
    adv_html = ""
    if adv_items:
        adv_cards = "".join(
            f"<div class='adv-item'><span class='adv-num'>{i + 1}</span><div><b>{esc(t)}</b><p>{esc(d)}</p></div></div>"
            for i, (t, d) in enumerate(adv_items)
        )
        adv_html = f"<section class='adv-sec'><h2 class='section'>Advanced use of {esc(name)}</h2><div class='adv-grid'>{adv_cards}</div></section>"
    blog_cards = "".join(
        f"<a class='card blog-card' href='../blog/{p['slug']}.html'><h3>{esc(p['title'])}</h3><p>{esc(p['desc'])}</p><span class='post-meta'>{p['date']}</span></a>"
        for p in BLOG_POSTS
    )
    n_live, n_coming = len(live_slugs), len(coming)
    n_all = n_live + n_coming
    crumb = f"""<nav class="breadcrumb" aria-label="Breadcrumb">
<a href="../index.html">{svg_icon("wrench", "crumb-ic")}Home</a>
<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
<span>{name}</span>
</nav>"""
    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://maisamwork.github.io/MSCALE/"},
            {"@type": "ListItem", "position": 2, "name": name, "item": f"https://maisamwork.github.io/MSCALE/{slug}/"},
        ],
    })
    filter_js = """
(function () {
  var input = document.getElementById('cat-search');
  var cards = [].slice.call(document.querySelectorAll('.grid .card'));
  var note = document.getElementById('cat-count');
  var state = { q: "", kind: "all" };
  function apply() {
    var n = 0;
    cards.forEach(function (c) {
      var hitQ = !state.q || (c.getAttribute('data-name') || '').indexOf(state.q) > -1;
      var hitK = state.kind === 'all' || c.getAttribute('data-kind') === state.kind;
      var hit = hitQ && hitK;
      c.style.display = hit ? '' : 'none';
      if (hit) n++;
    });
    [].slice.call(document.querySelectorAll('.cat-sec')).forEach(function (s) {
      var vis = [].slice.call(s.querySelectorAll('.card')).some(function (c) { return c.style.display !== 'none'; });
      s.style.display = vis ? '' : 'none';
    });
    if (note) note.textContent = (state.q || state.kind !== 'all') ? ('Showing ' + n + ' of ' + cards.length + ' tools') : '';
  }
  if (input) input.addEventListener('input', function () { state.q = input.value.trim().toLowerCase(); apply(); });
  var sbtn = document.getElementById('cat-search-btn');
  if (sbtn) sbtn.addEventListener('click', function () { apply(); });
  var tabs = document.getElementById('cat-tabs');
  if (tabs) tabs.addEventListener('click', function (e) {
    var b = e.target.closest('.cat-tab');
    if (!b) return;
    [].slice.call(tabs.querySelectorAll('.cat-tab')).forEach(function (x) { x.classList.remove('active'); });
    b.classList.add('active');
    state.kind = b.getAttribute('data-kind');
    apply();
  });
  var sort = document.getElementById('cat-sort');
  if (sort) sort.addEventListener('change', function () {
    var grid = document.getElementById('all-grid');
    if (!grid) return;
    var list = [].slice.call(grid.querySelectorAll('.card'));
    if (sort.value === 'az') list.sort(function (a, b) { return (a.getAttribute('data-name') || '') < (b.getAttribute('data-name') || '') ? -1 : 1; });
    else if (sort.value === 'za') list.sort(function (a, b) { return (a.getAttribute('data-name') || '') > (b.getAttribute('data-name') || '') ? -1 : 1; });
    else list.sort(function (a, b) { return (b.getAttribute('data-kind') === 'live' ? 1 : 0) - (a.getAttribute('data-kind') === 'live' ? 1 : 0); });
    list.forEach(function (c) { grid.appendChild(c); });
  });
})();
"""
    return (
        header(f"{name} \u2014 Free Online | MSCALE Tools", f"Free online {name.lower()} \u2014 fast, private, no sign-up.", "../")
        + f"""{crumb}
<script type="application/ld+json">{jsonld}</script>
<div class="cat-hero">
  <span class="icon-box cat-hero-ic" style="color:{hue};background:{hue}22">{svg_icon(slug)}</span>
  <div>
    <h1>{name}</h1>
    <p>{intro}</p>
    <p class="cat-stats"><b>{n_live} live tools</b> \u00b7 {n_coming}+ more coming \u00b7 100% free \u00b7 no sign-up</p>
  </div>
</div>
<div class="cat-search-row">
  <div class="cat-search-wrap">
    {svg_icon("search", "search-ic")}
    <input id="cat-search" placeholder="Search in {name.lower()} (e.g. 'password', 'convert')\u2026" />
  </div>
  <button id="cat-search-btn" class="btn" style="background:{hue}">Search</button>
</div>
<p id="cat-count"></p>
<div class="cat-tabs" id="cat-tabs">
  <button class="cat-tab active" data-kind="all">All <em>{n_all}</em></button>
  <button class="cat-tab" data-kind="live">Online now <em>{n_live}</em></button>
  <button class="cat-tab" data-kind="soon">Coming soon <em>{n_coming}</em></button>
</div>
<section class="cat-sec"><div class="sec-head"><h2 class="section">Most popular {name.lower()}</h2></div>
<div class="grid">{pop_cards}</div></section>
<section class="cat-sec"><div class="sec-head"><h2 class="section">All {name.lower()} tools</h2>
<select id="cat-sort" aria-label="Sort tools"><option value="pop">Sort: Popular first</option><option value="az">Sort: A to Z</option><option value="za">Sort: Z to A</option></select></div>
<p class="all-count">{n_all} tools</p>
<div class="grid" id="all-grid">{live_cards}{coming_cards}</div></section>
{adv_html}
{about_html}
<section class="cat-sec"><h2 class="section">Related guides from our blog</h2>
<div class="blog-grid">{blog_cards}</div></section>
<section class="nl-sec">
  <div><b>Get new {esc(name.lower())} tools first</b><p>One short email when new tools ship. No spam, unsubscribe anytime.</p></div>
  <form onsubmit="return nlSub(event)">
    <input type="email" required placeholder="you@email.com">
    <button class="btn" type="submit">Subscribe</button>
  </form>
  <div id="nl-msg" class="tool-note"></div>
</section>
<p style="margin-top:26px"><a class="btn ghost" href="../tools/">Browse all 1,800+ tools{svg_icon("arrow-right")}</a></p>
{ad_slot("cat-bottom", "970 \u00d7 120")}
<script>{filter_js}</script>"""
        + footer("../")
    )


def main():
    catalog = build_catalog()
    with open(f"{ROOT}/index.html", "w") as f:
        f.write(index_page(catalog))
    os.makedirs(f"{ROOT}/tools", exist_ok=True)
    for slug, (name, icon, live_slugs, catalog_cat) in CAT_PAGES.items():
        os.makedirs(f"{ROOT}/{slug}", exist_ok=True)
        with open(f"{ROOT}/{slug}/index.html", "w") as f:
            f.write(category_page(slug, name, icon, live_slugs, catalog_cat))
    live_by_slug = {s: (n, c) for s, n, c, _ in LIVE}
    for slug, body in TOOL_BODIES.items():
        name, cat = live_by_slug[slug]
        with open(f"{ROOT}/tools/{slug}.html", "w") as f:
            f.write(tool_page(slug, name, cat, TOOL_DESC[slug]))
    live_tools_js = json.dumps(
        [{"name": n, "desc": d, "cat": c, "catSlug": CAT_SLUG_BY_NAME.get(c, "wrench"), "url": "tools/" + s + ".html"} for s, n, c, d in LIVE]
    )
    icons_js = json.dumps({k: svg_icon(k) for k in ICONS})
    appjs = open(f"{ROOT}/assets/app.js").read()
    appjs = appjs.replace("let CATALOG = [];", f"let CATALOG = [];")
    with open(f"{ROOT}/assets/live-tools.js", "w") as f:
        f.write(f"window.LIVE_TOOLS = {live_tools_js};\nwindow.ICONS = {icons_js};")
    css = open(f"{ROOT}/assets/style.css").read()
    open(f"{ROOT}/404.html", "w").write(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Page not found — MSCALE Tools</title>
<meta name="robots" content="noindex"/>
<style>{css}</style>
</head>
<body>
<main class="container" style="text-align:center;padding:100px 20px">
  <h1 style="font-size:64px;margin:0">404</h1>
  <p style="color:var(--muted);font-size:18px">This tool doesn't exist yet — but 1,800+ more are coming.</p>
  <button class="btn" style="margin-top:20px;border:0;cursor:pointer" onclick="location.href=location.pathname.replace(/\\/[^\\/]+\\/[^\\/]*\\/?$/, '/')||'/'">← Back to all tools</button>
</main>
</body>
</html>""")
    os.makedirs(f"{ROOT}/blog", exist_ok=True)
    with open(f"{ROOT}/tools/index.html", "w") as f:
        f.write(tools_index_html(catalog))
    with open(f"{ROOT}/blog/index.html", "w") as f:
        f.write(blog_index_html())
    for post in BLOG_POSTS:
        with open(f"{ROOT}/blog/{post['slug']}.html", "w") as f:
            f.write(blog_post_html(post))
    report = [(s, article_wordcount(CONTENT[s])) for s in TOOL_BODIES]
    oob = [(s, n) for s, n in report if not (1000 <= n <= 1200)]
    if oob:
        raise SystemExit("TOOL CONTENT WORD COUNT OUT OF RANGE (1000-1200): " + repr(oob))
    from content import LENGTH_RANGES, blog_geo_checks, BLOG_META
    for post in BLOG_POSTS:
        wc = blog_wordcount(post)
        lo, hi = LENGTH_RANGES[BLOG_META[post["slug"]]["length"]]
        if not (lo <= wc <= hi):
            raise SystemExit(f'blog/{post["slug"]}: {wc} words outside {BLOG_META[post["slug"]]["length"]} range {lo}-{hi}')
    # --- SEO panel validations ---
    titles = [p["title"] for p in BLOG_POSTS]
    if len(titles) != len(set(titles)):
        raise SystemExit("SEO: duplicate article titles")
    slugs = [p["slug"] for p in BLOG_POSTS]
    if len(slugs) != len(set(slugs)):
        raise SystemExit("SEO: duplicate slugs")
    for post in BLOG_POSTS:
        m, seo = BLOG_META[post["slug"]], BLOG_META[post["slug"]]["seo"]
        md = seo["meta_desc"]
        if not (50 <= len(md) <= 160):
            raise SystemExit(f'SEO {post["slug"]}: meta description {len(md)} chars (guidance: 50-160)')
        if len(seo["seo_title"]) > 65:
            raise SystemExit(f'SEO {post["slug"]}: seo_title {len(seo["seo_title"])} chars > 65')
        if not seo["focus_keyword"]:
            raise SystemExit(f'SEO {post["slug"]}: missing focus keyword')
        blocks = full_blocks(post)
        h1 = [k for k, _ in blocks if k == "h1"]
        if h1:
            raise SystemExit(f'SEO {post["slug"]}: blocks must not contain h1 (template renders the single H1)')
        seen_h2 = False
        for k, _ in blocks:
            if k == "h2":
                seen_h2 = True
            elif k == "h3" and not seen_h2:
                raise SystemExit(f'SEO {post["slug"]}: heading hierarchy broken - h3 before first h2')
        if not m["featured"].get("alt"):
            raise SystemExit(f'SEO {post["slug"]}: featured image missing alt text')
        errs = blog_geo_checks(post, blog_wordcount(post))
        if errs:
            raise SystemExit("GEO/AEO checks failed: " + "; ".join(errs))
    print(f'SEO panel: titles/slugs unique, meta descs in range, H1 + hierarchy OK, alt text OK for {len(BLOG_POSTS)} posts')
    build_blog_images()
    gen_sitemap()
    report_b = [("blog/" + p["slug"], blog_wordcount(p)) for p in BLOG_POSTS]
    all_wc = [n for _, n in report] + [n for _, n in report_b]
    print("word counts OK: %d pages, min %d, max %d" % (len(all_wc), min(all_wc), max(all_wc)))
    print(f"catalog: {len(catalog)} entries; pages written")

main()
