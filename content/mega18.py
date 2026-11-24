# -*- coding: utf-8 -*-
"""Batch 29 module C: 16 flagship tools (wellness, fitness, everyday value)."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA18 = {}
CONTENT18 = {}

ADV18 = []

ADV18.append(("commute-time-value", "Commute Time Value Calculator", "Finance & Business",
 "Price the hours a commute consumes at your real wage",
 "A commute bills you twice: in fuel or fares, and in the hours you cannot sell, spend or sleep. Enter your hourly worth, the daily commute hours and the working days a year, and this calculator answers the annual hours consumed, their earned value, and what each individual trip costs in time alone.",
 "annual hours = daily hours \u00d7 working days; time value = annual hours \u00d7 hourly wage",
 "two hours a day across 230 working days takes 460 hours \u2014 $11,500 of earned time at $25 an hour, $50 a round trip",
 ["job offer comparisons","remote-work trade-offs","housing location decisions","salary negotiation context"],
 "For hours you would otherwise spend working, value them at your gross rate; for leisure hours, judgment discounts them \u2014 but they are never free. A hybrid week that removes one commute day returns about $2,300 a year here.",
 "cv3",
 _f("cv3-w", "Hourly wage", "25") + _f("cv3-h", "Commute hours per day", "2") + _f("cv3-d", "Working days per year", "230") +
 '''<button class="btn" onclick="cv3()">Price the commute</button>
  <div id="cv3-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("cost-per-wear", "Cost Per Wear Calculator", "Calculators",
 "The real cost of any garment from price divided by wears",
 "Cost per wear is the only honest garment statistic, and it has quietly justified good purchases and condemned bad ones for decades. Enter what the item cost and how many times you will realistically wear it, and this calculator answers the per-wear price, reads it against the classic bands and shows how many extra wears cut it in half.",
 "cost per wear = price \u00f7 wears; bands: under $1 excellent, $1\u20133 fine, over $10 a decision to revisit",
 "a $200 coat worn across five winters at 40 wears a year costs $1 a wear \u2014 while the $40 shirt worn twice cost $20",
 ["wardrobe budgeting","before big fashion purchases","secondhand valuation","minimalist closet planning"],
 "The number depends entirely on honest wear counts \u2014 aspirational counts flatter impulse buys. Trend pieces lose the race by construction; durable basics compound downward every season they survive.",
 "cw2",
 _f("cw2-p", "Item price", "200") + _f("cw2-w", "Expected wears", "200") +
 '''<button class="btn" onclick="cw2()">Judge the wardrobe</button>
  <div id="cw2-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("calorie-deficit-planner", "Calorie Deficit Planner", "Calculators",
 "Weekly weight math from the gap between intake and burn",
 "Fat loss is an energy ledger, and the ledger has exactly three entries: how much you burn, how much you eat, and what the gap converts to. Enter your maintenance calories and your planned intake, and this planner answers the daily deficit, the weekly change in kilograms, and how many weeks a five-kilogram goal actually takes.",
 "daily deficit = TDEE \u2212 intake; weekly kg = deficit \u00d7 7 \u00f7 7,700; weeks to goal = 5 kg \u00f7 weekly kg",
 "burning 2,400 while eating 1,900 banks a 500-calorie deficit \u2014 0.45 kg a week, five kilograms in about eleven",
 ["cutting and bulking seasons","post-holiday resets","plateau diagnosis","nutrition coaching plans"],
 "Sustainable deficits sit near 20% of maintenance; doubling it mostly accelerates muscle loss and rebound hunger. As weight falls, TDEE falls with it \u2014 recheck the numbers every few kilograms.",
 "cd4",
 _f("cd4-t", "Maintenance calories (TDEE)", "2400") + _f("cd4-i", "Planned daily intake", "1900") +
 '''<button class="btn" onclick="cd4()">Plan the deficit</button>
  <div id="cd4-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("daily-water-needs", "Daily Water Needs Calculator", "Calculators",
 "Litres and bottle-counts from body weight and exercise",
 "The eight-glasses folklore survives because nobody price-checks it against body weight. Enter your weight and how many minutes you train, and this calculator answers the litres per day, the number of standard bottles, and how a hot day or an extra workout shifts the same arithmetic.",
 "litres = weight kg \u00d7 0.033 + 0.4 per 30 minutes of exercise; bottles = litres \u00f7 0.5",
 "a 70 kg adult training an hour needs about 3.11 litres \u2014 seven standard 500 ml bottles, one of them earned",
 ["training day planning","office hydration habits","illness recovery guidance","hot-climate travel"],
 "The 0.033-per-kilogram rule is a baseline for temperate weather \u2014 heat, altitude and fever all raise it, caffeine merely shifts timing. Food provides about a fifth of intake, so the bottles can overcount thirst by a glass.",
 "wg3",
 _f("wg3-w", "Body weight (kg)", "70") + _f("wg3-m", "Exercise minutes", "60") +
 '''<button class="btn" onclick="wg3()">Count the bottles</button>
  <div id="wg3-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("hydration-by-weight", "Hydration by Weight Calculator", "Calculators",
 "A personalized daily hydration target with a workout top-up",
 "Hydration targets scale with the body, and the body's weight is the scale everyone already carries. Enter your weight and activity level, and this calculator answers the baseline litres, the workout top-up, the total for the day and the per-hour sipping pace that turns a number into a habit.",
 "baseline = weight kg \u00d7 0.033; top-up = 0.4 L per 30 min activity; pace = total \u00f7 16 waking hours",
 "a 90 kg lifter training 45 minutes targets about 3.57 litres \u2014 a 220 ml glass every waking hour",
 ["strength training days","hot-weather work shifts","hydration schedule building","dietitian consultations"],
 "Thirst lags actual fluid loss in trained adults, which is why athletes drink to schedule, not to thirst. Clear-ish urine twice a day is the free cross-check on every formula here.",
 "hb2",
 _f("hb2-w", "Body weight (kg)", "90") + _f("hb2-m", "Activity minutes", "45") +
 '''<button class="btn" onclick="hb2()">Target the intake</button>
  <div id="hb2-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("bench-press-standards", "Bench Press Standards", "Calculators",
 "Where your one-rep max stands against bodyweight bands",
 "Strength is relative, and the bench press is where the relativity is argued most. Enter your bodyweight, the weight you press and the reps, and this calculator estimates the one-rep max with the Epley formula, then reads it against novice to advanced bodyweight ratios so the bar knows where you stand.",
 "1RM = weight \u00d7 (1 + reps \u00f7 30); bands: 0.75\u00d7 beginner, 1.0\u00d7 novice, 1.5\u00d7 intermediate, 2\u00d7 advanced",
 "135 pressed for 8 reps at a 90 kg bodyweight estimates a 171 kg max \u2014 1.9\u00d7 bodyweight, deep in the intermediate band with advanced at 2\u00d7",
 ["training program benchmarks","meet preparation","progress tracking","coach assessments"],
 "Epley overestimates as reps climb past ten \u2014 trust it under eight. Standards differ by sex and age, and the bands assume raw lifting without supportive gear.",
 "bx2",
 _f("bx2-b", "Bodyweight (kg)", "90") + _f("bx2-w", "Weight pressed (kg)", "135") + _f("bx2-r", "Reps completed", "8") +
 '''<button class="btn" onclick="bx2()">Grade the bench</button>
  <div id="bx2-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("pushup-test", "Pushup Test Grader", "Calculators",
 "Maximum pushups scored against population norms",
 "The pushup test is the cheapest fitness assessment in existence \u2014 a floor and a timer. Enter your maximum consecutive pushups and your age, and this grader answers the score, reads it against age-band norms, and shows what a realistic six-week gaining plan should add.",
 "bands: under 10 poor, 10\u201324 below average, 25\u201334 good, 35\u201344 very good, 45+ excellent for under-40 adults",
 "26 consecutive pushups at 35 years old lands in the good band \u2014 about six weeks of practice from very good",
 ["home fitness baselines","military and job readiness","steady progress checks","warm-up capacity screens"],
 "Form counts: a chest near the floor or the rep is theatre, and graders will say so. Numbers decline roughly a rep a year past forty \u2014 track the trend, not the single test day.",
 "pu2",
 _f("pu2-n", "Max consecutive pushups", "26") + _f("pu2-a", "Age", "35") +
 '''<button class="btn" onclick="pu2()">Grade the set</button>
  <div id="pu2-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("plank-grade", "Plank Hold Grader", "Calculators",
 "A timed plank scored against durability bands",
 "The plank measures core endurance in wall-clock seconds, which makes it the fastest honesty test in fitness. Enter your hold time and this grader answers the band \u2014 from shaky to elite \u2014 plus how many seconds the next band demands and what breathing rhythm usually buys you.",
 "grade by seconds: under 30 weak, 30\u201359 developing, 60\u201389 good, 90\u2013119 strong, 120+ elite",
 "a 67-second hold sits in the good band \u2014 23 seconds from strong, one training block away",
 ["core training baselines","posture program checks","pre-season screening","desk-worker assessments"],
 "Planks past two minutes stop buying extra health and start buying wrist pain \u2014 load harder variants instead. Sagging or piked hips end the clock before the stopwatch does; self-scores run optimistic.",
 "pt3",
 _f("pt3-s", "Plank hold (seconds)", "67") +
 '''<button class="btn" onclick="pt3()">Grade the plank</button>
  <div id="pt3-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("grip-strength", "Grip Strength Grader", "Calculators",
 "Handgrip dynamometer numbers read against bodyweight",
 "Grip strength is the quiet biomarker researchers keep finding in longevity studies, and a $20 dynamometer makes it measurable. Enter your measured grip in kilograms and your bodyweight, and this calculator answers the ratio, scores it against typical adult bands, and names the training that moves it.",
 "relative grip = grip kg \u00f7 bodyweight kg; bands: under 0.5 low, 0.5\u20130.7 adequate, above 0.7 strong",
 "44 kg of grip on an 80 kg frame is a 0.55 ratio \u2014 adequate territory, with stronger living clearly ahead",
 ["longevity health tracking","climbing and sport training","physiotherapy baselines","aging fitness screens"],
 "Dynamometer readings vary by body position \u2014 standing, elbow at 90 degrees, retest the same way every time. Grip responds fast to hangs and carries; two weekly sessions move it within a month.",
 "gs2",
 _f("gs2-g", "Grip reading (kg)", "44") + _f("gs2-b", "Bodyweight (kg)", "80") +
 '''<button class="btn" onclick="gs2()">Score the grip</button>
  <div id="gs2-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("vo2max-estimate", "VO2 Max Estimate", "Calculators",
 "Aerobic fitness from the 12-minute Cooper run, no lab needed",
 "The Cooper 12-minute test turned a lab measurement into a running track, and it still tracks VO2 max within a few points of gas analysis for most runners. Enter the distance covered in twelve minutes, and this calculator answers the estimated VO2 max, reads it against age-band fitness norms, and translates it into a 5K target.",
 "VO2max = (distance metres \u2212 504.9) \u00f7 44.73",
 "2,500 metres in twelve minutes estimates a 44.6 VO2 max \u2014 solidly average-to-good for a 35-year-old male runner",
 ["running program baselines","military and fire service fitness","race goal setting","progress retesting"],
 "Body lag or tailwind rewrites the score, so run the test on a track in calm conditions. Elite distance runners clear 70; improvements of 3 to 5 points a season are the honest ceiling at most ages.",
 "vo3",
 _f("vo3-d", "Distance in 12 minutes (m)", "2500") + _f("vo3-a", "Age", "35") +
 '''<button class="btn" onclick="vo3()">Grade the engine</button>
  <div id="vo3-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("mets-calculator", "METs Calculator", "Calculators",
 "Intensity in metabolic equivalents from calories and bodyweight",
 "METs are the currency every exercise chart trades in \u2014 three is moderate, six is vigorous \u2014 yet almost nobody computes their own. Enter calories burned, bodyweight and duration, and this calculator answers the METs, names the intensity band, and lists the equivalent activities at that level.",
 "METs = kcal \u00f7 (kg \u00d7 hours); bands: under 3 light, 3\u20136 moderate, over 6 vigorous",
 "600 kcal across 90 minutes at 70 kg is 5.7 METs \u2014 hard moderate work, the top of a fast cycle ride",
 ["workout log analysis","prescription exercise dosing","rehabilitation monitoring","activity tracker auditing"],
 "Tracker-reported calories often inflate 20\u201330%, which drops your METs as soon as you feed them in. Weekly guidance of 500 to 1,000 MET-minutes is the public-health floor the bands exist to check.",
 "me2",
 _f("me2-k", "Calories burned", "600") + _f("me2-w", "Bodyweight (kg)", "70") + _f("me2-h", "Duration (hours)", "1.5") +
 '''<button class="btn" onclick="me2()">Compute the METs</button>
  <div id="me2-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("steps-to-health", "Steps to Health Calculator", "Calculators",
 "Distance, calories and time value of any daily step count",
 "The step counter counts; this calculator translates. Enter your daily steps, bodyweight and stride, and it answers the distance walked, the calories it costs at your weight, the walking minutes it represents, and where the count sits against the research thresholds of 7,000 and 10,000 steps.",
 "distance = steps \u00d7 stride; kcal = steps \u00d7 weight kg \u00d7 0.00053; minutes = distance \u00f7 80 m per min",
 "10,000 steps at a 0.76 m stride cover 7.6 km \u2014 about 95 minutes of walking and 371 kcal for a 70 kg adult",
 ["daily activity goals","desk-job movement audits","weight-management tracking","step-count challenges"],
 "Strides shrink with fatigue and shoes \u2014 measure yours over ten known metres, not from a chart. Beyond the 10,000-step headline, the biggest mortality drop happens by 7,500; every step past 12,000 is gravy.",
 "se2",
 _f("se2-s", "Steps per day", "10000") + _f("se2-w", "Bodyweight (kg)", "70") + _f("se2-str", "Stride (m)", "0.76") +
 '''<button class="btn" onclick="se2()">Read the steps</button>
  <div id="se2-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("caffeine-half-life", "Caffeine Half-Life Calculator", "Calculators",
 "How much caffeine is still circulating \u2014 and when to cut off",
 "Caffeine leaves the body by half-life, roughly 5.7 hours, which is why the 2 p.m. espresso is a stealth bedtime decision. Enter the dose and the hours since, and this calculator answers the milligrams still active, how many cups that equals, and the latest cutoff that leaves you clean at lights-out.",
 "remaining = dose \u00d7 0.5^(hours \u00f7 5.7)",
 "200 mg at midday still has 46.5 mg circulating twelve hours later \u2014 over half a coffee's worth at midnight",
 ["afternoon coffee decisions","pre-workout timing","sleep-hygiene debugging","charting the 3 p.m. crash"],
 "Half-lives range from 3 to 7 hours across individuals \u2014 smokers clear it twice as fast, oral contraceptives double it. A working bedtime rule: treat any 40 mg-plus still active as a light left on.",
 "ch4",
 _f("ch4-d", "Caffeine dose (mg)", "200") + _f("ch4-h", "Hours since", "12") +
 '''<button class="btn" onclick="ch4()">Count the caffeine</button>
  <div id="ch4-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("iron-intake-checker", "Iron Intake Checker", "Calculators",
 "Your daily iron against the RDA with plant-based adjustment",
 "Iron is the micronutrient adults most quietly under-consume, and the requirement swings with sex and life stage. Pick your category and enter your daily intake, and this checker answers the recommended amount, the gap remaining, and the larger plant-based target that absorbed-iron math demands of non-haem sources.",
 "RDA: 8 mg adult men and post-menopausal women, 18 mg pre-menopausal; plant sources need \u00d71.8 allowance",
 "a pre-menopausal woman absorbing 11 mg from plant sources effectively banks 6.1 mg \u2014 two-thirds short of the 18 mg RDA",
 ["vegetarian and vegan diets","fatigue investigations","blood-donation recovery","prenatal planning"],
 "Haem iron from meat absorbs at 15\u201335%; plant non-haem at 2\u201320%, which is why the multiplier exists. Vitamin C at the same meal roughly doubles plant absorption \u2014 the cheapest upgrade on the list.",
 "ir3",
 _sel("ir3-s", "Category", [("m", "Adult man \u2014 RDA 8 mg"), ("f", "Pre-menopausal woman \u2014 18 mg"), ("p", "Post-menopausal \u2014 8 mg"), ("v", "Vegan woman \u2014 18 mg with 1.8\u00d7")]) + _f("ir3-i", "Daily intake (mg)", "11") +
 '''<button class="btn" onclick="ir3()">Check the iron</button>
  <div id="ir3-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("sugar-intake-checker", "Sugar Intake Checker", "Calculators",
 "Sugar in teaspoons scored against the heart-association limits",
 "Labels print sugar in grams; limits are discussed in teaspoons; the gap is where the day goes wrong by lunchtime. Enter the grams in your item and the servings it contains, and this checker converts to teaspoons, totals it against your daily allowance and prices a week of the same habit.",
 "tsp = grams \u00f7 4.2; limits: 36 g (9 tsp) men, 25 g (6 tsp) women per added-sugar day",
 "a 330 ml cola at 35 g is 8.3 teaspoons \u2014 140% of the women's limit and 97% of the men's, one can",
 ["soda and juice habits","breakfast cereal auditing","kids' snack decisions","label-reading practice"],
 "The limits cover added sugar only \u2014 sugar arriving inside fruit or milk comes with structure, fibre and fluid. Liquid sugar spikes fast and leaves hungrier, which is how one can moves the whole day.",
 "sg3",
 _f("sg3-g", "Sugar per serving (g)", "35") + _f("sg3-n", "Servings", "1") + _sel("sg3-s", "Limit basis", [("36", "Adult man \u2014 36 g"), ("25", "Adult woman \u2014 25 g"), ("20", "Child \u2014 20 g")]) +
 '''<button class="btn" onclick="sg3()">Count the sugar</button>
  <div id="sg3-out" class="result" aria-live="polite"></div>'''))

ADV18.append(("fiber-intake-checker", "Fiber Intake Checker", "Calculators",
 "Daily fibre against the 30-gram target with food equivalents",
 "Fibre is the nutrient every guideline begs for and every menu forgets; most adults sit near half the target. Enter today's fibre grams, and this checker answers the gap to 30, the per-meal share that would close it evenly, and the count of ordinary foods \u2014 apples, oats, beans \u2014 that make up the difference.",
 "target = 30 g/day; per meal = target \u00f7 3; equivalents: apple 4.4 g, oats 4 g per 40 g, beans 9 g per half cup",
 "14 g of fibre still needs 16 more \u2014 about four apples, or one serving of beans plus two slices of wholegrain away",
 ["digestive health plans","weight management","cholesterol-lowering diets","grocery list planning"],
 "Raise fibre gradually and hydrate \u2014 doubling it overnight announces itself loudly, and most of fibre's work is mechanical. Whole foods beat supplements on every outcome that matters.",
 "fi2",
 _f("fi2-g", "Fibre so far today (g)", "14") +
 '''<button class="btn" onclick="fi2()">Close the fibre gap</button>
  <div id="fi2-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV18:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA18[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'<div class="panel">{extra}{tail}</div>',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT18[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
