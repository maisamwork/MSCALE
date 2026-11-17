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

def header(title, desc, depth=""):
    nav_items = [
        ("calculators", "Calculators"), ("text-tools", "Text"), ("developer-tools", "Developer"),
        ("converters", "Converters"), ("pdf-tools", "PDF"), ("image-tools", "Image"),
    ]
    nav = "".join(f'<a href="{depth}{slug}/">{name}</a>' for slug, name in nav_items)
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
<script>document.documentElement.setAttribute("data-theme", (function(){{try{{return localStorage.getItem("mscale-theme")||"dark"}}catch(e){{return "dark"}}}})());</script>
<link rel="stylesheet" href="{depth}assets/style.css"/>
<script src="{depth}assets/live-tools.js" defer></script>
<script src="{depth}assets/app.js" defer></script>
<script src="{depth}assets/tools.js" defer></script>
</head>
<body>
<header class="site"><div class="container">
  <a class="brand" href="{depth}index.html"><span class="brand-tile">{svg_icon("wrench")}</span>MSCALE<span>Tools</span></a>
  <nav class="main" id="main-nav">{nav}<a href="{depth}blog/">Blog</a><a class="nav-cta" href="{depth}tools/">All tools</a></nav>
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
  <input type="text" id="pw-in" oninput="pwCheck()" placeholder="Type a test password \u2014 nothing is sent anywhere" autocomplete="off">
  <div class="pw-meter"><div id="pw-fill"></div></div>
  <div id="pw-stats" class="stat-row"></div>
  <div id="pw-out" class="result"></div>
</div>""",
"cron-expression-explainer": """
<div class="panel">
  <label>Cron expression (5 fields)</label>
  <input id="cr-in" oninput="cronExplain()" placeholder="*/15 9-17 * * 1-5" autocomplete="off">
  <div id="cr-out" class="result"></div>
  <label>Next 5 runs (your local time)</label>
  <div id="cr-next" class="result"></div>
</div>""",
"css-gradient-generator": """
<div class="panel">
  <div class="row">
    <div><label>Start colour</label><input type="color" id="gr-c1" value="#ff7000" oninput="grDraw()"></div>
    <div><label>End colour</label><input type="color" id="gr-c2" value="#7c3aed" oninput="grDraw()"></div>
    <div><label>Angle: <span id="gr-angv">135</span>\u00b0</label><input type="range" id="gr-ang" min="0" max="360" value="135" oninput="grDraw()"></div>
  </div>
  <div id="gr-prev" class="gr-prev"></div>
  <label>CSS</label>
  <textarea id="gr-out" readonly style="min-height:80px"></textarea>
  <button class="btn ghost" onclick="copyText('gr-out')">Copy CSS</button>
</div>""",
"box-shadow-generator": """
<div class="panel">
  <div class="row">
    <div><label>X: <span id="bs-xv">0</span>px</label><input type="range" id="bs-x" min="-40" max="40" value="0" oninput="bsDraw()"></div>
    <div><label>Y: <span id="bs-yv">10</span>px</label><input type="range" id="bs-y" min="-40" max="40" value="10" oninput="bsDraw()"></div>
  </div>
  <div class="row">
    <div><label>Blur: <span id="bs-blv">30</span>px</label><input type="range" id="bs-bl" min="0" max="100" value="30" oninput="bsDraw()"></div>
    <div><label>Spread: <span id="bs-spv">-8</span>px</label><input type="range" id="bs-sp" min="-30" max="40" value="-8" oninput="bsDraw()"></div>
  </div>
  <div class="row">
    <div><label>Colour</label><input type="color" id="bs-color" value="#000000" oninput="bsDraw()"></div>
    <div><label>Opacity: <span id="bs-opv">18</span>%</label><input type="range" id="bs-op" min="0" max="100" value="18" oninput="bsDraw()"></div>
    <div><label>Inset</label><input type="checkbox" id="bs-inset" onchange="bsDraw()"></div>
  </div>
  <div class="bs-prev"><div id="bs-box"></div></div>
  <textarea id="bs-out" readonly style="min-height:80px"></textarea>
  <button class="btn ghost" onclick="copyText('bs-out')">Copy CSS</button>
</div>""",
"text-to-speech": """
<div class="panel">
  <label>Text to read aloud</label>
  <textarea id="tts-in" placeholder="Type or paste anything\u2026"></textarea>
  <div class="row">
    <div><label>Voice</label><select id="tts-voice"></select></div>
    <div><label>Speed: <span id="tts-ratev">1</span>\u00d7</label><input type="range" id="tts-rate" min="0.5" max="2" step="0.1" value="1" oninput="document.getElementById('tts-ratev').textContent=this.value"></div>
    <div><label>Pitch</label><input type="range" id="tts-pitch" min="0.5" max="2" step="0.1" value="1"></div>
  </div>
  <div class="row">
    <button class="btn" onclick="ttsPlay()">Speak</button>
    <button class="btn ghost" onclick="ttsStop()">Stop</button>
  </div>
  <div id="tts-msg" class="result"></div>
</div>""",
"typing-speed-test": """
<div class="panel">
  <div id="ty-words" class="ty-words"></div>
  <input id="ty-in" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Click here and start typing\u2026" oninput="tyInput()">
  <div id="ty-stats" class="stat-row"></div>
  <button class="btn ghost" onclick="tyNew()">Restart</button>
</div>""",
"pomodoro-timer": """
<div class="panel">
  <div id="po-mode" class="tool-note" style="text-align:center">Focus session</div>
  <div id="po-display" class="big-time">25:00</div>
  <div class="row">
    <button class="btn" id="po-start" onclick="poToggle()">Start</button>
    <button class="btn ghost" onclick="poSkip()">Skip</button>
    <button class="btn ghost" onclick="poReset()">Reset</button>
  </div>
  <div id="po-count" class="result">Completed focus sessions: 0</div>
