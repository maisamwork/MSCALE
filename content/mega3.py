# -*- coding: utf-8 -*-
from .mega1a import _fit
from .mega1b import calc_article

def _f(i, l, v="", ph=""):
    p = f' placeholder="{ph}"' if ph else ""
    return f'<div><label for="{i}">{l}</label><input type="number" id="{i}" step="any" value="{v}"{p} autocomplete="off" /></div>'

def _sel(i, l, opts):
    o = "".join(f'<option value="{v}">{t}</option>' for v, t in opts)
    return f'<div><label for="{i}">{l}</label><select id="{i}">{o}</select></div>'

MEGA3 = {}
CONTENT3 = {}

ADV = []

ADV.append(("compound-interest-pro","Compound Interest Calculator Pro","Finance & Business",
 "Future value with monthly contributions, compounding choice and a growth chart",
 "Compound interest is what makes long-term saving powerful: each period earns interest on the interest already earned, so growth accelerates with time. The effect becomes dramatic when regular monthly contributions are added on top. This pro version computes the final balance with monthly deposits, lets you choose the compounding frequency, and draws the growth year by year so you can see the curve, not just the number.",
 "FV = P(1 + r/n)^(nt) + contributions compounded monthly",
 "1,000 invested at 7% for 10 years with 100 per month grows to about 19,300 \u2014 of which 13,000 is your own contribution and 6,300 is interest",
 ["retirement and savings planning","comparing investment offers","motivating a savings habit","teaching how compounding works"],
 "Compounding frequency matters less than time: monthly vs yearly compounding changes the result slightly, but two extra years change it a lot.",
 "ci",
 '''<div class="row">''' + _f("ci-p","Initial amount","1000") + _f("ci-m","Monthly contribution","100") + _f("ci-r","Annual return (%)","7") + _f("ci-y","Years","10") + '''</div>''' + _sel("ci-f","Compounding", [("12","Monthly"),("4","Quarterly"),("1","Yearly")]) + '''<button class="btn" onclick="ci()">Calculate growth</button>
  <div id="ci-out" class="result" aria-live="polite"></div>
  <canvas id="ci-chart" width="640" height="220" class="chart"></canvas>'''))

ADV.append(("loan-amortization-calculator","Loan Amortization Calculator","Finance & Business",
 "Monthly payment plus the full year-by-year split of interest and principal",
 "A loan payment stays the same for years, but what it buys changes every month: early payments are mostly interest, late ones mostly principal. That schedule \u2014 the amortization \u2014 explains why paying a little extra early saves so much, and why the balance barely moves in year one. This calculator computes the payment and shows the schedule so you can see exactly where your money goes.",
 "M = P \u00d7 r(1+r)^n / ((1+r)^n \u2212 1), with r the monthly rate",
 "10,000 at 6% for 3 years gives a payment of about 304.22 and 950-ish total interest",
 ["checking a mortgage or car loan offer","seeing the cost of a longer term","planning extra repayments","comparing lender quotes"],
 "The schedule assumes fixed rate and equal payments; variable-rate loans and ones with fees will drift from this baseline.",
 "am",
 '''<div class="row">''' + _f("am-a","Loan amount","10000") + _f("am-r","Annual interest rate (%)","6") + _f("am-y","Term (years)","3") + '''</div>''' + '''<button class="btn" onclick="am()">Build schedule</button>
  <div id="am-out" class="result" aria-live="polite"></div>
  <div id="am-table" class="uc-tablewrap"></div>'''))

