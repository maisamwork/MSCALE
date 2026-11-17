# -*- coding: utf-8 -*-
# Blog CMS metadata: SEO panel fields, GEO/AEO enrichment, featured-image data,
# related links and length presets for every post.
# Length presets: short 500-800 | standard 800-1200 | detailed 1200-2000 | comprehensive 2000+

LENGTH_RANGES = {"short": (500, 800), "standard": (800, 1200), "detailed": (1200, 2000), "comprehensive": (2000, 100000)}

BASE_URL = "https://maisamwork.github.io/MSCALE/"
AUTHOR = {"name": "MSCALE Tools Team", "type": "Organization", "url": BASE_URL + "blog/"}

BLOG_META = {
"why-word-counts-matter": {
    "category": "Writing",
    "author": AUTHOR,
    "date": "2025-06-01",
    "updated": "2025-11-17",
    "length": "detailed",
    "quick_answer": "Word counts matter because every limit encodes a real constraint on the reader: attention, fairness or screen space. Treat the limit as part of the assignment, budget sections before drafting, count live while you write, and expand only with substance - never with padding.",
    "featured": {
        "alt": "Illustration of a document with a word counter panel showing a target range",
        "caption": "A live counter turns a word limit from a final-exam moment into a steering wheel.",
        "credit": "MSCALE Tools",
    },
    "table": {
        "title": "The three length metrics compared",
        "headers": ["Metric", "What it measures", "Typical use", "Hard limit?"],
        "rows": [
            ["Words", "Amount of substance the reader absorbs", "Essays, articles, freelance briefs", "Rarely hard"],
            ["Characters", "Physical space the text occupies", "Title tags, meta descriptions, social posts", "Usually hard"],
            ["Reading time", "Minutes of attention the piece costs", "Newsletters, video scripts, UX copy", "Soft"],
        ],
    },
    "conclusion": "Word limits are editing tools disguised as bureaucracy. Budget your sections before you draft, watch the count live instead of at the end, cut with rules rather than mood, and expand only with examples, steps and caveats that earn their place. Do that consistently and you will stop resenting limits and start using them - and the work you hand in will be tighter, clearer and more readable than the draft you would have submitted without one.",
    "references": [
        ("Plain English campaign - how to edit for length", "https://www.plainenglish.co.uk/how-to-write-in-plain-english.html"),
        ("MDN Web Docs - title tag length guidance", "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title"),
    ],
    "related_tools": ["word-counter", "case-converter", "text-diff-checker"],
    "seo": {
        "seo_title": "Why Word Counts Matter: A Practical Guide for Writers",
        "meta_desc": "Why word counts matter for essays, blogs and SEO - and how to hit any target without padding. Practical editing rules, live-count workflow and FAQs.",
        "focus_keyword": "why word counts matter",
        "secondary_keywords": ["word count guide", "how to hit a word count", "reading time meaning", "meta description character limit"],
        "search_intent": "Informational - writers and students want to understand and meet length requirements",
        "robots": "index, follow",
    },
},
"strong-passwords-guide": {
    "category": "Security",
    "author": AUTHOR,
    "date": "2025-06-05",
    "updated": "2025-11-17",
    "length": "detailed",
    "quick_answer": "A strong password is long (16+ characters), random and unique to every account, stored in a password manager and protected by two-factor authentication. Length beats symbol tricks, randomness beats clever patterns, and uniqueness stops one breach from cascading into all of your accounts.",
    "featured": {
        "alt": "Illustration of a padlock over a keyboard representing strong password security",
        "caption": "The strongest password is one you never had to invent: long, random and managed.",
        "credit": "MSCALE Tools",
    },
    "table": {
        "title": "Password strategies compared",
        "headers": ["Strategy", "Typical entropy", "Resistant to cracking?", "Resistant to reuse leaks?"],
        "rows": [
            ["Short + symbols (P@ssw0rd!)", "Low - predictable substitutions", "No", "No"],
            ["Long lowercase random (16+)", "High - ~75 bits", "Yes", "Only if unique"],
            ["Manager-generated, unique per site", "High - 80 to 100+ bits", "Yes", "Yes"],
        ],
    },
    "conclusion": "Password security does not require cleverness, only a system. Let a manager generate long random secrets so you never invent them, make every account unique so breaches stop at the border, and switch on two-factor authentication everywhere it is offered. Run the fifteen-minute upgrade today - check your weakest accounts, replace the reused passwords first, and the most common form of account takeover stops applying to you.",
    "references": [
        ("NIST SP 800-63B - Digital Identity Guidelines (password guidance)", "https://pages.nist.gov/800-63-3/sp800-63b.html"),
        ("UK NCSC - three random words password guidance", "https://www.ncsc.gov.uk/blog-post/three-random-words-or-think-random-when-generating-passwords"),
    ],
    "related_tools": ["password-generator", "password-strength-checker", "random-password-generator"],
    "seo": {
        "seo_title": "Strong Passwords: A Practical Guide to Password Security",
        "meta_desc": "What makes a password strong: entropy, length, randomness and uniqueness explained - plus a manager workflow and 2FA habits that stop account takeovers.",
        "focus_keyword": "strong passwords",
        "secondary_keywords": ["password strength", "password entropy", "password manager guide", "two-factor authentication"],
        "search_intent": "Informational - users want to understand and implement better password security",
        "robots": "index, follow",
    },
},
"json-explained": {
    "category": "Development",
    "author": AUTHOR,
    "date": "2025-06-10",
    "updated": "2025-11-17",
    "length": "detailed",
    "quick_answer": "JSON is a text format for structured data: objects written as {\"key\": value} pairs inside curly braces, arrays written inside square brackets, and only six value types allowed - strings, numbers, booleans, null, objects and arrays. Almost every JSON error is one of five syntax mistakes: a trailing comma, an unquoted key, single quotes, an unescaped character, or a comment.",
    "featured": {
        "alt": "Illustration of curly braces and formatted JSON code representing structured data",
        "caption": "JSON is one syntax with six value types - master those and every API response becomes readable.",
        "credit": "MSCALE Tools",
    },
    "table": {
        "title": "JSON values at a glance",
        "headers": ["Type", "Example", "Gotcha"],
        "rows": [
            ["String", "\"hello\"", "Double quotes only - single quotes are invalid"],
            ["Number", "42, 3.14, 1e6", "No leading zeros, no hex, no NaN"],
            ["Boolean", "true / false", "Lowercase only - TRUE is invalid"],
            ["Null", "null", "Lowercase - not NULL or None"],
            ["Object", "{\"key\": \"value\"}", "Keys must be double-quoted strings"],
            ["Array", "[1, 2, 3]", "No trailing comma after the last item"],
        ],
    },
    "conclusion": "JSON is a small language, which is exactly why its errors are so predictable: six value types, two containers, and a handful of syntax rules. Format before you read, validate before you parse, and when something breaks, check the five usual suspects first - trailing commas, unquoted keys, single quotes, unescaped characters and comments. Keep the formatter open in a tab and JSON stops being a source of bugs and becomes what it was designed to be: the simplest reliable way to move structured data between systems.",
    "references": [
        ("MDN Web Docs - Working with JSON", "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON"),
        ("JSON.org - the official grammar", "https://www.json.org/json-en.html"),
    ],
    "related_tools": ["json-formatter", "json-to-csv-converter", "url-parser"],
    "seo": {
        "seo_title": "JSON Explained: Syntax, Common Errors and a Debug Workflow",
        "meta_desc": "JSON explained simply: the six value types, the syntax rules, the five errors behind almost every failure, and a formatting and debugging workflow that works.",
        "focus_keyword": "json explained",
        "secondary_keywords": ["what is json", "json syntax", "json common errors", "json formatter"],
        "search_intent": "Informational - developers learning JSON or debugging invalid JSON",
        "robots": "index, follow",
    },
},
}

