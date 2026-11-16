# Batch 1: percentage-calculator, bmi-calculator, age-calculator, loan-emi-calculator
CONTENT = {
"percentage-calculator": {
"intro": [
"Percentages are everywhere: price cuts at the checkout, exam scores, interest rates, commission deals, battery levels and statistics in the news. Yet the maths behind them is easy to fumble under time pressure, and a small slip can change a price by a lot. This Percentage Calculator takes the guesswork out by handling the most common percentage questions in one place, with instant results as you type.",
"The tool covers the three calculations people need most often: finding what a given percent of a number is, finding what percentage one number is of another, and measuring the percentage increase or decrease between two values. Instead of remembering whether to multiply or divide, you simply pick the question that matches your situation and enter two numbers.",
"It is useful for shoppers comparing sale prices, students checking homework, employees reviewing raises or commissions, business owners calculating margins and taxes, and anyone who wants a quick, reliable answer without opening a spreadsheet. Everything runs locally in your browser, so nothing you type is sent anywhere.",
],
"how": [
"The calculator is organised into three modes, one for each common question. Choose the mode that matches what you want to know, fill in the two boxes, and the answer appears immediately. There is no calculate button to press.",
],
"steps": [
"Pick a mode: percent of a number, what percent X is of Y, or percentage change.",
"Type the first number, such as the percentage or the starting value.",
"Type the second number, such as the amount or the new value.",
"Read the highlighted result, which updates live as you edit the inputs.",
"Change a value to explore alternatives, for example comparing a 15 percent and a 25 percent discount.",
],
"works": [
"Each mode applies one simple formula. For percent of a number, the tool multiplies the number by the percentage and divides by 100, so 20 percent of 150 is 150 x 20 / 100 = 30. This matches how percentages are defined: a percentage is a fraction with a denominator of 100.",
"For the what-percent mode, the tool divides the first number by the second and multiplies by 100. If you scored 42 points out of 50, the calculation is 42 / 50 x 100 = 84 percent. The tool is careful about direction: 42 out of 50 is not the same question as 50 out of 42, and mixing up the order is the most common mistake in percentage maths.",
"For percentage change, the tool computes the difference between the new and old values, divides by the old value, and multiplies by 100. Percentage change is always measured against the original value, which is why a 50 percent loss followed by a 50 percent gain does not return you to the start: 100 down 50 percent is 50, and 50 up 50 percent is 75.",
],
"examples": [
("Shopping discount", "A jacket costs 120 and is advertised at 30 percent off. Using the percent-of-number mode, 120 x 30 / 100 = 36, so the discount is 36 and the sale price is 84. Doing this before you reach the till helps you judge whether a deal is genuinely good."),
("Exam and test scores", "You answered 37 questions correctly out of 45. The what-percent mode gives 37 / 45 x 100, which is about 82.2 percent. This is handy for converting raw marks into the percentage scale that schools and courses usually report."),
("Price and salary changes", "Your rent rises from 900 to 990 a month. The percentage-change mode gives (990 - 900) / 900 x 100 = 10 percent. The same mode works for falls: if a subscription drops from 20 to 15, the change is -25 percent, showing the size of the saving."),
],
"tips": [
"A percentage off is not the same as a percentage of the sale price. 25 percent off 80 is 60, not 80 minus 25.",
"For successive discounts, apply them one at a time. 20 percent then 10 percent off is a 28 percent total reduction, not 30 percent.",
"Percentage change uses the old value as the base, so increases and decreases are not symmetric.",
"Quick mental check: 10 percent of a number is the number with the decimal point moved one place left.",
"When comparing offers, convert everything to percentages of the same base so the comparison is fair.",
],
"faqs": [
("Can I use negative numbers?", "Yes. Negative values are useful for losses, temperature-style changes and decreases. In the percentage-change mode, a negative result simply means the value went down by that percent."),
("Why does 50 percent off then 50 percent off not make something free?", "Because the second discount applies to the reduced price, not the original. Half off 100 is 50, and half off 50 is 25. Two successive 50 percent discounts leave you paying 25 percent of the original price."),
("What is the difference between percentage and percentage points?", "Percentage points describe the difference between two percentages. If a rate moves from 4 percent to 6 percent, it rose by 2 percentage points, but by 50 percent in relative terms. This tool computes relative percentages."),
("How do I calculate a tip or service charge?", "Use the percent-of-number mode. A 15 percent tip on a 46 bill is 46 x 15 / 100 = 6.90. Add that to the bill for the total, or use the dedicated Tip Calculator for per-person splitting."),
("Does the tool round results?", "Results are shown with sensible precision and not silently rounded to whole numbers, so small percentages stay accurate. If you need a specific number of decimal places, round the displayed value according to your own rules."),
("Is my data sent to a server?", "No. All calculations run in your browser with JavaScript. Nothing you type is transmitted, stored or logged, which makes the tool safe for salary, pricing and other sensitive numbers."),
],
},
"bmi-calculator": {
"intro": [
"Body Mass Index, or BMI, is a quick screening number that compares your weight to your height. Health services around the world use it to sort adults into broad weight categories, because a single number is far easier to track over time than raw weight alone. This BMI Calculator computes your BMI instantly and shows the category it falls into.",
"You enter your height and weight, in metric or imperial units, and the tool returns your BMI together with the standard category: underweight, healthy weight, overweight or obese. It also shows the healthy weight range for your height, which turns an abstract number into a concrete target.",
"BMI is a screening tool, not a diagnosis. It is genuinely useful for spotting trends and for a first conversation about health, but it does not measure body fat directly and it cannot see the difference between muscle and fat. Athletes, older adults and pregnant people need extra context when reading the result, which this page explains below.",
],
"how": [
"The calculator needs just two inputs and takes seconds. Switch between metric and imperial units first so the labels match the numbers you have, then enter your values and read the result. The category and healthy range update together.",
],
"steps": [
"Choose metric (kilograms and centimetres) or imperial (pounds and feet and inches).",
"Enter your height using the fields provided.",
"Enter your weight.",
"Read your BMI number and the colour-coded category shown underneath.",
"Check the healthy weight range for your height to see the band your weight sits in.",
],
"works": [
"The formula is simple. In metric units, BMI equals weight in kilograms divided by the square of height in metres. Someone who is 170 cm tall and weighs 65 kg has a BMI of 65 / (1.70 x 1.70), which is about 22.5. In imperial units the formula includes a conversion factor of 703: BMI equals 703 x pounds divided by inches squared.",
"The result is compared against standard adult ranges. A BMI below 18.5 is classed as underweight, 18.5 to 24.9 is the healthy range, 25 to 29.9 is overweight, and 30 or above is obese. These cutoffs come from large population studies linking BMI ranges to health outcomes, and they apply to adults aged roughly 18 to 65.",
"The healthy weight range shown by the tool is simply the weight that would put you at the edges of the healthy band for your height. It is calculated by rearranging the formula: multiply 18.5 and then 24.9 by your height in metres squared. Seeing the range in kilograms or pounds makes it much easier to set a realistic personal target.",
],
"examples": [
("Metric example", "A person 165 cm tall weighing 82 kg has a BMI of 82 / (1.65 x 1.65) = 30.1. That falls just inside the obese category, suggesting a conversation with a health professional could be worthwhile and that modest weight loss would move them into the overweight band."),
("Imperial example", "Someone who is 5 feet 9 inches (69 inches) and weighs 150 pounds has a BMI of 703 x 150 / (69 x 69) = 22.1, comfortably in the healthy range. The same person would leave the healthy band above roughly 169 pounds."),
("Tracking change over time", "If your BMI was 27.8 three months ago and is 26.9 today, the number itself matters less than the direction. Recording BMI periodically turns vague intentions into measurable progress, which is one of the main reasons clinicians prefer it to raw weight."),
],
"tips": [
"Measure height without shoes and weigh yourself at a consistent time of day for comparable results.",
"BMI reads muscle as fat. Very muscular people can score high while being perfectly healthy.",
"Adult cutoffs do not apply to children, who need age and sex specific charts instead.",
"Where you carry weight matters too; waist measurement adds context that BMI alone lacks.",
"Use BMI as a trend line, not a verdict, and discuss big changes with a professional.",
],
"faqs": [
("Is BMI accurate for athletes?", "Not always. Muscle is denser than fat, so muscular athletes often land in the overweight range despite low body fat. For them, measures such as body fat percentage or waist-to-height ratio tell a more accurate story."),
("Does BMI work during pregnancy?", "No. Pregnancy changes weight in ways the formula cannot account for, so BMI categories should not be applied while pregnant. Use pre-pregnancy BMI only where a clinician specifically asks for it."),
("Are the categories the same for all adults?", "The standard ranges apply to most adults, but some health services use adjusted cutoffs for certain ethnic groups because health risks can begin at lower BMIs. Follow your local health guidance where it differs."),
("What BMI should I aim for?", "For most adults the healthy range of 18.5 to 24.9 is the target. If you are outside it, even small movements toward the range are linked to health benefits, so progress matters more than the exact number."),
("Why does the tool show a weight range?", "The healthy range converts the abstract BMI scale back into kilograms or pounds for your exact height. It answers the practical question of what the category means for you personally."),
("Is my information stored?", "No. The calculation happens entirely in your browser. Your height and weight are never sent over the network, stored, or seen by anyone else."),
],
},
"age-calculator": {
"intro": [
"Working out an exact age sounds trivial until you actually try it. Months have different lengths, leap years add a day, and counting by hand across decades invites mistakes. This Age Calculator does the calendar arithmetic for you and reports an exact age in years, months and days, plus totals in smaller units.",
"Enter any birth date and any reference date, and the tool computes the precise gap between them using proper calendar rules. By default the reference date is today, but you can set any date, which makes the tool equally good for historical questions, school cut-off rules or planning a future event.",
"Beyond curiosity, exact ages matter in real administration: school enrolment cut-offs, visa and pension paperwork, sports age brackets, insurance quotes and medical dosing all depend on precise ages. The tool also shows your next birthday and the day of the week you were born, which are the two age facts people most often want to know.",
],
"how": [
"You only need to enter a birth date to get a full result. The tool fills in today as the reference automatically; change it only if you want to measure against a different date. Results appear as soon as both dates are set.",
],
"steps": [
"Enter the birth date using the date picker.",
"Leave the second date as today, or set your own reference date.",
"Read the exact age in years, months and days.",
"Check the totals below for age in total months, weeks, days, hours and minutes.",
"Look at the next-birthday line to see how long until the next anniversary.",
],
"works": [
"The calculator counts the full calendar span between the two dates, borrowing like subtraction across a calendar. It takes the day and month of the birth date and works out how many whole years fit before the reference date, then how many whole months remain, then the leftover days. This years-months-days method matches how ages are stated officially in most countries.",
"Leap years are handled by the underlying date arithmetic rather than a simple count of days divided by 365. February 29 is treated as a real calendar day, so someone born on February 29 has a correct birthday counted on the anniversary, and ages spanning leap years stay accurate to the day.",
"The totals in smaller units are computed from the exact number of days between the dates multiplied out into hours and minutes. Because months vary between 28 and 31 days, a result like 25 years, 3 months, 12 days is the primary answer, and the day-based totals are a complementary way to think about the same span.",
],
"examples": [
("Standard age check", "A child born on 12 March 2015 measured on 1 November 2025 is 10 years, 7 months and 20 days old. A school with a September 1 cut-off can instantly see whether the child meets an age requirement."),
("Historical and future dates", "Set the reference date to a graduation, wedding or contract date to find how old someone will be on that day. Setting a past reference date answers questions like how old a historical figure was at a specific event."),
("Days-until milestone", "For a 10,000 days milestone, read the total-days figure and see how close you are. People use these totals for fun milestones, anniversaries of weekly habits and countdown planning."),
],
"tips": [
"Double-check the year first; entering the current year by mistake is the most common input error.",
"Use a past reference date to compute an age at any moment in history, not just today.",
"The day-of-week result is handy for verifying birth records and planning anniversaries.",
"For legal age questions, confirm whether the relevant rule counts the day before or the day of the birthday.",
"Totals in hours and minutes grow fast, so treat them as fun facts rather than precise measures.",
],
"faqs": [
("How are leap-year birthdays handled?", "The calculator uses real calendar dates, so February 29 is counted when it occurs. In non-leap years, the anniversary is treated on March 1 by convention in most systems that consume the result."),
("Why does my age in days not match another website?", "Some sites divide a rough year length into the total, which drifts by a day or two across decades. This tool counts actual calendar days between the two dates, which is the accurate method."),
("Can I calculate an age at a date in the future?", "Yes. Set the reference date to any future date and the tool reports the age that will apply then, which is useful for paperwork and event planning."),
("Does the tool count the birth day itself?", "Age is reported as completed years, months and days, which is the standard convention. The birth day itself is day zero of the count."),
("What is the maximum date range?", "The tool handles any dates your browser supports, from well before the modern era into the far future, so historical ages work without any special settings."),
("Is anything uploaded?", "No. All computation happens locally in your browser. Birth dates are sensitive, and none of them leave your device."),
],
},
"loan-emi-calculator": {
"intro": [
"A loan is easy to describe and surprisingly hard to price by intuition. The monthly payment depends not just on the amount borrowed but on the interest rate and the term in ways that do not scale linearly. This Loan and EMI Calculator turns the three inputs into a clear monthly payment, plus the total interest and total cost over the life of the loan.",
"EMI stands for Equated Monthly Instalment: the fixed amount you pay each month on a typical amortising loan such as a car loan, personal loan, mortgage or student loan. Early in the loan most of each payment is interest; late in the loan most of it goes to the principal. The calculator applies the standard amortisation formula so the numbers you see match what lenders quote.",
"Use it before you borrow to check affordability, while comparing offers to see the true cost of different rates and terms, and during the loan to understand how extra payments or refinancing might change your position. Seeing total interest in plain numbers is often the moment a loan offer starts to make sense.",
],
"how": [
"Enter the loan amount, the annual interest rate and the term in years or months. The calculator returns the monthly payment immediately, along with the total interest you would pay and the overall cost. Adjust any input to compare scenarios side by side.",
],
"steps": [
"Type the loan amount you intend to borrow.",
"Enter the annual interest rate offered by the lender.",
"Set the term, either in months or years depending on the field.",
"Read the monthly EMI in the highlighted result box.",
"Compare total interest across different terms before committing to a longer loan.",
],
"works": [
"The calculator uses the standard annuity formula: EMI equals P x r x (1 + r)^n / ((1 + r)^n - 1), where P is the principal, r is the monthly interest rate (annual rate divided by 12) and n is the number of monthly payments. This formula produces the fixed payment that exactly pays off principal and interest over the term.",
"The reason early payments are interest-heavy is the outstanding balance. Interest each month equals the balance times the monthly rate, and whatever remains of the fixed payment reduces the principal. As the balance falls, the interest slice shrinks and the principal slice grows, which is why overpaying early is disproportionately effective.",
"Total cost is the monthly payment multiplied by the number of payments. The gap between that figure and the amount borrowed is the total interest, and it is often larger than people expect. For example, a 200,000 loan at 6 percent for 25 years costs roughly 1,289 per month and about 186,600 in interest, nearly doubling the cost of the house itself. Shortening the term raises the payment but cuts total interest dramatically.",
],
"examples": [
("Car loan comparison", "A 20,000 car loan at 7 percent for 5 years costs about 396 per month and 3,761 in total interest. The same loan over 3 years costs about 618 per month but only 2,253 in interest, a saving of roughly 1,500 for 262 more per month."),
("Mortgage term choice", "On a 250,000 mortgage at 5 percent, 30 years costs about 1,342 per month with 233,000 total interest, while 20 years costs about 1,650 per month with 146,000 interest. Paying 308 more per month saves around 87,000."),
("Checking affordability", "Before applying, reverse the question: decide the maximum monthly payment you can comfortably make, then test loan amounts and terms until the EMI fits. This prevents being anchored to a purchase price rather than a payment."),
],
"tips": [
"Ask lenders for the APR, not just the headline rate; APR includes fees and reflects the true cost.",
"Shorter terms almost always mean less total interest, but only choose them if the payment is comfortably affordable.",
"Even small extra payments early in the loan shorten the term disproportionately.",
"Watch for arrangement fees and insurance add-ons that are not part of the EMI formula.",
"Fixed and variable rates behave differently over time; stress-test your budget at a higher rate.",
],
"faqs": [
("What is the difference between interest rate and APR?", "The interest rate is the cost of borrowing the principal. The APR spreads mandatory fees across the loan term, so it is usually slightly higher and is the better number for comparing offers."),
("Does the calculator include taxes and insurance?", "No. It models pure principal and interest, which is the EMI in the strict sense. Property taxes, insurance and fees vary by borrower and should be added separately when budgeting."),
("Why is my lender's payment slightly different?", "Lenders may round payments, charge fees upfront, or calculate interest daily rather than monthly. Differences of a small amount per month are normal; large differences deserve a question to the lender."),
("How do extra payments affect the EMI?", "Extra payments do not change the contractual EMI; they reduce the balance faster, which shortens the term and cuts total interest. Some lenders recalculate the payment instead, so confirm their policy."),
("Is a longer term always cheaper monthly?", "Yes, the monthly payment falls as the term grows, but total interest rises. A longer term trades a lower payment for a much higher total cost."),
("Are the calculations stored anywhere?", "No. Everything is computed in your browser and nothing is transmitted. You can safely enter real figures from loan offers."),
],
},
}