</div>""",
"url-parser": """
<div class="panel">
  <label>URL to parse</label>
  <input id="up-in" oninput="urlParse()" placeholder="https://user:pass@sub.example.com:8080/path/page?q=hello&lang=en#section" autocomplete="off">
  <div id="up-out" class="result" style="overflow:auto"></div>
</div>""",

"qr-code-generator": """
<div class="panel">
  <label>Text or URL to encode</label>
  <textarea id="qr-text" placeholder="https://example.com"></textarea>
  <div class="row">
    <div><label>Size</label>
      <select id="qr-size"><option value="200">200 px</option><option value="300" selected>300 px</option><option value="400">400 px</option><option value="500">500 px</option></select></div>
    <div><label>Error correction</label>
      <select id="qr-ecc"><option value="L">L \u2014 smallest</option><option value="M" selected>M \u2014 balanced</option><option value="Q">Q \u2014 robust</option><option value="H">H \u2014 most robust</option></select></div>
  </div>
  <button class="btn" onclick="qrGen()">Generate QR Code</button>
  <div id="qr-box" class="qr-box"></div>
  <button class="btn ghost" onclick="qrDownload()">Download PNG</button>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>""",
"text-diff-checker": """
<div class="panel">
  <div class="row">
    <div style="flex:1;min-width:240px"><label>Original text</label>
      <textarea id="diff-a" style="min-height:170px" placeholder="Paste the original version\u2026"></textarea></div>
    <div style="flex:1;min-width:240px"><label>Changed text</label>
      <textarea id="diff-b" style="min-height:170px" placeholder="Paste the changed version\u2026"></textarea></div>
  </div>
  <button class="btn" onclick="diffRun()">Compare texts</button>
  <div id="diff-out" class="diff-out"></div>
</div>""",
"markdown-previewer": """
<div class="panel">
  <div class="row">
    <div style="flex:1;min-width:240px"><label>Markdown input</label>
      <textarea id="md-in" oninput="mdRender()" style="min-height:280px" placeholder="# Heading&#10;&#10;Some **bold** and *italic* text with a [link](https://example.com)."></textarea></div>
    <div style="flex:1;min-width:240px"><label>Live preview</label>
      <div id="md-out" class="md-out"></div></div>
  </div>
  <button class="btn ghost" onclick="copyText('md-html')">Copy generated HTML</button>
  <textarea id="md-html" style="display:none"></textarea>
</div>""",
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
  <div id="fv-previews" class="fav-row"></div>
  <label>Link tags for your &lt;head&gt;</label>
  <textarea id="fv-tags" readonly style="min-height:130px"></textarea>
  <button class="btn ghost" onclick="copyText('fv-tags')">Copy link tags</button>
</div>""",
"base64-image-encoder": """
<div class="panel">
  <label>Image file</label>
  <input type="file" id="b64-file" accept="image/*" onchange="b64Enc()">
  <div id="b64-info" class="result"></div>
  <label>Data URI</label>
  <textarea id="b64-out" readonly style="min-height:120px"></textarea>
  <div class="row">
    <button class="btn ghost" onclick="copyText('b64-out')">Copy data URI</button>
    <button class="btn ghost" onclick="copyText('b64-html')">Copy HTML img tag</button>
    <button class="btn ghost" onclick="copyText('b64-css')">Copy CSS background</button>
  </div>
  <textarea id="b64-html" style="display:none"></textarea>
  <textarea id="b64-css" style="display:none"></textarea>
</div>""",
"stopwatch-online": """
<div class="panel">
  <div id="sw-display" class="big-time">00:00.00</div>
  <div class="row">
    <button class="btn" id="sw-start" onclick="swStart()">Start</button>
    <button class="btn ghost" onclick="swLap()">Lap</button>
    <button class="btn ghost" onclick="swPause()">Pause</button>
    <button class="btn ghost" onclick="swReset()">Reset</button>
  </div>
  <div id="sw-laps"></div>
</div>""",
"countdown-timer": """
<div class="panel">
  <label>Event name (optional)</label>
  <input id="cd-name" placeholder="Product launch">
  <div class="row">
    <div><label>Date</label><input type="text" id="cd-date" readonly placeholder="Pick a date"></div>
    <div><label>Time</label><input type="text" id="cd-time" readonly placeholder="Pick a time"><input type="hidden" id="cd-time-val" value="09:00"></div>
  </div>
  <button class="btn" onclick="cdStart()">Start countdown</button>
  <div id="cd-units" class="cd-units"></div>
  <div class="cd-bar"><div id="cd-fill"></div></div>
  <div id="cd-msg" class="result"></div>
</div>""",
"json-to-csv-converter": """
<div class="panel">
  <label>JSON array of objects</label>
  <textarea id="j2c-in" placeholder='[{"name": "Ada", "role": "Engineer"}, {"name": "Grace", "role": "Admiral"}]'></textarea>
  <button class="btn" onclick="jsonToCsv()">Convert to CSV</button>
  <label>CSV output</label>
  <textarea id="j2c-out" style="min-height:180px" readonly></textarea>
  <button class="btn" onclick="copyText('j2c-out')">Copy CSV</button>
  <a id="j2c-dl" class="btn ghost" style="display:none;margin-left:6px" download="data.csv">Download .csv</a>
</div>""",

