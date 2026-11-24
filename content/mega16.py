# -*- coding: utf-8 -*-
"""Batch 29 module A: 18 flagship tools (finance, work, household costs)."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA16 = {}
CONTENT16 = {}

ADV16 = []

ADV16.append(("overtime-rate-calculator", "Overtime Rate Calculator", "Finance & Business",
 "Weekly gross pay with straight time and overtime split",
 "Overtime looks simple on paper and stays simple no longer than one payslip. Enter the hours worked, the base rate and the multiplier your contract promises, and this calculator splits the week into straight-time and overtime dollars, shows the premium that overtime actually added, and prices the effective hourly rate of the whole week.",
 "gross = base_rate \u00d7 min(hours, 40) + base_rate \u00d7 multiplier \u00d7 max(0, hours \u2212 40); effective = gross \u00f7 hours",
 "46 hours at $20 with time-and-a-half pays $980 \u2014 the six OT hours contributed $180, a $30 effective rate for that slice",
 ["wage-law compliance checks","comparing job offers with overtime","contract negotiations","payroll spot-checks"],
 "US federal law sets the floor at 1.5\u00d7 for over 40 weekly hours, but contracts and states can promise more \u2014 never less. Salaried exempt employees fall outside this formula entirely, so running it on their behalf misleads.",
 "ov3",
 _f("ov3-h", "Hours worked this week", "46") + _f("ov3-r", "Base hourly rate", "20") + _sel("ov3-m", "Overtime multiplier", [("1.5", "Time and a half (1.5\u00d7)"), ("2", "Double time (2\u00d7)"), ("1.25", "Contract 1.25\u00d7"), ("1", "None \u2014 flat")]) +
 '''<button class="btn" onclick="ov3()">Run the week</button>
  <div id="ov3-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("hourly-to-salary", "Hourly to Salary Calculator", "Finance & Business",
 "Annual, monthly, weekly and daily pay from any hourly rate",
 "Job ads quote hourly, budgets run monthly, and annual-salary discussions assume neither. Enter the hourly rate, weekly hours and paid weeks per year, and this converter answers the full pay calendar \u2014 annual, monthly, fortnightly, weekly and per working day \u2014 so a $22 rate and a $45,760 salary can be compared on the same page.",
 "annual = hourly \u00d7 weekly hours \u00d7 paid weeks; monthly = annual \u00f7 12; daily = weekly \u00f7 days worked",
 "full time at $22 with 52 paid weeks is $45,760 a year \u2014 $3,813.33 a month and $110 a day",
 ["comparing contract and staff roles","freelance rate setting","renting and mortgage affordability","negotiating from an anchor"],
 "Unpaid holidays and sick days slash paid weeks well below 52 \u2014 contractors often bill 46, which is $3,056 a year less at this rate. Salaried roles usually expect unpaid overtime, which the hourly number is hiding.",
 "hs3",
 _f("hs3-h", "Hourly rate", "22") + _f("hs3-w", "Hours per week", "40") + _f("hs3-k", "Paid weeks per year", "52") +
 '''<button class="btn" onclick="hs3()">Annualize it</button>
  <div id="hs3-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("commission-earner", "Commission Earner Calculator", "Finance & Business",
 "Base salary plus commission with a per-deal average included",
 "Commission plans have three moving parts \u2014 the base, the rate and what happens past quota \u2014 and salespeople sign them faster than they read them. Enter the base, the commission rate and the sales run-rate, and this calculator totals the year, the month and the per-deal average so the plan only surprises you in good ways.",
 "income = base + sales \u00d7 rate% ; per deal = income \u00f7 deals closed",
 "$40,000 base plus 4% on $600,000 of sales is $64,000 \u2014 and those 48-odd closed deals averaged $1,333 each",
 ["sales role comparisons","freelance business development","quota-setting sanity checks","recruiting offers"],
 "Fully commission roles can swing wildly across months, so lenders often haircut commission income when you apply for a mortgage. Check whether clawbacks apply if customers cancel within the first year.",
 "ce3",
 _f("ce3-b", "Base salary", "40000") + _f("ce3-s", "Expected annual sales", "600000") + _f("ce3-r", "Commission rate (%)", "4") + _f("ce3-d", "Deals closed per year", "48") +
 '''<button class="btn" onclick="ce3()">Total the year</button>
  <div id="ce3-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("gratuity-guide", "Gratuity Guide", "Finance & Business",
 "Tip percentages by service quality with per-person splitting",
 "Tipping is percentages dressed as etiquette, and every country hides a different norm inside the bill. Enter the bill, pick the service level and party size, and this guide answers the tip at your chosen rate, the per-person total when splitting, and what the pre-tax versus post-tax distinction is worth on a typical bill.",
 "tip = bill \u00d7 rate%; per person = (bill + tip) \u00f7 diners",
 "an $86 bill for four at 18% tips $15.48 \u2014 $25.37 each, or about $24.60 if you tip on the pre-tax line",
 ["restaurant group bills","hair, taxi and delivery norms abroad","card-tipping verification","expense reports"],
 "In the US 15\u201322% is the operating range and delivery drops below it; in Japan and much of Europe tipping can insult \u2014 service charge is printed. Tipping on the post-tax total silently donates an extra percent.",
 "gt2",
 _f("gt2-b", "Bill total", "86") + _sel("gt2-q", "Service level", [("15", "Fine for basics \u2014 15%"), ("18", "Good service \u2014 18%"), ("22", "Excellent \u2014 22%"), ("10", "Counter service \u2014 10%")]) + _f("gt2-n", "Party size", "4") +
 '''<button class="btn" onclick="gt2()">Split the bill</button>
  <div id="gt2-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("bill-organizer", "Bill Organizer", "Finance & Business",
 "Recurring bills totalled, annualized and ranked for negotiation",
 "Fixed bills feel small individually and enormous in aggregate, and nobody totals them twice a year. Enter each monthly charge \u2014 rent, energy, internet, phone, insurance, subscriptions \u2014 and this organizer answers the monthly total, the annual cost and which single drain deserves the next negotiation hour.",
 "monthly = sum of fixed charges; annual = monthly \u00d7 12",
 "five bills of 1,100 rent, 120 energy, 45 internet, 30 phone and 28 insurance total $1,323 \u2014 $15,876 a year",
 ["switching to fortnightly budgeting","negotiation season prep","flatmate bill-splitting","cancellation priority"],
 "Annualized small leaks are where negotiation pays: repricing a $45 internet bill yearly beats a small raise at work most years. Check autopay dates after any bank change \u2014 failed debits add fees fast.",
 "bo2",
 _f("bo2-a", "Rent / mortgage", "1100") + _f("bo2-b", "Energy / electricity", "120") + _f("bo2-c", "Internet", "45") + _f("bo2-d", "Mobile phone", "30") + _f("bo2-e", "Insurance", "28") + _f("bo2-f", "Other recurring", "0") +
 '''<button class="btn" onclick="bo2()">Total the bills</button>
  <div id="bo2-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("grocery-budget", "Grocery Budget Planner", "Finance & Business",
 "Per-person weekly grocery budgets scaled to your household",
 "Food is the most flexible large monthly line and the one households track least. Enter the number of adults and children with your local weekly per-adult baseline, and this planner answers the household weekly, monthly and annual food spend, plus what one careful month or one guest-heavy month actually swings.",
 "monthly = (adults \u00d7 adult_rate + children \u00d7 0.67 \u00d7 adult_rate) \u00d7 4.33; annual = monthly \u00d7 12",
 "two adults and one child at a $75 weekly baseline run about $867 a month \u2014 $10,413 a year, or $28.53 a day",
 ["budget planning","moving out cost estimates","meal-prep ROI checks","food waste tracking"],
 "Children eat roughly two-thirds of an adult baseline until early teens, then more. The biggest lever is not brand choice \u2014 it is what gets thrown away at the end of the week.",
 "gr2",
 _f("gr2-a", "Adults", "2") + _f("gr2-c", "Children", "1") + _f("gr2-r", "Weekly per-adult baseline", "75") +
 '''<button class="btn" onclick="gr2()">Plan the food budget</button>
  <div id="gr2-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("net-worth-tracker", "Net Worth Tracker", "Finance & Business",
 "Everything you own minus everything you owe, in one panel",
 "Net worth is the only financial number that survives a change of country, currency or career, and it is still the one most people never compute. Enter assets by type and debts by type, and this tracker answers the total, the ratio of debt to assets, and how much of the balance is liquid versus locked in property.",
 "net worth = total assets \u2212 total debts; debt ratio = debts \u00f7 assets \u00d7 100",
 "cash 15,000 + investments 60,000 + home 320,000 against 210,000 mortgage and 9,500 other leaves $175,500 \u2014 debt at 55.6% of assets",
 ["annual financial reviews","mortgage and loan applications","retirement readiness checks","moving or emigrating plans"],
 "Home equity is an asset on paper and not spendable cash, which is why the tracker separates liquid from locked. Track the number quarterly \u2014 direction beats precision, and campaigns get built on quarterly wins.",
 "nw2",
 _f("nw2-c", "Cash & savings", "15000") + _f("nw2-i", "Investments & retirement", "60000") + _f("nw2-h", "Home / property value", "320000") + _f("nw2-o", "Other assets", "0") + _f("nw2-m", "Mortgage balance", "210000") + _f("nw2-l", "Loans & card debt", "9500") +
 '''<button class="btn" onclick="nw2()">Compute net worth</button>
  <div id="nw2-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("liquid-net-worth", "Liquid Net Worth Calculator", "Finance & Business",
 "The spendable slice of your wealth, measured in months",
 "A six-figure net worth with none of it liquid cannot pay a surprise invoice, which is why lenders and planners ask the liquid question separately. Enter cash, investments, short-term debts and monthly expenses, and this calculator answers the liquid balance, its share of total wealth and how many months of living it would actually cover.",
 "liquid = cash + investments \u2212 short-term debt; months = liquid \u00f7 monthly expenses",
 "cash 32,000 and investments 55,000 against 6,500 owing covers 16.1 months of $5,000 spending \u2014 more than a full year of disruption absorbed",
 ["emergency readiness checks","job-change runways","business credit applications","sale-and-relocation planning"],
 "Retirement accounts are liquid only with tax friction, so count them at a discount if a crisis is realistic. One to two months of expenses in pure cash beats a beautiful illiquid paper total.",
 "ln3",
 _f("ln3-c", "Cash & savings", "32000") + _f("ln3-i", "Investable investments", "55000") + _f("ln3-d", "Short-term debt", "6500") + _f("ln3-e", "Monthly expenses", "5000") +
 '''<button class="btn" onclick="ln3()">Measure liquidity</button>
  <div id="ln3-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("emergency-fund", "Emergency Fund Calculator", "Finance & Business",
 "Target fund size, the gap and the months left to fill it",
 "The emergency fund is the only insurance policy that pays cash wages, and the honest target is months of expenses, not a lucky round number. Enter monthly essentials, what is already saved and your monthly contribution, and this calculator answers the target at three, six and nine months, the remaining gap and the exact number of months to close it.",
 "target = essential monthly spend \u00d7 months; gap = target \u2212 saved; months to close = gap \u00f7 monthly saving",
 "$2,800 of essentials and $4,200 saved target $16,800 at six months \u2014 a $12,600 gap that $500 monthly closes in 25.2 months",
 ["layoff risk planning","self-employed buffer sizing","before big-ticket purchases","couples' finance talks"],
 "Three months suits stable dual incomes; six suits single earners and freelancers; nine suits volatile industries. Park the fund in a separate savings account \u2014 visibility is what keeps it from being spent.",
 "ef3",
 _f("ef3-e", "Essential monthly expenses", "2800") + _f("ef3-s", "Already saved", "4200") + _f("ef3-c", "Saving per month", "500") +
 '''<button class="btn" onclick="ef3()">Find the gap</button>
  <div id="ef3-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("sinking-fund", "Sinking Fund Calculator", "Finance & Business",
 "What a fixed monthly deposit grows into by a target date",
 "The sinking fund is the boring superpower of planned spending: a fixed deposit, a real interest rate, a firm date. Enter the monthly amount, the rate and the years, and this calculator answers the value at the end, the deposits you made and the interest the bank paid for the discipline \u2014 all forward-looking and exact.",
 "fv = pmt \u00d7 (((1 + r/12)^n \u2212 1) \u00f7 (r/12)); deposits = pmt \u00d7 n; interest = fv \u2212 deposits",
 "$100 a month for 10 years at 4% compounds to $14,724.98 \u2014 $2,725 of it pure interest you did not deposit",
 ["car-replacement savings","holiday and wedding funds","home-repair reserves","deposit and move-out planning"],
 "A sinking fund removes the payday-loan reflex from predictable costs like tyres and annual renewals. Check withdrawal penalties \u2014 the count only works if the money can actually be reached on the date.",
 "sf2",
 _f("sf2-p", "Monthly deposit", "100") + _f("sf2-r", "Annual rate (%)", "4") + _f("sf2-y", "Years", "10") + _f("sf2-g", "Goal amount (optional)", "") +
 '''<button class="btn" onclick="sf2()">Project the fund</button>
  <div id="sf2-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("savings-rate", "Savings Rate Calculator", "Finance & Business",
 "The percentage of income that disappears into savings",
 "The savings rate is the single lever that decides how many working years a career has left, and it hides inside two ordinary numbers. Enter income and expenses, and this calculator answers the rate, the dollars saved daily, the projected annual total and what the number means against common financial-independence benchmarks.",
 "rate = (income \u2212 expenses) \u00f7 income \u00d7 100; daily = annual savings \u00f7 365",
 "$5,000 income against $3,750 of spending saves 25% \u2014 $1,250 a month and $15,000 a year, one working month banked in every four",
 ["financial-independence planning","cost-cutting priority checks","dual-income household sync","bonus allocation rules"],
 "Fifteen percent is the classic retirement floor; twenty-five starts bending working years down sharply. Use take-home pay for both numbers \u2014 gross income flatters a rate the tax office has already reduced.",
 "sr3",
 _f("sr3-i", "Monthly take-home income", "5000") + _f("sr3-e", "Monthly expenses", "3750") +
 '''<button class="btn" onclick="sr3()">Rate my saving</button>
  <div id="sr3-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("credit-utilization", "Credit Utilization Calculator", "Finance & Business",
 "Card balances against limits with two target thresholds scored",
 "Second only to payment history, credit utilization is the fastest-moving number on a credit report, and it can halve a score one statement cycle after a big buy. Enter total balances and limits, and this calculator answers the utilization percentage, its verdict, and the exact dollar ceiling you should stay under at 30% and at the elite 10%.",
 "utilization = balances \u00f7 limits \u00d7 100; spending target = limit \u00d7 threshold",
 "$1,500 of balances across $8,000 of limits is 18.8% \u2014 fine, while the elite 10% band starts at $800",
 ["before mortgage applications","clearing a big holiday spend","rebuilding after late payments","asking for limit raises"],
 "The number that matters is the one printed on your statement date, not what you owe after paying \u2014 pay before that date to control it. Requesting a limit rise lowers utilization instantly but hard-pulls some reports.",
 "cu2",
 _f("cu2-b", "Total card balances", "1500") + _f("cu2-l", "Total credit limits", "8000") +
 '''<button class="btn" onclick="cu2()">Score the balances</button>
  <div id="cu2-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("auto-loan-calculator", "Auto Loan Calculator", "Finance & Business",
 "Monthly payment, interest damage and per-$1,000 cost of a car loan",
 "Car dealers quote a monthly payment because it hides the interest, and nobody reaches for the formula on the showroom floor. Enter the price, the deposit, the rate and the term, and this calculator answers the financed amount, the monthly payment, the interest the loan will burn and the per-$1,000 monthly rate the trade sheets use.",
 "pmt = L \u00d7 i \u00f7 (1 \u2212 (1 + i)^\u2212n) with i = rate/1200 and n = months; interest = pmt \u00d7 n \u2212 L",
 "$30,000 financed for 60 months at 6% is $579.98 a month \u2014 and $4,799 of interest on top of the sticker",
 ["dealership negotiation","comparing bank and dealer finance","shortening loan terms","used-car budgeting"],
 "Every extra $1,000 of deposit removes roughly $19 of monthly payment plus its interest share. Extending to 84 months lowers the payment while nearly doubling interest \u2014 the sheet favourite of every showroom.",
 "au2",
 _f("au2-p", "Car price", "32000") + _f("au2-d", "Down payment", "2000") + _f("au2-r", "APR (%)", "6") + _f("au2-t", "Term (months)", "60") +
 '''<button class="btn" onclick="au2()">Run the loan</button>
  <div id="au2-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("lease-vs-buy", "Lease vs Buy Calculator", "Finance & Business",
 "Total three-year and five-year driving costs compared honestly",
 "Leases advertise impressions and loans advertise payments, and only a total comparison exposes either. Enter the lease terms and the loan terms with expected resale value, and this calculator answers what each path actually spends over the term, the monthly gap and the break-even judgment in plain words.",
 "lease total = deposit + monthly \u00d7 months; buy total = loan payments \u2212 resale value",
 "$350 a month for 36 with a $2,000 deposit spends $14,600 \u2014 while a 60-month buy at $450 that resells for $12,000 costs $15,000",
 ["new-car decision","company-car schemes","family second vehicle","low-mileage drivers"],
 "Mileage caps are the lease trap: excess charges per mile add up at motorway speeds. Buying wins whenever you keep the car long past the loan \u2014 leases win on certainty and maintenance.",
 "lv2",
 _f("lv2-l", "Lease monthly", "350") + _f("lv2-d", "Lease deposit", "2000") + _f("lv2-t", "Lease term (months)", "36") + _f("lv2-b", "Buy monthly", "450") + _f("lv2-n", "Loan term (months)", "60") + _f("lv2-r", "Resale value at end", "12000") +
 '''<button class="btn" onclick="lv2()">Compare the paths</button>
  <div id="lv2-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("gap-insurance-cost", "Gap Insurance Cost Calculator", "Finance & Business",
 "The depreciation window your loan outlives, priced in dollars",
 "The dangerous first years of car ownership come from the loan balance falling slower than the car's value \u2014 the gap a write-off exposes. Enter the loan balance, the car's current value and the policy price, and this calculator answers the exact gap, weighs it against the policy's cost, and states plainly when the cover is worth it.",
 "gap = loan balance \u2212 vehicle value; policy verdict = gap \u2212 policy cost",
 "a $27,400 balance on a $23,900 car runs a $3,500 gap \u2014 a $350 policy that pays for itself ten times over in one total-loss claim",
 ["new-car purchases","small-deposit finance","buying out an existing lease","insurance renewal reviews"],
 "Gap cover matters most in the first two years, when cars lose value fastest, and becomes dead weight once value and balance cross. Dealer-sold policies are often triple the standalone price \u2014 buy them separately.",
 "gp4",
 _f("gp4-b", "Loan balance", "27400") + _f("gp4-v", "Vehicle value now", "23900") + _f("gp4-p", "Policy cost", "350") +
 '''<button class="btn" onclick="gp4()">Price the gap</button>
  <div id="gp4-out" class="result" aria-live="polite"></div>'''))

ADV16.append(("car-depreciation", "Car Depreciation Calculator", "Finance & Business",
 "Track a car's falling value year by year against any purchase price",
 "Depreciation is the biggest cost of car ownership and the only one no service plan ever itemizes. Enter the purchase price and how long you have held \u2014 or plan to hold \u2014 the car, and this calculator walks the value down with the classic steep first year and gentler ones after, then prices the total loss and the per-month burn.",
 "value = price \u00d7 0.85 \u00d7 0.9^(years \u2212 1); loss = price \u2212 value; monthly burn = loss \u00f7 (12 \u00d7 years)",
 "a $30,000 car holds $25,500 after year one and $16,730.55 by year five \u2014 $221.16 a month of quiet depreciation",
 ["new vs used purchase math","company car benefit checks","trade-in timing","lease residual sanity checks"],
 "The first year always hurts most, which is precisely why two-year-old one-owner cars are the used market's best value. Actual rates vary by brand; premium and EV models have run steeper recently.",
 "cd3",
 _f("cd3-p", "Purchase price", "30000") + _f("cd3-y", "Years held", "5") +
 '''<button class="btn" onclick="cd3()">Age the car</button>
  <div id="cd3-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV16:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA16[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'<div class="panel">{extra}{tail}</div>',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT16[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
