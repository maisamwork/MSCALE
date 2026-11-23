# -*- coding: utf-8 -*-
"""Batch 23: eight more brand-new flagship tools, mega3-8 pattern."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA9 = {}
CONTENT9 = {}

ADV9 = []

ADV9.append(("calories-burned-calculator", "Calories Burned Calculator", "Calculators",
 "MET-based calorie burn for twenty-plus activities, scaled to you",
 "Exercise trackers disagree because burn depends on body mass, effort and time together. This calculator uses the standard Metabolic Equivalent (MET) table: pick an activity, enter your weight and duration, and it computes the calories with the published compendium formula, plus the burn rate per minute for quick hour-by-hour planning.",
 "kcal = MET \u00d7 3.5 \u00d7 weight(kg) \u00f7 200 \u00d7 minutes",
 "a 70 kg runner (9.8 MET) burns about 360 kcal in half an hour \u2014 roughly 12 kcal every minute",
 ["planning weight-loss deficits", "comparing workouts by effort", "post-training refuelling maths", "physiotherapy activity budgets"],
 "MET values assume steady moderate effort \u2014 intervals hit higher numbers and the same workout burns less as fitness grows.",
 "kc2",
 _sel("kc2-a", "Activity", [("1.3", "Sitting, desk work (1.3 MET)"), ("2.5", "Walking slowly (2.5 MET)"), ("3.5", "Walking 5 km/h (3.5 MET)"), ("4.3", "Table tennis (4.3 MET)"), ("5.0", "Brisk walking 6.5 km/h (5.0 MET)"), ("6.0", "Weight lifting, moderate (6.0 MET)"), ("6.5", "Dancing (6.5 MET)"), ("7.5", "Cycling 20 km/h (7.5 MET)"), ("8.0", "Swimming laps (8.0 MET)"), ("8.8", "Stair climbing (8.8 MET)"), ("9.8", "Running 10 km/h (9.8 MET)"), ("12.0", "HIIT or jump rope (12.0 MET)")]) +
 _f("kc2-w", "Body weight (kg)", "70") + _f("kc2-m", "Duration (minutes)", "30") +
 '''<button class="btn" onclick="kc2()">Calculate burn</button>
  <div id="kc2-out" class="result" aria-live="polite"></div>'''))

ADV9.append(("slope-grade-calculator", "Slope Grade Calculator", "Converters",
 "Rise over run as percentage, degrees and 1-in-N ratio at once",
 "Roads quote percent, builders quote ratios, roofers and wheelchair standards quote degrees \u2014 all describing the same ramp. Enter any rise and run (or reverse them to compute rise from a known grade) and this converter shows the percentage grade, the angle in degrees and the tidy 1-in-N ratio, with accessibility thresholds flagged.",
 "grade % = rise/run \u00d7 100; angle = arctan(rise/run); ratio = 1 : run/rise",
 "0.5 m rising over 10 m is a 5% grade, a 2.86\u00b0 angle, 1 : 20 \u2014 the classic accessible-ramp limit (1 : 12 is 8.3%)",
 ["driveway and ramp design", "ADA or building-code checks", "pipe fall and drainage runs", "cycling climb steepness"],
 "Percent and degrees are not interchangeable shorthand: a 10% grade is 5.7\u00b0, not 10\u00b0 \u2014 always convert before comparing specs.",
 "sg2",
 _f("sg2-r", "Rise", "0.5") + _f("sg2-n", "Run (same units)", "10") + _f("sg2-g", "Or compute rise from a grade (%) \u2014 leave above blank", "") +
 '''<button class="btn" onclick="sg2()">Convert slope</button>
  <div id="sg2-out" class="result" aria-live="polite"></div>'''))

ADV9.append(("split-bill-calculator", "Split Bill Calculator", "Finance & Business",
 "Divide the bill fairly with tip, tax and any group discount",
 "The end-of-dinner arithmetic is nobody's favourite party job \u2014 and rounding errors always land on one unlucky divide. Enter the bill, tip and headcount and this calculator splits to the cent: per-person share, tip money, grand total, and a rounded-up amount with the modest overage stated so the table can just drop notes in one plate.",
 "per person = total \u00d7 (1 + tip%) \u00f7 guests; rounded share uses Math.ceil to the next unit",
 "an 84.50 bill with an 18% tip across 4 people is 99.71 split into 24.93 each",
 ["restaurant group outings", "shared subscription renewals", "stag and hen party floats", "office lunch collections"],
 "Decide who tips on what before paying \u2014 applying 18% to a bill that already carries service double-charges the tip.",
 "sb2",
 _f("sb2-b", "Bill amount", "84.50") + _f("sb2-t", "Tip (%)", "18") + _f("sb2-p", "People", "4") +
 '''<button class="btn" onclick="sb2()">Split the bill</button>
  <div id="sb2-out" class="result" aria-live="polite"></div>'''))

ADV9.append(("overtime-pay-calculator", "Overtime Pay Calculator", "Finance & Business",
 "Tiered overtime: 1.5\u00d7 after your threshold, 2\u00d7 after sixty hours",
 "Hours past forty in most US jobs earn time-and-a-half, and many contracts add double time somewhere past sixty \u2014 two tiers that simple calculators ignore. Enter the rate, total hours and thresholds, and this calculator separates regular pay, time-and-a-half hours and double-time hours, showing each tier's money share and the weekly total.",
 "regular = rate \u00d7 min(h, T); 1.5\u00d7 on hours T\u202660; 2\u00d7 on hours above 60 by default (both configurable)",
 "20 an hour for 52 hours pays 800 regular plus 360 of overtime (12 h) = 1,160 for the week",
 ["payroll spot-checks", "hourly worker forecourt maths", "verifying payslip hour bands", "comparing job offers"],
 "Check your state: California counts daily hours over 8 as overtime regardless of the weekly total, and paid leave usually does not count toward the trigger.",
 "ov2",
 _f("ov2-r", "Hourly rate", "20") + _f("ov2-h", "Hours worked in the week", "52") + _f("ov2-t", "Overtime starts after (h)", "40") + _f("ov2-x", "Double time starts after (h)", "60") +
 '''<button class="btn" onclick="ov2()">Calculate overtime</button>
  <div id="ov2-out" class="result" aria-live="polite"></div>'''))

ADV9.append(("breakeven-calculator", "Break-Even Calculator", "Finance & Business",
 "Units, revenue and time to break even on any fixed cost",
 "Every business plan hides the same question: how many sales before the money coming in covers everything going out. Enter fixed costs (rent, salaries, tools), price per unit and variable cost per unit, and this calculator returns the break-even quantity, the revenue at that point, the margin each sale contributes and how many months of sales reach it.",
 "break-even units = fixed \u00f7 (price \u2212 variable); revenue = units \u00d7 price",
 "10,000 of fixed costs at a 10 margin breaks even at 1,000 units \u2014 25,000 of revenue at a 25 price",
 ["new product pricing", "startup budget pitches", "renting premises decisions", "campaign cost coverage"],
 "If price is at or below variable cost no amount of volume saves you \u2014 the tool flags that case rather than dividing by zero.",
 "be2",
 _f("be2-f", "Fixed costs", "10000") + _f("be2-p", "Price per unit", "25") + _f("be2-v", "Variable cost per unit", "15") + _f("be2-m", "Expected units sold per month (optional)", "80") +
 '''<button class="btn" onclick="be2()">Calculate break-even</button>
  <div id="be2-out" class="result" aria-live="polite"></div>'''))

ADV9.append(("square-footage-calculator", "Square Footage Calculator", "Calculators",
 "Room or whole-floor area with a materials budget in one step",
 "Flooring, paint, turf and renovation quotes all begin with an area figure \u2014 and \u2018about 12 by 10\u2019 hides a 30% swing depending on which room you actually measured. Enter footage precisely, add cost per square foot and a waste allowance, and this calculator returns exact area, the material cost at that coverage and the padded total buyers actually need.",
 "area = L \u00d7 W; cost = area \u00d7 unit price \u00d7 (1 + waste%)",
 "a 12 by 10 ft room is 120 ft\u00b2; at 2.50 per ft\u00b2 with 10% waste the order is 330.00",
 ["flooring and tile orders", "rent or lease pricing", "turf and decking estimates", "interior painting quotes"],
 "Measure the longest wall in the widest place for each dimension, then add waste \u2014 cutting layouts on tile and boards consumes the last 5\u201315% no matter how tidy.",
 "sf3",
 _f("sf3-l", "Length (ft)", "12") + _f("sf3-w", "Width (ft)", "10") + _f("sf3-c", "Cost per ft\u00b2 (optional)", "2.50") + _f("sf3-x", "Waste allowance (%)", "10") +
 '''<button class="btn" onclick="sf3()">Calculate area</button>
  <div id="sf3-out" class="result" aria-live="polite"></div>'''))

ADV9.append(("keyboard-test", "Keyboard Test", "Developer Tools",
 "Live key codes, event codes and a stuck-key detective for any keyboard",
 "Dead keys, ghosting and swapped layouts show up only when something presses them. Open this tester and touch every key: each keystroke is captured live with its key value, physical event code and key code number, the page tracks how many different keys your browser can see, and a scrollable history highlights repeat presses \u2014 no download, no driver, nothing stored.",
 "the page listens to keydown document-wide; display uses event.key, event.code and the legacy keyCode",
 "pressing Q shows key \u201cq\u201d, code \u201cKeyQ\u201d, keyCode 81 \u2014 arrow keys show ArrowUp and friends instead of letters",
 ["testing new or second-hand keyboards", "debugging key remapping tools", "game controller-mapping checks", "ghosting and n-key-rollover hunts"],
 "Modifier combos deliberately show the held modifier \u2014 press and hold Shift, then tap letters, to check whether your modifier reaches the application.",
 "kb2",
 '''''' +
 '''<div id="kb2-live" class="result" aria-live="polite" style="min-height:44px">Press any key \u2014 nothing is sent anywhere; detection is local.</div>
  <div id="kb2-meta" class="jf-stats" style="margin-top:10px"></div>
  <div id="kb2-log" class="result" style="min-height:80px; margin-top:10px; font-family:monospace; font-size:13px"></div>'''))

ADV9.append(("secret-santa-generator", "Secret Santa Generator", "Random Generators",
 "Cryptographically fair gift assignments with a perfect no-self cycle",
 "Drawing names from a hat risks a person pulling themselves \u2014 and fussing with re-draws spoils the secrecy. Paste the participant list, generate, and this tool shuffles with the browser's crypto source, then arranges the circle so every person gives once and receives once, nobody gives to themselves, and every name gets exactly one partner.",
 "Fisher\u2013Yates shuffle, then assignment giver i \u2192 giver (i+1) mod n: one clean cycle, no duplicates",
 "ann, ben, cara, dinesh might draw ann \u2192 cara \u2192 ben \u2192 dinesh \u2192 ann \u2014 regenerating makes a fresh fair circle every time",
 ["office Christmas gift swaps", "family cinema and friend groups", "classroom party exchanges", "online community gift events"],
 "Re-running before sharing changes all assignments \u2014 screen-share or copy the finished list once and keep it, since screenshots after re-rolls mix up old circles.",
 "sa2",
 '''<div><label for="sa2-in">Participants (one name per line)</label><textarea id="sa2-in" class="in" rows="5" placeholder="ann\nben\ncara\ndinesh"></textarea></div>''' +
 '''<button class="btn" onclick="sa2()">Draw Secret Santa</button>
  <div id="sa2-meta" class="jf-stats" aria-live="polite"></div>
  <div id="sa2-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV9:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA9[slug] = {"name": name, "cat": cat, "short": short,
                   "body": f'''<div class="panel">{extra}{tail}</div>''',
                   "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT9[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
