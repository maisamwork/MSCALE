# -*- coding: utf-8 -*-
"""Batch 26: eight more brand-new flagship tools, mega3-11 pattern."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA12 = {}
CONTENT12 = {}

ADV12 = []

ADV12.append(("cagr-calculator", "CAGR Calculator", "Finance & Business",
 "Compound annual growth rate between two values and a year count",
 "An investment that doubled is impressive until you learn it took twenty years. Compound annual growth rate compresses any start value, end value and holding period into one comparable yearly percentage \u2014 the honest rate for pitting funds, property, revenue or a portfolio against each other. Enter the two values and the years to see the rate, the growth multiple and a doubling estimate.",
 "CAGR = (end \u00f7 start)^(1 \u00f7 years) \u2212 1; doubling time \u2248 ln 2 \u00f7 ln(1 + CAGR)",
 "10,000 growing to 25,000 across 8 years is a 12.14% CAGR \u2014 and doubles again in about 6.1 more years",
 ["comparing fund and ETF track records", "revenue growth targets in plans", "property value appreciation", "checking advisor performance claims"],
 "Irregular contributions muddy the figure \u2014 for money added along the way use a money-weighted return instead. Rule of 72 is the quick cousin: 72 \u00f7 the percentage rate estimates the doubling time in years.",
 "ca2",
 _f("ca2-b", "Start value", "10000") + _f("ca2-e", "End value", "25000") + _f("ca2-y", "Years held", "8") +
 '''<button class="btn" onclick="ca2()">Calculate CAGR</button>
  <div id="ca2-out" class="result" aria-live="polite"></div>'''))

ADV12.append(("ev-charging-cost-calculator", "EV Charging Cost Calculator", "Calculators",
 "Battery percentage points into kWh, cost, added range and price per mile",
 "Charging at home trickily bills by the kilowatt-hour while drivers think in miles, so \u201cwhat did tonight cost?\u201d needs three conversions at once. Enter the battery size, the charge window and your electric rate with efficiency, and this calculator answers kWh delivered, money out, miles added, cost per 100 miles and miles per dollar \u2014 the real comparison against petrol.",
 "kWh = battery \u00d7 (target \u2212 current) \u00f7 100; cost = kWh \u00d7 rate; miles added = kWh \u00d7 mi/kWh",
 "taking a 75 kWh pack from 20% to 80% moves 45 kWh \u2014 6.75 at 0.15/kWh and about 158 miles added",
 ["home wallbox budgeting", "public charger price checks", "road-trip charge planning", "petrol-versus-electric comparisons"],
 "Real mi/kWh drops in winter; use a cold-season figure or the answer flatters you. Charger losses stay on your meter at the wallbox, so expect about 10% more energy billed than stored.",
 "ev2",
 _f("ev2-b", "Battery size (kWh)", "75") + _f("ev2-c", "Current charge (%)", "20") + _f("ev2-t", "Target charge (%)", "80") +
 _f("ev2-p", "Electricity price per kWh", "0.15") + _f("ev2-e", "Efficiency (miles per kWh)", "3.5") +
 '''<button class="btn" onclick="ev2()">Cost the charge</button>
  <div id="ev2-out" class="result" aria-live="polite"></div>'''))

ADV12.append(("wind-chill-calculator", "Wind Chill Calculator", "Calculators",
 "The real-feel temperature when wind strips heat from exposed skin",
 "Thermometers read the air while your skin loses heat to whatever moves across it \u2014 that gap is wind chill, and it decides whether gloves and a hat are advisory or mandatory. Enter the air temperature and wind speed, and this calculator applies the official National Weather Service wind chill formula, translates both readings to Celsius and flags the frostbite-risk thresholds.",
 "WC = 35.74 + 0.6215T \u2212 35.75V^0.16 + 0.4275T\u00b7V^0.16 (T in \u00b0F, V in mph, valid T \u2264 50\u00b0F, V \u2265 3)",
 "air of 20\u00b0F with a 20 mph wind feels like 4\u00b0F; the same air at 5 mph only feels like 17\u00b0F",
 ["winter dog-walk and school-run checks", "running and cycling layering", "outdoor work safety briefings", "camping and mountain planning"],
 "Below about \u221219\u00b0F wind chill, exposed skin can freeze in 30 minutes. Unlike heat index, wind chill is purely convection.",
 "wi2",
 _f("wi2-t", "Air temperature (\u00b0F)", "20") + _f("wi2-v", "Wind speed (mph)", "20") +
 '''<button class="btn" onclick="wi2()">Compute wind chill</button>
  <div id="wi2-out" class="result" aria-live="polite"></div>'''))

ADV12.append(("heat-index-calculator", "Heat Index Calculator", "Calculators",
 "Temperature \u00d7 humidity into the real-feel heat stress number",
 "Humid heat is harder on the body than dry heat at the same reading, because sweat stops evaporating once the air is nearly saturated. Feed in the temperature and relative humidity, and this calculator applies the official National Weather Service heat-index equation, converts the result to Celsius and places you in the caution-to-extreme-danger risk band that heat-safety guidance actually uses.",
 "NWS HI = \u221242.379 + 2.049T + 10.143R \u2212 0.2248TR \u2212 0.00684T\u00b2 + \u2026 (T \u2265 80\u00b0F, R \u2265 40%)",
 "95\u00b0F at 60% humidity carries a heat index of 113\u00b0F \u2014 the danger band where heat illness becomes likely",
 ["heatwave coach and PE decisions", "construction site rest scheduling", "elderly and infant care checks", "outdoor event planning"],
 "The bands are medical, not decorative: 103\u00b0F or higher brings likely heat cramps and exhaustion without intervention. Direct sun adds up to 15\u00b0F on top of the standard shade-based figure.",
 "hi2",
 _f("hi2-t", "Air temperature (\u00b0F)", "95") + _f("hi2-r", "Relative humidity (%)", "60") +
 '''<button class="btn" onclick="hi2()">Compute heat index</button>
  <div id="hi2-out" class="result" aria-live="polite"></div>'''))

ADV12.append(("debt-payoff-planner", "Debt Payoff Planner", "Finance & Business",
 "Snowball versus avalanche across all your debts, month by month",
 "Paying the same total every month clears debt at very different speeds depending on the order the cards get the extra money. List each debt as balance, APR and minimum payment, choose avalanche or snowball, add any spare cash, and this planner simulates every month of the payoff, counts months and interest \u2014 and runs the rival strategy too so you can see exactly what the ordering is worth.",
 "each month: balance \u00d7 APR \u00f7 12 interest; minimums paid to all, the extra goes to the target debt",
 "5,000 at 20% plus 2,000 at 12% with 410 a month clears in 18 months \u2014 avalanche saves the snowball's extra interest",
 ["credit-card payoff plans", "loan consolidation decisions", "budget restarts after a windfall", "couples' finance goal-setting"],
 "Avalanche (highest APR first) is mathematically fastest; snowball (smallest balance first) wins on motivation. Keep paying the same total after one debt closes.",
 "dp2",
 '''<div><label for="dp2-l">Debts (one per line: balance, APR %, minimum payment)</label><textarea id="dp2-l" class="in" rows="4" placeholder="5000, 0.20, 150&#10;2000, 0.12, 60"></textarea></div>''' +
 _sel("dp2-s", "Strategy", [("avalanche", "Avalanche \u2014 highest APR first"), ("snowball", "Snowball \u2014 smallest balance first")]) + _f("dp2-x", "Extra per month", "100") +
 '''<button class="btn" onclick="dp2()">Simulate payoff</button>
  <div id="dp2-out" class="result" aria-live="polite"></div>'''))

ADV12.append(("anagram-checker", "Anagram Checker", "Text Tools",
 "Checks whether two words or phrases hide the same letters",
 "Anagrams hide one word inside another's letters, and eyes are badly calibrated to spot them \u2014 is \u201cthe eyes\u201d really \u201cthey see\u201d? Paste both words or phrases and this checker ignores case, spaces and punctuation the way anagram setters intend, compares the trimmed letter multisets exactly, and when they miss it names precisely which extra or missing letters break the match.",
 "sort each side's letters (a\u2013z, digits kept) and compare \u2014 equal multisets mean a true anagram",
 "\u201cListen\u201d and \u201cSilent\u201d match fully; \u201cListen\u201d vs \u201cSilents\u201d is told apart by exactly one stray s",
 ["scrabble and codeword setters", "party game night disputes", "pen-name and brand coinage", "cryptic crossword solving"],
 "A nineteenth-century habit survives because anagrams encode discovery: rearranged letters either answer a riddle or reveal a pseudonym.",
 "na2",
 '''<div><label for="na2-a">First word or phrase</label><input type="text" id="na2-a" class="in" value="Listen" autocomplete="off" /></div>''' +
 '''<div><label for="na2-b">Second word or phrase</label><input type="text" id="na2-b" class="in" value="Silent" autocomplete="off" /></div>''' +
 '''<button class="btn" onclick="na2()">Check anagram</button>
  <div id="na2-out" class="result" aria-live="polite"></div>'''))

ADV12.append(("tap-tempo", "Tap Tempo BPM Counter", "Calculators",
 "Tap along with the music and read the tempo in BPM",
 "Producers, DJs and dancers constantly meet the same question \u2014 how fast is this track actually? Tap the space bar in time with the beat and this counter averages the intervals of your most recent taps into a beats-per-minute figure, updates on every tap, and shows the per-beat duration and tap interval so you can match a metronome or plan a mix transition.",
 "BPM = 60,000 \u00f7 average interval in milliseconds across recent taps",
 "tapping with a 120 BPM track lands on 119\u2013121 live; the counter settles as taps accumulate",
 ["DJ beatmatching and transition planning", "metronome practice pacing", "dance choreography timing", "video edit beat-matching"],
 "Tap at least four or five beats before trusting the number \u2014 two intervals bounce with human timing. Half-time grooves read half the real tempo: double it if the counter keeps landing near 60.",
 "tp3",
 '''<button class="btn" onclick="tp3Tap()">Tap to the beat</button> <button type="button" class="btn ghost" onclick="tp3Reset()">Reset taps</button>
  <div id="tp3-out" class="result" aria-live="polite"></div>'''))

ADV12.append(("sleep-debt-calculator", "Sleep Debt Calculator", "Calculators",
 "The hours you owe your body after a week of short nights",
 "Sleep loss accumulates like interest on an overdraft: six as-good-enough nights quietly become ten hours owed by the weekend. Enter how long you actually slept each night and what you need, and this calculator totals the week's shortfall, averages your nights, names the best and worst, and converts the debt into a concrete recovery plan of catch-up nights.",
 "debt = nights \u00d7 needed hours \u2212 hours actually slept; recovery nights = debt \u00f7 extra hours per catch-up night",
 "sleeping 6, 6.5, 7, 5.5, 7, 6.5, 7.5 against an 8-hour need owes 10 hours \u2014 about 7 paid-back nights at +1.5 h",
 ["post-workweek recovery planning", "new-parent sleep budgeting", "shift-worker fatigue checks", "students' exam-week triage"],
 "Weekend lie-ins repay alertness but not fully; consistent 7\u20139 hours beats one heroic recovery night. If snoring or daytime fog persist with enough hours, screen properly for apnea.",
 "sd2",
 _f("sd2-n", "Hours you need per night", "8") + '''<div><label for="sd2-h">Hours slept each night (up to 7, comma-separated)</label><input type="text" id="sd2-h" class="in" value="8, 7.5, 7, 6, 7, 8, 9" autocomplete="off" /></div>''' +
 '''<button class="btn" onclick="sd2()">Compute sleep debt</button>
  <div id="sd2-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV12:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA12[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'''<div class="panel">{extra}{tail}</div>''',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT12[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