def enriched_blocks(slug):
    """Extra blocks appended to a post's base blocks: table before FAQ, conclusion + references after."""
    m = BLOG_META[slug]
    pre, post = [], []
    t = m.get("table")
    if t:
        pre.append(("h2", t["title"]))
        pre.append(("table", t))
    pre.append(("callout", m["quick_answer"]))
    if m.get("conclusion"):
        post.append(("h2", "Conclusion"))
        post.append(("p", m["conclusion"]))
    if m.get("references"):
        post.append(("h2", "References and further reading"))
        post.append(("refs", m["references"]))
    return pre, post

# GEO / AEO quality gates enforced at build time
def geo_checks(post, wordcount):
    m = BLOG_META[post["slug"]]
    errs = []
    if not m.get("quick_answer"):
        errs.append(f'{post["slug"]}: missing quick answer (AEO direct answer)')
    if not m.get("conclusion"):
        errs.append(f'{post["slug"]}: missing conclusion')
    faqs = [v for k, v in post["blocks"] if k == "faq"]
    if not faqs or len(faqs[0]) < 3:
        errs.append(f'{post["slug"]}: needs at least 3 FAQs')
    if not m.get("references"):
        errs.append(f'{post["slug"]}: missing external references (GEO credibility)')
    if not m.get("featured", {}).get("alt"):
        errs.append(f'{post["slug"]}: featured image missing alt text')
    lo, hi = LENGTH_RANGES[m.get("length", "standard")]
    if not (lo <= wordcount <= hi):
        errs.append(f'{post["slug"]}: {wordcount} words outside {m.get("length")} range {lo}-{hi}')
    return errs