"pdf-merge": """
<script src="https://cdn.jsdelivr.net/npm/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
<div class="panel">
  <label>PDF files (choose two or more, in order)</label>
  <input type="file" id="pm-files" accept="application/pdf" multiple />
  <div id="pm-list" style="margin-top:10px"></div>
  <div class="row"><div><label>Output file name</label><input type="text" id="pm-name" value="merged.pdf" /></div></div>
  <button class="btn" onclick="pdfMerge()">Merge PDFs</button>
  <div id="pm-out" class="result">Select two or more PDF files to merge.</div>
</div>""",
"pdf-split": """
<script src="https://cdn.jsdelivr.net/npm/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
<div class="panel">
  <label>PDF file</label>
  <input type="file" id="ps-file" accept="application/pdf" />
  <label>Pages to keep (e.g. 1-3,5,8-10)</label>
  <input type="text" id="ps-range" placeholder="1-3,5" />
  <div class="row"><div><label>Output file name</label><input type="text" id="ps-name" value="extracted.pdf" /></div></div>
  <button class="btn" onclick="pdfSplit()">Extract pages</button>
  <div id="ps-out" class="result">Select a PDF and type the pages to keep.</div>
</div>""",
"image-compressor": """
<div class="panel">
  <label>Image</label>
  <input type="file" id="ic-file" accept="image/*" />
  <div class="row">
    <div><label>Format</label><select id="ic-fmt"><option value="image/jpeg">JPEG</option><option value="image/webp">WebP</option><option value="image/png">PNG</option></select></div>
    <div><label>Quality: <span id="ic-qv">75</span>%</label><input type="range" id="ic-q" min="10" max="100" value="75" style="padding:0" oninput="document.getElementById('ic-qv').textContent=this.value" /></div>
    <div><label>Max width (px, optional)</label><input type="number" id="ic-w" placeholder="original" /></div>
  </div>
  <button class="btn" onclick="imgCompress()">Compress</button>
  <div id="ic-out" class="result">Select an image to compress.</div>
  <img id="ic-preview" alt="Preview" style="max-width:100%;margin-top:12px;display:none;border-radius:8px" />
  <a id="ic-dl" class="btn ghost" style="display:none;margin-top:10px" download>Download compressed image</a>
</div>""",
"image-cropper": """
<div class="panel">
  <label>Image</label>
  <input type="file" id="icr-file" accept="image/*" />
  <p id="icr-dims" class="tools-count">No image loaded.</p>
  <div class="row">
    <div><label>X</label><input type="number" id="icr-x" value="0" /></div>
    <div><label>Y</label><input type="number" id="icr-y" value="0" /></div>
    <div><label>Width</label><input type="number" id="icr-w" placeholder="to edge" /></div>
    <div><label>Height</label><input type="number" id="icr-h" placeholder="to edge" /></div>
    <div><label>Output width (optional)</label><input type="number" id="icr-ow" placeholder="original" /></div>
  </div>
  <div class="row"><div><label>Format</label><select id="icr-fmt"><option value="image/png">PNG</option><option value="image/jpeg">JPEG</option></select></div></div>
  <button class="btn" onclick="imgCrop()">Apply crop</button>
  <div id="icr-out" class="result">Load an image and set the crop area.</div>
  <img id="icr-preview" alt="Preview" style="max-width:100%;margin-top:12px;display:none;border-radius:8px" />
  <a id="icr-dl" class="btn ghost" style="display:none;margin-top:10px" download>Download cropped image</a>
</div>""",
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
  <label>Google preview</label>
  <div class="result" id="mt-google" style="white-space:normal;font-family:Arial,sans-serif"></div>
  <label>Generated tags</label>
  <textarea id="mt-code" style="min-height:220px" readonly></textarea>
  <button class="btn" onclick="copyText('mt-code')">Copy tags</button>
</div>""",
"keyword-density-checker": """
<div class="panel">
  <label>Text to analyse</label>
  <textarea id="kd-in" placeholder="Paste your article or page text here…"></textarea>
  <label style="text-transform:none;letter-spacing:0"><input type="checkbox" id="kd-stop" checked style="width:auto;margin-right:8px" /> Hide common stop words (the, and, of…)</label>
  <button class="btn" onclick="kwDensity()">Analyse density</button>
  <div id="kd-out" class="result" style="white-space:normal">Paste text and click Analyse.</div>
</div>""",
"xml-sitemap-generator": """
<div class="panel">
  <label>Page URLs (one per line)</label>
  <textarea id="sm-urls" placeholder="https://example.com/&#10;https://example.com/about&#10;https://example.com/blog/post-1"></textarea>
  <div class="row">
    <div><label>Change frequency</label><select id="sm-freq"><option value="">omit</option><option value="daily">daily</option><option value="weekly" selected>weekly</option><option value="monthly">monthly</option><option value="yearly">yearly</option></select></div>
    <div><label>Priority (0.1–1.0)</label><input type="number" id="sm-prio" min="0.1" max="1" step="0.1" placeholder="omit" /></div>
  </div>
  <button class="btn" onclick="sitemapGen()">Generate sitemap</button>
  <label>sitemap.xml</label>
  <textarea id="sm-out" style="min-height:220px" readonly></textarea>
  <button class="btn" onclick="copyText('sm-out')">Copy XML</button>
  <a id="sm-dl" class="btn ghost" style="display:none;margin-left:6px" download="sitemap.xml">Download sitemap.xml</a>
</div>""",
"slug-generator": """
<div class="panel">
  <label>Titles (one per line for batch mode)</label>
  <textarea id="sl-in" placeholder="10 Tips for Better Sleep&#10;Café Culture in Zürich&#10;How to Bake Sourdough"></textarea>
  <div class="row">
    <div><label>Separator</label><select id="sl-sep"><option value="-">Hyphen (-)</option><option value="_">Underscore (_)</option></select></div>
    <div><label>Max length (0 = no limit)</label><input type="number" id="sl-len" value="0" min="0" /></div>
  </div>
  <label style="text-transform:none;letter-spacing:0"><input type="checkbox" id="sl-lower" checked style="width:auto;margin-right:8px" /> Lowercase</label>
  <label style="text-transform:none;letter-spacing:0"><input type="checkbox" id="sl-stop" checked style="width:auto;margin-right:8px" /> Remove stop words (a, the, of, to…)</label>
  <button class="btn" onclick="slugGen()">Generate slugs</button>
  <label>Slugs</label>
  <textarea id="sl-out" style="min-height:140px" readonly></textarea>
  <button class="btn" onclick="copyText('sl-out')">Copy slugs</button>
