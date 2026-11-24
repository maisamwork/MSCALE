
/* --- M15 text & dev engines --- */
function un2() {
  var o = $("un2-out"); var s = _v("un2-in"); var mode = _v("un2-m");
  if (!o) return;
  if (!s) { o.innerHTML = "Paste text or escapes first."; return; }
  var res;
  if (mode === "e") {
    var outp = [];
    for (var ch of Array.from(s)) {
      var cp = ch.codePointAt(0);
      outp.push(cp > 0xFFFF ? "\\u{" + cp.toString(16) + "}" : "\\u" + cp.toString(16).padStart(4, "0"));
    }
    res = outp.join("");
    o.innerHTML = "<b>Encoded:</b><div class='result' style='margin-top:6px;word-break:break-all;white-space:pre-wrap'>" + escHtml(res) + "</div><span class='jf-chip'><b>" + Array.from(s).length + "</b>code points escaped</span>";
  } else {
    var m, parts = [], re = /\\u\{([0-9a-fA-F]+)\}|\\u([0-9a-fA-F]{4})/g, last = 0, str = "";
    while ((m = re.exec(s)) !== null) {
      str += s.slice(last, m.index) + String.fromCodePoint(parseInt(m[1] ? m[1] : m[2], 16));
      last = re.lastIndex;
    }
    str += s.slice(last);
    o.innerHTML = "<b>Decoded:</b><div class='result' style='margin-top:6px;word-break:break-all;white-space:pre-wrap'>" + escHtml(str) + "</div><span class='jf-chip'><b>" + (s.match(/\\u/g) || []).length + "</b>escapes decoded</span>";
  }
}

var NP2_W = {};
(function () {
  var L = "Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey Xray Yankee Zulu".split(" ");
  for (var i = 0; i < 26; i++) NP2_W[String.fromCharCode(65 + i)] = L[i];
  var N = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
  for (var j = 0; j < 10; j++) NP2_W[String(j)] = N[j];
})();
function np2() {
  var o = $("np2-out"); var s = _v("np2-in");
  if (!o) return;
  if (!s.trim()) { o.innerHTML = "Type the word or code to spell."; return; }
  var words = [];
  for (var ch of s.toUpperCase()) {
    if (ch === " ") { words.push("\u2014"); continue; }
    if (NP2_W[ch]) words.push(NP2_W[ch]);
    if (!/[A-Z0-9 ]/.test(ch)) { o.innerHTML = "Sounds only for letters and digits \u2014 " + escHtml(ch) + " is skipped."; }
  }
  o.innerHTML = "<b>" + escHtml(words.join("\u2003")) + "</b><span class='jf-chip'><b>" + words.length + "</b>code words</span><span class='jf-chip'><b>Alfa, Juliett</b>the official odd spellings: one L in Alfa, two Ts in Juliett</span>";
}

