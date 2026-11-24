# -*- coding: utf-8 -*-
"""Batch 30 module D: 18 flagship tools (developer, text, home)."""
from .mega1b import calc_article
from .mega3 import _f, _sel

def _ta(i, l, ph=""):
    p = (' placeholder="' + ph.replace('"', '') + '"') if ph else ""
    return '<div><label for="' + i + '">' + l + '</label><textarea id="' + i + '" rows="6"' + p + '></textarea></div>'

MEGA23 = {}
CONTENT23 = {}

ADV23 = []

ADV23.append(("text-diff-line", "Line Diff Checker", "Text Tools",
 "Two texts compared line by line with additions and removals counted",
 "Config files, contracts and row datasets break silently during edits, and a line-level diff is still the fastest way to see exactly what moved. Paste both versions and this checker walks them line by line, counts the additions, the removals and the unchanged rest, and prints the lists so the change can be reviewed without any diff tool installation.",
 "line-by-line comparison: a line changed reads as one addition plus one removal",
 "a paste of Alpha, Beta, Gamma against Alpha, Delta, Gamma reports one line added and one removed \u2014 and those exact two lines are listed for review",
 ["config file review", "contract redline checks", "dataset row comparison", "code snippet review"],
 "Line diffs do not see words: one changed comma makes a whole line added and removed, which is why the tool prints both lists rather than a merged story. Paste whole lines \u2014 partial lines still compare, but the counts read heavier than the real change.",
 "w53",
 _ta("w53-a", "Original text", "Alpha") + _ta("w53-b", "Changed text", "Alpha") +
 '''<button class="btn" onclick="w53()">Diff the lines</button>
  <div id="w53-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("sort-lines", "Line Sorter", "Text Tools",
 "Any list sorted alphabetically or numerically, with dedup built in",
 "Shopping lists, backlog dumps and domain spreadsheets all unsort themselves in minutes, and sorting by hand is how duplicates and near-duplicates slip through. Paste the lines and this sorter orders them alphabetically or numerically, optionally removes duplicates in the same pass, and reports how many lines made the cut.",
 "sort with locale collation; numeric mode compares parsed numbers; dedup removes exact repeats",
 "a paste of charlie, alpha, bravo, alpha comes back alpha, bravo, charlie \u2014 three lines where four started, the duplicate folded",
 ["list cleanup", "backend log scanning", "spreadsheet column prep", "flash card ordering"],
 "Numeric mode matters the moment 10 must sort after 9 \u2014 alphabetical order puts it before, and every phone book does this on purpose. Dedup treats near-duplicates as distinct: trailing spaces are different strings, so trim first when the copy came from a webpage.",
 "w54",
 _ta("w54-a", "Lines to sort", "charlie") + _sel("w54-b", "Order", [("az", "A to Z"), ("za", "Z to A"), ("num", "Numeric, ascending")]) + _sel("w54-c", "Duplicates", [("keep", "Keep"), ("drop", "Remove duplicates")]) +
 '''<button class="btn" onclick="w54()">Sort the lines</button>
  <div id="w54-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("repeat-text-n-times", "Text Repeater", "Text Tools",
 "Any snippet repeated exactly N times with a joining rule",
 "Testing padding, stress-testing layouts and building mock data all need the same string again and again, and manual copy-paste miscounts at about the fourth repeat. Enter the text, the count and a joiner, and this repeater produces the exact string, reports the final length in characters, and caps absurd sizes before they freeze a browser tab.",
 "output = text joined by the chosen separator, repeated N times; length counted in characters",
 "the word cheers repeated 8 times joins into one 48-character string \u2014 and the length read-out is what layout testing actually needs",
 ["placeholder generation", "layout stress testing", "separator experiments", "mock data creation"],
 "A repeat past a few thousand turns invisible text into real kilobytes \u2014 the tool caps the output at sane sizes and says so instead of hanging. The count is exact, not approximate: pasting the result elsewhere is reproducible letter for letter, which is the whole purpose.",
 "w55",
 _ta("w55-a", "Text to repeat", "cheers") + _f("w55-b", "Repeat count", "8") + _sel("w55-c", "Join with", [("", "Nothing \u2014 fused together"), ("newline", "New lines"), (" ", "Spaces"), (", ", "Commas")]) +
 '''<button class="btn" onclick="w55()">Repeat it</button>
  <div id="w55-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("nan-checker", "NaN Builder Checker", "Developer Tools",
 "Dataloads scanned for NaN, undefined and null before charts meet them",
 "A silent NaN travels far: it passes staging, lands in a chart, and surfaces as an empty week in the dashboard nobody can explain. Paste a JSON payload, API response log or array dump and this checker finds every NaN, undefined and null leak, counts them, and prints the offending lines so the bug is found at the door, not on stage.",
 "scan for literal NaN, undefined and null tokens with their line numbers",
 "a paste with three NaN leaks and two nulls lands flagged line by line \u2014 found at the door instead of in the chart at board meeting time",
 ["API response debugging", "chart data validation", "database export checks", "config file audits"],
 "The scan is textual, so a string that legitimately says NaN in prose also matches \u2014 read the reported lines before deleting anything. Serialization is where NaN enters: JSON writing turns it into null, which is precisely the leak this check is built to catch early.",
 "w56",
 _ta("w56-a", "Paste payload or log", "NaN") +
 '''<button class="btn" onclick="w56()">Scan the payload</button>
  <div id="w56-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("html-table-to-csv", "HTML Table to CSV Converter", "Developer Tools",
 "Any HTML table extracted into honest CSV, quoted where it matters",
 "Government portals, dashboards and archived pages all serve tabular data locked inside HTML tables, and copy-paste turns the columns to porridge. Paste table markup and this converter extracts every row into CSV, quotes the fields that contain commas, and reports the shape \u2014 rows, columns and any ragged rows flagged before spreadsheets find them.",
 "rows = tr elements; cells joined by commas, quoted when the text contains a comma or quote",
 "a four-row product table pastes into four CSV lines with quoted commas intact \u2014 and any short row is flagged by number",
 ["table data export", "report archival", "spreadsheet ingestion", "data journalism"],
 "Merged cells break every naive converter, including straight-line ones like this: a colspan cell reads as an empty slot for its absorbed neighbours. Check the row-count line against the visible table before trusting the CSV \u2014 the count is the checksum that sees everything.",
 "w57",
 _ta("w57-a", "Paste table HTML", "<table>") +
 '''<button class="btn" onclick="w57()">Extract the CSV</button>
  <div id="w57-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("yaml-explainer", "YAML Structure Explainer", "Developer Tools",
 "Config files summarized as structure first, values second",
 "CI configs, docker compose files and deployment manifests are YAML trees, and reviewing one means keeping the nesting depth in your head on every line. Paste the YAML and this explainer counts the top-level keys, the maximum nesting depth, lists and comments, and prints the outline so a reviewer reads structure first and values second.",
 "outline by indentation level; depth from leading spaces; lists detected by dash markers",
 "a config with 12 keys nesting two levels deep and one list gets read back as structure first, values second",
 ["CI config review", "docker compose reading", "deployment manifests", "indentation debugging"],
 "YAML errors are indentation errors wearing nicer clothes \u2014 the mixed use of spaces and tabs is undetectable by eye at depth three, which is where this outline earns its keep. It summarizes indentation; it does not promise a full parser, so keep the validator in the pipeline as well.",
 "w58",
 _ta("w58-a", "Paste YAML", "name: app") +
 '''<button class="btn" onclick="w58()">Explain the structure</button>
  <div id="w58-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("etag-explainer", "ETag Explainer", "Developer Tools",
 "Cache validators read apart: strong, weak, and what they promise",
 "ETags decide when browsers re-download the world, and the prefix difference between a strong and weak validator is the difference between byte-identical and merely semantically equal. Paste an ETag header value, and this explainer states which validator it is, how the server likely built it, and what the browser will do with it on the next request.",
 "weak validator = W/ prefix; strong validators claim byte-exact equality, weak claim semantic equality",
 "the etag 33a64df5 without the weak prefix validates as strong \u2014 a cache reusing it claims the body is byte-identical",
 ["caching reviews", "CDN behaviour checks", "API design reviews", "load testing"],
 "Weak ETags cannot be used for range requests \u2014 partial downloads demand strong validators \u2014 and a server that changes them on every response silently disables caching. The hash length is a fingerprint of the generator: long hashes usually mean content, short ones version numbers.",
 "w59",
 _f("w59-a", "ETag header value", "33a64df5", "33a64df5 or W/ followed by a hash") +
 '''<button class="btn" onclick="w59()">Read the validator</button>
  <div id="w59-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("user-agent-explainer", "User Agent Explainer", "Developer Tools",
 "Browser, engine, operating system and device read off any UA string",
 "Support tickets arrive as user-agent strings that look like noise and hide exactly the context needed to reproduce a bug. Paste one and this explainer identifies the browser family and version, the rendering engine, the operating system and architecture, the device class, and the legacy relics still piggybacking inside the string for compatibility reasons.",
 "ordered detection: engine tokens, then browser version, then OS tokens, then device class",
 "a Chrome 124 on Windows string flags Blink, 64-bit desktop \u2014 and the KHTML relic inside marks the whole WebKit family tree",
 ["support ticket triage", "analytics validation", "compatibility debugging", "bot detection checks"],
 "UA strings are self-reported and increasingly frozen \u2014 all modern browsers claim Mozilla compatibility they do not have and minor versions are being reduced, so treat precision as diminishing. Strings that brag about search crawlers can claim anything: verify by IP, not by polite declarations.",
 "w60",
 _ta("w60-a", "User agent string", "Mozilla/5.0") +
 '''<button class="btn" onclick="w60()">Read the string</button>
  <div id="w60-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("http-method-explainer", "HTTP Method Explainer", "Text Tools",
 "Any HTTP method graded for safety, idempotency and cacheability",
 "API interviews and code reviews both hinge on the same three questions \u2014 is the method safe, is it idempotent, is it cacheable \u2014 and the answers decide retry logic more than any diagram. Pick a method and this explainer states the three verdicts, what a correct response looks like, and the exact way the method is meant to differ from its nearest cousin.",
 "verdicts per RFC 7231/5789: safe, idempotent, cacheable \u2014 each with the reason attached",
 "PATCH changes parts, is neither safe nor reliably idempotent, and cannot be cached \u2014 the exact reason PUT and PATCH differ in real APIs",
 ["API design reviews", "interview preparation", "retry logic design", "gateway configuration"],
 "Idempotency is a server promise, not a client hope: repeated delete calls answer 404 rather than deleting twice, which is the whole point. PATCH earns its un-idempotency honestly on set-based semantics \u2014 design it, document it, then let retries carry an idempotency key.",
 "w61",
 _sel("w61-a", "HTTP method", [("GET", "GET"), ("POST", "POST"), ("PUT", "PUT"), ("PATCH", "PATCH"), ("DELETE", "DELETE"), ("HEAD", "HEAD"), ("OPTIONS", "OPTIONS")]) +
 '''<button class="btn" onclick="w61()">Grade the method</button>
  <div id="w61-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("ipv4-subnet-calculator", "IPv4 Subnet Calculator", "Developer Tools",
 "Network, broadcast and hosts computed for any address and prefix",
 "Every office network conversation stumbles over the same questions \u2014 which subnet, what broadcast, how many hosts \u2014 and the answers are bit arithmetic people promise to memorize and never do. Enter an IPv4 address with its prefix length, and this calculator computes the network and broadcast addresses, the usable host range and count, and the mask in dotted form.",
 "apply the prefix mask by bits: network = IP AND mask; broadcast = network OR NOT mask; hosts = 2^(32 \u2212 n) \u2212 2",
 "192.168.1.130/26 sits on network 192.168.1.128 with broadcast 192.168.1.191 and 62 usable hosts",
 ["network planning", "firewall rule writing", "DHCP scope sizing", "certification study"],
 "The minus two in the host count reserves the network and broadcast addresses \u2014 usable means assignable, a distinction exam questions and vendor docs love to blur. A /31 between two routers is a deliberate exception that keeps both; this tool follows the standard rule.",
 "w62",
 _f("w62-a", "IPv4 address", "192.168.1.130") + _f("w62-b", "Prefix length (0\u201332)", "26") +
 '''<button class="btn" onclick="w62()">Calculate the subnet</button>
  <div id="w62-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("moving-boxes", "Moving Boxes Calculator", "Calculators",
 "The box count and sizes a household move actually needs",
 "Everyone underestimates boxes by roughly half, then buys them one hardware-store run at a time at premium prices. Enter bedrooms, closets and years lived in, and this calculator prices the move in boxes by grade \u2014 small books, medium general, large light \u2014 with a fragile-goods note and the honest answer on when to stop buying and start decluttering.",
 "boxes = bedrooms \u00d7 10 + closets \u00d7 2 + years \u00d7 3, split across three grade sizes",
 "two bedrooms, four closets and three years of accumulation price out at 37 boxes \u2014 15 small, 15 medium and 7 large, with books the heavy exception",
 ["moving house", "storage unit sizing", "decluttering campaigns", "rental van planning"],
 "Books dominate weight, media dominates time, and the kitchen dominates length \u2014 plan for the kitchen to run double its bedroom share. Boxes are cheaper than vans wasted on second trips; the estimate errs slightly high on purpose.",
 "w63",
 _f("w63-a", "Bedrooms", "2") + _f("w63-b", "Closets and wardrobes", "4") + _f("w63-c", "Years lived there", "3") +
 '''<button class="btn" onclick="w63()">Price the move</button>
  <div id="w63-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("mulch-calculator", "Mulch Calculator", "Calculators",
 "Mulch volume and bags for any bed size and depth",
 "Mulch beds look bottomless on invoices because volume is invisible \u2014 and depth is the lever that swings the bill silently. Enter the bed area and the target depth, and this calculator answers the cubic volume, the bag count at the garden-centre 60-litre standard, and the margin bulk delivery usually charges less.",
 "volume = area \u00d7 depth in metres; bags = volume / 0.06 rounded up",
 "a 20 m\u00b2 bed mulched 7 cm deep asks for 1.4 m\u00b3 \u2014 twenty-four 60-litre bags at the garden centre",
 ["spring gardening", "landscaping quotes", "weed suppression plans", "moisture retention projects"],
 "Depths past 8 cm begin to smother shallow roots, and anything under 5 cm invites weeds back by midsummer \u2014 5 to 8 cm is the working window. Fresh mulch settles and fades within one season, so budget for a top-up rather than one heroic annual dump.",
 "w64",
 _f("w64-a", "Bed area (m\u00b2)", "20") + _f("w64-b", "Depth (cm)", "7") +
 '''<button class="btn" onclick="w64()">Mulch the bed</button>
  <div id="w64-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("paint-per-room", "Paint per Room Calculator", "Calculators",
 "Wall area minus openings, priced in coats and litres",
 "Paint is bought twice \u2014 once optimistically and once correctly \u2014 and the difference is usually one opened tin. Enter the room dimensions and the coats, and this calculator works the wall area, deducts a standard door and window share, and answers the litres needed at the standard 10 m\u00b2 of coverage per litre, with a ceiling option priced in.",
 "walls = 2 \u00d7 (length + width) \u00d7 height \u2212 openings; litres = walls \u00d7 coats / 10",
 "a 4.2 by 3.4 metre room with 2.5 metre ceilings exposes 34 usable square metres \u2014 two coats at 10 m\u00b2/L need 6.8 litres",
 ["room repaints", "rental-unit turnovers", "colour-change coverage", "budget checks"],
 "Dark colours over light walls read as one extra coat no matter what the tin claims, and textured surfaces eat another tenth. primer is paint's trompe-l'oeil solution \u2014 cheaper per litre than the second topcoat it replaces. Buy one litre over the answer and never a tin under it.",
 "w65",
 _f("w65-a", "Room length (m)", "4.2") + _f("w65-b", "Room width (m)", "3.4") + _f("w65-c", "Ceiling height (m)", "2.5") + _f("w65-d", "Base coats", "2") +
 '''<button class="btn" onclick="w65()">Size the paint</button>
  <div id="w65-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("gravel-tonnage", "Gravel Tonnage Calculator", "Calculators",
 "Path and driveway gravel priced in tonnes and bulk-bag reality",
 "Gravel sells by the tonne, driveways are measured in metres, and bridging them with guesses is how driveways end up two centimetres deep by winter. Enter the length, width and compacted depth, and this calculator converts to cubic volume, applies the standard 1.6 tonnes per m\u00b3 density, and translates the answer into bulk bags and trailer loads.",
 "tonnes = length \u00d7 width \u00d7 depth (m) \u00d7 1.6 tonnes per m\u00b3",
 "a 6 by 3 metre path at 5 cm deep asks for 0.9 m\u00b3 \u2014 1.44 tonnes, or three of the half-tonne bulk bags",
 ["driveway planning", "path builds", "drainage trenches", "landscaping orders"],
 "Order 10% over the calculation: gravel bedcuts are never masterpieces of level, and the depth that matters is the compacted one underneath wheels. Round gravel migrates and locks less; angular gravel stays where the tonnage lands it.",
 "w66",
 _f("w66-a", "Length (m)", "6") + _f("w66-b", "Width (m)", "3") + _f("w66-c", "Compacted depth (cm)", "5") +
 '''<button class="btn" onclick="w66()">Weigh the gravel</button>
  <div id="w66-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("garden-bed-spacing", "Garden Bed Spacing Calculator", "Calculators",
 "Plants per bed laid out on an honest spacing grid",
 "Overcrowded beds are bought as abundance and thinned as sacrifice, because every plant that grows into another wastes both. Enter the bed dimensions and the plant spacing, and this calculator lays out the planting grid, answers the total plants the bed honestly carries, and shows the rows-and-columns arithmetic so the layout fits on the seed packet.",
 "across = floor(length / spacing); down = floor(width / spacing); total = across \u00d7 down",
 "a 3 by 1.2 metre bed spacing 30 cm carries 10 across and 4 down \u2014 40 plants with none competing",
 ["vegetable beds", "annual borders", "seed order sizing", "succession planning"],
 "Spacing on the packet is the plant's mature radius, not its seedling size \u2014 tight spacing trades yield for upkeep. Staggered double rows squeeze about 15% more from the same bed when the bed is wider than one arm's reach.",
 "w67",
 _f("w67-a", "Bed length (m)", "3") + _f("w67-b", "Bed width (m)", "1.2") + _f("w67-c", "Plant spacing (cm)", "30") +
 '''<button class="btn" onclick="w67()">Lay the grid</button>
  <div id="w67-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("insulation-value", "Insulation R-Value Calculator", "Calculators",
 "Thermal resistance and real heat loss in watts for any wall build-up",
 "Insulation sells in R-values while bills arrive in watts, and the two connect through a division nobody performs at the counter. Enter the insulation thickness, its conductivity, the wall area and the winter temperature gap, and this calculator computes the R-value, the conductance, and the steady watts flowing through \u2014 the number the heating bill actually pays for.",
 "R = thickness / conductivity; heat flow = area \u00d7 temperature gap / R",
 "a 10 cm layer at 0.035 conductivity reaches R-2.86 \u2014 still leaking 420 watts on a 20-degree winter day across 60 m\u00b2",
 ["renovation planning", "heating system sizing", "material comparisons", "condensation reviews"],
 "Halving conductivity or doubling thickness both double R \u2014 but cost lines rarely move in parallel, so compare by euro per added R point. The calculation is steady-state: real walls also lose heat through every poorly sealed junction the R-value politely ignores.",
 "w68",
 _f("w68-a", "Insulation thickness (m)", "0.1") + _f("w68-b", "Conductivity (W/mK)", "0.035") + _f("w68-c", "Wall area (m\u00b2)", "60") + _f("w68-d", "Temperature gap (\u00b0C)", "20") +
 '''<button class="btn" onclick="w68()">Compute the heat flow</button>
  <div id="w68-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("fertilizer-npk", "Fertilizer N-P-K Calculator", "Calculators",
 "Nitrogen grams translated into exactly how much fertiliser to apply",
 "Fertiliser bags speak percentages and lawns speak grams, and the translation happens once a season at most \u2014 usually wrong by a factor of two. Enter the area, the nitrogen target and the bag's N percentage with bag weight, and this calculator answers the exact grams of product needed, what share of the bag it is, and the monthly split the target implies.",
 "need N grams = area \u00d7 target; product grams = N grams / (N% / 100)",
 "100 m\u00b2 at a 3 g/m\u00b2 nitrogen target pulls 300 g of N \u2014 1.5 kg of product from a 20% blend sold in a 25 kg bag",
 ["lawn care", "vegetable beds", "sports turf", "bag comparison shopping"],
 "Nitrogen moves through soil fast, which is why split applications beat one heroic feeding \u2014 the target is a season's plan, not a day's event. Phosphorus rarely needs supplementing in established lawns; the heavy lifting is almost always nitrogen.",
 "w69",
 _f("w69-a", "Area (m\u00b2)", "100") + _f("w69-b", "Nitrogen target (g/m\u00b2)", "3") + _f("w69-c", "Bag N (%)", "20") + _f("w69-d", "Bag weight (kg)", "25") +
 '''<button class="btn" onclick="w69()">Dose the feed</button>
  <div id="w69-out" class="result" aria-live="polite"></div>'''))