</div>""",
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
</div>""",
"percentage-calculator": """
<div class="panel">
  <div class="row">
    <div><label>Percentage (%)</label><input type="number" id="pct-x" value="15" /></div>
    <div><label>Of number</label><input type="number" id="pct-y" value="200" /></div>
  </div>
  <button class="btn" onclick="pctCalc()">Calculate</button>
  <div id="pct-out" class="result">Fill in both values to see results.</div>
</div>""",
"bmi-calculator": """
<div class="panel">
  <div class="row">
    <div><label>Weight (kg)</label><input type="number" id="bmi-w" placeholder="70" /></div>
    <div><label>Height (cm)</label><input type="number" id="bmi-h" placeholder="175" /></div>
  </div>
  <button class="btn" onclick="bmiCalc()">Calculate BMI</button>
  <div id="bmi-out" class="result">Enter weight and height.</div>
</div>""",
"age-calculator": """
<div class="panel">
  <label>Date of birth</label>
  <input type="text" id="age-dob" readonly placeholder="Pick your date of birth">
  <button class="btn" onclick="ageCalc()">Calculate age</button>
  <div id="age-out" class="result">Pick your date of birth.</div>
</div>""",
"loan-emi-calculator": """
<div class="panel">
  <div class="row">
    <div><label>Loan amount</label><input type="number" id="emi-p" placeholder="10000" /></div>
    <div><label>Interest rate (% / year)</label><input type="number" id="emi-r" placeholder="7.5" step="0.01" /></div>
    <div><label>Term (years)</label><input type="number" id="emi-n" placeholder="5" /></div>
  </div>
  <button class="btn" onclick="emiCalc()">Calculate EMI</button>
  <div id="emi-out" class="result">Enter loan details.</div>
</div>""",
"word-counter": """
<div class="panel">
  <label>Type or paste text</label>
  <textarea id="wc-in" oninput="wordCount()" placeholder="Start typing…"></textarea>
  <div id="wc-stats" class="stat-row"></div>
  <p class="tool-note">Reference table — pages and time estimates for common document lengths (Letter ≈ 250 words/page, A4 ≈ 500 words/page):</p>
  <div id="wc-table" class="wc-table-wrap"></div>
</div>""",
"case-converter": """
<div class="panel">
  <label>Your text</label>
  <textarea id="case-in" placeholder="Paste text here…"></textarea>
  <div>
    <button class="btn ghost" onclick="convertCase('upper')">UPPERCASE</button>
    <button class="btn ghost" onclick="convertCase('lower')">lowercase</button>
    <button class="btn ghost" onclick="convertCase('title')">Title Case</button>
    <button class="btn ghost" onclick="convertCase('sentence')">Sentence case</button>
    <button class="btn ghost" onclick="convertCase('camel')">camelCase</button>
    <button class="btn ghost" onclick="convertCase('snake')">snake_case</button>
    <button class="btn ghost" onclick="convertCase('kebab')">kebab-case</button>
  </div>
</div>""",
"remove-duplicate-lines": """
<div class="panel">
  <label>Lines</label>
  <textarea id="dd-in" placeholder="One item per line…"></textarea>
  <label><input type="checkbox" id="dd-case" style="width:auto" /> Ignore case</label>
  <label><input type="checkbox" id="dd-trim" checked style="width:auto" /> Trim whitespace</label>
  <button class="btn" onclick="dedupeLines()">Remove duplicates</button>
  <div id="dd-out" class="result mono"></div>
</div>""",
"reverse-text": """
<div class="panel">
  <label>Text</label>
  <textarea id="rev-in" placeholder="Hello world"></textarea>
  <div>
    <button class="btn" onclick="reverseText('chars')">Reverse characters</button>
    <button class="btn ghost" onclick="reverseText('words')">Reverse words</button>
    <button class="btn ghost" onclick="reverseText('lines')">Reverse lines</button>
  </div>
  <div id="rev-out" class="result mono"></div>
</div>""",
"json-formatter": """
<div class="panel">
  <label>JSON</label>
  <textarea id="json-in" placeholder='{"name":"MSCALE","tools":100}'></textarea>
  <div>
    <button class="btn" onclick="jsonFormat(2)">Beautify (2)</button>
    <button class="btn ghost" onclick="jsonFormat(4)">Beautify (4)</button>
    <button class="btn ghost" onclick="jsonFormat(0)">Minify</button>
  </div>
  <div id="json-err" class="error"></div>
  <div id="json-out" class="result mono"></div>
</div>""",
"base64-encoder-decoder": """
<div class="panel">
  <label>Text or Base64</label>
  <textarea id="b64-in"></textarea>
  <div>
    <button class="btn" onclick="b64('enc')">Encode →</button>
    <button class="btn ghost" onclick="b64('dec')">← Decode</button>
  </div>
  <div id="b64-out" class="result mono"></div>
</div>""",
"url-encoder-decoder": """
<div class="panel">
  <label>Text or URL</label>
  <textarea id="url-in"></textarea>
  <div>
    <button class="btn" onclick="urlEnc('enc')">Encode →</button>
    <button class="btn ghost" onclick="urlEnc('dec')">← Decode</button>
  </div>
  <div id="url-out" class="result mono"></div>
</div>""",
"uuid-generator": """
<div class="panel">
  <label>How many UUIDs?</label>
  <input type="number" id="uuid-n" value="5" min="1" max="100" />
  <button class="btn" onclick="uuidGen()">Generate</button>
  <div id="uuid-out" class="result mono"></div>
</div>""",
"unit-converter": """
<div class="panel">
  <label>Category</label>
  <select id="uc-cat" onchange="unitCatChange()">
    <option value="length">Length</option>
    <option value="weight">Weight</option>
    <option value="data">Data size</option>
    <option value="temp">Temperature</option>
  </select>
  <div class="row">
    <div><label>Value</label><input type="number" id="uc-val" value="1" oninput="unitConvert()" /></div>
    <div><label>From</label><select id="uc-from" onchange="unitConvert()"></select></div>
    <div><label>To</label><select id="uc-to" onchange="unitConvert()"></select></div>
  </div>
  <div id="uc-out" class="result big"></div>
</div>""",
"timestamp-converter": """
<div class="panel">
  <p>Current Unix time: <b id="ts-now">…</b></p>
  <label>Unix timestamp → date</label>
  <input type="text" id="ts-in" placeholder="1735689600" />
  <button class="btn" onclick="tsToDate()">Convert</button>
  <div id="ts-out" class="result mono"></div>
  <label>Date → timestamp</label>
  <input type="datetime-local" id="ts-date" />
  <button class="btn" onclick="dateToTs()">Convert</button>
  <div id="ts-out2" class="result mono"></div>
</div>""",
"password-generator": """
<div class="panel">
  <label>Length: <span id="pw-len-val">16</span></label>
  <input type="range" id="pw-len" min="6" max="64" value="16"
    oninput="document.getElementById('pw-len-val').textContent=this.value" />
  <label><input type="checkbox" id="pw-lower" checked style="width:auto" /> lowercase</label>
  <label><input type="checkbox" id="pw-upper" checked style="width:auto" /> UPPERCASE</label>
  <label><input type="checkbox" id="pw-digits" checked style="width:auto" /> digits</label>
  <label><input type="checkbox" id="pw-symbols" checked style="width:auto" /> symbols</label>
  <button class="btn" onclick="genPassword()">Generate password</button>
  <div id="pw-out" class="result mono"></div>
  <p id="pw-strength" style="color:var(--muted);font-size:13px"></p>
</div>""",
"color-converter": """
<div class="panel">
  <label>Hex color</label>
  <input type="text" id="col-in" value="#ff7000" oninput="colorConvert()" placeholder="#ff7000" />
  <div id="col-err" class="error"></div>
  <div id="col-out" class="result"></div>
  <div id="col-swatch" class="swatch"></div>
</div>""",
"random-number-generator": """
<div class="panel">
  <div class="row">
    <div><label>Min</label><input type="number" id="rn-min" value="1" /></div>
    <div><label>Max</label><input type="number" id="rn-max" value="100" /></div>
    <div><label>How many</label><input type="number" id="rn-count" value="1" min="1" max="1000" /></div>
  </div>
  <label><input type="checkbox" id="rn-unique" style="width:auto" /> Unique values only</label>
  <button class="btn" onclick="randNums()">Generate</button>
  <div id="rn-out" class="result"></div>
</div>""",
"dice-roller": """
<div class="panel">
  <div class="row">
    <div><label>Number of dice</label><input type="number" id="dice-n" value="2" min="1" max="20" /></div>
    <div><label>Sides</label><select id="dice-sides"><option>4</option><option selected>6</option><option>8</option><option>10</option><option>12</option><option>20</option><option>100</option></select></div>
  </div>
  <button class="btn" onclick="rollDice()">Roll 🎲</button>
  <div id="dice-out" class="result"></div>
</div>""",
"coin-flipper": """
<div class="panel">
  <label>How many flips?</label>
  <input type="number" id="coin-n" value="1" min="1" max="1000" />
  <button class="btn" onclick="flipCoin()">Flip 🪙</button>
  <div id="coin-out" class="result"></div>
</div>""",

