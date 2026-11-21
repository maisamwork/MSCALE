# -*- coding: utf-8 -*-
import re, json
from .mega1a import _WCRE, _fit

M2DOM = {
"text": {
 "ctx": "Text cleanup is one of those jobs that looks trivial until you are doing it on a real document: data pasted out of a PDF, names copied from a spreadsheet, notes dictated on a phone, a list merged from three sources. Every one of those arrives with stray spacing, line breaks, symbols or formatting that no editor fixes cleanly in one pass. The {name} exists to do exactly one of those passes perfectly, on any amount of text, without uploading any of it.",
 "w3": "The tool processes your text with well-defined regular expressions \u2014 the same pattern-matching machinery used by professional editors, search engines and data pipelines. That means the behavior is predictable and repeatable: the same input always produces the same output, character for character, whether the text is ten words or ten thousand. Nothing is sent to a server, so private notes, customer data and drafts never leave your device.",
 "mis": [
  "Not checking the result before copying it out. Automated cleanup is deterministic, but your input may contain edge cases you did not notice \u2014 scan the output once, especially the first and last lines.",
  "Mixing up what counts as whitespace. Tabs, non-breaking spaces and regular spaces look identical on screen but behave differently in code and spreadsheets \u2014 if a result looks unchanged, the culprit is often an invisible character the operation does not target."],
 "faq": [
  ("Is my text uploaded anywhere?", "No. The {name} runs entirely in your browser with JavaScript \u2014 your text never leaves the page, which makes it safe for confidential drafts, customer data and private notes."),
  ("How much text can it handle?", "Comfortably tens of thousands of words. The processing is a single pass over the string, so even very large documents complete in a fraction of a second on an ordinary device.")],
},
"color": {
 "ctx": "Color values are the plumbing of digital design, and they come in more notations than almost anything else on the web: designers speak in hex, CSS understands rgb() and hsl(), print workflows want percentages, and accessibility guidelines talk in contrast ratios. The {name} translates between those worlds instantly, so you can take a value from a style guide, a screenshot picker or a brand book and use it wherever it needs to go.",
 "w3": "All conversions run on the standard sRGB model that browsers and most design tools assume. The math is deterministic \u2014 the same hex value always produces the same RGB triplet and the same HSL coordinates \u2014 and the results match what Chrome, Figma and the CSS specification produce. Everything is computed locally, so brand palettes and unreleased designs stay on your machine.",
 "mis": [
  "Forgetting the # prefix or pasting an abbreviated three-digit hex. Both are handled \u2014 three-digit values like #36f are expanded correctly \u2014 but a stray space or letter will simply produce no result rather than a wrong color.",
  "Expecting perfect agreement with print. Screens use light (sRGB) and printers use ink (CMYK-ish gamuts), so a color that matches on screen can shift on paper \u2014 these tools convert screen-color values, which is what CSS and design files use."],
 "faq": [
  ("What is the difference between HEX, RGB and HSL?", "They describe the same color in different coordinate systems: HEX packs red, green and blue into a compact code; RGB states those channels directly; HSL describes hue, saturation and lightness, which is far easier to reason about when adjusting a color by hand."),
  ("Can I use the output directly in CSS?", "Yes \u2014 every value shown is valid CSS. Paste hex codes into color properties, or use the rgb() and hsl() forms when you want to animate or adjust channels with calc() or CSS variables.")],
},
"random": {
 "ctx": "Randomness settles arguments, allocates work and removes bias \u2014 provided it is genuinely unpredictable and everyone trusts the process. Drawing straws favors the quick; picking 'something at random' from memory favors the recent and the familiar. The {name} replaces all of that with a clear, repeatable draw that everyone can watch happen, which is usually half the value: people accept a result they saw being made.",
 "w3": "The tool uses JavaScript's Math.random(), a pseudo-random generator seeded from the browser's entropy pool. For draws, picks and shuffles it is more than adequate \u2014 it is uniform, unpredictable in practice and instant. It is not cryptographic, so it should not guard lottery-level stakes or security keys, but for teams, classrooms, games and giveaways its fairness is exactly as good as the question being asked.",
 "mis": [
  "Re-rolling results you dislike. The moment a draw can be repeated until it is agreeable, it stops being random and starts being theater \u2014 decide the rules (one roll, best of three, redraw on a tie) before you press the button.",
  "Feeding in a list with hidden duplicates or blank lines. Doubled names get double chances and empty entries can win a draw \u2014 tidy the input list first and every entry stands an equal, correct chance."],
 "faq": [
  ("Is the result really random?", "It is pseudo-random: generated by the browser's Math.random() from a large entropy pool. For picks, shuffles, draws and games it is uniform and unpredictable in any practical sense \u2014 just not suitable for cryptographic keys."),
  ("Can the same result come up twice?", "Yes \u2014 that is what genuine randomness means. Each press is an independent draw; the tool only prevents repeats where the task demands it, such as unique lottery numbers or shuffled lists.")],
},
"date": {
 "ctx": "Date arithmetic is deceptively hard to do in your head because the calendar is irregular: months run 28 to 31 days, weeks drift across month boundaries, leap years arrive every four years except most century years, and time zones lurk behind every 'what day will that be' question. The {name} handles that irregularity with the browser's own calendar engine, so the answer respects real months, real leap years and real week rules.",
 "w3": "All calculations use the standard Gregorian calendar rules implemented in every browser: leap years divisible by 4 but not by 100 unless also by 400, ISO-8601 week numbering where week 1 contains the first Thursday of the year, and correct month lengths everywhere. The results therefore match official calendars and libraries like date-fns or Python's datetime \u2014 not approximations of them.",
 "mis": [
  "Mixing up date formats. 03/04 means March 4 in the US and April 3 nearly everywhere else \u2014 enter dates through the calendar picker rather than typing digits, and read results in the full unambiguous form the tool prints.",
  "Ignoring that a 'day' can mean different things. Calendar days count every day; business days skip weekends; working days may also skip holidays. Decide which one your deadline, contract or payroll actually means before quoting a number."],
 "faq": [
  ("Does the tool account for leap years?", "Yes \u2014 it uses the browser's calendar engine, which applies the full Gregorian rule (divisible by 4, except centuries unless divisible by 400). February 29 is handled correctly in every direction."),
  ("Are time zones a problem?", "For pure date arithmetic, no: the tool works on calendar dates, which are the same everywhere. Only when a deadline is tied to a specific clock time in a specific zone does the zone need separate attention.")],
},
}

