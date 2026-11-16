# Batch 2: discount-calculator, tip-calculator, compound-interest-calculator, gst-vat-calculator
CONTENT = {
"discount-calculator": {
"intro": [
"Sale signs are designed to be exciting, and excitement is bad arithmetic. A 40 percent off label on an inflated original price, a stacked discount applied in the wrong order, or a final tax added at the till can all change what you actually pay. This Discount Calculator works out the real numbers: the discount amount, the final price, and the total with sales tax if you need it.",
"Enter the original price and the percentage off, and the tool instantly shows how much you save and what you will pay. Add your local sales tax or VAT rate and it calculates the true out-the-door price, which is the number that matters when you are comparing offers or staying inside a budget.",
"The calculator is useful for everyday shopping, seasonal sales, negotiating on big purchases, small businesses pricing clearance stock, and anyone who has ever stood in an aisle wondering whether the deal is as good as it looks. It runs entirely in your browser, so you can check prices discreetly while you shop.",
],
"how": [
"The calculator needs only a price and a discount percentage to produce its main results. The tax field is optional and defaults to zero, so you can ignore it for pre-tax comparisons. Everything updates as you type, and you can edit values repeatedly to compare scenarios.",
],
"steps": [
"Enter the original price of the item.",
"Type the discount percentage, for example 25 for 25 percent off.",
"Optionally enter your sales tax or VAT rate to see the final price with tax.",
"Read the discount amount, the sale price before tax, and the total with tax.",
"Change the percentage to compare offers, for example 20 percent off versus 15 off with a coupon.",
],
"works": [
"The core calculation is straightforward. The discount amount equals the original price multiplied by the discount percentage divided by 100. The sale price is the original price minus the discount. On an item priced at 80 with 25 percent off, the discount is 20 and the sale price is 60.",
"When a tax rate is provided, the tool multiplies the sale price by one plus the tax rate. A 60 sale price with 8 percent tax becomes 60 x 1.08 = 64.80. Tax is applied after the discount because, in most retail systems, tax is charged on the amount actually paid, not on the original ticket price.",
"Stacked discounts deserve a note because they are widely misunderstood. When a store applies 20 percent off and then a further 10 percent off, the second discount applies to the already-reduced price. The combined effect is 1 - 0.80 x 0.90 = 28 percent off, not 30 percent. To check a stacked offer, run the calculator twice: apply the first discount, then use the result as the new original price.",
],
"examples": [
("Judging a seasonal sale", "A 250 coat is listed at 35 percent off. The calculator shows 87.50 off and a sale price of 162.50. With 7 percent tax the total is 173.88. You now know the true cost before reaching the till, and can decide whether it beats last season's price you remember."),
("Comparing two offers", "Store A offers 30 percent off a 200 phone accessory; store B offers 60 off the same item. Thirty percent of 200 is 60, so the offers match, but if store B also charges delivery the calculator helps you price the difference exactly."),
("Clearance pricing for sellers", "A small shop wants to clear stock at 45 percent off a 40 item. The calculator confirms a sale price of 22, and with tax the customer pays 23.54 at 7 percent. The seller can sanity-check margin before printing labels."),
],
"tips": [
"Check the original price history if you can; some sale prices are permanent prices with a fictional anchor.",
"Percentage-off and fixed-amount-off offers are directly comparable once you compute both final prices.",
"Tax is usually charged on the discounted price, but a few jurisdictions differ, so verify locally.",
"For buy-one-get-one deals, halve the per-item price first, then apply any tax.",
"Round only at the end; intermediate rounding can shift a total by a cent or two.",
],
"faqs": [
("How do I calculate two discounts one after another?", "Apply the first discount and note the sale price, then enter that sale price as the new original price with the second percentage. Two 20 percent discounts, for example, combine to 36 percent off, not 40 percent."),
("Is the discount applied before or after tax?", "In most retail systems the discount reduces the price first and tax is charged on the reduced amount. This calculator follows that convention. If your local rule differs, add the tax manually to the pre-tax sale price."),
("Can I enter a discount over 100 percent?", "You can, but it is rarely meaningful: the sale price would go negative, which in practice means a payout or a price error. The tool will show the arithmetic; treat such results as a data-entry check."),
("How do I compare a percentage discount with a fixed amount off?", "Run the calculator once with the percentage and once with the fixed amount converted to a percentage of the price. The lower final price wins, and the tax field keeps the comparison honest."),
("Why does my receipt total differ by a few cents?", "Receipts often round per line item, apply loyalty discounts in a specific order, or use local rounding rules for cash payments. Small cent-level differences are normal."),
("Do you store the prices I enter?", "No. The calculation runs in your browser and nothing is sent to a server or saved."),
],
},
"tip-calculator": {
"intro": [
"Tipping is one of those moments where mental maths meets social pressure, usually at the end of a long meal with people waiting. This Tip Calculator removes the awkwardness: enter the bill, choose a tip percentage, optionally add the number of people, and you get the tip amount, the total, and the exact per-person share.",
"The tool is built for real dining situations. It handles the common percent choices used in different countries, supports rounding so you can leave a clean number, and splits the bill evenly across any group size. Whether you are travelling somewhere with unfamiliar tipping customs or just splitting dinner with friends, it gives you a confident number in seconds.",
"Because it runs entirely in your browser, you can use it at the table even with a weak connection, and nothing about your bill is sent anywhere. It is equally handy for taxi rides, hairdressers, tour guides, delivery drivers and any other service where a percentage tip is the custom.",
],
"how": [
"Using the calculator takes three inputs at most. Type the bill amount, pick or enter a tip percentage, and set the number of people if you are splitting. The results update instantly, and you can round the total up or down to a convenient figure.",
],
"steps": [
"Enter the bill amount, excluding any service charge already printed on it.",
"Choose a tip percentage, such as 10, 15, 18 or 20, or type your own.",
"Set the number of people sharing the bill, or leave it at one.",
"Read the tip amount, the total including tip, and the amount each person pays.",
"Adjust the percentage up or down to match the quality of service before paying.",
],
"works": [
"The maths is simple and transparent. The tip equals the bill multiplied by the tip percentage divided by 100. The total is the bill plus the tip. When splitting, each person pays the total divided by the number of people. A 84.50 bill with an 18 percent tip gains 15.21, making a total of 99.71; split four ways that is about 24.93 each.",
"Rounding is where small decisions matter. Many people round the per-person amount up to the nearest whole unit so everyone pays a clean figure, which slightly over-tips rather than under-tips. Others round the total and work backwards. The tool shows the exact figures first so any rounding you apply is a choice, not a guess.",
"One genuine subtlety is the tip base. Custom varies on whether to tip on the pre-tax or post-tax amount, and on whether a service charge already added to the bill replaces the tip. In countries where service is included, an additional tip is optional; where it is not, the percentage applies to the full bill. The calculator gives you the numbers; the convention is yours to apply.",
],
"examples": [
("Standard dinner split", "Four friends share a 132 bill and want an 18 percent tip. The tip is 23.76, the total is 155.76, and each person pays 38.94. Rounding each share to 39 leaves a slightly generous total, which suits good service."),
("Travelling abroad", "In a country where 10 percent is customary, a 58 meal needs a 5.80 tip for a 63.80 total. Checking before you pay avoids both over-tipping out of habit and under-tipping out of caution."),
("Large group with service charge", "A bill for 12 people shows a 15 percent service charge already added. In that case no further tip is required; enter 0 percent to get the exact per-person share of the printed total."),
],
"tips": [
"Check the bill for a service charge before adding a tip; doubling up is a common mistake.",
"Tipping on the pre-tax amount is a common convention where you want to be precise.",
"Round per-person shares up slightly to keep payment collection simple.",
"For poor service it is fine to reduce the percentage; the tool just provides the numbers.",
"Keep small notes handy; a precise per-person figure is useless if nobody has change.",
],
"faqs": [
("Should I tip on tax?", "Conventions differ. Tipping on the pre-tax amount is the traditional rule in many places, while simply tipping on the final bill is easier and slightly more generous. The calculator shows the bill you enter; enter the pre-tax figure if you follow that custom."),
("What tip percentage should I use?", "In the United States, 15 to 20 percent at restaurants is standard. In much of Europe and Asia, service is often included and small extra tips are optional. Check local customs when travelling."),
("How do I split a bill unevenly?", "Split the shared items yourself first, then run the calculator on each person's subtotal with the same tip percentage and add the results. The percentage must be the same for the maths to stay fair."),
("Does the calculator handle currencies?", "Yes. It works with plain numbers, so the results are correct in any currency. The currency symbol is a matter of what you type and where you are."),
("Is a tip on a delivery order calculated differently?", "The percentage approach still works, though many people use flat amounts for short deliveries. Enter the fee as the bill and adjust the percentage until the tip looks right."),
("Is anything saved or shared?", "No. The calculator runs entirely on your device, and bill amounts are never transmitted or stored."),
],
},
"compound-interest-calculator": {
"intro": [
"Compound interest is the idea that money earns interest on its interest. It is the force behind long-term saving, pension growth, debt snowballs and, less pleasantly, unpaid credit card balances. This Compound Interest Calculator shows exactly how a balance grows when interest is added repeatedly, with or without regular contributions.",
"You enter a starting amount, an annual interest rate, a compounding frequency, a time horizon and, optionally, a regular contribution. The tool returns the future value, the total contributed, and the interest earned, so you can see precisely how much of the final balance is your money and how much is growth.",
"The calculator is useful for planning savings goals, comparing investment options, visualising retirement scenarios, and understanding loan or credit card balances that compound against you. Seeing a 25-year projection in a single number is often the motivation a savings plan needs, and adjusting the rate or term by small amounts shows how powerful each variable is.",
],
"how": [
"Fill in the starting amount, the annual rate, the number of years, and the compounding frequency such as yearly, monthly or daily. Add a regular contribution if you plan to deposit money over time. The results update instantly, showing the future balance and the split between contributions and interest.",
],
"steps": [
"Enter the initial amount you start with, or zero if you begin from nothing.",
"Type the annual interest rate you expect to earn or pay.",
"Set the number of years for the projection.",
"Choose how often interest compounds: yearly, quarterly, monthly or daily.",
"Optionally add a recurring contribution and its frequency, then read the future value and interest earned.",
],
"works": [
"For a single deposit with no contributions, the tool uses the standard compound formula: A equals P multiplied by (1 + r/n) raised to the power n x t, where P is the principal, r the annual rate, n the compounding periods per year and t the time in years. One thousand at 5 percent compounded monthly for 10 years becomes 1000 x (1 + 0.05/12)^(12 x 10), which is about 1,647.",
"When regular contributions are included, the tool treats each contribution as a small deposit that then compounds for the time remaining, and sums them all. This matches how banks and investment platforms calculate growing balances, and it is why starting early matters so much: a deposit made in year one compounds for the entire horizon, while the same deposit made in year twenty compounds for a fraction of it.",
"The difference between compounding frequencies is real but modest at normal rates. Five percent compounded annually on 1,000 for 10 years gives 1,628.89; monthly gives 1,647.01. The gap widens with higher rates and longer terms. The interest earned is the future value minus everything you put in, which is the cleanest measure of what compounding actually did for you.",
],
"examples": [
("Retirement projection", "Saving 300 a month for 30 years at 7 percent annual growth, compounded monthly, with nothing to start, produces roughly 366,000. Total contributions are 108,000, so compounding supplies over 250,000 of the final balance."),
("Comparing two accounts", "An account paying 4.5 percent versus one paying 5 percent sounds trivial. On 10,000 over 20 years, the difference is about 1,900. Running both rates through the calculator turns a vague preference into a decision."),
("Understanding debt", "A 3,000 credit card balance at 22 percent compounded monthly with no payments grows to about 5,000 in just over three years. The same formula that grows savings shows why minimum payments barely dent high-rate debt."),
],
"tips": [
"Be conservative with the rate you assume; a few points of optimism changes projections enormously.",
"Time in the market matters more than the starting amount. Start early even if the amount is small.",
"Check whether contributions are monthly or annual; the timing of deposits changes the result.",
"Inflation reduces what a future balance will buy, so consider real (after-inflation) returns for long plans.",
"For debts, the same maths runs in reverse: compounding frequency and rate determine how fast a balance grows.",
],
"faqs": [
("What is the difference between simple and compound interest?", "Simple interest is paid only on the original principal. Compound interest is paid on the principal plus accumulated interest, so the balance grows faster and faster over time."),
("Which compounding frequency should I choose?", "Use whatever matches the real product: savings accounts usually compound monthly or daily, bonds often annually, and credit cards daily. Choosing the true frequency keeps projections accurate."),
("Are contributions made at the start or end of each period?", "This calculator treats contributions as made at the end of each period, the most common convention. If you deposit at the start of each month, the final balance will be slightly higher than shown."),
("Does the calculator account for taxes or fees?", "No. It models gross growth. Taxes on interest or gains, and any management fees, reduce the real outcome, so use a lower effective rate to approximate them."),
("Why is my bank's projection slightly different?", "Banks may use daily interest accrual, different rounding, or treat deposits on different dates. Small differences are normal; large ones usually mean a different assumption about contributions."),
("Can I project negative growth, like debt?", "Yes. Enter the debt as the principal and the interest rate as a positive number; the future value shows what the balance will grow to if unpaid. Contributions entered as regular payments would represent repayments."),
],
},
"gst-vat-calculator": {
"intro": [
"Sales taxes go by many names: GST, VAT, sales tax, HST. Whatever the label, the same two questions come up constantly: what will this item cost once tax is added, and how much of a tax-inclusive price was actually tax? This GST and VAT Calculator answers both directions instantly.",
"Enter an amount and a tax rate, and choose whether the amount is tax-exclusive (tax needs to be added) or tax-inclusive (tax needs to be removed). The tool returns the net amount, the tax component, and the gross total. It is equally useful for buyers checking receipts and for sellers preparing invoices.",
"Businesses use it daily for invoicing and bookkeeping, shoppers use it to understand prices in tax-inclusive countries, and importers use it to estimate landed costs. Because the maths is mechanical but error-prone by hand, a calculator that handles both directions removes an entire class of small, annoying mistakes.",
],
"how": [
"Choose the direction first: adding tax to a net price, or removing tax from a gross price. Then enter the amount and the tax rate. The tool shows the net value, the tax amount, and the gross total, updating live as you edit.",
],
"steps": [
"Select whether your amount excludes tax or includes tax.",
"Enter the amount in either direction.",
"Type the applicable tax rate, such as 5, 12.5, 20 or 23.",
"Read the three results: net amount, tax component and gross total.",
"Switch direction to double-check an invoice or receipt in the opposite way.",
],
"works": [
"Adding tax is direct multiplication: tax equals the net amount multiplied by the rate divided by 100, and gross equals net plus tax. A 500 net invoice at 10 percent GST gains 50 in tax, so the gross total is 550.",
"Removing tax requires division, not subtraction, and this is where most hand calculations go wrong. The net amount equals the gross divided by (1 + rate/100). From a 550 gross price at 10 percent, the net is 550 / 1.10 = 500 and the tax is 50. A common mistake is to compute 10 percent of 550, which gives 55 and a net of 495, and is wrong because the tax was charged on the net, not the gross.",
"The two directions are exact inverses. If you add 20 percent VAT to 250 you get 300, and removing 20 percent from 300 returns exactly 250. The tool keeps both directions consistent, which makes it easy to reconcile receipts, invoices and expense claims where the tax line must be reported separately.",
],
"examples": [
("Pricing a product for sale", "You want 80 net for a handmade item and your VAT rate is 20 percent. The gross price to display is 96. The calculator confirms the tax component is 16, which you will owe to the tax authority from that sale."),
("Reading a receipt", "A restaurant bill shows 115.80 inclusive of 10 percent GST. Removing the tax gives a net of 105.27 and tax of 10.53. That tax line is what you claim if the meal is a business expense."),
("Import cost estimate", "Goods valued at 2,000 with 15 percent duty-equivalent tax will land at 2,300 before shipping. Running several rates shows the range of possible landed costs and helps set a resale price."),
],
"tips": [
"Confirm the exact rate for the product category; many countries have reduced rates for food, books or medicine.",
"Tax-inclusive and tax-exclusive prices are easy to confuse; always check which one a quote uses.",
"For invoices, show net, tax and gross separately; most tax authorities require the tax line to be visible.",
"When rates change, recompute rather than adjusting percentages in your head.",
"Keep the direction straight: you divide to remove tax and multiply to add it.",
],
"faqs": [
("Why is removing 20 percent not the same as subtracting 20 percent?", "Because the tax was calculated on the smaller net amount. Twenty percent of the gross is a larger number than the tax actually charged, so you must divide by 1.20 rather than subtract 20 percent of the gross."),
("What is the difference between GST and VAT?", "Functionally they are the same consumption tax collected in stages. Different countries simply use different names and rates. This calculator treats them identically."),
("Can I use it for multiple tax lines, like state plus local?", "Yes. Combine the rates into one effective rate by adding them, then enter that total. For example, a 5 percent state tax plus 2 percent local tax is a 7 percent combined rate."),
("Does it handle fractional rates like 12.5 percent?", "Yes. Enter any decimal rate. The results keep full precision and display sensible rounding."),
("Is the calculator suitable for official tax filing?", "It performs standard arithmetic correctly, but filing rules involve exemptions, thresholds and rounding conventions set by each tax authority. Use it for calculation and checking, and follow official guidance for reporting."),
("Is any data stored?", "No. All computation happens in your browser and no amounts or rates are transmitted."),
],
},
}
