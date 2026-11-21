# -*- coding: utf-8 -*-
import re
from .mega1a import _WCRE, _fmt, _fit

def _fld(i, l, v="", ph=""):
    p = f' placeholder="{ph}"' if ph else ""
    return f'<div><label for="{i}">{l}</label><input type="number" id="{i}" step="any" value="{v}"{p} autocomplete="off" /></div>'

CALC = [
("simple-interest","Simple Interest Calculator","Simple interest, total amount and yearly breakdown",
 "Simple interest is the most transparent form of interest there is: it is charged only on the original principal, never on interest already earned. That makes it the right model for short-term loans, informal lending, exam problems and quick sanity checks on financial quotes. This calculator computes the interest, the final amount and the interest earned per year in one press.",
 "SI = P \u00d7 R \u00d7 T / 100 (interest); A = P + SI (total amount)",
 "1,000 at 5% for 3 years gives 150.00 interest and a total of 1,150.00",
 ["checking a loan or NBFC quote","homework and finance exams","short-term personal lending","estimating returns on flat-rate products"],
 "Simple interest assumes the principal never changes; most bank loans and savings accounts use compound interest, which grows faster the longer the term runs.",
 "si", _fld("si-p","Principal amount","1000") + _fld("si-r","Annual interest rate (%)","5") + _fld("si-t","Time (years)","3")),
("average","Average (Mean) Calculator","Mean of any list of numbers, with sum and count",
 "The average is the single most used statistic in daily work: grades, expenses, response times, sales, test scores. This calculator takes any list of numbers \u2014 one per line or separated by commas \u2014 and returns the mean together with the sum and the count, so you can see exactly what went into the result.",
 "Average = (sum of all values) / (number of values)",
 "12, 18, 24, 30, 36 gives a sum of 120, a count of 5 and an average of 24",
 ["school grades and test scores","monthly expense totals","sports and performance stats","survey response data"],
 "A single outlier drags the mean hard: one 10,000 expense among nine 100s makes the 'average' over 1,000, even though no typical value is near it.",
 "avg", '<div><label for="avg-n">Numbers (one per line or comma-separated)</label><textarea id="avg-n" rows="6" placeholder="12, 18, 24, 30, 36"></textarea></div>'),
("square-root","Square Root Calculator","Square root of any non-negative number, with verification",
 "The square root asks the question 'what number times itself gives this value?' and appears everywhere from geometry (the Pythagorean theorem) to statistics (standard deviation) to finance (volatility). This calculator returns the principal square root of any non-negative number and squares the answer back so you can verify it instantly.",
 "x = \u221an, verified by x \u00d7 x = n",
 "144 gives exactly 12, because 12 \u00d7 12 = 144",
 ["geometry and the Pythagorean theorem","standard deviation and statistics","physics formulas","checking perfect squares"],
 "Negative numbers have no real square root \u2014 \u2212n needs complex numbers. The tool reports this instead of returning a misleading error.",
 "sqrt", _fld("sqrt-n","Number","144")),
("power","Exponent (Power) Calculator","Raise any base to any power, including negatives and decimals",
 "Exponents compress repeated multiplication into one symbol, and they are everywhere: compound interest, population growth, computer storage (2 to the 10th), scientific notation. This calculator raises any base to any exponent, including negative powers (which produce fractions) and decimal powers (which produce roots).",
 "Result = base raised to the exponent (base^exponent)",
 "2 to the power 10 gives 1,024",
 ["compound growth estimates","computer science and storage math","scientific notation","physics and chemistry formulas"],
 "A negative exponent means 'one over the positive power': 2 to the \u22123 is 0.125, not a negative number \u2014 a very common exam mistake.",
 "pow", _fld("pw-b","Base","2") + _fld("pw-e","Exponent","10")),
("circle-area","Circle Area Calculator","Area of a circle from its radius or diameter",
 "The area of a circle tells you how much surface it covers: pizza sizes, garden beds, pipe cross-sections, camera aperture math. Because the formula involves \u03c0, hand calculations drift \u2014 this calculator uses full precision and shows the working so the result is trustworthy at any size.",
 "A = \u03c0 \u00d7 r\u00b2",
 "A circle with radius 5 gives an area of about 78.54 square units",
 ["comparing pizza and pan sizes","material coverage estimates","engineering cross-sections","gardening and landscaping"],
 "Double-check whether a spec quotes radius or diameter \u2014 using the diameter as the radius understates the area by exactly four times.",
 "cirA", _fld("cir-r","Radius","5") + '<div class="hint">Area = \u03c0 \u00d7 radius\u00b2. For a diameter, halve it first.</div>'),
("circle-circumference","Circle Circumference Calculator","Perimeter of a circle from radius or diameter",
 "Circumference is the distance around a circle, and it decides real quantities: how far a wheel travels per turn, how much trim a round table needs, how much fencing wraps a tank. The tool computes it from the radius with the exact \u03c0 relationship and shows the number to sensible precision.",
 "C = 2 \u00d7 \u03c0 \u00d7 r (or \u03c0 \u00d7 diameter)",
 "A circle with radius 10 gives a circumference of about 62.83 units",
 ["wheel rotation and distance","fencing and trim estimates","pipe and cable wrapping","physics orbit problems"],
 "Rolling-distance problems need the circumference, not the area \u2014 mixing the two formulas is the most frequent mistake with wheels.",
 "cirC", _fld("ccm-r","Radius","10")),
("triangle-area","Triangle Area Calculator","Area of a triangle from base and height",
 "The triangle area formula is one of the first pieces of geometry people learn and one of the last they stop using: roof surfaces, sails, gable walls, land plots and 3D graphics all reduce to triangles. This calculator applies the standard base-times-height formula and shows the result immediately.",
 "A = \u00bd \u00d7 base \u00d7 height",
 "A triangle with base 10 and height 6 gives an area of 30 square units",
 ["roofing and construction estimates","sails, tents and fabric work","land and plot measurement","graphics and game geometry"],
 "The height must be perpendicular to the base \u2014 the length of a slanted side is not the height, even though it looks like one on a drawing.",
 "triA", _fld("tri-b","Base","10") + _fld("tri-h","Perpendicular height","6")),
("rectangle-area","Rectangle Area Calculator","Area and perimeter of any rectangle or square",
 "Rectangles cover most of the built world: rooms, walls, floors, screens, fields, solar panels. Area decides material quantities and cost; perimeter decides trim, fencing and border work. This calculator returns both from the width and height so you can order the right amount of everything.",
 "A = width \u00d7 height;  P = 2 \u00d7 (width + height)",
 "A rectangle 12 by 8 gives an area of 96 and a perimeter of 40",
 ["flooring and paint quantities","screen and display sizes","land and garden planning","cost per square unit quotes"],
 "Area and perimeter answer different questions \u2014 paint needs the area, skirting board needs the perimeter. Ordering one because you computed the other wastes money.",
 "rectA", _fld("rec-w","Width","12") + _fld("rec-h","Height","8")),
("factorial","Factorial Calculator","n! for any whole number, with the multiplication shown",
 "The factorial counts arrangements: n! is the number of ways to order n items, which makes it the backbone of probability, combinatorics and algorithm analysis. Because factorials grow absurdly fast \u2014 20! already exceeds a 64-bit integer \u2014 the tool switches to precise floating-point results and shows the size of the number honestly.",
 "n! = n \u00d7 (n\u22121) \u00d7 (n\u22122) \u00d7 \u2026 \u00d7 1",
 "10! gives 3,628,800",
 ["probability and combinatorics","permutations of lists and teams","algorithm complexity analysis","statistics formulas"],
 "Factorials only exist for whole numbers \u2014 4.5! has no meaning here \u2014 and they turn enormous quickly: 70! has 101 digits.",
 "facCalc", _fld("fac-n","Whole number n","10")),
("gcd-lcm","GCD and LCM Calculator","Greatest common divisor and least common multiple of two numbers",
 "The GCD tells you the largest number that divides two values evenly \u2014 it simplifies ratios and fractions. The LCM tells you the smallest number both values divide into \u2014 it synchronizes repeating events, from bus schedules to gear teeth. This calculator returns both at once, using the efficient Euclidean algorithm.",
 "GCD by the Euclidean algorithm; LCM = (a \u00d7 b) / GCD",
 "12 and 18 give a GCD of 6 and an LCM of 36",
 ["simplifying ratios and fractions","synchronizing repeating schedules","gear and pulse timing","number theory coursework"],
 "The LCM of two numbers can never be smaller than either of them, and the GCD can never be larger \u2014 if your result breaks that, an input is mistyped.",
 "gcdCalc", _fld("gcd-a","First number","12") + _fld("gcd-b","Second number","18")),
("prime-checker","Prime Number Checker","Test whether a number is prime, with the smallest factor",
 "A prime is divisible only by 1 and itself, and primes are the atoms of arithmetic \u2014 every whole number factors into them uniquely. They matter practically in cryptography, hashing and error correction. This checker tests any number up to very large sizes and, for composites, shows a factor that proves it.",
 "Trial division up to \u221an \u2014 if no divisor is found, the number is prime",
 "97 is prime; 91 = 7 \u00d7 13 is not",
 ["cryptography and key sizes","homework and number theory","hash table sizing","puzzle and game design"],
 "1 is not prime by definition, and 2 is the only even prime \u2014 both facts break the assumptions people bring from intuition.",
 "primeCalc", _fld("pr-n","Number to test","97")),
("number-to-words","Number to Words Converter","Write any number out in English words, for cheques and documents",
 "Legal and financial documents require amounts in words precisely because digits can be altered or misread: a cheque, a contract, an invoice footer. This converter writes any whole number in correct English \u2014 including the British-style 'and' handling and hyphenation rules \u2014 so the written amount always matches the digits.",
 "Place-value decomposition into English number words",
 "12,345 becomes \u201ctwelve thousand three hundred forty-five\u201d",
 ["cheques and bank drafts","contracts and invoices","exam answers and worksheets","localization checks"],
 "Different regions hyphenate and pad differently (\u201cone hundred and five\u201d vs \u201cone hundred five\u201d) \u2014 match the convention your document or bank expects.",
 "n2wCalc", '<div><label for="n2w-n">Number</label><input type="number" id="n2w-n" step="1" value="12345" autocomplete="off" /></div>'),
("quadratic-equation","Quadratic Equation Solver","Roots of ax\u00b2 + bx + c = 0, with discriminant analysis",
 "Quadratics model projectiles, profit curves, areas and signal behavior, and the quadratic formula solves all of them in one line. The discriminant tells you in advance whether you get two roots, one repeated root or none. This solver computes the discriminant, classifies the equation and returns both roots with the working shown.",
 "x = (\u2212b \u00b1 \u221a(b\u00b2 \u2212 4ac)) / 2a",
 "For x\u00b2 \u2212 3x + 2 = 0 the roots are x = 2 and x = 1",
 ["physics projectile problems","optimization and profit curves","algebra homework","engineering signal models"],
 "The formula assumes 'a' is not zero \u2014 if a = 0 the equation is linear, not quadratic, and has a single root \u2212c/b instead.",
 "quadCalc", _fld("quad-a","a (coefficient of x\u00b2)","1") + _fld("quad-b","b (coefficient of x)","\u22123") + _fld("quad-c","c (constant)","2")),
("aspect-ratio","Aspect Ratio Calculator","Scale dimensions while keeping the exact aspect ratio",
 "Aspect ratios decide whether an image fits a frame, a video fills a screen or a thumbnail crops correctly. This calculator takes your original dimensions and one new measurement, then computes the other so proportions stay pixel-perfect \u2014 the fastest way to resize without distortion.",
 "new height = new width \u00d7 (original height / original width)",
 "1920 \u00d7 1080 resized to 1280 wide gives 720 high",
 ["image and video resizing","CSS layout and embed sizing","print and frame sizing","thumbnail production"],
 "Rounding the computed side to a whole pixel shifts the ratio slightly; for strict layouts, crop rather than round.",
 "arCalc", _fld("ar-w","Original width","1920") + _fld("ar-h","Original height","1080") + _fld("ar-nw","New width","1280")),
("profit-margin","Profit Margin Calculator","Margin and markup from revenue and cost",
 "Margin and markup are the two numbers every business quotes and every business confuses. Margin is profit as a share of the selling price; markup is profit as a share of cost. This calculator returns both from revenue and cost, plus the absolute profit, so quotes and reports use the right figure.",
 "Margin = (revenue \u2212 cost) / revenue \u00d7 100;  Markup = (revenue \u2212 cost) / cost \u00d7 100",
 "Revenue 1,000 with cost 650 gives a 35% margin, a 53.8% markup and 350 profit",
 ["pricing and quote preparation","retail and wholesale checks","financial reporting","negotiating supplier costs"],
 "A 50% margin is a 100% markup \u2014 quoting one when the other was asked for has derailed more pricing conversations than any other slip.",
 "pmCalc", _fld("pm-rev","Revenue (selling price)","1000") + _fld("pm-cost","Total cost","650")),
("log-calculator","Logarithm Calculator","Log of any number in any base, including natural log",
 "Logarithms answer 'how many times must I multiply the base to reach this number?' \u2014 they convert multiplication into addition and power curves into straight lines. They drive pH values, decibels, earthquake magnitudes, algorithm complexity and compound growth. This calculator computes log in any base you choose.",
 "log_b(x) = ln(x) / ln(b)",
 "log base 2 of 8 gives exactly 3",
 ["algorithm complexity analysis","pH, decibels and magnitudes","compound growth timelines","algebra and precalculus"],
 "The base matters enormously: log of 1000 is about 6.9 in base 10 but 3 in base 2 \u2014 always confirm which base a problem expects.",
 "logCalc", _fld("log-x","Number (the argument)","8") + _fld("log-b","Base","2")),
("hours-calculator","Hours Calculator","Hours and minutes between a start and end time, with break deduction",
 "Adding up worked time is a weekly chore with a surprising number of traps: crossing midnight, unpaid breaks, decimal versus clock notation. This calculator takes a start and end time, subtracts an optional break, and reports the total in both hours-and-minutes and decimal hours \u2014 the two formats timesheets actually ask for.",
 "Total = (end \u2212 start) \u2212 break, shown as H:MM and decimal hours",
 "09:00 to 17:30 with a 30-minute break gives 8h 00m, or 8.0 decimal hours",
 ["timesheets and payroll","freelance billing","shift handover planning","study and project logs"],
 "Shifts that cross midnight need the end time treated as the next day \u2014 the tool handles this automatically, but manual math usually forgets.",
 "hrsCalc", '<div class="row"><div><label for="hr-s">Start time</label><input type="text" id="hr-s" class="dt-input" readonly placeholder="09:00" /><input type="hidden" id="hr-sv" value="09:00" /></div><div><label for="hr-e">End time</label><input type="text" id="hr-e" class="dt-input" readonly placeholder="17:30" /><input type="hidden" id="hr-ev" value="17:30" /></div></div>' + _fld("hr-br","Unpaid break (minutes)","30")),
("fuel-cost-calculator","Fuel Cost Calculator","Trip fuel cost from distance, efficiency and price",
 "Whether a trip is worth driving, which of two cars is cheaper, or how to split costs between passengers \u2014 all of it reduces to distance \u00f7 efficiency \u00d7 price. This calculator does that in one step and shows the fuel volume used, so you can plan travel budgets on real numbers instead of gut feel.",
 "Cost = (distance / 100) \u00d7 consumption per 100 km \u00d7 price per liter",
 "500 km at 8 L/100km with fuel at 1.65 per liter costs 66.00",
 ["road trip budgeting","splitting costs between travelers","comparing vehicle running costs","expense reports"],
 "Efficiency figures from the brochure assume ideal conditions; city driving commonly uses 15\u201330% more fuel than the rating suggests.",
 "fuelCalc", _fld("fc-d","Trip distance (km)","500") + _fld("fc-e","Consumption (L per 100 km)","8") + _fld("fc-p","Fuel price per liter","1.65")),
("cube-root","Cube Root Calculator","Cube root of any number, including negatives",
 "The cube root inverts cubing: it answers 'what number times itself three times gives this?' It appears in volume problems (a box of 27 cubic units is 3 on a side), scaling laws, density calculations and graphics. Unlike square roots, cube roots exist for negative numbers too \u2014 the cube root of \u221227 is \u22123 \u2014 and this tool handles both signs.",
 "x = \u221b n, verified by x \u00d7 x \u00d7 x = n",
 "27 gives exactly 3, and \u221227 gives \u22123",
 ["volume and capacity problems","scaling in physics and biology","graphics and 3D modeling","homework verification"],
 "Volume scales with the cube of length: doubling a box's sides multiplies its volume eight times, which is why the cube root \u2014 not half \u2014 reverses that.",
 "cbrtCalc", _fld("cbrt-n","Number","27")),
("percentage-change","Percentage Change Calculator","Increase or decrease between two values, with direction",
 "Percentage change is how everything is reported \u2014 prices, revenue, followers, test scores \u2014 and it is asymmetric on purpose: a rise from 80 to 100 is +25%, but a fall from 100 to 80 is \u221220%. This calculator computes the change with the correct sign and shows the absolute difference, so reports state the movement honestly.",
 "Change % = (new \u2212 old) / old \u00d7 100",
 "From 80 to 100 is a +25% increase; from 100 to 80 is a \u221220% decrease",
 ["price and revenue reporting","KPI dashboards","investment performance","A/B test analysis"],
 "The old value must be the denominator \u2014 swapping old and new flips the sign and the size of the answer, which is how inflated growth claims happen.",
 "pctChCalc", _fld("pc-old","Old value","80") + _fld("pc-new","New value","100")),
("hypotenuse-calculator","Hypotenuse Calculator","Longest side of a right triangle from the other two",
 "The Pythagorean theorem is the most used relation in practical geometry: squaring walls, checking corners, computing screen diagonals, GPS distance shortcuts, graphics collision math. This calculator takes the two shorter sides and returns the hypotenuse, verifying the result by squaring it back.",
 "c = \u221a(a\u00b2 + b\u00b2)",
 "Sides 3 and 4 give a hypotenuse of exactly 5",
 ["construction and squareness checks","screen and TV diagonal sizing","navigation distance estimates","game and graphics math"],
 "The theorem only holds for right triangles \u2014 for any other triangle the longest side depends on the angles and needs the law of cosines.",
 "hypCalc", _fld("hy-a","Side a","3") + _fld("hy-b","Side b","4")),
("ratio-simplifier","Ratio Simplifier","Reduce any ratio to its simplest whole-number form",
 "Ratios appear in mixing instructions, screen resolutions, gear ratios, cooking and design grids \u2014 and an unsimplified ratio hides the pattern. This calculator reduces any two-number ratio to lowest terms using the GCD, and shows the decimal relationship so you can compare ratios numerically too.",
 "Divide both parts by their GCD (e.g. 1920:1080 \u2192 16:9)",
 "1920 : 1080 simplifies to 16 : 9",
 ["screen and video resolutions","mixing chemicals or ingredients","design grids and layouts","betting and probability odds"],
 "Simplifying loses the scale: 16:9 and 160:90 describe the same shape but different sizes \u2014 keep the original numbers when size matters.",
 "ratioCalc", _fld("rs-a","First quantity","1920") + _fld("rs-b","Second quantity","1080")),
]

