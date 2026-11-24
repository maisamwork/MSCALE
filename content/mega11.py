# -*- coding: utf-8 -*-
"""Batch 25: eight more brand-new flagship tools, mega3-10 pattern."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA11 = {}
CONTENT11 = {}

ADV11 = []

ADV11.append(("shoe-size-converter", "Shoe Size Converter", "Converters",
 "Foot length in cm to US, UK and EU shoe sizes, both directions",
 "Shoe numbers differ by region and by how the size was measured, which is why the same foot is a US 8, a UK 7 and an EU 40-41. Enter a foot length in centimetres or a US size, and this converter answers all three systems at once with the standard last-length formulas, plus separate men's and women's US scales.",
 "UK = 3 \u00d7 foot length in inches \u2212 23; US men = UK + 1; US women = UK + 2; EU \u2248 UK + 33",
 "a 26 cm foot is a US men's 8.7, UK 7.7, EU about 40.7 \u2014 women's US 9.7",
 ["online shoe ordering", "shopping abroad", "kids' growth measurements", "gift-buying for relatives far away"],
 "Sizes convert on paper but shoes fit on feet \u2014 width, brand lasts and sock thickness move the best size by half a step in either direction.",
 "sh3",
 _f("sh3-c", "Foot length (cm)", "26") + _f("sh3-u", "Or enter US men's size", "") +
 '''<button class="btn" onclick="sh3()">Convert shoe size</button>
  <div id="sh3-out" class="result" aria-live="polite"></div>'''))

ADV11.append(("tv-viewing-distance-calculator", "TV Viewing Distance Calculator", "Calculators",
 "How far to sit from any TV size for 4K, 1080p or cinema feel",
 "Sit too close to an HD set and you see pixels; sit too far from a 4K one and you paid for detail you cannot resolve. Enter the diagonal and resolution, and this calculator gives the resolution-limited distance band plus the THX 40-degree cinema recommendation, and \u2014 with your actual distance \u2014 the field of view you are currently getting.",
 "4K: 1.0\u20131.5 \u00d7 diagonal; 1080p: 1.5\u20132.5 \u00d7; THX cinema: 1.37 \u00d7; angle = 2 \u00d7 arctan(half-width \u00f7 distance)",
 "a 55-inch 4K set resolves fully from 4.6 ft and is best before 5.7 ft; THX cinema says 6.3 ft",
 ["living-room layout planning", "TV and projector buying", "gaming monitor setups", "home-cinema design"],
 "Distance advice changed with resolution \u2014 the old \u201ctwice the diagonal\u201d rule was written for 1080p and leaves a 4K screen feeling undersized from across the room.",
 "tv2",
 _f("tv2-d", "Screen diagonal (inches)", "55") + _sel("tv2-r", "Resolution", [("4k", "4K / 2160p"), ("1080", "1080p"), ("720", "720p"), ("8k", "8K / 4320p")]) + _f("tv2-m", "Your actual distance (ft, optional)", "8") +
 '''<button class="btn" onclick="tv2()">Calculate distance</button>
  <div id="tv2-out" class="result" aria-live="polite"></div>'''))

ADV11.append(("cooking-measurement-converter", "Cooking Measurement Converter", "Calculators",
 "Cups to grams per ingredient, plus tsp, tbsp, ml and ounces",
 "\u201cOne cup of flour\u201d is 125 grams; one cup of honey is 340 \u2014 volume-only converters quietly wreck baking. Choose an ingredient from the kitchen density table, enter the amount, and this converter answers in grams and ounces, converts cups, tablespoons, teaspoons, millilitres and fluid ounces among themselves, and shows the per-cup density it used.",
 "grams = volume in ml \u00d7 ingredient density (g per 240 ml cup); 1 cup = 16 tbsp = 48 tsp",
 "2 cups of flour weigh 250 g while 2 cups of honey weigh 680 g \u2014 same cup, different cake",
 ["baking by weight like the recipes say", "scaling bread and cake dough", "converting american recipes", "meal-prep portioning"],
 "Spoon flour into the cup rather than scooping \u2014 a scooped cup can carry 20% more flour, enough to turn bread into a brick.",
 "ck2",
 _sel("ck2-i", "Ingredient", [("125", "All-purpose flour (125 g/cup)"), ("200", "Granulated sugar (200 g/cup)"), ("200", "Brown sugar, packed (200 g/cup)"), ("227", "Butter (227 g/cup)"), ("85", "Cocoa powder (85 g/cup)"), ("340", "Honey / syrup (340 g/cup)"), ("185", "Uncooked white rice (185 g/cup)"), ("216", "Vegetable oil (216 g/cup)"), ("240", "Milk / water-like liquids (240 g/cup)")]) +
 _f("ck2-v", "Amount", "2") + _sel("ck2-u", "Unit", [("cup", "Cups"), ("tbsp", "Tablespoons"), ("tsp", "Teaspoons"), ("ml", "Millilitres"), ("floz", "Fluid ounces (US)")]) +
 '''<button class="btn" onclick="ck2()">Convert measure</button>
  <div id="ck2-out" class="result" aria-live="polite"></div>'''))

ADV11.append(("commute-cost-calculator", "Commute Cost Calculator", "Finance & Business",
 "Daily drive multiplied into weekly, monthly and yearly money",
 "A commute is a salary line item hiding in plain sight: fuel, tolls and parking compound over two hundred-plus working days. Enter the one-way distance, consumption, fuel price and parking or tolls, and this calculator converts the trip into per-day, per-week, per-month and annual costs so moving, remote days or carpooling can be judged with numbers.",
 "daily fuel = 2 \u00d7 distance \u00f7 mpg \u00d7 price; monthly adds parking once; annual = weekly \u00d7 52",
 "12 miles each way at 28 mpg and 3.50 a gallon is 3.00 of fuel a day \u2014 about 1,980 a year with 100 a month parking",
 ["remote-work savings maths", "moving house decisions", "carpool split negotiation", "company travel policy checks"],
 "Fuel price swings do most of the damage quietly \u2014 rerun this after any big petrol change and check whether the answer still justifies the drive.",
 "cq2",
 _f("cq2-d", "One-way distance (miles)", "12") + _f("cq2-g", "Fuel economy (mpg)", "28") + _f("cq2-p", "Fuel price per gallon", "3.50") +
 _f("cq2-w", "Driving days per week", "5") + _f("cq2-t", "Tolls per day (both directions)", "0") + _f("cq2-k", "Parking per month", "100") +
 '''<button class="btn" onclick="cq2()">Cost the commute</button>
  <div id="cq2-out" class="result" aria-live="polite"></div>'''))

ADV11.append(("mileage-reimbursement-calculator", "Mileage Reimbursement Calculator", "Finance & Business",
 "Track-driven reimbursement at any per-mile rate with yearly totals",
 "Reimbursing staff or self-claiming business miles needs the same arithmetic every month: miles driven \u00d7 agreed rate, with the rate decision either IRS-style or your own contract's. Enter the miles and the rate, add trip counts per month if you like, and the calculator outputs per-claim, monthly and full-year totals with a comparison against the standard IRS rate.",
 "claim = miles \u00d7 rate; annual = monthly miles \u00d7 12 \u00d7 rate",
 "900 business miles at the 0.70 IRS-style rate repays 630 in a month and 7,560 across the year",
 ["small-business expense policy", "contractor travel claims", "volunteer mileage returns", "checking an employer's rate"],
 "Log trips when they happen \u2014 reconstructed mileage logs are the first thing auditors test, and monthly estimates compound into sloppy claims.",
 "mr2",
 _f("mr2-m", "Miles per month", "900") + _f("mr2-r", "Rate per mile", "0.70") +
 '''<button class="btn" onclick="mr2()">Calculate claim</button>
  <div id="mr2-out" class="result" aria-live="polite"></div>'''))

ADV11.append(("study-plan-generator", "Study Plan Generator", "Date & Time Tools",
 "Spreads your subjects evenly across the days before an exam",
 "Revision collapses when every day starts by re-deciding what to study. List your subjects, set the exam date and how many session slots each day offers, and this generator spreads the subjects in rotation across every remaining day \u2014 later subjects are not written off early, and the plan shows exactly which pair or trio to sit down with on which date.",
 "days = exam date \u2212 today; day-by-day subjects rotate in list order: subject i goes to slot (day\u00d7slots + k) mod n",
 "three subjects with two slots a day reads \u201cDay 1: algebra, history\u201d, \u201cDay 2: biology, algebra\u201d \u2014 all the way to the exam",
 ["finals and GCSE prep weeks", "certification sprints", "language learning schedules", "driving-theory revision"],
 "Protect the plan from perfectionism \u2014 a skipped day is a rotation shift, not a restart, so just continue with the next listed slot.",
 "sp3",
 '''<div><label for="sp3-in">Subjects (one per line, in priority order)</label><textarea id="sp3-in" class="in" rows="4" placeholder="algebra\nhistory\nbiology"></textarea></div>''' +
 _f("sp3-e", "Exam date", "", "YYYY-MM-DD") + _f("sp3-s", "Sessions per day", "2") +
 '''<button class="btn" onclick="sp3()">Generate plan</button>
  <div id="sp3-out" class="result" aria-live="polite"></div>'''))

ADV11.append(("totp-code-checker", "TOTP Code Checker", "Security Tools",
 "Verify 2FA codes locally from any base32 secret \u2014 RFC 6238 exact",
 "Two-factor codes expire in thirty seconds, and a drifted clock or a typo in a pasted secret looks identical to a broken app until you verify by hand. Paste any base32 secret and this checker computes the current TOTP (and the next one) with real HMAC-SHA1 per RFC 6238 \u2014 all locally in your browser, with a live countdown to the next window.",
 "code = TRUNC(HMAC-SHA1(key, counter)) mod 10^digits, counter = floor(unix time \u00f7 30)",
 "the RFC 6238 test secret at unix time 59 yields 94287082 \u2014 the checker reproduces it digit for digit",
 ["verifying secrets pasted into an authenticator", "debugging server 2FA implementations", "clock-drift confusion", "learning how TOTP works"],
 "The secret generates codes forever \u2014 screen-share it once during support and the attacker owns the countdown too, so paste secrets only in private.",
 "to2",
 '''<div><label for="to2-k">Base32 secret (spaces auto-removed)</label><input id="to2-k" class="in" type="text" value="GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ" style="font-family:monospace" autocomplete="off"></div>''' +
 _sel("to2-d", "Digits", [("6", "6"), ("8", "8")]) + _sel("to2-p", "Period (s)", [("30", "30"), ("60", "60")]) + _f("to2-at", "Check at Unix time (advanced, blank = now)", "59") +
 '''<button class="btn" onclick="to2()">Compute code</button>
  <div id="to2-out" class="result" aria-live="polite"></div>'''))

ADV11.append(("salary-to-hourly-converter", "Salary to Hourly Converter", "Finance & Business",
 "Annual salary into hourly, daily, weekly and monthly rates, and back",
 "Comparing a staff job with hourly contract work needs the same denominator on both sides \u2014 and \u201cten pounds an hour\u201d hides whether the year is 2,080 hours or 1,800. Enter an annual salary (or flip the switch and type an hourly rate), set realistic hours and working weeks, and this converter answers hourly, daily, weekly, monthly and annual figures in one pass.",
 "hourly = annual \u00f7 (hours per week \u00d7 weeks per year); annual = hourly \u00d7 hours \u00d7 weeks",
 "52,000 across a standard 2,080-hour year is exactly 25 an hour \u2014 200 a day at eight hours",
 ["evaluating freelance day rates", "comparing two job offers", "setting contractor quotes", "checking a payslip salary"],
 "Contract hourly rates carry unpaid holiday, sick days and no employer pension \u2014 contractors typically charge 30\u201350% above the staff-equivalent hourly figure for that reason.",
 "sa3",
 _f("sa3-a", "Annual salary", "52000") + _f("sa3-h", "Hours per week", "40") + _f("sa3-w", "Paid weeks per year", "52") + _f("sa3-r", "Or enter hourly rate to reverse", "") +
 '''<button class="btn" onclick="sa3()">Convert salary</button>
  <div id="sa3-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV11:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA11[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'''<div class="panel">{extra}{tail}</div>''',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT11[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
