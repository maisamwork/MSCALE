# Expanders batch 3: developer tools
X = {
"json-formatter": {
"deep": [
"Understanding what the parser accepts explains both the errors and the limits. JSON's grammar is tiny: two containers, four scalar types, and strict quoting. Everything else, comments, trailing commas, single quotes, hex numbers, is rejected not because parsers are unkind but because the format's value is its universality. A format every language parses identically cannot afford dialects, and the strictness is the price of that guarantee.",
"For teams, formatting consistency is a collaboration tool. Agreeing on an indentation width and applying it mechanically means diffs show real changes rather than reformatting noise. This is why the tool offers indentation control rather than one fixed style: match your project's convention, and every formatted file blends into the codebase instead of standing out.",
],
"mistakes": [
"Hand-editing JSON without re-validating; a single trailing comma disables an entire configuration file.",
"Assuming an object with duplicate keys is an error the parser will catch; most parsers silently keep the last one.",
"Using single quotes out of JavaScript habit and debugging the resulting parse failure for minutes.",
"Formatting a huge file repeatedly in an editor that reflows the whole document on each save.",
],
"extra_faqs": [
("Does the formatter preserve key order?", "Yes. Objects keep their original key order, which matters because some systems and humans rely on a deliberate ordering even though JSON technically treats objects as unordered."),
("Can it convert JSON to other formats?", "This tool focuses on formatting and validation. For CSV conversion in the other direction, use the CSV to JSON Converter and read the structure it produces."),
],
},
"base64-encoder-decoder": {
"deep": [
"Knowing where Base64 appears in the wild makes the tool's uses concrete. Email attachments ride inside MIME containers as Base64 because email was designed for text. Data URLs embed resources directly in HTML, CSS and JSON. JSON Web Tokens encode their segments with the URL-safe variant. Basic authentication headers are literally the word Basic followed by Base64 of username colon password. Meeting any of these in the wild is a matter of time, and the decoder turns them from opaque strings into readable data.",
"The size cost has a precise arithmetic worth internalising: every 3 bytes become 4 characters, a 33 percent overhead, plus padding. For embedding small icons in stylesheets this is usually a good trade, one fewer request and no cache complexity. For large images it is a poor one, since the overhead multiplies and the benefit of data URLs disappears. The rule of thumb is small assets inline, large assets as files.",
],
"mistakes": [
"Treating Base64 as a security measure and shipping sensitive data thinking it is protected.",
"Embedding large files as data URLs and wondering why the page weight ballooned by a third.",
"Copying Base64 with surrounding whitespace or quotes, which breaks decoding.",
"Mixing up standard and URL-safe variants when moving encoded data between systems.",
],
"extra_faqs": [
("What is URL-safe Base64?", "A variant that replaces the plus and slash characters with minus and underscore so the output can appear in URLs without escaping. If decoding fails, check whether your input uses this variant."),
("Why do some Base64 strings have no padding?", "Some systems strip the trailing equals signs to save space and re-add it implicitly. This tool accepts unpadded input for decoding in most cases."),
],
},
"url-encoder-decoder": {
"deep": [
"The reserved characters are worth knowing by name because each one breaking a URL is a debugging story waiting to happen. The question mark separates the path from the query. The ampersand separates parameters. The equals sign joins a parameter to its value. The hash starts a fragment that never reaches the server. Each of these inside a parameter value must be encoded, or the URL's structure changes in exactly the way its author did not intend.",
"Internationalised URLs add a second layer: the address bar shows readable Unicode, while what travels on the wire is percent-encoded UTF-8. This is why copying a URL with non-Latin text sometimes produces an unreadable string of escapes, and why decoding is the reliable way to see what a link actually contains. Both views are correct; they are just layers of the same system.",
],
"mistakes": [
"Building query strings by string concatenation without encoding values, then debugging why ampersands split parameters.",
"Encoding an entire URL including its structure, when only a parameter value needed encoding.",
"Assuming a plus sign means a space in every context; that convention applies to form data, not paths.",
"Double-encoding by running encoded text through another encoder.",
],
"extra_faqs": [
("Why does my decoded text still look encoded?", "It was probably encoded twice, which happens when a framework encodes automatically and the value was encoded manually first. Decode again to fully restore it."),
("Should path segments be encoded?", "Yes, each segment individually, using component-style encoding. Characters like spaces and slashes inside a segment must be escaped, while the segment separators themselves stay literal."),
],
},
"uuid-generator": {
"deep": [
"Version 4 is the default for good reasons, but the UUID family is worth a glance because the choice of version is a design decision. Version 1 encodes a timestamp and the machine's identity, making IDs sortable but leaking information. Version 7, a newer standard, encodes a timestamp with random remainder, offering sortability without machine identity. Version 4 offers neither sortability nor leakage, which is exactly right when uniqueness is the only requirement.",
"The database angle matters for anyone storing many UUIDs. Random UUIDs scatter across index pages, which is harmless at small scale and measurable at very large scale; this is why systems that generate billions of rows sometimes prefer time-ordered identifiers. For the overwhelming majority of applications, a UUID primary key plus an index on the columns you actually query by is the right, boring answer.",
],
"mistakes": [
"Generating UUIDs one at a time in a loop when a batch would do, for seeding or fixtures.",
"Assuming UUIDs are secret because they look random; they are identifiers, not credentials.",
"Truncating UUIDs to shorter strings for display and then wondering about collisions.",
"Storing UUIDs as numbers, which loses precision, instead of text or a native UUID type.",
],
"extra_faqs": [
("Can I validate a UUID?", "Yes. The canonical form is 32 hex digits in the 8-4-4-4-12 grouping, with the version nibble indicating the type. Anything else is either malformed or a different identifier scheme."),
("Why 122 random bits specifically?", "The 128-bit format reserves a version nibble and a variant field, leaving 122 bits for randomness in version 4. Those bits are what make collisions negligible."),
],
},
"hash-generator": {
"deep": [
"Checksum verification is the workflow most people actually need, and doing it correctly has two details. First, hash the exact bytes: for files that means the file itself, not a copy-pasted representation of it. Second, compare digests case-insensitively and ignore surrounding whitespace, because publishers vary in convention. A match means the data is byte-identical to what the publisher hashed; there is no partial credit, and no need to eyeball hex strings when a comparison does it for you.",
"The security framing is worth stating precisely. Hashes protect integrity, the property that data is unchanged, and they support authentication when combined with a secret key in constructions like HMAC. A bare hash of a password, however, is not password storage: fast hashes are built for speed, and attackers run them billions of times per second on commodity hardware. Dedicated password hashing algorithms exist precisely because this tool's algorithms are the wrong shape for that job.",
],
"mistakes": [
"Using SHA-1 for anything an adversary could influence, given its demonstrated collision weaknesses.",
"Comparing hashes of text with hashes of files and expecting them to relate.",
"Forgetting a trailing newline added by an editor, which changes the digest completely.",
"Using a fast hash for password storage instead of a dedicated password hashing scheme.",
],
"extra_faqs": [
("What is a collision attack?", "Finding two different inputs with the same hash. It defeats signatures and integrity checks, which is why SHA-1's demonstrated collisions retired it for security use while it survives for legacy checksums."),
("Why does the tool hash text and not files?", "Text hashing covers the most common quick needs: verifying strings, learning the algorithms, comparing drafts. File verification tools read raw bytes directly and are the right instrument for downloads."),
],
},
"jwt-decoder": {
"deep": [
"The signature's role deserves a precise description, because decoding a token without understanding it leads to a dangerous misconception. The signature is computed over the header and payload with a secret or private key. Changing one character of the payload invalidates the signature, which is what stops tampering. But nothing about the signature hides the payload: reading requires no key, verifying does. Confidentiality is a separate feature, provided by encrypted token formats when it is actually needed.",
"Algorithm confusion is the classic JWT vulnerability worth knowing about. Systems that trust the header's algorithm field can be tricked into verifying with the wrong method, accepting a token the attacker signed. The defence lives on the server, pinning the expected algorithm. On the client side, the practical rule is simpler: treat decoded claims as unverified data until the backend has done its job.",
],
"mistakes": [
"Putting sensitive data in a JWT payload because it looks opaque; it is readable by anyone holding the token.",
"Assuming a token is valid because it decodes cleanly; decoding says nothing about the signature.",
"Storing tokens in URLs, where they leak into logs and referrer headers.",
"Ignoring the exp claim and reusing tokens long after they should have been refreshed.",
],
"extra_faqs": [
("What is the difference between JWT and session cookies?", "Sessions store state server-side and hand the client an opaque key. JWTs carry the state inside the token itself, signed so it cannot be altered. Each approach has trade-offs in scale and revocation."),
("Can I decode a token without the secret?", "Yes, that is the point of this tool. The header and payload are encoded, not encrypted. Only signature verification needs the key."),
],
},
"regex-tester": {
"deep": [
"A short tour of the constructs that do most of the work in real patterns: alternation with the pipe character chooses between options, so cat|dog matches either. Character classes with ranges, like a-z or 0-9, match one character from a set, and negation with a leading caret matches anything outside the set. Quantifiers apply to the preceding element, and grouping with parentheses both binds quantifiers to sequences and captures text for later use.",
"Lookahead and lookbehind, the zero-width constructs, are the step from competent to powerful: they assert what must surround a match without consuming it, enabling patterns like match every word not followed by a comma. The tester is the ideal place to learn them because the highlight shows exactly what is and is not consumed, which is the property that makes these constructs confusing in prose and obvious in practice.",
],
"mistakes": [
"Writing greedy patterns that swallow more than intended and not noticing until real data breaks them.",
"Forgetting the global flag and concluding a pattern matches only once.",
"Escaping incorrectly, double-escaping characters that needed one backslash.",
"Testing only on clean sample data that lacks the messy real-world cases.",
],
"extra_faqs": [
("Why do my results differ from another language's regex?", "Flavours differ in advanced constructs. The core syntax is shared, but features like lookbehind and Unicode handling vary; test in the flavour your code will use."),
("How do I match a whole word?", "Wrap the term in word-boundary anchors, the backslash-b sequence, so cat matches in the cat sat but not in category."),
],
},
"csv-to-json-converter": {
"deep": [
"The quoting rules of CSV are a small standard with big consequences, and they are worth knowing because so much software gets them subtly wrong. A field containing a comma, a quote or a line break must be wrapped in double quotes, and a quote inside a quoted field is escaped by doubling it. Exports from spreadsheet applications follow these rules; hand-generated CSV frequently does not, which is why data from unknown sources deserves a spot check before bulk conversion.",
"Type handling is the other design decision with consequences. This converter deliberately preserves values as strings, because guessing types from text corrupts data in ways that surface far from the cause: leading zeros vanish from codes, large numbers lose precision, and dates get reinterpreted. Applications that know their schema should convert types explicitly, which is one line of code per field and completely predictable.",
],
"mistakes": [
"Splitting on commas naively, which shreds any field containing a quoted comma.",
"Letting a tool auto-convert types and losing leading zeros from codes and phone numbers.",
"Assuming the delimiter is a comma when semicolon and tab exports are common.",
"Forgetting the header row toggle, which shifts every field by one row.",
],
"extra_faqs": [
("Can it handle quoted fields with embedded line breaks?", "Yes. The parser is quote-aware across line breaks, so a quoted description spanning two lines converts as a single field, which is where naive splitters fail visibly."),
("How do I convert JSON back to CSV?", "Flatten the JSON to one object per row with consistent keys, then map each object's values into a comma-separated line with quoting where needed. The reverse direction needs your schema's knowledge."),
],
},
"html-encoder-decoder": {
"deep": [
"Context is the concept that separates correct escaping from cargo-cult escaping. Text placed in an element's body needs the five-character escape. Text placed inside an attribute needs quote escaping as well. Text placed inside a URL parameter needs percent-encoding, not entity encoding. Text placed inside a script block needs JavaScript string escaping. Each context has its own escaping function, and using the entity encoder in the wrong context is a bug, not a style choice.",
"The security framing deserves its own paragraph because this is the defence behind a whole class of attacks. Cross-site scripting happens when attacker-controlled text reaches a browser as markup. Escaping that text before display turns the attack payload into visible characters, defusing it. Every templating language's auto-escaping feature is this exact operation applied automatically, and knowing what it does makes its occasional failures legible.",
],
"mistakes": [
"Pasting user content into HTML without escaping, the root cause of injection bugs.",
"Double-escaping by applying encoding to already-escaped text, producing visible entity codes on the page.",
"Using entity encoding inside JavaScript strings or URL parameters where a different escape belongs.",
"Encoding text that will be processed by a system expecting raw HTML, breaking its formatting.",
],
"extra_faqs": [
("Why does the ampersand need escaping even in URLs?", "Inside HTML, a bare ampersand begins an entity reference, so a URL like page?a=1&b=2 should write the ampersand as an entity to be strictly correct HTML."),
("What is the difference between encoding and sanitising?", "Encoding makes text safe to display as text. Sanitising removes or neutralises dangerous constructs when some HTML is intentionally allowed. They solve different problems and are not interchangeable."),
],
},
}
