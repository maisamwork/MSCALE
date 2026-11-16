# Final adjustments: bring every page into the 1000-1200 range
X = {
"case-converter": {
"extra_faqs": [
("Why does my team's style guide specify one case over another?", "Conventions exist for scanability and consistency: snake_case reads easily in prose-heavy code, camelCase is traditional in JavaScript, and PascalCase marks classes. Following the local convention matters more than the choice itself."),
],
},
"coin-flipper": {
"deep": [
"Fairness in a digital flip also removes the physical tells that experienced observers use to predict real coins. A caught coin can be peeked at, a spun coin lands biased by its design, and a tossed coin can be called mid-air by someone tracking rotation. None of these channels exist here: the result is decided at the moment of the click and displayed simultaneously to everyone, which is as close to incorruptible as a decision procedure gets.",
],
"extra_faqs": [
("Can I use this for official random selection?", "For informal draws and decisions, yes. For formal processes with legal or audit requirements, use a certified drawing procedure or a documented, auditable method."),
("What if I need best-of-three with a record?", "Flip three single coins in sequence and note each result, or flip three coins at once and take the majority. Either approach maps cleanly onto a best-of series."),
],
},
"csv-to-json-converter": {
"extra_faqs": [
("Does the order of rows and columns survive the conversion?", "Yes. Rows appear in the JSON array in their original order, and object keys follow the header row's column order, so the output mirrors the input's structure exactly."),
],
},
"date-difference-calculator": {
"deep": [
"A practical tip for recurring calculations: keep the two dates in the same format your source documents use, and re-read them before entering. Transposed day and month values are the most common input error, especially with dates like the third of May, which some regions write 03/05 and others 05/03. The tool accepts dates unambiguously through its picker, which is precisely why pickers beat typed dates for this kind of work.",
],
"extra_faqs": [
("Can I add or subtract from a date here?", "This tool measures between two dates. To shift a date by a duration, use the Age Calculator with a future reference date, or compute the target date in a calendar and measure from there."),
],
},
"dice-roller": {
"extra_faqs": [
("Can I roll for a random order of players?", "Roll one die per player with a distinct range per roll, or use the Random Number Generator's unique mode for a straight draw. Both approaches produce a fair, dispute-free order."),
("Why does the tool cap at twenty dice?", "Twenty covers essentially every game system and keeps the individual results readable on one screen. Larger pools are a statistics exercise better served by the Random Number Generator."),
],
},
"html-encoder-decoder": {
"extra_faqs": [
("Does encoding affect SEO or accessibility?", "No. Encoded entities render as the intended characters, so search engines and screen readers see the same text as readers do. Encoding is purely about correct display of markup-critical characters."),
],
},
"lorem-ipsum-generator": {
"extra_faqs": [
("How much filler should a wireframe use?", "Enough to match the expected final copy: roughly the number of paragraphs the finished page will carry. Matching density is what makes wireframe reviews predictive of the real design."),
],
},
"number-base-converter": {
"extra_faqs": [
("Why does hexadecimal use letters?", "Sixteen values need sixteen symbols, and the digits 0 through 9 provide only ten. The letters A through F stand for the values 10 through 15, completing the set in a convention older than modern computing."),
],
},
"palette-generator": {
"extra_faqs": [
("Can I use the palette for print work?", "The values are screen-space RGB-derived. For print, convert your chosen steps with a print-production tool that applies the correct colour profile, since screens and printers use different colour models."),
],
},
"random-number-generator": {
"extra_faqs": [
("Can I generate numbers for a lottery-style draw with multiple prizes?", "Yes: set the range to the ticket numbers, enable unique mode, and generate as many values as there are prizes. Each winner is guaranteed distinct, and every ticket had an equal chance."),
("What if I need a random order rather than random numbers?", "Generate unique numbers across the range and read them as a ranking, or use the Line Sorter's shuffle mode on a pasted list. Both produce uniformly random orderings."),
],
},
"remove-duplicate-lines": {
"extra_faqs": [
("How do I keep the last occurrence instead of the first?", "Reverse the list with the Reverse Text tool's line mode, deduplicate, then reverse back. The first occurrence in the reversed order is the last occurrence in the original."),
],
},
"reverse-text": {
"extra_faqs": [
("Can I reverse only part of my text?", "Process the whole input, then copy back the portion you need, or split the text first. The tool operates on everything pasted, so selective reversal is a copy-paste step."),
],
},
"roman-numeral-converter": {
"extra_faqs": [
("How do I read a long numeral quickly?", "Scan for the six subtractive pairs first and treat each as a single unit, then add the remaining symbols left to right. Two passes make even long numerals like MMDCCCXLVIII manageable."),
],
},
"text-sorter": {
"extra_faqs": [
("Does sorting handle accented characters correctly?", "Yes. Comparison uses the browser's text collation rules, so accented letters sort with their base letters rather than being pushed to the end of the alphabet."),
("Can I sort and deduplicate in one step?", "Use the Remove Duplicate Lines tool first, then sort here. Keeping the operations separate makes each result verifiable and the order of transformations explicit."),
],
},
"url-encoder-decoder": {
"extra_faqs": [
("Do I need to encode the hash fragment of a URL?", "Only if the fragment's content contains reserved characters. The fragment never reaches the server, but the browser still parses it, so encoding its values keeps the URL unambiguous."),
],
},
"uuid-generator": {
"extra_faqs": [
("Can I format UUIDs without hyphens?", "The canonical form includes hyphens, which is what most systems expect on input. If a system wants the compact form, strip the hyphens after copying; the value is identical."),
],
},
"word-frequency-counter": {
"extra_faqs": [
("Does the tool handle hyphenated words?", "Yes. A hyphenated compound counts as one word, matching standard word-processor conventions, so well-known is tallied as a single term."),
],
},
}
