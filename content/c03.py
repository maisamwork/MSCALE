# Batch 3: word-counter, case-converter, remove-duplicate-lines, reverse-text
CONTENT = {
"word-counter": {
"intro": [
"Almost every piece of writing has a limit. Essays specify 2,000 words, meta descriptions cap out near 160 characters, tweets and titles have hard cut-offs, and freelance work is often priced per word. This Word Counter gives you live counts of words, characters, sentences, paragraphs and estimated reading time as you type or paste, so you always know exactly where you stand against a limit.",
"The tool analyses ordinary text instantly: paste a draft, an article, an email or a chapter and every statistic updates in real time. Nothing is uploaded; the analysis happens entirely in your browser, which makes it safe for confidential drafts, unpublished manuscripts and private messages.",
"It is useful for students meeting assignment requirements, writers tracking daily output, marketers fitting copy into character limits, bloggers checking readability, and professionals trimming reports to a page budget. Because counts update live, it also works well as a writing pad: type directly into the box and watch the numbers climb toward your target.",
],
"how": [
"There is nothing to configure. Paste or type text into the box and the statistics panel updates immediately. Clear the box to start again. The counts follow standard word-processing conventions, so the numbers match what you would see in a desktop word processor.",
],
"steps": [
"Type or paste your text into the input area.",
"Watch the live statistics update: words, characters, sentences and paragraphs.",
"Check the estimated reading time to gauge how long an average reader needs.",
"Trim or expand your text until the count fits your target or limit.",
"Copy your text back out when the count is right; nothing was changed in the process.",
],
"works": [
"Words are counted the way word processors do it: any run of visible characters separated by spaces or line breaks is one word. Hyphenated terms like well-known count as a single word, and a string of numbers counts as a word too. Characters are counted both with and without spaces, since different limits specify different things.",
"Sentences are detected by terminal punctuation: a period, question mark or exclamation mark followed by whitespace ends a sentence. Paragraphs are blocks of text separated by blank lines. Reading time is estimated from the words count using a typical adult silent-reading speed of around 200 to 250 words per minute, which is why a 1,000-word article shows a reading time of roughly four to five minutes.",
"Character counts matter as much as word counts online. Search engines truncate titles near 60 characters and descriptions near 160, and social platforms enforce their own limits. Watching the character count while you write is the fastest way to fit copy into these fixed slots without awkward last-minute cuts.",
],
"examples": [
("Meeting an essay limit", "An assignment requires 1,500 to 2,000 words. Watching the live counter while drafting shows when you cross the minimum, and the sentence and paragraph counts help you judge whether the structure matches the length or one section is bloated."),
("Writing for the web", "A meta description must fit 160 characters. Paste the draft line into the tool, watch the character count, and trim until it fits, knowing exactly how many characters remain rather than guessing."),
("Tracking writing output", "A writer with a daily 500-word goal types directly into the box each morning and stops when the counter crosses the line. Over a month the totals turn an intention into a measurable habit."),
],
"tips": [
"Check whether a limit counts words or characters; they are very different constraints.",
"Use the no-spaces character count for platforms that count every keystroke.",
"Reading time assumes adult silent reading; aloud, expect roughly 130 words per minute.",
"Counts update live, so you can delete a sentence and immediately see the effect.",
"For long documents, paste section by section to see each part's contribution.",
],
"faqs": [
("How are words defined?", "Any sequence of visible characters separated by spaces or line breaks counts as one word. This matches the convention used by mainstream word processors."),
("Do counts include the spaces?", "The tool shows both variants: characters with spaces and characters without spaces. Use whichever your limit specifies."),
("How accurate is the reading time?", "It uses an average silent-reading speed of about 200 to 250 words per minute. Individual readers vary, but the estimate is reliable for planning purposes."),
("Is there a limit on text length?", "The tool comfortably handles very long documents in a modern browser. Extremely large texts of several million characters may slow down on older devices."),
("Is my text uploaded anywhere?", "No. All counting happens locally in your browser. Your text never leaves your device, making the tool safe for confidential material."),
("Does it count words in other languages?", "Yes. The whitespace-based counting rule works for any language that separates words with spaces. Languages without spaces, such as Chinese and Japanese, are counted by character instead in most conventions."),
],
},
"case-converter": {
"intro": [
"Text arrives in the wrong case more often than anyone expects: a form that upper-cased every name, a headline typed in lowercase, a spreadsheet of codes that must be uppercase, or a title that needs proper Title Case. Retyping is slow and error-prone. This Case Converter fixes the case of any text instantly, with every common style one click away.",
"The tool supports the everyday styles, UPPERCASE, lowercase and Title Case, plus the programming conventions camelCase, PascalCase, snake_case and kebab-case, and Sentence case for tidying up shouted paragraphs. Paste your text, click the style you need, and copy the result.",
"Writers use it to fix caps-lock accidents and format titles; developers use it to turn labels into variable names; data workers use it to normalise imported lists; students use it for citation styles with strict capitalisation rules. Because everything runs locally in your browser, even confidential text can be converted safely.",
],
"how": [
"Paste your text into the input box, click the button for the case style you want, and the converted text replaces the output area, ready to copy. You can apply several styles in sequence to experiment; each click converts the current text anew.",
],
"steps": [
"Type or paste your text into the input area.",
"Click the style you need, such as UPPERCASE, Title Case or snake_case.",
"Review the converted text in the output area.",
"Apply a different style if needed; each button converts from the current text.",
"Copy the result and paste it wherever it is needed.",
],
"works": [
"UPPERCASE and lowercase use the text's built-in letter mappings, which handle accented and non-Latin letters correctly in modern browsers. Sentence case lowercases everything and then capitalises the first letter of each sentence, detected by punctuation followed by whitespace.",
"Title Case capitalises the first letter of each word. In the simple convention used here every word is capitalised; editorial styles that skip short words like of and the vary by publisher, so apply those exceptions by hand if your style guide requires them.",
"The programming styles first normalise the text into word tokens by splitting on spaces, hyphens and underscores. camelCase joins words with the first word lowercase and subsequent words capitalised; PascalCase capitalises every word; snake_case joins with underscores and lowercases everything; kebab-case joins with hyphens. This token-based approach means multi-word phrases convert cleanly into identifiers ready for code.",
],
"examples": [
("Fixing a caps-lock paragraph", "A colleague sends three paragraphs typed entirely in caps. Paste, click Sentence case, and the text becomes readable instantly, with each sentence correctly capitalised and the shouting gone."),
("Creating a variable name", "The phrase user account balance becomes userAccountBalance in camelCase or user_account_balance in snake_case. Developers converting design copy into code identifiers use this dozens of times a day."),
("Normalising imported data", "A supplier list arrives with mixed-case product codes. Converting everything to UPPERCASE creates one consistent format, which prevents duplicate-looking entries and failed lookups downstream."),
],
"tips": [
"Apply Sentence case before Title Case when cleaning up all-caps text; the result reads better.",
"snake_case and kebab-case strip spaces, so they are ideal for URLs, file names and code.",
"Title Case here capitalises every word; adjust short words manually for strict editorial styles.",
"For acronyms like HTML, convert first, then restore the capitals you need.",
"The tool never changes your original text until you copy the result, so experimenting is safe.",
],
"faqs": [
("What is the difference between camelCase and PascalCase?", "camelCase lowercases the first word (userAccountBalance), while PascalCase capitalises every word including the first (UserAccountBalance). Different languages and teams prefer one or the other."),
("Does Title Case handle small words like of and the?", "This tool capitalises every word for consistency. Many editorial styles leave short words lowercase except at the start, so apply those exceptions manually if your style guide requires it."),
("Will it work with accented characters?", "Yes. Modern case mappings handle letters such as E with accents and other non-Latin scripts correctly, not just the basic English alphabet."),
("Can I convert a whole document?", "Yes. Paste as much text as you need; conversion is instantaneous and runs locally in your browser."),
("What happens to numbers and punctuation?", "They are preserved exactly as typed. Only letters change case, and word boundaries for the programming styles are recognised at spaces, hyphens and underscores."),
("Is my text sent to a server?", "No. All conversions run in your browser, so sensitive text never leaves your device."),
],
},
"remove-duplicate-lines": {
"intro": [
"Duplicate lines creep into lists from everywhere: merged exports, copied email addresses, repeated log entries, combined keyword lists. Cleaning them by hand is tedious and unreliable at any real size. This Remove Duplicate Lines tool deduplicates any list instantly, with options that match how real lists behave.",
"Paste your text and the tool removes repeated lines, keeping the first occurrence of each. Two options handle the common complications: case-insensitive comparison treats Email@example.com and email@example.com as the same entry, and trimming removes stray spaces around lines so that padded duplicates are caught too.",
"It is a workhorse for email and mailing lists, keyword and SEO lists, log analysis, inventory codes, playlist lines, and any dataset where the same value appearing twice is an error. Because processing happens in your browser, private lists never leave your machine.",
],
"how": [
"Paste the list with one entry per line, toggle the comparison options to match your data, and the deduplicated list appears immediately. The tool reports how many lines were removed so you can sanity-check the result at a glance.",
],
"steps": [
"Paste or type your list, with one entry per line.",
"Enable case-insensitive mode if capitalisation should be ignored when comparing.",
"Enable trimming if lines may have leading or trailing spaces.",
"Review the cleaned list and the count of removed duplicates.",
"Copy the result, or clear and paste a new list.",
],
"works": [
"The tool scans the lines in order and keeps a set of entries it has already seen. The first time a line appears it is kept; every later identical line is dropped. This preserves the original order of first appearances, which matters for ranked or grouped lists where reordering would destroy meaning.",
"Case-insensitive mode compares a normalised version of each line: the letters are lowercased for comparison purposes, but the original line is what gets kept and output. So the first-seen capitalisation wins. Trimming works the same way: surrounding whitespace is ignored for comparison, while the trimmed form is output, which is almost always what you want in a clean list.",
"Empty lines are treated like any other line: one blank line is kept and the rest are removed as duplicates. This quietly collapses messy gaps in pasted data while still preserving paragraph structure where it existed. The removed-count readout lets you verify that the scale of the cleanup matches your expectations.",
],
"examples": [
("Cleaning an email list", "A merged signup export contains 4,300 addresses with repeated entries from overlapping campaigns. Running it with case-insensitive and trim enabled removes 312 duplicates, producing a clean list ready for import into a mailing tool."),
("Keyword research dedup", "Combining keyword exports from several sources produces many overlapping terms. Deduplicating the combined list gives an accurate count of unique keywords before prioritisation."),
("Log triage", "A log extract shows the same error line hundreds of times. Deduplicating collapses it to a single instance, instantly revealing the variety of distinct messages behind the noise."),
],
"tips": [
"Enable trimming first for pasted data; invisible trailing spaces are the top cause of missed duplicates.",
"Use case-insensitive mode for emails, names and tags; keep it off for codes where case is significant.",
"The first occurrence is kept, so order your input by importance before deduplicating.",
"Sort the cleaned list afterwards if you need alphabetical order; dedup and sort are separate concerns.",
"Empty lines are deduplicated too, so gappy pastes come out tidy automatically.",
],
"faqs": [
("Does the tool change the order of my list?", "No. Lines keep the position of their first appearance, so a ranked or grouped list stays in order apart from the removed repeats."),
("Which duplicate is kept?", "The first occurrence. Everything after the first appearance of a line is removed, regardless of the options you choose."),
("What is the difference between case-sensitive and case-insensitive mode?", "Case-sensitive treats Apple and apple as different lines. Case-insensitive treats them as the same and keeps whichever appeared first."),
("Can it deduplicate by column in CSV data?", "It compares whole lines. To deduplicate by one column, sort or extract that column first, or paste the column on its own, deduplicate it, and match the results back."),
("How large a list can it handle?", "Lists of tens of thousands of lines process instantly in a modern browser. Very large files of many megabytes may be slower on older devices."),
("Is my data uploaded?", "No. Everything runs locally in your browser; your list never leaves your device."),
],
},
"reverse-text": {
"intro": [
"Reversing text sounds like a novelty until the day you need it: checking palindromes, creating mirror-word puzzles, testing how a layout handles bidirectional text, generating backwards names for a game, or flipping a list so the newest entry comes first. This Reverse Text tool flips characters, words or lines, whichever your task needs.",
"Three distinct modes cover three distinct jobs. Character reversal turns hello into olleh. Word reversal keeps each word intact but reverses their order, turning one two three into three two one. Line reversal flips the order of lines in a list, which is the quickest way to put a newest-first log or feed into chronological order.",
"The tool is instant and entirely local: paste, click a mode, copy the result. Writers, puzzle makers, developers and data cleaners all find a use for it, and because the modes are separate, there is no ambiguity about what will be flipped.",
],
"how": [
"Paste your text, choose one of the three modes, and the reversed result appears immediately. You can switch modes at any time to see the other interpretations of the same input, then copy the one you need.",
],
"steps": [
"Type or paste your text into the input area.",
"Choose a mode: reverse characters, reverse words, or reverse lines.",
"Read the result in the output area, which updates on every mode change.",
"Try another mode if a different interpretation suits your task better.",
"Copy the result when it is right.",
],
"works": [
"Character reversal walks the string from the end to the start and rebuilds it, so every character including spaces and punctuation changes position. Modern JavaScript handles this correctly for most scripts, working on code units, which is accurate for everyday Latin text and emoji in common use.",
"Word reversal splits the text on whitespace, reverses the array of words, and rejoins it with single spaces. Each word's internal spelling is untouched, which preserves readability of the individual words while inverting their sequence. Punctuation attached to a word travels with it, so sentence-final periods end up at the start.",
"Line reversal splits on line breaks, reverses the list, and rejoins it. This is the mode for lists: a chat log, a feed export or a set of timestamps flips from newest-first to oldest-first or back in one click, with every line's content untouched.",
],
"examples": [
("Palindrome checking", "To test whether a phrase is a palindrome, reverse its characters and compare. A name like Hannah reads the same backwards, and puzzle setters use the character mode to verify their clues work."),
("Fixing a backwards list", "An exported chat log lists newest messages first. Line reversal puts it into natural reading order instantly, no matter how many hundreds of lines it contains."),
("Word games and puzzles", "Creating a riddle where the answer must be read backwards, or a word ladder puzzle, needs exact character reversal. The tool guarantees the reversal is perfect rather than trusting manual transcription."),
],
"tips": [
"Choose the mode deliberately; reversing characters when you meant lines produces very different output.",
"Line reversal is the safe way to flip any list; it never alters the content of lines.",
"Word reversal collapses multiple spaces into single spaces in the output.",
"For palindrome checks, strip spaces and punctuation first, then use character mode.",
"Emoji and complex symbols may render oddly after character reversal; check visually for decorative uses.",
],
"faqs": [
("What is the difference between the three modes?", "Characters reverse every single character. Words keep each word intact but flip their order. Lines keep each line intact but flip the order of the lines in the list."),
("Does reversal handle punctuation?", "Yes, punctuation is treated like any other character and moves with the reversal. In word mode it stays attached to its word."),
("Can I reverse text in other languages?", "Yes. The tool works on any text your browser can display. For complex scripts where character order carries meaning, always check the result visually."),
("Why do multiple spaces disappear in word mode?", "Word mode splits on whitespace and rejoins with single spaces, which normalises spacing. Use character mode if exact spacing matters."),
("Is there a length limit?", "The tool handles very long texts instantly. Extremely large pastes may be slower on older devices, but there is no artificial limit."),
("Does anything get uploaded?", "No. Reversal happens entirely in your browser; your text never leaves your device."),
],
},
}
