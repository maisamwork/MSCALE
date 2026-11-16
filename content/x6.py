# Final micro-adjustments
X = {
"dice-roller": {
"extra_faqs": [
("Does the roller work offline?", "Yes. Once the page has loaded, rolling needs no connection, which makes it reliable in basements, campsites and anywhere table games actually happen."),
],
},
"lorem-ipsum-generator": {
"extra_faqs": [
("Can I mix paragraph lengths?", "Yes. Natural paragraphs vary in length, so generate a few batches of different sizes and combine them for the most realistic-looking draft text."),
],
},
"remove-duplicate-lines": {
"extra_faqs": [
("Why did my count of removed lines differ from my expectation?", "Usually invisible whitespace: lines that look identical can differ in trailing spaces. Enable trimming and re-run; the count will match what your eyes expected."),
],
},
"reverse-text": {
"extra_faqs": [
("Does line reversal change line contents at all?", "No. Lines move as complete units, keeping every character intact, which is why it is the safe mode for logs, lists and any structured text."),
],
},
"text-sorter": {
"extra_faqs": [
("What happens to duplicate lines when sorting?", "Duplicates are kept and sort adjacent to each other, which actually makes them easy to spot. Deduplicate first if you want each value to appear once."),
("Can I sort a checklist while keeping its checkboxes?", "The tool sorts whole lines as text. If checkbox markers lead each line, they sort with their lines; verify the result visually if marker position matters."),
],
},
"uuid-generator": {
"extra_faqs": [
("Are these UUIDs safe to use as database primary keys?", "Yes. They are unique across systems and time, which suits distributed generation. For very large tables, add indexes on the columns you query by, as with any key strategy."),
],
},
"word-frequency-counter": {
"extra_faqs": [
("Can I compare two documents' profiles?", "Run the tool on each document separately and compare the top lists. Shared high-frequency content words reveal overlap; differing profiles show where the texts diverge."),
],
},
}
