# Batch 6: hash-generator, jwt-decoder, regex-tester, csv-to-json-converter
CONTENT = {
"hash-generator": {
"intro": [
"A cryptographic hash function turns any input, a password, a file, a message, into a fixed-length fingerprint. The same input always produces the same hash, the tiniest change produces a completely different one, and the process cannot be reversed. This Hash Generator computes SHA-1, SHA-256 and SHA-512 hashes of any text instantly, using your browser's native cryptography.",
"Paste your text and all three hashes appear at once. The tool uses the Web Crypto API, the same vetted implementation your browser uses for secure connections, so the results are trustworthy and match every standards-compliant tool and library.",
"Hashes are used to verify downloads against published checksums, to store password verifiers safely, to detect whether two files or two versions of a document differ, to build signatures and integrity checks, and countless other integrity tasks. Having all three algorithms side by side makes comparing and verifying quick work.",
],
"how": [
"Paste or type your text and the three hash values appear immediately, one per algorithm. Choose lowercase or uppercase output to match whatever you are comparing against, then copy the hash you need.",
],
"steps": [
"Type or paste the text you want to hash.",
"Read the SHA-1, SHA-256 and SHA-512 results, which update live.",
"Pick the output case that matches the checksum you are comparing against.",
"Copy the relevant hash.",
"Change the input to see how completely the hashes change.",
],
"works": [
"Each algorithm processes the input through a series of mixing and compression steps, producing a fixed-length digest: 160 bits for SHA-1, 256 for SHA-256, 512 for SHA-512, displayed as 40, 64 and 128 hex characters respectively. The input is first converted to UTF-8 bytes, so text in any language hashes consistently.",
"Two properties make hashes useful. Determinism means the same input always yields the same digest, which is what makes checksum verification possible. The avalanche effect means changing a single character of input changes roughly half of the output bits, so even near-identical texts produce unrecognisably different hashes.",
"One caution belongs in every honest explanation: SHA-1 is no longer considered collision-resistant and should not be used where an attacker could craft inputs. It remains here because legacy systems still publish SHA-1 checksums. For anything new, SHA-256 is the sensible default, and SHA-512 offers a longer digest with similar properties.",
],
"examples": [
("Verifying a download", "A software site publishes a SHA-256 checksum for its installer. Hash the downloaded file's text representation or use the same published convention, and compare digests: a match confirms the file arrived uncorrupted."),
("Detecting document changes", "Hash a contract draft, send it, and hash the returned version. Identical digests prove the text is unchanged; different digests prove something changed, even if the change is invisible at a glance."),
("Learning hash behaviour", "Type hello, then hello with a trailing space, and compare. The digests share no visible pattern, a memorable demonstration of the avalanche effect for students new to cryptography."),
],
"tips": [
"Use SHA-256 for anything new; keep SHA-1 only for compatibility with legacy checksums.",
"Whitespace counts: a trailing space or newline produces a completely different hash.",
"Match the case convention of the checksum you are comparing; the bytes are the same either way.",
"Hashing proves integrity, not identity; it tells you data is unchanged, not who created it.",
"Password storage needs specialised slow hashing, not a single fast SHA pass.",
],
"faqs": [
("Can a hash be reversed to reveal the input?", "No. Hash functions are one-way. The only practical attack is guessing inputs and comparing hashes, which is why strong, unique passwords matter."),
("Why do SHA-1, SHA-256 and SHA-512 exist side by side?", "They offer different digest lengths and security margins. SHA-256 is today's general-purpose default; SHA-512 suits cases wanting a longer digest; SHA-1 survives mainly in legacy systems."),
("Do these hashes match the ones from other tools?", "Yes. The tool uses standard algorithms on UTF-8 bytes, so results match any compliant implementation for the same input."),
("Does file hashing work here?", "This tool hashes text. For files, use a tool that reads the file bytes directly; the principle and the expected digests are identical."),
("Is hashing the same as encryption?", "No. Encryption is reversible with a key; hashing is not reversible at all. Hashes verify integrity and identity of content, they do not conceal it for later reading."),
("Is my text uploaded?", "No. Hashing runs in your browser using its native cryptography; your text never leaves the device."),
],
},
"jwt-decoder": {
"intro": [
"A JSON Web Token, JWT, is the credential format used by most modern authentication systems: a compact, signed string carrying claims about who you are. It looks opaque, but its first two parts are simply Base64-encoded JSON that anyone can read. This JWT Decoder opens the token up instantly, showing the header, the payload and the expiry status.",
"Paste a token and the tool decodes the header, which names the signing algorithm, and the payload, which carries the claims: subject, issuer, issued-at and expiry timestamps, and any custom claims your system adds. The expiry is interpreted into a human-readable time with a clear expired or valid indication.",
"Developers use it to debug authentication failures, to see exactly which claims a system is issuing, and to check expiry maths; security learners use it to internalise the crucial lesson that JWT contents are readable by anyone, and that only the signature, not encoding, protects integrity. The tool runs locally, so tokens are never transmitted.",
],
"how": [
"Paste the token into the input box and the decoded header and payload appear immediately, formatted as readable JSON. The expiry status line tells you whether the token is currently valid and when it lapses.",
],
"steps": [
"Copy the full JWT from your application, request header or storage.",
"Paste it into the input area.",
"Read the decoded header to see the algorithm and token type.",
"Read the payload to see the claims, including subject and issuer.",
"Check the expiry line to see whether the token is valid and when it expires.",
],
"works": [
"A JWT is three Base64url-encoded segments joined by dots: header, payload and signature. The header is JSON naming the algorithm, typically HS256 or RS256. The payload is JSON containing registered claims such as sub for subject, iss for issuer, iat for issued-at and exp for expiry, expressed as seconds since the Unix epoch, plus any custom claims.",
"The tool decodes the first two segments with the URL-safe Base64 variant and parses the JSON for display. The third segment, the signature, is deliberately not processed: verifying it requires the secret or public key, and this tool does not ask for keys. Decoding shows what a token says; verification is a separate question answered by your backend.",
"The expiry claim is compared against your device's current time and shown as valid or expired with the exact lapse time. A frequent debugging discovery is a clock mismatch: a token that looks valid may be expired on a server whose clock differs, or vice versa. Seeing the exact expiry timestamp resolves that class of confusion quickly.",
],
"examples": [
("Debugging a 401 error", "An API rejects a request as unauthorized. Decoding the token reveals an expiry from yesterday: the client kept using a stale token instead of refreshing. The decoded exp claim turns a mystery into a one-line fix."),
("Inspecting issued claims", "A developer wants to know which roles an identity provider includes in tokens. Decoding a live token lists the exact claim names and values, which is far faster than reading provider documentation."),
("Teaching token safety", "A security instructor pastes a student's token into the decoder, revealing their email and role in plain text. The lesson lands: encoding is not encryption, and tokens must never contain secrets."),
],
"tips": [
"Never paste production tokens into tools that send data to a server; this one runs locally.",
"The signature is not verified here; decoding shows claims, verification needs the key.",
"Check exp first when a token misbehaves; expiry is the most common failure.",
"Claims are just names; custom claims like roles are only meaningful within your system.",
"Tokens are credentials: decoding one does not make it safe to share the original.",
],
"faqs": [
("Does this tool verify the signature?", "No. Verification requires the signing key and belongs on the server. This tool decodes and displays the readable parts, which is exactly what most debugging needs."),
("Is a JWT encrypted?", "Usually not. A standard JWT is only encoded, so anyone holding it can read the claims. Encrypted tokens use the separate JWE format and look similar."),
("Why does my token contain strange characters instead of JSON?", "You may have pasted only part of the token, or the string was altered. A JWT has exactly three dot-separated segments."),
("What does the exp number mean?", "It is seconds since the Unix epoch, the same convention as Unix timestamps. The tool converts it to a readable date and compares it to now."),
("Can decoding damage or invalidate the token?", "No. Decoding is read-only. The token remains valid wherever it is used; nothing about this tool changes it."),
("Is my token uploaded?", "No. Decoding happens entirely in your browser, and the token never leaves your device."),
],
},
"regex-tester": {
"intro": [
"Regular expressions are the sharpest tool in text processing and the easiest to get subtly wrong. A pattern that works on your test string fails on real data; a greedy match swallows too much; a group captures the wrong slice. This Regex Tester shows exactly what your pattern matches, live, with highlighting that makes every match visible.",
"Enter a pattern and a test string, and the tool lists every match with its position, highlighting them inside the original text. Flags such as case-insensitive, global and multiline are a click away, and capture groups are broken out so you can see precisely what each parenthesis captured.",
"Developers use it while writing validation and parsing logic, data workers use it to build extraction patterns, and learners use it to understand how patterns behave. Seeing matches update as you type shortens the write-test-fix loop from minutes to seconds, which is how regex skills actually develop.",
],
"how": [
"Type a pattern, paste a test string, and read the results: highlighted matches in the text plus a list of each match with its position and captured groups. Adjust flags to change how the pattern is interpreted, and refine until the matches are exactly what you need.",
],
"steps": [
"Type or paste your regular expression into the pattern box.",
"Paste your sample text into the test area.",
"Watch the matches highlight and the match list update live.",
"Toggle flags such as case-insensitive, global and multiline as needed.",
"Inspect capture groups for each match, then refine the pattern until it is exact.",
],
"works": [
"The tool compiles your pattern with the browser's regular expression engine, the same syntax used in JavaScript and closely aligned with other mainstream flavours. Each match is reported with its index in the text, its full text, and the contents of any capture groups, numbered in order of their opening parentheses.",
"Flags change interpretation in important ways. Without the global flag the engine stops at the first match, which is useful for testing whether a pattern matches at all. Case-insensitive mode makes letter comparisons ignore case. Multiline mode makes the caret and dollar anchors apply at every line break rather than only at the string's ends.",
"Two classic behaviours become visible here. Greedy quantifiers consume as much as possible, so a dot-star pattern often spans further than intended; the highlight shows this immediately. And special characters such as dots and brackets carry meaning, so a literal dot must be escaped with a backslash. Watching the highlight while toggling these details builds correct intuition faster than any reference page.",
],
"examples": [
("Building an email validation pattern", "Start with a simple pattern, paste a list of valid and invalid addresses, and refine until the highlights divide them correctly. The live feedback shows precisely which edge cases the pattern still accepts."),
("Extracting data from logs", "A pattern with capture groups pulls timestamps and error codes out of log lines. The group breakdown confirms each group captures the intended slice before the pattern goes into production code."),
("Learning anchors and boundaries", "A learner tests the difference between matching cat anywhere and matching it only at word boundaries. The highlight shows category matching in one case and not the other, making the concept concrete."),
],
"tips": [
"Include intentionally tricky cases in your test string: empty lines, duplicates, edge values.",
"Use the global flag to see all matches; without it you only see the first.",
"Escape literal dots, brackets and other special characters, or they will act as operators.",
"Name your capture groups in complex patterns to keep the group list readable.",
"Test the negative case too: strings your pattern should not match are as important as those it should.",
],
"faqs": [
("Which regex flavour does the tool use?", "The browser's JavaScript engine, which follows the ECMAScript flavour. It is very close to PCRE for common patterns, with minor differences in advanced constructs."),
("What do the flags mean?", "Global finds all matches rather than stopping at the first. Case-insensitive ignores letter case. Multiline makes anchors apply at line breaks. Dotall lets the dot match newlines."),
("Why does my pattern match too much?", "Greedy quantifiers consume as much as possible. Make them lazy with a question mark after the quantifier, or narrow the character class to stop earlier."),
("How do I match a literal dot or bracket?", "Escape it with a backslash. Unescaped, these characters are operators with special meaning."),
("Can the tool replace text too?", "This tool focuses on testing and visualising matches. For replacements, use the Find and Replace tool, which supports regex with capture-group references."),
("Is my pattern or text uploaded?", "No. All matching happens locally in your browser."),
],
},
"csv-to-json-converter": {
"intro": [
"CSV is the universal format for spreadsheets and exports; JSON is the universal format for applications and APIs. Moving data between them by hand is slow and error-prone, especially once quoted fields, embedded commas and different delimiters appear. This CSV to JSON Converter converts tabular data to clean JSON instantly, quote-aware and delimiter-aware.",
"Paste your CSV, optionally enable a header row, and the tool produces a JSON array where each row becomes an object keyed by the header names. Without headers, rows become arrays instead. Tab-separated data works too: the delimiter is detected or set explicitly, so TSV exports convert just as cleanly.",
"Developers use it to turn spreadsheet data into fixtures and mock APIs; analysts use it to move exports into tools that speak JSON; students use it to understand the relationship between the two formats. Quoted fields containing commas, the classic CSV complication, are handled correctly rather than split naively.",
],
"how": [
"Paste your CSV text, confirm the delimiter and header settings, and the JSON output appears immediately. Copy the result or clear it and convert another dataset. Large datasets convert in a moment.",
],
"steps": [
"Paste or type your CSV data, one record per line.",
"Confirm or change the delimiter: comma, semicolon, tab or pipe.",
"Enable the header option if the first row contains column names.",
"Review the JSON output, formatted for readability.",
"Copy the result for use in your code or tool.",
],
"works": [
"The parser reads the input character by character, honouring the CSV quoting rules: a field wrapped in double quotes may contain commas, line breaks and escaped quotes, and those must not be interpreted as structure. This quote-aware parsing is what separates a correct converter from one that silently corrupts data containing quoted commas.",
"With headers enabled, the first row supplies the object keys and every subsequent row becomes an object mapping those keys to its values. Empty cells become empty strings, preserving the row's shape. Without headers, each row becomes an array of values, which suits position-based processing.",
"The output is serialised as readable JSON with consistent indentation, ready for direct use or for further formatting with the JSON Formatter. Numbers remain strings exactly as they appear in the CSV; automatic type conversion is deliberately avoided because guessing types from text is a common source of subtle data bugs.",
],
"examples": [
("Spreadsheet to API fixture", "A product list exported from a spreadsheet, complete with quoted descriptions containing commas, converts into a JSON array used directly as a mock API response during front-end development."),
("Migrating data between tools", "An analytics export in CSV needs to live in a system that only accepts JSON. One conversion preserves every field, including the quoted ones that a naive split on commas would have shredded."),
("Teaching data formats", "A student pastes a five-row table and studies how each CSV row becomes a JSON object, with headers becoming keys. The mapping between the formats becomes obvious in a single example."),
],
"tips": [
"Check the delimiter first; semicolons are common in European exports and pipes in database dumps.",
"Enable the header option only when the first row really is column names.",
"Quoted fields with embedded commas are handled correctly; verify with a sample if unsure.",
"Values stay as strings; convert types in your code where numbers are required.",
"For JSON back to CSV, paste the JSON into a formatter first to inspect the structure you are mapping from.",
],
"faqs": [
("Are quoted commas handled correctly?", "Yes. The parser is quote-aware, so commas inside quoted fields are treated as data, not as delimiters. This is the main correctness feature of a proper CSV parser."),
("Can it convert tab-separated files?", "Yes. Set the delimiter to tab, or let detection choose it, and TSV data converts identically."),
("Why are numbers shown as strings?", "The converter preserves values exactly as they appear in the CSV. Automatic type guessing corrupts data like leading-zero codes, so conversion to numbers is left to your application."),
("What happens to empty cells?", "They become empty strings in the output objects, preserving each row's field count and alignment."),
("Does it support very large files?", "Datasets of thousands of rows convert instantly. Multi-megabyte files may take a moment on older devices but are handled."),
("Is my data uploaded?", "No. The conversion runs entirely in your browser; your data never leaves your device."),
],
},
}
