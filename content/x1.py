# Expanders batch 1: calculators + finance
X = {
"percentage-calculator": {
"deep": [
"Direction errors deserve a closer look because they produce plausible-looking wrong answers. When asked what percent 30 is of 150, the correct base is 150, the whole amount. Reversing the inputs gives 500 percent, a number that looks impressive and is simply the answer to a different question. A reliable habit is to say the question in words first, X is what percent of Y, and enter the numbers in exactly that order.",
],
"mistakes": [
"Dividing by the new value instead of the original when computing percentage change, which understates increases and overstates decreases.",
"Adding successive discount percentages arithmetically instead of applying them one at a time to the shrinking price.",
"Confusing a percentage change with a percentage-point change when comparing two rates.",
"Forgetting to move the decimal point, treating 0.5 percent as 50 percent or the reverse.",
],
"extra_faqs": [
("What is a basis point?", "One hundredth of a percentage point. A move from 4.00 percent to 4.25 percent is 25 basis points. Finance uses basis points because percentage-point talk gets clumsy at small scales."),
("How do I add a percentage to a number in one step?", "Multiply by one plus the rate as a decimal: adding 20 percent is multiplying by 1.20. The percent-of-number mode gives the added part; this single multiplication gives the new total directly."),
],
},
"bmi-calculator": {
"deep": [
"BMI's history explains both its usefulness and its limits. It was devised in the 1830s by the statistician Adolphe Quetelet as a population measure, not an individual diagnosis, and it entered clinical use because it is cheap, repeatable and correlates with body fat at the population level. Those properties remain valuable: no laboratory test is as easy to take repeatedly as height and weight on a scale.",
"Where BMI misleads is exactly where the population average does not describe the individual. Muscle mass, frame size, age and fat distribution all move the number without moving health in the same direction. This is why modern guidance pairs BMI with a waist measurement, since abdominal fat carries different risk implications than fat stored elsewhere, and why the category bands are brackets rather than verdicts.",
],
"mistakes": [
"Using adult BMI categories for children, who need age and sex specific percentile charts.",
"Measuring height with shoes on or weight at inconsistent times, which shifts the result without any real change.",
"Treating a single high reading as a trend; day-to-day weight fluctuates by a kilogram or more.",
"Ignoring the muscle caveat for athletes and reading a high BMI as automatic proof of excess fat.",
],
"extra_faqs": [
("What is a healthy waist-to-height ratio?", "Guidance commonly points to a waist under half your height. It is a useful companion to BMI because it captures where weight is carried, which BMI cannot see."),
("Does age change the healthy BMI range?", "The standard 18.5 to 24.9 band applies broadly to adults, but some guidance suggests slightly higher ranges may be acceptable for older adults. Individual factors matter, so discuss targets with a clinician."),
],
},
"age-calculator": {
"deep": [
"The years-months-days method is worth understanding because it is the convention officialdom uses. When a form asks for age in years and months, it almost always means completed units: a child who has lived 10 full years, 7 full months and 20 extra days is 10 years and 7 months old, not 10 years and 8 months. The calculator follows this completed-units rule, which is why its output matches passports, school systems and medical records.",
"Timezone edge cases are worth a note for anyone doing precision work. A birth moment near midnight can fall on different calendar dates in different zones, and this tool works purely on calendar dates as entered, with no timezone conversion. For legal and administrative purposes this is the right behaviour: the birth certificate's date is the date, wherever in the world the birth happened.",
],
"mistakes": [
"Entering the current year instead of the birth year, which produces an implausibly small age.",
"Forgetting that a future reference date changes the question from current age to age at that future moment.",
"Comparing a years-months-days result with a day-count total and expecting them to feel consistent; they measure the same span in different units.",
"Assuming every year has 365 days in hand calculations, which drifts by a day per leap year crossed.",
],
"extra_faqs": [
("Can I find the day of the week for any date?", "Yes. The tool reports the weekday of the birth date, which works for historical dates too and is a quick way to verify records or settle trivia."),
("Why do the month and day totals look inconsistent with the years?", "They are different decompositions of the same span. Years-months-days follows the calendar; the totals count absolute units. Both are correct for their own purpose."),
],
},
"loan-emi-calculator": {
"deep": [
"The amortisation schedule is the mental model worth acquiring. Imagine the loan as a table with one row per payment: interest owed that month, principal repaid, remaining balance. The EMI is designed so the table reaches zero exactly at the final payment. Reading that table, even mentally, explains everything about how loans behave: why the balance falls slowly at first, why refinancing mid-loan resets the interest-heavy period, and why two loans with the same EMI can have very different total costs.",
"This is also why the annual rate must be divided by twelve rather than applied annually. Interest on amortising loans accrues monthly on the outstanding balance, so the monthly rate is the one that compounds. Using the annual rate directly overestimates interest dramatically, a mistake that makes loan offers look worse than they are.",
],
"mistakes": [
"Comparing loans by monthly payment alone, which hides differences in term length and total interest.",
"Forgetting fees, insurance and taxes that sit outside the EMI but inside the real cost.",
"Entering the annual rate as a monthly rate or vice versa, which distorts results by an order of magnitude.",
"Assuming the advertised rate is fixed for the whole term without checking whether it is variable.",
],
"extra_faqs": [
("What is an amortisation schedule?", "The table of every payment over the loan's life, showing how each splits into interest and principal and how the balance declines. Lenders provide one on request, and it is illuminating reading."),
("How much can I afford to borrow?", "A common guideline keeps total housing or debt payments under about a third of take-home income. Work backwards from a comfortable payment using the calculator to find the loan amount that fits."),
],
},
"discount-calculator": {
"deep": [
"Retail pricing psychology deserves a mention because it changes how to read the inputs. Anchoring research shows that a high original price makes the discounted price feel like a bargain regardless of the item's real market value. The defence is to compare the final price against what the item is worth to you, not against the crossed-out number. The calculator supports exactly this: it makes the final price explicit, so the anchor loses its power.",
"Currency and rounding rules explain most receipt mismatches. Some jurisdictions round cash totals to the nearest five cents, some retailers round per line before tax, and some apply loyalty discounts last. A difference of a few cents between the calculator's total and a receipt is arithmetic convention, not error.",
],
"mistakes": [
"Adding stacked discounts instead of compounding them, overestimating the total saving.",
"Comparing a percentage-off deal at one store with a fixed-amount deal at another without computing both final prices.",
"Forgetting that delivery fees can erase a discount advantage between stores.",
"Trusting the crossed-out original price without any check of the item's usual selling price.",
],
"extra_faqs": [
("How do I calculate the original price from a sale price?", "Divide the sale price by one minus the discount rate: an item selling at 60 after 25 percent off had an original price of 60 / 0.75 = 80. Reverse-engineering like this is handy for verifying claims."),
("Do coupons stack with sales?", "Often yes, and the order matters less than people think for percentages: two percentage discounts compound to the same result in either order. A percentage plus a fixed amount does depend on order, so test both sequences."),
],
},
"tip-calculator": {
"deep": [
"International conventions are worth knowing before travelling, because the percentage that is polite in one country is an insult or an overpayment in another. In the United States, table-service tips of 15 to 20 percent are customary because service wages are structured around them. In much of Europe, service is included by law and rounding up or leaving a few percent is a gesture, not an obligation. In Japan, tipping can cause genuine confusion. Ten seconds with the calculator plus local knowledge beats importing home habits abroad.",
"Group dynamics are the other recurring challenge. The fairest systems either split evenly, which the calculator does, or itemise, which the calculator supports by running each person's subtotal separately. What fails socially is the vague compromise: someone rounds loosely, the total comes up short, and the difference quietly lands on one person. An explicit per-person figure from the calculator prevents exactly that.",
],
"mistakes": [
"Tipping an additional percentage on top of a bill that already includes a service charge.",
"Computing the tip on the total including a prior tip, compounding by accident.",
"Splitting the bill evenly when one person's items were far more expensive, without agreeing on it first.",
"Forgetting that card minimums and cash-only situations change what a precise per-person figure is worth.",
],
"extra_faqs": [
("How do I handle a bill where some people did not drink?", "Itemise: run the calculator separately for the shared food and each person's drinks, applying the same tip percentage to each subtotal, then add the results. It takes a minute and ends the debate."),
("Should delivery tips be a percentage or flat?", "Both are accepted conventions. A percentage scales with order size; a flat amount recognises that delivery effort barely varies with the order. Many people use a floor: the percentage, but never less than a few units."),
],
},
"compound-interest-calculator": {
"deep": [
"The rule of 72 is the pocket version of this calculator's maths: divide 72 by the annual rate to estimate how many years it takes money to double. At 6 percent, money doubles roughly every 12 years; at 9 percent, every 8. The rule is approximate but remarkably good in the range of ordinary rates, and it is the quickest sanity check on whether a projection the calculator produces is plausible.",
"Compounding's dark twin applies to debt, and it is worth facing directly. The same formula that turns 300 monthly savings into six figures over decades turns an unpaid credit card balance into a growing liability at double-digit rates. The direction is a choice made by whoever controls the cash flow, which is why the same calculator is instructive for both plans.",
],
"mistakes": [
"Assuming an aggressive investment return for decades of projection, which inflates the result enormously.",
"Ignoring inflation, which makes a nominal future figure look richer than it will feel.",
"Forgetting that fees of even one percent a year compound against you exactly like returns compound for you.",
"Confusing the compounding frequency with the contribution frequency; they are independent settings.",
],
"extra_faqs": [
("What is the rule of 72?", "A quick mental approximation: divide 72 by the annual percentage rate to get the years for money to double. At 8 percent, about 9 years. The calculator gives exact figures; the rule gives instant intuition."),
("How do contributions change the growth curve?", "Dramatically. Early contributions compound for the whole term, so the same monthly amount started ten years earlier can end up worth far more than a larger amount started later."),
],
},
"gst-vat-calculator": {
"deep": [
"Rate tables reward a few minutes of attention because consumption taxes are rarely single-rate. Most systems apply a standard rate to most goods, one or more reduced rates to categories like food, books or medicine, and a zero rate to exports. Using the wrong rate is the most common error in this domain, and it is a bookkeeping error, not an arithmetic one: the maths is trivial once the rate is right.",
"The reverse calculation has a formal name in accounting, gross-to-net, and it appears constantly in expense processing. When an employee submits a receipt for a tax-inclusive amount, the accounting system must split out the tax to reclaim it. The division method this tool uses is exactly what those systems do, which is why the numbers reconcile when both are done correctly.",
],
"mistakes": [
"Subtracting the percentage from the gross instead of dividing by one plus the rate, which understates the net.",
"Applying the standard rate to reduced-rate categories like basic food or children's clothing.",
"Mixing up tax-inclusive and tax-exclusive quotes when comparing supplier prices.",
"Forgetting that some jurisdictions round the tax line per invoice while others round per item.",
],
"extra_faqs": [
("What is the difference between zero-rated and exempt?", "Zero-rated goods are taxable at zero, so businesses can reclaim input tax on their costs. Exempt goods sit outside the tax entirely, with no reclaim. The distinction matters to registered businesses, not to shoppers."),
("How do I handle a partial refund?", "Apply the same direction logic to the refunded amount: remove the tax from a tax-inclusive refund to find its net part. The proportions match the original invoice exactly."),
],
},
}
