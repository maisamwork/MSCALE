# Expanders batch 2: text tools
X = {
"word-counter": {
"deep": [
"Different institutions count differently at the margins, and knowing which convention applies saves disputes. Some count hyphenated compounds as one word, others as two. Some count numbers and standalone symbols, others skip them. The whitespace rule used here matches mainstream word processors, which is the convention most briefs implicitly mean. When a limit genuinely matters, the safest practice is to use the same counting method the recipient will use, and this tool's convention is the common default.",
"Reading time deserves a little more nuance because it changes with the text's density. Simple narrative prose reads faster than the word count suggests; dense technical material with numbers and unfamiliar terms reads slower. The estimate shown assumes average prose, so treat it as a midpoint: marketing copy may read a touch quicker, documentation a touch slower.",
],
"mistakes": [
"Meeting a word limit by padding with restatements, which editors and graders spot immediately.",
"Checking only the word count when the real limit was characters, a mismatch that fails silently.",
"Forgetting that a title page or headings may or may not count, depending on the brief.",
"Trusting an estimate from a different tool that divides by a nominal word count rather than counting.",
],
"extra_faqs": [
("Do headings count toward the word total?", "Usually yes, since they are read as part of the text, but some academic briefs exclude them. Match the convention your recipient specifies; when unspecified, count everything."),
("How do I check a section's length in a long document?", "Paste just that section. Counting section by section reveals structure problems, like one section consuming half the budget, that a single total hides."),
],
},
"case-converter": {
"deep": [
"The boundary between presentation and data is the reason case tools exist at all. Databases, file systems and code treat case as significant: User and user are different identifiers, and IMG_001.jpg is a different file from img_001.jpg on case-sensitive systems. Human-facing text treats case as style. Converting case is therefore usually a data-normalisation task, and the programming modes exist precisely because that is the common serious use.",
"A note on identifiers: converting prose to snake_case or camelCase produces a valid identifier shape, but real code also has reserved words and naming conventions to respect. The converter gets you most of the way there; the remainder, avoiding a reserved word or matching a team's prefix conventions, is judgement. Treating the output as a strong draft rather than a finished identifier is the correct mental model.",
],
"mistakes": [
"Converting file names or identifiers that are case-sensitive downstream, breaking references silently.",
"Applying Title Case to text containing acronyms, which mangles HTML into Html.",
"Forgetting that some editorial styles leave short words lowercase in titles.",
"Converting user-entered emails to uppercase; email domains are case-insensitive but conventions expect lowercase.",
],
"extra_faqs": [
("Can it convert to alternating or random case?", "The tool covers the standard practical styles. Alternating case is a stylistic joke with no data use, and random case would defeat the purpose of normalisation."),
("What is kebab-case best for?", "URLs and file names. It is lowercase with hyphens, readable by humans and safe in web addresses, which is why slugs and static-site file names use it almost universally."),
],
},
"remove-duplicate-lines": {
"deep": [
"Order preservation is a deliberate design choice worth understanding. Some dedup tools sort as they clean, which destroys ranked lists. This tool keeps first-occurrence order, so a priority-ordered keyword list stays priority-ordered after deduplication. When you do want sorting, it is a separate step with the Line Sorter, and keeping the two operations distinct means you always know which transformation happened.",
"For data work, the trim and case options model the two ways real-world duplicates hide. Export systems pad fields to fixed widths, producing visually identical lines that differ in trailing spaces; humans capitalise inconsistently. Comparing normalised forms catches both, while outputting the trimmed original keeps the data clean for whatever consumes the list next.",
],
"mistakes": [
"Deduplicating case-sensitively when the list contains human-typed entries with inconsistent capitalisation.",
"Losing a ranked order by sorting when the task only required deduplication.",
"Forgetting that one empty line survives deduplication, which is usually desired but can surprise.",
"Assuming duplicates are exact when invisible whitespace differences are present.",
],
"extra_faqs": [
("Can I deduplicate items separated by commas instead of lines?", "Not directly; the tool works line by line. Convert commas to line breaks first, for example with Find and Replace, deduplicate, then convert back."),
("Does deduplication affect special characters?", "No. Lines are compared as text; special characters, emoji and accented letters are handled correctly and preserved in the output."),
],
},
"reverse-text": {
"deep": [
"The three modes exist because reversal means different things in different contexts, and choosing correctly is the whole skill. For text-level puzzles and aesthetics, character mode is right. For list manipulation, line mode is right, and it is worth noting that line reversal plus a sort gives you control over ordering in ways sorting alone does not: reversing a date-ordered list flips its direction without otherwise disturbing it.",
"A Unicode caveat belongs in an honest explanation. Emoji and some complex scripts are stored as sequences of code units, and strict character reversal can split those sequences, producing visually odd output. For Latin text and everyday punctuation the tool is exact; for decorative emoji strings, check the result visually before using it in anything important.",
],
"mistakes": [
"Using character mode on a list when line mode was intended, scrambling every line's contents.",
"Reversing text that contains emoji and assuming the result is display-safe without checking.",
"Forgetting that punctuation travels with its word in word mode, moving sentence periods to the front.",
"Assuming reversal preserves multi-space layout; word mode normalises spacing.",
],
"extra_faqs": [
("Why would a developer reverse lines?", "Log files and feeds commonly arrive newest-first, while analysis wants oldest-first. Line reversal converts direction instantly without touching content, which is faster than re-exporting."),
("Is reversal useful for testing?", "Yes. Reversed strings are a standard edge case for testing how layouts and parsers handle unexpected input, and this tool produces them instantly."),
],
},
"find-and-replace": {
"deep": [
"Regular expressions reward a small investment disproportionately, and three constructs cover most real needs. Character classes like [0-9] or [aeiou] match any of a set of characters. Quantifiers like plus and star repeat the previous element, with the question mark making them lazy so they stop at the first opportunity. Capture groups, written in parentheses, both isolate part of the match for reuse in the replacement and structure the pattern itself.",
"Anchors are the fourth construct worth learning: the caret matches the start of a line and the dollar sign the end, which is what turns a global replace into a disciplined one. Replacing only whole lines, or only prefixes, or only suffixes, are all anchor operations. Combined with the match count, anchors make bulk edits predictable enough to run on important documents.",
],
"mistakes": [
"Forgetting to escape regex special characters like dots and brackets when matching literal text.",
"Running a broad pattern on a large document without checking the match count first.",
"Using case-insensitive mode on code, where identifier case is significant.",
"Replacing inside URLs or identifiers because whole-word mode was off.",
],
"extra_faqs": [
("How do I match across multiple lines?", "Enable multiline mode so anchors work per line, and use patterns that include newline handling. The tool's highlighting shows exactly what each match spans."),
("Can I preview replacements before applying them?", "The output area is the preview: it shows the full result live before you copy anything, and the match count tells you how many replacements occurred."),
],
},
"text-sorter": {
"deep": [
"Stability is the property that separates a careful sort from a careless one. A stable sort keeps lines that compare equal in their original relative order, which matters when the list was already partially organised, for example grouped by category and then sorted alphabetically within the whole. The tool's comparisons are designed to behave predictably so that re-sorting a sorted list is a no-op rather than a shuffle.",
"Numeric sorting has a subtlety worth knowing: it reads leading numbers, so lines like 10 apples and 2 apples sort by 10 and 2, but lines where the number appears later sort as text. For data where the number is embedded mid-line, extract it to the front first, or accept text ordering for those lines. Knowing where the number must sit prevents most surprises.",
],
"mistakes": [
"Sorting numerically without numeric mode, producing the classic 1, 10, 100, 2 order.",
"Sorting before deduplicating, which leaves duplicates scattered in clean order.",
"Forgetting that blank lines sort to the top and cleaning them first.",
"Shuffling a list that needed deterministic order, then being unable to reproduce it.",
],
"extra_faqs": [
("Can I sort by a column in CSV-like data?", "Not directly; the tool compares whole lines. Sort by the column's values by extracting them first, or reformat so the sort key leads each line."),
("Is the shuffle reproducible?", "No, and that is the point: each shuffle is independent and uniformly random. If you need reproducibility, copy the shuffled result immediately."),
],
},
"lorem-ipsum-generator": {
"deep": [
"The choice of filler text is a small design decision with real consequences. Lorem ipsum's non-lexical Latin means stakeholders read the layout rather than the words, which is exactly what a design review wants. Alternatives exist for specific cases: realistic copy drawn from the target domain tests how actual vocabulary fits; translated filler tests non-Latin scripts; deliberately repetitive text tests overflow states. The classic remains the default because it fails gracefully in every direction.",
"Quantity discipline matters more than people expect. Filling a layout with three times the expected copy hides overflow problems; filling it with half the expected copy hides emptiness problems. The correct amount is the amount the final content will occupy, which is why the generator offers fine control over paragraphs, sentences and exact word counts rather than one fixed block.",
],
"mistakes": [
"Using one repeated block everywhere, which looks obviously unfinished in reviews.",
"Generating far more filler than the real content will occupy, hiding layout problems.",
"Shipping placeholder text to production because it was never replaced.",
"Using lorem ipsum in user-facing tests where realistic domain copy would reveal different issues.",
],
"extra_faqs": [
("Can I generate filler in other languages?", "This generator produces the classic Latin-derived filler. For other scripts, generate equivalent-length text in the target language, or use the tool for length planning and translate the structure."),
("Is lorem ipsum copyrighted?", "No. The passage derives from classical Latin text over two thousand years old, and the scrambled filler has been in the public domain for centuries."),
],
},
"word-frequency-counter": {
"deep": [
"Beyond spotting overuse, frequency analysis has a comparative mode that is genuinely useful: run the same analysis on two texts and compare the profiles. A draft against its target keyword list shows alignment at a glance. Two chapters by the same author show stylistic consistency. A summary against its source shows whether the summary borrowed the source's emphasis or invented its own. The tool supports all of these because it does one thing, counting, reliably.",
"Normalisation choices shape the results, and knowing them prevents misreading. Lowercasing merges proper nouns with common nouns, so a text about the company Apple counts apple generously. Singulars and plurals stay separate. These are conventional choices, not errors, but reading the output with them in mind is the difference between analysis and confusion.",
],
"mistakes": [
"Reading the raw list without the stop-word filter and concluding a text is about the word the.",
"Expecting singular and plural forms to merge; they count separately by design.",
"Analysing very short texts, where frequency rankings are noise rather than signal.",
"Forgetting that names and proper nouns count like any other word.",
],
"extra_faqs": [
("Can I export the frequency list?", "Select and copy the list directly; the counts are plain text and paste cleanly into spreadsheets for further analysis or charting."),
("What is a healthy keyword frequency for SEO copy?", "There is no magic number and keyword stuffing is penalised. The useful check is balance: the target term should appear naturally, and the frequency profile should look like ordinary language, not repetition."),
],
},
}