"discount-calculator": """
<div class="panel">
  <div class="row">
    <div><label>Original price</label><input type="number" id="disc-p" placeholder="99.99" /></div>
    <div><label>Discount (%)</label><input type="number" id="disc-off" placeholder="25" /></div>
    <div><label>Tax (%) — optional</label><input type="number" id="disc-tax" placeholder="0" /></div>
  </div>
  <button class="btn" onclick="discountCalc()">Calculate</button>
  <div id="disc-out" class="result">Enter price and discount.</div>
</div>""",
"tip-calculator": """
<div class="panel">
  <div class="row">
    <div><label>Bill amount</label><input type="number" id="tip-bill" placeholder="64.50" /></div>
    <div><label>Tip (%)</label><input type="number" id="tip-pct" value="15" /></div>
    <div><label>Split between</label><input type="number" id="tip-people" value="1" min="1" /></div>
  </div>
  <button class="btn" onclick="tipCalc()">Calculate tip</button>
  <div id="tip-out" class="result">Enter the bill amount.</div>
</div>""",
"compound-interest-calculator": """
<div class="panel">
  <div class="row">
    <div><label>Initial amount</label><input type="number" id="ci-p" placeholder="1000" /></div>
    <div><label>Annual rate (%)</label><input type="number" id="ci-r" placeholder="7" step="0.1" /></div>
    <div><label>Years</label><input type="number" id="ci-t" placeholder="10" /></div>
  </div>
  <div class="row">
    <div><label>Compounds per year</label><select id="ci-n"><option value="1">Yearly</option><option value="4">Quarterly</option><option value="12" selected>Monthly</option><option value="365">Daily</option></select></div>
    <div><label>Monthly contribution — optional</label><input type="number" id="ci-monthly" placeholder="0" /></div>
  </div>
  <button class="btn" onclick="compoundCalc()">Calculate</button>
  <div id="ci-out" class="result">Enter your investment details.</div>
</div>""",
"gst-vat-calculator": """
<div class="panel">
  <div class="row">
    <div><label>Amount</label><input type="number" id="tax-amt" placeholder="100" /></div>
    <div><label>Tax rate (%)</label><input type="number" id="tax-rate" value="18" step="0.1" /></div>
  </div>
  <button class="btn" onclick="taxCalc('add')">Add tax →</button>
  <button class="btn ghost" onclick="taxCalc('remove')">← Remove tax</button>
  <div id="tax-out" class="result">Enter amount and rate.</div>
</div>""",
"date-difference-calculator": """
<div class="panel">
  <div class="row">
    <div><label>Start date</label><input type="text" id="dd2-a" readonly placeholder="Pick start date"></div>
    <div><label>End date</label><input type="text" id="dd2-b" readonly placeholder="Pick end date"></div>
  </div>
  <button class="btn" onclick="dateDiff()">Calculate difference</button>
  <div id="dd2-out" class="result">Pick two dates.</div>
</div>""",
"find-and-replace": """
<div class="panel">
  <label>Text</label>
  <textarea id="fr-in" placeholder="Paste your text…"></textarea>
  <div class="row">
    <div><label>Find</label><input type="text" id="fr-find" placeholder="old" /></div>
    <div><label>Replace with</label><input type="text" id="fr-repl" placeholder="new" /></div>
  </div>
  <label><input type="checkbox" id="fr-case" style="width:auto" /> Case sensitive</label>
  <label><input type="checkbox" id="fr-regex" style="width:auto" /> Regular expression</label>
  <button class="btn" onclick="findReplace()">Replace all</button>
  <span id="fr-count" style="color:var(--muted);font-size:13px"></span>
  <div id="fr-out" class="result mono"></div>
</div>""",
"text-sorter": """
<div class="panel">
  <label>Lines to sort</label>
  <textarea id="sort-in" placeholder="banana&#10;apple&#10;cherry"></textarea>
  <div>
    <button class="btn" onclick="sortLines('az')">A → Z</button>
    <button class="btn ghost" onclick="sortLines('za')">Z → A</button>
    <button class="btn ghost" onclick="sortLines('len')">Short → Long</button>
    <button class="btn ghost" onclick="sortLines('len2')">Long → Short</button>
    <button class="btn ghost" onclick="sortLines('shuffle')">Shuffle</button>
  </div>
</div>""",
"lorem-ipsum-generator": """
<div class="panel">
  <div class="row">
    <div><label>Paragraphs</label><input type="number" id="lorem-n" value="3" min="1" max="20" /></div>
    <div><label>Sentences per paragraph</label><input type="number" id="lorem-s" value="4" min="1" max="20" /></div>
  </div>
  <button class="btn" onclick="genLorem()">Generate</button>
  <div id="lorem-out" class="result mono"></div>
</div>""",
"word-frequency-counter": """
<div class="panel">
  <label>Text to analyze</label>
  <textarea id="wf-in" oninput="wordFreq()" placeholder="Paste an article, essay or any text…"></textarea>
  <p id="wf-total" style="color:var(--muted);font-size:13px"></p>
  <div id="wf-out" class="result"></div>
</div>""",
"hash-generator": """
<div class="panel">
  <label>Text to hash</label>
  <textarea id="hash-in" placeholder="Enter text…"></textarea>
  <button class="btn" onclick="hashGen()">Generate hashes</button>
  <div id="hash-out" class="result mono"></div>
</div>""",
"jwt-decoder": """
<div class="panel">
  <label>JWT token</label>
  <textarea id="jwt-in" placeholder="eyJhbGciOi…"></textarea>
  <button class="btn" onclick="jwtDecode()">Decode</button>
  <div id="jwt-out" class="result mono"></div>
</div>""",
"regex-tester": """
<div class="panel">
  <div class="row">
    <div style="flex:2"><label>Pattern</label><input type="text" id="re-pattern" placeholder="\\b\\w+@\\w+\\.\\w+\\b" /></div>
    <div><label>Flags</label><input type="text" id="re-flags" value="g" /></div>
  </div>
  <label>Test text</label>
  <textarea id="re-text" placeholder="Paste text to test against…"></textarea>
  <button class="btn" onclick="regexTest()">Test</button>
  <span id="re-count" style="color:var(--muted);font-size:13px"></span>
  <div id="re-out" class="result"></div>
  <div id="re-groups" class="result mono"></div>
</div>""",
"csv-to-json-converter": """
<div class="panel">
  <div class="row">
    <div><label>Delimiter</label><select id="csv-delim"><option value=",">Comma</option><option value=";">Semicolon</option><option value="tab">Tab</option><option value="|">Pipe</option></select></div>
  </div>
  <label>CSV input (first row = headers)</label>
  <textarea id="csv-in" placeholder="name,age&#10;Alice,30&#10;Bob,25"></textarea>
  <button class="btn" onclick="csvToJson()">Convert →</button>
  <span id="csv-count" style="color:var(--muted);font-size:13px"></span>
  <div id="csv-out" class="result mono"></div>
</div>""",
"html-encoder-decoder": """
<div class="panel">
  <label>Text or HTML</label>
  <textarea id="henc-in" placeholder='<div class="hello">…'></textarea>
  <div>
    <button class="btn" onclick="htmlEnc('enc')">Encode →</button>
    <button class="btn ghost" onclick="htmlEnc('dec')">← Decode</button>
  </div>
  <div id="henc-out" class="result mono"></div>
</div>""",
"number-base-converter": """
<div class="panel">
  <div class="row">
    <div style="flex:2"><label>Number</label><input type="text" id="nb-in" value="255" oninput="baseConvert()" /></div>
    <div><label>Input base</label><select id="nb-from" onchange="baseConvert()"><option value="2">Binary (2)</option><option value="8">Octal (8)</option><option value="10" selected>Decimal (10)</option><option value="16">Hex (16)</option></select></div>
  </div>
  <div id="nb-out" class="result"></div>
</div>""",
"roman-numeral-converter": """
<div class="panel">
  <label>Number (1–3999) or Roman numeral</label>
  <input type="text" id="roman-in" placeholder="2024 or MMXXIV" />
  <div>
    <button class="btn" onclick="romanConvert('to')">Number → Roman</button>
    <button class="btn ghost" onclick="romanConvert('from')">Roman → Number</button>
  </div>
  <div id="roman-out" class="result big"></div>
</div>""",
"image-resizer": """
<div class="panel">
  <label>Choose image (stays on your device)</label>
  <input type="file" id="img-file" accept="image/*" onchange="imgLoaded()" />
  <div class="row">
    <div><label>Width (px)</label><input type="number" id="img-w" /></div>
    <div><label>Height (px)</label><input type="number" id="img-h" /></div>
    <div><label>Format</label><select id="img-fmt"><option value="jpeg">JPG</option><option value="png">PNG</option><option value="webp">WebP</option></select></div>
    <div><label>Quality (%)</label><input type="number" id="img-q" value="90" min="10" max="100" /></div>
  </div>
  <label><input type="checkbox" id="img-lock" checked style="width:auto" /> Lock aspect ratio</label>
  <button class="btn" onclick="resizeImage()">Resize & convert</button>
  <p id="img-info" style="color:var(--muted);font-size:13px"></p>
  <img id="img-preview" alt="preview" />
  <a id="img-download" class="btn" style="display:none">↓ Download</a>
</div>""",
"palette-generator": """
<div class="panel">
  <label>Base color (hex)</label>
  <input type="text" id="pal-in" value="#ff7000" oninput="genPalette()" placeholder="#ff7000" />
  <div id="pal-err" class="error"></div>
  <div id="pal-out" class="pal-row"></div>
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


def blog_wordcount(post):
    texts = []
    for kind, val in post["blocks"]:
        if kind in ("p", "h2", "h3"):
            texts.append(val)
        elif kind in ("ul", "ol"):
            texts.extend(val)
        elif kind == "faq":
            texts.extend(f"{q} {a}" for q, a in val)
    return len(re.findall(r"[A-Za-z0-9'\u2019\-]+", " ".join(texts)))


def blog_blocks_html(post):
    out = []
    for kind, val in post["blocks"]:
        if kind == "p":
            out.append(f"<p>{esc(val)}</p>")
        elif kind == "h2":
            out.append(f'<h2 class="section">{esc(val)}</h2>')
        elif kind == "h3":
            out.append(f"<h3>{esc(val)}</h3>")
        elif kind in ("ul", "ol"):
            tag = "ul" if kind == "ul" else "ol"
            out.append(f"<{tag}>" + "".join(f"<li>{esc(i)}</li>" for i in val) + f"</{tag}>")
        elif kind == "faq":
            out.append('<h2 class="section">Frequently Asked Questions</h2>')
            for q, a in val:
                out.append(f"<h3>{esc(q)}</h3><p>{esc(a)}</p>")
    return "\n".join(out)


def blog_post_html(post):
    blocks = blog_blocks_html(post)
    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post["title"],
        "description": post["desc"],
        "datePublished": post["date"],
        "author": {"@type": "Organization", "name": "MSCALE Tools"},
    })
    related = "".join(
        f'<a class="card" href="../tools/{s}.html"><div class="card-head">{svg_icon(CAT_SLUG_BY_NAME.get(c, "wrench"), "card-ic", hue_of(CAT_SLUG_BY_NAME.get(c, "wrench")))}<h3>{n}</h3></div><p>{d}</p><span class="tag">LIVE</span></a>'
        for s, n, c, d in LIVE[:4]
    )
    return (
        header(f'{post["title"]} | MSCALE Tools Blog', post["desc"], "../")
        + f"""<nav class="breadcrumb" aria-label="Breadcrumb">
