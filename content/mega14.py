# -*- coding: utf-8 -*-
"""Batch 28 module A: 10 finance + 12 calculator flagship tools, mega3-13 pattern."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA14 = {}
CONTENT14 = {}

ADV14 = []

ADV14.append(("apy-calculator", "APY Calculator", "Finance & Business",
 "Convert an annual percentage rate into the true yearly yield with compounding",
 "Two accounts can both advertise 6% and pay different money. The annual percentage yield folds compounding into one comparable figure, so savings history stops being guesswork. Enter a rate and how often it compounds, and this calculator converts both directions: rate into APY for fair comparisons, or a target yield back into the rate it needs.",
 "APY = (1 + r/n)^n \u2212 1, with r the nominal rate and n the compounding periods per year",
 "a nominal 6% compounded monthly is a real 6.17% \u2014 over 30 years that gap compounds into 4.7% more money",
 ["comparing savings and CD accounts honestly","credit-card cost awareness","bond and money-market analysis","spotting advertised-rate fine print"],
 "Compounding frequency matters more than the headline: 12% monthly is 12.68%, not 12%. Available rates quote the nominal figure, so always run both directions before moving money.",
 "ay2",
 _f("ay2-r", "Nominal rate (APR, % per year)", "6") + _sel("ay2-n", "Compounding", [("12", "Monthly"), ("365", "Daily"), ("4", "Quarterly"), ("1", "Annually"), ("2", "Semi-annually")]) + _sel("ay2-d", "Direction", [("a", "Rate \u2192 APY"), ("b", "APY \u2192 Rate")]) +
 '''<button class="btn" onclick="ay2()">Convert</button>
  <div id="ay2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("savings-goal", "Savings Goal Calculator", "Finance & Business",
 "Monthly deposit needed to hit any target by a chosen date",
 "Vague goals stay vague because nobody converts them into a monthly number. Enter what you want saved, what is already set aside, the interest the pot earns and the deadline, and this calculator works back from the compound future value of your savings to the deposit that closes the exact gap.",
 "monthly = (goal \u2212 saved\u00d7(1+r/n)^(n\u00b7years)) \u00f7 [((1+r/n)^(n\u00b7years) \u2212 1) \u00f7 (r/n)]",
 "50,000 target, 10,000 already banked at 4% for 5 years needs 570 a month \u2014 not the 667 interest ignores would suggest",
 ["house deposits and down payments","emergency-fund buildouts","wedding and travel budgets","retirement catch-up planning"],
 "Interest works for you while you save: the existing balance grows on its own, so the gap shrinks before your first deposit. Skip months and the ending number punishes you compounding-wise.",
 "vg2",
 _f("vg2-g", "Goal amount", "50000") + _f("vg2-s", "Already saved", "10000") + _f("vg2-r", "Annual interest (%)", "4") + _f("vg2-y", "Years to reach goal", "5") +
 '''<button class="btn" onclick="vg2()">Solve the deposit</button>
  <div id="vg2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("credit-card-interest", "Credit Card Interest Calculator", "Finance & Business",
 "Months and dollars to clear a card balance at your real payment size",
 "Minimum payments are engineered to feel affordable and cost years. This simulator runs your actual card month by month: interest accrues on the daily-equivalent rate, the payment lands, the balance shrinks. Enter what you owe, the APR and either a fixed payment or the minimum, and see the true payoff date, total interest and what paying 20% more saves.",
 "balance\u2099 = balance\u2099\u208b\u2081\u00d7(1 + APR/12) \u2212 payment, iterated until zero; interest = sum of monthly accruals",
 "5,000 owed at 20% APR with 200 paid monthly clears in 33 months for 1,522 in interest \u2014 pay 250 and it drops to 24 months",
 ["digging out of card balances","deciding on balance transfers","budgeting payoff buffers","debate-testing larger payment sizes"],
 "Paying the 2% minimum on a fresh balance can stretch decades; a fixed payment that never shrinks is the escape hatch. Interest compounds monthly here, matching most issuer disclosure terms.",
 "ci3",
 _f("ci3-b", "Card balance", "5000") + _f("ci3-a", "APR (%)", "20") + _f("ci3-p", "Monthly payment", "200") +
 '''<button class="btn" onclick="ci3()">Simulate payoff</button>
  <div id="ci3-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("rent-affordability", "Rent Affordability Calculator", "Finance & Business",
 "The monthly rent your income honestly supports before lifestyle creep",
 "The landlady rule of thumb \u2014 rent under 30% of gross income \u2014 still guards against the usual spiral: a place that fits the salary but starves savings. Enter your gross pay and a strictness level, and this calculator returns the maximum rent, what that leaves for living, and the paired-income version for shared leases.",
 "max rent = gross income \u00d7 rule% \u00f7 12; leftovers = income \u2212 12\u00d7rent, split by month",
 "60,000 gross at the classic 30% rule supports 1,500 a month \u2014 the 40x rule landlords apply puts the same flat near 125,000 income",
 ["apartment hunting budget lines","flatmate and co-lease splits","moving-city salary negotiation","avoiding lifestyle creep after raises"],
 "Gross rules flatter renters: taxes take a fifth before rent is due, so try the 25% setting after a raise reaches your payslip. landlords often screen on annual income at 40\u00d7 monthly rent.",
 "ra3",
 _f("ra3-i", "Gross annual income", "60000") + _sel("ra3-r", "Budget rule", [("30", "30% \u2014 classic"), ("25", "25% \u2014 stringent saver"), ("35", "35% \u2014 high-cost city"), ("20", "20% \u2014 aggressive saver")]) +
 '''<button class="btn" onclick="ra3()">Cap my rent</button>
  <div id="ra3-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("investment-fee-impact", "Investment Fee Impact Calculator", "Finance & Business",
 "What a 1% management fee quietly deletes from your future wealth",
 "Fees never appear on a statement as a line item; they shave the compounding rate year after year. Enter your balance, expected return, the fee percentage and years invested, and this calculator compounds the same portfolio twice \u2014 once gross, once net \u2014 and names the exact wealth the fee deletes.",
 "gross = P(1+r)^years; net = P(1+r\u2212fee)^years; drag = gross \u2212 net",
 "100,000 at 7% for 30 years grows to 761,226 gross \u2014 a 1% fee leaves 574,349, deleting 186,876 for the privilege",
 ["choosing index funds over managed","comparing 401k expense ratios","robo-advisor versus DIY math","adviser fee negotiation leverage"],
 "The drag compounds: the same 1% fee costs about twice as much at 30 years as it does at 20. Fee ratios stack \u2014 a 0.75% fund inside a high-fee wrapper charges both.",
 "ie2",
 _f("ie2-p", "Portfolio value", "100000") + _f("ie2-r", "Expected return (%/yr)", "7") + _f("ie2-f", "Annual fee (%)", "1") + _f("ie2-y", "Years invested", "30") +
 '''<button class="btn" onclick="ie2()">Show the drag</button>
  <div id="ie2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("salary-raise", "Salary Raise Calculator", "Finance & Business",
 "Raise percentage, real purchasing-power gain and future salary projection",
 "A raise that outpaces inflation buys life; one that loses to it is a polite pay cut. Enter your old and new salary plus the CPI number you trust, and this calculator returns the percentage increase, the real (inflation-adjusted) gain, the new salary in today's money, and how much a 3% drift each year takes from any flat wage.",
 "pct = (new \u2212 old) \u00f7 old \u00d7 100; real = (new \u00f7 old \u00f7 (1 + CPI/100)) \u2212 1, in today's money = new \u00f7 (1 + CPI/100)",
 "50,000 to 55,000 is a 10% raise; with 3% inflation it is a 6.80% real raise \u2014 still a win, but 2,300 smaller than it looks",
 ["offer evaluation and negotiation","annual review preparation","raise vs relocation comparisons","inflation adjustment conversations"],
 "Match periods before judging: a mid-year raise earned for only part of the year reads smaller than it truly is hourly. Raise percentages compound \u2014 two 5% raises are 10.25% overall, not 10%.",
 "sl3",
 _f("sl3-o", "Old salary", "50000") + _f("sl3-n", "New salary", "55000") + _f("sl3-c", "Inflation / CPI (%)", "3") +
 '''<button class="btn" onclick="sl3()">Score the raise</button>
  <div id="sl3-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("vacation-accrual", "Vacation Accrual Calculator", "Finance & Business",
 "Earned PTO days and running balance from any accrual rate",
 "PTO handed out in a lump hides its own math; PTO accrued per pay period is where balances go missing. Enter the accrual rate per month or per period, the months worked and days already taken, and this calculator totals what you have earned, what remains, whether your year-end cap will burn entitled days, and the fraction you have used.",
 "earned = rate \u00d7 months; balance = earned \u2212 used; burn risk = (earned \u2212 used) \u00f7 remaining months\u00d7rate cap",
 "accruing 1.5 days a month over 24 months earns 36 days \u2014 take 8 and 28 remain, more than most caps re-bank",
 ["tracking part-year PTO balances","join-date and anniversary maths","end-of-year use-it-lose-it decisions","contractor and part-time entitlements"],
 "Check whether unused days expire on the company anniversary or roll with a cap \u2014 the same 28 remaining days are worth nothing in January if the year resets silently.",
 "va2",
 _f("va2-r", "Accrual (days per month)", "1.5") + _f("va2-m", "Months worked", "24") + _f("va2-u", "Days already taken", "8") +
 '''<button class="btn" onclick="va2()">Total my PTO</button>
  <div id="va2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("down-payment", "Down Payment Calculator", "Finance & Business",
 "Percent saved, the 20% PMI escape line and months to close the gap",
 "The 20% down mark is not superstition \u2014 it is the line where private mortgage insurance stops charging rent on your loan. Enter the home price and savings, and this calculator reports the percentage covered, the PMI charged monthly below the line, the exact target, how much more is needed, and how many months your saving rate takes to get there.",
 "down% = saved \u00f7 price; PMI \u2248 (price \u2212 down) \u00d7 0.5% \u00f7 12; months to target \u2191 = 20% target shortfall \u00f7 monthly saving",
 "60,000 saved on a 400,000 home is 15% \u2014 PMI charges roughly 141.67 monthly; another 20,000 saved at 500 monthly kills it in 40 months",
 ["first-time-buyer PMI planning","ranking houses within a budget","setting automatic savings targets","cash-flow versus bigger-deposit tradeoffs"],
 "PMI rates vary with credit: 0.5% is mid-quartile, so treat the figure as a floor estimate. A bigger deposit cuts both payment and insurance, but starves emergency cash \u2014 the trade is real.",
 "dn2",
 _f("dn2-p", "Home price", "400000") + _f("dn2-s", "Savings for down payment", "60000") + _f("dn2-m", "Monthly amount you can add", "500") +
 '''<button class="btn" onclick="dn2()">Run the deposit math</button>
  <div id="dn2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("mortgage-points", "Mortgage Points Calculator", "Finance & Business",
 "Upfront point cost, monthly saving and the true break-even month",
 "Buying points trades cash today for a lower rate forever \u2014 but only pays off if you keep the loan past break-even. Enter the loan, the base rate, points purchased and the rate cut each point buys, and this calculator prices the up-front cost, the new monthly payment, the saving per month and the exact month the points start winning.",
 "cost = points% \u00d7 loan; monthly saving = payment at base rate \u2212 payment at cut rate; break-even = cost \u00f7 saving",
 "1 point (3,000) on a 300,000 loan at 6.5% cut to 6.25% saves 49.05 monthly and breaks even at month 61 \u2014 sell earlier and the points lost money",
 ["purchase versus refinance decisions","sequencing cash at closing","estimating staying horizon honestly","loan-offer comparison sheets"],
 "Break-even ignores refinancing exit fees and premature-sale tax effects, so pad the estimate by a few years of doubt.",
 "mp2",
 _f("mp2-l", "Loan amount", "300000") + _f("mp2-r", "Base rate (%)", "6.5") + _f("mp2-p", "Points bought", "1") + _f("mp2-c", "Rate cut per point (%)", "0.25") + _f("mp2-y", "Loan term (years)", "30") +
 '''<button class="btn" onclick="mp2()">Price the points</button>
  <div id="mp2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("freelance-rate", "Freelance Rate Calculator", "Finance & Business",
 "Hourly rate that turns a target income into invoices, not hope",
 "Freelancers who charge what employees earn forget three things: no paid holidays, no pension, and at least a third of hours unbilled. Enter your target take-home, business expenses, hours and billable share, and this calculator works the arithmetic backwards to the hourly rate the target actually demands.",
 "rate = (target income + expenses) \u00f7 (hours per week \u00d7 billable% \u00d7 working weeks)",
 "an 80,000 income with 12,000 expenses needs 83.33 per hour at 60% billed of a 46-week year \u2014 not the 40 that matching salary implies",
 ["setting project and day rates","quarterly income target checks","comparing job offers to freelancing","pricing under-supply and over-demand"],
 "Billable share is the silent killer: 60% is optimistic for beginners, 80% for veterans. Cost of illness and admin belong in expenses, otherwise the rate quietly subsidises the client.",
 "fr3",
 _f("fr3-i", "Target income", "80000") + _f("fr3-e", "Business expenses/year", "12000") + _f("fr3-b", "Billable hours share (%)", "60") + _f("fr3-h", "Hours per week", "40") + _f("fr3-w", "Working weeks per year", "46") +
 '''<button class="btn" onclick="fr3()">Set my rate</button>
  <div id="fr3-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("protein-intake", "Protein Intake Calculator", "Calculators",
 "Daily protein grams tuned by bodyweight and training goal",
 "Protein advice ranges from newspaper guesses to bodybuilder excess. The evidence band sits in grams per kilogram of bodyweight, scaled by what you are training for: maintenance lower, muscle building middle, aggressive cutting highest to protect lean mass. Enter weight and goal, and this calculator returns the daily target, the safe upper ceiling and a per-meal spread.",
 "target = weight \u00d7 goal factor: maintain 1.2, build 1.6, cut 2.0 g/kg; ceiling 2.2 g/kg",
 "an 80 kg lifter building muscle lands on 128 g daily \u2014 32 g across four meals, comfortably above the RDA floor",
 ["training and diet planning","weight-loss muscle protection","vegan and plant-based totals","appetite and meal-prep maths"],
 "The RDA (0.8 g/kg) is a population floor, not a training target. Spread protein across meals; one giant dinner absorbs worse than the same grams through the day.",
 "pi2",
 _f("pi2-w", "Weight (kg)", "80") + _sel("pi2-g", "Goal", [("1.2", "General health \u2014 1.2 g/kg"), ("1.6", "Build muscle \u2014 1.6 g/kg"), ("1.8", "Fat loss \u2014 1.8 g/kg"), ("2.0", "Aggressive cut \u2014 2.0 g/kg")]) +
 '''<button class="btn" onclick="pi2()">Calculate target</button>
  <div id="pi2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("waist-to-height", "Waist-to-Height Ratio Calculator", "Calculators",
 "The one-tape-measure health number doctors now prefer over BMI",
 "Waist-to-height ratio answers the question BMI cannot: where the weight sits. Ratio 0.5 \u2014 waist half your height \u2014 is the strongest simple predictor of central-fat risk, valid across ages and heights. Enter both measurements, and this calculator returns the ratio, its risk band, and what waist size keeps you on the healthy side.",
 "WHtR = waist \u00f7 height; under 0.4 slim, 0.4\u20130.49 healthy, 0.5\u20130.59 increased, 0.6+ high",
 "a 170 cm frame with an 85 cm waist scores exactly 0.50 \u2014 the boundary line, and the number worth beating",
 ["heart-health self-checks","tracking fat loss beyond the scale","children's growth conversations","diabetes risk awareness"],
 "Measure at the navel, not where trousers sit, exhale normally and twice for consistency. Ratio beats BMI because muscle mass cannot confuse it \u2014 a rugby player and a beer belly read differently.",
 "wt2",
 _f("wt2-w", "Waist circumference (cm)", "85") + _f("wt2-h", "Height (cm)", "170") +
 '''<button class="btn" onclick="wt2()">Check the ratio</button>
  <div id="wt2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("steps-to-calories", "Steps to Calories Calculator", "Calculators",
 "Distance walked and energy burned from your step count",
 "Eight thousand steps is a nice round number until you ask what it bought. Steps become metres through stride length, metres become kilometres, and kilometres become calories through bodyweight \u2014 each link is one multiplication. Enter steps, stride and weight, and this calculator returns distance, energy burned and how far that puts you toward the classic 10,000 benchmark.",
 "distance km = steps \u00d7 stride (m) \u00f7 1000; calories \u2248 km \u00d7 weight (kg) \u00d7 0.53",
 "10,000 steps at a 0.70 m stride and 70 kg bodyweight walks 7.0 km for about 260 calories",
 ["walking-program motivation","weight-loss deficit accounting","step-count comparison across heights","activity-band sense checks"],
 "Stride changes with pace \u2014 walking strides run shorter than brisk ones, so measure yours over ten steps and divide. The 0.53 constant assumes flat walking; hills and load raise the burn.",
 "sc3",
 _f("sc3-s", "Steps taken", "10000") + _f("sc3-st", "Stride length (m)", "0.70") + _f("sc3-w", "Weight (kg)", "70") +
 '''<button class="btn" onclick="sc3()">Work out the walk</button>
  <div id="sc3-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("pack-year", "Pack-Year Calculator", "Calculators",
 "The standard pack-years figure lung screening guidelines run on",
 "Pack-years convert smoking history into one number clinicians screen against: packs per day times years smoked. Twenty pack-years is the line where lung-cancer screening eligibility discussions begin. Enter your cigarettes per day and years of smoking, and this calculator converts both, with the pack definition made explicit.",
 "pack-years = (cigarettes per day \u00f7 20) \u00d7 years smoked",
 "15 cigarettes a day for 20 years is 15.0 pack-years \u2014 a three-quarter-pack habit for two decades zones past the 20-year threshold under half a pack more",
 ["lung-screening eligibility checks","clinic and intake history forms","quitting-milestone perspective","risk conversations with a doctor"],
 "A pack means 20 cigarettes regardless of brand strength. Combine periods: two quitting-and-restarting stretches simply add their pack-years together.",
 "pk2",
 _f("pk2-c", "Cigarettes per day", "15") + _f("pk2-y", "Years smoked", "20") +
 '''<button class="btn" onclick="pk2()">Compute pack-years</button>
  <div id="pk2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("blood-pressure-explainer", "Blood Pressure Category Explainer", "Calculators",
 "Where your systolic and diastolic sit on the medical band scale",
 "Blood-pressure readings only mean something against the clinical bands, and those bands changed with modern guidelines. Enter the systolic (top) and diastolic (bottom) numbers, and this explainer classifies the pair by the stricter of the two \u2014 exactly as clinics do \u2014 and returns the pulse pressure, the gap cardiologists also watch.",
 "category = stricter of systolic and diastolic bands; pulse pressure = systolic \u2212 diastolic",
 "118 over 76 is Normal with a 40 pulse pressure; 132 over 76 is already Stage 1 on the systolic side alone",
 ["home-monitor reading checks","doctor-visit preparation","medication-schedule context","family health education"],
 "Classification follows the stricter reading, so a high top number alone raises the band. Home readings run lower than office ones; diagnose nothing here \u2014 screen first, ask the clinic second.",
 "bp2",
 _f("bp2-s", "Systolic (top number)", "118") + _f("bp2-d", "Diastolic (bottom number)", "76") +
 '''<button class="btn" onclick="bp2()">Classify reading</button>
  <div id="bp2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("deadline-days", "Deadline Days Calculator", "Calculators",
 "Calendar days, working days and weeks between any two dates",
 "Deadlines lie when counted in calendar days: two months of calendar is forty working ones. Pick a start and an end date, and this calculator returns calendar days, honest working days with the weekends removed, the week count, and the per-day pace any remaining work has to sustain.",
 "days = end \u2212 start; working days = days \u2212 weekend days between; weeks = days \u00f7 7",
 "1 January to 1 March 2025 spans 59 calendar days but only 42 working ones \u2014 seventeen Saturdays and Sundays the schedule cannot bill",
 ["project planning and sprint math","contract and notice periods","holiday countdowns","study and exam pacing"],
 "Working days here skip weekends only \u2014 public holidays vary by country and need subtracting by hand. Crossing a leap February adds a day; the calendar math handles it.",
 "dl3",
 '<div class="row"><div><label for="dl3-a">From date</label><input type="date" id="dl3-a" value="2025-01-01" /></div><div><label for="dl3-b">Deadline</label><input type="date" id="dl3-b" value="2025-03-01" /></div></div>' +
 '''<button class="btn" onclick="dl3()">Count down to it</button>
  <div id="dl3-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("sunrise-sunset", "Sunrise Sunset Calculator", "Calculators",
 "Astronomical sunrise and sunset times for any place and date",
 "Sunlight is geometry: the sun rises when the horizon clears the solar disc accounting for refraction \u2014 the zenith angle 90.833 degrees astronomers codified. Enter a date, latitude, longitude and your UTC offset, and this calculator applies the NOAA algorithm for both events plus the daylight length between them.",
 "NOAA equations: declination from the true longitude L, hour angle H = arccos[(cos 90.833\u00b0 \u2212 sin\u03b4 sin\u03c6) \u00f7 (cos\u03b4 cos\u03c6)], time from H + RA \u2212 0.06571t \u2212 6.622",
 "New York (40.71N, 74.01W) on 21 June 2024 rises 5:25 and sets 20:31 local \u2014 fifteen hours of daylight",
 ["photography golden-hour planning","running and riding in daylight","vacation and campsite planning","garden and solar-panel siting"],
 "Times are astronomical estimates good to a couple of minutes; local terrain and weather do not enter the equation. The UTC offset must include daylight-saving \u2014 New York is \u22124 in summer, \u22125 in winter.",
 "su2",
 '<div class="row"><div><label for="su2-d">Date</label><input type="date" id="su2-d" value="2024-06-21" /></div><div><label for="su2-tz">UTC offset (hours)</label><select id="su2-tz">' + "".join(f'<option value="{v}"{" selected" if v=="-4" else ""}>{t}</option>' for v, t in [("-8","-8 (Pacific)"),("-7","-7 (Mountain)"),("-6","-6 (Central)"),("-5","-5 (Eastern winter)"),("-4","-4 (Eastern summer)"),("-3","-3"),("0","0 (London winter)"),("1","1 (Central Europe)"),("2","2 (Eastern Europe)"),("5.5","5.5 (India)"),("9","9 (Japan)")]) + '</select></div></div><div class="row"><div><label for="su2-lat">Latitude (\u00b0, + north)</label><input type="number" id="su2-lat" step="any" value="40.7128" autocomplete="off" /></div><div><label for="su2-lon">Longitude (\u00b0, + east)</label><input type="number" id="su2-lon" step="any" value="-74.0060" autocomplete="off" /></div></div>' +
 '''<button class="btn" onclick="su2()">Chart the sun</button>
  <div id="su2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("julian-day", "Julian Day Calculator", "Calculators",
 "Calendar dates into the astronomer's continuous Julian Day Number",
 "Astronomers refused to juggle months and leap years, so they number every day since 4713 BC as one running integer: the Julian Day Number. Noon on 1 January 2000 is JDN 2451545. Enter any date, and this calculator converts it, with the fractional day-of-year and Modified Julian Date the spacecraft logs use.",
 "JDN = Date.UTC(year, month, day, 12) \u00f7 86400000 + 2440587.5 (Unix epoch offset)",
 "2000-01-01 noon UTC converts to exactly 2451545 \u2014 and 2024-06-01 noon is JDN 2460463",
 ["astronomy and telescope logs","spacecraft and mission timestamps","historical date arithmetic","photography and eclipse planning"],
 "Astronomical Julian Days turn over at noon UTC, not midnight \u2014 that is why observations log 12:00 cleanly. The Modified Julian Date subtracts 2400000.5 to keep the digits short.",
 "jd2",
 '<div class="row"><div><label for="jd2-d">Date (UTC)</label><input type="date" id="jd2-d" value="2000-01-01" /></div></div>' +
 '''<button class="btn" onclick="jd2()">Convert to JDN</button>
  <div id="jd2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("minutes-to-decimal", "Minutes to Decimal Hours Converter", "Calculators",
 "Timesheet minutes into decimal hours payroll systems expect",
 "Payroll wants 7.25 hours, your brain recorded 7 hours 15 minutes \u2014 and forty weeks of that mismatch is a silent paycheck error. Paste or type minutes (one value per line or space-separated), and this converter returns decimal hours, hours-and-minutes form and the rounding payroll applies.",
 "decimal hours = minutes \u00f7 60; hours and minutes split the integer part back out of sixty",
 "540 minutes is exactly 9.00 hours; 7 hours 45 minutes typed the other way returns 465 minutes",
 ["timesheet entry and approval","invoicing hourly clients","payroll-check spot audits","study and shift logging"],
 "Convert before multiplying by your rate \u2014 7:45 at an hourly rate is decimal 7.75 first, or the bill sits wrong by 7.5 minutes for every quarter hour.",
 "mn3",
 '<div class="row"><div><label for="mn3-in">Minutes (one or several, separated by spaces or lines)</label><textarea id="mn3-in" rows="3" placeholder="540 90 37.5">540 90 37.5</textarea></div></div>' +
 '''<button class="btn" onclick="mn3()">Convert to decimals</button>
  <div id="mn3-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("pregnancy-due-date", "Pregnancy Due Date Calculator", "Calculators",
 "Estimated due date and gestational milestones from the last period",
 "The standard estimate clinicians still chart is Naegele's rule: last menstrual period, plus 280 days. Enter the LMP date, and this calculator returns the estimated due date, today's gestational age, and the week thresholds that mark trimester boundaries \u2014 the same milestones appointment letters reference.",
 "due = LMP + 280 days (40 weeks); trimester II starts +91 days, III +196 days",
 "an LMP of 2024-01-01 dates the due estimate Monday 2024-10-07, with the second trimester opening in early April",
 ["early pregnancy appointment planning","work and leave date estimates","family milestone countdown","expectant-parent checklists"],
 "The rule assumes a 28-day cycle and day-14 ovulation; scans re-date reliably by a week or more. Treat the estimate as a four-week window \u2014 most babies arrive between 37 and 42 weeks.",
 "pd2",
 '<div class="row"><div><label for="pd2-l">First day of last period</label><input type="date" id="pd2-l" value="2024-01-01" /></div></div>' +
 '''<button class="btn" onclick="pd2()">Estimate the date</button>
  <div id="pd2-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("planet-age", "Planet Age Calculator", "Calculators",
 "Your age rescaled to every planet in the solar system",
 "Birthdays measure trips around the Sun, so on Mercury you would ration them \u2014 and on Neptune barely have had one. Enter your Earth age, and this calculator converts it into each planet's years and a next-birthday countdown using the published orbital periods.",
 "planet years = Earth years \u00f7 orbital period (Mercury 0.2408, Venus 0.6152, Mars 1.8808, Jupiter 11.863, Saturn 29.447, Uranus 84.017, Neptune 164.79 Earth years)",
 "age 30 on Earth is 124.56 Mercurian years but barely 1.02 Saturnian \u2014 and still under one Neptunian birthday",
 ["classroom astronomy hooks","solar-system scale intuition","party-trivia and quiz material","planet fact sheets sanity checks"],
 "Periods here are sidereal years in Earth time; birthday-counting is simpler than season-counting on tilted planets. The Moon, not a planet, runs 27.3 Earth days \u2014 monthly birthdays if you insist.",
 "pl3",
 _f("pl3-a", "Earth age (years)", "30") +
 '''<button class="btn" onclick="pl3()">Age me across planets</button>
  <div id="pl3-out" class="result" aria-live="polite"></div>'''))

ADV14.append(("quiz-score", "Quiz Score Calculator", "Calculators",
 "Raw answers into percentage, letter grade and per-question value",
 "Scores need context: how much each question was worth, what the grade bands say, and what one more correct answer changes. Enter questions correct and total, and this calculator returns the percentage, the letter grade on the standard band, and the per-question weight \u2014 plus the retake targets for each grade jump.",
 "score% = correct \u00f7 total \u00d7 100; grade bands A 90+, B 80+, C 70+, D 60+, F below",
 "18 of 20 is 90% \u2014 an A on the line worth 5 points a question, where one miss would have dropped a full half grade",
 ["teachers marking faster","self-testing and flashcard sessions","exam-prep trending across mocks","training assessment scoring"],
 "Watch curve semantics: percentage grading differs from percentile ranking, and rubric bands vary by institution \u2014 this uses the common 10-point band. Weight per question only stays equal in flat quizzes.",
 "qs2",
 _f("qs2-c", "Questions correct", "18") + _f("qs2-t", "Questions total", "20") +
 '''<button class="btn" onclick="qs2()">Score the quiz</button>
  <div id="qs2-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV14:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA14[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'''<div class="panel">{extra}{tail}</div>''',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT14[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