def _m2_extra_faqs(name):
    return [
 ("Does the {name} work on mobile?".format(name=name), "Yes \u2014 the layout adapts to small screens and the same processing runs in every modern mobile browser, so the tool works wherever you are."),
 ("Is there a limit on how often I can use it?", "No. There is no sign-up, no quota and no watermark \u2014 use it as often as the task needs."),
 ("Can I undo a conversion?", "There is nothing to undo: your original input stays untouched in its field, and the result is written separately. Clear the result or edit the input and run it again at any time."),
 ("Why choose this over doing it manually?", f"For a single value, manual work is fine; for anything repeated, the {name.lower()} is faster, never has an off day, and applies exactly the same rule every time \u2014 which is what consistency across a document or dataset requires."),
]

def m2_article(f):
    slug, name, cat, short, about, uses, got, ex_t, ex_b = f
    dom = M2DOM[{"Text Tools": "text", "Color Tools": "color", "Random Generators": "random", "Date & Time Tools": "date"}[cat]]
    intro = [
        about + " The tool on this page does that one job cleanly: open it, give it your input, and the result appears immediately \u2014 free, with no sign-up, no ads inside the work area and nothing uploaded to any server.",
        dom["ctx"].format(name=name),
        dom["w3"].format(name=name),
    ]
    how = (f"Using the {name.lower()} is a single pass. Give the tool your input \u2014 paste text, pick a value or press the action button, depending on what the tool takes \u2014 and the result appears instantly in the output area. "
           "Copy it with the copy button, adjust the input, and run it again as many times as you like; nothing is cached or locked in. "
           "If the result looks odd, re-read the input for hidden characters or a wrong unit \u2014 the tool applies its rule exactly, so surprises almost always live in the input, not the logic. "
           "Everything happens on your device, so the page keeps working offline once it has loaded.")
    steps = [
        "Open the tool and give it your input \u2014 paste, type or pick, exactly as the interface prompts.",
        "Set any options the tool offers (a value to find, a count, a format) before running the action.",
        "Press the action button or simply edit the input \u2014 the result updates immediately either way.",
        "Read the whole output, not just the headline; the detail lines are where edge cases show up.",
        "Copy the result to your clipboard, or download it where the tool offers that.",
        "If the input changes later, come back and re-run \u2014 the tool is stateless, so results are always reproducible.",
    ]
    works = [
        f"Under the hood the {name.lower()} is a small, explicit function: it takes your input, applies one well-defined rule \u2014 {short.split(' for ')[0].lower() if ' for ' in short else short.lower()} \u2014 and writes the output. There is no hidden preprocessing, no 'smart' guessing and no server-side model deciding what you meant; the behavior you see is the behavior the code specifies.",
        "The processing is deterministic and local. JavaScript runs the same steps on the same input every time, at double-precision where numbers are involved, and the page never contacts a server \u2014 which is why results are instant, repeatable and private.",
        "The interface follows a strict input-to-output flow with the result clearly separated from the input, so you can compare the two side by side, verify the transformation line by line, and copy the output without ever touching the original.",
    ]
    examples = [
        (ex_t, ex_b),
        ("A quick sanity check", f"However you use the {name.lower()}, it is worth running one input whose answer you already know. If the tool reproduces your known answer, you can trust it for the inputs you do not know \u2014 that two-minute habit catches misread options and paste errors before they reach a document."),
        ("Where this earns its keep", f"In practice this shows up in {uses[0]}, {uses[1]} and {uses[2]}. The common thread is that the task is easy once, tedious twice and error-prone by the tenth time \u2014 exactly the profile of work that should be delegated to a small, reliable tool."),
    ]
    mistakes = [
        dom["mis"][0],
        dom["mis"][1],
        got,
        "Assuming the tool 'knows' your intent. It applies the stated rule literally \u2014 if you meant something slightly different, adjust the options or the input rather than expecting inference.",
        "Skipping the copy step and retyping results by hand. Manual transcription is where good tool output goes to die; use the clipboard.",
    ]
    tips = [
        f"Keep the {name.lower()} open in a second tab while you work \u2014 round-tripping between your document and the tool takes seconds.",
        "Prepare your input before you start: clean input in, clean output out.",
        "If the tool offers options, set them deliberately once and reuse the same settings across a project for consistency.",
        "For recurring work, note the exact input and settings you used so any result can be reproduced later.",
        "Use the copy button rather than selecting text by hand \u2014 it grabs the exact output with no stray whitespace.",
        "Bookmark the page if the task recurs weekly; the tool loads instantly and works offline after the first visit.",
    ]
    faqs = [
        (dom["faq"][0][0].format(name=name), dom["faq"][0][1].format(name=name)),
        (dom["faq"][1][0].format(name=name), dom["faq"][1][1].format(name=name)),
        ("Is the tool free?", "Yes \u2014 completely free, with no account, no usage cap and no restrictions on commercial use of the results."),
        ("What happens to my input after I close the page?", "Nothing persists. The tool holds your input only in the current page's memory; closing or refreshing the tab clears everything."),
    ]
    a = {"intro": intro, "how": [how], "steps": steps, "works": works,
         "examples": examples, "mistakes": mistakes, "tips": tips, "faqs": faqs,
         "_fn": name, "_tn": "result"}
    return _fit(a)