<a href="../index.html">{svg_icon("wrench", "crumb-ic")}Home</a>
<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
<a href="../blog/">Blog</a>
<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
<span>{esc(post["title"])}</span>
</nav>
<article class="prose">
<script type="application/ld+json">{jsonld}</script>
<p class="post-meta">{post["date"]} &middot; MSCALE Tools</p>
<h1>{esc(post["title"])}</h1>
{blocks}
</article>
<h2 class="section">Try these tools</h2>
<div class="grid">{related}</div>"""
        + footer("../")
    )


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
{ad_slot("tools-top")}
<div class="tools-layout">
  <aside class="tools-side" id="tools-side">{side}</aside>
  <div class="tools-main">
    <div class="tools-controls">
      <div class="search-wrap">{svg_icon("search", "search-ic")}<input id="tools-search" placeholder="Search tools (e.g. 'word count', 'password')" /></div>
      <select id="tools-sort" aria-label="Sort tools">
        <option value="pop">Popular</option>
        <option value="az">A to Z</option>
        <option value="za">Z to A</option>
      </select>
    </div>
    <p id="tools-count" class="tools-count"></p>
    <div class="grid" id="tools-grid"></div>
    <div style="text-align:center;margin-top:22px"><button id="tools-more" class="btn ghost" style="display:none">Load more tools</button></div>
    {ad_slot("tools-feed", "970 × 160")}
    <div class="banner-cta">
      <div><b>Every tool you need right here in your browser.</b><span>Free, private, no sign-up — {total_live} tools live today.</span></div>
      <a class="btn" href="word-counter.html">Try Now</a>
    </div>
  </div>
</div>"""
        + footer("../")
    )


