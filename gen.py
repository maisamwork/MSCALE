import json, os, re
from openpyxl import load_workbook

ROOT = os.path.dirname(os.path.abspath(__file__))
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

def svg_icon(cat, cls=""):
    return ('<svg class="' + cls + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            + ICONS.get(cat, ICONS["wrench"]) + "</svg>")
LIVE = [
    ("percentage-calculator", "Percentage Calculator", "Calculators", "Percent of a number, percentage change and more"),
    ("bmi-calculator", "BMI Calculator", "Calculators", "Body Mass Index with weight category"),
    ("age-calculator", "Age Calculator", "Calculators", "Exact age in years, months and days"),
    ("loan-emi-calculator", "Loan / EMI Calculator", "Calculators", "Monthly payment, total interest and total cost"),
    ("word-counter", "Word Counter", "Text", "Words, characters, sentences and reading time"),
    ("case-converter", "Case Converter", "Text", "UPPER, lower, Title, camelCase, snake_case, kebab"),
    ("remove-duplicate-lines", "Remove Duplicate Lines", "Text", "Deduplicate text lines, with case and trim options"),
    ("reverse-text", "Reverse Text", "Text", "Reverse characters, words or lines"),
    ("json-formatter", "JSON Formatter", "Developer", "Beautify, validate and minify JSON"),
    ("base64-encoder-decoder", "Base64 Encode / Decode", "Developer", "UTF-8 safe Base64 conversion"),
    ("url-encoder-decoder", "URL Encoder / Decoder", "Developer", "Percent-encode or decode URLs and text"),
    ("uuid-generator", "UUID Generator", "Developer", "Generate v4 UUIDs in bulk"),
    ("unit-converter", "Unit Converter", "Converters", "Length, weight, data size and temperature"),
    ("timestamp-converter", "Timestamp Converter", "Converters", "Unix timestamp to date and back, live clock"),
    ("password-generator", "Password Generator", "Security", "Strong random passwords with entropy estimate"),
    ("color-converter", "Color Converter", "Color", "HEX to RGB to HSL with live preview"),
    ("random-number-generator", "Random Number Generator", "Random", "Random numbers in any range, unique option"),
    ("dice-roller", "Dice Roller", "Random", "Roll up to 20 dice with any number of sides"),
    ("coin-flipper", "Coin Flipper", "Random", "Flip one coin or a thousand, with counts"),
    ("discount-calculator", "Discount Calculator", "Calculators", "Sale price, savings and final price with tax"),
    ("tip-calculator", "Tip Calculator", "Calculators", "Tip amount, total and per-person split"),
    ("compound-interest-calculator", "Compound Interest Calculator", "Finance", "Future value with contributions and compounding"),
    ("gst-vat-calculator", "GST / VAT Calculator", "Finance", "Add or remove sales tax from any amount"),
    ("date-difference-calculator", "Date Difference Calculator", "Date & Time", "Days, weeks, months and years between dates"),
    ("find-and-replace", "Find and Replace", "Text", "Replace text with case and regex options"),
    ("text-sorter", "Line Sorter", "Text", "Sort lines A-Z, Z-A, by length or shuffle"),
    ("lorem-ipsum-generator", "Lorem Ipsum Generator", "Text", "Placeholder text by paragraphs and sentences"),
    ("word-frequency-counter", "Word Frequency Counter", "Text", "Top words with visual frequency bars"),
    ("hash-generator", "Hash Generator", "Developer", "SHA-1, SHA-256 and SHA-512 hashes instantly"),
    ("jwt-decoder", "JWT Decoder", "Developer", "Decode JWT header and payload, check expiry"),
    ("regex-tester", "Regex Tester", "Developer", "Test regular expressions with live highlighting"),
    ("csv-to-json-converter", "CSV to JSON Converter", "Developer", "Convert CSV or TSV to JSON, quote-aware"),
    ("html-encoder-decoder", "HTML Encoder / Decoder", "Developer", "Escape or unescape HTML entities"),
    ("number-base-converter", "Number Base Converter", "Converters", "Binary, octal, decimal and hexadecimal"),
    ("roman-numeral-converter", "Roman Numeral Converter", "Converters", "Roman numerals to numbers and back"),
    ("image-resizer", "Image Resizer", "Image", "Resize and convert images in your browser"),
    ("palette-generator", "Color Palette Generator", "Color", "Shades and tints from any color, click to copy"),
]