TX_SVG = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m16 3 4 4-4 4"/><path d="M20 7H4"/><path d="m8 21-4-4 4-4"/><path d="M4 17h16"/></svg>'

def tx_body(conf, extra="", ph="Paste or type your text here\u2026"):
    c = json.dumps(conf)
    return f'''<div class="panel">
  <label for="tx-in">Input text</label>
  <textarea id="tx-in" rows="7" placeholder="{ph}" autocomplete="off"></textarea>
  {extra}
  <div class="btnrow">
    <button class="btn" onclick="txRun()">{TX_SVG} Process</button>
    <button class="btn ghost" onclick="txCopyOut()">Copy result</button>
    <button class="btn ghost" onclick="txClear()">Clear</button>
    <button class="btn ghost" onclick="tx2Sample()">Load sample</button>
    <button class="btn ghost" onclick="tx2Download()">Download result</button>
    <button class="btn ghost" onclick="tx2Swap()">Use result as input</button>
  </div>
  <div id="tx2-stats" class="jf-stats" style="margin:10px 0"></div>
  <label for="tx-out">Result</label>
  <textarea id="tx-out" rows="7" readonly placeholder="Result appears here\u2026"></textarea>
</div>
<script>window.TX_CONF={c};</script>'''

TXF = {
"prefix-suffix": ('<div class="row"><div><label for="tx-pre">Prefix (added before each line)</label><input type="text" id="tx-pre" placeholder="- " autocomplete="off" /></div><div><label for="tx-suf">Suffix (added after each line)</label><input type="text" id="tx-suf" placeholder="" autocomplete="off" /></div></div>'),
"occurrences": ('<div class="row"><div><label for="tx-find">Text to count</label><input type="text" id="tx-find" placeholder="the" autocomplete="off" /></div></div>'),
"columns": ('<div class="row"><div><label for="tx-delim">Column separator in the input</label><input type="text" id="tx-delim" value="," autocomplete="off" /></div></div>'),
"join": ('<div class="row"><div><label for="tx-sep">Join lines with</label><input type="text" id="tx-sep" value=", " autocomplete="off" /></div></div>'),
"truncate": ('<div class="row"><div><label for="tx-len">Maximum characters</label><input type="number" id="tx-len" value="100" step="1" /></div></div>'),
}