def blog_index_html():
    cards = "".join(
        f"""<a class="card blog-card" href="{p['slug']}.html">
<h3>{esc(p["title"])}</h3>
<p>{esc(p["desc"])}</p>
<span class="post-meta">{p["date"]}</span>
</a>"""
        for p in BLOG_POSTS
    )
    return (
        header("Blog | MSCALE Tools", "Practical guides on word counts, password security, JSON, images and getting the most from online tools.", "../")
        + """<div class="tool-head"><div class="tool-title">""" + svg_icon("book-open", "tool-ic big") + """<h1>Blog</h1></div>
<p>Practical, in-depth guides from the MSCALE Tools team. Every article is a full read, no fluff.</p></div>
<div class="blog-grid">""" + cards + "</div>"
        + footer("../")
    )


def tool_page(slug, name, cat, desc):
    cat_slug = CAT_SLUG_BY_NAME.get(cat, "calculators")
    body = TOOL_BODIES[slug]
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
        n = cat_counts.get(slug, 0) + len(live_by_cat.get(slug, []))
        subs = "".join(f"<a href='tools/{s}.html'>{nm}</a>" for s, nm in live_by_cat.get(slug, [])[:3])
        cat_cards += (f"<a class='cat-card' href='{slug}/'><span class='icon-box' style='color:{hue_of(slug)};background:{hue_of(slug)}22'>{svg_icon(slug)}</span>"
                      f"<h3>{name}</h3><p>{n} tools<span class='cat-arrow'>{svg_icon('arrow-right')}</span></p><div class='cat-links'>{subs}</div></a>")
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
    all_cards = "".join(
        f"<a class='card' href='tools/{s}.html'><div class='card-head'>{svg_icon(CAT_SLUG_BY_NAME.get(c, 'wrench'), 'card-ic', hue_of(CAT_SLUG_BY_NAME.get(c, 'wrench')))}<h3>{n}</h3></div><p>{d}</p><span class='tag'>LIVE</span></a>"
        for s, n, c, d in LIVE
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
{ad_slot("home-pre-all")}
<h2 class="section" id="all">All live tools</h2>
<div class="grid" id="tool-list">{all_cards}</div>
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

def category_page(slug, name, icon, live_slugs, catalog_cat):
    live_names_by_slug = {s: (n, d) for s, n, _, d in LIVE}
    hue = hue_of(slug)
    tile = f"<span class='icon-box' style='color:{hue};background:{hue}22'>{svg_icon(slug)}</span>"
    live_cards = "".join(
        f"<a class='card' data-name='{esc(live_names_by_slug[s][0].lower())}' href='../tools/{s}.html'><div class='card-head'>{tile}<h3>{live_names_by_slug[s][0]}</h3></div>"
        f"<p>{live_names_by_slug[s][1]}</p><span class='tag'>LIVE</span></a>"
        for s in live_slugs
    )
    live_names = {live_names_by_slug[s][0].lower() for s in live_slugs}
    coming = [(i["n"], i.get("s", "")) for i in CATALOG if i["c"] == slug and i["n"].lower() not in live_names][:120]
    coming_cards = "".join(
        f"<div class='card soon' data-name='{esc(n.lower())}'><div class='card-head'>{tile}<h3>{esc(n)}</h3></div>"
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
    n_live, n_coming = len(live_slugs), len(coming)
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
  if (!input) return;
  var cards = [].slice.call(document.querySelectorAll('.grid .card'));
  var note = document.getElementById('cat-count');
  input.addEventListener('input', function () {
    var q = input.value.trim().toLowerCase(), n = 0;
    cards.forEach(function (c) {
      var hit = !q || (c.getAttribute('data-name') || '').indexOf(q) > -1;
      c.style.display = hit ? '' : 'none';
      if (hit) n++;
    });
    [].slice.call(document.querySelectorAll('.cat-sec')).forEach(function (s) {
      var vis = [].slice.call(s.querySelectorAll('.card')).some(function (c) { return c.style.display !== 'none'; });
      s.style.display = vis ? '' : 'none';
    });
    if (note) note.textContent = q ? ('Showing ' + n + ' of ' + cards.length + ' tools') : '';
  });
})();
"""
    return (
        header(f"{name} — Free Online | MSCALE Tools", f"Free online {name.lower()} — fast, private, no sign-up.", "../")
        + f"""{crumb}