CAT_PAGES = {
    "calculators": ("Calculators", "\U0001F9EE", ["percentage-calculator", "bmi-calculator", "age-calculator", "loan-emi-calculator", "discount-calculator", "tip-calculator"], "Calculators"),
    "text-tools": ("Text Tools", "\U0001F4DD", ["word-counter", "case-converter", "remove-duplicate-lines", "reverse-text", "find-and-replace", "text-sorter", "lorem-ipsum-generator", "word-frequency-counter"], "Text Tools"),
    "developer-tools": ("Developer Tools", "\U0001F4BB", ["json-formatter", "base64-encoder-decoder", "url-encoder-decoder", "uuid-generator", "hash-generator", "jwt-decoder", "regex-tester", "csv-to-json-converter", "html-encoder-decoder"], "Developer Tools"),
    "converters": ("Converters", "\U0001F504", ["unit-converter", "timestamp-converter", "number-base-converter", "roman-numeral-converter"], "Converters (Units & Numbers)"),
    "security": ("Security Tools", "\U0001F512", ["password-generator"], "Security & Encoding"),
    "color-tools": ("Color Tools", "\U0001F3A8", ["color-converter", "palette-generator"], "Color & Design Tools"),
    "random-generators": ("Random Generators", "\U0001F3B2", ["random-number-generator", "dice-roller", "coin-flipper"], "Random & Fun Generators"),
    "pdf-tools": ("PDF Tools", "\U0001F4C4", [], "PDF Tools"),
    "image-tools": ("Image Tools", "\U0001F5BC\uFE0F", ["image-resizer"], "Image Tools"),
    "seo-web-tools": ("SEO & Web Tools", "\U0001F4C8", [], "SEO & Web Tools"),
    "date-time-tools": ("Date & Time Tools", "\U0001F550", ["date-difference-calculator"], "Date & Time Tools"),
    "finance-tools": ("Finance & Business", "\U0001F4B0", ["compound-interest-calculator", "gst-vat-calculator"], "Finance & Business"),
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
    nav = "".join(
        f'<a href="{depth}{slug}/">{name}</a>'
        for slug, (name, _, _, _) in CAT_PAGES.items()
    )
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
<link rel="stylesheet" href="{depth}assets/style.css"/>
<script src="{depth}assets/live-tools.js" defer></script>
<script src="{depth}assets/app.js" defer></script>
<script src="{depth}assets/tools.js" defer></script>
</head>
<body>
<header class="site"><div class="container">
  <a class="brand" href="{depth}index.html">{svg_icon("wrench", "brand-icon")}MSCALE<span>Tools</span></a>
  <nav class="main">{nav}<a href="{depth}index.html#all">All tools</a></nav>
</div></header>
<main class="container">"""

def footer(depth):
    cats = "".join(
        f'<a href="{depth}{slug}/">{name}</a>'
        for slug, (name, _, _, _) in CAT_PAGES.items()
    )
    popular = ["percentage-calculator", "word-counter", "json-formatter", "password-generator",
               "bmi-calculator", "unit-converter", "image-resizer", "compound-interest-calculator"]
    names_by_slug = {s: n for s, n, _, _ in LIVE}
    pop = "".join(f'<a href="{depth}tools/{s}.html">{names_by_slug[s]}</a>' for s in popular)
    return f"""</main>
<footer class="site"><div class="container">
  <div class="footer-grid">
    <div class="footer-brand">
      <a class="brand" href="{depth}index.html">{svg_icon("wrench", "brand-icon")}MSCALE<span>Tools</span></a>
      <p>Free online tools that run entirely in your browser — fast, private, no sign-up, no uploads.</p>
      <p><a href="https://github.com/maisamwork/MSCALE">GitHub</a></p>
    </div>
    <div>
      <h4>Categories</h4>
      {cats}
    </div>
    <div>
      <h4>Popular tools</h4>
      {pop}
    </div>
  </div>
  <p class="copyright">© 2026 MSCALE Tools. All processing happens client-side in your browser.</p>
</div></footer>
</body>
</html>"""

TOOL_BODIES = {
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
  <input type="date" id="age-dob" />
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
    <div><label>Start date</label><input type="date" id="dd2-a" /></div>
    <div><label>End date</label><input type="date" id="dd2-b" /></div>
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

def tool_page(slug, name, cat, desc):
    cat_slug = CAT_SLUG_BY_NAME.get(cat, "calculators")
    body = TOOL_BODIES[slug]
    related = [(s, n) for s, n, c, _ in LIVE if c == cat and s != slug][:4]
    rel_html = ""
    if related:
        rel_html = "<h2 class='section'>Related tools</h2><div class='grid'>" + "".join(
            f"<a class='card' href='../tools/{s}.html'><div class='card-head'>{svg_icon(cat_slug, 'card-ic')}<h3>{n}</h3></div></a>"
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
    return (
        header(f"{name} — Free Online Tool | MSCALE Tools", desc, "../")
        + f"""<div class="tool-wrap">
{crumb}
<script type="application/ld+json">{jsonld}</script>
<div class="tool-head"><div class="tool-title">{svg_icon(cat_slug, "tool-ic")}<h1>{name}</h1></div><p>{desc}</p></div>
{body}
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

def index_page(catalog):
    cat_counts = {}
    for item in catalog:
        cat_counts[item["c"]] = cat_counts.get(item["c"], 0) + 1
    extra_cats = [("pdf-tools", "PDF Tools"), ("image-tools", "Image Tools"), ("seo-web-tools", "SEO & Web Tools"),
                  ("date-time-tools", "Date & Time Tools"), ("finance-tools", "Finance & Business")]
    cat_cards = ""
    for slug, (name, _, _, _) in CAT_PAGES.items():
        n = cat_counts.get(slug, 0) + len([1 for s, _, c, _ in LIVE if CAT_SLUG_BY_NAME.get(c) == slug])
        cat_cards += (f"<a class='cat-card' href='{slug}/'><span class='icon-box'>{svg_icon(slug)}</span>"
                      f"<h3>{name}</h3><p>{n} tools</p></a>")
    for slug, name in extra_cats:
        if slug not in CAT_PAGES:
            continue
        n = cat_counts.get(slug, 0) + len([1 for s, _, c, _ in LIVE if CAT_SLUG_BY_NAME.get(c) == slug])
        cat_cards += (f"<a class='cat-card' href='{slug}/'><span class='icon-box'>{svg_icon(slug)}</span>"
                      f"<h3>{name}</h3><p>{n} tools</p></a>")
    live_cards = "".join(
        f"<a class='card' href='tools/{s}.html'><div class='card-head'>{svg_icon(CAT_SLUG_BY_NAME.get(c, 'wrench'), 'card-ic')}<h3>{n}</h3></div><p>{d}</p><span class='tag'>LIVE</span></a>"
        for s, n, c, d in LIVE
    )
    total = len(catalog) + len(LIVE)
    return header("MSCALE Tools — Free Online Tools", "Free online calculators, text tools, developer tools and converters. Fast, private, no sign-up.") + f"""
<div class="hero">
  <h1>Every tool you need, <em>in one place</em></h1>
  <p>{total}+ tools indexed — {len(LIVE)} live right now, more shipping weekly. Everything runs in your browser: fast and private.</p>
  <div class="search-wrap">{svg_icon("search", "search-ic")}<input id="search" placeholder="Search {total}+ tools… (e.g. percentage, json, password)" /></div>
  <p id="count-note" style="font-size:13px"></p>
</div>
<h2 class="section" id="all">Live tools</h2>
<div class="grid" id="tool-list">{live_cards}</div>
<h2 class="section">Browse by category</h2>
<div class="cat-grid">{cat_cards}</div>
""" + footer("")


def category_page(slug, name, icon, live_slugs, catalog_cat):
    live_names_by_slug = {s: (n, d) for s, n, _, d in LIVE}
    live_cards = "".join(
        f"<a class='card' href='../tools/{s}.html'><div class='card-head'>{svg_icon(slug, 'card-ic')}<h3>{live_names_by_slug[s][0]}</h3></div>"
        f"<p>{live_names_by_slug[s][1]}</p><span class='tag'>LIVE</span></a>"
        for s in live_slugs
    )
    coming = [i["n"] for i in CATALOG if i["c"] == slug]
    live_names = {live_names_by_slug[s][0].lower() for s in live_slugs}
    coming = [n for n in coming if n.lower() not in live_names][:80]
    coming_cards = "".join(
        f"<div class='card soon'><div class='card-head'>{svg_icon(slug, 'card-ic')}<h3>{esc(n)}</h3></div><span class='tag'>coming soon</span></div>"
        for n in coming
    )
    intro = INTROS.get(slug, "")
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
    return (
        header(f"{name} — Free Online | MSCALE Tools", f"Free online {name.lower()} — fast, private, no sign-up.", "../")
        + f"""{crumb}
<script type="application/ld+json">{jsonld}</script>
<div class="tool-head"><div class="tool-title">{svg_icon(slug, "tool-ic big")}<h1>{name}</h1></div><p>{intro}</p></div>
<h2 class="section">Live now</h2>
<div class="grid">{live_cards}</div>
<h2 class="section">Coming soon</h2>
<div class="grid">{coming_cards}</div>"""
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
    print(f"catalog: {len(catalog)} entries; pages written")

main()