ADV23.append(("days-until-christmas", "Days Until Christmas Calculator", "Calculators",
 "A countdown between any two dates with weeks and weekends named",
 "Countdowns carry plans: shopping budgets, travel bookings and shipping cut-offs all hang on the exact number of days and weekends remaining. Pick a from date and a target date, and this calculator answers the days, the weeks and spare days, the full weekends inside, and how the rest of the run divides between shopping days and posting days.",
 "days = target \u2212 from in calendar days; weeks and weekends computed from the span",
 "from 24 November to Christmas Day is 31 days \u2014 4.4 weeks with four full weekends inside for shopping and posting",
 ["holiday shipping deadlines", "gift budget pacing", "travel booking windows", "event countdowns"],
 "Count calendar days for deadlines and shipping \u2014 working days are a different instrument with holidays inside them, and couriers publish in one while planners think in the other. The full weekends line matters because most of the countdown's usable hours hide there.",
 "w70",
 '<div><label for="w70-a">From date</label><input type="date" id="w70-a" value="2026-11-24" /></div>\n  <div><label for="w70-b">Target date</label><input type="date" id="w70-b" value="2026-12-25" /></div>' +
 '''<button class="btn" onclick="w70()">Count the days</button>
  <div id="w70-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV23:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA23[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'<div class="panel">{extra}{tail}</div>',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT23[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