ADV.append(("calorie-calculator","Calorie Calculator (BMR & TDEE)","Calculators",
 "Daily calorie needs from your body stats and activity level, with goal targets",
 "Calorie planning starts with two numbers: BMR, the energy your body burns at complete rest, and TDEE, which adds your daily activity on top. Eat below TDEE and you lose weight; above it and you gain. This calculator uses the Mifflin\u2013St Jeor formula \u2014 the one modern dietitians consider most accurate \u2014 and turns your TDEE into practical targets for losing, maintaining or gaining.",
 "BMR (Mifflin\u2013St Jeor) = 10\u00d7kg + 6.25\u00d7cm \u2212 5\u00d7age + s;  TDEE = BMR \u00d7 activity factor",
 "A 30-year-old man, 180 cm, 80 kg, lightly active has a BMR near 1,780 and a TDEE near 2,440 kcal",
 ["setting a weight-loss or gain target","planning meals around a number","checking a diet plan's assumptions","fitness coaching"],
 "TDEE multipliers are averages \u2014 track your actual weight trend for two weeks and adjust by 100\u2013200 kcal rather than trusting any formula blindly.",
 "cal",
 '''<div class="row">''' + _f("cal-age","Age","30") + _sel("cal-sex","Sex",[("m","Male"),("f","Female")]) + _f("cal-h","Height (cm)","180") + _f("cal-w","Weight (kg)","80") + '''</div>''' + _sel("cal-act","Activity level", [("1.2","Sedentary (desk job)"),("1.375","Light (1\u20133 workouts/wk)"),("1.55","Moderate (3\u20135)"),("1.725","Very active (6\u20137)"),("1.9","Athlete (2\u00d7 daily)")]) + '''<button class="btn" onclick="cal()">Calculate needs</button>
  <div id="cal-out" class="result" aria-live="polite"></div>'''))

ADV.append(("body-fat-calculator","Body Fat Calculator (Navy Method)","Calculators",
 "Body fat percentage from tape measurements, with fitness categories",
 "Weight alone cannot tell fat from muscle \u2014 two people at 80 kg can have completely different body composition. The US Navy tape method estimates body fat percentage from circumference measurements, and it tracks change over time well even where its absolute accuracy is a few percent off. This calculator applies the official formula and places your result in standard fitness categories.",
 "Navy method: %BF = 495 / (1.0324 \u2212 0.19077\u00d7log10(waist\u2212neck) + 0.15456\u00d7log10(height)) \u2212 450 (men)",
 "A man 180 cm tall with a 90 cm waist and 38 cm neck measures roughly 20% body fat",
 ["tracking a fitness program","setting a realistic target","health and insurance assessments","between-scale progress checks"],
 "Measure consistently: same time of day, tape level and snug but not pressing \u2014 sloppy measuring moves the result by whole percentage points.",
 "bf",
 '''<div class="row">''' + _sel("bf-sex","Sex",[("m","Male"),("f","Female")]) + _f("bf-h","Height (cm)","180") + '''</div>''' + '''<div class="row">''' + _f("bf-neck","Neck circumference (cm)","38") + _f("bf-waist","Waist circumference (cm)","90") + _f("bf-hip","Hip circumference (cm, women)","100") + '''</div>''' + '''<button class="btn" onclick="bf()">Estimate body fat</button>
  <div id="bf-out" class="result" aria-live="polite"></div>'''))

ADV.append(("one-rep-max-calculator","One Rep Max Calculator","Calculators",
 "Your 1RM from any weight \u00d7 reps set, plus training percentages",
 "Testing a true one-rep max is risky and exhausting, so lifters estimate it from a lighter set: the most weight you can lift for 3\u201310 reps predicts your 1RM very reliably. This calculator runs both standard formulas (Epley and Brzycki), averages them, and prints the classic training percentages \u2014 the numbers strength programs are actually built from.",
 "Epley: 1RM = w \u00d7 (1 + reps/30);  Brzycki: 1RM = w \u00d7 36 / (37 \u2212 reps)",
 "Squatting 100 kg for 5 reps predicts a one-rep max of about 113 kg",
 ["programming strength training","tracking progress without maxing out","planning safe testing sessions","comparing lifts across body weights"],
 "The formulas are calibrated for sets of 10 reps or fewer \u2014 a 20-rep set predicts a 1RM that is pure fantasy.",
 "orm",
 '''<div class="row">''' + _f("orm-w","Weight lifted (kg)","100") + _f("orm-r","Reps completed","5") + '''</div>''' + '''<button class="btn" onclick="orm()">Estimate 1RM</button>
  <div id="orm-out" class="result" aria-live="polite"></div>
  <div id="orm-table" class="uc-tablewrap"></div>'''))