TEXT = [
("remove-extra-spaces","Remove Extra Spaces","Text Tools","Collapse double spaces, tabs and blank lines in one pass",
 "Extra spaces are invisible until they bite: a double space after a name, a tab hiding between two columns, a blank line that breaks a CSV import. They survive copy-paste from PDFs, chat apps and OCR scans, and no word processor finds them all reliably. This tool collapses every run of whitespace into a single space, trims each line and removes repeated blank lines, leaving clean, even text.",
 ["cleaning text pasted from PDFs","preparing copy for publication","tidying data before import","fixing OCR output"],
 "The tool trims leading and trailing spaces on each line too \u2014 if you actually rely on indentation, use a tool that preserves it instead.",
 "Cleaning a pasted paragraph","Paste the paragraph, press Process, and every double space, stray tab and doubled blank line is gone \u2014 the output reads evenly with single spacing throughout, ready to paste into your document.",
 "spaces", {}, "", "Paste text with messy spacing\u2026"),
("remove-line-breaks","Remove Line Breaks","Text Tools","Join broken lines into flowing paragraphs or single lines",
 "Text copied from PDFs, emails and some websites arrives chopped into short lines, one fragment per row, which wrecks wrapping when you paste it elsewhere. This tool removes the line breaks and joins the fragments into continuous text \u2014 either one flowing paragraph or a single line \u2014 while optionally keeping intentional paragraph breaks intact.",
 ["fixing text copied from PDFs","preparing subtitles or captions","joining wrapped email text","cleaning scraped content"],
 "If you need paragraph breaks preserved, put a blank line between paragraphs before processing \u2014 the tool keeps those.",
 "Turning a wrapped email into a paragraph","Paste the chopped text, press Process, and the mid-sentence breaks vanish \u2014 the output is one continuous paragraph you can paste into a document or CMS without reflow surprises.",
 "linebreaks", {}, "", "Paste line-broken text\u2026"),
("remove-special-characters","Remove Special Characters","Text Tools","Strip symbols and punctuation, keep letters, digits and spaces",
 "Symbols that are harmless in prose are poison in data: accents that break old encodings, emoji that crash a parser, punctuation that corrupts a filename or a CSV field. This tool strips everything except letters, digits and spaces, and it normalizes accented letters to their plain equivalents first so names like Jos\u00e9 survive as Jose.",
 ["preparing identifiers and filenames","cleaning data for CSV or database import","making URL-safe slugs","normalizing text for search indexes"],
 "The tool transliterates common accented letters (\u00e9 \u2192 e, \u00fc \u2192 u) before stripping, so words stay readable instead of losing letters.",
 "Cleaning a name list for import","Paste the list, press Process, and accents, emoji and punctuation are gone \u2014 what remains is plain letters and digits that any system will accept without a fight.",
 "specialchars", {}, "", "Paste text with symbols, accents or emoji\u2026"),
("add-prefix-suffix","Add Prefix and Suffix","Text Tools","Add text before and after every line at once",
 "Turning a list into quoted strings, adding a country code to phone numbers, wrapping every line in an HTML tag, prefixing CSS selectors \u2014 these are all the same job: add fixed text before and after each line. Doing it by hand is exactly as tedious as it sounds. This tool applies a prefix, a suffix or both to every non-empty line in one press.",
 ["wrapping lines in quotes or tags","adding codes or prefixes to IDs","building HTML from plain lists","preparing bulk commands"],
 "Empty lines are skipped, so a list with blank separators keeps its structure instead of gaining empty quoted strings.",
 "Quoting a list of product codes","Paste the codes, set the prefix and suffix to double quotes, press Process, and every line comes back wrapped \u2014 ready to paste into code, a formula or a CSV field.",
 "prefixsuffix", {}, TXF["prefix-suffix"], "One item per line\u2026"),
("extract-emails","Extract Emails from Text","Text Tools","Pull every email address out of any text, deduplicated",
 "Inboxes, CRM exports, meeting notes and web pages all bury email addresses inside larger text. Collecting them by hand is slow and error-prone; a wrong character makes an address undeliverable. This tool scans the text with a proper email pattern and returns every address it finds, one per line, with duplicates removed.",
 ["building a contact list from notes","auditing a document for addresses","cleaning up pasted email threads","checking which addresses appear where"],
 "The tool deduplicates case-insensitively \u2014 Name@Example.com and name@example.com count as one address \u2014 and preserves the first form it saw.",
 "Harvesting addresses from meeting notes","Paste the raw notes, press Process, and every address in the text appears as a clean list \u2014 sorted by first appearance, with duplicates collapsed, ready to paste into your CRM.",
 "emails", {}, "", "Paste any text containing email addresses\u2026"),
("extract-numbers","Extract Numbers from Text","Text Tools","Pull every number out of text, including decimals and negatives",
 "Reports, invoices and measurements arrive as prose with the numbers scattered through it. Pulling them out by hand invites transcription errors \u2014 exactly the kind that quietly change a total. This tool extracts every number, including decimals and negative values, and lists them one per line so you can sum, chart or import them directly.",
 ["pulling figures from reports","extracting measurements from specs","collecting prices from listings","preparing data for a spreadsheet"],
 "Numbers glued to words (like 2024Q3) are extracted as written \u2014 check context if you need the figures interpreted, not just listed.",
 "Extracting prices from a listing page","Paste the page text, press Process, and every price and quantity appears as a plain list \u2014 paste it into a spreadsheet and the numbers are ready to sum or chart.",
 "numbers", {}, "", "Paste text containing numbers\u2026"),
("extract-urls","Extract URLs from Text","Text Tools","Find every link in a document or page source",
 "Whether you are auditing a document's links, harvesting sources from notes or pulling addresses out of a log, links hide in prose, markdown and raw HTML alike. This tool extracts every http and https URL it finds, deduplicates the list and hands it back one per line \u2014 ready for a link checker, a crawler or a bibliography.",
 ["auditing the links in a document","collecting sources from research notes","pulling URLs from logs or page source","building a crawl or check list"],
 "Trailing punctuation is stripped intelligently \u2014 a URL ending a sentence is extracted without the final period, comma or bracket.",
 "Collecting sources from an article draft","Paste the draft, press Process, and every link appears as a clean list with duplicates removed \u2014 paste it into your notes or a link-checking tool and nothing gets missed.",
 "urls", {}, "", "Paste text or page source containing links\u2026"),
("count-occurrences","Count Occurrences","Text Tools","Count how often a word or phrase appears in your text",
 "Word frequency matters more than it seems: writers check for overused words, teachers check for plagiarism patterns, analysts count brand mentions, editors verify a term is used consistently. This tool counts every occurrence of a phrase \u2014 case-insensitively, across line breaks \u2014 and reports the total at a glance.",
 ["checking for overused words in writing","counting keyword mentions in copy","verifying consistent terminology","quick text analysis for research"],
 "The count is case-insensitive and matches inside longer words too \u2014 searching for 'cat' will count 'category' \u2014 so pick your search term with that in mind.",
 "Checking keyword usage in an article","Paste the article, type the keyword, press Process, and you get the exact number of mentions \u2014 enough to know whether the term is emphasized, balanced or missing.",
 "occurrences", {}, TXF["occurrences"], "Paste the text to search in\u2026"),
("text-to-columns","Text to Columns","Text Tools","Split each line into tab-separated columns on any delimiter",
 "Comma-separated data pasted into tools that do not parse it, name lists exported as 'Last, First', log lines glued together with semicolons \u2014 messy delimiters are a daily nuisance. This tool splits every line on the separator you choose and re-joins the pieces with tabs, so a spreadsheet's paste splits them into columns automatically.",
 ["preparing data for spreadsheet paste","splitting name lists into fields","normalizing log lines","converting CSV fragments to TSV"],
 "Quoted commas inside values (like Smith, John) will still split \u2014 clean the input first or choose a delimiter that does not appear in the data.",
 "Turning 'Last, First' into two columns","Paste the name list with comma as the delimiter, press Process, and each line comes back tab-separated \u2014 paste into a spreadsheet and the names land in two tidy columns.",
 "columns", {}, TXF["columns"], "One record per line, e.g. Smith, John\u2026"),
("join-lines","Join Lines","Text Tools","Merge many lines into one line with any separator",
 "Turning a list into a comma-separated string is a tiny chore that appears everywhere: building an SQL IN clause, a CSS selector list, a set of tags, a list of email recipients. This tool joins all your lines into one, using whatever separator you type \u2014 comma, space, pipe, or something exotic \u2014 and skips empty lines so the result stays clean.",
 ["building SQL IN clauses","creating comma-separated tag lists","joining code fragments","flattening lists for single-line fields"],
 "The separator is literal \u2014 type a comma and space if you want ', ' \u2014 and blank lines are dropped automatically so you never get doubled separators.",
 "Building a tag list from a column of words","Paste the words, set the separator to ', ', press Process, and the whole column becomes one tag string \u2014 ready to paste into a CMS field or a config file.",
 "join", {}, TXF["join"], "One item per line\u2026"),
("add-line-numbers","Add Line Numbers","Text Tools","Number every line of a list or document",
 "Numbered lists make anything checkable: checklists, test steps, code reviews, agenda points. Word processors renumber when text moves, and plain-text contexts have no numbering at all. This tool prefixes every line with its number \u2014 permanently, in the text itself \u2014 so the numbering survives any copy, paste or export.",
 ["numbering checklists and procedures","preparing code review comments","making printable agendas","referencing specific lines in feedback"],
 "The numbers are real characters, not formatting \u2014 they will not renumber automatically if you reorder the lines afterwards.",
 "Numbering a checklist for a printed handout","Paste the steps, press Process, and every line is prefixed 1., 2., 3. \u2014 print it, share it or paste it anywhere and the numbering travels with the text.",
 "linenumbers", {}, "", "Paste the lines to number\u2026"),
("truncate-text","Truncate Text","Text Tools","Cut text to an exact character limit, cleanly",
 "Meta descriptions, tweets, SMS fields, database columns and UI labels all enforce hard character limits \u2014 and counting characters by hand is exactly as fun as it sounds. This tool cuts your text to the limit you set and appends an ellipsis when it truncates, so nothing is silently lost and the cut is always visible.",
 ["writing meta descriptions to length limits","fitting text into UI labels","preparing SMS and notification copy","checking database field lengths"],
 "The limit counts every character including spaces and the appended ellipsis \u2014 the same way databases and search engines count.",
 "Fitting a meta description to 160 characters","Paste the description, set the limit to 160, press Process, and you get the exact text that fits \u2014 if it was truncated you will see the ellipsis and know to tighten the copy.",
 "truncate", {}, TXF["truncate"], "Paste the text to trim\u2026"),
("swap-case","Swap Case Converter","Text Tools","Flip uppercase to lowercase and back across the whole text",
 "SHOUTING IN ALL CAPS and whispering in all lowercase are both hard to read, and fixing either by hand means retyping. This tool flips the case of every letter in one pass \u2014 capitals become lowercase and vice versa \u2014 which is the fastest way to neutralize a badly cased paste before reformatting it properly.",
 ["neutralizing all-caps pastes","fixing text typed with Caps Lock on","preparing text for case-sensitive systems","quick formatting experiments"],
 "Swap case is literal: 'Hello WORLD' becomes 'hELLO world'. For proper Title Case or Sentence case, use the Case Converter tool instead.",
 "Taming an all-caps paste","Paste the shouting text, press Process, and every letter flips \u2014 the result is lowercase where it was capital and vice versa, a clean base for proper reformatting.",
 "swapcase", {}, "", "Paste text in the wrong case\u2026"),
("alternate-case","Alternate Case Generator","Text Tools","Produce aLtErNaTiNg CaPs for memes and mockups",
 "Alternating caps \u2014 the mocking sponge case of internet fame \u2014 is also genuinely useful for testing: it exercises case-insensitive matching, makes placeholder text impossible to mistake for real copy, and produces distinctive demo strings. This tool alternates the case of every letter in your text on demand.",
 ["creating meme and parody text","making unmistakable placeholder copy","testing case-insensitive matching","generating demo content"],
 "Alternation applies to letters only \u2014 digits and punctuation pass through untouched, so numbers and spacing stay exactly as you typed them.",
 "Making unmistakable placeholder text","Paste any sentence, press Process, and every other letter flips case \u2014 the output is instantly recognizable as placeholder, which stops dummy text reaching production by accident.",
 "altcase", {}, "", "Type or paste any text\u2026"),
("remove-numbers","Remove Numbers from Text","Text Tools","Strip digits from text, keeping words and punctuation",
 "Footnote markers, page numbers, timestamps and pasted table fragments leave digits scattered through otherwise clean text. When you need the words alone \u2014 for a summary, a search index or a pronunciation pass \u2014 this tool removes every digit in one pass while leaving letters, punctuation and spacing untouched.",
 ["cleaning text scraped from paginated sources","removing footnote and page numbers","preparing text for pronunciation tools","stripping IDs from pasted records"],
 "Dates and prices are numbers too \u2014 stripping digits removes them along with the noise, so keep a copy of the original if you may need them back.",
 "Cleaning scraped page text","Paste the fragmented text, press Process, and every digit disappears \u2014 what remains is the prose itself, ready for summarizing or quoting without stray figures.",
 "removenumbers", {}, "", "Paste text containing stray numbers\u2026"),
]

