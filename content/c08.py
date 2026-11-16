# Batch 8: password-generator, color-converter, palette-generator, random-number-generator, dice-roller, coin-flipper, date-difference-calculator, image-resizer
CONTENT = {
"password-generator": {
"intro": [
"Most account takeovers do not involve clever hacking; they involve reused or guessable passwords. A strong password is long, random and unique, and the only practical way to get all three is to generate them. This Password Generator creates strong random passwords with any combination of length and character types, and shows an entropy estimate so you can see the strength, not just hope for it.",
"Set the length, choose which character sets to include, and generate. The tool uses your browser's cryptographic random number generator, the same source used for security-sensitive operations, so the passwords are genuinely unpredictable rather than pseudo-random leftovers from a simple algorithm.",
"Use it for new accounts, for upgrading old weak passwords one by one, for Wi-Fi keys, for encryption passphrases, and anywhere a memorable-but-weak password is currently doing a security-sensitive job. Everything happens locally: generated passwords never touch a server.",
],
"how": [
"Choose a length and toggle the character types you want, then generate. The entropy estimate updates with your settings, so you can see exactly how each choice affects strength. Generate repeatedly until you have what you need, then copy.",
],
"steps": [
"Set the password length; sixteen or more is a good default.",
"Toggle character sets: uppercase, lowercase, digits and symbols.",
"Check the entropy estimate to confirm the strength meets your needs.",
"Click generate to create the password.",
"Copy it straight into your password manager.",
],
"works": [
"Strength against guessing is measured in entropy, expressed in bits. Each bit doubles the number of guesses an attacker would need. The tool computes entropy from the length and the size of the character pool: length times the base-2 logarithm of the pool size. Sixteen characters drawn from all four sets, a pool of about 95 characters, yields roughly 105 bits, far beyond any realistic brute-force attack.",
"The random source matters as much as the length. The tool draws from the browser's cryptographic random generator, designed so that outputs cannot be predicted from previous outputs. Passwords made from human-chosen patterns, names, dates and substitutions like a for an at, have dramatically less real entropy than their length suggests, which is why generated randomness wins.",
"Length beats complexity. A twenty-character password of just lowercase letters carries more entropy than an eight-character password using every symbol. This is why the tool lets you push length high, and why the estimate updates live: you can watch four extra characters add more strength than every symbol combined.",
],
"examples": [
("Upgrading an old account", "An old email password turns out to be a name and a birth year. Generating a twenty-character replacement and storing it in a password manager upgrades the account from trivially guessable to effectively unbreakable."),
("Creating a Wi-Fi passphrase", "A home network needs a key that guests can type but attackers cannot guess. A sixteen-character password with letters and digits balances typeability with roughly 95 bits of entropy."),
("Seeding a passphrase", "For systems where you must remember the password, generate several short random words worth of characters as a base, then build a memorable phrase around them rather than inventing one from memory."),
],
"tips": [
"Prefer length: each extra character multiplies the work an attacker must do.",
"Use every character set unless a system forbids it; the pool size drives entropy.",
"Store passwords in a password manager rather than reusing variations of one password.",
"Never reuse a generated password across accounts; uniqueness contains any single breach.",
"Check the entropy estimate, not how the password looks; randomness is not the same as strength.",
],
"faqs": [
("How long should a password be?", "Sixteen characters with mixed sets is a strong default for most accounts. Twenty or more is a sensible choice for anything high-value like email or banking."),
("Are these passwords truly random?", "Yes. They come from the browser's cryptographic random number generator, which is designed for security-sensitive use and is not predictable from previous outputs."),
("What is entropy, in plain terms?", "It measures how many guesses an attacker would need. Each bit doubles the guess count, so a 100-bit password is beyond any realistic brute-force effort."),
("Can I include symbols if a site rejects them?", "Yes, toggle the symbol set off and regenerate. The estimate updates so you can compensate with a little extra length."),
("Is it safe to generate passwords in a browser tool?", "Here, yes: generation uses your device's cryptographic source and the password is never transmitted or stored. Close the tab when you are done."),
("Should I change passwords regularly?", "Modern guidance says change on evidence of compromise, not on a calendar. A strong unique password plus prompt updates when a breach affects you is the better pattern."),
],
},
"color-converter": {
"intro": [
"Colour appears in different notations depending on where you work: HEX in design files and CSS, RGB in screens and image editors, HSL when humans need to reason about hue, saturation and lightness. This Color Converter translates between HEX, RGB and HSL instantly, with a live preview of the colour itself.",
"Paste any colour in any of the three formats and the tool shows it in the other two immediately, alongside a swatch so you can confirm you have the colour you meant. Values update as you type, and each format is ready to copy in the exact syntax CSS expects.",
"Developers use it to move colours from design tools into stylesheets, designers use it to hand off colours in the format each tool needs, and learners use it to see how the same colour is described three ways. The preview is the safety net: notation mistakes are caught by the eye before they reach production.",
],
"how": [
"Paste a colour in HEX, RGB or HSL form and all three representations update at once, with a preview swatch alongside. Copy whichever syntax you need; editing any one field re-derives the others.",
],
"steps": [
"Paste or type a colour in HEX, RGB or HSL format.",
"Read the equivalent values in the other two formats.",
"Check the preview swatch to confirm the colour is what you intended.",
"Copy the format your stylesheet or tool requires.",
"Adjust values in any format to explore nearby colours.",
],
"works": [
"HEX notation is a compact form of RGB: six hex digits are three pairs giving red, green and blue from 0 to 255. Converting HEX to RGB is therefore a base conversion, and converting to HSL is a well-defined transformation into cylindrical coordinates: hue is the angle around the colour wheel, saturation the distance from grey, lightness the position between black and white.",
"HSL exists because it matches how people think about colour changes. Making a colour lighter is a lightness adjustment, not a redesign of three RGB values. This is why the tool's HSL output is so useful for generating variations: shift the hue for a different colour at the same vibrancy, or raise lightness for a tint, and the relationships stay intuitive.",
"The preview swatch closes the loop. Notation errors, a five-digit hex, swapped RGB channels, a hue of 400, are caught visually, because the swatch shows what the parsed values actually produce. What you see is derived from the parsed values, not from your input string, which is exactly what a converter should do.",
],
"examples": [
("Design handoff", "A designer specifies a brand colour as HEX 1A73E8. The developer copies the RGB form for a canvas operation and the HSL form for generating a lighter hover state at the same hue, all from one conversion."),
("Building a hover state", "A button's base colour converts to HSL, the lightness is raised ten points for the hover variant, and the result converts back to HEX for the stylesheet. The two colours stay visibly related because only lightness moved."),
("Debugging a colour mismatch", "A colour looks wrong on screen. Converting the CSS value shows its RGB channels, revealing that two channels were transposed somewhere in the pipeline. The preview makes the error obvious at a glance."),
],
"tips": [
"Use HSL when you need to reason about a colour; use HEX or RGB when you need to write it into code.",
"The preview shows the parsed colour; trust it over your reading of the notation.",
"Three-digit HEX shorthand expands each digit doubled, so F53 is FF5533.",
"Hue is a circle: 0 and 360 are the same red, and crossing 360 wraps around.",
"Screen colours depend on display settings; convert values, but judge final colours on target devices.",
],
"faqs": [
("What is the difference between HEX and RGB?", "None in meaning. HEX is a base-16 shorthand for the same red, green and blue values. FF0000 and rgb(255, 0, 0) are the same colour written differently."),
("When should I use HSL?", "Whenever you are reasoning about or varying a colour: lightness for tints and shades, saturation for vibrancy, hue for colour family. It matches human colour intuition."),
("Can it parse colours with alpha, like RGBA?", "This tool focuses on the three opaque formats. For transparency, extend the RGB value with an alpha channel in your stylesheet after converting."),
("Why does my three-digit HEX work?", "CSS shorthand doubles each digit, so F53 is interpreted as FF5533. The tool follows the same rule."),
("Are converted values exact?", "Yes. The conversions between the formats are mathematically defined, so values match any compliant tool for the same colour."),
("Is anything uploaded?", "No. Conversion and preview happen entirely in your browser."),
],
},
"palette-generator": {
"intro": [
"Every good colour scheme starts from one colour and grows outward: a darker shade for pressed states, a lighter tint for backgrounds, neighbours that harmonise. This Palette Generator takes any base colour and produces its shades and tints systematically, each one click to copy.",
"Pick a base colour and the tool builds a full ramp: shades stepping toward black and tints stepping toward white, all sharing the base colour's hue and character. The result is the kind of scale design systems use, where every step has a defined role in an interface.",
"Designers use it to build product palettes that hold together; developers use it to fill in the missing steps of a design token scale; anyone creating charts, presentations or themes uses it to get a consistent family of colours from a single brand colour rather than improvising.",
],
"how": [
"Choose a base colour, and the palette appears immediately: a row of shades darkening below it and tints lightening above it. Click any swatch to copy its value. Adjust the base and the whole ramp follows.",
],
"steps": [
"Pick your base colour using the picker or by pasting a value.",
"Review the generated shades, stepping darker from the base.",
"Review the tints, stepping lighter from the base.",
"Click a swatch to copy its colour value.",
"Adjust the base colour to regenerate the entire ramp around the new colour.",
],
"works": [
"Shades and tints are defined by lightness. A tint mixes the base colour with white, raising lightness while keeping hue and character; a shade mixes it with black, lowering lightness. The generator steps lightness by fixed intervals, producing an evenly spaced ramp rather than ad-hoc eyeballed steps.",
"Keeping hue and saturation constant across the ramp is what makes the result feel like a family. Random darker colours rarely relate to their base; systematic lightness changes always do. This is the same principle behind the numbered colour scales in design systems, where each step has a consistent relationship to its neighbours.",
"Click-to-copy is the workflow feature that matters: building a real palette means moving a dozen values into CSS or a design tool, and friction there adds up. Each swatch copies in standard HEX form, ready to paste without further conversion.",
],
"examples": [
("Building a brand colour scale", "A product's primary colour becomes a full ramp: the darkest shade for text on light backgrounds, mid steps for hover states, the base for primary buttons, and tints for surfaces and highlights."),
("Filling in missing design tokens", "A design system defines steps 100, 500 and 900 but the implementation needs every step. Generating a ramp from the 500 value supplies consistent intermediates instead of guesses."),
("Chart and data colours", "A report needs five related colours for a series. A ramp from one hue gives steps that are clearly related but visually distinct, which is exactly what sequential data needs."),
],
"tips": [
"Choose the base colour from your brand or design first; the ramp inherits its character.",
"Use tints for backgrounds and surfaces, shades for text and pressed states.",
"Consistent steps read as intentional; avoid mixing ramp steps with ad-hoc colours.",
"Check contrast between text and background steps for accessibility as you assign roles.",
"Click-to-copy outputs HEX, ready for CSS and most design tools.",
],
"faqs": [
("What is the difference between a shade and a tint?", "A shade mixes the base with black, making it darker; a tint mixes it with white, making it lighter. Both keep the base colour's hue."),
("How many steps does the palette include?", "The generator produces an evenly spaced ramp of shades and tints around your base, enough to cover the usual roles in an interface or document."),
("Can I export the whole palette at once?", "Each swatch copies individually on click, which keeps the workflow simple and works with every tool that accepts pasted colour values."),
("Why do my ramp colours look different on another screen?", "Displays vary in calibration and profile. The values are exact; judge final colours on the devices your audience actually uses."),
("Can I start from a colour in another format?", "Yes. Convert it with the Color Converter first, or paste the HEX form directly as the base."),
("Is anything uploaded?", "No. Palette generation happens entirely in your browser."),
],
},
"random-number-generator": {
"intro": [
"A random number is useful in more situations than it first appears: picking a winner from a range, simulating dice and games, sampling data, choosing a pin, shuffling decisions, or just breaking a tie fairly. This Random Number Generator produces random integers in any range you specify, with an option to keep every pick unique.",
"Set the minimum and maximum, say how many numbers you need, and generate. Results appear instantly, and the unique option guarantees no repeats, which is exactly what draws, sampling and raffles require. Generate as many times as you like; each run is independent.",
"Teachers use it for classroom draws and problem sets, developers for test data and game logic, researchers for simple sampling, and anyone running a giveaway for verifiably fair selection. It runs entirely in your browser using a solid random source, so the results are as fair as the platform allows.",
],
"how": [
"Enter the range and the count, toggle uniqueness if you need it, and generate. The numbers appear immediately and can be copied as a list. Changing the range or count and regenerating takes a second.",
],
"steps": [
"Set the minimum value of the range.",
"Set the maximum value of the range.",
"Choose how many numbers to generate.",
"Enable unique mode if repeats are not allowed.",
"Generate and copy the results.",
],
"works": [
"The tool generates uniformly distributed integers in your chosen range: every value in the range is equally likely on each pick. It uses the browser's random source, which is suitable for games, draws and sampling, though not for cryptographic keys; for security purposes use the Password Generator instead.",
"Unique mode changes the selection model from independent picks to drawing without replacement, like pulling numbered balls from a bowl. Each new pick comes from the remaining values, so no number repeats. This is the right mode for raffles, assigning unique slots, and sampling without replacement; leave it off for dice-style rolls where repeats are natural.",
"Range boundaries are inclusive: a range of 1 to 100 can produce both 1 and 100. This matches how people state ranges in everyday language and avoids the classic off-by-one surprise where the maximum never appears.",
],
"examples": [
("Running a raffle", "Two hundred ticket numbers go into the range 1 to 200, five winners are needed, and unique mode guarantees five different winners. The result is a fair, instantly verifiable draw."),
("Creating test data", "A developer needs fifty random values between 1 and 1,000 to exercise a sorting function. Generating them instantly beats inventing numbers, and regenerating produces a fresh batch for each test run."),
("Classroom randomness", "A teacher needs ten random subtraction problems with numbers under 100. Two generations produce the numbers; the exercise writes itself, and every student gets a different set."),
],
"tips": [
"Enable unique mode for draws and disable it for dice-style rolls where repeats are expected.",
"Ranges are inclusive on both ends, so 1 to 10 can return 1 and 10.",
"For a coin-flip decision, generate a number from 1 to 2 instead of overthinking it.",
"For cryptographic purposes like keys, use a dedicated security tool rather than a general random generator.",
"Copy results as a list for pasting into spreadsheets or documents.",
],
"faqs": [
("How random are the numbers?", "They come from your browser's random source, which is high quality for games, draws and sampling. It is not certified for cryptographic key generation."),
("What does unique mode do?", "It draws without replacement, so no number appears twice, like raffle balls from a bowl. Without it, each pick is independent and repeats can occur."),
("Are the range endpoints included?", "Yes. Both minimum and maximum can appear in the results."),
("Can I generate decimal numbers?", "This tool generates integers, which covers draws, games and sampling. For decimals, generate in a wider range and divide in your head or a spreadsheet."),
("Is there a limit on how many I can generate?", "You can generate large batches instantly; the practical limit is what you want to read and copy."),
("Is anything uploaded?", "No. Generation happens entirely in your browser."),
],
},
"dice-roller": {
"intro": [
"Physical dice get lost, biased and disputed, and some games need dice nobody owns, like a twenty-sided die or five dice at once. This Dice Roller rolls up to twenty dice with any number of sides, showing each die's result and the total, with rolls that are as fair as software can make them.",
"Choose the number of dice, choose the sides per die, from classic six-sided to twenty-sided and beyond, and roll. Each die's individual value is displayed alongside the sum, so games that care about individual rolls and games that care about totals both work naturally.",
"Board game players use it when the physical dice are missing or disputed, tabletop role-players use it for polyhedral dice they do not own, teachers use it for probability demonstrations, and anyone making a quick decision uses it to let chance decide. It runs entirely in your browser with no setup.",
],
"how": [
"Set how many dice to roll and how many sides each has, then roll. Every die's value appears individually along with the total, and rolling again takes one click.",
],
"steps": [
"Set the number of dice, from one to twenty.",
"Set the number of sides per die, such as 6, 10 or 20.",
"Click roll to throw all the dice at once.",
"Read each die's individual result and the combined total.",
"Roll again as often as needed; each roll is independent.",
],
"works": [
"Each die is an independent random integer from 1 to its number of sides, generated uniformly so every face is equally likely. The total is simply the sum of the individual values, which are all displayed, so nothing about the roll is hidden.",
"Independence is the property that makes digital dice fair: no roll is influenced by previous rolls, and every face of every die has the same chance every time. Physical dice develop wear and throwing habits that bias results; digital dice do not, which is why groups sometimes prefer them for important rolls.",
"The multi-dice display matters for games that read individual dice, not just totals. Role-playing systems check for individual maximums and minimums; probability lessons compare the distribution of individual dice against the bell-shaped distribution of sums. Showing both supports all of these uses without any extra settings.",
],
"examples": [
("Board game night", "The dice are under the sofa and nobody wants to pause the game. Roll two six-sided dice per turn with individual results shown, and the game proceeds without dispute."),
("Tabletop role-playing", "A party needs four twenty-sided dice for a check. Rolling four d20s shows each result individually, which is exactly what the system requires for its rules."),
("Probability lessons", "A class rolls thirty six-sided dice and watches the individual results spread across all faces, then compares the totals against the expected bell curve. More rolls make the pattern clearer."),
],
"tips": [
"Individual die results matter for many games; read them before collapsing to the total.",
"Each roll is independent; streaks mean nothing statistically, however they feel.",
"For a single decision, one die with two sides is a coin flip.",
"Set dice to 1 and sides to your range maximum for a simple uniform pick.",
"Rolling many dice at once is a quick way to demonstrate probability distributions.",
],
"faqs": [
("Are the rolls fair?", "Each die uses a uniform random source, so every face is equally likely and rolls are independent. Fairness matches or exceeds typical physical dice."),
("Can I roll different-sized dice together?", "This tool rolls dice of one size per throw. Roll each size separately and add the results for mixed pools."),
("How many dice can I roll at once?", "Up to twenty per roll, which covers virtually every game and classroom use."),
("Can I use it for a d100 roll?", "Yes. Set one die with one hundred sides, or roll two ten-sided dice and use your system's percentile convention."),
("Does it remember previous rolls?", "Each roll replaces the display. For record-keeping, copy the results after each roll."),
("Is anything uploaded?", "No. Rolling happens entirely in your browser."),
],
},
"coin-flipper": {
"intro": [
"The coin flip is the world's smallest decision procedure: two outcomes, equal odds, no arguments. This Coin Flipper flips one coin or a thousand, showing each result and running counts of heads and tails, so it works for a quick decision and for probability demonstrations alike.",
"Choose how many coins to flip and flip. Individual results appear as a sequence of heads and tails, with live totals showing the running balance. Flip again as often as you like; each flip is independent and fair.",
"Beyond settling everyday disputes, the tool is a compact probability lab: flipping ten coins shows how uneven results are normal, flipping a thousand shows the ratio settling toward half, and the running counts make the law of large numbers visible instead of abstract. It runs entirely in your browser.",
],
"how": [
"Set the number of coins, from one to a thousand, and flip. Results display immediately with running totals for heads and tails. One coin gives a single instant answer; many coins give the statistical picture.",
],
"steps": [
"Set the number of coins to flip, from 1 to 1,000.",
"Click flip to toss them all at once.",
"Read the sequence of results, heads and tails.",
"Check the running counts and ratio of heads to tails.",
"Flip again for a fresh, independent set of results.",
],
"works": [
"Each coin is an independent random choice between two equally likely outcomes, generated from your browser's random source. Fairness here means exactly 50 percent probability per flip and independence between flips, the two properties physical coins approximate and digital coins implement cleanly.",
"The running counts turn the tool into a demonstration. With ten flips, a 7-3 split is entirely ordinary; with a thousand flips, the ratio reliably drifts toward 50-50 even though short streaks never stop appearing. Watching the counts across successive flips makes the difference between short-run luck and long-run probability tangible.",
"One thousand coins per flip is also a practical limit chosen for readability: the sequence display stays meaningful, and the totals update instantly. For larger experiments, flip repeatedly and add the counts, which itself mirrors how real probability experiments are conducted.",
],
"examples": [
("Settling a decision", "Two options, one coin. A single flip decides, and the answer arrives without the negotiation that usually follows an informal maybe."),
("Probability homework", "A student flips one hundred coins and compares the heads count against the expected fifty, then flips again to see the variation between trials. The abstract idea of random variation becomes concrete."),
("Best-of series", "A best-of-five needs five flips, read as a sequence rather than a total. Setting five coins and reading the majority result settles the series in one throw."),
],
"tips": [
"One coin answers decisions; many coins demonstrate probability.",
"Short-run imbalance is normal; only large counts approach an even ratio.",
"Each flip is independent, so past results never change future odds.",
"Use the counts, not the visible sequence, for anything statistical.",
"For repeats of an experiment, flip again rather than reading more into one sequence.",
],
"faqs": [
("Are the flips fair?", "Yes. Each flip is an independent 50-50 random choice from your browser's random source."),
("Can I flip more than one coin at once?", "Yes, up to a thousand, with individual results and running totals displayed."),
("Why did I get seven heads out of ten?", "Entirely normal. With small counts, uneven splits are common; the ratio approaches half only as the number of flips grows large."),
("Does the tool remember my flip history?", "Each flip replaces the previous results and the counts reset, so every experiment starts fresh."),
("Is this suitable for statistics demonstrations?", "Yes. The running counts and ratio make it a compact demonstration of randomness, independence and the law of large numbers."),
("Is anything uploaded?", "No. Flipping happens entirely in your browser."),
],
},
"date-difference-calculator": {
"intro": [
"How long between two dates is a question with deceptively many answers: days is simple, but working people think in weeks, contracts in months, and life in years. This Date Difference Calculator gives all of them at once, computed properly across real calendar rules including leap years.",
"Pick a start date and an end date, and the tool reports the total days between them plus the breakdown in weeks, months and years. Both orders work: the tool computes the absolute gap, so end before start gives the same span.",
"Project managers use it for timelines and deadlines, HR for tenure and notice periods, travellers for trip lengths, students for countdowns, and anyone handling contracts, warranties or subscriptions where the exact span matters. It runs entirely in your browser, so the dates you check stay private.",
],
"how": [
"Choose two dates and read the results immediately: total days, weeks and days, and the calendar breakdown in years, months and days. Change either date and everything updates together.",
],
"steps": [
"Pick the start date.",
"Pick the end date.",
"Read the total number of days between them.",
"Check the weeks-and-days view for a more human scale.",
"Read the years-months-days breakdown for calendar-accurate phrasing.",
],
"works": [
"Total days counts the actual calendar days between the dates, inclusive of the span's length and correctly handling leap years, because the arithmetic uses real dates rather than a nominal 365-day year. This is the figure to use for interest, deadlines and anything measured in days.",
"The weeks-and-days view divides total days by seven, which is how most people actually schedule: a 45-day project is easier to plan as six weeks and three days. The remainder is shown explicitly rather than rounded away.",
"The years-months-days breakdown counts completed calendar units, borrowing across unequal month lengths the way age is calculated. This is the phrasing contracts and formal documents use: two years, three months and ten days is a different claim from 815 days, and both views are provided so you can use whichever the situation requires.",
],
"examples": [
("Project timeline", "A project starts March 3 and must finish June 30. The tool reports 119 days, or 17 weeks exactly, which becomes the number the schedule is built around rather than a vague about four months."),
("Tenure and notice periods", "An employment span from a start date to a leaving date reads as 3 years, 2 months and 14 days, the format HR systems and references require, alongside the 806-day total for records."),
("Travel and subscriptions", "A trip from the 10th to the 24th is 14 days for insurance purposes; a subscription held from one renewal to the cancellation date shows exactly how many days were paid for."),
],
"tips": [
"Decide whether your context counts the start day, the end day, or both; the tool reports the span.",
"Use the days figure for anything contractual or interest-bearing; it is unambiguous.",
"Use the weeks view for planning and the years-months-days view for formal phrasing.",
"Leap years are handled automatically, so February spans need no manual adjustment.",
"The order of the dates does not matter; the gap is reported as a positive span.",
],
"faqs": [
("Does the count include both endpoint dates?", "The tool reports the span between the dates. If your context counts both the first and last day inclusively, add one day to the total."),
("How are leap years handled?", "Automatically. The calculation uses real calendar dates, so spans containing February 29 count the extra day correctly."),
("Why do the months differ from multiplying weeks by seven?", "Months have 28 to 31 days, so a month is not exactly four weeks. The days figure and the calendar breakdown are both exact; they measure the same span in different units."),
("Can I compare a date in the past with one in the future?", "Yes. Any two valid dates work, and the span is reported as a positive gap regardless of order."),
("What is the maximum range?", "Any range your browser's date handling supports, which comfortably covers a lifetime and most historical questions."),
("Is anything uploaded?", "No. The calculation happens entirely in your browser."),
],
},
"image-resizer": {
"intro": [
"Images arrive too big for their purpose: a 4,000-pixel photo for a 400-pixel avatar, a 5-megabyte screenshot for a forum post, a PNG that should be a JPG. Uploading them anyway wastes bandwidth and time. This Image Resizer resizes and converts images entirely in your browser, with no upload at any point.",
"Drop in an image, set the target width or height, and the tool scales it while preserving aspect ratio. You can also convert the format, choosing JPEG for photographs, PNG for sharp graphics and transparency, or WebP for the best size-to-quality balance, and adjust quality to hit a target file size.",
"Because the resizing happens on your device using the browser's canvas, private photos never leave your machine, and there is no upload wait even on slow connections. Bloggers, developers, marketplace sellers and anyone attaching images to forms or emails get right-sized files in seconds.",
],
"how": [
"Select or drop an image, set the desired dimensions, choose the output format and quality, and process. The preview shows the result before you download it, so sizing and quality can be adjusted and re-processed until the file is right.",
],
"steps": [
"Select or drop your image into the input area.",
"Set the target width or height; the other dimension follows the aspect ratio.",
"Choose the output format: keep the original, JPEG, PNG or WebP.",
"Adjust the quality slider for lossy formats to balance size against sharpness.",
"Process, check the preview and file size, then download the result.",
],
"works": [
"Resizing uses the browser's canvas with high-quality scaling: the image is redrawn at the target dimensions rather than cropped or stretched. Locking to one dimension preserves the aspect ratio automatically, which prevents the distorted look that comes from setting width and height independently.",
"Format choice drives file size more than anything else. JPEG compresses photographs efficiently but discards detail and does not support transparency. PNG stores every pixel losslessly and keeps transparency, making it right for screenshots, logos and line art, at a larger size. WebP typically beats both, often producing 25 to 35 percent smaller files than JPEG at similar visual quality, with broad modern browser support.",
"Quality settings apply to lossy formats: lower quality means smaller files and progressively more visible compression artefacts, especially around sharp edges and text. The practical method is to process, inspect the preview at actual size, and step the quality down until artefacts appear, then back up one notch. The displayed file size confirms the saving before you download.",
],
"examples": [
("Preparing a profile picture", "A 3,000-pixel phone photo becomes a clean 400-pixel square avatar. Resizing with the aspect ratio preserved, then converting to JPEG at 85 percent quality, takes the file from megabytes to tens of kilobytes."),
("Lightening a blog post", "A writer's screenshots are crisp but heavy PNGs. Converting body-image screenshots to WebP at 80 percent quality typically cuts the page weight by more than half with no visible difference."),
("Meeting an upload limit", "A form accepts images up to 1 megabyte. Processing at progressively lower quality until the displayed size fits gives a compliant file in one pass, without guesswork."),
],
"tips": [
"Shrink on one dimension only and let the aspect ratio handle the other.",
"Use JPEG for photos, PNG for sharp graphics and transparency, WebP when size matters most.",
"Step quality down until artefacts appear, then back up; 75 to 85 percent is often indistinguishable.",
"Resize before uploading anywhere; sending full-resolution originals is the most common waste.",
"Keep your original file; processing here never modifies your source, it produces a new download.",
],
"faqs": [
("Are my images uploaded to a server?", "No. All processing happens in your browser using the canvas API. Your images never leave your device."),
("What is the best format for photographs?", "WebP generally gives the smallest files at equal quality, with JPEG as the universally safe fallback. PNG is the wrong choice for photos; it produces files several times larger."),
("Why did my PNG get bigger as a JPEG?", "If it was a screenshot or graphic with flat colours and sharp edges, PNG is the efficient format. JPEG suits continuous-tone photographs; converting graphics to it can inflate size and blur edges."),
("How do I hit an exact file size limit?", "Adjust quality and re-process while watching the displayed output size. Each pass takes seconds, so converging on a limit is quick."),
("Does resizing reduce image quality?", "Downscaling discards pixels by design, which is appropriate and usually invisible at display size. Quality settings on lossy formats add a separate, controllable trade-off."),
("Can it enlarge small images?", "It can scale up, but enlarging cannot recreate detail that was never captured, so results soften. Downscaling is where this tool shines."),
],
},
}