CALC_CTX = ("Every calculator on this site solves one question completely rather than many questions badly. The {name} focuses on the single formula that matters for its job, exposes only the inputs that formula needs, and shows its result immediately so you can check it against your own estimate. "
"That focus is deliberate: a page with two or three inputs you understand beats a dashboard of fields you have to guess at. "
"You will find this tool useful whenever the question comes up \u2014 {u1}, {u2} or {u3} \u2014 and it behaves identically on a phone, a tablet and a desktop.")

CALC_W3 = ("The math runs in your browser the moment you press Calculate, using JavaScript's double-precision floating point \u2014 the same 64-bit standard that spreadsheets use. "
"For the {name} that means results are accurate to roughly 15 significant digits, far beyond what the task requires, and the display rounds sensibly instead of truncating. "
"Nothing is uploaded: the numbers you enter never leave your device, the page keeps working if your connection drops, and there is no quota, account or waiting on a remote server.")

CALC_PRIV = ("Because the calculation is local, the tool is also safe for figures you would rather not paste into an unknown website \u2014 salaries, invoices, grades, medical numbers. "
"Nothing is transmitted, nothing is logged, and closing the tab clears every field. "
"The result is deterministic too: the same inputs always produce the same output, so you can reproduce any figure you quote later.")

def _calc_extra_faqs(name):
    return [
 ("Is the {name} free to use?".format(name=name), "Yes \u2014 like every tool on this site it runs entirely in your browser with no sign-up, no usage limits and no watermark on results."),
 ("How accurate are the results?", "The calculation uses 64-bit double-precision floating point, giving about 15 significant digits of accuracy. Displayed values are rounded for readability, but the underlying result carries full precision."),
 ("Does it work on a phone?", "Yes. The layout adapts to small screens and the same math runs in every modern mobile browser, so you can use it standing in a store or on a job site."),
 ("Is my data sent anywhere?", "No. All computation happens locally in your browser; the inputs are never transmitted, stored or logged anywhere."),
 ("Can I use it offline?", "After the page has loaded once, the calculation keeps working without a connection, because everything runs in local JavaScript."),
 ("What if the result looks wrong?", "Check the inputs for typos and unit mismatches first \u2014 the tool computes exactly what the formula says for the values given. Comparing against a rounded mental estimate usually exposes a wrong entry in seconds."),
]