ADV.append(("running-pace-calculator","Running Pace Calculator","Calculators",
 "Pace per km and per mile, plus speed, from any race time",
 "Every training plan is written in pace, not speed: 'run 5:30 per kilometre' means something on any route, while '10 km/h' needs mental math. Enter a distance and a finish time and this calculator returns your pace per kilometre and per mile plus your speed \u2014 the fastest way to check whether a race result matches a goal or a plan.",
 "Pace = time / distance, shown per km and per mile;  Speed = distance / time",
 "A 25:00 5K is a 5:00 per-km pace, about 8:03 per mile, at 12 km/h",
 ["race goal setting","training plan zones","comparing performances over different distances","predicting finish times"],
 "Pace from a GPS watch drifts on tree-covered routes; compute from a known distance for goal-setting numbers.",
 "pace",
 '''<div class="row">''' + _f("pace-d","Distance (km)","5") + _f("pace-h","Hours","0") + _f("pace-m","Minutes","25") + _f("pace-s","Seconds","0") + '''</div>''' + '''<button class="btn" onclick="pace()">Calculate pace</button>
  <div id="pace-out" class="result" aria-live="polite"></div>'''))

ADV.append(("break-even-calculator","Break-Even Calculator","Finance & Business",
 "Units and revenue needed before a business makes its first unit of profit",
 "Every product decision hides one question: how many units must I sell before the fixed costs are covered? Selling below break-even is funding the loss from savings; knowing the number turns a vague worry into a target. This calculator divides fixed costs by the per-unit margin and shows both the unit and revenue break-even points.",
 "Break-even units = fixed costs / (price per unit \u2212 variable cost per unit)",
 "3,000 fixed costs, a 25 price and a 15 variable cost mean break-even at 300 units, or 7,500 of revenue",
 ["pricing a new product","writing a business plan","deciding whether a discount is survivable","setting a sales team target"],
 "If price minus variable cost is zero or negative, no volume ever breaks even \u2014 the tool flags it instead of dividing by zero.",
 "be",
 '''<div class="row">''' + _f("be-f","Fixed costs (rent, salaries\u2026)","3000") + _f("be-p","Price per unit","25") + _f("be-v","Variable cost per unit","15") + '''</div>''' + '''<button class="btn" onclick="be()">Find break-even</button>
  <div id="be-out" class="result" aria-live="polite"></div>'''))

ADV.append(("roi-calculator","ROI Calculator","Finance & Business",
 "Return on investment with annualized rate for fair comparisons",
 "ROI answers 'was it worth it?' \u2014 but a raw percentage hides time: 50% over five years is much weaker than 50% over one. This calculator computes total ROI and, when you enter the holding period, the annualized equivalent (CAGR), so a marketing campaign, a course, a renovation or a stock can be judged on the same scale.",
 "ROI = (final \u2212 initial) / initial \u00d7 100;  annualized = ((final/initial)^(1/years) \u2212 1) \u00d7 100",
 "10,000 growing to 16,000 in 3 years is a 60% ROI, or about 16.96% per year",
 ["evaluating investments and campaigns","comparing projects of different lengths","business cases and reports","personal finance decisions"],
 "ROI on paper ignores risk and extra contributions \u2014 compare annualized figures between options of similar risk, not just the biggest percentage.",
 "roi",
 '''<div class="row">''' + _f("roi-i","Initial investment","10000") + _f("roi-f","Final value","16000") + _f("roi-y","Holding period (years)","3") + '''</div>''' + '''<button class="btn" onclick="roi()">Calculate ROI</button>
  <div id="roi-out" class="result" aria-live="polite"></div>'''))

ADV.append(("unit-price-calculator","Unit Price Calculator","Finance & Business",
 "Compare two products by true price per unit and see which wins",
 "Shelf prices are designed to be incomparable: 750 ml against 1 L, a 6-pack against a single, 400 g against 12 oz. The only fair comparison is price per unit \u2014 and stores that print unit prices do it in inconsistent units. This calculator converts two products to price per unit of your chosen size and names the cheaper one with the saving percentage.",
 "Unit price = price / quantity; compare the smaller value",
 "A 1.20 L bottle at 3.00 costs 2.50 per liter; a 750 ml bottle at 2.10 costs 2.80 \u2014 the big one wins by 11%",
 ["grocery shopping decisions","bulk vs small packaging","supplier quote comparison","budgeting household staples"],
 "Enter both quantities in the same unit \u2014 convert milliliters to liters first or the comparison is meaningless.",
 "up",
 '''<div class="row">''' + _f("up-pa","Product A price","3.00") + _f("up-sa","Product A size (units)","1.2") + _f("up-pb","Product B price","2.10") + _f("up-sb","Product B size (units)","0.75") + '''</div>''' + '''<button class="btn" onclick="up()">Compare prices</button>
  <div id="up-out" class="result" aria-live="polite"></div>'''))

