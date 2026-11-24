# -*- coding: utf-8 -*-
"""Batch 30 module C: 16 flagship tools (math, science, sport)."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA22 = {}
CONTENT22 = {}

ADV22 = []

ADV22.append(("decimal-to-fraction", "Decimal to Fraction Converter", "Calculators",
 "Any decimal restated as the simplest exact fraction",
 "Recipes, shims and scale drawings hand you decimals while the tape, the cup and the drafting rule speak fractions, and the two never meet politely. Enter a decimal and this converter walks the continued-fraction algorithm to the simplest fraction that owns the value, shows the nearest coarse fractions for real-world tools, and flags the ones that are only approximations.",
 "value = numerator / denominator reduced by gcd; continued fractions give the shortest exact chain",
 "0.375 converts to 3/8 exactly \u2014 and those three eighths are 9.53 mm of lathe or router reality",
 ["woodworking dimensions", "recipe scaling by hand", "machining drawings", "teaching rational numbers"],
 "Some decimals are liars: 0.333 from a rounded source is 1/3 nearby but not equal, so the tool states the closest short fraction instead of inventing false exactness. Denominators above 64 stop being practical for tape measures and recipe spoons alike.",
 "w37",
 _f("w37-a", "Decimal value", "0.375") +
 '''<button class="btn" onclick="w37()">Find the fraction</button>
  <div id="w37-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("percent-of-percent", "Percent of Percent Calculator", "Calculators",
 "A percentage multiplied by another percentage, the compounding corner of percentages",
 "A 20% step applied to something that is already 50% of its original self lands at 10% of the whole \u2014 and that is exactly where mental arithmetic falls over in shops, commissions and exam curves. Enter both percentages and this calculator multiplies them correctly, adds the add-versus-multiply trap, and rounds everything the way spreadsheets do.",
 "a% of b% = (a/100) \u00d7 (b/100) \u00d7 base = a \u00d7 b / 10000 of the base",
 "20% of the remaining 50% is 10% of the whole \u2014 not 70%, which is the classic additive mistake",
 ["rapid discount stacking", "commission on commission structures", "exam grade curves", "sequential tax and fee problems"],
 "Percentages of percentages are multiplicative, and the direction of the quote matters: a 50% rise then 50% fall returns to 75%, not zero, because the base moved. Convert to fractions when more than two steps stack \u2014 the mixed labels fall apart by step three.",
 "w38",
 _f("w38-a", "First percentage (%)", "20") + _f("w38-b", "Second percentage (%)", "50") +
 '''<button class="btn" onclick="w38()">Multiply the percents</button>
  <div id="w38-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("weighted-mean", "Weighted Mean Calculator", "Calculators",
 "A true weighted average for grades, portfolios and blended rates",
 "The plain average treats every value equally, which flatters expensive mistakes and underweights the positions that actually matter. Enter two value\u2013weight pairs \u2014 grades with credits, funds with sizes, regions with populations \u2014 and this calculator computes the weighted mean, shows each pair's share of the total weight, and compares it with the unweighted answer.",
 "weighted mean = (\u03a3 value \u00d7 weight) / \u03a3 weight",
 "an 85 weighted 3 and a 92 weighted 1 average 86.75 \u2014 not 88.5, because the heavier item pulls the centre",
 ["grade point calculations", "portfolio return blending", "customer satisfaction scores", "regional price indices"],
 "Weights should mean the same thing everywhere in one calculation \u2014 credits, dollars or headcount \u2014 and mixing them quietly corrupts the mean. If the weighted and plain averages disagree by more than a couple of points, some big-weight item is steering the number.",
 "w39",
 _f("w39-a", "Value 1", "85") + _f("w39-b", "Weight 1", "3") + _f("w39-c", "Value 2", "92") + _f("w39-d", "Weight 2", "1") +
 '''<button class="btn" onclick="w39()">Weight the average</button>
  <div id="w39-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("geometric-series-sum", "Geometric Series Sum Calculator", "Calculators",
 "The total of any doubling, halving or fixed-ratio chain",
 "Doubling payments, halving dosages, chain emails and pyramid pitches all follow the geometric series, and its total outruns every intuition. Enter the first term, the ratio and the number of terms, and this calculator totals the sum, prices the final term alone, and shows the per-step growth as a percentage so the leap step stops hiding.",
 "sum = a \u00d7 (r^n \u2212 1) / (r \u2212 1) for r \u2260 1; growth per step = (r \u2212 1) \u00d7 100%",
 "a series starting at 1 and doubling for 10 terms totals 1,023 \u2014 the tenth term alone carries 512, half the whole sum",
 ["salary doubling negotiations", "viral and network spread checks", "loan and annuity checkouts", "puzzle solving"],
 "The last term dominates whenever the ratio exceeds 1 \u2014 which is precisely why doubling wagers and chain promises both end in collapse or fortune with nothing in between. Inverse ratios below 1 converge instead: that is what mortgage amortization is banking on.",
 "w40",
 _f("w40-a", "First term", "1") + _f("w40-b", "Ratio (r)", "2") + _f("w40-c", "Number of terms", "10") +
 '''<button class="btn" onclick="w40()">Total the series</button>
  <div id="w40-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("permutation-combination", "Permutation and Combination Calculator", "Calculators",
 "Arrangements and selections computed both ways for the same numbers",
 "Lock codes, race podiums, committee seats and password rules all count order differently, and picking the wrong counter overstates armies of possibilities. Enter n and k, and this calculator answers arrangements (order matters), selections (order does not) and the ratio between them, with a plain-language note on which one your problem actually asks for.",
 "permutations = n! / (n \u2212 k)! ; combinations = n! / (k!(n \u2212 k)!)",
 "from 10 runners take 3: 720 podium orders but 120 plain teams \u2014 the sixfold gap is pure order sensitivity",
 ["password policy sizing", "committee and team selection", "race and ranking analysis", "probability homework"],
 "The factorial arithmetic overflows twenty digits fast, which is why the tool computes ratios without materialising factorials. If the problem says choose, group or committee, combinations; if it says rank, order or podium, permutations.",
 "w41",
 _f("w41-a", "Items (n)", "10") + _f("w41-b", "Chosen (k)", "3") +
 '''<button class="btn" onclick="w41()">Count both ways</button>
  <div id="w41-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("modular-arithmetic", "Modular Arithmetic Calculator", "Calculators",
 "Clock remainders: a mod m with wrap-around applications built in",
 "Clocks, pages of a book, hash buckets and encryption keys all run on remainders, and modular arithmetic is the grammar behind every wrap-around. Enter a and m, and this calculator answers a mod m with the quotient shown, prices it against a clock-face wrap, and adds the hash-bucket equivalent for developers who need the same thing on servers.",
 "a mod m = a \u2212 m \u00d7 floor(a / m); bucket = a mod buckets",
 "100 mod 7 is 2 \u2014 fourteen weeks and two days later, the weekly club meets on a Tuesday's neighbour",
 ["cyclic scheduling", "hash and bucket assignment", "cryptography basics", "check digit validation"],
 "Modular wraps keep only the remainder, which is exactly the point and exactly the trap: two very different numbers can share one residue, so buckets and cycles need collisions planned for. Negative inputs wrap differently in code and on paper \u2014 this tool follows the mathematical floor rule.",
 "w42",
 _f("w42-a", "a", "100") + _f("w42-b", "m (modulus)", "7") +
 '''<button class="btn" onclick="w42()">Take the remainder</button>
  <div id="w42-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("cube-of-a-number", "Cube of a Number Calculator", "Calculators",
 "x cubed computed exactly, with volume and scale comparisons",
 "Cubing is volume's home operation \u2014 boxes, tanks, dice and cumulative interest all multiply a length by itself three times and shock everyone at the rate the number climbs. Enter any value and this calculator computes the cube exactly, adds the cube-root companion, and compares the cube against the square to show how fast the third power outruns the second.",
 "x\u00b3 = x \u00d7 x \u00d7 x; volume of a cube with edge x",
 "12 cubed is 1,728 \u2014 while 12 squared is only 144, a twelve-fold leap from one extra multiplication",
 ["tank and box capacities", "dice game probabilities", "growth model checks", "cube root reverse checks"],
 "The cube's cruelty is scale: doubling an edge multiplies the volume eightfold, which is why big ships are cheap per tonne and city towers economics bend around materials. Negative numbers keep the operation's sign \u2014 cubes of negatives stay negative.",
 "w43",
 _f("w43-a", "Value (x)", "12") +
 '''<button class="btn" onclick="w43()">Cube it</button>
  <div id="w43-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("speed-of-sound", "Speed of Sound Calculator", "Calculators",
 "How fast sound travels at any air temperature, in every practical unit",
 "Thunder lags lightning and stadium chants echo late because sound needs about three seconds per kilometre \u2014 and the exact lag depends on air temperature. Enter the temperature, and this calculator computes the speed of sound from the standard gas formula in metres per second, km/h and mph, then converts it into the seconds-per-kilometre rule for storm counting.",
 "v = 331.3 \u00d7 \u221a(1 + T/273.15) m/s",
 "at 20\u00b0C sound travels 343 m/s \u2014 so thunder four seconds behind lightning marks a storm about 1.4 km away",
 ["storm distance estimating", "acoustics and venue setup", "physics homework", "aviation ground checks"],
 "The formula assumes dry air at sea level; humidity nudges the speed up slightly and altitude pulls it down. Every 10\u00b0C swing moves the answer by about 6 m/s \u2014 enough to matter for concert timing, relay races and anyone who counts storm seconds with a stopwatch instead of a chant.",
 "w44",
 _f("w44-a", "Air temperature (\u00b0C)", "20") +
 '''<button class="btn" onclick="w44()">Compute sound speed</button>
  <div id="w44-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("wake-up-cycle", "Wake Up Cycle Calculator", "Calculators",
 "Bed and rise times placed on 90-minute sleep cycles both ways",
 "Waking mid-cycle feels like a bug in the morning even after eight hours \u2014 sleep runs in roughly 90-minute cycles, and the difference between gifted and groggy often hides inside 15 minutes. Enter a bedtime, and this calculator lists the cycle-aligned rise options with the fall-asleep latency stated separately, so the alarm lands at a cycle boundary instead of mid-dream.",
 "rise = bedtime + latency + n \u00d7 90 minutes, for cycles n = 3 to 8",
 "asleep at 23:00 with six full cycles and 15 minutes of falling asleep lands a 08:15 rise \u2014 five cycles give 06:45, seven give 09:45",
 ["shift and early-start planning", "jet lag preparation", "exam week scheduling", "new-parent naps"],
 "The 90 minutes is a population average \u2014 individuals run 80 to 120, so track your own wake-ups for two weeks before trusting any schedule made of pure arithmetic. Falling asleep fast or slow shifts every option by that latency, which is the tool's honest limit.",
 "w45",
 _f("w45-a", "Bedtime hour (0\u201323)", "23") + _f("w45-b", "Bedtime minutes", "0") +
 '''<button class="btn" onclick="w45()">Find the cycles</button>
  <div id="w45-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("cycling-power-to-weight", "Cycling Power to Weight Calculator", "Calculators",
 "Functional threshold power normalized per kilogram and graded properly",
 "Cycling climbs are won per kilogram, not per watt, and the same rider is a hero uphill and a passenger on the flat for exactly this reason. Enter sustained power in watts and body weight, and this calculator computes watts per kilogram, grades it against recreational through pro-climber bands, and shows the advantage a few shed kilograms genuinely buy.",
 "W/kg = power / weight; graded against recreational through professional climbing bands",
 "250 watts from a 70 kg rider is 3.57 W/kg \u2014 solid enthusiast territory, and dropping 2 kg lifts it to 3.68 W/kg",
 ["climbing performance planning", "power meter users", "race category targets", "weight-loss payoff checks"],
 "W/kg describes climbing and FTP tests, not sprints \u2014 flat racing rewards absolute watts and technology. Test under fresh legs: fatigue fakes a 10% loss nobody can train out, and comparing grades across different test protocols is mostly self-flattery.",
 "w46",
 _f("w46-a", "Sustained power (watts)", "250") + _f("w46-b", "Rider weight (kg)", "70") +
 '''<button class="btn" onclick="w46()">Grade the power</button>
  <div id="w46-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("running-pace-band", "Running Pace Band Calculator", "Calculators",
 "A 5K result graded and turned into an explicit per-kilometre pacing band",
 "Race results in one direction read as vanity in the other, and an honest grading needs the per-kilometre arithmetic done for you. Enter a 5K time in minutes, and this calculator states the exact per-km pace, grades it across beginner to elite bands, and prints a pacing band that splits the race into goal splits with a negative-tilt finish.",
 "pace = time / 5 for a 5K; graded across experience bands; negative split opens slightly slow, closes fast",
 "a 25-minute 5K runs at 5:00 per km \u2014 solid recreational class, so band the race as 5:10 opening and 4:50 finish",
 ["race pacing plans", "parkrun improvement tracking", "coaching beginners", "treadmill equivalence checks"],
 "Bands assume a flat course and cool conditions; hills and heat re-price everything \u2014 add roughly 2% for each degree above 15\u00b0C. The negative-split layout exists because even splits feel great and fade splits feel like betrayal by kilometre four.",
 "w47",
 _f("w47-a", "5K time (minutes)", "25") +
 '''<button class="btn" onclick="w47()">Build the band</button>
  <div id="w47-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("golf-handicap", "Golf Handicap Calculator", "Calculators",
 "A handicap index estimated from a score, course rating and slope",
 "The handicap exists so a 95 and a 78 can play riveting golf on the same card, and the arithmetic uses course rating and slope to normalize them. Enter your adjusted score, the course rating and slope, and this calculator computes the score differential and approximates the official index, with the low-round discount the handicapping rules apply.",
 "differential = (score \u2212 course rating) \u00d7 113 / slope; index \u2248 differential \u00d7 0.96",
 "a 95 on a 72.4-rated, 125-slope course is a 20.43 differential \u2014 about a 19.6 index once the 0.96 discount lands",
 ["club competition entry", "friendly-match fairness", "holiday golf abroad", "progress tracking"],
 "Official indexes average the best 8 of your last 20 differentials \u2014 this single-round version is an estimate for casual matches, not a tournament card. Slope above 130 signals a course that punishes wayward driving, so price mulligans accordingly.",
 "w48",
 _f("w48-a", "Adjusted gross score", "95") + _f("w48-b", "Course rating", "72.4") + _f("w48-c", "Slope rating", "125") +
 '''<button class="btn" onclick="w48()">Compute the index</button>
  <div id="w48-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("recovery-heart-rate", "Recovery Heart Rate Calculator", "Calculators",
 "Heart-rate falloff after exercise graded against fitness benchmarks",
 "How fast your pulse falls in the first minute after hard effort is one of medicine's cheapest fitness tests \u2014 and it needs nothing but a watch and honesty. Enter the heart rate at the instant you stop and again a minute later, and this calculator states the drop and grades it against the 12-to-30 bpm research bands.",
 "recovery = heart rate at stop \u2212 heart rate after 1 minute; fitness scales with the size of the drop",
 "stopping at 140 and sitting at 120 a minute later is a 20 bpm drop \u2014 inside the healthy band, with room to improve",
 ["fitness progress checks", "overtraining detection", "cardio baseline testing", "return-to-exercise reviews"],
 "Recovery readings are cheap and repeatable \u2014 test weekly under the same conditions and the trend matters more than any single number. Under 12 bpm earns a doctor's conversation, not a harder block.",
 "w49",
 _f("w49-a", "Heart rate at stop (bpm)", "140") + _f("w49-b", "Heart rate after 1 minute", "120") +
 '''<button class="btn" onclick="w49()">Grade the recovery</button>
  <div id="w49-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("rowing-split-calculator", "Rowing Split Calculator", "Calculators",
 "A row time split into 500 m pace and watts, erg-honest",
 "Rowers think in 500-metre splits, coaches think in watts, and the cube-root relationship between them humbles everyone who guesses. Enter a total row time and distance, and this calculator states the per-500m split, converts it into watts using the erg's own constant, and prices small split improvements in watts so indoor targets stop being folklore.",
 "split = time / (distance / 500); watts = 2.8 / (split seconds / 500)\u00b3",
 "a 2,000 m row in 8:00 is a 2:00.0 split \u2014 about 202.5 watts for the whole piece",
 ["erg test preparation", "crew selection pieces", "CrossFit row benchmarks", "training zone setting"],
 "The watts formula is the standard erg constant of 2.8 \u2014 screen brands agree on it, open water does not. A 2K is mostly a breathless negotiation with the last 500; negative-splitting it costs seconds up front and repays them double at the end.",
 "w50",
 _f("w50-a", "Row time (minutes)", "8") + _f("w50-c", "Distance (m)", "2000") +
 '''<button class="btn" onclick="w50()">Split the piece</button>
  <div id="w50-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("swimming-pace", "Swimming Pace Calculator", "Calculators",
 "Pool splits and projections graded for swimmers in any lane",
 "Swim sessions repeat hundreds until the numbers mean something, and the meaningfulness lives in the pace-per-100 line nobody holds in their head. Enter a repeat time in seconds and the pool length, and this calculator states the per-100 metre pace, projects the 1,000 m session and a triathlon's 1,500 m leg, and grades the speed across lane-level bands.",
 "pace per 100 = time \u00d7 100 / pool length; projections scale linearly, fatigue honestly",
 "a 105-second hundred in a 25 m pool \u2014 four lengths \u2014 projects to 26:15 for the triathlon's 1,500 m leg",
 ["triathlon training paces", "lane etiquette and intervals", "open-water session planning", "fitness checks"],
 "Pool training assumes wall push-offs every length \u2014 open water removes them and usually adds 5% to 10% to the same athlete. Flip turns are free speed; breathing drills cost pace now and refund it on race day with interest.",
 "w51",
 _f("w51-a", "Repeat time (seconds)", "105") + _sel("w51-b", "Pool length", [("25", "25 m short course"), ("50", "50 m Olympic / long course")]) + _f("w51-c", "Project distance (m)", "1500") +
 '''<button class="btn" onclick="w51()">Set the pace</button>
  <div id="w51-out" class="result" aria-live="polite"></div>'''))

ADV22.append(("dog-chocolate-safety", "Dog Chocolate Safety Calculator", "Calculators",
 "Theobromine dose for a dog's weight, graded by chocolate type and severity",
 "Dogs and chocolate meet at parties, and the arithmetic that decides whether it is a vet visit is theobromine per kilogram of dog. Enter the dog's weight, the chocolate type and the grams eaten, and this calculator computes the dose, grades it across the watch, mild and emergency bands, and states what to do next in one honest sentence.",
 "dose = grams \u00d7 theobromine strength (mg/g) / body weight in kg",
 "50 g of dark chocolate eaten by a 15 kg dog delivers 18.3 mg/kg \u2014 into the watch band: restlessness and a call to the vet",
 ["emergency triage", "vet calls", "party prevention", "multi-dog households"],
 "Theobromine strengths vary by cocoa percentage, so err upward when in doubt and call the vet regardless \u2014 this tool never says you are safe, only where the dose sits. White chocolate is practically harmless chemically, but the packaging is still a blockage risk.",
 "w52",
 _f("w52-a", "Dog's weight (kg)", "15") + _sel("w52-b", "Chocolate type", [("5.5", "Dark chocolate"), ("2.2", "Milk chocolate"), ("20", "Cocoa powder / baking"), ("0.1", "White chocolate")]) + _f("w52-c", "Grams eaten", "50") +
 '''<button class="btn" onclick="w52()">Compute the dose</button>
  <div id="w52-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV22:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA22[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'<div class="panel">{extra}{tail}</div>',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT22[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