var ST5_W = ("a about above after again against all am an and any are aren't as at be because been before being below between both but by can cannot could couldn't did didn't do does doesn't doing don't down during each few for from further had hadn't has hasn't have haven't having he her here hers herself him himself his how i if in into is isn't it its itself let's me more most mustn't my myself no nor not of off on once only or other ought our ours ourselves out over own same shan't she should shouldn't so some such than that the their theirs them themselves then there these they this those through to too under until up very was wasn't we were weren't what when where which while who whom why with won't would wouldn't you your yours yourself yourselves just also ever never now new own time like get got will can't").split(" ");
function st5() {
  var o = $("st5-out"); var s = _v("st5-in");
  if (!o) return;
  if (!s.trim()) { o.innerHTML = "Paste the text to filter."; return; }
  var toks = s.split(/\s+/), kept = [], dropped = 0, total = 0;
  for (var i = 0; i < toks.length; i++) {
    var raw = toks[i]; if (!raw) continue;
    total++;
    var w = raw.toLowerCase().replace(/[^\w'-]/g, "");
    if (ST5_W.indexOf(w) !== -1) dropped++; else kept.push(toks[i]);
  }
  o.innerHTML = "<b>" + kept.length + " of " + total + " words kept</b> (" + nfmt(total ? kept.length / total * 100 : 0, 1) + "%)<div class='result' style='margin-top:6px;white-space:pre-wrap'>" + escHtml(kept.join(" ")) + "</div>" +
    "<span class='jf-chip'><b>" + dropped + "</b>stopwords removed from a 130+ word list</span>" +
    "<span class='jf-chip'><b>" + nfmt(total ? dropped / total * 100 : 0, 1) + "%</b>density reduction</span>";
}

function dw2() {
  var o = $("dw2-out"); var s = _v("dw2-in");
  if (!o) return;
  if (!s.trim()) { o.innerHTML = "Paste the text to check."; return; }
  var words = (s.toLowerCase().match(/[a-z0-9']+/g)) || [], seen = {}, order = [];
  for (var i = 0; i < words.length; i++) {
    if (seen[words[i]]) seen[words[i]].n++;
    else { seen[words[i]] = { n: 1, first: i }; order.push(words[i]); }
  }
  var dups = order.filter(function (w) { return seen[w].n > 1; }).sort(function (a, b) { return seen[b].n - seen[a].n || a.localeCompare(b); });
  if (!dups.length) { o.innerHTML = "<b>No repeated words</b> in " + words.length + " words \u2014 clean." + "<span class='jf-chip'><b>" + words.length + "</b>total words counted</span>"; return; }
  var lines = "";
  for (var j = 0; j < dups.length; j++) lines += "<span class='jf-chip " + (seen[dups[j]].n > 2 ? "jf-chip-bad" : "") + "'><b>" + escHtml(dups[j]) + " \u00d7" + seen[dups[j]].n + "</b>remaining" + (seen[dups[j]].n > 2 ? " \u2014 over-repeat" : "") + "</span>";
  o.innerHTML = "<b>" + dups.length + " word(s) repeated</b> across " + words.length + " words" + lines;
}

function vo2() {
  var o = $("vo2-out"); var s = (_v("vo2-in") || "").toLowerCase();
  if (!o) return;
  if (!s.trim()) { o.innerHTML = "Paste the text to count."; return; }
  var c = { a: 0, e: 0, i: 0, o: 0, u: 0 }, tot = 0;
  for (var i = 0; i < s.length; i++) if (c[s[i]] !== undefined) { c[s[i]]++; tot++; }
  var letters = (s.match(/[a-z]/g) || []).length;
  o.innerHTML = "<b>" + tot + " vowels</b> of " + letters + " letters \u2014 " + nfmt(letters ? tot / letters * 100 : 0, 1) + "% vowel density" +
    "<span class='jf-chip'><b>a\u00d7" + c.a + " e\u00d7" + c.e + " i\u00d7" + c.i + " o\u00d7" + c.o + " u\u00d7" + c.u + "</b>per-vowel counts</span>" +
    "<span class='jf-chip'><b>" + nfmt(tot ? s.length / tot : 0, 1) + " avg</b>text characters per vowel \u2014 screen the sample before inferring</span>" +
    "<span class='jf-chip'><b>" + (letters - tot) + "</b>consonants (y included as consonant)</span>";
}

function ch3sym(d) { return { 0: "---", 1: "--x", 2: "-w-", 3: "-wx", 4: "r--", 5: "r-x", 6: "rw-", 7: "rwx" }[d]; }
function ch3() {
  var o = $("ch3-out"); var io = _v("ch3-o"), ig = _v("ch3-g"), it = _v("ch3-t");
  if (!o) return;
  var oi = parseInt(io, 10), gi = parseInt(ig, 10), ti = parseInt(it, 10);
  if (isNaN(oi) || isNaN(gi) || isNaN(ti)) { o.innerHTML = "Pick a digit for each of owner, group and others."; return; }
  var code = "" + oi + gi + ti, sym = ch3sym(oi) + ch3sym(gi) + ch3sym(ti);
  o.innerHTML = "<b>chmod " + code + "</b>&nbsp;\u2194 rwxr-xr-x\u2010style string <b>" + sym + "</b>" +
    "<span class='jf-chip'><b>" + oi + "</b>owner " + ch3sym(oi).replace(/-/g, "\u2013").replace(/r/, "read").replace(/w/, "\u00b7write").replace(/x/, "\u00b7exec") + "</span>" +
    "<span class='jf-chip'><b>" + gi + "</b>group " + ch3sym(gi) + "</span>" +
    "<span class='jf-chip'><b>" + ti + "</b>others " + ch3sym(ti) + "</span>" +
    (code === "600" ? "<span class='jf-chip jf-chip-bad'>600 = owner only \u2014 correct for private keys, breaks web files</span>" : code === "777" ? "<span class='jf-chip jf-chip-bad'>777 \u2014 anyone can rewrite the file; almost always a mistake</span>" : "");
}

function as2() {
  var o = $("as2-out"); var ch = _v("as2-c"), n = parseFloat($("as2-n") ? $("as2-n").value : "");
  if (!o) return;
  var html = "";
  if (ch) {
    var cps = Array.from(ch), cp = cps[0].codePointAt(0);
    html += "<b>" + escHtml(cps.join(" ")) + "</b> \u2192 decimal <b>" + cp + "</b>, hex <b>0x" + cp.toString(16).toUpperCase() + "</b>, binary <b>" + cp.toString(2).padStart(8, "0") + "</b>";
    if (cp < 32) html += "<span class='jf-chip jf-chip-bad'>Control character \u2014 never prints</span>";
    else html += "<span class='jf-chip'><b>" + (cp <= 0x7F ? "ASCII" : "Unicode beyond 127") + "</b>code band</span>";
  }
  if (!isNaN(n) && n >= 0) {
    var chs = "";
    try { chs = String.fromCodePoint(Math.round(n)); } catch (e2) { chs = "\u2014"; }
    html += (html ? "<div style='margin-top:6px'></div>" : "") + "<b>" + nfmt(n, 0) + "</b> \u2192 character <b>" + escHtml(chs) + "</b>";
  }
  if (!html) { o.innerHTML = "Type a character or a numeric code \u2014 either direction works."; return; }
  o.innerHTML = html;
}

var HS2_DB = { 100: ["Continue", "the client should keep sending the body"], 101: ["Switching Protocols", "a websocket handshake often rewrites this hand"], 102: ["Processing", "server still working, keep waiting"], 103: ["Early Hints", "preload hints sent before the final headers"], 200: ["OK", "request landed; the body has what you asked"], 201: ["Created", "new resource minted; Location header points at it"], 202: ["Accepted", "queued for later \u2014 not done yet"], 204: ["No Content", "success, empty body; look no further than headers"], 206: ["Partial Content", "range request satisfied \u2014 video scrubbing lives here"], 301: ["Moved Permanently", "update links; caches remember this forever"], 302: ["Found", "temporary redirect; keep the original URL"], 303: ["See Other", "fetch the new location with GET"], 304: ["Not Modified", "cache still valid \u2014 free bandwidth won"], 307: ["Temporary Redirect", "like 302 but the method must survive"], 308: ["Permanent Redirect", "301 that must not change method"], 400: ["Bad Request", "malformed syntax \u2014 the server could not read it"], 401: ["Unauthorized", "credentials missing or stale, not insufficient"], 402: ["Payment Required", "reserved, occasionally used by paid APIs"], 403: ["Forbidden", "server understood and refuses \u2014 auth will not help"], 404: ["Not Found", "no resource at this URL did exist then or now"], 405: ["Method Not Allowed", "wrong verb; Allow header lists the survivors"], 406: ["Not Acceptable", "your Accept headers rule out every response"], 408: ["Request Timeout", "client too slow sending the request"], 409: ["Conflict", "state clash \u2014 edit-then-resend or merge"], 410: ["Gone", "was here, deliberately removed; drop the link"], 411: ["Length Required", "Content-Length header mandatory"], 412: ["Precondition Failed", "If-Match or family rejected the request"], 413: ["Payload Too Large", "shrink the body or raise the server cap"], 414: ["URI Too Long", "GET with a novel in the query string"], 415: ["Unsupported Media Type", "wrong Content-Type for the endpoint"], 418: ["I'm a teapot", "the classic joke status; occasions are rare"], 422: ["Unprocessable Entity", "syntax fine, semantics impossible"], 425: ["Too Early", "replayed risk too high \u2014 wait for TLS certainty"], 426: ["Upgrade Required", "the server demands a different protocol"], 428: ["Precondition Required", "condiitional headers are mandatory here"], 429: ["Too Many Requests", "rate limit hit; back off or add jitter"], 431: ["Request Header Fields Too Large", "cookies or headers bloat \u2014 trim them"], 451: ["Unavailable For Legal Reasons", "censorship or court order blocked it"], 500: ["Internal Server Error", "unhandled exception server-side; read the stack trace"], 501: ["Not Implemented", "the method or feature is not supported at all"], 502: ["Bad Gateway", "upstream answered garbage or not at all"], 503: ["Service Unavailable", "overloaded or in maintenance \u2014 retry later"], 504: ["Gateway Timeout", "upstream was too slow to answer"], 505: ["HTTP Version Not Supported", "nobody speaks that protocol version"], 507: ["Insufficient Storage", "server out of room for the resource"], 508: ["Loop Detected", "recursive redirect chain detected"], 511: ["Network Authentication Required", "captive portal wants a login first"] };
function hs2() {
  var o = $("hs2-out"); var c = Math.round(_n("hs2-c") || 0);
  if (!o) return;
  var cat = Math.floor(c / 100), catname = { 1: "Informational", 2: "Success", 3: "Redirect", 4: "Client error", 5: "Server error" }[cat];
  if (!(cat >= 1 && cat <= 5)) { o.innerHTML = "Status codes run 100\u2013599 \u2014 enter one of those."; return; }
  var hit = HS2_DB[c];
  var specific = hit ? "<b>" + c + " " + hit[0] + "</b>&nbsp;&#8212; " + hit[1] : "<b>" + c + "</b> is registered but unofficial \u2014 the class below still applies";
  o.innerHTML = specific +
    "<span class='jf-chip'><b>" + cat + "xx</b>" + catname + " class</span>" +
    (cat === 4 ? "<span class='jf-chip jf-chip-bad'>Client error \u2014 inspect the request before blaming the server</span>" : cat === 5 ? "<span class='jf-chip jf-chip-bad'>Server error \u2014 logs first, request second</span>" : "<span class='jf-chip'><b>" + catname + "</b>no alarm implied by the class itself</span>");
}

function ma2() {
  var o = $("ma2-out"); var s = _v("ma2-in");
  if (!o) return;
  var hex = s.toLowerCase().replace(/[^0-9a-f]/g, "");
  if (hex.length !== 12) { o.innerHTML = "Needs exactly 12 hex digits \u2014 found " + hex.length + " in " + escHtml(s) + ". Separators of any kind are welcome."; return; }
  var pairs = hex.match(/../g), up = pairs.map(function (x) { return x.toUpperCase(); });
  var b0 = parseInt(pairs[0], 16), bits = [];
  bits.push((b0 & 1) ? "multicast" : "unicast");
  bits.push((b0 & 2) ? "locally administered" : "burned-in (OUI)");
  o.innerHTML = "<b>" + up.join(":") + "</b>" +
    "<span class='jf-chip'><b>" + up.join("-") + "</b>hyphen notation (Windows)</span>" +
    "<span class='jf-chip'><b>" + hex.slice(0, 4).toUpperCase() + "." + hex.slice(4, 8).toUpperCase() + "." + hex.slice(8, 12).toUpperCase() + "</b>Cisco dot notation</span>" +
    "<span class='jf-chip'><b>" + bits.join(" \u00b7 ") + "</b>read from the first octet's low bits</span>";
}

function sv2parse(v) {
  var m = String(v || "").trim().match(/^v?(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:-([0-9A-Za-z][0-9A-Za-z.\-]*))?(?:\+[0-9A-Za-z.\-]+)?$/);
  if (!m) return null;
  return { M: parseInt(m[1], 10), m: parseInt(m[2] || 0, 10), p: parseInt(m[3] || 0, 10), pre: m[4] || null };
}
function sv2() {
  var o = $("sv2-out"); var a = sv2parse(_v("sv2-a")), b = sv2parse(_v("sv2-b"));
  if (!o) return;
  if (!a || !b) { o.innerHTML = "Both must be versions like 1.10.0, 2.1 or 3.0.0-rc.1."; return; }
  var verdict, why;
  if (a.M !== b.M) { verdict = a.M > b.M; why = "major field decides: " + a.M + (a.M > b.M ? " > " : " < ") + b.M; }
  else if (a.m !== b.m) { verdict = a.m > b.m; why = "minor field decides: " + a.m + (a.m > b.m ? " > " : " < ") + b.m; }
  else if (a.p !== b.p) { verdict = a.p > b.p; why = "patch field decides: " + a.p + (a.p > b.p ? " > " : " < ") + b.p; }
  else if (a.pre !== b.pre) {
    if (a.pre === null) { verdict = true; why = "pre-release loses: 1.0.0 beats any 1.0.0-rc.x"; }
    else if (b.pre === null) { verdict = false; why = "pre-release loses: 1.0.0 beats any 1.0.0-rc.x"; }
    else { var pa = a.pre.split("."), pb = b.pre.split("."); verdict = 0; why = "pre-release identifiers compare part by part";
      for (var i = 0; i < Math.max(pa.length, pb.length); i++) {
        var wa = pa[i] === undefined ? null : pa[i], wb = pb[i] === undefined ? null : pb[i];
        if (wa === wb) continue;
        if (wa === null) { verdict = true; break; }
        if (wb === null) { verdict = false; break; }
        var na = /^\d+$/.test(wa), nb = /^\d+$/.test(wb);
        if (na && nb) verdict = parseInt(wa, 10) > parseInt(wb, 10) ? true : parseInt(wa, 10) === parseInt(wb, 10) ? verdict : false;
        else if (na) verdict = true; else if (nb) verdict = false; else verdict = wa > wb ? true : wa === wb ? verdict : false;
        if (wa !== wb) break;
      }
    }
  } else { verdict = null; why = "all fields equal"; }
  var color = verdict === null ? "" : verdict ? "" : "";
  var line = verdict === null ? "<b>identical (ignoring build metadata)</b>" : "<b>" + (verdict ? escHtml(_v("sv2-a")) : escHtml(_v("sv2-b"))) + "</b> is newer";
  o.innerHTML = line + "<span class='jf-chip " + color + "'><b>" + why + "</b>deciding rule</span>" +
    "<span class='jf-chip'><b>" + a.M + "." + a.m + "." + a.p + (a.pre ? "-" + a.pre : "") + "</b>parsed A</span>" +
    "<span class='jf-chip'><b>" + b.M + "." + b.m + "." + b.p + (b.pre ? "-" + b.pre : "") + "</b>parsed B</span>";
}

function jq2() {
  var o = $("jq2-out"); var raw = _v("jq2-in");
  if (!o) return;
  var obj;
  try { obj = JSON.parse(raw); } catch (e) { o.innerHTML = "That is not valid JSON \u2014 the parser says: " + escHtml(String(e.message).slice(0, 120)); return; }
  if (obj === null || typeof obj !== "object" || Array.isArray(obj)) { o.innerHTML = "Pass a JSON object at the top level (in curly braces)."; return; }
  var keys = Object.keys(obj).sort(), pairs = [];
  for (var i = 0; i < keys.length; i++) {
    var v = obj[keys[i]];
    var vs = v === null ? "" : (typeof v === "object" ? JSON.stringify(v) : String(v));
    pairs.push(encodeURIComponent(keys[i]) + "=" + encodeURIComponent(vs));
  }
  o.innerHTML = "<b>?" + escHtml(pairs.join("&")) + "</b>" +
    "<span class='jf-chip'><b>" + pairs.length + "</b>parameters, keys sorted</span>" +
    "<span class='jf-chip'><b>percent-encoded once</b>double-encoding corrupts signatures silently</span>" +
    "<span class='jf-chip'><b>decoded check</b>" + escHtml(pairs.length ? decodeURIComponent(pairs[0]) : "\u2014") + "</span>";
}

function ua2() {
  var o = $("ua2-out"); var t = _v("ua2-in");
  if (!o) return;
  if (!t.trim()) { o.innerHTML = "Paste a user-agent string first."; return; }
  var browser = "Unknown", engine = "Unknown", os = "Unknown", dev = "Desktop", bot = /bot|crawl|spider|slurp|headless|facebook|pingdom|uptimerobot/i.test(t);
  var m;
  if ((m = t.match(/Edg(?:e|A|iOS)?\/([\d.]+)/))) browser = "Edge " + m[1];
  else if ((m = t.match(/OPR\/([\d.]+)/))) browser = "Opera " + m[1];
  else if ((m = t.match(/Firefox\/([\d.]+)/))) browser = "Firefox " + m[1];
  else if ((m = t.match(/MSIE ([\d.]+)/))) browser = "Internet Explorer " + m[1];
  else if ((m = t.match(/Chrome\/([\d.]+)/))) browser = "Chrome " + m[1];
  else if ((m = t.match(/Version\/([\d.]+)[\s\S]*Safari/))) browser = "Safari " + m[1];
  if (/Trident/.test(t)) engine = "Trident"; else if (/Gecko|Firefox/.test(t) && !/like Gecko/.test(t)) engine = "Gecko"; else if (/AppleWebKit/.test(t)) engine = /Chrome|Edg|OPR/.test(t) ? "Blink" : "WebKit"; else if (/Presto/.test(t)) engine = "Presto";
  if ((m = t.match(/Windows NT ([\d.]+)/))) os = m[0] === "Windows NT 10.0" ? "Windows 10/11" : "Windows (NT " + m[1] + ")";
  else if (/CrOS/.test(t)) os = "ChromeOS";
  else if ((m = t.match(/Android ([\d.]+)/))) os = "Android " + m[1];
  else if (/iPhone|iPod/.test(t)) os = "iOS"; else if (/iPad/.test(t)) os = "iPadOS";
  else if ((m = t.match(/Mac OS X ([\d_.]+)/))) os = "macOS " + m[1].replace(/_/g, ".");
  else if (/Linux/.test(t)) os = "Linux";
  if (/Mobile|iPhone|iPod/.test(t)) dev = "Mobile"; else if (/iPad|Tablet/.test(t)) dev = "Tablet";
  o.innerHTML = "<b>" + (browser === "Unknown" ? escHtml(t.slice(0, 40)) + "..." : escHtml(browser)) + "</b>on " + escHtml(os) + " \u00b7 " + dev +
    "<span class='jf-chip'><b>" + engine + " engine</b>renders the page</span>" +
    "<span class='jf-chip'><b>" + (bot ? "bot" : "human-ish") + "</b>crawler-pattern scan</span>" +
    (browser === "Chrome" && /Edg/.test(t) ? "<span class='jf-chip jf-chip-bad'>Edge wins \u2014 check fork tokens before Chrome</span>" : "<span class='jf-chip'><b>forks checked first</b>Chromium clones spoof as Chrome</span>");
}

function al2() {
  var o = $("al2-out"); var s = _v("al2-in");
  if (!o) return;
  var lines = s.split(/\n/), outs = [], ids = [];
  for (var i = 0; i < lines.length; i++) {
    var t = lines[i].replace(/^\s*#+\s*/, "").trim();
    if (!t) continue;
    var slug = t.toLowerCase().replace(/[^\w\- ]/g, "").replace(/\s+/g, "-");
    outs.push("[Jump to \u201c" + t + "\u201d](#" + slug + ")");
    ids.push("id=\"" + slug + "\"");
  }
  if (!outs.length) { o.innerHTML = "Paste headings \u2014 one per line, markdown hashes optional."; return; }
  o.innerHTML = "<b>" + outs.length + " anchor(s) generated</b><div class='result' style='margin-top:6px;white-space:pre-wrap'>" + escHtml(outs.join("\n")) + "</div>" +
    "<div style='margin-top:6px;line-height:1.8' class='jf-chip-wrap'>" + ids.map(function (x) { return "<span class='jf-chip'><b>" + escHtml(x) + "</b>put on the heading</span>"; }).join("") + "</div>";
}
