# Expanders batch 4: converters, security, color, random, date, image
X = {
"unit-converter": {
"deep": [
"The distinction between exact definitions and measured quantities explains why some conversions feel more certain than others. An inch is defined as exactly 2.54 centimetres by international agreement, so that conversion is perfect by law. A pound is exactly 0.45359237 kilograms. Data units, by contrast, suffer from a genuine ambiguity: the engineering world says kilo means a thousand while operating systems traditionally say 1,024, and both conventions are alive. This tool uses the binary convention for data sizes because that matches what file managers report.",
"Temperature's offsets are a small piece of physics worth understanding once. Zero degrees Celsius is not zero heat; it is the freezing point of water. Fahrenheit's zero is colder still. Because the scales start at different places, ratios between temperatures are meaningless, and the conversion formulas must shift before scaling. This is also why negative temperatures in Celsius and Fahrenheit describe entirely different conditions.",
],
"mistakes": [
"Converting data sizes with the wrong convention, expecting 1,000-based values and getting 1,024-based ones.",
"Applying a ratio to temperature, which ignores the offset and produces confidently wrong answers.",
"Mixing up mass and weight units in casual use; the tool converts mass units, which is what kitchen and lab scales report.",
"Forgetting that US and imperial gallons differ by about twenty percent.",
],
"extra_faqs": [
("Why is my converted storage size different from the drive label?", "Drive makers use the 1,000-based decimal convention, while operating systems report 1,024-based binary units. Both are correct in their own convention; the gap is about seven percent per kilo step."),
("Can I convert cooking measurements like cups?", "Volume units are not in this tool's categories. Weight-based recipe conversion is more reliable anyway, since a cup of flour varies with how it is packed."),
],
},
"timestamp-converter": {
"deep": [
"Timezones are the reason timestamps exist, and they are also the source of every timestamp bug, so the model is worth spelling out. A timestamp is one absolute instant, the same everywhere in the universe. A timezone is a display rule that renders that instant as a local clock reading. The conversion bug almost everybody meets once is comparing a local clock reading against a timestamp, or storing a local time as if it were absolute. The fix is always the same: keep absolutes as timestamps, apply timezones only at the edges where humans read or speak times.",
"Leap seconds are the fine print. The Unix day is defined as 86,400 seconds, but Earth's rotation occasionally demands an extra second, which systems handle by various workarounds. For every practical purpose this noise is invisible; for high-precision systems it is a real discipline with published tables. The tool follows the standard convention, which is what every mainstream system uses.",
],
"mistakes": [
"Storing local times as timestamps, which breaks the moment the data crosses a timezone.",
"Comparing a UTC display string with a local one and concluding time is broken.",
"Assuming every timestamp is in seconds when the API actually speaks milliseconds.",
"Forgetting that date-only values, birthdays and deadlines, are not instants and should not be timestamps at all.",
],
"extra_faqs": [
("What happens at the 2038 limit?", "Systems storing timestamps as signed 32-bit seconds overflow in January 2038. Modern 64-bit systems are unaffected, which is why the industry has been migrating for years."),
("Why do some timestamps have ten digits and others thirteen?", "Seconds versus milliseconds. The magnitude tells you which, and the tool detects it automatically, which removes the most common interpretation error."),
],
},
"number-base-converter": {
"deep": [
"Two's complement is the piece of context that makes binary arithmetic in real computers coherent. Positive numbers are plain binary; negative numbers are represented by flipping all bits and adding one, which lets the same addition circuit handle signed values. This is why a byte holds values from minus 128 to 127, and why reading raw memory as unsigned produces surprising large numbers. Base conversion and signed representation are separate topics, but they meet constantly in practice.",
"Bitwise intuition is the practical payoff of binary fluency. A mask of ones selects bits, a shift multiplies or divides by two, and flags packed into a single integer are just bits read positionally. Developers who can glance at FF and see eight ones debug bit-twiddling code at a speed that decimal thinking cannot match, and the simultaneous display here is how that glance gets trained.",
],
"mistakes": [
"Pasting a hexadecimal value into the decimal field and reading a plausible but wrong number.",
"Forgetting that hex digits A through F are values, not letters.",
"Confusing the number of digits with the number of bits; two hex digits are one byte.",
"Ignoring integer precision limits for very large decimal values.",
],
"extra_faqs": [
("How do I convert by hand to check the tool?", "For decimal to binary, repeatedly divide by two and read the remainders backwards. For binary to decimal, sum the place values where ones appear. Both are quick for small numbers and build real intuition."),
("Why do programmers group bits in fours?", "Because sixteen is a power of two, each hex digit is exactly four bits. Grouping in fours makes hex and binary interconvertible by sight, which octal's three-bit grouping does for older systems."),
],
},
"roman-numeral-converter": {
"deep": [
"The history explains the rules. Roman numerals descend from tally systems, and the subtractive principle arrived late; early inscriptions happily write IIII and VIIII. Mediaeval standardisation settled on the classical canon this tool enforces. Knowing that the rules are a convention, not a law of nature, makes the surviving anomalies legible: clock faces using IIII, publishers using additive forms for stylistic effect, and the total absence of zero, which entered European arithmetic only with Hindu-Arabic numerals.",
"Reading strategy matters more than memorisation for numerals of any length. Scan for subtractive pairs first, marking IV, IX, XL, XC, CD and CM as single units worth four, nine, forty, ninety, four hundred and nine hundred. Then sum everything left to right. This two-pass reading turns an intimidating string like MMDCCCXLVIII into a handful of familiar chunks, and the converter is a good place to practise until the scan is automatic.",
],
"mistakes": [
"Writing subtractive pairs that do not exist, like IC for 99 instead of XCIX.",
"Repeating a symbol four times, which classical rules forbid.",
"Reading a subtractive pair as additive when the smaller symbol precedes the larger.",
"Forgetting the 3,999 ceiling and expecting modern-style larger numbers.",
],
"extra_faqs": [
("How did Romans do arithmetic with these numerals?", "Mostly on abacuses and with finger reckoning; the numerals were for recording results, not computing. The Hindu-Arabic system with zero is what made written calculation practical."),
("Are Roman numerals still used officially?", "Yes, in limited slots: regnal numbers, film credits, annual events, outline numbering and cornerstones. They persist where a formal, traditional look is the point."),
],
},
"password-generator": {
"deep": [
"Passphrases deserve their own explanation because they solve the memorability problem without sacrificing strength. Four or five unrelated common words, chosen at random, carry entropy comparable to a random character password of similar practical strength, while being typeable and speakable. The technique's security rests on the words being genuinely random; a passphrase from a famous quote has the entropy of the quote, which is to say none.",
"The threat model determines the right length, and it is worth reasoning about once rather than vaguely. Online attacks, guessing through a login form, are rate-limited to a few tries per second, against which even modest entropy is safe. Offline attacks, guessing against a stolen hash database, run at billions per second, which is what pushes recommendations toward sixteen characters and beyond. Since you cannot always know which model applies, generating for the harsher one is the robust choice.",
],
"mistakes": [
"Generating a strong password and then storing it in a plaintext note that defeats the purpose.",
"Using personal patterns, names or dates, which shrink real entropy far below the estimate.",
"Reusing one strong password everywhere, converting any single breach into a cascade.",
"Choosing length so extreme that typing it on shared devices encourages unsafe workarounds.",
],
"extra_faqs": [
("Can I generate a passphrase instead of characters?", "Generate a long password with lowercase only and mentally group it into chunks, or use a dedicated passphrase generator. What matters is that the words are random, not memorable to you alone."),
("Is it safe to generate passwords on a public computer?", "No. On a machine you do not trust, nothing is safe: keystrokes and clipboards may be monitored. Generate and store passwords on devices you control."),
],
},
"color-converter": {
"deep": [
"Gamma and colour spaces are the hidden reason conversions sometimes look slightly off, and a paragraph of honesty about them is worthwhile. The RGB values in CSS are encoded for display, and the mathematical relationships between RGB and HSL assume that encoding. Converting values is exact; predicting how a colour will look on an uncalibrated display is not. Designers who need colour fidelity work in managed colour spaces with calibrated displays, and everyone else works with the pragmatic knowledge that values transfer exactly and perception varies.",
"Picking between formats is also a communication decision. HEX is the compact default of the web. RGB with alpha, RGBA, is the natural choice when transparency varies. HSL is the format of choice whenever a colour will be varied systematically, because its channels correspond to the changes a designer actually wants to make. Choosing the format to match the next operation saves a conversion step later.",
],
"mistakes": [
"Reading RGB channels in the wrong order, which produces a different but plausible colour.",
"Forgetting that three-digit HEX shorthand doubles digits rather than padding with zeros.",
"Expecting screen colours to match print; screens emit light, print reflects it, and the gamuts differ.",
"Converting to HSL and treating hue as linear; it is a circle that wraps at 360.",
],
"extra_faqs": [
("What is the difference between HSL and HSB or HSV?", "They are sibling cylindrical models differing in how they define the vertical axis: HSL's lightness runs black to white through the pure colour, while HSB's brightness runs black to the pure colour. Conversions exist; the intuition differs slightly."),
("Can I convert to CMYK for print?", "Not here. Screen-to-print conversion depends on colour profiles and is a print-production task, not a formula. Convert values with profile-aware tools when preparing print work."),
],
},
"palette-generator": {
"deep": [
"Assigning roles to ramp steps is where palettes become interfaces. A common pattern: the darkest shade for primary text, a mid shade for secondary text, the base colour for primary actions, one step lighter for hover states, and the lightest tints for backgrounds, borders and surfaces. Writing this assignment down once, as a rule, turns every future colour decision into a lookup instead of a debate, which is exactly how design systems earn their keep.",
"Accessibility belongs in the palette conversation from the start, not as a retrofit. Text must contrast with its background at a ratio that readers with normal vision find comfortable and readers with low vision can still read; the common target is 4.5 to 1 for body text. A ramp makes this checkable: pick the text step and the background step and verify the pair, rather than hoping two ad-hoc colours happen to work.",
],
"mistakes": [
"Using the base colour for everything instead of assigning ramp roles, which flattens the interface's hierarchy.",
"Choosing steps by eye repeatedly instead of from a systematic ramp, which drifts over time.",
"Ignoring contrast ratios between text and background steps until an accessibility review finds them.",
"Generating a ramp from a colour that already has very low saturation, which produces muddy steps.",
],
"extra_faqs": [
("How many ramp steps does a project need?", "Enough to cover the roles: typically a handful of shades and tints around the base. More steps offer flexibility; fewer steps enforce consistency. Start small and add only when a real need appears."),
("Can I generate a palette from a photo?", "Not in this tool, which works from a single colour. Extract a dominant colour from the photo first, then generate its ramp; that two-step flow covers most photo-derived palettes."),
],
},
"random-number-generator": {
"deep": [
"Uniformity is the property that makes a random number generator fair, and it is worth knowing what it promises: every value in the range is equally likely on each draw. It does not promise that short sequences look balanced. Ten draws from 1 to 10 will frequently miss several values and repeat others; that is exactly what uniform randomness produces. Expecting short-run balance is the gambler's fallacy, and recognizing it in your own expectations is a small but real benefit of playing with these tools.",
"Sampling without replacement, the unique mode, changes the mathematics in a way that matters for fairness in draws. With replacement, every pick is independent and a person can win twice. Without replacement, each pick removes a value, and five winners are guaranteed to be five different values. Raffles, seating assignments and slot allocation want the second model; simulated dice want the first.",
],
"mistakes": [
"Using a general random generator for cryptographic keys instead of a security-focused tool.",
"Expecting short sequences to look balanced and distrusting correct results.",
"Forgetting to enable unique mode for a draw, then explaining why someone won twice.",
"Setting the range from memory instead of checking whether endpoints are inclusive.",
],
"extra_faqs": [
("Can I weight the numbers so some are more likely?", "Not in this tool, which is strictly uniform. Weighted selection is a different model; approximate it by generating in a wider range and mapping ranges to outcomes."),
("Is this suitable for statistical simulation?", "For demonstration and lightweight sampling, yes. For published research, use a statistical package with documented generators and seeds, which is a reproducibility requirement."),
],
},
"dice-roller": {
"deep": [
"The distribution of sums is the most instructive thing dice can teach, and the tool's totals make it visible. One six-sided die is uniform: every face equally likely. Two dice summed are not: seven is the most likely total because six combinations produce it, while two and twelve have one combination each. Roll a few dozen times and the humped shape emerges from the totals, which is the central-limit intuition in its simplest form.",
"Digital dice also settle the fairness disputes that physical dice invite. Worn edges, uneven surfaces and throwing style all bias physical dice in small, real ways. A uniform digital roll has no such history: no throw inherits anything from the last. Groups that argue about dice can simply agree to trust the tool, which removes an entire genre of tabletop negotiation.",
],
"mistakes": [
"Reading only the total when the game's rules depend on individual die results.",
"Believing a streak of high rolls means a low roll is due; each roll is independent.",
"Rolling mixed dice sizes in one throw, which this tool does not support; roll each size separately.",
"Forgetting that a single die with two sides is functionally a coin flip.",
],
"extra_faqs": [
("Can I roll percentile dice, a d100?", "Yes, as one die with one hundred sides, or two ten-sided dice using your game's tens-and-units convention. The result distribution is identical; the ceremony differs."),
("Why show individual dice and not just the total?", "Many games depend on individual results, such as counting successes or spotting maximums. Showing both supports every rule system without extra settings."),
],
},
"coin-flipper": {
"deep": [
"Independence is the property worth internalising, because it is where intuition reliably fails. After five heads, the sixth flip is still fifty-fifty; the coin has no memory and no obligation to balance. The running counts make this vivid: streaks of six or seven appear regularly within a few hundred flips, and none of them change the next flip's probability. This is the same misunderstanding that powers gambling systems, and watching it fail in a tool this transparent is a cheap education.",
"The thousand-coin flip is the demonstration that teaches the long run. Short sequences wobble visibly; a thousand flips settle toward half with high reliability, though never exactly. This is the law of large numbers in action, and it generalises far beyond coins: it is why casinos profit reliably on games that are individually fair-ish and individually random, and why large samples are the backbone of statistics.",
],
"mistakes": [
"Reading meaning into streaks; independence means the next flip ignores history entirely.",
"Flipping again after an unwanted result, which defeats the purpose of letting chance decide.",
"Using tiny flip counts for probability demonstrations and expecting an even split.",
"Assuming a physical coin is fairer than a digital one; worn coins have real biases.",
],
"extra_faqs": [
("Is there a way to make the flip biased?", "Not in this tool, which is strictly fair. Biased coins are a different model, used in teaching probability precisely because real coins are hard to bias in practice."),
("Why flip a thousand coins?", "To see the long run. Individual flips are unpredictable, but aggregate counts are remarkably stable, and that contrast is the foundation of statistics."),
],
},
"date-difference-calculator": {
"deep": [
"Boundary conventions are the detail that turns a date difference from a calculation into a decision, and they deserve explicit attention. Interest calculations, rental periods and legal notice periods each specify whether the start day, the end day, or both count. The tool reports the span between the dates; translating that span into the convention your document uses is a one-line decision, but making it explicitly is what prevents the off-by-one that surfaces in an audit.",
"Month arithmetic has a quirk worth knowing because it affects the years-months-days breakdown: months are counted as completed calendar units, so a span from January 31 to March 1 contains one completed month, February, and one day. This matches how tenancy and employment spans are normally counted, but it can surprise anyone expecting thirty-day months. The days total is always available as the unambiguous alternative.",
],
"mistakes": [
"Using the days figure where the convention requires inclusive counting of both endpoints, or vice versa.",
"Expecting the years-months-days breakdown to equal a fixed multiple of the weeks figure.",
"Ignoring leap years in hand calculations spanning February.",
"Comparing spans across different timezones as if date-only values carried timezone information.",
],
"extra_faqs": [
("How do I count business days between dates?", "This tool counts calendar days. For business days, subtract weekends and holidays from the total, or use a dedicated business-day calculator that applies a holiday calendar."),
("Why does the same span show different month counts in different tools?", "Month counting conventions differ: completed calendar months versus nominal thirty-day months. This tool uses completed calendar months, the convention most contracts and HR systems use."),
],
},
"image-resizer": {
"deep": [
"Choosing dimensions is a design decision that starts with the destination. Profile avatars, thumbnails and inline blog images each have conventional sizes, and matching them avoids both blurry upscaling and wasted bytes on downscaling done by the receiving platform. A useful habit is to decide the largest size at which the image will ever display, export at that size, and let responsive layouts shrink it as needed.",
"The quality-versus-size trade has a shape worth knowing: the first steps down from maximum quality buy large size reductions for imperceptible changes, while the last steps buy tiny reductions for visible damage. This is why the practical advice is to start around 80 percent quality and adjust from evidence, inspecting the preview rather than assuming. WebP's better compression shifts the whole curve, which is why it has become the default choice for web images where supported.",
],
"mistakes": [
"Uploading full-resolution originals because resizing felt optional, wasting bandwidth on every view.",
"Setting both width and height independently and distorting the aspect ratio.",
"Using maximum quality on lossy formats and wondering why files barely shrank.",
"Converting sharp graphics to JPEG and being surprised by ringing artefacts around edges.",
],
"extra_faqs": [
("Does the tool keep EXIF data like location?", "Re-encoding through the canvas strips metadata, including location tags, which is a privacy benefit when sharing photos. Keep your original file if you need the metadata."),
("What resolution should I target for the web?", "Match the largest display size on the devices your audience uses, commonly 1,200 to 1,600 pixels wide for content images, and let the format and quality settings handle file size."),
],
},
}
