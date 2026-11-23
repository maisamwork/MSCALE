# -*- coding: utf-8 -*-
"""Batch 20: eight more brand-new flagship tools, mega3/4/5 pattern."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA6 = {}
CONTENT6 = {}

ADV6 = []

ADV6.append(("prime-factorization", "Prime Factorization Calculator", "Calculators",
 "Factor any integer to its primes with exponents, divisor count and working",
 "Every whole number above 1 is either prime or a product of primes, and that factorisation is its fingerprint. This calculator factorises any integer up to a trillion by trial division, shows the repeated-prime exponent form, counts the divisors and flags the primes outright \u2014 all the working shown, not just an answer.",
 "trial division by successive primes produces n = p1^a1 \u00d7 p2^a2 \u00d7 \u2026; divisor count = (a1+1)(a2+1)\u2026",
 "360 = 2^3 \u00d7 3^2 \u00d7 5 with (3+1)(2+1)(1+1) = 24 divisors \u2014 the count matches the divisor list the tool builds",
 ["simplifying fractions to lowest terms", "finding LCM and GCD foundations", "cryptography and number-theory homework", "checking whether large numbers are prime"],
 "Inputs above one trillion are rejected, not guessed \u2014 trial division needs the full range to stay exact, and a silent wrong answer is worse than a limit.",
 "pf2",
 '''<div class="row">''' + _f("pf2-n", "Number to factorise (1 to 1,000,000,000,000)", "360") + '''</div>''' + '''<button class="btn" onclick="pf2()">Factorise</button>
  <div id="pf2-out" class="result" aria-live="polite"></div>'''))

ADV6.append(("hourly-wage-calculator", "Hourly Wage Calculator", "Finance & Business",
 "Hourly rate and hours in, gross pay out with overtime and projections",
 "An advertised salary and an hourly rate hide each other behind different periods and unpaid breaks, which is why comparing offers is confusing. This calculator turns hours and rate into gross pay, applies overtime (time-and-a-half beyond your threshold by default, adjustable), and projects the weekly, monthly and yearly totals \u2014 all gross, before tax, so you can compare like with like.",
 "gross = rate \u00d7 regular hours + rate \u00d7 overtime multiplier \u00d7 overtime hours; projections multiply the weekly total by 52 and take a twelfth for monthly",
 "25/hour at 45 hours with overtime after 40 pays 1,187.50 for the week, 1,050 of it regular and 137.50 overtime",
 ["comparing job offers", "checking payslip totals", "budgeting on variable hours", "quoting freelance day rates"],
 "Gross is not take-home: taxes, insurance and deductions can remove a quarter or more, so compare net figures before signing anything.",
 "wg2",
 '''<div class="row">''' + _f("wg2-r", "Hourly rate", "25") + _f("wg2-h", "Hours this week", "45") + _f("wg2-o", "Overtime after (hours)", "40") + _f("wg2-m", "Overtime multiplier", "1.5") + '''</div>''' + '''<button class="btn" onclick="wg2()">Calculate pay</button>
  <div id="wg2-out" class="result" aria-live="polite"></div>'''))

ADV6.append(("random-string-generator", "Random String Generator", "Developer Tools",
 "Bulk crypto-random strings with charset, length and look-alike controls",
 "Test data needs strings that look nothing like words: API keys, session ids, filenames that never collide, filler rows for a database. This generator builds cryptographically random strings in bulk \\u2014 you choose the length, the character sets, how many, and whether look-alike characters (0/O, 1/l/I) are excluded so strings stay readable when humans type them back.",
 "the browser's crypto.getRandomValues supplies unbiased random indices into the enabled character set for every position of every string",
 "10 strings of 20 characters over 62 possible symbols gives 10 \u00d7 20 \u00d7 log2(62) \u2248 1,190 bits of entropy",
 ["generating API keys and tokens locally", "unique test fixtures and seed data", "collision-free temporary file names", "readable one-time codes without 0/O and 1/l"],
 "Cutting the character set cuts security proportionally: excluding look-alikes is fine for human-read codes but unnecessary for machine-only keys.",
 "rs2",
 '''<div class="row">''' + _f("rs2-l", "Length", "20") + _f("rs2-c", "How many", "10") + '''</div>''' + '''<div class="btnrow">
  <label class="pg-switch"><input type="checkbox" id="rs2-up" checked onchange="rs2()" /><span class="pg-track"></span> A-Z</label>
  <label class="pg-switch"><input type="checkbox" id="rs2-low" checked onchange="rs2()" /><span class="pg-track"></span> a-z</label>
  <label class="pg-switch"><input type="checkbox" id="rs2-dig" checked onchange="rs2()" /><span class="pg-track"></span> 0-9</label>
  <label class="pg-switch"><input type="checkbox" id="rs2-sym" onchange="rs2()" /><span class="pg-track"></span> Symbols</label>
  <label class="pg-switch"><input type="checkbox" id="rs2-amb" checked onchange="rs2()" /><span class="pg-track"></span> No look-alikes</label>
</div>''' + '''<button class="btn" onclick="rs2()">Generate</button>
  <textarea id="rs2-out" rows="5" readonly></textarea>'''))

ADV6.append(("text-repeater", "Text Repeater", "Text Tools",
 "Repeat any text N times with separator and numbering options",
 "Stamping a divider between sections, filling a test buffer, shouting a word a hundred times for a joke, or padding a document to a page count \\u2014 repeating text by hand is exactly the kind of chore computers exist for. Paste the text, set the count and the separator, and the repeated result appears live with a size readout before you copy it anywhere.",
 "output joins N copies (or numbered copies) with the chosen separator: none, space, comma, newline or a custom string",
 "\\u201cGo team!\\u201d repeated 10 times with newline joins to 10 lines \\u2014 about 90 characters total",
 ["creating dividers and ASCII decoration", "buffer data for testing", "building chants, lists and patterns", "padding text to an exact length"],
 "Counts above a few thousand silently produce megabytes: check the size readout before pasting into an email or an editor that charges by size.",
 "rp2",
 '''<div><label for="rp2-in">Text to repeat</label><textarea id="rp2-in" rows="3" oninput="rp2()" placeholder="Type text&hellip;">Go team!</textarea></div>''' + '''<div class="row">''' + _f("rp2-t", "Repeat times", "10") + _sel("rp2-s", "Separator", [("", "None"), (" ", "Space"), (", ", "Comma"), ("nl", "New line"), ("custom", "Custom\u2026")]) + _f("rp2-x", "Custom separator", "") + '''</div>''' + '''<label class="pg-switch"><input type="checkbox" id="rp2-num" onchange="rp2()" /><span class="pg-track"></span> Number each copy (1. 2. 3.)</label>
  <button class="btn" onclick="rp2()">Repeat</button>
  <textarea id="rp2-out" rows="5" readonly></textarea>
  <div id="rp2-meta" class="jf-stats" style="margin-top:10px"></div>'''))

ADV6.append(("coordinate-converter", "Coordinate Converter (DMS \u2194 Decimal)", "Converters",
 "GPS coordinates between decimal, DMS and degrees-decimal-minutes formats",
 "GPS devices spit out decimal degrees while nautical charts, property deeds and many apps expect degrees-minutes-seconds \u2014 and a misplaced second is about 30 metres on the ground. This converter runs both directions with live parsing, shows every format side by side (decimal, DMS, degrees-decimal-minutes), validates ranges so a longitude of 200 cannot slip through, and copies a clean result ready to paste into a map.",
 "decimal = degrees + minutes/60 + seconds/3600 (south and west negative); DMS reverses the arithmetic per axis",
 "40\u00b0 26\u2032 46\u2033 N, 79\u00b0 58\u2032 56\u2033 W = 40.446194, \u221279.982222 \u2014 the W is the negative sign, not a separate field",
 ["entering waypoints into different devices", "geocaching and surveying notes", "checking geo-tagged photo data", "aviation and marine paperwork"],
 "Longitude spans \u00b1180 and latitude \u00b190: values outside those bands are typos, and the converter refuses them instead of relocating your waypoint to an ocean.",
 "gc2",
 '''<div class="row">''' + _f("gc2-lat", "Latitude (decimal or 40 26 46)", "40.446194") + _f("gc2-lon", "Longitude (decimal or 79 58 56)", "-79.982222") + '''</div>''' + '''<button class="btn" onclick="gc2()">Convert coordinates</button>
  <div id="gc2-out" class="result" aria-live="polite"></div>'''))

ADV6.append(("scientific-notation-converter", "Scientific Notation Converter", "Converters",
 "Numbers to scientific, engineering and SI-prefix notation instantly",
 "Very large and very small numbers defeat ordinary reading: 0.00000031 hides its magnitude while 310,000,000,000 hides its precision. This converter moves any number between plain decimal, scientific notation (3.1 \u00d7 10\u2077), engineering notation (31 \u00d7 10\u2076) and the matching SI prefix (31 M) instantly, so figures go from unreadable to unambiguous whichever audience writes first.",
 "mantissa \u00d7 10^exponent with the mantissa in [1, 10) for scientific form; engineering form steps the exponent in multiples of three and attaches the matching SI prefix",
 "0.00000031 = 3.1 \u00d7 10\u207b\u2077 = 310 \u00d7 10\u207b\u2079 = 310 nano (n)",
 ["physics and chemistry notation", "engineering units and datasheets", "reading astronomical distances", "typing exact tiny tolerances"],
 "Scientific form also encodes precision: 3.1 \u00d7 10\u2077 claims two significant figures while 31000000 claims eight, so choose the form that matches what you actually measured.",
 "sn2",
 '''<div><label for="sn2-in">Number (plain or 3.1e-7 or 3.1\u00d710^-7)</label><input id="sn2-in" class="in" type="text" value="0.00000031" autocomplete="off"></div>''' + '''<button class="btn" onclick="sn2()">Convert</button>
  <div id="sn2-out" class="result" aria-live="polite"></div>'''))

ADV6.append(("caffeine-calculator", "Caffeine Calculator", "Calculators",
 "Track caffeine decay from dose and time with a half-life timeline",
 "Caffeine leaves the body exponentially: about half of a coffee's 95 mg is still acting on you five hours later, which is how an afternoon espresso can quietly schedule your 1 a.m. Another dose stacks on whatever remains from the last one. This calculator tracks that decay from your intake time, shows a mini timeline of remaining milligrams hour by hour, and names the cut-off time after which caffeine is more likely to steal sleep than give energy.",
 "remaining = dose \u00d7 0.5^(hours elapsed / half-life), half-life typically 5 hours and adjustable",
 "200 mg at 14:00 with a 5-hour half-life leaves 100 mg at 19:00, 50 mg at midnight and 25 mg at 5 a.m.",
 ["timing the last coffee of the day", "reading energy-drink labels", "checking medication timing interactions", "shifting off a caffeine-crash cycle"],
 "Half-life varies widely with genetics, pregnancy and medication \\u2014 treat the timeline as a model that helps you notice your own pattern, not a lab test.",
 "ke2",
 '''<div class="row">''' + _f("ke2-mg", "Caffeine dose (mg)", "200") + _f("ke2-hl", "Half-life (hours)", "5") + _f("ke2-el", "Hours since drinking it", "5") + '''</div>''' + '''<button class="btn" onclick="ke2()">Update levels</button>
  <div id="ke2-out" class="result" aria-live="polite"></div>'''))

ADV6.append(("luhn-checker", "Luhn Algorithm Checker", "Developer Tools",
 "Validate digit strings and compute missing Luhn check digits",
 "The Luhn checksum is the quiet workhorse printed into credit card numbers, IMEI digits, national id schemes and countless API keys: one check digit catches every single-character typo and almost all transpositions. This validator checks any digit string, computes the missing check digit when you leave it as X, and explains the arithmetic without touching any real account.",
 "every second digit from the right doubles (summing 9 for values above 9); the string is valid when the total modulo 10 is zero",
 "79927398713 is valid; 79927398714 shows which digits were doubled and why the total misses the next multiple of ten",
 ["testing payment-form validation", "validating IMEI and id numbers", "building quiz and interview examples", "checking digit entry in CLI tools"],
 "A valid Luhn string is not a real card or valid account \u2014 it only proves no digit was mistyped, which is exactly why the check lives inside the number.",
 "lc2",
 '''<div><label for="lc2-in">Digit string (use X for an unknown check digit)</label><input id="lc2-in" class="in" type="text" style="font-family:monospace" value="79927398713" autocomplete="off"></div>''' + '''<button class="btn" onclick="lc2()">Validate</button>
  <div id="lc2-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV6:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA6[slug] = {"name": name, "cat": cat, "short": short,
                   "body": f'''<div class="panel">{extra}{tail}</div>''',
                   "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT6[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
