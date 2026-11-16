# Batch 7: html-encoder-decoder, unit-converter, timestamp-converter, number-base-converter, roman-numeral-converter
CONTENT = {
"html-encoder-decoder": {
"intro": [
"HTML reserves a handful of characters for its own syntax: angle brackets build tags, ampersands start entities, quotes wrap attributes. When your text legitimately needs those characters, it must be escaped, or the browser will interpret them as markup. This HTML Encoder and Decoder converts text to safe HTML entities and back, instantly.",
"Encoding turns a less-than sign into its entity form, an ampersand into its escaped form, and quotes into attribute-safe equivalents, so code samples, user content and mathematical text display exactly as written instead of being eaten by the browser. Decoding reverses the process, restoring entities to plain characters.",
"Developers use it when displaying code examples inside pages, when inserting user-generated content safely, and when preparing snippets for documentation. Writers use it for mathematical comparisons and arrows that browsers would otherwise misread. Everything runs locally in your browser.",
],
"how": [
"Paste your text, choose encode or decode, and the result appears instantly. Encoding is the direction you need before placing text inside HTML; decoding is what you need when text arrives full of entities that should be readable characters.",
],
"steps": [
"Paste or type the text you want to convert.",
"Choose encode to escape HTML special characters, or decode to restore them.",
"Review the converted output, which updates as you type.",
"Copy the result into your page, template or document.",
"Round-trip check: decode your encoded text to confirm it returns to the original.",
],
"works": [
"Encoding replaces the five characters that carry markup meaning with their entity equivalents: the less-than and greater-than signs become lt and gt entities, the ampersand becomes amp, and double and single quotes become quot and the numeric apostrophe entity. The ampersand replacement happens with care so that already-encoded text is not double-escaped.",
"Decoding maps entities back to characters, including the numeric forms like sixty-five followed by a hash code, which appear in text processed by other systems. This restores readability when copying text out of HTML sources, templates or encoded feeds.",
"The reason this matters beyond tidiness is correctness and safety. Unescaped user content can break a page layout or, worse, constitute an injection risk when rendered by a template that trusts it. Escaping user text before display is the standard defence, and this tool shows exactly what that escaped form looks like.",
],
"examples": [
("Showing code on a page", "A tutorial needs to display the literal text of an HTML tag inside a paragraph. Encoding the snippet converts the angle brackets to entities, so the browser prints the tag instead of rendering it."),
("Preparing user comments for display", "A discussion system escapes every comment before rendering. A comment containing angle brackets displays as typed rather than disappearing into a broken tag or altering the page."),
("Cleaning up encoded text", "Text scraped from a web source arrives as plain text littered with entities like amp and nbsp. Decoding restores it to natural readable characters in one pass."),
],
"tips": [
"Encode user-supplied content before displaying it in HTML; it is both correct and safer.",
"Decode text copied from HTML sources to restore entities to real characters.",
"Ampersands in URLs inside HTML should be encoded too, per the HTML specification.",
"Encoding twice produces double-escaped text; decode once to undo it.",
"Entities are case-sensitive in a few cases, so copy decoded text rather than retyping it.",
],
"faqs": [
("Which characters get encoded?", "The five markup-critical characters: less-than, greater-than, ampersand, and the double and single quote characters. Everything else passes through unchanged."),
("What is the difference between named and numeric entities?", "Named entities like amp use short names; numeric entities use the character's code point. Both are valid, and the decoder handles both forms."),
("Why does encoded text look ugly?", "Entities are designed for machines, not readers. They exist so browsers display the right character; the escaped form is never meant to be read by humans."),
("Is escaping the same as protection against all attacks?", "Escaping is the core defence for text contexts, but attributes, URLs and JavaScript contexts need context-appropriate handling. Escape for the context where data will land."),
("Does it handle accented characters?", "They pass through unchanged when encoding, since they are not markup-critical. Numeric entities for them decode correctly on the way back."),
("Is my text uploaded?", "No. Conversion happens entirely in your browser."),
],
},
"unit-converter": {
"intro": [
"Units trip everyone up eventually: a recipe in ounces, a blueprint in inches, a spec sheet in megabytes, a weather report in Fahrenheit. This Unit Converter handles the everyday conversions across length, weight, temperature and data size in one place, with instant, accurate results.",
"Pick a category, choose the units you are converting from and to, type a value, and the answer appears immediately. The conversions use exact standard definitions, such as 1 inch equals 2.54 centimetres exactly, so results match reference values rather than approximations.",
"Students use it for homework and science classes, cooks for recipes from other countries, travellers for weather and distances, developers for storage sizes and bandwidth maths, and professionals of every kind for the unit that is not the one in front of them. It runs entirely in your browser with no setup.",
],
"how": [
"Choose a category first, then the from and to units, then type the value. The result updates as you type, and switching categories keeps the interface identical so moving from lengths to weights is seamless.",
],
"steps": [
"Select a category: length, weight, temperature or data size.",
"Choose the unit you are converting from.",
"Choose the unit you are converting to.",
"Type the value; the result updates live.",
"Swap the units to run the conversion in reverse.",
],
"works": [
"For length, weight and data size, conversions are done through exact base ratios. Length converts through metres using exact definitions like 1 inch equals 2.54 centimetres and 1 mile equals 1,609.344 metres. Weight converts through kilograms, and data size uses binary definitions where 1 kilobyte here means 1,024 bytes, the convention familiar from operating systems.",
"Temperature is different because its units have offsets as well as scales, so simple ratios do not work. The tool converts through a common reference: Celsius to Fahrenheit multiplies by nine fifths and adds 32; Fahrenheit to Celsius subtracts 32 and multiplies by five ninths; Kelvin is Celsius plus 273.15. These offsets are why temperature conversions cannot be memorised as simple multiplication.",
"Precision is preserved end to end: the tool computes with full floating-point accuracy and displays sensible precision rather than long artefact tails. For everyday use the displayed precision is far beyond what a ruler or a kitchen scale can measure, which is the right place to stop.",
],
"examples": [
("Recipe conversion", "A British recipe calls for 250 grams of flour and your scale reads ounces. Converting gives about 8.8 ounces. A US oven setting of 375 Fahrenheit converts to about 190 Celsius for the same bake."),
("Travel distances", "A road sign says the next fuel is 85 kilometres away and your car reports miles per tank. Converting 85 kilometres gives about 53 miles, enough to judge whether the tank will make it."),
("Bandwidth and storage maths", "A 2 gigabyte download over a 50 megabit-per-second connection: converting gigabytes to megabits gives about 16,384 megabits, so roughly five and a half minutes at full speed in theory."),
],
"tips": [
"Check the category before the units; most wrong answers come from the wrong category, not the wrong maths.",
"Data size here uses the binary convention, 1,024-based, which matches what operating systems report.",
"Temperature needs offsets, so never convert it with a simple ratio.",
"Swap the units to invert a conversion instead of recomputing by hand.",
"For critical engineering work, confirm the exact standard definitions; everyday units here use exact legal values.",
],
"faqs": [
("Are the conversion factors exact?", "Yes for the defined units: inches to centimetres, miles to metres and similar are exact legal definitions. Temperature formulas are the standard exact equations."),
("Does 1 kilobyte mean 1,000 or 1,024 bytes?", "Here it means 1,024, the binary convention used by operating systems for storage reporting. Marketing materials sometimes use the 1,000-based decimal convention instead."),
("Why can't I convert temperature by ratio?", "Because temperature scales have different zero points. Forty degrees Celsius is not twice as hot as twenty; the offsets in the formulas account for this correctly."),
("Can I convert compound units like speed?", "This tool covers the core categories of length, weight, temperature and data size. Speed can be derived by converting distance and time separately."),
("How precise are the results?", "The tool computes at full floating-point precision and displays clearly rounded values. The precision shown exceeds any everyday measuring device."),
("Is anything uploaded?", "No. All conversion happens locally in your browser."),
],
},
"timestamp-converter": {
"intro": [
"A Unix timestamp is a count of seconds since January 1, 1970, and it is how almost every computer system records time. It is unambiguous and timezone-proof, which is exactly why it is unreadable: nobody glances at 1735689600 and thinks New Year's Day 2025. This Timestamp Converter translates in both directions, instantly.",
"Paste a timestamp to convert it to readable dates in UTC and your local timezone, or pick a date and time to get its timestamp. A live clock shows the current timestamp ticking, which is invaluable when debugging time-based logic or setting up scheduled tasks.",
"Developers use it daily for debugging logs, APIs and cron jobs; analysts use it to make exports readable; anyone configuring systems that speak in timestamps uses it to avoid off-by-a-timezone mistakes. The conversions run entirely in your browser.",
],
"how": [
"Paste a timestamp to decode it, or use the date picker to encode a moment. The live clock at the top shows the current second in case you need a timestamp for right now. Results show both UTC and local interpretations so timezone confusion is impossible.",
],
"steps": [
"Paste a Unix timestamp to convert it to human-readable dates.",
"Read the UTC interpretation to see the absolute moment.",
"Read the local interpretation to see the moment in your timezone.",
"Or pick a date and time to convert in the other direction.",
"Use the live clock to grab the current timestamp when needed.",
],
"works": [
"The Unix epoch is midnight UTC on January 1, 1970, and a timestamp counts seconds from that moment, ignoring timezones entirely. Converting to a date therefore has one absolute answer in UTC, and one answer per timezone for local display. Showing both is what prevents the classic bug of comparing a UTC time against a local one.",
"Modern systems increasingly use millisecond timestamps, a 13-digit count. The tool detects the magnitude of what you paste: 10 digits are treated as seconds and 13 digits as milliseconds, which removes the most common conversion mistake. Dates before 1970 are negative counts and convert correctly too.",
"In the other direction, a chosen date and time is interpreted in your local timezone, because that is how humans mean time, and its absolute timestamp is derived from that. This is the correct behaviour for scheduling: when you say a meeting is at 9 o'clock, you mean 9 o'clock where you are, and the timestamp captures that absolute instant.",
],
"examples": [
("Debugging a log line", "A server log shows an error at 1735689600. Converting reveals it happened at exactly midnight UTC on New Year's Day 2025, which suggests a scheduled job rather than user activity, and the investigation changes direction."),
("Preparing a cron schedule", "A task must run at 6 in the morning UTC. Converting candidate times shows their timestamps, which are then used to verify the schedule fires at the intended absolute moment."),
("Reading an API response", "An API returns createdAt as 13 digits. Pasting it converts to a readable local date, confirming the record was created last Tuesday at 14:32 local time, not the UTC reading that first assumption suggested."),
],
"tips": [
"Ten-digit timestamps are seconds; thirteen-digit ones are milliseconds. The tool detects this automatically.",
"Always check whether a spec means UTC or local time; the timestamp is absolute, the display is not.",
"Use the live clock to capture now when writing time-based tests or examples.",
"Negative timestamps are valid and represent times before 1970.",
"When comparing times from two systems, convert both to UTC first; comparing local strings invites errors.",
],
"faqs": [
("What exactly is a Unix timestamp?", "The number of seconds elapsed since 00:00:00 UTC on January 1, 1970, not counting leap seconds. It is the standard way computers store absolute time."),
("Does it handle millisecond timestamps?", "Yes. Thirteen-digit inputs are interpreted as milliseconds automatically, and the conversion accounts for the difference."),
("Why do UTC and local show different times?", "They are the same instant described in two frames. UTC is the absolute reference; local applies your timezone's offset. Both are shown to prevent mix-ups."),
("Can it convert dates before 1970?", "Yes. Timestamps before the epoch are negative numbers and convert correctly to historical dates."),
("Why does my converted time differ from another tool by hours?", "One tool is showing UTC and the other local time, or one assumed a different timezone for the input. Both displays here are labelled to make that distinction explicit."),
("Is anything uploaded?", "No. All conversion happens locally in your browser."),
],
},
"number-base-converter": {
"intro": [
"Computers count in binary, programmers read hexadecimal, and occasionally octal appears, while humans think in decimal. Converting between these bases by hand is a classic source of errors, especially with longer values. This Number Base Converter converts any value between binary, octal, decimal and hexadecimal instantly.",
"Type a value in any base and see it in all the others at once. The tool validates input strictly: binary accepts only 0 and 1, hexadecimal accepts digits and A through F, and invalid characters are flagged immediately rather than silently producing nonsense.",
"Students use it to check homework and build intuition for place value; developers use it for bit masks, memory addresses, colour codes and protocol fields; electronics hobbyists use it for register values. The simultaneous display of all four bases is what turns rote conversion into actual understanding.",
],
"how": [
"Type a number in any of the four bases; the other three update instantly. The input box declares which base you are typing in, and validation catches impossible digits for that base immediately.",
],
"steps": [
"Select the base you are typing in: binary, octal, decimal or hexadecimal.",
"Type the value, using only valid digits for that base.",
"Read the equivalent values in all other bases simultaneously.",
"Toggle uppercase or lowercase hex output to match your context.",
"Copy any of the four representations.",
],
"works": [
"Positional notation is the underlying idea: in any base, each digit position carries a weight that is a power of the base. Binary's places are ones, twos, fours, eights; hexadecimal's are ones, sixteens, two-hundred-fifty-sixes. Conversion to decimal evaluates those weights; conversion from decimal repeatedly divides by the target base and collects remainders.",
"Hexadecimal exists because it maps perfectly onto binary: each hex digit represents exactly four bits, so a byte is always two hex digits. This is why memory addresses, colour codes like the web's FF7700, and file signatures are written in hex. Octal groups three bits per digit and survives mainly in Unix file permissions.",
"The tool's strict validation matters because base confusion is silent: BEEF is valid hex, nonsense in decimal, and the difference matters. By declaring the input base and rejecting invalid digits, the tool prevents the classic mistake of pasting a hex value into a decimal field and reading a confidently wrong answer.",
],
"examples": [
("Reading a colour code", "The web colour FF7700 converts to decimal 16,734,464 and to binary 111111110111000000000000. Seeing the red channel FF, green 77, blue 00 split explains the colour's composition instantly."),
("Understanding subnet masks", "A network mask of 255.255.255.0 converts per octet to binary, showing the twenty-four leading ones that define a slash-24 network. The conversion makes the mask's meaning visible."),
("Checking homework", "A student converts 101101 from binary, getting 45 in decimal, then verifies by converting 45 back to binary and recovering the original. The round trip builds genuine confidence."),
],
"tips": [
"Declare the input base first; the same digits mean different values in different bases.",
"Each hex digit is exactly four bits; use this to sanity-check binary-to-hex conversions.",
"Hex A through F equal decimal 10 through 15; memorising this speeds up reading hex.",
"Octal survives in Unix permissions: 755 means rwxr-xr-x.",
"Round-trip any critical conversion: convert there and back and confirm you recover the input.",
],
"faqs": [
("What is the largest number it can convert?", "Very large values convert fine, limited by JavaScript's integer precision. Beyond about fifteen or sixteen decimal digits, precision degrades, as it does in most software."),
("Why is hexadecimal so common in computing?", "Because each hex digit maps to exactly four binary bits, making it a compact, human-readable shorthand for binary data like addresses, colours and byte values."),
("Can it convert fractional values?", "This tool handles integers, which covers the overwhelming majority of base-conversion needs. Fractional conversion requires positional arithmetic after the point."),
("Are negative numbers supported?", "Enter the magnitude and apply the sign convention your context uses. Computers represent negatives via two's complement, which is a separate topic from base conversion."),
("Why does my binary input get rejected?", "Binary accepts only 0 and 1. A stray space, an O instead of a zero, or a decimal point will fail validation, which is the tool protecting you from a wrong answer."),
("Is anything uploaded?", "No. All conversion happens locally in your browser."),
],
},
"roman-numeral-converter": {
"intro": [
"Roman numerals still surround us: film credits, monarchs and popes, Super Bowls, cornerstones, book chapters and watch faces. Reading XLII quickly, or writing 1988 properly, is a small skill most people never quite mastered. This Roman Numeral Converter translates both directions instantly, and validates as it goes.",
"Type a number to get its Roman numeral, or type a numeral to get its number. The converter follows the classical rules, including the subtractive principle where IV means one before five and CM means one before thousand, and it rejects malformed numerals instead of guessing.",
"Students use it for history and Latin classes, writers and editors for checking chapter and credit numbering, designers for clock and engraving work, and puzzle enthusiasts for decoding references. The two-way, instantly validated design makes it equally good for reading and for writing numerals correctly.",
],
"how": [
"Choose the direction, type either a number or a numeral, and the translation appears immediately. Invalid inputs, whether a numeral that breaks the rules or a number outside the classical range, produce a clear message rather than a wrong answer.",
],
"steps": [
"Choose whether you are converting a number to a numeral or the reverse.",
"Type the value: a number from 1 to 3,999, or a Roman numeral.",
"Read the translation, which appears instantly.",
"Correct any validation message by adjusting the input.",
"Copy the result when it is right.",
],
"works": [
"Roman numerals use seven letters: I, V, X, L, C, D and M, worth 1, 5, 10, 50, 100, 500 and 1,000. The additive rule says symbols in descending order add up, so XVI is 16. The subtractive rule says a smaller symbol before a larger one is subtracted, giving the compact forms IV, IX, XL, XC, CD and CM.",
"Converting a number to a numeral is greedy: take the largest value that fits, write its symbol or subtractive pair, subtract, and repeat. Converting a numeral to a number walks the symbols left to right, adding each value but subtracting it instead when it is smaller than the symbol that follows.",
"Validation enforces the classical canon: proper subtractive pairs only, no more than three repetitions of a symbol, and descending order otherwise. The strict range up to 3,999 reflects genuine classical practice, since the Romans had no consistent written form for larger numbers without special notation like the vinculum.",
],
"examples": [
("Reading a film credit", "A film is copyrighted MCMXCIV. Walking the symbols gives 1000, then 900 from CM, then 90 from XC, then 4 from IV: 1994. The converter confirms the reading instantly."),
("Numbering chapters and events", "An editor numbering a book's parts needs Part VII through Part XII and wants them right first time. Converting the numbers verifies each numeral before it goes to print."),
("Checking a watch face", "A watch face shows a curious IIII instead of IV, a real watchmaking tradition. Converting both forms shows they equal 4, and the difference between tradition and classical rules becomes a conversation rather than a confusion."),
],
"tips": [
"Only I, X and C are used subtractively, and only before the next two larger values.",
"Classical numerals stop at 3,999; beyond that, special notations apply.",
"Three repetitions is the maximum: III is fine, IIII is not, with the watch-face exception being a stylistic tradition.",
"When reading, subtract a symbol only when it is smaller than the one immediately after it.",
"Convert both directions as a check: number to numeral and back should return the original.",
],
"faqs": [
("Why is there no zero or negative number?", "Roman numerals were for counting and labelling, not arithmetic, and classical notation has no zero. The converter therefore accepts 1 through 3,999."),
("Why does a watch show IIII instead of IV?", "It is a long-standing watchmaking tradition with several proposed origins, including visual balance on the dial. Classical rules prefer IV, which is what this converter produces."),
("What is the largest number representable?", "In standard notation, 3,999, written MMMCMXCIX. Larger values historically used a bar over the numeral to multiply by a thousand, which is outside everyday use."),
("Can I type lowercase numerals?", "Yes. Input is case-insensitive, so xiv converts the same as XIV."),
("Why is my numeral rejected?", "It breaks a classical rule, such as an invalid subtractive pair like IC, four repetitions, or symbols out of order. The message indicates the problem so you can correct it."),
("Is anything uploaded?", "No. Conversion happens entirely in your browser."),
],
},
}
