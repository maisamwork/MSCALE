# -*- coding: utf-8 -*-
"""Batch 30 module B: 18 flagship tools (converters, number bases, odds)."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA21 = {}
CONTENT21 = {}

ADV21 = []

ADV21.append(("meters-to-yards", "Meters to Yards Converter", "Converters",
 "Metres into yards both ways, with feet and inches as a bonus",
 "Quilts, golf drives, Gaelic pitches and American fabric shops all measure in yards while the rest of the world draws metres. Enter either value and this converter answers both directions at once, adds feet-and-inches for tape measures, and keeps a fabric-swatch rounding note so cutting plans stay honest.",
 "yards = metres \u00d7 1.09361; metres = yards / 1.09361",
 "100 metres converts to 109.36 yards \u2014 and those 100 metres are also 328.08 feet if the tape is imperial",
 ["sewing and fabric buying", "golf and athletics distances", "Gaelic and gridiron pitches", "DIY project planning"],
 "The conversion constant is exact, but fabric cuts, landfill skips and course markers round \u2014 always round in the direction that leaves spare cloth or spare room, never the other way. For lawns and flooring, order 5% over the converted figure for offcuts.",
 "w19",
 _f("w19-a", "Metres", "100") +
 '''<button class="btn" onclick="w19()">Convert</button>
  <div id="w19-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("pints-to-liters", "Pints to Liters Converter", "Converters",
 "US pints into litres both directions, bottled-water maths included",
 "Recipes travel badly across the Atlantic because a pint means different things in different kitchens \u2014 the US pint is 473 ml while a bottle reads litres. Enter either value and this converter answers both directions, prices the difference against a standard bottle, and notes where the UK pint would land so imported recipes stop lying.",
 "litres = US pints \u00d7 0.473176; US pints = litres / 0.473176",
 "4 US pints convert to 1.89 litres \u2014 a 2-litre bottle holds 4.23 of them, so buy one bottle and open a small one",
 ["recipe conversion", "beer and cider measures", "freezer batch planning", "shop unit-price checks"],
 "One conversion per recipe is fine; chaining conversions compounds rounding until sauces and cement both behave oddly. Convert once into the units your tools use, then work there. And never trust a pint glass that has no crown or stamp \u2014 it may be short.",
 "w20",
 _f("w20-a", "US pints", "4") +
 '''<button class="btn" onclick="w20()">Convert</button>
  <div id="w20-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("imperial-pints-to-us-pints", "Imperial Pints to US Pints Converter", "Converters",
 "UK pints against US pints, with litres as the referee",
 "The pint controversy is real arithmetic: an imperial pint is 568 ml and a US pint is 473 ml, a 20% ambush waiting inside every pub crawl or imported recipe. Enter either pint type and this converter answers both pints and litres, so a hand-pulled ale or a US brew-kit recipe lands on the honest volume.",
 "US pints = imperial pints \u00d7 0.473176 / 0.568261 (\u2248 \u00d7 0.83267)",
 "4 imperial pints convert to 4.80 US pints \u2014 the UK pour is 20% bigger, about 380 ml extra across a round of four",
 ["pub measure checks", "imported recipe conversion", "brewing calculations", "bartender training"],
 "The gap repeats at every step of a recipe: four imperial cups, four US cups, and soon the batter has changed character. Convert the whole list once at the start. Beer and milk in the UK are legally sealed measures; coffee, not so much.",
 "w21",
 _f("w21-a", "Imperial pints", "4") +
 '''<button class="btn" onclick="w21()">Convert</button>
  <div id="w21-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("watts-to-horsepower", "Watts to Horsepower Converter", "Converters",
 "Electrical power into mechanical horsepower with amps included",
 "Generators are sold in watts, motors in horsepower, and heart-rate equivalents in none of the above \u2014 so shoppers compare labels that never meet. Enter watts or horsepower and this converter answers both directions, adds the current draw at common voltages, and places human, machine and grid scales side by side for honest comparisons.",
 "horsepower = watts / 745.7; amps = watts / volts",
 "1,500 watts converts to 2.01 hp \u2014 on a 120 V circuit that same load draws 12.5 amps, which decides the extension lead",
 ["generator and inverter sizing", "motor swaps and upgrades", "EV spec reading", "circuit load planning"],
 "Mechanical and metric horsepower differ slightly, and marketing bolts the flattering one onto spec sheets; this tool uses the mechanical definition. Motors also draw a surge on start \u2014 size circuits for peak, not nameplate, or breakers will educate you.",
 "w22",
 _f("w22-a", "Watts", "1500") + _sel("w22-b", "Circuit voltage", [("120", "120 V (US)"), ("230", "230 V (EU/UK)")]) +
 '''<button class="btn" onclick="w22()">Convert power</button>
  <div id="w22-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("bar-to-psi", "Bar to PSI Converter", "Converters",
 "Pressure units for tires, compressors and dive computers",
 "Tyre pressure is printed in bar in Europe and psi in America, compressors dial one or the other, and an off-by-tenth prints unevenly across a tread. Enter bar or psi and this converter answers both directions with kPa for dashboards, and grades the reading against typical tyre guidance bands.",
 "psi = bar \u00d7 14.5038; kPa = bar \u00d7 100",
 "2.2 bar converts to 31.9 psi \u2014 the door sticker's 32 psi is the same pressure wearing another badge",
 ["tyre pressure setting", "compressor tool setup", "diving gauge reading", "bike pump calibrations"],
 "Cold readings matter: pressures rise roughly a tenth of a bar as tyres warm, so set them before driving far. Under-inflation quietly eats fuel and shoulders of tread long before a flat announces the mistake.",
 "w23",
 _f("w23-a", "Pressure in bar", "2.2") +
 '''<button class="btn" onclick="w23()">Convert pressure</button>
  <div id="w23-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("knots-to-mph", "Knots to MPH Converter", "Converters",
 "Nautical knots into miles per hour with Beaufort context",
 "Wind forecasts, shipping lanes and flight plans live in knots while road signs and car speedometers live in mph, so every waterside day trips over the gap. Enter knots or mph and this converter answers both directions plus metres per second, and places the wind on the Beaufort scale with plain-language effects.",
 "mph = knots \u00d7 1.15078; m/s = knots \u00d7 0.51444",
 "20 knots converts to 23.02 mph \u2014 a fresh breeze by Beaufort where umbrellas stop cooperating",
 ["sailing and boating", "weather forecast reading", "ferry timing checks", "drone and kite safety"],
 "A knot is one nautical mile per hour \u2014 strictly, one minute of latitude \u2014 which is why aviation and shipping never dropped it: the maths of charts stays honest. Between 25 and 33 knots winds start renaming themselves rather than just blowing.",
 "w24",
 _f("w24-a", "Speed in knots", "20") +
 '''<button class="btn" onclick="w24()">Convert speed</button>
  <div id="w24-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("liters-per-100km-to-mpg", "Liters per 100km to MPG Converter", "Converters",
 "Fuel consumption flipped between European and American scales",
 "Europe measures fuel per distance and America measures distance per fuel, which is why one side reads downwards as good and the other upwards \u2014 and cross-shopping cars means doing the inverted sums in your head. Enter a figure in either system, and this converter answers US mpg, UK mpg and L/100km all at once with a typical-tank range line.",
 "US mpg = 235.215 / (L/100km); UK mpg = 282.481 / (L/100km)",
 "8 L/100 km converts to 29.40 US mpg \u2014 and 35.31 mpg(UK), because the imperial gallon is bigger",
 ["imported car shopping", "fleet policy writing", "road-trip budgeting", "efficiency upgrades"],
 "The inverted scale means savings are nonlinear: going 12 to 10 L/100 km saves less fuel than 6 to 5, which argues for fixing the thirstiest vehicle first. Ranges use a 50-litre tank for the rounding.",
 "w25",
 _f("w25-a", "Consumption (L/100 km)", "8") +
 '''<button class="btn" onclick="w25()">Convert consumption</button>
  <div id="w25-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("square-feet-to-square-meters", "Square Feet to Square Meters Converter", "Converters",
 "Floor areas compared across listing languages and floor plans",
 "Property is advertised in square feet in some markets and square metres in others, and the same flat can shrink in print purely by unit. Enter either area and this converter answers both directions, prices the space per unit area if a price is entered, and adds the ten-square-foot comfort rule for furniture planning.",
 "m\u00b2 = ft\u00b2 / 10.7639; ft\u00b2 = m\u00b2 \u00d7 10.7639",
 "850 sq ft converts to 78.97 m\u00b2 \u2014 the same one-bed flat by two vocabularies, at $300 per sq ft or $3,229 per m\u00b2",
 ["property listing checks", "rental comparisons", "office space planning", "flooring quotations"],
 "Developers count differently \u2014 usable area, gross area and the space rented to walls \u2014 so identical numbers can differ by a tenth of the flat. When comparing listings, use the smaller of the two quoted figures for both, or your shortlist is fiction.",
 "w26",
 _f("w26-a", "Area (square feet)", "850") + _f("w26-b", "Price (optional, total)", "255000") +
 '''<button class="btn" onclick="w26()">Convert area</button>
  <div id="w26-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("cubic-feet-to-cubic-meters", "Cubic Feet to Cubic Meters Converter", "Converters",
 "Van loads, fridges and freezers compared across volume units",
 "Moving quotes in cubic metres meet fridge specs in cubic feet and exporter manifests invent a third language entirely. Enter either volume and this converter answers both directions, prices the volume against a big product's shipping carton, and adds a washing-machine-bucket for scale.",
 "m\u00b3 = ft\u00b3 / 35.3147; ft\u00b3 = m\u00b3 \u00d7 35.3147",
 "40 cu ft converts to 1.13 m\u00b3 \u2014 about the chest freezer's 14-cu-ft box three times over",
 ["moving van sizing", "appliance purchase checks", "storage rental comparison", "shipping quotes"],
 "Volume lies about shape: a 40-cu-ft non-rectangular carton may not take what a 40-cu-ft cube does, so plan loads around doorways and handles. For movers, weight limits matter more than volume once libraries and dumbbells join the manifest.",
 "w27",
 _f("w27-a", "Volume (cubic feet)", "40") +
 '''<button class="btn" onclick="w27()">Convert volume</button>
  <div id="w27-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("minutes-to-days", "Minutes to Days Converter", "Converters",
 "Long durations flipped between minutes, days and weeks",
 "Binge logs, outages and sabbaticals arrive in minutes while schedules plan in days, and the mental division by 1,440 loses whole afternoons. Enter minutes and this converter answers days, weeks and hours at once, adds a work-day equivalent at 8 hours, and keeps the arithmetic exact so no rounding sells you a shorter outage.",
 "days = minutes / 1,440; weeks = minutes / 10,080",
 "5,000 minutes converts to 3.47 days \u2014 over three full days, or 10.4 eight-hour workdays if only the day job counts",
 ["outage and downtime reports", "parental leave planning", "media-hours tracking", "project timers"],
 "Counting sleep or not doubles many answers, so be explicit about which clock you mean \u2014 screen-time bans and internships use different ones. For service credits, round in the customer's favour; for deadlines, round the other way.",
 "w28",
 _f("w28-a", "Minutes", "5000") +
 '''<button class="btn" onclick="w28()">Convert minutes</button>
  <div id="w28-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("weeks-to-months", "Weeks to Months Converter", "Converters",
 "Project timelines flipped between weeks and calendar months",
 "Contracts run in weeks, invoices in months, and the mismatch quietly misprices both sides of every freelance engagement. Enter weeks and this converter answers the calendar-month equivalent across three conventions \u2014 flat 4-week, average 4.348-week and working-month at 4.33 \u2014 so terms stop shifting meaning between documents.",
 "months = weeks / 4.34812 (12 months = 52.1775 weeks)",
 "20 weeks converts to 4.6 average months \u2014 the flat-4 habit would call it 5, and payroll always believes the bigger one",
 ["contract length setting", "pregnancy tracking", "project plan conversions", "rent and lease maths"],
 "Say which convention you used when quoting; flat-4 favours the buyer, average favours the seller, and the gap across a year is 11 whole weeks. For pregnancy counts, weeks and lunar months agree only through week 40 by convention.",
 "w29",
 _f("w29-a", "Weeks", "20") +
 '''<button class="btn" onclick="w29()">Convert weeks</button>
  <div id="w29-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("seconds-to-days", "Seconds to Days Converter", "Converters",
 "Uptime, compile times and big counts made human in days",
 "Uptime claims, render farms and step counters speak seconds the way weather services speak pascals \u2014 correct and unusable. Enter seconds and this converter answers days, hours and minutes with a workday equivalent, plus the classic million-seconds-is-days fact family for teaching.",
 "days = seconds / 86,400",
 "250,000 seconds converts to 2.89 days \u2014 just under three full days, or 8.7 eight-hour workdays if only shifts count",
 ["uptime and SLA reports", "render and job timers", "teaching time scales", "milestone celebrations"],
 "SLA maths favors saying nine-and-six nines in seconds but billing in hours \u2014 always convert before comparing contracts. And a million seconds is under 12 days while a billion is 31.7 years, which is the fastest way to explain data breaches to anyone.",
 "w30",
 _f("w30-a", "Seconds", "250000") +
 '''<button class="btn" onclick="w30()">Convert seconds</button>
  <div id="w30-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("binary-to-hex", "Binary to Hex Converter", "Converters",
 "Binary into hex and decimal with per-nibble grouping for readability",
 "Binary is what machines read, hex is what humans skim, decimal is what invoices say \u2014 and byte-level debugging lives exactly where the three meet. Enter a binary string and this converter validates each digit, prints hex and decimal, and groups the binary into nibbles so truncation errors surface before they become bugs.",
 "hex groups binary in nibbles: 11010110 \u2192 D6 0110 1010; decimal = \u03a3 bit \u00d7 2^position",
 "11010110 reads 214 decimal and D6 hex \u2014 one byte wearing two alphabets, nibble by nibble 1101|0110",
 ["byte-level debugging", "colour code reading", "exam practice", "embedded systems work"],
 "Hex exists because 16 is a power of two: every 4 binary digits collapse into exactly one hex digit without guesswork, which decimal can never promise. Leading zeros change nothing here \u2014 but they matter when widths are fixed.",
 "w31",
 _f("w31-a", "Binary string (1s and 0s)", "11010110") +
 '''<button class="btn" onclick="w31()">Convert binary</button>
  <div id="w31-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("octal-to-decimal", "Octal to Decimal Converter", "Converters",
 "Unix permissions and octal into decimal, hex and plain English",
 "Octal survived the digital age almost entirely inside Unix file permissions, which is alone reason enough to be fluent. Enter an octal number \u2014 like 755 \u2014 and this converter answers decimal and hex, spells the permission string in plain English, and flags invalid digits so a typo never silently becomes a security hole.",
 "decimal = \u03a3 digit \u00d7 8^position; permissions digit = owner\u00d7100 + group\u00d710 + other",
 "755 octal is 493 decimal and 1ED hex \u2014 the classic rwxr-xr-x: owner full, group and others read-and-run",
 ["chmod and permissions", "legacy system migration", "exam practice", "embedded firmware"],
 "A 644 written where 464 was intended looks identical in decimal, which is why permission mistakes are self-camouflaging \u2014 always speak triads aloud. The 8^position structure is why octal digits never contain 8 or 9; if one appears, the number was decimal all along.",
 "w32",
 _f("w32-a", "Octal number", "755") +
 '''<button class="btn" onclick="w32()">Convert octal</button>
  <div id="w32-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("roman-numeral-date", "Roman Numeral Date Converter", "Converters",
 "Any date engraved as Roman numerals, tattoo-grade accuracy included",
 "Wedding invitations, cornerstones, championship rings and tattoos all reach for Roman numerals, and everyone's favourite mistake is writing 4 as IIII. Enter a date and this converter renders day, month and year in full Roman form with classical subtractive notation, plus a validation line for numerals typed back in.",
 "value = \u03a3 symbols with subtractive pairs IV, IX, XL, XC, CD, CM applied",
 "14 July 1789 becomes XIV \u00b7 VII \u00b7 MDCCLXXXIX \u2014 and those numerals read straight back as 14, 7, 1789",
 ["wedding and tattoo dates", "cornerstone readings", "film production credits", "monarch and pope numbering"],
 "True classical engravers did write IIII on clock faces, so a family heirloom is not automatically a typo \u2014 but a tattoo should follow subtractive notation. Validators cry visually: MDCCLXXXIX is long, which is why empires stopped dating things this way.",
 "w33",
 _f("w33-a", "Day (1\u201331)", "14") + _sel("w33-b", "Month", [("1", "I \u2014 January"), ("2", "II \u2014 February"), ("3", "III \u2014 March"), ("7", "VII \u2014 July"), ("12", "XII \u2014 December")]).replace('value="7"', 'value="7" selected') + _f("w33-c", "Year", "1789") +
 '''<button class="btn" onclick="w33()">Engrave the date</button>
  <div id="w33-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("hex-color-to-rgba", "Hex to RGBA Converter", "Converters",
 "Hex colours opened up into rgb() and rgba() with alpha control",
 "Hex speaks to designers, rgba() speaks to CSS motion and overlays \u2014 and translucency is where the two dialects shake hands. Enter a hex colour and an alpha value, and this converter prints rgba() and its 8-digit hex cousin, shows the swatch on white, and warns when alpha crosses the readability line against plain backgrounds.",
 "rgba(r, g, b, a); 8-digit hex appends alpha: #3b82f6 + 0.6 \u2192 #3b82f699",
 "#3b82f6 at 60% alpha becomes rgba(59, 130, 246, 0.6) \u2014 and #3b82f699 in the 8-digit form",
 ["CSS overlay and glass effects", "design-token setup", "hover state tuning", "brand palette exports"],
 "Alpha is linear gamma in the modern web only \u2014 screen rendering and print proofing disagree, so always check overlays at both the darkest and lightest content behind them. Below roughly 0.4 alpha, small grey-on-white text starts failing accessibility quickly.",
 "w34",
 _f("w34-a", "Hex colour", "3b82f6", "#3b82f6") + _f("w34-b", "Alpha (0\u20131)", "0.6") +
 '''<button class="btn" onclick="w34()">Convert colour</button>
  <div id="w34-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("lottery-odds", "Lottery Odds Calculator", "Converters",
 "Jackpot and lower-tier odds computed honestly for any lottery",
 "Lottery odds are combinatorics with confetti, and most players quote numbers off the wrong ticket entirely. Enter the pool size, the numbers drawn and a lower tier to check, and this calculator computes the jackpot probability exactly, prices the lower-tier match, and puts the odds into games-played language nobody can argue with.",
 "jackpot ways = n! / (k!(n \u2212 k)!); tier odds = C(k, m) \u00d7 C(n \u2212 k, k \u2212 m) / C(n, k)",
 "a 6-of-49 draw lists C(49,6) = 13,983,816 combinations \u2014 matching three lands 1 in 56.7, and the jackpot 1 in 13.98 million",
 ["syndicate fairness maths", "lottery strategy checks", "probability teaching", "scratch-card comparisons"],
 "Every draw is independent, so last week's numbers carry no debt \u2014 and a system that raises bet sizes after losses only changes the variance, not the edge. The house margin on lotteries is among the steepest in any legal game; play it as entertainment pricing.",
 "w35",
 _f("w35-a", "Pool size (n)", "49") + _f("w35-b", "Numbers drawn (k)", "6") + _f("w35-c", "Match count for lower tier", "3") +
 '''<button class="btn" onclick="w35()">Compute the odds</button>
  <div id="w35-out" class="result" aria-live="polite"></div>'''))

ADV21.append(("expected-value", "Expected Value Calculator", "Converters",
 "The long-run average of any bet, offer or gamble, stated per play",
 "Expected value is the quiet Number behind insurance premiums, raffles, cashback offers and casino floors, and it decides who is buying and who is being bought. Enter a win probability, the prize and the cost per play, and this calculator states the expected value per play, the net position and the plays it takes for the house to collect reliably.",
 "EV = probability \u00d7 prize \u2212 cost; net per play = EV",
 "a 1% shot at $500 costs $10 a play and is worth $5 \u2014 an expected loss of $5 every time, costing $500 across 100 plays",
 ["raffle and sweepstakes checks", "cashback and bonus offers", "insurance product pricing", "game design balance"],
 "Positive EV needs the probability and prize read honestly \u2014 headline prizes overstate both. Variance, not EV, decides short-run joy: a $5 expected loss can still pay tonight, but the hundredth play is where the arithmetic always arrives on schedule.",
 "w36",
 _f("w36-a", "Win probability (%)", "1") + _f("w36-b", "Prize amount", "500") + _f("w36-c", "Cost per play", "10") +
 '''<button class="btn" onclick="w36()">Find the edge</button>
  <div id="w36-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV21:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA21[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'<div class="panel">{extra}{tail}</div>',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT21[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
