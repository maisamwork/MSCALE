# -*- coding: utf-8 -*-
"""Batch 22: eight more brand-new flagship tools, mega3/4/5/6/7 pattern."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA8 = {}
CONTENT8 = {}

ADV8 = []

ADV8.append(("take-home-pay-calculator", "Take-Home Pay Calculator", "Finance & Business",
 "From gross salary to actual paycheck after deductions and tax",
 "A salary sticker number and the amount that lands in your bank can differ by a quarter. Enter gross pay, pre-tax deductions and a tax rate, and this calculator works the take-home amount out step by step: first what leaves for retirement, then the tax that applies to what remains, then the monthly and weekly cash you can actually plan around.",
 "pre-tax keeps its money; tax applies to gross minus pre-tax; net = gross \u2212 tax \u2212 pre-tax",
 "a 60,000 salary with 5% pre-tax and a 22% rate nets 44,460 \u2014 about 3,705 a month, an effective 25.9% off",
 ["job offer comparison", "budgeting around a raise", "checking payslip deductions", "self-employment rate setting"],
 "Taxes are almost always bracketed, so use your marginal rate only for top-up decisions and the effective average rate for full-salary estimates \u2014 this tool accepts either.",
 "th2",
 _f("th2-g", "Gross annual pay", "60000") + _f("th2-p", "Pre-tax deductions (% of gross)", "5") + _f("th2-t", "Tax rate (%)", "22") +
 '''<button class="btn" onclick="th2()">Calculate take-home</button>
  <div id="th2-out" class="result" aria-live="polite"></div>'''))

ADV8.append(("sample-size-calculator", "Sample Size Calculator", "SEO & Web Tools",
 "How many visitors or responses a test needs to be trusted",
 "Running a survey or an A/B test with too few people simply re-measures luck. Give this calculator the baseline conversion rate, the relative improvement you want to detect and your daily traffic, and it returns the exact number of visitors each variant needs \u2014 plus how many days the test will realistically take before the result means anything.",
 "n per variant = 7.84 \u00d7 2 \u00d7 p(1\u2212p) \u00f7 (p \u00d7 relative MDE)\u00b2 \u2014 the 80%-power, two-sided 95% confidence figure",
 "a 10% baseline detecting a 10% lift needs 14,112 per variant; at 5,000 visitors a day that is 5.6 days",
 ["A/B testing landing pages", "survey and poll design", "email marketing holdouts", "pricing and UX experiments"],
 "Stop the test early only when this sample size is met \u2014 peeking before then inflates false positives far more than most teams expect.",
 "ss2",
 _f("ss2-p", "Baseline conversion rate (%)", "10") + _f("ss2-m", "Minimum detectable lift (%)", "10") + _f("ss2-v", "Daily visitors / responses (both variants combined, optional)", "5000") +
 '''<button class="btn" onclick="ss2()">Calculate sample size</button>
  <div id="ss2-meta" class="jf-stats" aria-live="polite"></div>
  <div id="ss2-out" class="result" aria-live="polite"></div>'''))

ADV8.append(("split-test-significance-calculator", "Split Test Significance Calculator", "SEO & Web Tools",
 "Is variant B really winning, or is it noise? Z-test it",
 "A raising hand looks like victory until the maths quietly disagrees. Enter visitors and conversions for both variants and this calculator runs a two-proportion z-test: conversion rates, the z-score, the two-sided p-value and a plain verdict on whether B beats A at the 95% confidence level, with the relative lift stated alongside.",
 "z = (pB \u2212 pA) \u00f7 \u221a(p(1\u2212p)(1/nA + 1/nB)); significance when the two-sided p-value is under 0.05",
 "130 of 1,000 vs 100 of 1,000 gives z = 2.10, p \u2248 0.035 \u2014 significant, and a 30% relative lift",
 ["landing page experiments", "checkout flow tests", "ad creative comparisons", "teaching hypothesis testing"],
 "Significance is not importance \u2014 a 30% lift on a tiny baseline can be statistically certain while barely moving revenue, so read the lift chip next to the verdict.",
 "ab2",
 _f("ab2-va", "Variant A visitors", "1000") + _f("ab2-ca", "Variant A conversions", "100") +
 _f("ab2-vb", "Variant B visitors", "1000") + _f("ab2-cb", "Variant B conversions", "130") +
 '''<button class="btn" onclick="ab2()">Test significance</button>
  <div id="ab2-out" class="result" aria-live="polite"></div>'''))

ADV8.append(("pond-volume-calculator", "Pond Volume Calculator", "Calculators",
 "Litres, US gallons and surface area for rectangular or round ponds",
 "Dosing treatments, sizing pumps and choosing filters all start from one number nobody can eyeball: how much water the pond actually holds. Pick a rectangular or circular pond, enter its dimensions, and this calculator converts length \u00d7 width \u00d7 depth (or \u03c0r\u00b2 \u00d7 depth) into litres, US gallons and cubic metres, plus the surface area.",
 "rectangular: L \u00d7 W \u00d7 D \u00d7 28.3168 L; circular: \u03c0 \u00d7 (diameter/2)\u00b2 \u00d7 D \u00d7 28.3168; 1 ft\u00b3 = 7.48052 US gal",
 "a 10 by 5 by 2 ft rectangular pond holds about 2,832 L or 748 gallons across 50 ft\u00b2 of surface",
 ["medication and algaecide dosing", "pump and filter flow sizing", "fish stocking limits", "heater and aerator selection"],
 "Measure averages, not depths at the waterfall \u2014 and remember rock shelves displace real volume, so treated volume is often 10\u201315% below geometry.",
 "pv2",
 _sel("pv2-s", "Pond shape", [("rect", "Rectangular"), ("circ", "Circular")]) +
 _f("pv2-l", "Length or diameter (ft)", "10") + _f("pv2-w", "Width (rectangular only, ft)", "5") + _f("pv2-d", "Average depth (ft)", "2") +
 '''<button class="btn" onclick="pv2()">Calculate volume</button>
  <div id="pv2-out" class="result" aria-live="polite"></div>'''))

ADV8.append(("paint-coverage-calculator", "Paint Coverage Calculator", "Calculators",
 "Room paint volume in litres with doors, windows and coats factored in",
 "Buying paint is an exercise in lazy rounding \u2014 one can too few and the second coat stays imaginary. Enter the room dimensions, subtract doors and windows, choose coats and can size, and this calculator returns the paintable wall area, the litres required and how many cans to buy, so the store trip happens exactly once.",
 "wall area = 2 \u00d7 (L + W) \u00d7 H \u2212 doors/windows; paint = area \u00d7 coats \u00f7 coverage (m\u00b2 per litre); cans = litres \u00f7 can size, rounded up",
 "a 5 \u00d7 4 m room at 2.4 m height with one door and window paints 40.2 m\u00b2 \u2014 8.04 L for two coats, so three 4 L cans",
 ["repainting bedrooms and lounges", "rental-unit turnover work", "paint ordering for contractors", "comparing brand coverage claims"],
 "Rough or absorbent walls drink 20\u201330% more paint than the tin claims \u2014 for new plaster drop coverage to about 8 m\u00b2 per litre before buying.",
 "pt2",
 _f("pt2-l", "Room length (m)", "5") + _f("pt2-w", "Room width (m)", "4") + _f("pt2-h", "Wall height (m)", "2.4") +
 _f("pt2-d", "Doors", "1") + _f("pt2-n", "Windows", "1") + _f("pt2-c", "Coats", "2") +
 '''<button class="btn" onclick="pt2()">Calculate paint</button>
  <div id="pt2-out" class="result" aria-live="polite"></div>'''))

ADV8.append(("btu-calculator", "BTU Air Conditioner Calculator", "Calculators",
 "Right-size an air conditioner or heater for any room in BTU and kW",
 "An oversized unit cools fast and leaves a clammy room because it never runs long enough to dry the air; an undersized one just never stops. Enter room dimensions, how sunny it is, how many people share it and whether it contains a kitchen, and this calculator converts floor area into the BTU-per-hour target and its kW equivalent.",
 "BTU = floor area in ft\u00b2 \u00d7 20, \u00d7 1.1 if sunny or \u00d7 0.9 if shaded, + 600 per extra person, + 4,000 for kitchens",
 "a typical 4 \u00d7 5 m living room needs about 4,306 BTU (1.26 kW) before occupancy or sunlight adjustments",
 ["buying window and split units", "portable AC sizing", "heater capacity checks", "comparing kW specs to room needs"],
 "Both extremes waste money \u2014 size to the calculated BTU and, if the room gets morning-or-afternoon sun only, split the difference rather than rounding up.",
 "bt2",
 _f("bt2-l", "Room length (m)", "5") + _f("bt2-w", "Room width (m)", "4") +
 _sel("bt2-s", "Sunlight", [("avg", "Average"), ("sunny", "Very sunny (+10%)"), ("shade", "Shaded (\u221210%)")]) +
 _f("bt2-n", "People usually in the room", "2") + _sel("bt2-k", "Has a kitchen?", [("no", "No"), ("yes", "Yes (+4,000 BTU)")]) +
 '''<button class="btn" onclick="bt2()">Calculate BTU</button>
  <div id="bt2-out" class="result" aria-live="polite"></div>'''))

ADV8.append(("screen-time-calculator", "Screen Time Calculator", "Calculators",
 "Total the hours your day spends on screens \u2014 and those hours as years",
 "Phone, work computer, television and gaming hours feel small one evening at a time. Add a typical day's split and this calculator totals them into daily, weekly and yearly screen hours, shows the equivalent in round-the-clock days, and \u2014 with your age \u2014 converts the habit into waking years between now and age eighty.",
 "daily sum \u00d7 365 days/year; years = daily hours \u00d7 365 \u00d7 (80 \u2212 age) \u00f7 24 \u00f7 365",
 "three hours on the phone and two watching TV at age thirty is 1,825 screen hours a year \u2014 about 12.5 waking years before eighty",
 ["digital-wellbeing check-ins", "family screen rules", "new-year habit resets", "productivity time audits"],
 "The years figure assumes every screen hour is awake time \u2014 it is not a life-expectancy claim, just the honest scale of one daily habit.",
 "st2",
 _f("st2-p", "Phone (h/day)", "3") + _f("st2-c", "Computer or work (h/day)", "2") + _f("st2-t", "Television (h/day)", "1") + _f("st2-g", "Gaming or other (h/day)", "0") + _f("st2-a", "Current age (optional)", "30") +
 '''<button class="btn" onclick="st2()">Total screen time</button>
  <div id="st2-out" class="result" aria-live="polite"></div>'''))

ADV8.append(("voltage-drop-calculator", "Voltage Drop Calculator", "Calculators",
 "Check AWG wire sizing: volts lost, percentage and end-of-run voltage",
 "A long, thin cable can quietly starve an appliance a few volts below its rating. Choose gauge, material, load current, distance and system voltage, and this calculator applies the NEC constant method \u2014 volts dropped = 2 \u00d7 K \u00d7 I \u00d7 L \u00f7 circular mils \u2014 then reports the percentage loss and the voltage that actually arrives, with pass or flag verdicts.",
 "VD = 2 \u00d7 K \u00d7 I \u00d7 L \u00f7 CM (K = 12.9 copper, 21.2 aluminium); keep drops under 3%, investigate above 5%",
 "15 A over 50 ft of 12 AWG copper at 120 V loses 2.96 V \u2014 2.5%, leaving 117.04 V at the load",
 ["workshop extension cord checks", "12 V and RV circuit planning", "well-pump and long feeder runs", "verifying electrician quotes"],
 "Aluminium conducts worse \u2014 its higher 21.2 constant is built in \u2014 and always size on one-way distance, not the round trip.",
 "vd2",
 _f("vd2-i", "Load current (A)", "15") + _f("vd2-l", "One-way distance (ft)", "50") +
 _sel("vd2-g", "Wire gauge (AWG)", [("14", "14 AWG"), ("12", "12 AWG"), ("10", "10 AWG"), ("8", "8 AWG"), ("6", "6 AWG"), ("4", "4 AWG"), ("2", "2 AWG"), ("0", "1/0 AWG"), ("00", "2/0 AWG"), ("000", "3/0 AWG"), ("0000", "4/0 AWG")]) +
 _sel("vd2-m", "Material", [("cu", "Copper"), ("al", "Aluminium")]) + _sel("vd2-v", "System voltage", [("120", "120 V"), ("240", "240 V"), ("12", "12 V")]) +
 '''<button class="btn" onclick="vd2()">Calculate drop</button>
  <div id="vd2-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV8:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA8[slug] = {"name": name, "cat": cat, "short": short,
                   "body": f'''<div class="panel">{extra}{tail}</div>''',
                   "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT8[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
