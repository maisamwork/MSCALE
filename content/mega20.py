# -*- coding: utf-8 -*-
"""Batch 30 module A: 18 flagship tools (finance, work, planning)."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA20 = {}
CONTENT20 = {}

ADV20 = []

ADV20.append(("rule-of-72", "Rule of 72 Calculator", "Finance & Business",
 "How many years it takes money to double at any growth rate",
 "The Rule of 72 is the fastest mental-math shortcut in finance: divide 72 by an annual growth rate and you get roughly the number of years it takes money to double. Enter any rate and this calculator gives the shortcut answer, the exact compound-math answer, and where the rule starts to fray so you know when to trust it and when to do the real arithmetic.",
 "years to double = 72 / rate; exact years = ln(2) / ln(1 + rate/100)",
 "at an 8% return, 72 divided by 8 says 9.0 years \u2014 the exact compound answer is 9.01 years, so the shortcut is spot on",
 ["quick investment sanity checks", "inflation impact estimates", "comparing fund fees", "explaining compounding to beginners"],
 "The rule is excellent within 4% to 12% annual rates, drifting a few months off at the edges. Beyond that range the exact logarithm matters \u2014 this calculator always shows both.",
 "w01",
 _f("w01-a", "Annual growth or inflation rate (%)", "8") +
 '''<button class="btn" onclick="w01()">Apply the rule</button>
  <div id="w01-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("future-value-annuity", "Future Value of Annuity Calculator", "Finance & Business",
 "What steady monthly deposits grow into with compounding, split from what you contribute",
 "A pile of small deposits behaves nothing like one big deposit, and the difference is interest working month after month. Enter the deposit, the annual return and the years, and this calculator totals the future balance, splits it honestly into money you put in versus money the market added, and shows what percentage of the finish line your discipline alone crossed.",
 "FV = deposit \u00d7 ((1 + r)^n \u2212 1) / r with r = annual rate / 12, n = years \u00d7 12",
 "a $250 monthly deposit at 5% for 10 years reaches $38,820 \u2014 $30,000 of it is contributions and $8,820 is growth, 22.7% of the total",
 ["retirement contribution planning", "college savings targets", "comparing deposit amounts", "savings automation decisions"],
 "The figures assume deposits land at the end of each month and the return compounds monthly \u2014 real funds wobble around that average, sometimes badly. Fees are the silent counterparty: a 1% expense ratio on this account can eat a sixth of the growth shown.",
 "w02",
 _f("w02-a", "Monthly deposit", "250") + _f("w02-b", "Expected annual return (%)", "5") + _f("w02-c", "Years of deposits", "10") +
 '''<button class="btn" onclick="w02()">Project the growth</button>
  <div id="w02-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("present-value", "Present Value Calculator", "Finance & Business",
 "What a future lump sum is actually worth in today's money",
 "A dollar promised ten years from now is not a dollar today, and every settlement, pension quote and deferred bonus hides behind that gap. Enter the future amount, your discount rate and the wait, and this calculator answers the honest today-value, what each future dollar costs you, and the waiting period that halves it.",
 "PV = future amount / (1 + rate)^years",
 "a $50,000 payout due in 10 years discounted at 7% is worth $25,417 today \u2014 each future dollar costs 51 cents",
 ["settlement and pension evaluations", "lottery lump-sum decisions", "deferred compensation comparisons", "bond price sanity checks"],
 "Pick the discount rate to match your realistic alternative \u2014 what the same money could earn elsewhere after tax. A too-low rate flatters distant promises, which is exactly how deferred-commission plans look magical on paper.",
 "w03",
 _f("w03-a", "Future amount", "50000") + _f("w03-b", "Discount rate per year (%)", "7") + _f("w03-c", "Years until paid", "10") +
 '''<button class="btn" onclick="w03()">Discount it</button>
  <div id="w03-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("inflation-adjusted-value", "Inflation Adjusted Value Calculator", "Finance & Business",
 "What today's money will really buy after years of inflation",
 "Inflation is a slow leak in every wallet and a permanent tax on cash under the mattress. Enter an amount, an inflation rate and a time horizon, and this calculator answers what the money will buy later, how much of its power quietly disappears, and the amount you would need then to match today's lifestyle.",
 "real value = amount / (1 + inflation)^years; future cost = amount \u00d7 (1 + inflation)^years",
 "$1,000 of cash after 10 years at 3% inflation buys what $744.09 buys today \u2014 replacing that lifestyle takes $1,343.92",
 ["salary negotiation anchors", "pension adequacy checks", "cash savings decisions", "long-term contract pricing"],
 "Three percent is a planning average, not a promise \u2014 recent history includes years above eight. Real returns beat nominal ones only if your income rises with prices; fixed pensions and fixed rents quietly fail that test every single year.",
 "w04",
 _f("w04-a", "Amount today", "1000") + _f("w04-b", "Inflation rate per year (%)", "3") + _f("w04-c", "Years ahead", "10") +
 '''<button class="btn" onclick="w04()">Deflate the cash</button>
  <div id="w04-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("roi-annualizer", "ROI Annualizer Calculator", "Finance & Business",
 "Total return on any project annualized into a comparable yearly rate",
 "A 30% return in eight months and 30% in eight years are letters apart in quality, yet people quote both as 30% ROI. Enter what went in, what came out and the holding time, and this calculator states the total return, the annualized equivalent, and how the figure stacks against a plain index fund year.",
 "total ROI = (out \u2212 in) / in; annualized = (1 + ROI)^(12 / months) \u2212 1",
 "$20,000 in and $26,000 out eight months later is 30% total \u2014 annualized to 48.2%, comfortably above a 7% index year",
 ["project and campaign reviews", "flip and resale deals", "course and equipment buys", "side-business evaluations"],
 "Annualizing short windows amplifies luck \u2014 a great nine months can read as a heroic yearly rate nobody sustains. Compare against your true alternative including taxes and effort, and treat sub-annual results as a signal, not a promise.",
 "w05",
 _f("w05-a", "Money in", "20000") + _f("w05-b", "Money out", "26000") + _f("w05-c", "Months held", "8") +
 '''<button class="btn" onclick="w05()">Annualize the return</button>
  <div id="w05-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("margin-percentage", "Gross Margin Calculator", "Finance & Business",
 "Margin, markup and profit split apart on any price and cost",
 "Margin and markup get swapped constantly, and the swap quietly overprices or underprices everything from freelance quotes to shop shelves. Enter the revenue and the direct costs, and this calculator answers gross profit, margin as a share of price, markup as a share of cost, and the price floor where the job stops paying you.",
 "margin = (revenue \u2212 cost) / revenue; markup = (revenue \u2212 cost) / cost",
 "$12,000 of revenue against $7,800 of direct costs is $4,200 gross \u2014 a 35% margin that is a 53.85% markup on cost",
 ["quoting freelance work", "retail pricing decisions", "product line reviews", "profit leakage checks"],
 "Most service businesses need a 40% to 60% gross margin to survive overhead, taxes and unpaid admin time. Track margin per project, not per year \u2014 annual averages hide exactly the loss-making jobs you need to spot early.",
 "w06",
 _f("w06-a", "Revenue", "12000") + _f("w06-b", "Direct costs", "7800") +
 '''<button class="btn" onclick="w06()">Split margin and markup</button>
  <div id="w06-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("sales-tax-reverse", "Reverse Sales Tax Calculator", "Finance & Business",
 "The pre-tax price hiding inside any tax-inclusive receipt",
 "Tax-inclusive pricing is the norm in dozens of countries, which makes the shelf price a puzzle: how much of what you paid was ever the seller's money? Enter the receipt total and the rate, and this calculator extracts the true pre-tax price, the exact tax portion, and the miscue people make by subtracting the percentage off the top.",
 "pre-tax = total / (1 + rate/100); tax = total \u2212 pre-tax",
 "a $424 receipt at a 6% rate holds a $400 pre-tax price and $24 of tax \u2014 not $424 \u2212 6%, which is the classic miscue",
 ["VAT invoice checks", "resale claim preparation", "expense report reconciliations", "price-setting math"],
 "The error is directional: subtracting the rate from the total under-recovers tax every time, and the gap grows with the rate \u2014 at 20% the miscue passes a full percent of the receipt. Accounting software divides; so does this tool.",
 "w07",
 _f("w07-a", "Tax-inclusive total", "424") + _f("w07-b", "Tax rate (%)", "6") +
 '''<button class="btn" onclick="w07()">Strip the tax out</button>
  <div id="w07-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("salary-to-hourly", "Salary to Hourly Calculator", "Finance & Business",
 "The real hourly rate behind any annual salary, overtime included",
 "Salaried pay hides its hourly price, and the hiding is worst exactly when hours creep past contract. Enter the salary, contracted hours and your realistic weekly total, and this calculator answers the on-paper rate, the true rate with overtime unpaid, and what each extra unpaid hour per week actually costs across a year.",
 "hourly = annual / (contracted hours \u00d7 weeks); true rate = annual / (real hours \u00d7 weeks)",
 "a $52,000 salary on a 40-hour contract is $25.00 an hour \u2014 regularly working 45 makes the true rate $22.22",
 ["job offer comparisons", "part-time conversion talks", "burnout cost checks", "hourly consulting baselines"],
 "The on-paper rate only survives if hours do, so log a typical month before quoting it anywhere. Salaried roles with regular 50-hour weeks pay materially less per hour than the contract says \u2014 this is the number to negotiate against, not the headline.",
 "w08",
 _f("w08-a", "Annual salary", "52000") + _f("w08-b", "Contracted hours per week", "40") + _f("w08-c", "Realistic hours per week", "45") +
 '''<button class="btn" onclick="w08()">Reveal the rate</button>
  <div id="w08-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("contract-vs-permanent", "Contract vs Permanent Calculator", "Finance & Business",
 "Freelance hourly against salaried pay with overhead honesty included",
 "Contract hourly rates look enormous set beside salary equivalents, and the comparison flatters them until overhead, unpaid weeks and self-funded benefits get their turn. Enter the contract rate, realistic billable hours and weeks, your overhead share and the salary on offer, and this calculator totals both paths and finds the contract rate where the two truly break even.",
 "contract net = rate \u00d7 hours \u00d7 weeks \u00d7 (1 \u2212 overhead); break-even rate = salary / (hours \u00d7 weeks \u00d7 (1 \u2212 overhead))",
 "$65 an hour for 35 billable hours across 46 weeks with 30% overhead nets $73,255 \u2014 short of a $95,000 salary, so the break-even rate is $84.29",
 ["accepting a contract offer", "setting freelance rates", "consulting-to-staff moves", "agency margin checks"],
 "Overhead is not a punishment \u2014 it is your pension, sick pay, equipment and the quarter of the year you spend selling instead of billing. Anyone quoting a rate without that haircut is comparing their best week to a salaried worst month.",
 "w09",
 _f("w09-a", "Contract hourly rate", "65") + _f("w09-b", "Billable hours per week", "35") + _f("w09-c", "Billable weeks per year", "46") + _f("w09-d", "Overhead share (%)", "30") + _f("w09-e", "Permanent salary on offer", "95000") +
 '''<button class="btn" onclick="w09()">Weigh both paths</button>
  <div id="w09-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("day-rate-calculator", "Day Rate Calculator", "Finance & Business",
 "A defensible freelance day rate from salary, overhead and billable days",
 "Day rates get hand-waved in both directions \u2014 too low to fund a business, too high to win work. Enter the salary you need to match, your overhead and the realistic number of billable days per year, and this calculator answers the day rate that keeps you whole, with half-day and weekly figures for quoting convenience.",
 "day rate = salary \u00d7 (1 + overhead) / billable days",
 "a $68,000 salary with 30% overhead across 200 real billable days needs a $442 day rate \u2014 $491.11 if you only sell 180",
 ["freelance quoting", "agency subcontract budgets", "sabbatical bridge planning", "client day-rate negotiations"],
 "Billable days is the honest denominator: a 250-day work year sells far fewer days once sales, invoices and admin take their share. Track your real sold days for a quarter before trusting any default.",
 "w10",
 _f("w10-a", "Salary to match", "68000") + _f("w10-b", "Overhead (%)", "30") + _f("w10-c", "Billable days per year", "200") +
 '''<button class="btn" onclick="w10()">Price the day</button>
  <div id="w10-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("overtime-hours-tracker", "Overtime Hours Pay Tracker", "Finance & Business",
 "Weekly pay with an overtime premium shown as its own line",
 "Overtime is the most policy-dependent pay in any workplace, and it is still computed on napkins in every break room. Enter straight hours, overtime hours, the base rate and the premium multiplier, and this tracker totals the week, shows what share of pay the premium added, and prices a year of the same week for planning purposes.",
 "pay = hours \u00d7 rate + OT hours \u00d7 rate \u00d7 multiplier",
 "40 straight hours plus 7 at time-and-a-half on $22 pays $1,111 \u2014 the $231 premium is 20.8% of the weekly total",
 ["weekly budget cashflow", "shift-pattern comparisons", "second-job decisions", "overtime ban impact checks"],
 "Whether overtime is one-and-a-half or double is set by law and contract, not habit \u2014 flat-rate overtime at regular pay is illegal for most non-exempt staff. Voluntary bans hurt fastest for those trading overtime for fixed bills.",
 "w11",
 _f("w11-a", "Straight-time hours", "40") + _f("w11-b", "Overtime hours", "7") + _f("w11-c", "Base hourly rate", "22") + _sel("w11-d", "Overtime multiplier", [("1.5", "Time and a half"), ("2", "Double time"), ("1", "Flat \u2014 regular rate")]) +
 '''<button class="btn" onclick="w11()">Total the week</button>
  <div id="w11-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("mileage-log", "Mileage Log Value Calculator", "Finance & Business",
 "What a year of business miles is worth at approved rates",
 "Business miles are one of the few tax-free income streams you have to track yourself, and untracked miles are donated to the tax office. Enter the business miles driven and the approved per-mile rates, and this calculator totals the claim at the full rate, at a fuel-only rate, and prices a typical year so you can see what skipping the log costs.",
 "claim = miles \u00d7 full rate; fuel-only claim = miles \u00d7 fuel rate",
 "2,150 business miles at $0.67 claim $1,440.50 \u2014 logged at a fuel-only $0.30 they would lose $645 of value",
 ["self-employed tax deductions", "reimbursement claims", "charity drive records", "vehicle cost allocation"],
 "Mileage logs survive audits when they are contemporaneous \u2014 a reconstructed log is a weaker document than a spreadsheet you filled at the week's end. Keep odometer photos at year boundaries; they resolve disputes in minutes.",
 "w12",
 _f("w12-a", "Business miles", "2150") + _f("w12-b", "Full rate per mile", "0.67") + _f("w12-c", "Fuel-only rate per mile", "0.30") +
 '''<button class="btn" onclick="w12()">Value the miles</button>
  <div id="w12-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("redundancy-pay", "Statutory Redundancy Pay Calculator", "Finance & Business",
 "UK statutory redundancy from age, service years and capped weekly pay",
 "UK statutory redundancy pay follows an age-weighted formula that surprises almost everyone who meets it first at a termination meeting. Enter your weekly pay, your age and full years of service, and this calculator walks the statutory table year by year \u2014 half a week under 22, one week from 22 to 40, one and a half beyond \u2014 and caps the service years as the law does.",
 "weeks = sum over service years of (0.5 if under 22, 1 if 22\u201340, 1.5 if 41+), capped at 20 years; pay = weeks \u00d7 weekly pay",
 "a 36-year-old with seven full years on a capped $719 week collects 7 weeks \u2014 $5,033",
 ["redundancy letter checks", "settlement negotiations", "financial buffer planning", "HR compliance checks"],
 "The weekly-pay cap and age bands change by tax year, so verify the current cap before final numbers. Enhanced contractual schemes often exceed statutory \u2014 and a settlement agreement may trade a bit more cash for waiving claims, which deserves independent advice.",
 "w13",
 _f("w13-a", "Weekly pay (statutory cap)", "719") + _f("w13-b", "Age", "36") + _f("w13-c", "Full years of service", "7") +
 '''<button class="btn" onclick="w13()">Apply the table</button>
  <div id="w13-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("job-offer-comparer", "Job Offer Comparer", "Finance & Business",
 "Two offers compared after benefits and the commute get their say",
 "Offers get compared on salary alone, then the commute, benefits and flexibility remix the verdict months later. Enter both salaries, each benefits package and each commute or setup cost, and this comparer totals the true yearly value of both offers and names the winner.",
 "true value = salary + benefits \u2212 annual commute / setup costs",
 "a $92,000 role with $4,000 of benefits and $3,200 of commuting nets $92,800 \u2014 the $88,000 offer with $9,000 of benefits and a $1,200 setup reaches $95,800, a $3,000 win for the smaller salary",
 ["comparing offers", "remote-work position checks", "internal transfer decisions", "raise-versus-move talks"],
 "Value benefits at what you will actually use \u2014 a gym you never visit is not compensation. Commuting costs more than tickets \u2014 time is the bigger invoice, and remote offers priced at half your hourly rate win outright.",
 "w14",
 _f("w14-a", "Offer A salary", "92000") + _f("w14-b", "Offer A benefits value", "4000") + _f("w14-c", "Offer A annual commute cost", "3200") + _f("w14-d", "Offer B salary", "88000") + _f("w14-e", "Offer B benefits value", "9000") + _f("w14-f", "Offer B annual setup cost", "1200") +
 '''<button class="btn" onclick="w14()">Compare the offers</button>
  <div id="w14-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("round-robin-scheduler", "Round Robin Scheduler", "Finance & Business",
 "Every pairing needed so all teams meet exactly once",
 "League tables, mentoring circles and tasting flights all run on round robins, and the arithmetic of pairings is a classic counting exercise. Enter the team or participant count and the format, and this scheduler answers the rounds required, matches per round, total matches, and what a home-and-away double format does to the calendar.",
 "matches = n \u00d7 (n \u2212 1) / 2; rounds = n \u2212 1 for even n, n for odd n with a bye",
 "8 teams produce 28 matches across 7 rounds \u2014 4 games every round, and doubling the format makes 56 fixtures",
 ["league planning", "tournament scheduling", "mentor pairing programs", "tasting or product rotation nights"],
 "With an odd count the bye round is not wasted idle time \u2014 it is the perfect slot for catch-up fixtures or officials' rest. Double round robins multiply the fixture list by two and guarantee every pairing visits both venues.",
 "w15",
 _f("w15-a", "Teams or participants", "8") + _sel("w15-e", "Format", [("1", "Single \u2014 each meets once"), ("2", "Double \u2014 home and away")]) +
 '''<button class="btn" onclick="w15()">Draw the schedule</button>
  <div id="w15-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("skill-matrix", "Team Skill Matrix Calculator", "Finance & Business",
 "Coverage depth, gaps and single-person risks across a team's skills",
 "A team's strength is not its best individual \u2014 it is what keeps working when any one person is out. Enter the team size, the skills you track, average proficiency and how many skills only one person can do, and this matrix grades coverage, flags bus-factor risks, and sizes the cross-training queue.",
 "coverage = average proficiency / 5 \u00d7 100; risk count = skills with a single holder",
 "six engineers across five skills averaging 3 out of 5 cover 60% \u2014 with one single-holder skill, cross-training is overdue",
 ["team health reviews", "hiring gap analysis", "on-call rota planning", "promotion case building"],
 "Bus factor is the quiet killer: one resignation removes whole capability slices overnight. Aim for at least two competent holders per critical skill before chasing shiny new ones \u2014 depth first, breadth close behind.",
 "w16",
 _f("w16-a", "Team size", "6") + _f("w16-b", "Skills tracked", "5") + _f("w16-c", "Average proficiency (1\u20135)", "3") + _f("w16-d", "Skills only one person holds", "1") +
 '''<button class="btn" onclick="w16()">Grade the coverage</button>
  <div id="w16-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("task-quadrant-sorter", "Task Quadrant Sorter", "Finance & Business",
 "Your task list sorted into the four Eisenhower quadrants with honest totals",
 "Every to-do list is a priority argument in disguise, and most lists lose the argument by lunchtime. Enter how many tasks fall in each Eisenhower quadrant \u2014 do, schedule, delegate, drop \u2014 and this sorter totals the load, shows the quadrant where your time actually goes, and prices the reclaim from dropping or delegating the bottom half.",
 "share = quadrant count / total \u00d7 100; reclaim = drop + delegate tasks",
 "nineteen tasks split do 4 / schedule 7 / delegate 3 / drop 5 \u2014 42% of the list never needed you personally",
 ["weekly planning", "inbox and backlog triage", "delegate-and-freedom reviews", "burnout prevention"],
 "The schedule quadrant is where careers compound \u2014 important work without deadlines always loses today's fight to urgent noise. If your drop quadrant stays near zero, the list is trusted too much, not worked well enough.",
 "w17",
 _f("w17-a", "Urgent + important (do)", "4") + _f("w17-b", "Important, not urgent (schedule)", "7") + _f("w17-c", "Urgent, not important (delegate)", "3") + _f("w17-d", "Neither (drop)", "5") +
 '''<button class="btn" onclick="w17()">Sort the list</button>
  <div id="w17-out" class="result" aria-live="polite"></div>'''))

ADV20.append(("weekly-hours-planner", "Weekly Hours Planner", "Finance & Business",
 "168 hours honestly split across sleep, work, commute and care",
 "A week holds exactly 168 hours, and most people can name neither where they go nor what remains. Enter sleep, work, commuting and recurring chores per week, and this planner totals the committed hours, answers what free time actually remains per day, and prices what one reclaimed hour a day becomes across a year.",
 "free = 168 \u2212 committed; free per day = free / 7; yearly = one daily hour \u00d7 365",
 "sleep 56, work 45, commute 7.5 and chores 14 leave 45.5 free hours \u2014 6.5 a day, and one reclaimed hour daily is 365 hours a year",
 ["time audits", "commute decisions", "part-time study plans", "care-burden reviews"],
 "The planner counts hours, not quality \u2014 forty fragmented minutes feel poorer than one clean evening. Reclaiming a single recurring hour weekly is usually easier than finding a free day, and it compounds the same way money does.",
 "w18",
 _f("w18-a", "Sleep per week (hours)", "56") + _f("w18-b", "Work per week", "45") + _f("w18-c", "Commute per week", "7.5") + _f("w18-d", "Recurring chores per week", "14") +
 '''<button class="btn" onclick="w18()">Budget the week</button>
  <div id="w18-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV20:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA20[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'<div class="panel">{extra}{tail}</div>',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT20[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