ADV.append(("grade-calculator","Final Grade Calculator","Calculators",
 "The score you need on the final exam to hit your target grade",
 "Weeks before an exam, the question that actually matters is concrete: what do I need on the final to finish with 80%? Guessing leads to either panic or complacency. This calculator takes your current grade, the weight of the remaining exam and your target, and returns the exact score required \u2014 including the cases where the target is already locked in or mathematically out of reach.",
 "Needed = (target \u2212 current \u00d7 (1 \u2212 w)) / w, with w the exam weight as a decimal",
 "An 82% current grade with a 40% final and a target of 85% needs a 89.5% on the exam",
 ["exam preparation priorities","setting realistic grade targets","checking whether a goal is still possible","advising students on effort allocation"],
 "Weights must add up: if the final is worth 40%, your current grade covers the other 60% \u2014 entering the wrong weight reverses the logic entirely.",
 "gr",
 '''<div class="row">''' + _f("gr-c","Current grade (%)","82") + _f("gr-w","Final exam weight (%)","40") + _f("gr-d","Target overall grade (%)","85") + '''</div>''' + '''<button class="btn" onclick="gr()">What do I need?</button>
  <div id="gr-out" class="result" aria-live="polite"></div>'''))

ADV.append(("electricity-cost-calculator","Electricity Cost Calculator","Calculators",
 "What any appliance really costs to run, per day and per year",
 "Appliances quietly bill you: an old fridge, a space heater, a gaming PC left on \u2014 each has a watt rating and each hour has a price. This calculator turns watts and hours into kilowatt-hours and money, per day, month and year, which is the only way to know whether that 'small' device is a 5-euro or a 150-euro line on your annual budget.",
 "Cost = (watts / 1000) \u00d7 hours \u00d7 price per kWh",
 "A 2,000 W heater running 5 h/day at 0.30 per kWh costs 3.00 per day \u2014 about 547 per heating season",
 ["cutting household energy bills","comparing appliances before buying","estimating office equipment costs","checking a heater or AC's real cost"],
 "Use the rated watts for resistive devices (heaters, kettles); for fridges and pumps that cycle on and off, halve the hours to approximate real duty.",
 "ec",
 '''<div class="row">''' + _f("ec-w","Power (watts)","2000") + _f("ec-h","Hours per day","5") + _f("ec-d","Days per year","365") + _f("ec-p","Price per kWh","0.30") + '''</div>''' + '''<button class="btn" onclick="ec()">Calculate cost</button>
  <div id="ec-out" class="result" aria-live="polite"></div>'''))

ADV.append(("sleep-cycle-calculator","Sleep Cycle Calculator","Calculators",
 "Bedtimes that let you wake between sleep cycles, not in the middle of one",
 "Sleep runs in roughly 90-minute cycles, and waking in the middle of deep sleep is what makes mornings feel like sand \u2014 waking between cycles feels dramatically better even with the same total hours. This calculator works backwards from your wake-up time: it lists the bedtimes that allow 6, 5, 4 or 3 full cycles plus the ~15 minutes most people need to fall asleep.",
 "Bedtime = wake time \u2212 (cycles \u00d7 90 min) \u2212 15 min to fall asleep",
 "To wake at 7:00 AM, the six-cycle bedtime is about 9:45 PM; five cycles land at 11:15 PM",
 ["planning a better morning","shifting a sleep schedule","recovering after late nights","parents and shift workers"],
 "The 90-minute cycle is an average, not a law \u2014 use the list as a starting range and adjust by how you actually feel after a week.",
 "sleep",
 '''<div class="row"><div><label for="sl-time">I want to wake up at</label><input type="text" id="sl-time" class="dt-input" readonly placeholder="07:00" /><input type="hidden" id="sl-tv" value="07:00" /></div></div>''' + '''<button class="btn" onclick="sleep()">Find bedtimes</button>
  <div id="sleep-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV:
    MEGA3[slug] = {"name": name, "cat": cat, "short": short,
                   "body": f'''<div class="panel">{extra}</div>''',
                   "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT3[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
