# Expander for batch 9+10: brings each new tool into the 1000-1200 word range
X = {
"pdf-merge": {
"deep": [
"Ordering aside, one more practical detail matters when merging: bookmarks and form fields. Page-level copying keeps visible content perfectly, but document-level outlines from the source files are not carried into the merged result, and form fields are flattened to their current appearance in some readers. For purely informational documents this is irrelevant; for forms you intend to keep fillable, merge first and fill in afterwards rather than the reverse.",
],
},
"pdf-split": {
"deep": [
"Splitting also plays a role in file size management. A single page extracted from a large scan is usually far smaller than the whole document, which matters when an upload form enforces a strict limit or an email client chokes on attachments. Extracting only the required pages is often the fastest way to shrink a PDF without any compression step, because you simply stop carrying the pages you do not need.",
],
},
"image-compressor": {
"deep": [
"Transparency is the one property the quality slider cannot preserve. PNG images with transparent backgrounds become solid when saved as JPEG, because that format has no alpha channel. WebP keeps transparency while still compressing hard, which makes it the right target for logos and interface graphics that need to sit on varying backgrounds; JPEG remains the choice only when the image is a rectangle of photography with nothing behind it.",
],
},
"image-cropper": {
"deep": [
"Aspect ratio thinking helps before any numbers are typed. Decide the final shape first, square for avatars, sixteen to nine for a banner, four to three for a card thumbnail, and then position the crop rectangle inside the original at that ratio. Working shape-first prevents the most common disappointment, a crop that fits the platform's box but decapitates the subject, because the framing was chosen around content rather than around the destination format.",
],
"extra_faqs": [
("Can I crop without losing pixels outside the frame?", "The saved file contains only the cropped region, by definition. Your original file on disk is never modified, so you can always return and crop a different region later."),
],
},
"json-to-csv-converter": {
"deep": [
"Character encoding is the quiet variable in CSV work. The tool outputs UTF-8, which covers every language and symbol, and Excel reads it correctly when you open the file directly or choose UTF-8 in the import dialog. Problems appear when a tool assumes a legacy Windows encoding and displays accented characters as mojibake; re-importing with UTF-8 selected fixes it, which is why the import dialog, not the file, is the first thing to check.",
],
},
"meta-tag-generator": {
"deep": [
"Structure your tags in a fixed order in the page head: title first, then description, canonical, Open Graph set, and Twitter set last. A consistent order does not affect rendering, but it makes templates diffable and audits fast, because a missing block is visible at a glance. When you later add hreflang or structured data, appending to an ordered head keeps the file readable instead of descending into tag soup.",
],
"extra_faqs": [
("Do I still need meta keywords?", "No. Major search engines ignored the meta keywords tag years ago because it was spammed into uselessness. Spend the effort on the title and description instead, where real signals live."),
],
},
"keyword-density-checker": {
"deep": [
"Synonyms and variants are the healthy answer to high density. If a phrase for a running shoes guide climbs past three percent, replacing some occurrences with trainers, footwear or the specific model names lowers the count while broadening the topical coverage, which is precisely how natural expert writing behaves. The checker makes this visible: after a synonym pass, the one-word table spreads across more distinct terms instead of spiking on one.",
"Word count changes density arithmetic in non-obvious ways. Adding a two-hundred-word section that never mentions your topic dilutes every existing density figure, which can fix borderline over-optimisation without touching a single existing sentence. The reverse is also true: trimming an article for length silently raises the density of everything left behind, so re-check after major edits in either direction.",
],
},
"xml-sitemap-generator": {
"deep": [
"Sitemaps and internal links are complements, not substitutes. A sitemap tells crawlers a URL exists, but crawl priority still flows through links, so pages that appear in the sitemap and in site navigation get discovered and refreshed fastest. Pages listed only in the sitemap, with no internal link anywhere, are the slowest to be revisited, which is why the fix for a page that never re-indexes is usually better internal linking alongside an up-to-date sitemap file.",
],
"extra_faqs": [
("Should PDF files appear in my sitemap?", "Yes, if they are content worth indexing, such as catalogues, whitepapers or forms. The same loc, lastmod and optional tags apply, and search engines do index PDF documents."),
("How often should I regenerate the file?", "Whenever pages are added, removed or substantially changed. For a static site, every publish; for a busier site, tie regeneration to your deployment so the file never drifts from reality."),
],
},
"slug-generator": {
"deep": [
"Slugs interact with site architecture more than most people expect. A slug is only the last segment; the full URL also carries category and date segments depending on your permalink structure. Short, keyword-led slugs pay off most on flat structures like example.com/post-slug, while deep structures benefit even more from compact slugs because every extra segment adds length and dilutes the keyword's visual weight in search snippets.",
"Changing slugs is a normal part of content maintenance, but it must be paired with redirects. A permanent redirect from the old URL transfers most of the accumulated link equity and keeps bookmarks working; skipping it is the single most damaging slug mistake, converting a cosmetic improvement into a traffic loss. Plan slug changes in batches, redirect every old path, and update internal links to point directly at the new addresses.",
],
},
"invoice-generator": {
"deep": [
"Numbering and records are what turn a document into an accounting trail. Keep the issued PDFs in one folder named by year, and keep a simple spreadsheet alongside it mapping invoice numbers to clients, amounts and payment dates. The generator produces the document; that index turns it into a system, which is what an accountant or tax authority actually asks to see: every invoice accounted for, in order, with nothing missing from the sequence.",
],
"extra_faqs": [
("Can I use it for quotes and estimates too?", "Yes. The layout works for any numbered commercial document: set the title context in your item descriptions, or keep a parallel numbering series like Q-001 for quotes that later convert into invoices."),
],
},
}
