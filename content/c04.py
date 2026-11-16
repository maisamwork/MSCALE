# Batch 4: find-and-replace, text-sorter, lorem-ipsum-generator, word-frequency-counter
CONTENT = {
"find-and-replace": {
"intro": [
"Find and replace is one of the oldest tools in computing because it solves one of the most common problems: the same wrong text repeated many times. A product name changed across a document, a date corrected in fifty places, inconsistent spacing cleaned up, or a variable renamed through a file. This Find and Replace tool does all of it in the browser, with optional regular expressions for pattern-based edits.",
"Type or paste your text, enter what to find and what to replace it with, and see the result instantly. Basic mode replaces exact text. Advanced mode interprets the search box as a regular expression, letting you match patterns rather than fixed strings, such as every number in a document or any whitespace run.",
"Options cover the details that matter: case-sensitive matching for code and identifiers, whole-word matching to avoid replacing inside longer words, and a match counter so you know how many replacements happened. Everything runs locally, so confidential documents are safe to process.",
],
"how": [
"The workflow is paste, specify, review, copy. Enter your text, fill in the find and replace boxes, and toggle the options to match your intent. The output updates live, and the tool reports how many matches were found and replaced.",
],
"steps": [
"Paste or type your text into the input area.",
"Enter the text or pattern to find.",
"Enter the replacement text, leaving the box empty to delete matches.",
"Toggle case sensitivity, whole words, or regex mode as needed.",
"Review the output and the match count, then copy the result.",
],
"works": [
"In basic mode the tool performs literal text matching. Every exact occurrence of the find string is swapped for the replacement, respecting the case-sensitivity and whole-word options. The whole-word option adds word boundaries around the search term, so replacing cat will not touch category or concatenate.",
"In regex mode the find box is compiled as a regular expression, the standard pattern language used across programming tools. Patterns like [0-9]+ match any run of digits, \s+ matches any whitespace run, and capture groups in parentheses can be reused in the replacement as back-references, enabling swaps like turning last, first into first last in one pass.",
"The match count is the safety net. Before copying, check that the number of replacements matches your expectation. A count of zero usually means a typo or a case mismatch; a suspiciously large count means the pattern is broader than intended. Because the output is shown in full before you copy anything, mistakes are caught before they escape.",
],
"examples": [
("Renaming across a document", "A client renames a product from AeroLite to AeroLite Pro. One pass with whole-word matching updates every standalone mention while leaving URLs and filenames containing the old string untouched, exactly as intended."),
("Cleaning inconsistent spacing", "Pasted text riddled with double spaces and stray tabs is normalised in one regex pass: find \s+ and replace with a single space, then trim the result. What would be dozens of manual edits becomes one operation."),
("Reordering name lists", "A list of names in last, first order becomes first last by finding ^([^,]+), (.*)$ with regex mode enabled and replacing with the capture groups reversed. Hundreds of lines are restructured in a single operation."),
],
"tips": [
"Use whole-word mode for short search terms to avoid partial matches inside longer words.",
"Test regex patterns on a small sample first; a greedy pattern can match more than expected.",
"An empty replace box deletes matches, which is the fastest way to strip unwanted characters.",
"Case-sensitive mode is essential when editing code, where identifiers are case-significant.",
"The match count is your safety check; always glance at it before copying the output.",
],
"faqs": [
("What is regex mode for?", "It lets you match patterns instead of literal text, such as any number, any whitespace run, or any word in a list. It is the standard pattern language used by programmers and power tools."),
("Can I use capture groups in the replacement?", "Yes. In regex mode, groups defined with parentheses in the pattern can be referenced in the replacement, which enables reordering and restructuring in a single pass."),
("Why did my replacement find zero matches?", "The most common causes are a case mismatch with case-sensitivity enabled, invisible extra spaces in the search box, or a regex character that needs escaping. Try case-insensitive mode first."),
("Does it replace inside words by default?", "Yes, literal matching finds the search string wherever it occurs. Turn on whole-word matching to restrict replacements to standalone words."),
("Is my text uploaded anywhere?", "No. All processing happens locally in your browser, so confidential documents never leave your device."),
("Can I process very large documents?", "Yes. The tool handles large texts comfortably. Extremely long files with complex regex may take a moment on older devices, but there is no artificial size limit."),
],
},
"text-sorter": {
"intro": [
"Lists are everywhere, and unsorted lists are hard to use: name lists that need alphabetical order, keyword lists to group, code lines that must be consistent, or a random draw that needs shuffling fairly. This Line Sorter organises any list of lines instantly, with the sorting modes real work actually requires.",
"Paste your list and choose a mode: alphabetical A to Z, reverse alphabetical, shortest line first, longest line first, or a random shuffle. Numerical sorting understands that 9 comes before 10, which plain text sorting gets wrong, and case handling keeps mixed-capitalisation lists predictable.",
"Teachers use it for class lists and draws, developers for normalising config files and dependency lists, writers for organising notes, and analysts for quick data checks. Sorting happens entirely in your browser, so there is no limit on list privacy or size beyond your device's memory.",
],
"how": [
"Paste one entry per line, click the sorting mode you need, and the sorted list appears immediately. The original input stays in place until you copy the output, so trying several modes on the same list is encouraged.",
],
"steps": [
"Paste or type your list, one entry per line.",
"Choose a mode: A to Z, Z to A, by length, or shuffle.",
"Enable numeric mode if your lines start with numbers that should sort by value.",
"Review the sorted output.",
"Copy the result, or try another mode on the same input.",
],
"works": [
"Alphabetical sorting compares lines character by character using standard text ordering. Case handling matters here: by default the comparison ignores case so that apple and Apple sort together, avoiding the classic problem where all capitalised words sort before all lowercase ones.",
"Numeric mode detects leading numbers on each line and sorts by their value, so 2, 10 and 100 sort in true numerical order instead of the text order 1, 10, 100, 2. Lines without a leading number fall back to text comparison, keeping mixed lists stable and predictable.",
"Length modes measure each line and order by character count, which is useful for finding the shortest labels or the longest descriptions in a list. Shuffle uses a random generator to reorder lines uniformly at random, giving every arrangement an equal chance, which is exactly what a fair draw or a randomised test order requires.",
],
"examples": [
("Alphabetising a name list", "A class list of 60 names pasted in arbitrary order becomes alphabetical in one click, ready for a register, seating chart or certificate printing."),
("Sorting version numbers", "Version strings like v2.10 and v2.9 sort wrongly in plain text. Numeric mode reads the leading numbers so release lists order correctly by actual version value."),
("Random draws", "Paste participant names, click shuffle, and read the winner from the top of the list. Every ordering is equally likely, which keeps classroom draws and prize picks fair."),
],
"tips": [
"Clean duplicates first with the Remove Duplicate Lines tool, then sort for a tidy final list.",
"Use numeric mode whenever lines begin with numbers; text order will surprise you otherwise.",
"Shuffle twice if you want extra confidence in a draw; each run is independent.",
"Length mode is a quick way to spot outliers, such as labels that are too long for a UI.",
"Blank lines sort to the top; remove them first if you want a clean result.",
],
"faqs": [
("How are numbers sorted?", "With numeric mode enabled, lines are compared by the value of their leading number, so 9 sorts before 10. Without it, lines sort as plain text."),
("Is the shuffle fair?", "Yes. It uses a uniform random shuffle, meaning every possible ordering is equally likely, which is appropriate for draws and randomisation."),
("Does sorting ignore capitalisation?", "Yes, by default comparisons are case-insensitive so mixed-capitalisation lists sort naturally together."),
("Will my original list be changed?", "No. The sorted result is shown separately; your input stays as typed until you replace it."),
("Can I sort a very long list?", "Yes. Lists of tens of thousands of lines sort instantly in a modern browser."),
("Is anything uploaded?", "No. All sorting happens locally in your browser."),
],
},
"lorem-ipsum-generator": {
"intro": [
"Placeholder text lets design and layout work proceed before the real copy exists. Lorem ipsum has been the standard filler since the 1500s precisely because it looks like language: realistic word lengths, familiar punctuation, readable rhythm, but no distracting meaning. This Lorem Ipsum Generator produces clean placeholder text on demand, in exactly the quantity your layout needs.",
"Choose how many paragraphs or sentences you need and the tool generates them instantly. The output is ready to paste into designs, templates, CMS drafts or mockups. Because the generator runs in your browser, there is no waiting and no request, however many times you need to regenerate.",
"Designers use it to test how layouts behave with realistic text density, developers use it to fill templates during development, and content teams use it to reserve space before final copy is approved. The classic vocabulary is deliberately neutral, so stakeholders review the layout rather than editing the placeholder words.",
],
"how": [
"Set the amount of text you need, generate, and copy. The tool produces variation on every click, so regenerating gives you fresh filler rather than the same block repeated.",
],
"steps": [
"Choose whether you want paragraphs, sentences or words.",
"Set the quantity, such as 3 paragraphs or 50 words.",
"Generate the placeholder text.",
"Regenerate if you want a different variation.",
"Copy the output and paste it into your design or document.",
],
"works": [
"The generator draws from the classic lorem ipsum vocabulary, a scrambled excerpt of Latin by Cicero that has served as filler since a printer used it in the 1500s. Words are combined into sentences of realistic length, and sentences into paragraphs, so the texture of the text mimics real prose.",
"Paragraph mode builds whole paragraphs, which is what most page layouts need for realistic density. Sentence mode produces a run of standalone sentences, useful for shorter slots like card bodies and form hints. Word mode gives an exact word count, which matters when a specification says something like fill with about 40 words.",
"Regeneration is genuinely random rather than a fixed block, so clicking generate again produces different text. This matters for design reviews: several distinct placeholder blocks look far more like a finished page than the same paragraph repeated, which is a common giveaway of unfinished work.",
],
"examples": [
("Filling a page layout", "A designer building a magazine-style page generates five paragraphs to fill the body column, checking how the type scale and line length feel with realistic text before the article is written."),
("Testing a component library", "A developer populates card components with two sentences each to verify that buttons and headings align correctly across many cards, then regenerates longer text to test the overflow states."),
("Reserving space in a CMS", "An editor stubs out ten articles with generated paragraphs so the homepage layout can be approved today, with real copy slotted in later without changing the design."),
],
"tips": [
"Match the amount of placeholder to the expected real copy; wildly wrong lengths hide layout problems.",
"Regenerate rather than repeating one block; variety exposes layout issues repetition hides.",
"Use sentence mode for short UI slots and paragraph mode for body copy.",
"Replace placeholders before launch; lorem ipsum in production is a classic embarrassment.",
"For right-to-left or non-Latin layouts, generate equivalent filler in the target script for honest testing.",
],
"faqs": [
("Where does lorem ipsum come from?", "It is scrambled Latin from a passage by Cicero, De Finibus Bonorum et Malorum, used as printer's filler since the 1500s and standardised by the typesetting industry in the 20th century."),
("Why not just use repeated text like aaa?", "Realistic-looking filler exercises line breaking, hyphenation and visual rhythm the way real text will. Repeated characters hide layout problems that placeholder text reveals."),
("Is the generated text always different?", "Yes. Each generation draws randomly from the vocabulary, so clicking generate again produces fresh variations rather than a fixed block."),
("Can I get an exact word count?", "Yes. Word mode generates precisely the number of words you request, which is useful for slots with strict length limits."),
("Does the generator need an internet connection?", "Only to load the page itself. Generation happens locally in your browser and works offline once loaded."),
("Is the text real Latin?", "Not meaningfully. The words come from real Latin but the passages are deliberately scrambled and do not carry coherent meaning, which is exactly the point of filler."),
],
},
"word-frequency-counter": {
"intro": [
"What a text actually says, statistically, can be surprising. The words you lean on, the repetition you did not notice, the keywords that dominate a page: all of this is invisible while reading and obvious once counted. This Word Frequency Counter tallies every word in a text and shows the most frequent ones with visual bars.",
"Paste any text and the tool counts occurrences of every word, lists the top words in order, and displays a bar for each so relative frequency is visible at a glance. Common short words can be filtered out so the meaningful terms rise to the top instead of the, and, of.",
"The tool is used by writers checking for overused words, students analysing sources, marketers comparing their copy against target keywords, SEO practitioners checking term balance, teachers building vocabulary exercises, and researchers doing quick textual analysis. It runs entirely in your browser, so unpublished drafts stay private.",
],
"how": [
"Paste your text and the frequency table appears immediately, ranked from most to least frequent. Toggle the option to ignore common stop words, and set how many top words to display. The bars make relative frequency obvious without reading any numbers.",
],
"steps": [
"Paste or type the text you want to analyse.",
"Review the ranked list of the most frequent words with their counts.",
"Enable the stop-word filter to hide very common words like the and and.",
"Adjust the number of results shown if you want a longer or shorter list.",
"Use the bars to spot words that dominate disproportionately, then edit your text accordingly.",
],
"works": [
"The tool normalises the text before counting: letters are lowercased so that The and the count as one word, and punctuation is stripped so that words followed by commas or periods tally correctly. Each remaining token is tallied, and the totals are sorted by count, with ties broken alphabetically.",
"Stop words are the high-frequency glue words of a language, such as the, a, in and of. They are usually the top of any raw count while carrying little meaning. The filter removes them from the ranking so content words, the ones that carry your message, are what you see. This single option is the difference between a curiosity and an analysis.",
"The bars are scaled to the most frequent word in the filtered list, so the top word's bar is full and everything else is proportional. This makes it easy to see whether frequency falls off smoothly, which is typical, or whether one term dominates, which is usually a signal worth acting on.",
],
"examples": [
("Catching overused words", "A writer pastes a chapter and finds relied appearing 14 times, far above any synonym. A targeted editing pass varies the wording, and re-running the counter confirms the fix."),
("Checking keyword balance", "A marketer pastes a landing page and confirms the target keyword appears appropriately without crowding out natural language, keeping the copy readable and the term properly present."),
("Classroom vocabulary analysis", "A teacher pastes a news article and students compare the top content words before and after reading, connecting statistical patterns to the article's actual topic."),
],
"tips": [
"Always enable the stop-word filter first; raw counts are dominated by glue words.",
"Compare frequency before and after editing to verify that a revision actually varied word use.",
"Singular and plural count separately; words and word are tallied as different terms.",
"Use the bars, not just the numbers, to judge whether a term dominates.",
"For long documents, analyse section by section to see how emphasis shifts across the piece.",
],
"faqs": [
("Are capital letters counted separately?", "No. Words are lowercased before counting, so Dog and dog are tallied together."),
("What are stop words?", "Very common function words such as the, a, an, in, and of. They top almost every raw frequency list while adding little meaning, so the tool can filter them out."),
("Does punctuation affect the counts?", "No. Punctuation is stripped before counting, so hello, and hello count as the same word."),
("Can it analyse other languages?", "Yes. Counting works for any language that separates words with spaces. The stop-word list is English-focused, so for other languages read the unfiltered list."),
("How many top words are shown?", "You control the display length, from a handful to a long tail. The ranking itself covers every distinct word in the text."),
("Is my text uploaded?", "No. All counting happens locally in your browser and nothing is transmitted or stored."),
],
},
}
