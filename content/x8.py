# Expander for batch 11: brings each new tool into the 1000-1200 word range
X = {
"qr-code-generator": {
"deep": [
"Error correction level deserves a second look because it changes how forgiving your code is in the wild. Level L packs the most data into the smallest modules but tolerates the least damage, while level H sacrifices density for the ability to survive a torn corner, a sticker over part of the code, or a heavily compressed screenshot. For posters, product labels and anything handled by people, H or Q is the safer default; for clean digital displays where the code is rendered crisply, L or M works and stays easier to scan at distance.",
],
},
"text-diff-checker": {
"deep": [
"Line-level comparison is the right default for prose and config files, but it helps to understand what it cannot see. Two lines that differ only in trailing whitespace still count as changed, which is often exactly what you want when debugging a YAML file where an invisible space breaks parsing. Conversely, a paragraph rewritten as one long line shows as a single giant change even if only two words moved; for prose at that granularity, split sentences onto their own lines before comparing and the highlight becomes surgical.",
"Empty lines carry meaning in diffs more than people expect. Removing a blank line between sections registers as a change, and in formats like Markdown or Python that blank line changes how the content renders or parses. When a diff looks noisier than the edit felt, scan for blank-line and indentation churn first; normalising those before comparing often collapses a hundred highlighted lines into the handful that actually matter.",
],
"extra_faqs": [
("Does the diff tool store my text anywhere?", "No. Both text areas are compared entirely in your browser with JavaScript, and nothing is uploaded, logged or saved. Close the tab and the comparison is gone."),
],
},
"markdown-previewer": {
"deep": [
"Understanding the dialect question saves frustration. The previewer follows the common Markdown conventions used by GitHub and most modern editors, so tables, fenced code blocks, task lists and strikethrough behave the way you expect from README files. Some older flavours differ on details like line breaks, where a single trailing space forces a new line; if a preview looks slightly different from another renderer you use, that flavour difference, not an error, is almost always the cause.",
"Copy the generated HTML rather than screenshotting whenever the destination accepts HTML. A screenshot freezes your formatting into an image that cannot be searched, restyled or edited, while the HTML output keeps headings semantic, links clickable and code blocks selectable. Pasting that HTML into a CMS editor, an email composer that accepts rich text, or a help-desk article preserves the structure you authored in Markdown with none of the syntax characters showing.",
],
"extra_faqs": [
("Which Markdown flavour does the previewer follow?", "It follows the common conventions shared by GitHub-flavoured Markdown and most modern editors, including tables, fenced code blocks and task lists, which covers the overwhelming majority of everyday writing."),
("Can I preview very long documents?", "Yes. The preview updates as you type and handles long documents fine, though extremely large files are easier to work with if you split them into sections and preview each while drafting."),
],
},
"image-watermarker": {
"deep": [
"Opacity is the setting most people get wrong on the first pass. A watermark at full strength shouts over the image and ruins the very content you are protecting, while something near five percent disappears on bright screens. The reliable range for a visible-but-courteous watermark sits around twenty to forty percent, high enough to survive a screenshot crop and low enough that the photograph remains the subject. Preview at the size you will actually publish, because a watermark that reads well at full resolution can vanish entirely in a four-hundred-pixel thumbnail.",
"Placement is a trade-off between visibility and vulnerability. Corners are the convention because they stay out of the subject's way, but they are also the first thing a lazy thief crops away. A centred, semi-transparent watermark cannot be cropped out without destroying the image, which is why stock libraries use it for previews. For your own published work, a corner mark at moderate opacity plus keeping originals at full resolution unpublished is a pragmatic balance.",
],
"extra_faqs": [
("Will watermarking reduce my image quality?", "Only slightly and only once. The output is re-encoded when the watermark is drawn, so use a high quality setting; your original file on disk is never modified either way."),
],
},
"favicon-generator": {
"deep": [
"The 512-pixel size in the generated set is not strictly a favicon, it is the touch icon and PWA tile size that modern devices request. Including it costs nothing and prevents Android and iOS from scaling a small favicon up into blur when a visitor saves your site to a home screen. The same logic applies to the 180-pixel Apple touch icon; supplying the exact sizes devices ask for avoids the resampling step that softens edges on icon artwork.",
"If your logo has fine detail, simplify it before generating. Favicons render between sixteen and thirty-two pixels on a browser tab, where a detailed emblem becomes an unreadable smudge. The strongest favicon designs use a single bold shape or letterform from the logo, high contrast against the background, and no text smaller than a single initial. Test the generated icons at actual tab size before shipping, because what looks perfect at 64 pixels can still fail the sixteen-pixel test.",
],
"extra_faqs": [
("Do I need all the generated sizes?", "The 32 and 16 pixel files cover desktop browser tabs, the 180 pixel file covers Apple devices, and the 512 pixel file covers Android home screens. Shipping all of them is a few kilobytes and guarantees a crisp icon everywhere."),
],
},
"base64-image-encoder": {
"deep": [
"The decision to inline an image is a bandwidth trade-off, not a free win. Base64 encoding inflates a file by roughly a third, and the data cannot be cached separately from the document that contains it, so a large inlined hero image is re-downloaded with every page view. The sweet spot is small, rarely-changing graphics that appear on nearly every page, such as interface icons, logos under a few kilobytes, and placeholder patterns, where saving an HTTP request outweighs the size penalty. Large photographs almost always belong in separate cached files.",
"Data URIs also sidestep some embedding restrictions that trip up shared HTML. Email clients that block external images will still render inlined ones, single-file HTML documents stay self-contained when moved between folders or machines, and CSS background images defined as data URIs cannot 404. Those properties make the encoder a standard step when preparing HTML email templates or portable demo files.",
],
},
"stopwatch-online": {
"deep": [
"Timestamp-based timing is why the stopwatch stays accurate even when the browser is busy. The displayed time is always computed from the difference between the current clock and the moment you pressed start, not by counting interval ticks, so background tabs, slow rendering or a briefly frozen page cannot make the recorded time drift. Lap times are captured the same way, each one anchored to real elapsed time rather than to when the interface happened to redraw.",
"Lap versus split is worth keeping straight when you review the table. Each lap row shows both the split, which is the time for that segment alone, and the total elapsed at the moment you pressed the button. Runners use laps for per-kilometre pace, presenters use them to check segment lengths against a run sheet, and quality inspectors use them to time repeated process steps; in every case the split column is the number that answers the question how long did this one take.",
],
"extra_faqs": [
("Does the stopwatch keep running if I switch tabs?", "Yes. Timing is based on real clock timestamps rather than display updates, so the elapsed time stays correct even while the tab is in the background."),
("Can I copy my lap times out of the tool?", "Yes. After stopping, select the lap table and copy it, or take the totals from the display; the values are plain text you can paste into a spreadsheet."),
],
},
"countdown-timer": {
"deep": [
"The progress bar is calibrated against the total distance you set, not against an arbitrary maximum. If you set a countdown for two days, the bar fills across those forty-eight hours; set one for ten minutes and it fills across those ten minutes. That makes the bar an honest at-a-glance indicator of how much of the window has elapsed, which is why it works equally well for a product launch, an exam date or a coffee steeping on the desk.",
"Timezone handling is the detail that matters most for shared deadlines. The timer counts toward the exact moment you select in your browser's local timezone, so if a launch goes live at nine in the morning in one city and colleagues in another timezone copy the same wall-clock time, they will get different instants. For distributed teams, agree on the moment in UTC or share the countdown from the person who owns the deadline, and the displayed remaining time will agree everywhere.",
],
"extra_faqs": [
("What happens when the countdown reaches zero?", "The display shows zeros, the progress bar completes, and a finished state is indicated so you can see at a glance that the deadline has passed rather than mistaking it for a timer that never started."),
],
},
}