COLOR = [
("hex-to-rgb","HEX to RGB Converter","Color Tools","Convert any hex color to RGB values for CSS and design",
 "Hex codes are the lingua franca of web color, but plenty of tools, APIs and design specs want plain RGB numbers instead \u2014 rgba() with opacity, canvas drawing, image editors, accessibility math. This converter takes any hex value (three or six digits, with or without the hash) and returns the exact RGB triplet plus a live preview of the color itself.",
 ["writing CSS rgba() values","canvas and SVG drawing code","matching colors in image editors","accessibility contrast calculations"],
 "Three-digit hex like #36f is expanded automatically \u2014 each digit doubles \u2014 so #36f and #3366ff are the same color.",
 "Converting a brand hex to RGB","Paste #3366ff, and the tool shows rgb(51, 102, 255) immediately with a swatch preview \u2014 copy the RGB form straight into a canvas script or an image editor's custom color dialog.",
 "hex2rgb"),
("rgb-to-hex","RGB to HEX Converter","Color Tools","Convert RGB values to a hex code with a live preview",
 "Color pickers in design tools hand you RGB numbers, while CSS stylesheets, brand guides and most web tooling expect hex. This converter takes three channel values, clamps them to the valid 0\u2013255 range, and produces the six-digit hex code with a live swatch so you can confirm you have the color you meant before copying it.",
 ["converting picker values to CSS hex","matching screen colors to brand guides","building color palettes in code","documenting design tokens"],
 "Values outside 0\u2013255 are clamped, not rejected \u2014 a slider that overshoots cannot silently produce an invalid color.",
 "Converting a designer's RGB spec","The designer specifies rgb(220, 90, 43); enter the three values, read #DC5A2B with the swatch confirming the shade, and paste the hex into the stylesheet with confidence.",
 "rgb2hex"),
("hex-to-hsl","HEX to HSL Converter","Color Tools","Convert hex colors to HSL for easier color adjustments",
 "Hex tells you the channels but not the character of a color; HSL \u2014 hue, saturation, lightness \u2014 describes what humans actually perceive. Converting hex to HSL is the first step in building variants: spin the hue for a related color, drop the lightness for a hover state. This converter shows the exact hsl() values plus a live preview.",
 ["creating hover and active states","building color variations from a base","matching colors described by hue","teaching and learning color theory"],
 "HSL lightness is perceptual, not physical \u2014 two colors with equal lightness can look different in brightness depending on hue, which is why contrast still needs checking.",
 "Deriving a hover state from a brand color","Convert the brand hex to hsl(225, 100%, 60%), then read the values and know exactly which dial to turn \u2014 drop lightness ten points for the hover variant and you are done.",
 "hex2hsl"),
("rgb-to-hsl","RGB to HSL Converter","Color Tools","Convert RGB channel values to hue, saturation and lightness",
 "When your source is a color picker or an image editor, you have RGB; when your goal is an adjustable color, you want HSL. This converter translates the channel triplet into hue, saturation and lightness with the standard CSS algorithm \u2014 the same math browsers use internally \u2014 and previews the result so you can verify at a glance.",
 ["preparing theme variables from picker colors","analyzing palettes by hue and tone","converting legacy CSS to modern forms","color science coursework"],
 "The conversion is exact, not approximate: rgb(51, 102, 255) always yields hsl(225, 100%, 60%), matching browser dev tools and the CSS spec.",
 "Converting picker output for a theme file","Enter the picked RGB values, read the hsl() string, and paste it into a CSS custom property \u2014 from then on the whole theme can be tuned by adjusting one lightness variable.",
 "rgb2hsl"),
("color-shades-generator","Color Shades Generator","Color Tools","Generate tints and shades of any color in even steps",
 "Design systems need scales, not single colors: a base brand color plus lighter tints for backgrounds and darker shades for hover states and shadows. This generator takes any hex color and produces an evenly stepped scale from near-white to near-black, each swatch clickable to copy its hex \u2014 a usable palette in one press.",
 ["building design-system color scales","hover, active and disabled states","chart and data-viz palettes","background and border hierarchies"],
 "The steps are even in lightness, not in perceptual contrast \u2014 verify text-on-background pairs with the contrast checker before committing a scale to production.",
 "Building a ten-step brand scale","Enter the brand hex, press Generate, and ten swatches appear from lightest tint to deepest shade \u2014 click each one to copy its hex and the scale is ready for the design tokens file.",
 "shades"),
("complementary-color","Complementary Color Finder","Color Tools","Find the exact opposite color, plus split complements",
 "The color directly opposite another on the wheel is its complement \u2014 maximum contrast, maximum vibrance when paired, and the basis of countless logos and CTAs. This tool computes the true complement of any hex color by rotating the hue 180 degrees, and adds the split complements (plus and minus 150 degrees) for subtler palettes.",
 ["call-to-action button colors","logo and brand accent pairing","art and illustration color schemes","finding readable accents for a base color"],
 "A pure complement is maximum-contrast, not maximum-tasteful \u2014 split complements and adjusted saturation usually read better in real UI work.",
 "Finding an accent for a brand blue","Enter the brand blue, read its orange complement plus the two split-complement options, and preview each against the base \u2014 pick the pairing that keeps text readable and the design lively.",
 "complementary"),
("color-contrast-checker","Color Contrast Checker","Color Tools","Check WCAG contrast ratios with AA and AAA pass levels",
 "Contrast is the difference between text people can read and text they squint at or bounce off \u2014 and it is a legal requirement under WCAG for public sites. This checker computes the exact contrast ratio between a text color and a background color, then grades it against the official AA and AAA thresholds for both normal and large text, with a live preview of the pairing.",
 ["auditing website accessibility","choosing text colors for backgrounds","passing WCAG compliance checks","designing dark-mode palettes"],
 "The thresholds are 4.5:1 for normal text and 3:1 for large text at AA; AAA doubles the demand at 7:1 and 4.5:1 \u2014 aim for AA minimum everywhere.",
 "Checking a button's text color","Enter the white text and the brand green background, read the ratio \u2014 if it falls under 4.5:1 the tool flags the AA failure and you darken the green or switch to dark text before shipping.",
 "contrast"),
("random-color-generator","Random Color Generator","Color Tools","Generate random colors with hex, RGB and HSL all at once",
 "A random color is a surprisingly practical thing: seed palettes for brainstorming, test values for CSS, placeholder swatches for mockups, or a starting point when a blank canvas stalls. This generator produces a random color and shows all three notations at once \u2014 hex, RGB and HSL \u2014 with a large preview swatch and one-click copy.",
 ["brainstorming palette starting points","generating test values for CSS","placeholder colors for mockups","creative exercises and games"],
 "Pure random hues cluster chaotically \u2014 if you want usable schemes, generate several and keep the ones that share a saturation and lightness range.",
 "Seeding a palette for a new project","Press Generate a few times, keep the two or three results that feel right, and copy their hex codes into the mood board \u2014 the random start beats staring at a blank artboard.",
 "random"),
("invert-color","Invert Color Tool","Color Tools","Invert any color to its photographic negative",
 "Inverting a color keeps its brightness roughly where it was while flipping every channel \u2014 which is exactly how photographic negatives work, and exactly what you need when a dark-mode design needs the 'same' color in reverse. This tool inverts any hex value and previews the original beside the result.",
 ["adapting colors for dark mode","creating photographic negative effects","generating high-contrast opposites","testing logo colors on flipped backgrounds"],
 "Inversion is channel-flipping, not hue-rotation: the inverse of a mid-gray is a mid-gray, so near-neutral colors stay near-neutral.",
 "Flipping a light-mode accent for dark mode","Enter the light accent color, read the inverted value, and preview it on the dark background \u2014 a one-step starting point that usually needs only a small saturation tweak.",
 "invert"),
("grayscale-converter","Grayscale Converter","Color Tools","Convert any color to its exact grayscale equivalent",
 "Grayscale conversion reveals the brightness structure of a design: if a layout works in gray, it works in color, and if two colors look identical in gray, they carry the same visual weight. This tool converts any hex color to gray using proper luminance weighting \u2014 green counts brighter than red, red brighter than blue \u2014 rather than a naive average.",
 ["checking designs for color-blind safety","verifying visual hierarchy in print","creating monochrome versions of logos","luminance-based contrast work"],
 "The tool uses luminance weighting (about 0.299 red, 0.587 green, 0.114 blue), so its gray matches how bright the color actually appears \u2014 not a flat average of channels.",
 "Checking a chart's hierarchy in grayscale","Convert each chart color to its gray equivalent and compare the values \u2014 if two series convert to nearly the same gray, color-blind readers cannot tell them apart and the palette needs another differentiator.",
 "grayscale"),
]