def calc_article(f):
    slug, name, short, about, formula, exline, uses, got, fn, extra = f
    labels = re.findall(r'<label[^>]*>([^<]+)</label>', extra)
    l0 = labels[0].lower() if labels else "the first field"
    l1 = labels[1].lower() if len(labels) > 1 else "the second field"
    l2 = labels[2].lower() if len(labels) > 2 else "the remaining fields"
    intro = [
        about + " The calculator on this page implements the standard formula, shows the result the instant you press Calculate, and works entirely in your browser \u2014 free, with no sign-up and nothing uploaded.",
        CALC_CTX.format(name=name, u1=uses[0], u2=uses[1], u3=uses[2]),
        CALC_W3.format(name=name),
    ]
    how = (f"Enter your values in the fields above \u2014 {l0}, {l1} and {l2} \u2014 then press the Calculate button. "
           "The result appears below with the figures you need, formatted to a sensible number of decimals. "
           "Change any input and press Calculate again to recompute; there is no page reload and nothing to reset. "
           "If a field is left blank or contains invalid text, the tool tells you what is missing instead of producing a silently wrong answer. "
           "For repeat work, keep your typical inputs in a note so you can reproduce any past result exactly.")
    steps = [
        f"Fill in {l0} with your value \u2014 plain numbers only, no commas or unit symbols.",
        f"Fill in {l1} with the matching value, making sure both use the same units.",
        "Check any remaining fields " + ("(" + l2 + ")" if len(labels) > 2 else "for typos") + " so nothing is missing or doubled.",
        "Press the Calculate button \u2014 the result appears immediately below the form.",
        "Read the full output, including any breakdown or verification line, not just the headline number.",
        "Adjust an input and recalculate to test scenarios \u2014 that is usually where the real insight comes from.",
    ]
    works = [
        f"The {name} implements {formula}, which is the standard relationship used in textbooks, reference tables and professional practice for this exact question. "
        "The page does not improvise a shortcut or a rounded constant \u2014 it performs the same operation a careful person would do with a calculator and a formula sheet, just without the slips.",
        "Precision is handled deliberately. JavaScript computes with 64-bit double-precision floating point, so intermediate values keep about 15 significant digits and only the displayed result is rounded. "
        "That ordering matters: rounding early is the classic way small errors become large ones, and the tool avoids it by construction.",
        CALC_PRIV,
    ]
    examples = [
        ("Worked example", f"{exline} That is the kind of figure you can copy straight into a document, and because the tool shows the full result you can trace where every part of it came from."),
        ("Check it against a rough estimate", f"Before trusting any calculator, round the inputs and run the math in your head: with {formula.split('(')[0].strip()} the ballpark is easy to see. If the tool's answer and your estimate differ by a factor \u2014 not a few percent \u2014 an input is wrong, and you have caught it in seconds instead of after the report goes out."),
        ("Where this matters", f"This calculation earns its keep in {uses[0]}, {uses[1]} and {uses[2]}. In each of those settings the same pattern applies: the arithmetic itself is simple, but doing it by hand under time pressure \u2014 or doing it slightly differently each time \u2014 is what produces inconsistencies that are expensive to untangle later."),
    ]
    mistakes = [
        "Leaving a field blank or typing text into a number input. The calculator reports incomplete inputs rather than guessing, so fill every field before pressing Calculate.",
        "Mixing units across inputs \u2014 for example entering one value in centimeters and another in meters. Convert everything to a single unit first and the formula takes care of the rest.",
        got,
        "Rounding intermediate results when chaining calculations. Keep full precision until the final step, then round once.",
        "Forgetting that the output is not saved. A refresh resets the form, so copy any figure you need into your notes before leaving the page.",
    ]
    tips = [
        f"Bookmark the {name.lower()} if you run this calculation regularly \u2014 loading the page is faster than searching for the formula each time.",
        "Use Tab to move between fields and Enter to recalculate; the whole workflow works without touching the mouse.",
        "If a result looks wrong by a factor of ten or a hundred, hunt for a unit mismatch before doubting the math.",
        "State the inputs next to the result in any report (\u201c" + exline.split(" gives ")[0] + "\u201d) so a reader can reproduce the number.",
        "Sanity-check with a rounded estimate before trusting the precise figure \u2014 agreement within a few percent means both are probably right.",
        "Test edge cases once (zero, a large value, a negative) so you know how the tool behaves before it matters.",
    ]
    faqs = [
        ("What formula does this calculator use?", f"It uses {formula} \u2014 the standard relationship for this calculation, identical to what reference books and professional tools apply."),
        ("Can I use decimals and negative numbers?", "Yes. The number inputs accept decimals, and negative values are handled where they are mathematically meaningful \u2014 the tool explains it when they are not."),
        ("Does the calculator store my inputs?", "No. Everything is computed in your browser's memory and discarded when you close or reload the page."),
        ("Why is this better than a spreadsheet formula?", f"For a one-off question it is faster: no file to open, no formula to remember, no cell references to get wrong. For repeated bulk work a spreadsheet wins \u2014 the {name.lower()} is the quicker path for the single case in front of you."),
    ]
    a = {"intro": intro, "how": [how], "steps": steps, "works": works,
         "examples": examples, "mistakes": mistakes, "tips": tips, "faqs": faqs,
         "_fn": name, "_tn": "result"}
    return _fit(a)

def calc_body(f):
    slug, name, short, about, formula, exline, uses, got, fn, extra = f
    tail = ('<div id="cb2-meta" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="cb2Copy(\'' + fn + '\', this)">Copy result</button>'
            '<button type="button" class="btn ghost" onclick="cb2Reset()">Reset</button></div>')
    return f'''<div class="panel">
  <div class="row">
  {extra}
  </div>
  <button class="btn" onclick="{fn}()">Calculate</button>
  <div id="{fn}-out" class="result" aria-live="polite">Fill in the fields to see the result.</div>{tail}
  <script>window.CB2_FN="{fn}";</script>
</div>'''
