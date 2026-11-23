# -*- coding: utf-8 -*-
"""Batch 19: eight more brand-new flagship tools, mega3/mega4 pattern."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA5 = {}
CONTENT5 = {}

ADV5 = []

SC2_KEYS = [
    ["AC", "\u232b", "(", ")", "^"],
    ["sin(", "cos(", "tan(", "ln(", "log("],
    ["7", "8", "9", "\u00f7", "\u221a("],
    ["AC2", "5", "6", "\u00d7", "%"],
    ["1", "2", "3", "\u2212", "+"],
    ["\u03c0", "e", "0", ".", ","],
]

ADV5.append(("scientific-calculator", "Scientific Calculator", "Calculators",
 "Full-expression trig, logs, powers and roots with precedence and history",
 "A phone calculator hides the functions you actually need, and typing expressions into search slips digits between searches. This scientific calculator evaluates a whole expression at once with correct precedence \u2014 so 2+3\u00d74^2 is written the way you would write it on paper \u2014 plus trigonometry in degrees or radians, logarithms, roots and constants, with a running history of your last results.",
 "standard operator precedence: parentheses, then powers, then multiplication and division, then addition and subtraction; trig functions honor the degrees/radians setting",
 "sin(30) + 2^8 evaluates to 256.5 in degrees mode, since sin 30\u00b0 = 0.5 and 2^8 = 256",
 ["physics and engineering coursework", "checking spreadsheet formulas", "finance and chemistry problem sets", "quick desk calculations with history"],
 "Degrees versus radians is the classic silent error: switch the angle unit before trusting any trig result, because both settings give plausible-looking numbers.",
 "sc2",
 '''<div class="row"><div><label for="sc2-d">Expression</label><input id="sc2-d" class="in" style="font-family:monospace" value="sin(30) + 2^8" autocomplete="off"></div><div><label for="sc2-m">Angle unit</label><select id="sc2-m"><option value="deg">Degrees</option><option value="rad">Radians</option></select></div></div>''' + '''<button class="btn" onclick="sc2()">Calculate</button>
  <div id="sc2-out" class="result" aria-live="polite"></div>
  <div class="uc-tablewrap" style="margin-top:10px"><div class="btnrow">''' + "".join(
        '<button type="button" class="ir2-preset" onclick="sc2K(\'' + k + '\')">' + k.replace("(", "") + "</button>"
        for row in SC2_KEYS for k in row) + '''</div></div>
  <div id="sc2-hist" class="jf-stats" style="margin-top:10px"></div>'''))

ADV5.append(("spinner-wheel", "Spin the Wheel", "Random Generators",
 "Animated random chooser wheel for any list, with winner history",
 "When a group cannot agree \u2014 where to eat, who presents first \u2014 a visible spin settles it better than a hidden draw, because everyone watches the same arrow decelerate together. This wheel takes any list, splits the circle fairly, animates a physical-feeling spin, announces the winner and keeps a session record of every outcome.",
 "a uniformly random spin angle selects one of N equal sectors, so every listed option has exactly the same chance regardless of name length",
 "with 5 evenly spaced options each slice covers 72\u00b0 of the circle, so every option wins one spin in five on average",
 ["deciding lunch with a team", "picking presenters in order", "giving kids a fair chooser", "breaking stalemate debates quickly"],
 "Duplicate entries double an option's odds \u2014 paste a list without repeats unless weighted probability on purpose is what you want.",
 "wh2",
 '''<div><label for="wh2-in">Options (one per line)</label><textarea id="wh2-in" rows="5" oninput="wh2()">Pizza&#10;Sushi&#10;Tacos&#10;Burgers&#10;Ramen</textarea></div>
  <div class="btnrow"><button class="btn" onclick="wh2Spin(this)">Spin the wheel</button><button class="btn ghost" onclick="wh2Copy(this)">Copy winner</button></div>
  <canvas id="wh2-canvas" width="360" height="360" class="chart" aria-label="Prize wheel"></canvas>
  <div id="wh2-out" class="result" aria-live="polite"></div>
  <div id="wh2-hist" class="jf-stats" style="margin-top:10px"></div>'''))

ADV5.append(("inflation-calculator", "Inflation Calculator", "Finance & Business",
 "Convert a sum forward or backward across years at any average rate",
 "Money quietly loses buying power: at 3% average inflation, a price doubles in about 24 years. Whether you are comparing a 1995 salary to today, deciding how much a future goal really costs, or checking an indexation clause in a contract, this calculator converts a sum across years at your chosen average rate \u2014 forward to project and backward to deflate \u2014 so figures from different eras finally speak the same language.",
 "nominal value = amount \u00d7 (1 + rate)^years going forward; real value = amount \u00f7 (1 + rate)^years deflating backward",
 "1,000 at 3% inflation for 10 years equals 1,343.92 of future buying power need \u2014 and a 1,000 sum from ten years ago is worth about 744 today",
 ["comparing salaries across decades", "sizing long-term savings goals", "checking rent and contract indexation", "teaching real vs. nominal value"],
 "The result is only as honest as the rate you feed it: long-run averages hide spikes, so run the calculation at two rates (pessimistic and likely) before committing to a number.",
 "if2",
 '''<div class="row">''' + _f("if2-m", "Amount", "1000") + _f("if2-r", "Average inflation (% per year)", "3") + _f("if2-y", "Years", "10") + _sel("if2-mo", "Direction", [("fwd", "Forward: today's money in N years"), ("bwd", "Backward: past money in today's terms")]) + '''</div>''' + '''<button class="btn" onclick="if2()">Calculate</button>
  <div id="if2-out" class="result" aria-live="polite"></div>'''))

ADV5.append(("z-score-calculator", "Z-Score Calculator", "Calculators",
 "Turn a raw score into a z-score and bell-curve percentile",
 "A raw score means little without context: scoring 85 is impressive in a class averaging 75 with wide spread, and ordinary in a class that averages 84. The z-score re-expresses any value in standard deviations from the mean, and the percentile tells you the share of a bell-curve population below it \u2014 the language admissions officers, test publishers and quality engineers actually use.",
 "z = (x \u2212 mean) \u00f7 sd; percentile = the fraction of a normal distribution below z, computed from the error-function approximation",
 "a score of 85 in a distribution with mean 75 and sd 10 gives z = 1.00, the 84th percentile \u2014 about 16% score higher",
 ["standardised test interpretation", "grading on a curve explanations", "quality control process limits", "comparing metrics with different units"],
 "Percentiles assume the data is roughly bell-shaped: an 84th percentile is meaningless for a heavily skewed distribution, so sanity-check the shape before quoting it.",
 "zs2",
 '''<div class="row">''' + _f("zs2-x", "Your value (x)", "85") + _f("zs2-mu", "Distribution mean", "75") + _f("zs2-sd", "Standard deviation", "10") + '''</div>''' + '''<button class="btn" onclick="zs2()">Compute z-score</button>
  <div id="zs2-out" class="result" aria-live="polite"></div>'''))

ADV5.append(("text-to-binary-converter", "Text to Binary Converter", "Developer Tools",
 "UTF-8 text to 8-bit binary groups and back, emoji-safe round trips",
 "Computers store every character as bytes, and seeing text as raw binary makes that tangible \u2014 handy for teaching, debugging protocols, building escapes for puzzle hunts or inspecting data. This converter encodes UTF-8 bytes to 0/1 groups and decodes them back, so emoji, accents and non-Latin scripts survive the round trip exactly, while plain ASCII stays one byte per character.",
 "each character \u2192 its UTF-8 bytes \u2192 each byte shown as an 8-bit group; decoding reads the groups back eight bits at a time",
 "\u201cSOS\u201d is 3 bytes \u2192 01010011 01001111 01010011 \u2014 exactly 24 bits, one group per character",
 ["teaching binary and encoding", "debugging byte-level protocols", "CS homework and practice", "puzzle hunts and escape rooms"],
 "Paste binary in groups of eight bits: partial groups cannot name a byte, and the tool tells you exactly which group is malformed instead of guessing.",
 "bn2",
 '''<div><label for="bn2-in">Text, or binary (groups of 8 bits)</label><textarea id="bn2-in" rows="4" oninput="bn2()" placeholder="Type text or paste 01001...">SOS</textarea></div>''' + _sel("bn2-m", "Direction", [("tobin", "Text \u2192 binary"), ("totext", "Binary \u2192 text")]) + '''<div class="btnrow"><button class="btn" onclick="bn2()">Convert</button><button class="btn ghost" onclick="bn2Swap()">Use result as input</button></div>
  <textarea id="bn2-out" rows="4" readonly></textarea>
  <div id="bn2-meta" class="jf-stats" style="margin-top:10px"></div>'''))

ADV5.append(("ideal-weight-calculator", "Ideal Weight Calculator", "Calculators",
 "Four classic formulas plus the healthy BMI range for your height",
 "There is no single ideal weight: the classic formulas (Devine, Robinson, Miller, Hamwi) were built for drug dosing and disagree by several kilograms. A more useful target is the range where population data shows lowest health risk. This calculator lists the classic estimates side by side and overlays the healthy BMI range for your height.",
 "Devine/Robinson/Miller/Hamwi add a fixed base (50 kg male, 45.5 kg female) plus kilograms per inch above five feet; healthy range = BMI 18.5\u201324.9 \u00d7 height\u00b2",
 "a 170 cm male gets Devine 65.9 kg, other formulas roughly 60\u201367 kg, and a healthy BMI band of about 53.5\u201372.0 kg",
 ["setting a realistic scale target", "medical dosing references", "fitness programme goal setting", "understanding what BMI means for you"],
 "Muscle mass moves these limits: athletes read the healthy range as a band, and a doctor's context beats any formula written decades ago.",
 "iw2",
 '''<div class="row">''' + _f("iw2-h", "Height (cm)", "170") + _sel("iw2-g", "Sex", [("m", "Male"), ("f", "Female")]) + '''</div>''' + '''<button class="btn" onclick="iw2()">Estimate ideal weight</button>
  <div id="iw2-out" class="result" aria-live="polite"></div>'''))

ADV5.append(("macro-calculator", "Macro Calculator", "Calculators",
 "Calorie target in and protein, carb and fat grams out, by goal",
 "Calories decide weight trend, but the protein\u2013carb\u2013fat split decides how those calories feel: satiety, gym recovery and blood-sugar stability all follow the macros, not the total. This calculator takes your daily calorie target, applies a proven split for your goal \u2014 balanced, high-protein or low-carb \u2014 and converts the percentages into grams you can actually weigh and track.",
 "grams = calories \u00d7 percentage \u00f7 energy density (protein and carbohydrate 4 kcal/g, fat 9 kcal/g)",
 "a 2,000 kcal day on the balanced split is 150 g protein, 200 g carbohydrate and 67 g fat",
 ["matching a calorie budget to a goal", "high-protein cutting phases", "endurance fuelling plans", "learning to read nutrition labels"],
 "The split percentages must use an energy density of 9 kcal/g for fat \u2014 mixing that up with 4 kcal/g roughly doubles your fat target in grams.",
 "mc2",
 '''<div class="row">''' + _f("mc2-c", "Daily calories", "2000") + _sel("mc2-g", "Split", [("bal", "Balanced (30/40/30)"), ("hp", "High protein (40/30/30)"), ("lc", "Low carb (40/20/40)")]) + '''</div>''' + '''<button class="btn" onclick="mc2()">Calculate macros</button>
  <div id="mc2-out" class="result" aria-live="polite"></div>'''))

ADV5.append(("reading-time-calculator", "Reading Time Calculator", "Text Tools",
 "Estimate reading time, speaking time and pages from any text",
 "Every blog you respect stamps a \u201c7 min read\u201d on its articles, and the number is just word count divided by a reading speed. For writers, timing your own drafts matters: a newsletter that overruns its slot, a talk script that ignores the pause budget, or documentation nobody finishes all trace back to unmeasured length. This tool estimates reading time at realistic speeds, includes speaking pace, and converts length into page equivalents.",
 "minutes = word count \u00f7 reading speed (words per minute); pages = words \u00f7 300 (typical printed page); speaking adds a slower 130 wpm channel",
 "600 words is 4 minutes at a 150 wpm study pace, 3 minutes at the common 200 wpm, and about 4.6 minutes spoken aloud",
 ["blog post and newsletter timing", "script and presentation pacing", "planning reading assignments", "estimating documentation effort"],
 "Reading speed is not one number \u2014 light fiction runs 250+ wpm while dense technical text drops near 150 \u2014 so trust the pace that matches your actual audience.",
 "rt2",
 '''<div><label for="rt2-in">Your text</label><textarea id="rt2-in" rows="5" oninput="rt2()" placeholder="Paste text to estimate reading time&hellip;">Paste a sample paragraph or two here to see the estimate&hellip;</textarea></div>''' + _sel("rt2-s", "Reading speed", [("150", "150 wpm \u2014 study pace"), ("200", "200 wpm \u2014 average adult"), ("250", "250 wpm \u2014 fast skim"), ("130", "130 wpm \u2014 spoken aloud")]) + '''<button class="btn" onclick="rt2()">Estimate reading time</button>
  <div id="rt2-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV5:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA5[slug] = {"name": name, "cat": cat, "short": short,
                   "body": f'''<div class="panel">{extra}{tail}</div>''',
                   "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT5[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