def col_body(kind):
    if kind == "hex2rgb":
        ui = ('<div class="row"><div><label for="cx-in">Hex color</label><input type="text" id="cx-in" value="#3366ff" autocomplete="off" oninput="cxHex()"/></div>'
              '<div><label>Preview</label><div id="cx-prev" class="swatch"></div></div></div>'
              '<div id="cx-out" class="result" aria-live="polite"></div>'
              '<button class="btn ghost" onclick="cxCopy(\'rgb\')">Copy RGB</button>')
    elif kind == "rgb2hex":
        ui = ('<div class="row"><div><label for="cr-r">Red (0\u2013255)</label><input type="number" id="cr-r" min="0" max="255" value="220" oninput="cxRgb()"/></div>'
              '<div><label for="cr-g">Green (0\u2013255)</label><input type="number" id="cr-g" min="0" max="255" value="90" oninput="cxRgb()"/></div>'
              '<div><label for="cr-b">Blue (0\u2013255)</label><input type="number" id="cr-b" min="0" max="255" value="43" oninput="cxRgb()"/></div></div>'
              '<div id="cr-out" class="result" aria-live="polite"></div>'
              '<div id="cr-prev" class="swatch"></div>'
              '<button class="btn ghost" onclick="cxCopy(\'hex\')">Copy hex</button>')
    elif kind == "hex2hsl":
        ui = ('<div class="row"><div><label for="ch-in">Hex color</label><input type="text" id="ch-in" value="#3366ff" autocomplete="off" oninput="cxHexHsl()"/></div>'
              '<div><label>Preview</label><div id="ch-prev" class="swatch"></div></div></div>'
              '<div id="ch-out" class="result" aria-live="polite"></div>'
              '<button class="btn ghost" onclick="cxCopy(\'hsl\')">Copy HSL</button>')
    elif kind == "rgb2hsl":
        ui = ('<div class="row"><div><label for="rh-r">Red</label><input type="number" id="rh-r" min="0" max="255" value="51" oninput="cxRgbHsl()"/></div>'
              '<div><label for="rh-g">Green</label><input type="number" id="rh-g" min="0" max="255" value="102" oninput="cxRgbHsl()"/></div>'
              '<div><label for="rh-b">Blue</label><input type="number" id="rh-b" min="0" max="255" value="255" oninput="cxRgbHsl()"/></div></div>'
              '<div id="rh-out" class="result" aria-live="polite"></div>'
              '<div id="rh-prev" class="swatch"></div>'
              '<button class="btn ghost" onclick="cxCopy(\'hsl\')">Copy HSL</button>')
    elif kind == "shades":
        ui = ('<div class="row"><div><label for="sh-in">Base color (hex)</label><input type="text" id="sh-in" value="#e05e00" autocomplete="off" oninput="cxShades()"/></div></div>'
              '<button class="btn" onclick="cxShades()">Generate shades</button>'
              '<div id="sh-out" class="shade-grid" aria-live="polite"></div>')
    elif kind == "complementary":
        ui = ('<div class="row"><div><label for="cp-in">Base color (hex)</label><input type="text" id="cp-in" value="#3366ff" autocomplete="off" oninput="cxComp()"/></div></div>'
              '<div id="cp-out" class="result" aria-live="polite"></div>'
              '<div id="cp-prev" class="shade-grid"></div>')
    elif kind == "contrast":
        ui = ('<div class="row"><div><label for="ct-fg">Text color (hex)</label><input type="text" id="ct-fg" value="#ffffff" autocomplete="off" oninput="cxContrast()"/></div>'
              '<div><label for="ct-bg">Background color (hex)</label><input type="text" id="ct-bg" value="#2f7d32" autocomplete="off" oninput="cxContrast()"/></div></div>'
              '<div id="ct-out" class="result" aria-live="polite"></div>'
              '<div id="ct-prev" class="ct-prev">Sample text 16px \u2014 the quick brown fox</div>')
    elif kind == "random":
        ui = ('<button class="btn" onclick="cxRandom()">Generate random color</button>'
              '<div id="rn-out" class="result" aria-live="polite">Press the button to draw a color.</div>'
              '<div id="rn-prev" class="swatch big"></div>'
              '<button class="btn ghost" onclick="cxCopy(\'all\')">Copy values</button>')
    elif kind == "invert":
        ui = ('<div class="row"><div><label for="iv-in">Color (hex)</label><input type="text" id="iv-in" value="#3366ff" autocomplete="off" oninput="cxInvert()"/></div></div>'
              '<div id="iv-out" class="result" aria-live="polite"></div>'
              '<div id="iv-prev" class="shade-grid"></div>')
    else:
        ui = ('<div class="row"><div><label for="gs-in">Color (hex)</label><input type="text" id="gs-in" value="#e05e00" autocomplete="off" oninput="cxGray()"/></div></div>'
              '<div id="gs-out" class="result" aria-live="polite"></div>'
              '<div id="gs-prev" class="shade-grid"></div>')
    return f'<div class="panel">{ui}</div>'
