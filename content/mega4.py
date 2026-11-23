# -*- coding: utf-8 -*-
"""Batch 18: eight brand-new flagship tools, built with the mega3 pattern."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA4 = {}
CONTENT4 = {}

ADV4 = []

TZ_OPTS = [
    ("America/Los_Angeles", "Los Angeles"), ("America/Denver", "Denver"),
    ("America/Chicago", "Chicago"), ("America/New_York", "New York"),
    ("America/Toronto", "Toronto"), ("America/Mexico_City", "Mexico City"),
    ("America/Sao_Paulo", "Sao Paulo"), ("Europe/London", "London"),
    ("Europe/Paris", "Paris"), ("Europe/Berlin", "Berlin"),
    ("Europe/Madrid", "Madrid"), ("Europe/Rome", "Rome"),
    ("Europe/Athens", "Athens"), ("Europe/Istanbul", "Istanbul"),
    ("Europe/Moscow", "Moscow"), ("Africa/Lagos", "Lagos"),
    ("Africa/Cairo", "Cairo"), ("Africa/Johannesburg", "Johannesburg"),
    ("Asia/Dubai", "Dubai"), ("Asia/Karachi", "Karachi"),
    ("Asia/Kolkata", "Mumbai (Kolkata)"), ("Asia/Bangkok", "Bangkok"),
    ("Asia/Singapore", "Singapore"), ("Asia/Shanghai", "Shanghai"),
    ("Asia/Hong_Kong", "Hong Kong"), ("Asia/Tokyo", "Tokyo"),
    ("Asia/Seoul", "Seoul"), ("Australia/Sydney", "Sydney"),
    ("Australia/Perth", "Perth"), ("Pacific/Auckland", "Auckland"),
    ("UTC", "UTC"),
]


def _tzsel(i, l):
    o = "".join(f'<option value="{v}">{t}</option>' for v, t in TZ_OPTS)
    return f'<div><label for="{i}">{l}</label><select id="{i}">{o}</select></div>'


ADV4.append(("time-zone-converter", "Time Zone Converter", "Date & Time Tools",
 "Convert a date and time between 31 world cities with real daylight-saving rules",
 "The trap is daylight saving: the New York\u2013London offset is five hours most of the year but four while the two switch-over dates differ. This converter applies the real IANA rules on the exact date entered, so March plans do not fail in June.",
 "target time = source wall time \u2212 source UTC offset + target UTC offset (offsets resolved per IANA rules for the chosen date)",
 "2:30 PM on 15 June in New York converts to 8:30 PM in Paris; the same clock time on 15 January is 7:30 PM",
 ["scheduling international calls and interviews", "planning travel itineraries and layovers", "coordinating remote teams across continents", "checking market and deadline times"],
 "Never schedule by memory across DST boundaries: pick the actual meeting date in the converter so the missing (or extra) hour is caught before the invite goes out.",
 "tz3",
 '''<div class="row"><div><label for="tz3-dt">Date &amp; time to convert (leave blank for right now)</label><input type="datetime-local" id="tz3-dt" autocomplete="off" /></div>''' + _tzsel("tz3-f", "From city") + _tzsel("tz3-t", "To city") + '''</div>''' + '''<button class="btn" onclick="tz3()">Convert time</button>
  <div id="tz3-out" class="result" aria-live="polite"></div>'''))

ADV4.append(("morse-code-translator", "Morse Code Translator", "Text Tools",
 "Translate text to Morse code and back, with audio playback of the signal",
 "Morse code encodes every letter as a short pattern of dots and dashes, and it is still alive in radio, aviation beacons, amateur radio licences and countless puzzles. The hard part is that it is not a one-for-one symbol swap: each letter is one to five signals long, so timing and separators carry meaning exactly like brackets do in math. This translator handles both directions, plays the code aloud and works as you type.",
 "text becomes dot\u2013dash patterns (E = \u00b7, T = \u2013, S = \u00b7\u00b7\u00b7, O = \u2013\u2013\u2013); patterns separated by spaces decode back letter by letter, with / marking word breaks",
 "\u201cSOS MSCALE\u201d becomes \u00b7\u00b7\u00b7 / \u2013\u2013\u2013 / \u00b7\u00b7\u00b7 // M \u00b7\u2013 S \u00b7\u00b7\u00b7 A \u00b7\u2013 C \u2013\u00b7\u00b7 L \u00b7\u2013\u00b7\u00b7 E \u00b7",
 ["ham radio and shortwave hobbyists", "escape-room and puzzle design", "learning emergency signalling", "adding authentic flavour to games and stories"],
 "Punctuation exists too \u2014 the period is \u00b7\u2212\u00b7\u2212\u00b7\u2212 and the comma is \u2212\u2212\u00b7\u00b7\u2212\u2212 \u2014 but most nets spell unusual characters out letter by letter to stay unambiguous.",
 "mo3",
 '''<div><label for="mo3-in">Plain text or Morse code (dots and dashes, / or | between words)</label><textarea id="mo3-in" rows="4" oninput="mo3()" placeholder="Type text, or paste Morse like .... ...">SOS MSCALE</textarea></div>
  <div class="btnrow"><button class="btn" onclick="mo3()">Translate</button><button class="btn ghost" onclick="mo3Swap()">Use result as input</button><button class="btn ghost" onclick="mo3Play(this)">Play audio</button></div>
  <div id="mo3-out" class="result" aria-live="polite"></div>'''))

ADV4.append(("statistics-calculator", "Statistics Calculator (Mean, Median, SD)", "Calculators",
 "Paste any list of numbers for mean, median, mode, sd, quartiles and spread",
 "Test scores, weekly sales, lab readings, delivery times \u2014 one column of numbers is the most common dataset there is, and the questions are always the same: what is typical, how spread out is it, are there outliers. This calculator answers all of that from one pasted list, including quartiles, so nothing has to be hand-sorted.",
 "mean = \u03a3x/n; median = middle of the sorted list; sample sd = \u221a(\u03a3(x\u2212mean)\u00b2/(n\u22121)); quartiles by linear interpolation",
 "12, 15, 15, 18, 22 gives mean 16.4, median 15, sample sd 3.78, range 10 and mode 15",
 ["summarising survey or test results", "checking spread before computing averages", "spotting outliers in experiment data", "homework checks for statistics courses"],
 "Mean and median disagree when the data is skewed: if the mean is well above the median, a few large values \u2014 not the typical case \u2014 are pulling it up.",
 "st3",
 '''<div><label for="st3-in">Your numbers (any separators: spaces, commas, new lines)</label><textarea id="st3-in" rows="4" oninput="st3()" placeholder="e.g. 12, 15, 15, 18, 22">12, 15, 15, 18, 22</textarea></div>''' + '''<button class="btn" onclick="st3()">Analyze numbers</button>
  <div id="st3-out" class="result" aria-live="polite"></div>'''))

ADV4.append(("speed-distance-time-calculator", "Speed Distance Time Calculator", "Calculators",
 "Solve for speed, distance or time with ready unit conversions and pace",
 "Distance, speed and time are locked together by one triangle of formulas, and which one you need depends on which number is missing \u2014 that is why half-built spreadsheet templates fail when the question changes. This calculator solves for any of the three: type what you know, pick what to find, and read the answer with the useful conversions (mph, m/s, minutes per kilometre) already computed.",
 "speed = distance \u00f7 time; distance = speed \u00d7 time; time = distance \u00f7 speed (keep units consistent: km with hours, miles with hours)",
 "120 km at 80 km/h takes 1.5 hours; at that speed 0.75 minutes pass per kilometre",
 ["trip and commute planning", "tracking and race estimates", "logistics and delivery ETAs", "physics homework on uniform motion"],
 "Time inputs are hours \u2014 enter 1.5 for an hour and a half, or solve for time and read the hours-and-minutes breakdown in the results instead of guessing the decimal.",
 "sd3",
 '''<div class="row">''' + _f("sd3-d", "Distance (km)", "120") + _f("sd3-s", "Speed (km/h)", "80") + _f("sd3-t", "Time (hours)", "") + _sel("sd3-m", "Solve for", [("speed", "Speed from distance & time"), ("distance", "Distance from speed & time"), ("time", "Time from distance & speed")]) + '''</div>''' + '''<button class="btn" onclick="sd3()">Solve</button>
  <div id="sd3-out" class="result" aria-live="polite"></div>'''))

ADV4.append(("fraction-calculator", "Fraction Calculator", "Calculators",
 "Add, subtract, multiply or divide fractions with automatic reduction",
 "Adding fractions by hand forces you through least-common denominators, and multiplying them tempts you into simplifying halfway and losing track. This calculator runs all four operations on two fractions, reduces the result to lowest terms automatically, shows the mixed-number form and the decimal equivalent, and explains itself when a denominator is zero \u2014 which is where most manual slips happen.",
 "(a/b) \u00b1 (c/d) = (ad \u00b1 cb)/bd; (a/b) \u00d7 (c/d) = ac/bd; (a/b) \u00f7 (c/d) = ad/bc \u2014 all results reduced by the greatest common divisor",
 "3/4 + 5/6 = (18 + 20)/24 = 38/24 which reduces to 19/12, written as the mixed number 1 7/12",
 ["cooking and recipe scaling", "helping with school maths homework", "woodworking and plan dimensions", "checking invoice or split quantities"],
 "Denominators must be non-zero, and dividing by a zero fraction is undefined \u2014 the tool says so explicitly instead of showing a nonsense number.",
 "fc3",
 '''<div class="row">''' + _f("fc3-a", "Numerator 1", "3") + _f("fc3-b", "Denominator 1", "4") + _sel("fc3-op", "Operation", [("+", "Add (+)"), ("-", "Subtract (\u2212)"), ("*", "Multiply (\u00d7)"), ("/", "Divide (\u00f7)")]) + _f("fc3-c", "Numerator 2", "5") + _f("fc3-d", "Denominator 2", "6") + '''</div>''' + '''<button class="btn" onclick="fc3()">Calculate fractions</button>
  <div id="fc3-out" class="result" aria-live="polite"></div>'''))

GP3_ROW = '''<div class="row gp3-row"><div><input class="in" type="text" placeholder="Course name (optional)" aria-label="Course" autocomplete="off"></div><div><select class="gp3-g" aria-label="Grade (4.0 scale)"><option value="4">A (4.0)</option><option value="3.7">A- (3.7)</option><option value="3.3">B+ (3.3)</option><option value="3">B (3.0)</option><option value="2.7">B- (2.7)</option><option value="2.3">C+ (2.3)</option><option value="2">C (2.0)</option><option value="1.7">C- (1.7)</option><option value="1.3">D+ (1.3)</option><option value="1">D (1.0)</option><option value="0">F (0.0)</option></select></div><div><input class="in gp3-cre" type="number" step="any" min="0" value="3" aria-label="Credits" autocomplete="off"></div><div><button type="button" class="btn ghost" onclick="gp3Del(this)" aria-label="Remove course">&times;</button></div></div>'''

GP3_ROW_1 = '''<div class="row gp3-row"><div><label for="gp3-g-1">Course</label><input class="in" type="text" id="gp3-g-1" placeholder="Course name (optional)" autocomplete="off"></div><div><label for="gp3-g-2">Grade (4.0 scale)</label><select class="gp3-g" id="gp3-g-2"><option value="4">A (4.0)</option><option value="3.7">A- (3.7)</option><option value="3.3">B+ (3.3)</option><option value="3">B (3.0)</option><option value="2.7">B- (2.7)</option><option value="2.3">C+ (2.3)</option><option value="2">C (2.0)</option><option value="1.7">C- (1.7)</option><option value="1.3">D+ (1.3)</option><option value="1">D (1.0)</option><option value="0">F (0.0)</option></select></div><div><label for="gp3-g-3">Credits</label><input class="in gp3-cre" id="gp3-g-3" type="number" step="any" min="0" value="3" autocomplete="off"></div><div><button type="button" class="btn ghost" onclick="gp3Del(this)" aria-label="Remove course">&times;</button></div></div>'''

ADV4.append(("gpa-calculator", "GPA Calculator (4.0 Scale)", "Calculators",
 "Credit-weighted GPA on the 4.0 scale with add/remove course rows",
 "A grade point average is not the average of your grades; it is weighted by credits, so a hard four-credit class moves it more than a one-credit seminar. This calculator weights every course on the 4.0 scale, counts quality points, and lets you add or remove rows.",
 "GPA = \u03a3(grade points \u00d7 credits) \u00f7 \u03a3credits, on the 4.0 scale where A = 4.0, B = 3.0, C = 2.0, D = 1.0 and F = 0.0",
 "four courses of A, B+ (3.3), B and A- (3.7) at 3 credits each give 39 quality points over 12 credits = 3.25",
 ["end-of-semester GPA checks", "umping scholarship and programme requirements", "planning what final grades are needed", "unweighted GPA comparisons between schools"],
 "Pluses and minuses matter \u2014 a B+ is 3.3, a third of the way to an A \u2014 so pick grade options carefully; rounding every grade to the bare letter changes the result.",
 "gp3",
 '''<div id="gp3-rows">''' + GP3_ROW_1 + GP3_ROW * 3 + '''</div>''' + '''<div class="btnrow"><button class="btn" onclick="gp3()">Calculate GPA</button><button class="btn ghost" onclick="gp3Add()">+ Add course</button></div>
  <div id="gp3-out" class="result" aria-live="polite"></div>'''))

ADV4.append(("depreciation-calculator", "Depreciation Calculator", "Finance & Business",
 "Straight-line or double-declining depreciation schedule year by year",
 "Assets lose value on a schedule, and accounting and tax rules want that schedule written down. Straight-line depreciation spreads the loss evenly across the useful life, while the double-declining balance front-loads it \u2014 the choice changes year-by-year profit and the book value you can defend in an audit. This calculator draws the full schedule under either method, year by year, down to salvage value.",
 "straight line: annual depreciation = (cost \u2212 salvage) \u00f7 life; double declining: rate = 2 \u00f7 life applied to current book value, never below salvage",
 "a 20,000 machine with 2,000 salvage over 5 years loses 3,600 per year straight-line; double-declining starts at 8,000 in year one and tapers",
 ["fixed-asset accounting schedules", "tax and book-value planning", "resale and trade-in decisions", "small-business equipment budgeting"],
 "Book value is an accounting figure, not the market price \u2014 a fully depreciated laptop can still sell used; the numbers answer different questions.",
 "dp3",
 '''<div class="row">''' + _f("dp3-c", "Asset cost", "20000") + _f("dp3-s", "Salvage value", "2000") + _f("dp3-y", "Useful life (years)", "5") + _sel("dp3-m", "Method", [("sl", "Straight line"), ("ddb", "Double declining balance")]) + '''</div>''' + '''<button class="btn" onclick="dp3()">Build schedule</button>
  <div id="dp3-out" class="result" aria-live="polite"></div>
  <div class="uc-tablewrap"><table class="uc-table" id="dp3-table" aria-label="Depreciation schedule"></table></div>'''))

ADV4.append(("water-intake-calculator", "Water Intake Calculator", "Calculators",
 "Daily water target scaled to body weight, exercise minutes and climate",
 "The old Old advice says eight glasses a day; real need depends on body size and sweat loss. A baseline scales fluid to weight, then adds exercise and heat, and the tool shows it in cups and glasses.",
 "daily water \u2248 33 ml per kg of body weight + 500 ml per 30 minutes of exercise, +12% allowance for hot or humid conditions",
 "70 kg, 60 minutes of exercise, hot climate: 2.3 L + 1.0 L + 12% \u2192 3.7 L per day",
 ["setting a daily hydration target", "training and gym hydration planning", "adjusting for summer or hot climates", "office and wellness-programme goals"],
 "Water is not the only source \u2014 food, tea and coffee also count toward the total, so do not score them as zero.",
 "wq3",
 '''<div class="row">''' + _f("wq3-w", "Body weight (kg)", "70") + _f("wq3-x", "Exercise per day (minutes)", "30") + _sel("wq3-cl", "Climate", [("mild", "Mild / indoor"), ("hot", "Hot or humid")]) + '''</div>''' + '''<button class="btn" onclick="wq3()">Calculate intake</button>
  <div id="wq3-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV4:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA4[slug] = {"name": name, "cat": cat, "short": short,
                   "body": f'''<div class="panel">{extra}{tail}</div>''',
                   "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT4[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