<script type="application/ld+json">{jsonld}</script>
<div class="cat-hero">
  <span class="icon-box cat-hero-ic" style="color:{hue};background:{hue}22">{svg_icon(slug)}</span>
  <div>
    <h1>{name}</h1>
    <p>{intro}</p>
    <p class="cat-stats"><b>{n_live} live tools</b> · {n_coming}+ more coming · 100% free · no sign-up</p>
  </div>
</div>
<div class="cat-search-wrap">
  {svg_icon("search", "search-ic")}
  <input id="cat-search" placeholder="Search in {name.lower()} (e.g. 'password', 'convert')…" />
</div>
<p id="cat-count"></p>
<section class="cat-sec"><h2 class="section">Most popular {name.lower()}</h2>
<div class="grid">{live_cards}</div></section>
<section class="cat-sec"><h2 class="section">All {name.lower()} tools</h2>
<div class="grid">{coming_cards}</div></section>
{about_html}
<p style="margin-top:26px"><a class="btn ghost" href="../tools/">Browse all 1,800+ tools{svg_icon("arrow-right")}</a></p>
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
    for post in BLOG_POSTS:
        report.append(("blog/" + post["slug"], blog_wordcount(post)))
    oob = [(s, n) for s, n in report if not (1000 <= n <= 1200)]
    if oob:
        raise SystemExit("CONTENT WORD COUNT OUT OF RANGE (1000-1200): " + repr(oob))
    print("word counts OK: %d pages, min %d, max %d" % (len(report), min(n for _, n in report), max(n for _, n in report)))
    print(f"catalog: {len(catalog)} entries; pages written")

main()
