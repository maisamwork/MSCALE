# -*- coding: utf-8 -*-
"""Batch 24: eight more brand-new flagship tools, mega3-9 pattern."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA10 = {}
CONTENT10 = {}

ADV10 = []

ADV10.append(("time-card-calculator", "Time Card Calculator", "Finance & Business",
 "Five daily hour totals into weekly pay with overtime split",
 "Adding up a paper time card by hand invites exactly one 40-minute mistake that costs real wages. Enter the hours for each weekday plus the rate, and this calculator totals the week, splits regular from overtime past your threshold, and prints biweekly and quarterly projections so the payslip can be checked before payday, not after.",
 "weekly pay = rate \u00d7 regular hours + 1.5 \u00d7 rate \u00d7 hours past the threshold",
 "8, 8, 7.5, 9 and 8.5 hours at 20 an hour is 41 total \u2014 800 regular plus 30 of overtime, 830 for the week",
 ["hourly payroll checking", "contractor timesheet audits", "part-time schedule math", "summer-job wage disputes"],
 "Blank days count as zero rather than erroring \u2014 for split shifts such as 8\u201312 and 1\u20135, enter the total 8 for the day.",
 "tc2",
 _f("tc2-d1", "Monday (h)", "8") + _f("tc2-d2", "Tuesday (h)", "8") + _f("tc2-d3", "Wednesday (h)", "7.5") +
 _f("tc2-d4", "Thursday (h)", "9") + _f("tc2-d5", "Friday (h)", "8.5") +
 _f("tc2-r", "Hourly rate", "20") + _f("tc2-t", "Overtime starts after (h/week)", "40") +
 '''<button class="btn" onclick="tc2()">Total the week</button>
  <div id="tc2-out" class="result" aria-live="polite"></div>'''))

ADV10.append(("subnet-calculator", "Subnet Calculator", "Developer Tools",
 "IPv4 CIDR to mask, broadcast, host range and usable count",
 "Working out which addresses a /26 actually contains needs integer masks most people would rather never compute by hand. Paste any IPv4 address with its CIDR prefix and this calculator shows the mask, wildcard, network and broadcast addresses, the exact usable host range and count, plus a private-address flag \u2014 all with the binary shown against each octet.",
 "mask = 32\u2212prefix leading ones; network = ip AND mask; hosts = 2^(32\u2212prefix) \u2212 2",
 "192.168.10.5/26 gives mask 255.255.255.192, network 192.168.10.0, broadcast .63 and 62 usable hosts",
 ["planning office LANs", "AWS or GCP subnet sizing", "firewall and ACL writing", "certification study (Network+, CCNA)"],
 "A /31 has no room for the reserved network and broadcast pair the two-subtracted hosts assume \u2014 point-to-point links make that exception on purpose.",
 "ip2",
 _f("ip2-in", "IPv4 address with CIDR (e.g. 192.168.10.5/26)", "192.168.10.5/26", ) +
 '''<button class="btn" onclick="ip2()">Break down subnet</button>
  <div id="ip2-out" class="result" aria-live="polite"></div>'''))

ADV10.append(("board-foot-calculator", "Board Foot Calculator", "Calculators",
 "Lumber volume in board feet with a full order cost",
 "Lumber is sold by the board foot, yet every project list speaks in inches and feet of different dimensions. Enter thickness and width in inches, length in feet and piece count, and this calculator converts each board to board feet, multiplies out the order, shows the cubic-metre equivalent mills quote and totals the cost at your price per board foot.",
 "board feet = thickness(in) \u00d7 width(in) \u00d7 length(ft) \u00f7 12, \u00d7 quantity; 1 BF \u2248 0.00236 m\u00b3",
 "ten boards at 1 \u00d7 6 inches \u00d7 8 feet are 40 BF \u2014 128.00 at 3.20 per board foot",
 ["hardwood lumber ordering", "workshop and shelving projects", "comparing sawmill quotes", "decking and trim estimating"],
 "Ask whether quoted stock is rough or finished \u2014 planing a rough 4/4 board down to 3/4 inch quietly deletes a quarter of the volume you are paying for.",
 "bf2",
 _f("bf2-q", "Number of pieces", "10") + _f("bf2-t", "Thickness (in)", "1") + _f("bf2-w", "Width (in)", "6") +
 _f("bf2-l", "Length (ft)", "8") + _f("bf2-c", "Cost per board foot (optional)", "3.20") +
 '''<button class="btn" onclick="bf2()">Calculate board feet</button>
  <div id="bf2-out" class="result" aria-live="polite"></div>'''))

ADV10.append(("ring-size-converter", "Ring Size Converter", "Converters",
 "Inside diameter to US, UK and circumference ring sizes",
 "Surprising a partner with a ring means guessing a size without admitting anything. Measure an existing ring's inside diameter in millimetres \u2014 or enter a US size \u2014 and this converter reports the equivalent US, UK and EU sizes plus the inside circumference jewellers measure with just diameter and arithmetic.",
 "diameter mm = 11.63 + 0.8128 \u00d7 US size; circumference = \u03c0 \u00d7 diameter",
 "a 16.5 mm inside diameter is a US 6.0, UK about 5.5, with a 51.8 mm inside circumference",
 ["secret engagement planning", "online jewellery orders", "resale and vintage listings", "international size confusion"],
 "Knuckle-heavy fingers need a quarter size up and wide bands dress tight \u2014 when a measurement sits between sizes, jewellers say take the larger.",
 "rg2",
 _f("rg2-d", "Inside diameter (mm)", "16.5") + _f("rg2-u", "Or enter US ring size", "") +
 '''<button class="btn" onclick="rg2()">Convert ring size</button>
  <div id="rg2-out" class="result" aria-live="polite"></div>'''))

ADV10.append(("caesar-cipher", "Caesar Cipher Encoder", "Security Tools",
 "Shift-encode and decode text, with all 25 shifts visible at a tap",
 "The Caesar shift is the first cipher most people meet, and it still teaches everything about substitution: every letter slides through the alphabet by a fixed amount, punctuation untouched. Type text, pick the shift, and this tool encodes or decodes instantly, keeps capitals in place, and offers a brute-force panel listing all 25 reads so any caught message explains itself.",
 "encryption: (letter index + shift) mod 26 for A\u2013Z and a\u2013z; every other character passes through",
 "\u201cHello, World!\u201d shifted by 3 becomes \u201cKhoor, Zruog!\u201d \u2014 and \u201cz\u201d wraps around to \u201cc\u201d",
 ["puzzle and escape-room design", "teaching modular arithmetic", "kids' secret notes", "CTF warm-up practice"],
 "Three shifts of history meet three keystrokes of cryptanalysis \u2014 with 25 possible keys a Caesar message is solved by looking, which is why nobody uses it for secrets.",
 "ce2",
 _f("ce2-in", "Text", "Hello, World!") + _f("ce2-s", "Shift (1\u201325)", "3") + _sel("ce2-d", "Direction", [("enc", "Encode"), ("dec", "Decode")]) +
 '''<button class="btn" onclick="ce2()">Apply cipher</button>
  <button class="btn ghost" onclick="ce2Brute()">Show all 25 shifts</button>
  <div id="ce2-out" class="result" aria-live="polite"></div>'''))

ADV10.append(("palindrome-checker", "Palindrome Checker", "Text Tools",
 "Checks words and phrases backwards with the cleaned text shown",
 "\u201cMadam, I'm Adam\u201d is a palindrome only if the commas and apostrophes politely step aside \u2014 and that cleaning step is where manual checking goes wrong. Paste any word, phrase or name and this checker strips punctuation and casing, compares the result to its reverse, shows the exact cleaned string it judged, and flags a same-turn verdict you can trust.",
 "palindrome if cleaned text (letters and digits only, case-folded) equals its own reversal",
 "\u201cA man, a plan, a canal: Panama!\u201d cleans to \u201camanaplanacanalpanama\u201d \u2014 21 characters, palindrome true",
 ["school and puzzle homework", "quirky domain or brand screening", "nameaday games", "teaching strings in code"],
 "Numbers count: 12321 passes while 1230 fails \u2014 and a single-character string is a palindrome only in the most boring sense of the word.",
 "pa2",
 '''<div><label for="pa2-in">Word, phrase or sentence</label><textarea id="pa2-in" class="in" rows="3" placeholder="A man, a plan, a canal: Panama!"></textarea></div>''' +
 '''<button class="btn" onclick="pa2()">Check palindrome</button>
  <div id="pa2-out" class="result" aria-live="polite"></div>'''))

ADV10.append(("bac-calculator", "BAC Calculator", "Calculators",
 "Widmark estimate of blood alcohol with elimination over time",
 "Blood alcohol follows a curve pharmacologists have modelled for a century: grams of alcohol divided by body water, minus per-hour elimination. Enter standard drinks, body weight, sex and hours elapsed, and this calculator estimates the current BAC with the Widmark method, states the legal-driving verdict against the 0.05 and 0.08 limits and shows the time until zero by elimination alone.",
 "BAC = (drinks \u00d7 14 g \u00f7 (weight g \u00d7 r)) \u00d7 100 \u2212 0.015 \u00d7 hours; r = 0.68 male, 0.55 female",
 "two standard drinks in a 70 kg man with no elapsed time estimates about 0.059 \u2014 over 0.08 takes more drinks, over 0.05 just hours",
 ["deciding when to hand over keys", "understanding unit labels on bottles", "health Teaching and safety courses", "checking medication warnings"],
 "Only a breathalyser measures you \u2014 this Widmark estimate assumes standard 14 g drinks, misses food timing and metabolism, and must never be used to argue legality.",
 "ba2",
 _f("ba2-d", "Standard drinks", "2") + _f("ba2-w", "Body weight (kg)", "70") +
 _sel("ba2-s", "Sex", [("m", "Male (r 0.68)"), ("f", "Female (r 0.55)")]) + _f("ba2-h", "Hours since drinking ended", "0") +
 '''<button class="btn" onclick="ba2()">Estimate BAC</button>
  <div id="ba2-out" class="result" aria-live="polite"></div>'''))

ADV10.append(("heart-rate-zones-calculator", "Heart Rate Zones Calculator", "Calculators",
 "Five training zones from age and resting heart rate",
 "Training by feel turns every easy run into a race; training by zones keeps effort honest. Enter your age and resting heart rate and this calculator applies the Karvonen method \u2014 zones based on how much heart-rate reserve you actually have, not the bare maximum \u2014 and lays out the five classic zones with their beats-per-minute ranges and what each zone trains.",
 "Karvonen: target = ((220 \u2212 age) \u2212 resting) \u00d7 zone % + resting",
 "age 30 with resting 60 has a 190 maximum and 130 reserve \u2014 zone 3 runs 151 to 164 bpm",
 ["polarised endurance training plans", "watch and strap zone setup", "rehab and cardiac programmes", "interval session design"],
 "The 220-minus-age maximum is a population average that misses individuals by ten beats or more \u2014 a field test beats the formula if you race seriously.",
 "hr2",
 _f("hr2-a", "Age", "30") + _f("hr2-r", "Resting heart rate (bpm)", "60") +
 '''<button class="btn" onclick="hr2()">Calculate zones</button>
  <div id="hr2-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV10:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA10[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'''<div class="panel">{extra}{tail}</div>''',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT10[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
