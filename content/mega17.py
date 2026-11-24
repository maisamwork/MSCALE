# -*- coding: utf-8 -*-
"""Batch 29 module B: 19 more flagship tools (housing, energy, investing)."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA17 = {}
CONTENT17 = {}

ADV17 = []

ADV17.append(("mortgage-refi-check", "Mortgage Refinance Check", "Finance & Business",
 "Break-even month and lifetime net benefit of refinancing",
 "Refinancing is a loan to buy a lower rate, and its whole case fits in three numbers: the new payment, the break-even month and the net benefit if you stay. Enter the balance, both rates, closing costs and your horizon, and this check answers the monthly saving, how many months the costs take to repay and what the move is worth in full.",
 "new pmt from the standard payment formula; breakeven = closing \u00f7 (old pmt \u2212 new pmt); net = saving \u00d7 months \u2212 closing",
 "$300,000 refinanced from 6.5% to 5.9% saves $116.79 a month \u2014 costs repaid in month 26, and $39,046 net if you ride the full 30 years",
 ["rate-drop opportunities","credit-score upgrade refinances","term-shortening moves","before jumping lenders"],
 "The break-even month only matters if you actually stay \u2014 moving or repaying before it erases the saving. Resetting to a fresh 30-year term can lower the payment while quietly raising the lifetime total.",
 "mr3",
 _f("mr3-l", "Loan balance", "300000") + _f("mr3-o", "Current rate (%)", "6.5") + _f("mr3-n", "New rate (%)", "5.9") + _f("mr3-c", "Closing costs", "3000") + _f("mr3-y", "Years remaining / new term", "30") +
 '''<button class="btn" onclick="mr3()">Check the refinance</button>
  <div id="mr3-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("electricity-rate-compare", "Electricity Rate Comparison", "Finance & Business",
 "Two tariffs priced across monthly use and contract length",
 "Tariff letters arrive marketing a few cents and bury the arithmetic, yet the arithmetic is only one multiplication. Enter your monthly usage and both rates, and this comparator answers the monthly spend on each, the annual difference, the contract-term total and the break-even usage at which the cheaper tariff flips sides.",
 "monthly = kWh \u00d7 rate; annual = monthly \u00d7 12; term = annual \u00d7 contract years",
 "400 kWh a month at rates of 0.18 versus 0.15 differs $12 a month \u2014 $144 a year and $1,008 across seven years",
 ["switching season checks","fixed vs variable tariffs","moving-house setup","solar feed-in sanity checks"],
 "Watch standing charges \u2014 a daily fee can erase a headline-rate saving on low usage. Exit fees belong in the comparison too: a locked-in small saving often loses to a flexible small loss.",
 "er2",
 _f("er2-k", "Monthly usage (kWh)", "400") + _f("er2-a", "Current rate ($/kWh)", "0.18") + _f("er2-b", "New rate ($/kWh)", "0.15") + _f("er2-y", "Contract years", "7") +
 '''<button class="btn" onclick="er2()">Compare the tariffs</button>
  <div id="er2-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("solar-payback", "Solar Payback Calculator", "Finance & Business",
 "Payback years and lifetime profit of a rooftop solar array",
 "Solar quotes sell headline wattage and hide the payback arithmetic, which is the only number that answers whether the panels are an investment or a roof decoration. Enter the gross cost, incentives, expected annual production and your electricity rate, and this calculator answers net cost, yearly saving, payback years and the profit over a 25-year life.",
 "net = cost \u00d7 (1 \u2212 incentive%); payback = net \u00f7 (production \u00d7 rate); profit = saving \u00d7 25 \u2212 net",
 "an $18,000 array cut to $12,600 net producing 9,000 kWh billed at 0.18 saves $1,620 a year \u2014 paid back in 7.8 years",
 ["quote evaluation","loan vs upfront comparison","battery add-on decisions","rental and new-build reviews"],
 "Degradation shadows everything: panels fade about 0.5% a year, so later years save slightly less. Export rates paid for surplus power sit far below import rates \u2014 size the array to self-consumption, not the roof.",
 "sp4",
 _f("sp4-c", "System cost", "18000") + _f("sp4-i", "Incentives (%)", "30") + _f("sp4-p", "Annual production (kWh)", "9000") + _f("sp4-r", "Electricity rate ($/kWh)", "0.18") +
 '''<button class="btn" onclick="sp4()">Find the payback</button>
  <div id="sp4-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("thermostat-savings", "Thermostat Savings Calculator", "Finance & Business",
 "What each degree of set-back returns over a heating season",
 "The engineer's rule \u2014 three percent per degree per eight-hour block \u2014 prices the thermostat dial directly, and almost nobody has ever run the sum. Enter the annual heating bill, the degrees you set back, the daily hours and the season length, and this calculator answers the season's saving, the share of the bill reclaimed and the per-degree rate.",
 "saving = bill \u00d7 3% \u00d7 degrees \u00d7 (hours \u00f7 24) \u00d7 (season months \u00f7 12)",
 "a $1,200-winter household that sets back four degrees for eight hours a day over five months keeps about $20",
 ["winter budgeting","programmable thermostat setup","landlord-tenant split decisions","heat-pump comparisons"],
 "The rule assumes an ordinary insulated home in a normal climate; a draughty hall rewrites it upward. Setbacks win most between night and the workday \u2014 not during the three evening hours you are actually home.",
 "th3",
 _f("th3-b", "Annual heating bill", "1200") + _f("th3-d", "Degrees set back (\u00b0F)", "4") + _f("th3-h", "Hours per day", "8") + _f("th3-m", "Season months", "5") +
 '''<button class="btn" onclick="th3()">Price the set-back</button>
  <div id="th3-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("water-heater-cost", "Water Heater Cost Calculator", "Finance & Business",
 "Daily and monthly energy cost of heating your hot water",
 "Hot water is the quiet line on the energy bill, priced by physics nobody writes down: gallons warmed, degrees of rise, and the delivery rate you pay. Enter daily gallons and temperature rise, and this calculator answers the daily kWh, the monthly cost at your rate and the yearly spend \u2014 enough to know whether shorter showers actually matter.",
 "kWh = gallons \u00d7 8.34 \u00d7 \u0394\u00b0F \u00f7 3412; monthly = kWh \u00d7 30 \u00d7 rate",
 "40 gallons heated 90\u00b0F warmer costs 8.79 kWh a day \u2014 about $42.19 a month at $0.16 per kWh",
 ["energy bill audits","tankless upgrade comparisons","off-peak heating schedules","rental utility splits"],
 "Recovering 90\u00b0F covers most winter use; cold-climate basements demand more. A family of four often runs double the 40-gallon figure, and sediment buildup quietly inflates every number \u2014 flush the tank yearly.",
 "wh3",
 _f("wh3-g", "Gallons per day", "40") + _f("wh3-t", "Temperature rise (\u00b0F)", "90") + _f("wh3-r", "Rate ($/kWh)", "0.16") +
 '''<button class="btn" onclick="wh3()">Cost the hot water</button>
  <div id="wh3-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("heating-oil-cost", "Heating Oil Cost Calculator", "Finance & Business",
 "Season cost and per-month burn from gallons and price per gallon",
 "Oil-heated households buy fuel by the delivery, so the seasonal reality hides behind single invoices. Enter the price per gallon, the deliveries you expect and the burn months, and this calculator answers each fill-up's cost, the seasonal total and the monthly budget line that spreads it evenly across winter.",
 "fill cost = gallons \u00d7 price; seasonal = gallons per season \u00d7 price; monthly total = seasonal \u00f7 burn months",
 "a 200-gallon order at $3.60 costs $720 \u2014 and a season burning 900 gallons, spread over six burn months, budgets $540 a month",
 ["pre-buy and budget-plan compare","delivery-timing decisions","oil vs heat-pump reviews","landlord utility budgeting"],
 "Price per gallon swings by 50 cents within a season, and pre-buy locks in whatever comes. Burn rates climb with wind exposure \u2014 temperature-adjusted guesses beat calendar guesses in hard winters.",
 "ho2",
 _f("ho2-g", "Gallons per delivery", "200") + _f("ho2-p", "Price per gallon", "3.60") + _f("ho2-s", "Gallons per season", "900") + _f("ho2-m", "Burn months", "6") +
 '''<button class="btn" onclick="ho2()">Budget the oil</button>
  <div id="ho2-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("meal-prep-cost", "Meal Prep Cost Calculator", "Finance & Business",
 "Per-serving cost of home cooking against bought lunches",
 "Every meal-prep brochure claims savings without arithmetic, so the arithmetic lives here. Enter the recipe cost, the number of servings and the bought alternative price, and this calculator answers the per-serving cost, the weekly and annual saving, and how many bought lunches the whole batch replaces at your weekday pace.",
 "per serving = recipe cost \u00f7 servings; weekly saving = (bought price \u2212 per serving) \u00d7 lunches replaced; annual = weekly \u00d7 48",
 "an $18 batch making 8 servings costs $2.25 each \u2014 against $11 bought lunches, five a week saves $2,100 by year end",
 ["salary-day budgeting","fitness nutrition plans","family lunchboxes","student budgets"],
 "Store batch recipes swap cost for monotony \u2014 plan two alternating preps weekly to survive the habit. Protein-heavy recipes swing the total most; dried pulses and frozen vegetables rarely move it.",
 "mc3",
 _f("mc3-r", "Recipe total cost", "18") + _f("mc3-s", "Servings per batch", "8") + _f("mc3-b", "Bought lunch price", "11") + _f("mc3-w", "Lunches per week", "5") +
 '''<button class="btn" onclick="mc3()">Price the prep</button>
  <div id="mc3-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("bulk-buy-savings", "Bulk Buy Savings Calculator", "Finance & Business",
 "Unit prices of small versus bulk packs with the honest verdict",
 "Bulk labels shout value and quietly break above a certain pack size, so the unit price stays king. Enter both pack sizes and prices, and this calculator answers the cost per unit of each, the percentage saved and \u2014 for the bulk pack \u2014 how many of the small ones it replaces, so storage reality can meet arithmetic.",
 "unit price = price \u00f7 units; saving = 1 \u2212 bulk_unit \u00f7 small_unit; equivalents = bulk_units \u00f7 small_units",
 "a $12 twelve-pack at $1.00 each versus a $40 case of fifty at $0.80 each saves 20% \u2014 if the fifty actually get used",
 ["warehouse club runs","pantry staples","co-op and group buys","freezer space decisions"],
 "Savings above 15\u201320% on staples are real; the cost is spoilage and cash tied up. Perishables bought big are savings theatre \u2014 only stable goods like rice, oil and detergent compound safely.",
 "bb2",
 _f("bb2-q1", "Small pack quantity", "12") + _f("bb2-p1", "Small pack price", "12") + _f("bb2-q2", "Bulk pack quantity", "50") + _f("bb2-p2", "Bulk pack price", "40") +
 '''<button class="btn" onclick="bb2()">Price the units</button>
  <div id="bb2-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("subscription-audit", "Subscription Audit", "Finance & Business",
 "Track, rank and total every recurring charge for the year",
 "Subscriptions are designed to be forgotten, and the forgotten ones are precisely where audits pay. Enter how many you hold, the monthly total and your honest estimate of unused ones, and this audit answers the annual cost, the share being burned on services you did not open, and what the cancellations put back into the month.",
 "annual = monthly \u00d7 12; waste = unused monthly \u00d7 12; reclaimed = cancelled \u00d7 12",
 "eleven services at $97 a month total $1,164 a year \u2014 and the two you have not opened since spring burn $312 of it",
 ["January and autumn money resets","shared household plans","app and media bundles","before a new sign-up"],
 "Most audits find one or two ghosts per household; the habit, not the list, is the fix. Cancel the week before renewal, not after \u2014 annual plans refund pro-rata on nobody's calendar.",
 "su3",
 _f("su3-n", "Subscriptions held", "11") + _f("su3-t", "Monthly total", "97") + _f("su3-u", "Monthly on unused ones", "26") + _f("su3-c", "Ready to cancel (count)", "3") +
 '''<button class="btn" onclick="su3()">Audit the charges</button>
  <div id="su3-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("annuity-payout", "Annuity Payout Calculator", "Finance & Business",
 "Monthly income a lump sum sustains, with interest and principal split",
 "A lifetime of savings converts to an income stream by one formula, and the split between returned principal and earned interest is the part people misread. Enter the balance, the annual rate and the years of payout, and this calculator answers the monthly payment, the total paid out and how much of it was your principal under a new name.",
 "pmt = P \u00d7 i \u00f7 (1 \u2212 (1 + i)^\u2212n) with i = rate/12, n = years \u00d7 12; interest = pmt \u00d7 n \u2212 P",
 "$500,000 paying out at 5% for 20 years sustains $3,299.78 a month \u2014 $291,947.53 of the total is interest doing the chauffeuring",
 ["retirement drawdown planning","lottery and settlement decisions","pension buyout comparisons","trust planning"],
 "Longer payouts lower the monthly but raise the interest share \u2014 the same balance ends up paying much more over 25 years. These are ordinary payments; life-annuity products add mortality credits that change the numbers.",
 "an3",
 _f("an3-p", "Lump sum", "500000") + _f("an3-r", "Annual rate (%)", "5") + _f("an3-y", "Payout years", "20") +
 '''<button class="btn" onclick="an3()">Size the income</button>
  <div id="an3-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("bond-price-yield", "Bond Price & Yield", "Finance & Business",
 "Price a bond from coupon, yield and term \u2014 premium or discount",
 "Bond prices move opposite to yields, a rule quoted everywhere and computed almost nowhere. Enter the face value, the coupon rate, the market yield and the years to maturity, and this calculator discounts every coupon and the principal back to today's price, then states plainly whether you are paying a premium or buying at a discount.",
 "price = \u03a3 coupon / (1 + y)^t + face / (1 + y)^n for t = 1\u2026n",
 "5% coupons ten years out discounted to a 4% yield price at $1,081.11 \u2014 an 8.1% premium, because the coupon beats the market",
 ["rate-change preparation","secondary-market comparisons","portfolio income planning","exam and interview prep"],
 "When market yield equals the coupon the price is exactly face \u2014 everything above or below is discounting at work. Quoted prices ignore accrued interest, which the settlement invoice adds between coupon dates.",
 "bp3",
 _f("bp3-f", "Face value", "1000") + _f("bp3-c", "Coupon rate (%)", "5") + _f("bp3-y", "Market yield (%)", "4") + _f("bp3-n", "Years to maturity", "10") +
 '''<button class="btn" onclick="bp3()">Price the bond</button>
  <div id="bp3-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("dividend-yield", "Dividend Yield Calculator", "Finance & Business",
 "Yield on cost from share price, dividend and holdings",
 "Dividend yield looks like a stock statistic and behaves like a market-price echo \u2014 it moves when the price moves, even if the dividend never changes. Enter the annual dividend per share, the current price and how many shares you hold, and this calculator answers the yield, your quarterly and monthly income, and the cash the position produces.",
 "yield = annual dividend \u00f7 share price \u00d7 100; income = dividend \u00d7 shares",
 "$2.40 a year on a $48 share yields 5% \u2014 and a 300-share position pays $720 a year, $180 a quarter",
 ["income portfolio checks","retirement income planning","dividend-growth tracking","yield-trap screening"],
 "Screaming yields usually scream dividend cuts \u2014 screen the payout ratio before celebrating. Companies pay quarterly in the US and twice yearly in much of Europe, which changes the cash calendar though not the total.",
 "dy2",
 _f("dy2-d", "Annual dividend per share", "2.40") + _f("dy2-p", "Share price", "48") + _f("dy2-s", "Shares held", "300") +
 '''<button class="btn" onclick="dy2()">Yield the income</button>
  <div id="dy2-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("payout-ratio", "Payout Ratio Calculator", "Finance & Business",
 "How much of every earned dollar the company mails away",
 "The payout ratio decides whether a dividend can survive a bad year, and it is two numbers nobody puts on the marketing page. Enter the earnings per share and the dividend per share, and this calculator answers the ratio, the retained slice, and reads the result against the classic bands \u2014 sustainable, stretched or unsustainable.",
 "payout ratio = DPS \u00f7 EPS \u00d7 100; retained = 1 \u2212 payout",
 "$1.80 paid from $4.50 earned is a 40% payout \u2014 over half the profit retained for reinvestment, the classic sustainable band",
 ["dividend safety checks","stock comparison screens","income fund reviews","equity analyst basics"],
 "Below 30% means the dividend barely uses earnings and can grow; above 80% any earnings dip threatens the cheque. Mature utilities run high by design \u2014 compare within sector, not across the whole market.",
 "pr2",
 _f("pr2-e", "Earnings per share", "4.50") + _f("pr2-d", "Dividend per share", "1.80") +
 '''<button class="btn" onclick="pr2()">Judge the payout</button>
  <div id="pr2-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("pe-ratio-explainer", "P/E Ratio Explainer", "Finance & Business",
 "Price to earnings with the earnings-yield translation included",
 "The price-to-earnings ratio is the market's first sentence about any stock and the one most quoted with the least context. Enter the share price and the earnings per share, and this explainer answers the multiple, its earnings-yield translation \u2014 the inverse, in percent \u2014 and the price implied by your own target multiple.",
 "P/E = price \u00f7 EPS; earnings yield = EPS \u00f7 price \u00d7 100 = 1 \u00f7 (P/E); implied price = EPS \u00d7 target multiple",
 "a $48 price on $3.20 of earnings is a 15\u00d7 multiple \u2014 a 6.7% earnings yield, better than many bond coupons before growth",
 ["stock screening","market-context gauging","growth vs value debates","fund fact-sheet decoding"],
 "A P/E without the sector, growth rate and debt beside it is a number in a vacuum \u2014 15\u00d7 is cheap for software and dear for a steel mill. Negative earnings make the ratio meaningless; switch to price against sales.",
 "pe3",
 _f("pe3-p", "Share price", "48") + _f("pe3-e", "Earnings per share", "3.20") + _f("pe3-t", "Target multiple (optional)", "15") +
 '''<button class="btn" onclick="pe3()">Read the multiple</button>
  <div id="pe3-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("market-cap", "Market Cap Calculator", "Finance & Business",
 "Company size in one multiplication, with the size bands named",
 "Market capitalization is a single multiplication that decides which indexes a company joins, who can buy it and how violently it can move. Enter the share price and the shares outstanding, and this calculator answers the value, names the size band from mega down to micro, and shows what one percent of the company costs.",
 "market cap = share price \u00d7 shares outstanding; bands from mega (\u2265$200bn) down to micro",
 "500 million shares at $42 make $21 billion \u2014 a large-cap that tilts an index but cannot dominate it",
 ["index eligibility checks","stock comparison baselines","takeover speculation sizing","fund concentration checks"],
 "Share price alone means nothing without the count \u2014 a $500 stock can be smaller than a $6 one. Buybacks and new issues move the cap monthly, which is why screens pin a date to every figure.",
 "mk2",
 _f("mk2-p", "Share price", "42") + _f("mk2-s", "Shares outstanding (millions)", "500") +
 '''<button class="btn" onclick="mk2()">Size the company</button>
  <div id="mk2-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("beta-calculator", "Beta Calculator", "Finance & Business",
 "Stock sensitivity computed from covariance versus market variance",
 "Beta compresses a stock's whole relationship with the market into one slope, and slope is the whole story: above one it amplifies, below one it absorbs. Enter the covariance of the stock with the market and the market's variance, and this calculator answers the beta, names the profile from defensive to aggressive, and translates it into an expected move per market percent.",
 "beta = covariance \u00f7 variance; expected move = market move \u00d7 beta",
 "a covariance of 0.0004 against market variance 0.0008 gives beta 0.5 \u2014 a 2% market day is expected to move this stock 1%",
 ["portfolio risk budgeting","hedge ratio setup","CAPM cost-of-equity inputs","fund risk disclosure reading"],
 "Beta is a historian, not a prophet \u2014 it describes the past window and can flip after regime changes. Leveraged stocks drift upward in beta; utilities sink below one for boring, structural reasons.",
 "bt3",
 _f("bt3-c", "Covariance (stock, market)", "0.0004") + _f("bt3-v", "Market variance", "0.0008") + _f("bt3-m", "Expected market move (%)", "2") +
 '''<button class="btn" onclick="bt3()">Compute the beta</button>
  <div id="bt3-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("position-size", "Position Size Calculator", "Finance & Business",
 "Shares to buy from risk budget, entry and stop \u2014 not gut feeling",
 "Professional traders decide position size before they decide to trade; amateurs do it after, which is how one trade becomes the account. Enter the account size, the percent you risk per position, the entry price and the stop, and this calculator answers the dollar risk, the exact share count and the cash the position will consume.",
 "risk $ = account \u00d7 risk%; shares = risk $ \u00f7 (entry \u2212 stop); position value = shares \u00d7 entry",
 "a $25,000 account risking 2% with entry $50 and stop $47.50 risks $500 \u2014 exactly 200 shares, $10,000 deployed",
 ["day-trading discipline","swing-trade sizing","backtesting position rules","prop-firm risk compliance"],
 "If the share count feels small, widen nothing \u2014 the risk budget is the input you never move. Gaps through stops make real losses larger than planned, which is why the budget stays a fraction, never a half.",
 "ps3",
 _f("ps3-a", "Account size", "25000") + _f("ps3-r", "Risk per trade (%)", "2") + _f("ps3-e", "Entry price", "50") + _f("ps3-s", "Stop price", "47.50") +
 '''<button class="btn" onclick="ps3()">Size the position</button>
  <div id="ps3-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("risk-reward", "Risk Reward Calculator", "Finance & Business",
 "Trade quality as a ratio between target and stop distance",
 "Win rate gets the headlines and the risk-reward ratio decides the account, because 40% winners at 1-to-3 print money while 70% winners at 1-to-0.5 bleed it. Enter entry, stop and target prices, and this calculator answers both dollar distances, the ratio, and the minimum win rate that makes the plan profitable.",
 "risk = entry \u2212 stop; reward = target \u2212 entry; ratio = reward \u00f7 risk; breakeven win% = 1 \u00f7 (1 + ratio)",
 "buy at 100 with a 97 stop and a 112 target risks $3 to make $12 \u2014 1:4, which pays even when you lose four of five",
 ["trade plan writing","options position structuring","stop and target placement","journal review scoring"],
 "The ratio assumes you honor the stop \u2014 widening it silently rewrites the arithmetic to something worse. Targets beyond obvious resistance levels are wishes; place them where the market actually pauses.",
 "rr2",
 _f("rr2-e", "Entry price", "100") + _f("rr2-s", "Stop price", "97") + _f("rr2-t", "Target price", "112") +
 '''<button class="btn" onclick="rr2()">Rate the trade</button>
  <div id="rr2-out" class="result" aria-live="polite"></div>'''))

ADV17.append(("kelly-criterion", "Kelly Criterion Calculator", "Finance & Business",
 "Mathematically optimal bet size from odds and win probability",
 "The Kelly criterion answers the only sizing question with a provable answer: what fraction of the bankroll maximizes long-run growth without certain ruin. Enter the win probability and the win-to-loss odds, and this calculator answers the full Kelly fraction, the half-Kelly professionals actually use, and what the same bet would stake in dollars.",
 "f* = (bp \u2212 q) \u00f7 b with b = win/loss ratio, p = win probability, q = 1 \u2212 p",
 "a 55% shot paying even money gives f* = 10% of the bankroll \u2014 $500 of $5,000 at full Kelly, $250 on half-Kelly",
 ["blackjack and poker staking","systematic trading sizing","betting bankroll management","teaching expected value"],
 "Kelly assumes you know the true probability \u2014 nobody does \u2014 and punishes overestimation with ruin, not merely loss. Half-Kelly gives up a sliver of growth for most of the variance reduction, which is why professionals pay that price.",
 "ke3",
 _f("ke3-p", "Win probability (%)", "55") + _f("ke3-b", "Win/loss payout ratio", "1") + _f("ke3-a", "Bankroll amount", "5000") +
 '''<button class="btn" onclick="ke3()">Stake the bet</button>
  <div id="ke3-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV17:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA17[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'<div class="panel">{extra}{tail}</div>',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT17[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
