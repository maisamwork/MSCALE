# -*- coding: utf-8 -*-
"""Batch 21: eight more brand-new flagship tools, mega3/4/5/6 pattern."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA7 = {}
CONTENT7 = {}

ADV7 = []

ADV7.append(("commission-calculator", "Commission Calculator", "Finance & Business",
 "Split sales commissions, house cuts and agent shares from any deal",
 "Commission agreements are easier to check than to read. This calculator takes the deal value, the commission rate and the optional house split, then shows the gross commission, the amount that stays with the house and the amount the seller or agent actually banks, with yearly projections if the deal repeats \u2014 all at once, no spreadsheet.",
 "commission = sale \u00d7 rate% ; agent share = commission \u00d7 you% ; house keeps the rest",
 "a 250,000 sale at 3% makes 7,500 commission; with a 30% house split the agent banks 5,250 and the house 2,250",
 ["real-estate sales and referrals", "car dealership pay plans", "freelance finder's fees", "checking a split offer before signing"],
 "House splits are negotiable per deal \u2014 always read whether the rate applies to the full sale price before taxes and closing costs.",
 "cm2",
 _f("cm2-s", "Sale price", "250000") + _f("cm2-r", "Commission rate (%)", "3") + _f("cm2-y", "Your share of the commission (%) \u2014 leave blank if it is all yours", "70") +
 '''<button class="btn" onclick="cm2()">Calculate commission</button>
  <div id="cm2-out" class="result" aria-live="polite"></div>'''))

ADV7.append(("meeting-cost-calculator", "Meeting Cost Calculator", "Finance & Business",
 "Put a real money figure on every meeting you schedule",
 "A one-hour meeting with five salaried people is rarely free \u2014 it is their hourly cost multiplied across the room, every time it runs. This calculator converts headcount, durations and pay into cost per meeting, per week and per year, and shows the total person-hours consumed, so trimming the calendar becomes a visible saving instead of a feeling.",
 "cost = people \u00d7 hourly rate \u00d7 hours ; annual = per-meeting \u00d7 meetings per week \u00d7 46 working weeks",
 "six people at 45 an hour for 60 minutes costs 270 per run; weekly at 3 meetings that is 37,260 a year",
 ["justifying shorter stand-ups", "pricing client workshops", "academia and consultancy time budgeting", "deciding who really needs the invite"],
 "Use fully-loaded wages (salary plus overhead) rather than raw hourlies, and remember recurring meetings multiply \u2014 forty-six working weeks compounds fast.",
 "mg2",
 _f("mg2-n", "People attending", "6") + _f("mg2-r", "Average hourly cost per person", "45") + _f("mg2-d", "Meeting length (minutes)", "60") + _f("mg2-w", "How many times per week", "3") +
 '''<button class="btn" onclick="mg2()">Cost the meeting</button>
  <div id="mg2-out" class="result" aria-live="polite"></div>'''))

ADV7.append(("angle-converter", "Angle Converter", "Converters",
 "Convert degrees to radians, gradians, turns, arcminutes and arcseconds",
 "Angle units come from three different traditions \u2014 geometry uses radians, surveying uses gradians, navigation splits degrees into arcminutes and arcseconds, and programmers speak in turns or fractions of a circle. Enter a value in any one of them and this converter answers in all of them at once, exactly, with the \u03c0-radians form spelled out.",
 "radians = degrees \u00d7 \u03c0/180 ; gradians \u00d7 0.9 ; turns \u00f7 360 ; arcminutes \u00d7 60 ; arcseconds \u00d7 3600",
 "90\u00b0 is \u03c0/2 radians, 100 gon, 0.25 turns and 324,000 arcseconds \u2014 all five chips update from one input",
 ["trigonometry and physics homework", "CAD, CNC and surveying drawings", "navigation and astronomy calculations", "stylesheet or shader rotations"],
 "Most confusion comes from mixing degrees and radians inside one formula \u2014 convert first, compute second, and let the chips confirm which unit you actually typed.",
 "an2",
 _f("an2-v", "Angle value", "90") + _sel("an2-u", "Input unit", [("deg", "Degrees"), ("rad", "Radians"), ("gon", "Gradians (gon)"), ("turn", "Turns (fractions of a circle)"), ("amin", "Arcminutes (\u2032)"), ("asec", "Arcseconds (\u2033)")]) +
 '''<button class="btn" onclick="an2()">Convert angle</button>
  <div id="an2-out" class="result" aria-live="polite"></div>'''))

ADV7.append(("fuel-economy-converter", "Fuel Economy Converter", "Converters",
 "Compare mpg US, mpg UK, L/100 km and km/L at once",
 "Two cars can both quote 40 \u2014 one means US miles per gallon, the other kilometres per litre. Fuel figures also split into \u2018higher is better\u2019 (mpg, km/L) and \u2018lower is better\u2019 (L/100 km) systems, so this converter answers in all four units simultaneously using the exact imperial gallon definitions.",
 "1 mpg US = 0.425144 km/L = 235.215/L/100 km ; 1 UK gallon = 4.54609 L ; 1 mile = 1.60934 km",
 "40 mpg US is 6.72 L/100 km; 40 mpg UK is only 7.06 \u2014 the UK gallon is bigger, so UK mpg always reads higher",
 ["importing cars across the Atlantic", "comparing manufacturer claims", "fleet and expense reporting", "trailering and towing range maths"],
 "Watch the gallon: US sites quote 231-cubic-inch gallons, UK sources 4.546 litres \u2014 never mix the two when judging consumption figures.",
 "fe2",
 _f("fe2-v", "Fuel economy value", "40") + _sel("fe2-u", "Input unit", [("us", "mpg (US)"), ("uk", "mpg (UK, imperial)"), ("l100", "L/100 km"), ("kml", "km/L")]) +
 '''<button class="btn" onclick="fe2()">Convert fuel economy</button>
  <div id="fe2-out" class="result" aria-live="polite"></div>'''))

ADV7.append(("flesch-reading-level", "Flesch Reading Level Checker", "Text Tools",
 "Score any text for readability with Flesch Reading Ease and grade level",
 "Plain language is measured, not guessed. Paste an article, policy page or school text and this checker counts sentences, words and syllables, then returns the Flesch Reading Ease score, the Flesch\u2013Kincaid grade level and a plain-language verdict \u2014 so you can see whether the writing suits a grade-schooler, a busy professional or a specialist audience.",
 "reading ease = 206.835 \u2212 1.015 \u00d7 (words/sentences) \u2212 84.6 \u00d7 (syllables/words); grade = 0.39 \u00d7 (w/s) + 11.8 \u00d7 (syl/w) \u2212 15.59",
 "60\u201370 reads like everyday magazine prose; below 50 needs a college-level reader and a rewrite",
 ["editing web copy for skimmers", "plain-language compliance and legal text", "matching school reading lists", "team style-guide checks"],
 "Long is not the same as hard \u2014 sentence length drives the first term, syllable load the second, so shortening sentences usually lifts the score more than swapping every long word.",
 "fl2",
 '''<div><label for="fl2-in">Text to score</label><textarea id="fl2-in" class="in" rows="6" placeholder="Paste paragraphs here \u2014 sentences, words and syllables are counted live."></textarea></div>''' +
 '''<button class="btn" onclick="fl2()">Score readability</button>
  <div id="fl2-out" class="result" aria-live="polite"></div>'''))

ADV7.append(("random-decimal-generator", "Random Decimal Generator", "Random Generators",
 "Cryptographically random decimals in any range with live min/mean stats",
 "Quick dice-like decimals with a fixed number of digits are awkward to make by hand and biased when made with ordinary random functions. This generator draws numbers uniformly across any range using the browser's cryptographic source, rounds to your chosen precision and reports the smallest, largest and mean draw so you can sanity-check the spread.",
 "uniform draw = min + (max \u2212 min) \u00d7 (crypto integer / 2\u00b3\u00b2), rounded to the requested decimals",
 "5 draws between 1 and 10 at 2 decimals lands for example 7.31, 1.02, 9.88 \u2014 mean near 5.5 over many runs proves fairness",
 ["science fair sampling", " allocating share of wallet or survey quotas", "Monte Carlo style games", "test fixtures that need believable decimals"],
 "The crypto source is far stronger than Math.random, and every output is stated to your exact decimal count \u2014 including trailing zeros you can copy straight into sheets.",
 "rd2",
 _f("rd2-min", "Minimum (inclusive)", "0") + _f("rd2-max", "Maximum (exclusive)", "10") + _f("rd2-d", "Decimal places (0\u20138)", "2") + _f("rd2-c", "How many numbers", "10") +
 '''<button class="btn" onclick="rd2()">Generate decimals</button>
  <div id="rd2-meta" class="jf-stats" aria-live="polite"></div>
  <div id="rd2-out" class="result" aria-live="polite"></div>'''))

ADV7.append(("recipe-scaler", "Recipe Scaler", "Calculators",
 "Scale ingredient lines up or down when servings change",
 "Half or double a recipe and the maths gets annoying exactly where precision matters \u2014 three-quarters of a cup, two-thirds of a tablespoon. Paste your ingredient lines, tell it the original and desired servings, and this scaler multiplies every leading amount by the exact ratio, neatening the result into clean fractions with 8ths at worst.",
 "scaled amount = amount \u00d7 (desired servings \u00f7 original servings); results snap to the nearest 1/8 and reduce to lowest terms",
 "scaling 4 serves to 6 turns \u201c2 1/2 cups flour\u201d into \u201c3 3/4 cups flour\u201d and \u201c1 tsp salt\u201d into \u201c1 1/2 tsp salt\u201d",
 ["batch cooking and meal prep", "halving recipes for two", "doubling party bakes", "converting family recipes to portions"],
 "Spices and salt scale non-linearly \u2014 scale them to about three-quarters of the calculated amount, adjust to taste, and keep cook times unchanged even when quantities change.",
 "rc2",
 _f("rc2-o", "Original servings", "4") + _f("rc2-n", "Desired servings", "6") +
 '''<div><label for="rc2-in">Ingredient lines (amount first, e.g. \u201c2 1/2 cups flour\u201d)</label><textarea id="rc2-in" class="in" rows="5" placeholder="2 1/2 cups flour\n1 tsp salt\n3 tbsp olive oil"></textarea></div>''' +
 '''<button class="btn" onclick="rc2()">Scale recipe</button>
  <div id="rc2-meta" class="jf-stats" aria-live="polite"></div>
  <div id="rc2-out" class="result" aria-live="polite"></div>'''))

ADV7.append(("dilution-calculator", "Dilution Calculator", "Calculators",
 "Solve C1V1=C2V2 for whichever concentration or volume is missing",
 "Every dilution in a lab, a kitchen or a pool shed obeys one short law: concentration \u00d7 volume is conserved. Fill in any three of C\u2081, V\u2081, C\u2082 and V\u2082 and this calculator solves the fourth exactly for you, then adds the dilution factor and how much solvent to add \u2014 all the working shown, so the numbers can go straight onto a worksheet.",
 "C\u2081V\u2081 = C\u2082V\u2082 ; factor = V\u2082/V\u2081 ; solvent to add = V\u2082 \u2212 V\u2081",
 "1 ml of 10 M stock diluted to 100 ml gives 0.1 M with a 100\u00d7 factor \u2014 add 99 ml of solvent",
 ["lab stock solutions and titrations", "cleaning-product and pool chemicals", "food brines and cordials", "teaching molarity basics"],
 "Volumes must share one unit \u2014 mixing millilitres with litres silently shifts answers a thousandfold, so convert first and let the factor chip confirm the scale.",
 "dl2",
 _sel("dl2-s", "Solve for", [("v1", "V\u2081 \u2014 volume of stock"), ("v2", "V\u2082 \u2014 final volume"), ("c1", "C\u2081 \u2014 stock concentration"), ("c2", "C\u2082 \u2014 target concentration")]) +
 _f("dl2-c1", "C\u2081 concentration", "10") + _f("dl2-v1", "V\u2081 volume", "1") + _f("dl2-c2", "C\u2082 concentration", "0.1") + _f("dl2-v2", "V\u2082 volume", "100") +
 '''<button class="btn" onclick="dl2()">Solve dilution</button>
  <div id="dl2-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV7:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA7[slug] = {"name": name, "cat": cat, "short": short,
                   "body": f'''<div class="panel">{extra}{tail}</div>''',
                   "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT7[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
