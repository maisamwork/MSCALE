function $(id) { return document.getElementById(id); }
function out(id, html, cls) {
  const n = $(id);
  if (!n) return false;
  n.innerHTML = html;
  n.className = "result" + (cls ? " " + cls : "");
  return true;
}

/* ---------- Calculators ---------- */
let PCT2_MODE = "of", PCT2_ADD = true;
function pct2N(id) { const v = parseFloat($(id).value); return isNaN(v) ? null : v; }
function pct2F(n, d) { return (+n).toLocaleString(undefined, { maximumFractionDigits: d === undefined ? 4 : d }); }
function pct2Mode(m, btn) {
  PCT2_MODE = m;
  document.querySelectorAll(".pct2-pane").forEach(p => { p.style.display = "none"; });
  $("pct2-p-" + m).style.display = "block";
  if (btn) {
    document.querySelectorAll(".pct2-tabs .pg-tab").forEach(t => t.classList.remove("active"));
    btn.classList.add("active");
  }
  pct2Run();
}
function pct2Dir(add, btn) {
  PCT2_ADD = add;
  $("pct2-add").classList.toggle("active", add);
  $("pct2-sub").classList.toggle("active", !add);
  pct2Run();
}
function pct2Big(main, sub) {
  $("pct2-big").innerHTML = main + (sub ? `<span class="pct2-big-sub">${sub}</span>` : "");
}
function pct2Steps(lines) {
  $("pct2-steps").innerHTML = lines.map(l => `<div class="pct2-step">${l}</div>`).join("");
}
function pct2Run() {
  const ex = $("pct2-extra");
  if (PCT2_MODE === "of") {
    const p = pct2N("pct2-of-p"), n = pct2N("pct2-of-n");
    if (p === null || n === null) { pct2Big("\u2014", "Fill in both values"); ex.innerHTML = ""; return; }
    const r = p / 100 * n;
    pct2Big(pct2F(r), `${pct2F(p)}% of ${pct2F(n)}`);
    pct2Steps([
      `<b>Formula:</b> result = (percent \u00f7 100) \u00d7 number`,
      `= (${pct2F(p)} \u00f7 100) \u00d7 ${pct2F(n)} = ${pct2F(p / 100)} \u00d7 ${pct2F(n)} = <b>${pct2F(r)}</b>`
    ]);
    ex.innerHTML = `<span class="pct2-chip">${pct2F(n)} \u2212 ${pct2F(r)} = ${pct2F(n - r)} (remaining)</span><span class="pct2-chip">${pct2F(n)} + ${pct2F(r)} = ${pct2F(n + r)} (total)</span>`;
  } else if (PCT2_MODE === "iswhat") {
    const x = pct2N("pct2-iw-x"), y = pct2N("pct2-iw-y");
    if (x === null || y === null) { pct2Big("\u2014", "Fill in both values"); ex.innerHTML = ""; return; }
    if (y === 0) { pct2Big("\u2014", "Y cannot be zero"); ex.innerHTML = ""; return; }
    const r = x / y * 100;
    pct2Big(pct2F(r) + "%", `${pct2F(x)} out of ${pct2F(y)}`);
    pct2Steps([
      `<b>Formula:</b> percent = (X \u00f7 Y) \u00d7 100`,
      `= (${pct2F(x)} \u00f7 ${pct2F(y)}) \u00d7 100 = ${pct2F(x / y, 6)} \u00d7 100 = <b>${pct2F(r)}%</b>`
    ]);
    ex.innerHTML = `<span class="pct2-chip">Fraction: ${pct2F(x)} / ${pct2F(y)} = ${pct2F(x / y, 4)}</span><span class="pct2-chip">Missing to 100%: ${pct2F(Math.max(0, y - x))}</span>`;
  } else if (PCT2_MODE === "change") {
    const a = pct2N("pct2-ch-a"), b = pct2N("pct2-ch-b");
    if (a === null || b === null) { pct2Big("\u2014", "Fill in both values"); ex.innerHTML = ""; return; }
    if (a === 0) { pct2Big("\u2014", "Old value cannot be zero"); ex.innerHTML = ""; return; }
    const ch = (b - a) / Math.abs(a) * 100;
    const up = ch >= 0;
    pct2Big((up ? "+" : "") + pct2F(ch) + "%", `${up ? "increase" : "decrease"} from ${pct2F(a)} to ${pct2F(b)}`, up);
    pct2Big(`<span class="${up ? "pct2-up" : "pct2-down"}">${up ? "\u2191" : "\u2193"} ${up ? "+" : ""}${pct2F(ch)}%</span>`, `${up ? "increase" : "decrease"} from ${pct2F(a)} to ${pct2F(b)}`);
    pct2Steps([
      `<b>Formula:</b> change = (new \u2212 old) \u00f7 |old| \u00d7 100`,
      `= (${pct2F(b)} \u2212 ${pct2F(a)}) \u00f7 ${pct2F(Math.abs(a))} \u00d7 100 = ${pct2F(b - a)} \u00f7 ${pct2F(Math.abs(a))} \u00d7 100 = <b>${pct2F(ch)}%</b>`
    ]);
    ex.innerHTML = `<span class="pct2-chip">Difference: ${pct2F(b - a)}</span><span class="pct2-chip">Multiplier: \u00d7${pct2F(b / a, 4)}</span>`;
  } else if (PCT2_MODE === "addsub") {
    const n = pct2N("pct2-as-n"), p = pct2N("pct2-as-p");
    if (n === null || p === null) { pct2Big("\u2014", "Fill in both values"); ex.innerHTML = ""; return; }
    const part = p / 100 * n;
    const r = PCT2_ADD ? n + part : n - part;
    pct2Big(pct2F(r), `${PCT2_ADD ? "+" : "\u2212"}${pct2F(p)}% on ${pct2F(n)}`);
    pct2Steps([
      `<b>Formula:</b> ${PCT2_ADD ? "result = number \u00d7 (1 + percent \u00f7 100)" : "result = number \u00d7 (1 \u2212 percent \u00f7 100)"}`,
      `= ${pct2F(n)} \u00d7 ${PCT2_ADD ? "(1 + " + pct2F(p / 100, 6) + ")" : "(1 \u2212 " + pct2F(p / 100, 6) + ")"} = <b>${pct2F(r)}</b>`
    ]);
    ex.innerHTML = `<span class="pct2-chip">${PCT2_ADD ? "Added" : "Removed"}: ${pct2F(part)}</span><span class="pct2-chip">Reverse: ${pct2F(PCT2_ADD ? r / (1 + p / 100) : r / (1 - p / 100))} (original)</span>`;
  } else {
    const f = pct2N("pct2-rv-f"), p = pct2N("pct2-rv-p");
    if (f === null || p === null) { pct2Big("\u2014", "Fill in both values"); ex.innerHTML = ""; return; }
    if (p === -100) { pct2Big("\u2014", "Percent cannot be \u2212100"); ex.innerHTML = ""; return; }
    const base = f / (1 + p / 100);
    pct2Big(pct2F(base), `original before ${pct2F(p)}% was added`);
    pct2Steps([
      `<b>Formula:</b> original = final \u00f7 (1 + percent \u00f7 100)`,
      `= ${pct2F(f)} \u00f7 ${pct2F(1 + p / 100, 6)} = <b>${pct2F(base)}</b>`
    ]);
    ex.innerHTML = `<span class="pct2-chip">Added amount: ${pct2F(f - base)}</span><span class="pct2-chip">Proof: ${pct2F(base)} + ${pct2F(base * p / 100)} = ${pct2F(base + base * p / 100)}</span>`;
  }
}
if ($("pct2-of-p")) pct2Run();

function bmiCalc() {
  const w = parseFloat($("bmi-w").value), h = parseFloat($("bmi-h").value) / 100;
  if (!w || !h) return;
  const bmi = w / (h * h);
  const cat = bmi < 18.5 ? "Underweight" : bmi < 25 ? "Normal weight" : bmi < 30 ? "Overweight" : "Obese";
  out("bmi-out", `BMI: <b>${bmi.toFixed(1)}</b> — ${cat}`);
}

function ageCalc() {
  const dob = new Date($("age-dob").value);
  if (isNaN(dob)) return;
  const now = new Date();
  let y = now.getFullYear() - dob.getFullYear();
  let m = now.getMonth() - dob.getMonth();
  let d = now.getDate() - dob.getDate();
  if (d < 0) { m--; d += new Date(now.getFullYear(), now.getMonth(), 0).getDate(); }
  if (m < 0) { y--; m += 12; }
  const days = Math.floor((now - dob) / 86400000);
  out("age-out", `<b>${y}</b> years, <b>${m}</b> months, <b>${d}</b> days<br><small>${days.toLocaleString()} days old · next birthday in ${Math.ceil((new Date(now.getFullYear(), dob.getMonth(), dob.getDate()) > now ? new Date(now.getFullYear(), dob.getMonth(), dob.getDate()) : new Date(now.getFullYear() + 1, dob.getMonth(), dob.getDate()) - 0).valueOf ? Math.abs((new Date(now.getFullYear(), dob.getMonth(), dob.getDate()) > now ? new Date(now.getFullYear(), dob.getMonth(), dob.getDate()) : new Date(now.getFullYear() + 1, dob.getMonth(), dob.getDate())) - now) / 86400000 : 0)} days</small>`);
}

function emiCalc() {
  const P = parseFloat($("emi-p").value), r = parseFloat($("emi-r").value) / 1200, n = parseFloat($("emi-n").value) * 12;
  if (!P || !n || isNaN(r)) return;
  const emi = r === 0 ? P / n : P * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1);
  const total = emi * n;
  out("emi-out",
    `Monthly EMI: <b>${emi.toFixed(2)}</b><br>Total interest: <b>${(total - P).toFixed(2)}</b><br>Total payment: <b>${total.toFixed(2)}</b>`);
}

/* ---------- Text ---------- */
function wcDur(words, wpm) {
  const m = words / wpm;
  if (m < 1) return "< 1 min";
  if (m < 60) return Math.ceil(m) + " min";
  return (m / 60).toFixed(1) + " hr";
}
function wcPages(words, perPage) {
  const p = words / perPage;
  return p < 0.01 ? "0" : p.toFixed(p < 1 ? 2 : 1);
}
function wcRefTable() {
  const rows = [100, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2500, 3000, 4000, 5000];
  let h = `<table class="wc-table"><thead><tr><th>Words</th><th>Pages (Letter, 250 w/p)</th><th>Pages (A4, 500 w/p)</th><th>Reading (230 wpm)</th><th>Speaking (130 wpm)</th></tr></thead><tbody>`;
  for (const w of rows) {
    h += `<tr><td><b>${w.toLocaleString()}</b></td><td>${wcPages(w, 250)}</td><td>${wcPages(w, 500)}</td><td>${wcDur(w, 230)}</td><td>${wcDur(w, 130)}</td></tr>`;
  }
  $("wc-table").innerHTML = h + "</tbody></table>";
}
const WC_STOP = new Set(("the,a,an,and,or,but,if,then,else,when,at,by,for,with,about,against,between,into,through,during,before,after,above,below,to,from,up,down,in,out,on,off,over,under,again,further,once,here,there,all,any,both,each,few,more,most,other,some,such,no,nor,not,only,own,same,so,than,too,very,can,will,just,should,now,is,are,was,were,be,been,being,have,has,had,having,do,does,did,doing,would,could,ought,i,me,my,we,our,you,your,he,him,his,she,her,it,its,they,them,their,what,which,who,whom,this,that,these,those,am,as,until,while,of").split(","));
function wc2Syllables(w) {
  w = w.toLowerCase().replace(/[^a-z]/g, "");
  if (w.length <= 3) return 1;
  w = w.replace(/(?:[^laeiouy]es|ed|[^laeiouy]e)$/, "").replace(/^y/, "");
  return (w.match(/[aeiouy]{1,2}/g) || ["x"]).length;
}
function wc2Flesch(words, sentences, syl) {
  if (!words || !sentences) return null;
  const score = 206.835 - 1.015 * (words / sentences) - 84.6 * (syl / words);
  return Math.max(0, Math.min(100, score));
}
function wc2ReadLabel(s) {
  if (s === null) return { cls: "r-na", lab: "\u2014", note: "Not enough text yet" };
  if (s >= 90) return { cls: "r-easy", lab: "Very easy", note: "5th grade \u00b7 very simple words" };
  if (s >= 80) return { cls: "r-easy", lab: "Easy", note: "6th grade \u00b7 easy to read" };
  if (s >= 70) return { cls: "r-ok", lab: "Fairly easy", note: "7th grade \u00b7 clear and simple" };
  if (s >= 60) return { cls: "r-ok", lab: "Standard", note: "8th-9th grade \u00b7 plain English" };
  if (s >= 50) return { cls: "r-mid", lab: "Fairly difficult", note: "10th-12th grade \u00b7 some complexity" };
  if (s >= 30) return { cls: "r-hard", lab: "Difficult", note: "College level \u00b7 dense wording" };
  return { cls: "r-hard", lab: "Very difficult", note: "Graduate level \u00b7 best for academics" };
}
function wc2Bar(pct, cls) {
  return `<div class="wc-bar"><div class="wc-bar-fill ${cls || ""}" style="width:${Math.max(2, Math.min(100, pct))}%"></div></div>`;
}
function wc2Stats(t) {
  const trimmed = t.trim();
  const words = trimmed ? trimmed.split(/\s+/).length : 0;
  const sentences = (t.match(/[^.!?]+[.!?]+(\s|$)/g) || (trimmed ? [1] : [])).length;
  const paras = trimmed ? trimmed.split(/\n\s*\n/).filter(p => p.trim()).length : 0;
  const noSp = t.replace(/\s/g, "").length;
  const tokens = (t.toLowerCase().match(/[a-z0-9'\u2019-]+/g) || []);
  const uniq = new Set(tokens).size;
  const letters = t.replace(/[^\w'\u2019-]/g, "").length;
  const avgLen = words ? (letters / words).toFixed(1) : "0";
  let syl = 0;
  for (const w of tokens) syl += wc2Syllables(w);
  const flesch = wc2Flesch(words, sentences, syl);
  const longest = trimmed ? trimmed.split(/(?<=[.!?])\s+/).reduce((a, b) => (b.split(/\s+/).length > a.split(/\s+/).length ? b : a), "") : "";
  const longestWords = longest ? longest.split(/\s+/).length : 0;
  return { t, words, sentences, paras, noSp, uniq, avgLen, flesch, longest, longestWords, tokens };
}
function wc2Tiles(s) {
  $("wc-tiles").innerHTML = `
    <div class="wc-tile"><b>${s.words.toLocaleString()}</b><span>Words</span></div>
    <div class="wc-tile"><b>${s.t.length.toLocaleString()}</b><span>Characters</span></div>
    <div class="wc-tile"><b>${s.noSp.toLocaleString()}</b><span>No spaces</span></div>
    <div class="wc-tile"><b>${s.sentences.toLocaleString()}</b><span>Sentences</span></div>
    <div class="wc-tile"><b>${s.paras.toLocaleString()}</b><span>Paragraphs</span></div>
    <div class="wc-tile"><b>${s.uniq.toLocaleString()}</b><span>Unique words</span></div>
    <div class="wc-tile"><b>${s.avgLen}</b><span>Avg word length</span></div>
    <div class="wc-tile"><b>${wcDur(s.words, 230)}</b><span>Reading time</span></div>
    <div class="wc-tile"><b>${wcDur(s.words, 130)}</b><span>Speaking time</span></div>
    <div class="wc-tile"><b>${wcPages(s.words, 250)}</b><span>Pages \u00b7 Letter</span></div>`;
}
function wc2Keywords(s) {
  const el = $("wc-kw");
  if (!s.words) { el.innerHTML = '<p class="wc-empty">Start typing to see keyword density.</p>'; return; }
  const stop = $("wc-kw-stop").checked;
  const phrases = $("wc-kw-2w").checked;
  let units = s.tokens.filter(w => w.length >= 3 && (!stop || !WC_STOP.has(w)));
  if (phrases) {
    const raw = s.tokens;
    const ph = [];
    for (let i = 0; i < raw.length - 1; i++) {
      if (raw[i].length >= 3 && raw[i + 1].length >= 3 && (!stop || (!WC_STOP.has(raw[i]) && !WC_STOP.has(raw[i + 1])))) ph.push(raw[i] + " " + raw[i + 1]);
    }
    units = units.concat(ph);
  }
  const freq = new Map();
  for (const u of units) freq.set(u, (freq.get(u) || 0) + 1);
  const top = [...freq.entries()].sort((a, b) => b[1] - a[1]).slice(0, 10);
  if (!top.length) { el.innerHTML = '<p class="wc-empty">No keywords yet \u2014 keep typing.</p>'; return; }
  const max = top[0][1];
  el.innerHTML = top.map(([w, n]) => {
    const d = ((n / s.words) * 100).toFixed(1);
    const hot = d > 4 ? " hot" : "";
    return `<div class="wc-kw-row${hot}"><span class="wc-kw-word">${escHtml(w)}</span><span class="wc-kw-n">${n}\u00d7</span><span class="wc-kw-d">${d}%</span>${wc2Bar((n / max) * 100)}</div>`;
  }).join("");
}
function wc2Readability(s) {
  const r = wc2ReadLabel(s.flesch);
  const score = s.flesch === null ? "\u2014" : Math.round(s.flesch);
  $("wc-read").innerHTML = `
    <div class="wc-read-card ${r.cls}">
      <div class="wc-read-score">${score}</div>
      <div><b>${r.lab}</b><span>${r.note}</span></div>
    </div>
    <div class="wc-read-meta"><span>Flesch reading ease</span>${s.longestWords ? `<span>Longest sentence: <b>${s.longestWords} words</b></span>` : ""}</div>`;
}
function wc2Social(s) {
  const limits = [["SEO title", 60], ["Meta description", 160], ["X / Twitter post", 280], ["LinkedIn post", 3000], ["Instagram caption", 2200], ["SMS message", 160]];
  const n = s.t.length;
  $("wc-social").innerHTML = limits.map(([name, lim]) => {
    const pct = (n / lim) * 100;
    const cls = pct > 100 ? " over" : pct > 85 ? " near" : "";
    const left = lim - n;
    const txt = left >= 0 ? `${left.toLocaleString()} left` : `${(-left).toLocaleString()} over`;
    return `<div class="wc-soc-row"><span class="wc-soc-name">${name}</span><span class="wc-soc-n${cls.trim()}">${txt}</span>${wc2Bar(pct, cls.trim())}</div>`;
  }).join("");
}
function wordCount() {
  const t = $("wc-in").value;
  const s = wc2Stats(t);
  wc2Tiles(s); wc2Keywords(s); wc2Readability(s); wc2Social(s);
  if (!$("wc-table").innerHTML) wcRefTable();
}
function wc2Clear() { $("wc-in").value = ""; wordCount(); $("wc-in").focus(); }
function wc2Copy(btn) {
  const t = $("wc-in").value;
  if (!t) return;
  (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(() => {
    btn.textContent = "Copied!"; setTimeout(() => { btn.textContent = "Copy text"; }, 1200);
  }).catch(() => {});
}
function wc2Sample() {
  $("wc-in").value = "Content length is one of the quietest ranking factors in modern search. Articles that answer a question completely tend to earn links, keep readers on the page, and give search engines enough context to understand the topic. A good word counter does more than tally characters: it shows reading time, keyword density, and readability so writers can edit with confidence. Aim for clarity first. Short sentences, familiar words, and a logical structure will always beat a padded paragraph. When you finish a draft, check the platform limits below before you publish, because a perfect headline that gets cut off at sixty characters helps nobody.";
  wordCount();
}
if ($("wc-in")) wordCount();

function convertCase(mode) {
  const t = $("case-in").value;
  let r = t;
  if (mode === "upper") r = t.toUpperCase();
  if (mode === "lower") r = t.toLowerCase();
  if (mode === "title") r = t.toLowerCase().replace(/\b\w/g, (c) => c.toUpperCase());
  if (mode === "sentence") r = t.toLowerCase().replace(/(^\s*\w|[.!?]\s+\w)/g, (c) => c.toUpperCase());
  if (mode === "camel") r = t.toLowerCase().replace(/[^a-z0-9]+(.)/g, (_, c) => c.toUpperCase()).replace(/^(.)/, (c) => c.toLowerCase());
  if (mode === "snake") r = t.trim().toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_|_$/g, "");
  if (mode === "kebab") r = t.trim().toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
  $("case-in").value = r;
}

function dedupeLines() {
  const ci = $("dd-case").checked, trim = $("dd-trim").checked;
  const seen = new Set(), res = [];
  for (const raw of $("dd-in").value.split("\n")) {
    const line = trim ? raw.trim() : raw;
    const key = ci ? line.toLowerCase() : line;
    if (key === "" && line === "") { res.push(line); continue; }
    if (!seen.has(key)) { seen.add(key); res.push(line); }
  }
  out("dd-out", res.join("\n"), "mono");
}

function reverseText(mode) {
  const t = $("rev-in").value;
  let r = t;
  if (mode === "chars") r = [...t].reverse().join("");
  if (mode === "words") r = t.split(/\s+/).reverse().join(" ");
  if (mode === "lines") r = t.split("\n").reverse().join("\n");
  out("rev-out", r, "mono");
}

/* ---------- Developer ---------- */
let JF2_LAST = null, JF2_TEXT = "";
function jf2Parse(t) {
  try { return { ok: true, val: JSON.parse(t) }; }
  catch (e) { return { ok: false, err: e.message }; }
}
function jf2Pos(t, msg) {
  const m = msg.match(/position (\d+)/);
  if (!m) return "";
  const pos = +m[1];
  const before = t.slice(0, pos);
  const line = (before.match(/\n/g) || []).length + 1;
  const col = pos - before.lastIndexOf("\n");
  return ` at line ${line}, column ${col}`;
}
function jf2SortVal(v) {
  if (Array.isArray(v)) return v.map(jf2SortVal);
  if (v && typeof v === "object") {
    const o = {};
    for (const k of Object.keys(v).sort()) o[k] = jf2SortVal(v[k]);
    return o;
  }
  return v;
}
function jf2Hi(json) {
  return escHtml(json).replace(
    /("(\\u[a-fA-F0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false)\b|\bnull\b|-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)/g,
    (m) => {
      let cls = "jf-num";
      if (/^"/.test(m)) cls = /:$/.test(m) ? "jf-key" : "jf-str";
      else if (/true|false/.test(m)) cls = "jf-bool";
      else if (/null/.test(m)) cls = "jf-null";
      return `<span class="${cls}">${m}</span>`;
    }
  );
}
function jf2Depth(v) {
  if (Array.isArray(v)) return 1 + Math.max(0, ...v.map(jf2Depth));
  if (v && typeof v === "object") return 1 + Math.max(0, ...Object.values(v).map(jf2Depth));
  return 0;
}
function jf2Count(v, st) {
  st.nodes++;
  if (Array.isArray(v)) { st.arrays++; v.forEach(x => jf2Count(x, st)); }
  else if (v && typeof v === "object") { st.objects++; st.keys += Object.keys(v).length; Object.values(v).forEach(x => jf2Count(x, st)); }
}
function jf2Stats(val, raw) {
  const st = { nodes: 0, objects: 0, arrays: 0, keys: 0 };
  const depth = jf2Depth(val);
  jf2Count(val, st);
  const kb = (n) => n < 1024 ? n + " B" : (n / 1024).toFixed(1) + " KB";
  $("jf-stats").innerHTML = `
    <div class="jf-chip"><b>${kb(new Blob([raw]).size)}</b><span>Input size</span></div>
    <div class="jf-chip"><b>${kb(new Blob([JF2_TEXT]).size)}</b><span>Output size</span></div>
    <div class="jf-chip"><b>${st.keys.toLocaleString()}</b><span>Keys</span></div>
    <div class="jf-chip"><b>${st.objects.toLocaleString()}</b><span>Objects</span></div>
    <div class="jf-chip"><b>${st.arrays.toLocaleString()}</b><span>Arrays</span></div>
    <div class="jf-chip"><b>${depth}</b><span>Max depth</span></div>`;
}
function jf2TreeHtml(v, key) {
  const lbl = key === null ? "" : `<span class="jf-key">${escHtml(String(key))}</span>: `;
  if (v === null) return `<li>${lbl}<span class="jf-null">null</span></li>`;
  if (typeof v === "string") return `<li>${lbl}<span class="jf-str">"${escHtml(v)}"</span></li>`;
  if (typeof v === "number" || typeof v === "boolean") return `<li>${lbl}<span class="${typeof v === "number" ? "jf-num" : "jf-bool"}">${v}</span></li>`;
  const isArr = Array.isArray(v);
  const entries = isArr ? v.map((x, i) => [i, x]) : Object.entries(v);
  const items = entries.map(([k, x]) => jf2TreeHtml(x, isArr ? null : k)).join("");
  const badge = isArr ? `[${entries.length}]` : `{${entries.length}}`;
  return `<li><details open><summary>${lbl}<span class="jf-badge">${badge}</span></summary><ul>${items}</ul></details></li>`;
}
function jf2RenderOut() {
  if (JF2_LAST === null) return;
  const pretty = JSON.stringify(JF2_LAST, null, 2);
  $("json-out").innerHTML = jf2Hi(pretty);
  $("jf-tree").innerHTML = "<ul>" + jf2TreeHtml(JF2_LAST, null) + "</ul>";
}
function jf2Show(r, raw) {
  if (!r.ok) {
    $("json-err").innerHTML = `<b>Invalid JSON:</b> ${escHtml(r.err)}${jf2Pos(raw, r.err)}`;
    $("json-out").textContent = ""; $("jf-tree").innerHTML = ""; $("jf-stats").innerHTML = "";
    JF2_LAST = null; JF2_TEXT = "";
    return;
  }
  $("json-err").textContent = "";
  JF2_LAST = r.val;
  jf2RenderText();
  jf2Stats(r.val, raw);
  jf2RenderOut();
}
function jf2RenderText() {
  if (JF2_LAST === null) return;
  JF2_TEXT = JSON.stringify(JF2_LAST, null, 2);
}
function jf2Format(space) {
  const raw = $("json-in").value;
  if (!raw.trim()) { $("json-err").textContent = "Paste some JSON first."; return; }
  const r = jf2Parse(raw);
  if (!r.ok) { jf2Show(r, raw); return; }
  JF2_LAST = r.val;
  $("json-err").textContent = "";
  JF2_TEXT = JSON.stringify(r.val, null, space || 0);
  jf2Stats(r.val, raw);
  $("json-out").innerHTML = jf2Hi(JF2_TEXT);
  $("jf-tree").innerHTML = "<ul>" + jf2TreeHtml(r.val, null) + "</ul>";
}
function jf2Minify() {
  const raw = $("json-in").value;
  if (!raw.trim()) { $("json-err").textContent = "Paste some JSON first."; return; }
  const r = jf2Parse(raw);
  if (!r.ok) { jf2Show(r, raw); return; }
  JF2_LAST = r.val;
  $("json-err").textContent = "";
  JF2_TEXT = JSON.stringify(r.val);
  jf2Stats(r.val, raw);
  $("json-out").innerHTML = jf2Hi(JF2_TEXT);
  $("jf-tree").innerHTML = "<ul>" + jf2TreeHtml(r.val, null) + "</ul>";
}
function jf2Sort() {
  const raw = $("json-in").value;
  if (!raw.trim()) { $("json-err").textContent = "Paste some JSON first."; return; }
  const r = jf2Parse(raw);
  if (!r.ok) { jf2Show(r, raw); return; }
  const sorted = jf2SortVal(r.val);
  JF2_LAST = sorted;
  $("json-err").textContent = "";
  $("json-in").value = JSON.stringify(sorted, null, 2);
  JF2_TEXT = JSON.stringify(sorted, null, 2);
  jf2Stats(sorted, $("json-in").value);
  $("json-out").innerHTML = jf2Hi(JF2_TEXT);
  $("jf-tree").innerHTML = "<ul>" + jf2TreeHtml(sorted, null) + "</ul>";
}
function jf2Tab(which) {
  $("jf-tab-out").classList.toggle("active", which === "out");
  $("jf-tab-tree").classList.toggle("active", which === "tree");
  $("json-out").style.display = which === "out" ? "block" : "none";
  $("jf-tree").style.display = which === "tree" ? "block" : "none";
}
function jf2Live() {
  const raw = $("json-in").value;
  if (!raw.trim()) { $("json-err").textContent = ""; $("jf-stats").innerHTML = ""; return; }
  const r = jf2Parse(raw);
  if (!r.ok) return;
  $("json-err").textContent = "";
  JF2_LAST = r.val;
  jf2RenderText();
  jf2Stats(r.val, raw);
  jf2RenderOut();
}
function jf2Copy(btn) {
  if (!JF2_TEXT) return;
  (navigator.clipboard ? navigator.clipboard.writeText(JF2_TEXT) : Promise.reject()).then(() => {
    btn.textContent = "Copied!"; setTimeout(() => { btn.textContent = "Copy"; }, 1200);
  }).catch(() => {});
}
function jf2Download() {
  if (JF2_LAST === null) return;
  const blob = new Blob([JF2_TEXT || JSON.stringify(JF2_LAST, null, 2)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "formatted.json";
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000);
}
function jf2Clear() {
  $("json-in").value = ""; $("json-err").textContent = ""; $("json-out").textContent = "";
  $("jf-tree").innerHTML = ""; $("jf-stats").innerHTML = "";
  JF2_LAST = null; JF2_TEXT = "";
}
function jf2Sample() {
  $("json-in").value = JSON.stringify({ site: "MSCALE Tools", live: 176, categories: 12, tags: ["free", "no-signup", "browser-based"], featured: { name: "Password Generator Pro", modes: ["random", "memorable", "pin"], min_length: 4, max_length: 64, offline: true }, stats: { pages: 194, uptime: "99.9%", price: null } }, null, 2);
  jf2Format(2);
}
function jf2Paste() {
  if (navigator.clipboard && navigator.clipboard.readText) {
    navigator.clipboard.readText().then(t => { $("json-in").value = t; jf2Live(); }).catch(() => {});
  }
}
if ($("json-in")) jf2Live();

function b64(op) {
  const t = $("b64-in").value;
  try {
    if (op === "enc") out("b64-out", btoa(String.fromCharCode(...new TextEncoder().encode(t))), "mono");
    else out("b64-out", new TextDecoder().decode(Uint8Array.from(atob(t.trim()), (c) => c.charCodeAt(0))), "mono");
  } catch (e) { out("b64-out", "Error: invalid input for " + op, "error"); }
}

function urlEnc(op) {
  const t = $("url-in").value;
  try {
    out("url-out", op === "enc" ? encodeURIComponent(t) : decodeURIComponent(t.replace(/\+/g, " ")), "mono");
  } catch (e) { out("url-out", "Error: malformed URL encoding", "error"); }
}

function uuidGen() {
  const n = Math.min(parseInt($("uuid-n").value) || 1, 100);
  const list = Array.from({ length: n }, () => crypto.randomUUID());
  out("uuid-out", list.join("\n"), "mono");
}

/* ---------- Converters ---------- */
const UC2 = {
  length: { label: "Length", units: { "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344, "nmi": 1852 } },
  weight: { label: "Weight", units: { "mg": 1e-6, "g": 0.001, "kg": 1, "t": 1000, "oz": 0.028349523125, "lb": 0.45359237, "st": 6.35029318 } },
  temp: { label: "Temperature", units: { "\u00b0C": 1, "\u00b0F": 1, "K": 1 } },
  data: { label: "Data size", units: { "B": 1, "KB": 1024, "MB": 1048576, "GB": 1073741824, "TB": 1099511627776 } },
  area: { label: "Area", units: { "cm\u00b2": 0.0001, "m\u00b2": 1, "ha": 10000, "km\u00b2": 1e6, "in\u00b2": 0.00064516, "ft\u00b2": 0.09290304, "acre": 4046.8564224, "mi\u00b2": 2589988.110336 } },
  volume: { label: "Volume", units: { "ml": 0.001, "l": 1, "m\u00b3": 1000, "tsp": 0.00492892159375, "tbsp": 0.01478676478125, "fl oz": 0.0295735295625, "cup": 0.2365882365, "pint": 0.473176473, "quart": 0.946352946, "gallon": 3.785411784 } },
  speed: { label: "Speed", units: { "m/s": 1, "km/h": 0.277777778, "mph": 0.44704, "kn": 0.514444444, "ft/s": 0.3048 } },
  time: { label: "Time", units: { "ms": 0.001, "s": 1, "min": 60, "h": 3600, "day": 86400, "week": 604800, "month": 2629746, "year": 31556952 } },
};
let UC2_CAT = "length";
function uc2ToBase(cat, v, u) {
  if (cat === "temp") {
    if (u === "\u00b0C") return v;
    if (u === "\u00b0F") return (v - 32) * 5 / 9;
    return v - 273.15;
  }
  return v * UC2[cat].units[u];
}
function uc2FromBase(cat, c, u) {
  if (cat === "temp") {
    if (u === "\u00b0C") return c;
    if (u === "\u00b0F") return c * 9 / 5 + 32;
    return c + 273.15;
  }
  return c / UC2[cat].units[u];
}
function uc2Fmt(n) {
  if (!isFinite(n)) return "\u2014";
  const a = Math.abs(n);
  if (a !== 0 && (a < 1e-6 || a >= 1e12)) return n.toExponential(6);
  return (+n.toPrecision(10)).toLocaleString(undefined, { maximumFractionDigits: 8 });
}
function uc2Cats() {
  $("uc2-cats").innerHTML = Object.keys(UC2).map(k =>
    `<button class="uc2-cat${k === UC2_CAT ? " active" : ""}" onclick="uc2SetCat('${k}')">${UC2[k].label}</button>`).join("");
}
function uc2SetCat(k) { UC2_CAT = k; uc2Cats(); uc2Fill(); uc2Run(); }
function uc2Fill() {
  const keys = Object.keys(UC2[UC2_CAT].units);
  const cur = [$("uc2-from").value, $("uc2-to").value];
  $("uc2-from").innerHTML = keys.map(u => `<option>${u}</option>`).join("");
  $("uc2-to").innerHTML = keys.map(u => `<option>${u}</option>`).join("");
  const defFrom = keys.includes(cur[0]) ? cur[0] : keys[Math.min(2, keys.length - 1)];
  let defTo = keys.includes(cur[1]) ? cur[1] : keys[Math.min(3, keys.length - 1)];
  if (defTo === defFrom) defTo = keys[(keys.indexOf(defFrom) + 1) % keys.length];
  $("uc2-from").value = defFrom;
  $("uc2-to").value = defTo;
}
function uc2Swap() {
  const f = $("uc2-from").value;
  $("uc2-from").value = $("uc2-to").value;
  $("uc2-to").value = f;
  uc2Run();
}
function uc2Convert(v, from, to) {
  const c = uc2ToBase(UC2_CAT, v, from);
  return uc2FromBase(UC2_CAT, c, to);
}
function uc2Run() {
  const v = parseFloat($("uc2-val").value);
  const from = $("uc2-from").value, to = $("uc2-to").value;
  if (isNaN(v)) { $("uc2-big").innerHTML = "\u2014"; $("uc2-table").innerHTML = ""; return; }
  const r = uc2Convert(v, from, to);
  $("uc2-big").innerHTML = `${uc2Fmt(v)} ${escHtml(from)} = <b>${uc2Fmt(r)}</b> ${escHtml(to)}`;
  const keys = Object.keys(UC2[UC2_CAT].units).filter(u => u !== from);
  $("uc2-table").innerHTML = `<table class="wc-table"><thead><tr><th>Unit</th><th>Value</th></tr></thead><tbody>` +
    keys.map(u => `<tr><td>${escHtml(u)}</td><td><b>${uc2Fmt(uc2Convert(v, from, u))}</b></td></tr>`).join("") +
    `</tbody></table>`;
}
if ($("uc2-val")) { uc2Cats(); uc2Fill(); uc2Run(); }

function tsToDate() {
  const v = $("ts-in").value.trim();
  if (!v) return;
  const ms = v.length > 10 ? parseInt(v) : parseInt(v) * 1000;
  const d = new Date(ms);
  out("ts-out", isNaN(d) ? "Invalid timestamp" :
    d.toISOString() + `<br><small>Local: ${d.toString()}</small>`);
}
function dateToTs() {
  const d = new Date($("ts-date").value);
  if (isNaN(d)) return;
  out("ts-out2", `Seconds: <b>${Math.floor(d.getTime() / 1000)}</b><br>Milliseconds: <b>${d.getTime()}</b>`);
}
setInterval(() => {
  const n = $("ts-now");
  if (n) n.textContent = Math.floor(Date.now() / 1000);
}, 1000);

/* ---------- Security ---------- */
var PG_MODE = "random";
var PG_WORDS = ("able acid aged also area army away baby back ball band bank base bath bear beat been beer bell belt best bird blow blue boat body bomb bond bone book boom boot born boss both bowl bulk burn bush busy calm came camp card care case cash cast cell chat chef chip city club coal coast coat code cold come cook cool cope copy core cost crew crop dark data date dawn days dead deal dear dean debt deep deny desk dial dice diet disc disk does done door dose down draw drew drop drug drum dual duck duke dust duty each earn ease east easy edge edit else even ever exit face fact fail fair fall farm fast fate fear feed feel feet fell felt file fill film find fine fire firm fish fist five flat flow foam fold folk food foot ford fork form fort four free frog from fuel full fund gain game gate gave gear gift girl give glad glow goal goat goes gold gone good gray grew grey grow gulf hair half hall hand hang hard harm hate have head hear heat held hell help here hero high hill hint hire hold hole holy home hope horn host hour huge hunt hurt idea inch into iron item join jump just keen keep kept kick kind king knee knew know lack lady laid lake land lane last late lawn lazy lead leaf lean left less life lift like limb lime line link list live load loan lock loft logo long look lord lose loss lost loud love luck made mail main make male mall many mark mask mass mate math meal mean meat meet melt memo menu mere mess mild mile milk mill mind mine miss mist mode mood more most move much must myth nail name navy near neat neck need neon nest news next nice nine node none norm nose note noun oath obey odds okay once only onto open oral ours oven over pace pack page paid pain pair palm park part pass past path peak peel peer pier pile pilot pine pink pipe plan play plot plug plus poem poet pole poll pool poor port pose post pour pray prey prop pull pump pure push quit quiz race rack raft rage raid rail rain rank rare rate read real rear reed reef rely rent rest rice rich ride ring rise risk road roar robe rock role roll roof room root rope rose ruby rude ruin rule rush rust safe sage said sail sake sale salt same sand save scan seal seat seed seek seem seen self sell send sent shed ship shoe shop shot show shut side sigh sign silk sing sink site size skin skip slam slap sled slid slim slip slot slow snap snow soap soar sock soda sofa soft soil sold sole solo some song soon sort soul soup sour spin spot spun star stay stem step stew stir stop stow such suit sung sunk sure surf swap swim tail take tale talk tall tank tape task taxi team tear tech tell tend tent term test text than that thaw thee them then they thin this thus tick tide tidy tied tier tile till tilt time tiny tire toad toll tomb tone tool torn toss tour town trap tray tree trek trim trip true tube tune turn twin type ugly undo unit upon urge used user vain vane vary vase vast veil vein verb very vest veto vibe view vine visa void vote wage wait wake walk wall wand want ward warm warn wash wasp wave weak wear weed week weep well went were west what when whom wide wife wild will wind wine wing wipe wire wise wish with wolf wood wool word wore work worm worn wrap yard yarn yawn year yell your zeal zero zone").split(" ");
function pgChars() {
  var c = "";
  if ($("pg-lower").checked) c += "abcdefghijklmnopqrstuvwxyz";
  if ($("pg-upper").checked) c += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  if ($("pg-digits").checked) c += "0123456789";
  if ($("pg-symbols").checked) c += "!@#$%^&*()-_=+[]{};:,.<>?";
  if ($("pg-ambig").checked) c = c.replace(/[il1LoO0]/g, "");
  return c;
}
function pgRand(len, chars) {
  var a = new Uint32Array(len);
  crypto.getRandomValues(a);
  return Array.prototype.map.call(a, function (n) { return chars[n % chars.length]; }).join("");
}
function pgBuild() {
  var len = parseInt($("pg-len").value) || 16;
  if (PG_MODE === "pin") return pgRand(Math.min(len, 12), "0123456789");
  if (PG_MODE === "memorable") {
    var n = Math.max(3, Math.min(8, Math.round(len / 4)));
    var a = new Uint32Array(n);
    crypto.getRandomValues(a);
    return Array.prototype.map.call(a, function (i) { return PG_WORDS[i % PG_WORDS.length]; }).join("-");
  }
  var chars = pgChars();
  if (!chars) return null;
  return pgRand(len, chars);
}
function pgEntropy(pw) {
  if (PG_MODE === "pin") return pw.length * Math.log2(10);
  if (PG_MODE === "memorable") return (pw.split("-").length) * Math.log2(PG_WORDS.length);
  return pw.length * Math.log2(Math.max(pgChars().length, 2));
}
function pgCrackText(entropy) {
  var sec = Math.pow(2, entropy) / 2 / 1e11;
  if (sec < 1) return "instantly";
  if (sec < 3600) return Math.round(sec) + " seconds";
  if (sec < 86400) return Math.round(sec / 3600) + " hours";
  if (sec < 31557600) return Math.round(sec / 86400) + " days";
  var y = sec / 31557600;
  if (y < 1e3) return Math.round(y) + " years";
  if (y < 1e6) return nfmt(y / 1e3, 0) + " thousand years";
  if (y < 1e9) return nfmt(y / 1e6, 0) + " million years";
  if (y < 1e12) return nfmt(y / 1e9, 0) + " billion years";
  return "longer than the age of the universe";
}
function pgShow(pw) {
  $("pg-out").textContent = pw;
  var e = pgEntropy(pw);
  var fill = $("pg-fill");
  fill.style.width = Math.min(100, (e / 128) * 100) + "%";
  var cls = e > 100 ? "vs" : e > 75 ? "s" : e > 50 ? "g" : e > 30 ? "f" : "w";
  fill.className = "pg-fill " + cls;
  $("pg-label").textContent = e > 100 ? "Very strong" : e > 75 ? "Strong" : e > 50 ? "Good" : e > 30 ? "Fair" : "Weak";
  $("pg-entropy").textContent = Math.round(e) + " bits of entropy";
  $("pg-crack").textContent = "Estimated offline crack time at 100 billion guesses/sec: " + pgCrackText(e);
}
function pgGen() {
  var pw = pgBuild();
  if (pw === null) { $("pg-out").textContent = "Select at least one character set"; return; }
  pgShow(pw);
}
function pgMode(m) {
  PG_MODE = m;
  var tabs = document.querySelectorAll(".pg-tab");
  for (var i = 0; i < tabs.length; i++) tabs[i].classList.toggle("active", tabs[i].getAttribute("data-mode") === m);
  var t = document.getElementById("pg-toggles");
  if (t) t.classList.toggle("pg-off", m !== "random");
  pgGen();
}
function pgSlider() { $("pg-len-val").textContent = $("pg-len").value; pgGen(); }
function pgCopy() {
  var btn = $("pg-copy");
  navigator.clipboard.writeText($("pg-out").textContent).then(function () {
    btn.textContent = "Copied!";
    setTimeout(function () { btn.textContent = "Copy"; }, 1200);
  });
}
function pgMulti() {
  var rows = "";
  for (var i = 0; i < 5; i++) {
    var pw = pgBuild();
    rows += "<div class='pg-row'><span class='mono'>" + pw + "</span><button class='btn btn-sm' onclick='pgCopyVal(this)'>Copy</button></div>";
  }
  $("pg-multi").innerHTML = rows;
}
function pgCopyVal(btn) {
  navigator.clipboard.writeText(btn.parentNode.querySelector("span").textContent);
  btn.textContent = "Copied!";
  setTimeout(function () { btn.textContent = "Copy"; }, 1200);
}
if ($("pg-out")) pgGen();

/* ---------- Color ---------- *//* ---------- Color ---------- */
function hexToRgb(hex) {
  const m = hex.replace("#", "").match(/^([0-9a-f]{3}|[0-9a-f]{6})$/i);
  if (!m) return null;
  let h = m[1];
  if (h.length === 3) h = [...h].map((c) => c + c).join("");
  return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)];
}
function rgbToHsl(r, g, b) {
  r /= 255; g /= 255; b /= 255;
  const max = Math.max(r, g, b), min = Math.min(r, g, b);
  let h = 0, s = 0, l = (max + min) / 2;
  if (max !== min) {
    const d = max - min;
    s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
    if (max === r) h = ((g - b) / d + (g < b ? 6 : 0)) / 6;
    else if (max === g) h = ((b - r) / d + 2) / 6;
    else h = ((r - g) / d + 4) / 6;
  }
  return [Math.round(h * 360), Math.round(s * 100), Math.round(l * 100)];
}
function colorConvert() {
  const rgb = hexToRgb($("col-in").value.trim());
  if (!rgb) { $("col-err").textContent = "Enter a valid hex color like #34d399"; return; }
  $("col-err").textContent = "";
  const [h, s, l] = rgbToHsl(...rgb);
  $("col-out").innerHTML = `HEX: <b>${$("col-in").value.trim()}</b><br>RGB: <b>rgb(${rgb.join(", ")})</b><br>HSL: <b>hsl(${h}, ${s}%, ${l}%)</b>`;
  $("col-swatch").style.background = `rgb(${rgb.join(",")})`;
}

/* ---------- Random ---------- */
function randNums() {
  const min = parseInt($("rn-min").value), max = parseInt($("rn-max").value);
  const count = Math.min(parseInt($("rn-count").value) || 1, 1000);
  const unique = $("rn-unique").checked;
  if (isNaN(min) || isNaN(max) || max < min) { out("rn-out", "Invalid range", "error"); return; }
  if (unique && max - min + 1 < count) { out("rn-out", "Range too small for unique values", "error"); return; }
  const set = new Set(), res = [];
  while (res.length < count) {
    const v = Math.floor(Math.random() * (max - min + 1)) + min;
    if (!unique || !set.has(v)) { if (unique) set.add(v); res.push(v); }
  }
  out("rn-out", res.join(", "));
}

function flipCoin() {
  const n = Math.min(parseInt($("coin-n").value) || 1, 1000);
  const flips = Array.from({ length: n }, () => (Math.random() < 0.5 ? "Heads" : "Tails"));
  const heads = flips.filter((f) => f === "Heads").length;
  out("coin-out", n === 1 ? flips[0] : `Heads: ${heads} · Tails: ${n - heads}<br><small>${flips.slice(0, 50).join(", ")}${n > 50 ? " …" : ""}</small>`);
}

function rollDice() {
  const count = Math.min(parseInt($("dice-n").value) || 1, 20);
  const sides = parseInt($("dice-sides").value) || 6;
  const rolls = Array.from({ length: count }, () => 1 + Math.floor(Math.random() * sides));
  out("dice-out", `You rolled: <b>${rolls.join(", ")}</b>${count > 1 ? ` — total <b>${rolls.reduce((a, b) => a + b)}</b>` : ""}`);
}

/* ---------- shared helpers ---------- */
function escHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
function toHexStr(r, g, b) {
  return "#" + [r, g, b].map((v) => Math.max(0, Math.min(255, Math.round(v))).toString(16).padStart(2, "0")).join("").toUpperCase();
}

/* ---------- Calculators ---------- */
function discountCalc() {
  const price = parseFloat($("disc-p").value), off = parseFloat($("disc-off").value);
  const tax = parseFloat($("disc-tax").value) || 0;
  if (isNaN(price) || isNaN(off)) return;
  const saved = price * off / 100;
  const after = price - saved;
  const final = after * (1 + tax / 100);
  out("disc-out", `You save: <b>${saved.toFixed(2)}</b><br>Price after discount: <b>${after.toFixed(2)}</b>${tax ? `<br>After ${tax}% tax: <b>${final.toFixed(2)}</b>` : ""}`);
}

function tipCalc() {
  const bill = parseFloat($("tip-bill").value), pct = parseFloat($("tip-pct").value);
  const people = parseInt($("tip-people").value) || 1;
  if (isNaN(bill) || isNaN(pct)) return;
  const tip = bill * pct / 100;
  const total = bill + tip;
  out("tip-out", `Tip: <b>${tip.toFixed(2)}</b><br>Total: <b>${total.toFixed(2)}</b>${people > 1 ? `<br>Per person (${people}): <b>${(total / people).toFixed(2)}</b>` : ""}`);
}

function compoundCalc() {
  const P = parseFloat($("ci-p").value), r = parseFloat($("ci-r").value) / 100;
  const t = parseFloat($("ci-t").value), n = parseInt($("ci-n").value);
  const monthly = parseFloat($("ci-monthly").value) || 0;
  if (isNaN(P) || isNaN(r) || isNaN(t) || !n) return;
  const periodRate = r / n;
  const periods = Math.round(t * n);
  const contribPerPeriod = monthly * (n / 12);
  let bal = P, contributed = P;
  for (let i = 0; i < periods; i++) { bal = bal * (1 + periodRate) + contribPerPeriod; contributed += contribPerPeriod; }
  out("ci-out", `Future value: <b>${bal.toFixed(2)}</b><br>Total contributed: <b>${contributed.toFixed(2)}</b><br>Interest earned: <b>${(bal - contributed).toFixed(2)}</b>`);
}

function taxCalc(mode) {
  const amt = parseFloat($("tax-amt").value), rate = parseFloat($("tax-rate").value);
  if (isNaN(amt) || isNaN(rate)) return;
  if (mode === "add") {
    const tax = amt * rate / 100;
    out("tax-out", `Tax amount: <b>${tax.toFixed(2)}</b><br>Gross total: <b>${(amt + tax).toFixed(2)}</b>`);
  } else {
    const net = amt / (1 + rate / 100);
    out("tax-out", `Net (before tax): <b>${net.toFixed(2)}</b><br>Tax included: <b>${(amt - net).toFixed(2)}</b>`);
  }
}

/* ---------- Text ---------- */
function findReplace() {
  const text = $("fr-in").value, find = $("fr-find").value;
  if (!find) return;
  const repl = $("fr-repl").value;
  const flags = ($("fr-case").checked ? "" : "i") + "g";
  let re;
  try { re = new RegExp($("fr-regex").checked ? find : find.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), flags); }
  catch (e) { return out("fr-out", "Invalid regex: " + e.message, "error"); }
  const count = (text.match(re) || []).length;
  out("fr-out", text.replace(re, repl), "mono");
  $("fr-count").textContent = count + " replacement(s)";
}

function sortLines(mode) {
  const lines = $("sort-in").value.split("\n");
  if (mode === "az") lines.sort((a, b) => a.localeCompare(b));
  if (mode === "za") lines.sort((a, b) => b.localeCompare(a));
  if (mode === "len") lines.sort((a, b) => a.length - b.length);
  if (mode === "len2") lines.sort((a, b) => b.length - a.length);
  if (mode === "shuffle") { for (let i = lines.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [lines[i], lines[j]] = [lines[j], lines[i]]; } }
  $("sort-in").value = lines.join("\n");
}

const LOREM_WORDS = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure in reprehenderit voluptate velit esse cillum eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt culpa qui officia deserunt mollit anim id est laborum".split(" ");
let LR2_TYPE = "paras";
function lr2Type(t, btn) {
  LR2_TYPE = t;
  ["paras", "sents", "words", "lists"].forEach(k => $("lr2-t-" + k).classList.toggle("active", k === t));
  const nLabel = $("lr2-n-label"), sWrap = $("lr2-s-wrap");
  if (t === "paras") { nLabel.textContent = "Paragraphs"; sWrap.style.display = "block"; $("lr2-start-wrap").style.display = "block"; }
  else if (t === "sents") { nLabel.textContent = "Sentences"; sWrap.style.display = "none"; $("lr2-start-wrap").style.display = "block"; }
  else if (t === "words") { nLabel.textContent = "Words"; sWrap.style.display = "none"; $("lr2-start-wrap").style.display = "none"; }
  else { nLabel.textContent = "List items"; sWrap.style.display = "none"; $("lr2-start-wrap").style.display = "none"; }
  lr2Gen();
}
function lr2Sentence(minW, maxW) {
  const len = minW + Math.floor(Math.random() * (maxW - minW + 1));
  const words = Array.from({ length: len }, () => LOREM_WORDS[Math.floor(Math.random() * LOREM_WORDS.length)]);
  return words[0][0].toUpperCase() + words[0].slice(1) + " " + words.slice(1).join(" ") + ".";
}
function lr2Paragraph(sents, startClassic) {
  const s = [];
  for (let i = 0; i < sents; i++) s.push(lr2Sentence(6, 17));
  let p = s.join(" ");
  if (startClassic) p = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " + p;
  return p;
}
function lr2Text() {
  const n = Math.min(parseInt($("lorem-n").value) || 3, 50);
  const sents = Math.min(parseInt($("lorem-s").value) || 4, 30);
  const classic = $("lr2-start") && $("lr2-start").checked;
  if (LR2_TYPE === "paras") {
    const arr = [];
    for (let p = 0; p < n; p++) arr.push(lr2Paragraph(sents, classic && p === 0));
    return arr.join("\n\n");
  }
  if (LR2_TYPE === "sents") {
    const arr = [];
    for (let i = 0; i < n; i++) arr.push(classic && i === 0 ? "Lorem ipsum dolor sit amet, consectetur adipiscing elit." : lr2Sentence(6, 17));
    return arr.join(" ");
  }
  if (LR2_TYPE === "words") {
    const arr = [];
    for (let i = 0; i < n; i++) arr.push(LOREM_WORDS[Math.floor(Math.random() * LOREM_WORDS.length)]);
    return arr.join(" ").replace(/^\w/, c => c.toUpperCase()) + ".";
  }
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(lr2Sentence(4, 10).replace(/\.$/, ""));
  return arr;
}
function lr2Stats(text) {
  const words = text.trim().split(/\s+/).length;
  const chars = text.length;
  $("lr2-stats").innerHTML = `
    <div class="jf-chip"><b>${words.toLocaleString()}</b><span>words</span></div>
    <div class="jf-chip"><b>${chars.toLocaleString()}</b><span>characters</span></div>
    <div class="jf-chip"><b>${lr2Kb(new Blob([text]).size)}</b><span>size</span></div>`;
}
function lr2Kb(n) { return n < 1024 ? n + " B" : (n / 1024).toFixed(1) + " KB"; }
function lr2Html() {
  const t = lr2Text();
  if (LR2_TYPE === "paras") return t.split("\n\n").map(p => "<p>" + escHtml(p) + "</p>").join("\n");
  if (LR2_TYPE === "lists") return "<ul>\n" + t.map(li => "  <li>" + escHtml(li) + "</li>").join("\n") + "\n</ul>";
  return "<p>" + escHtml(Array.isArray(t) ? t.join(" ") : t) + "</p>";
}
function lr2Gen() {
  const t = lr2Text();
  const text = Array.isArray(t) ? t.join("\n") : t;
  $("lorem-out").textContent = text;
  lr2Stats(text);
}
function lr2Live() { clearTimeout(LR2_TIMER); LR2_TIMER = setTimeout(lr2Gen, 300); }
let LR2_TIMER = null;
function lr2Copy(btn) {
  const t = $("lorem-out").textContent;
  if (!t) return;
  (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(() => {
    btn.textContent = "Copied!"; setTimeout(() => { btn.textContent = "Copy text"; }, 1200);
  }).catch(() => {});
}
function lr2CopyHtml(btn) {
  const h = lr2Html();
  (navigator.clipboard ? navigator.clipboard.writeText(h) : Promise.reject()).then(() => {
    btn.textContent = "HTML copied!"; setTimeout(() => { btn.textContent = "Copy HTML"; }, 1200);
  }).catch(() => {});
}
function lr2Download() {
  const t = $("lorem-out").textContent;
  if (!t) return;
  const blob = new Blob([t], { type: "text/plain" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "lorem-ipsum.txt";
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000);
}
if ($("lorem-out")) lr2Gen();

function wordFreq() {
  const stop = new Set("the a an and or but of to in on at for with by from as is are was were be been being it its this that these those i you he she they we not no do does did have has had will would can could should may might must about into over after".split(" "));
  const words = ($("wf-in").value.toLowerCase().match(/[a-zà-ÿ0-9']+/g) || []).filter((w) => w.length > 1 && !stop.has(w));
  const freq = {};
  for (const w of words) freq[w] = (freq[w] || 0) + 1;
  const top = Object.entries(freq).sort((a, b) => b[1] - a[1]).slice(0, 25);
  const max = top.length ? top[0][1] : 1;
  $("wf-out").innerHTML = top.map(([w, c]) =>
    `<div class="wf-row"><span class="wf-word">${w}</span><span class="wf-bar" style="width:${Math.round(c / max * 100)}%"></span><b>${c}</b></div>`).join("") || "Paste text to analyze";
  $("wf-total").textContent = `${words.length} words analyzed (${Object.keys(freq).length} unique)`;
}

/* ---------- Developer ---------- */
async function hashGen() {
  const t = $("hash-in").value;
  if (!t) return;
  const data = new TextEncoder().encode(t);
  let html = "";
  for (const a of ["SHA-1", "SHA-256", "SHA-512"]) {
    const d = await crypto.subtle.digest(a, data);
    const hex = [...new Uint8Array(d)].map((b) => b.toString(16).padStart(2, "0")).join("");
    html += `<b>${a}</b><br>${hex}<br><br>`;
  }
  out("hash-out", html, "mono");
}

function jwtDecode() {
  const parts = $("jwt-in").value.trim().split(".");
  if (parts.length < 2) return out("jwt-out", "Not a valid JWT (expected header.payload.signature)", "error");
  const dec = (s) => { s = s.replace(/-/g, "+").replace(/_/g, "/"); while (s.length % 4) s += "="; return new TextDecoder().decode(Uint8Array.from(atob(s), (c) => c.charCodeAt(0))); };
  try {
    const h = JSON.stringify(JSON.parse(dec(parts[0])), null, 2);
    const p = JSON.stringify(JSON.parse(dec(parts[1])), null, 2);
    let extra = "";
    if (p.exp) {
      const e = new Date(p.exp * 1000);
      extra = `<br><br>Expires: ${e.toLocaleString()} ${e < new Date() ? "— <b style='color:var(--err)'>EXPIRED</b>" : "— still valid"}`;
    }
    out("jwt-out", `<b>HEADER</b>\n${h}\n\n<b>PAYLOAD</b>\n${p}${extra}`, "mono");
  } catch (e) { out("jwt-out", "Invalid JWT: " + e.message, "error"); }
}

function regexTest() {
  const text = $("re-text").value;
  try {
    const re = new RegExp($("re-pattern").value, $("re-flags").value || "g");
    const matches = [...text.matchAll(re)];
    $("re-count").textContent = matches.length + " match(es)";
    let html = "";
    let last = 0;
    for (const m of matches) {
      if (m.index > last) html += escHtml(text.slice(last, m.index));
      html += "<mark>" + escHtml(m[0]) + "</mark>";
      last = m.index + m[0].length;
      if (m[0] === "") { if (last < text.length) html += escHtml(text[last]); last++; if (last > text.length) break; }
    }
    html += escHtml(text.slice(last));
    out("re-out", html || "(empty)");
    out("re-groups", matches.slice(0, 25).map((m, i) =>
      `#${i + 1}: ${JSON.stringify(m[0])}${m.length > 1 ? "  groups: " + m.slice(1).map((g) => JSON.stringify(g)).join(", ") : ""}`).join("\n"), "mono");
  } catch (e) {
    $("re-count").textContent = "Invalid regex: " + e.message;
    $("re-out").textContent = "";
    $("re-groups").textContent = "";
  }
}

function csvParseRows(text, delim) {
  const rows = []; let row = []; let cur = ""; let inQ = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (inQ) {
      if (c === '"') { if (text[i + 1] === '"') { cur += '"'; i++; } else inQ = false; }
      else cur += c;
    } else if (c === '"') inQ = true;
    else if (c === delim) { row.push(cur); cur = ""; }
    else if (c === "\n") { row.push(cur); rows.push(row); row = []; cur = ""; }
    else if (c !== "\r") cur += c;
  }
  if (cur !== "" || row.length) { row.push(cur); rows.push(row); }
  return rows;
}
function csvToJson() {
  const delim = $("csv-delim").value === "tab" ? "\t" : $("csv-delim").value;
  const rows = csvParseRows($("csv-in").value.trim(), delim);
  if (!rows.length) return out("csv-out", "No data", "error");
  const headers = rows[0].map((h, i) => h.trim() || "column_" + (i + 1));
  const rows2 = rows.slice(1).filter((r) => r.some((c) => c !== "")).map((r) => Object.fromEntries(headers.map((h, i) => [h, r[i] ?? ""])));
  out("csv-out", JSON.stringify(rows2, null, 2), "mono");
  $("csv-count").textContent = rows2.length + " row(s) converted";
}

function htmlEnc(op) {
  const t = $("henc-in").value;
  if (op === "enc") out("henc-out", t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;"), "mono");
  else { const d = document.createElement("div"); d.innerHTML = t; out("henc-out", d.textContent, "mono"); }
}

/* ---------- Converters ---------- */
function baseConvert() {
  const v = $("nb-in").value.trim(), from = parseInt($("nb-from").value);
  const n = parseInt(v, from);
  if (isNaN(n) || !/^[0-9a-fA-F]+$/.test(v)) return out("nb-out", "Invalid number for base " + from, "error");
  out("nb-out", `Binary: <b>${n.toString(2)}</b><br>Octal: <b>${n.toString(8)}</b><br>Decimal: <b>${n.toString(10)}</b><br>Hex: <b>${n.toString(16).toUpperCase()}</b>`);
}

function romanToArabic(s) {
  const map = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
  let total = 0;
  s = s.toUpperCase();
  for (let i = 0; i < s.length; i++) {
    const v = map[s[i]];
    if (!v) return NaN;
    if (i + 1 < s.length && map[s[i + 1]] > v) total -= v; else total += v;
  }
  return total;
}
function arabicToRoman(n) {
  const table = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]];
  let r = "";
  for (const [v, s] of table) while (n >= v) { r += s; n -= v; }
  return r;
}
function romanConvert(mode) {
  if (mode === "to") {
    const n = parseInt($("roman-in").value);
    if (!n || n < 1 || n > 3999) return out("roman-out", "Enter a number from 1 to 3999", "error");
    out("roman-out", `${n} = <b>${arabicToRoman(n)}</b>`);
  } else {
    const v = romanToArabic($("roman-in").value.trim());
    if (isNaN(v)) return out("roman-out", "Invalid Roman numeral", "error");
    out("roman-out", `${$("roman-in").value.trim().toUpperCase()} = <b>${v}</b>`);
  }
}

/* ---------- Image ---------- */
let IR2_IMG = null, IR2_ORIG_SIZE = 0, IR2_ORIG_NAME = "image";
function ir2Kb(n) { return n < 1024 ? n + " B" : n < 1048576 ? (n / 1024).toFixed(1) + " KB" : (n / 1048576).toFixed(2) + " MB"; }
function ir2Load() {
  const file = ($("ir2-file") || {}).files && $("ir2-file").files[0];
  if (!file) return;
  IR2_ORIG_SIZE = file.size;
  IR2_ORIG_NAME = (file.name || "image").replace(/\.[^.]+$/, "");
  const img = new Image();
  img.onload = () => {
    IR2_IMG = img;
    $("ir2-w").value = img.width;
    $("ir2-h").value = img.height;
    $("ir2-before").src = img.src;
    $("ir2-meta-a").textContent = `${img.width}\u00d7${img.height} \u00b7 ${ir2Kb(file.size)}`;
    $("ir2-controls").style.display = "block";
    ir2Apply();
  };
  img.src = URL.createObjectURL(file);
}
function ir2Scale(p) {
  if (!IR2_IMG) return;
  $("ir2-lock").checked = true;
  $("ir2-w").value = Math.max(1, Math.round(IR2_IMG.width * p / 100));
  $("ir2-h").value = Math.max(1, Math.round(IR2_IMG.height * p / 100));
  ir2Apply();
}
function ir2Fit(w, h) {
  if (!IR2_IMG) return;
  $("ir2-lock").checked = false;
  $("ir2-w").value = w;
  $("ir2-h").value = h;
  ir2Apply();
}
function ir2OnW() {
  if (!IR2_IMG) return;
  const w = parseInt($("ir2-w").value);
  if ($("ir2-lock").checked && w > 0) $("ir2-h").value = Math.max(1, Math.round(w * IR2_IMG.height / IR2_IMG.width));
  ir2Apply();
}
function ir2OnH() {
  if (!IR2_IMG) return;
  const h = parseInt($("ir2-h").value);
  if ($("ir2-lock").checked && h > 0) $("ir2-w").value = Math.max(1, Math.round(h * IR2_IMG.width / IR2_IMG.height));
  ir2Apply();
}
function ir2Q() { $("ir2-qv").textContent = $("ir2-q").value; ir2Apply(); }
function ir2Apply() {
  if (!IR2_IMG) return;
  const w = parseInt($("ir2-w").value), h = parseInt($("ir2-h").value);
  if (!w || !h || w < 1 || h < 1) return;
  const fmt = $("ir2-fmt").value;
  const q = parseInt($("ir2-q").value) / 100;
  const canvas = document.createElement("canvas");
  canvas.width = w; canvas.height = h;
  const ctx = canvas.getContext("2d");
  if (fmt === "jpeg") { ctx.fillStyle = "#ffffff"; ctx.fillRect(0, 0, w, h); }
  ctx.drawImage(IR2_IMG, 0, 0, w, h);
  const url = canvas.toDataURL("image/" + fmt, q);
  const prev = $("ir2-preview");
  prev.src = url;
  const bytes = Math.round((url.length - "data:image/png;base64,".length) * 3 / 4);
  const saved = IR2_ORIG_SIZE ? Math.max(0, Math.round((1 - bytes / IR2_ORIG_SIZE) * 100)) : 0;
  $("ir2-meta-b").textContent = `${w}\u00d7${h} \u00b7 ~${ir2Kb(bytes)}` + (saved > 0 ? ` \u00b7 ${saved}% smaller` : "");
  const link = $("ir2-download");
  link.href = url;
  link.download = IR2_ORIG_NAME + "-" + w + "x" + h + "." + (fmt === "jpeg" ? "jpg" : fmt);
  link.style.display = "inline-block";
}
(function () {
  const drop = $("ir2-drop");
  if (!drop) return;
  ["dragover", "dragenter"].forEach(ev => drop.addEventListener(ev, (e) => { e.preventDefault(); drop.classList.add("drag"); }));
  ["dragleave", "drop"].forEach(ev => drop.addEventListener(ev, (e) => { e.preventDefault(); drop.classList.remove("drag"); }));
  drop.addEventListener("drop", (e) => {
    const f = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
    if (!f || !/^image\//.test(f.type)) return;
    try {
      const dt = new DataTransfer();
      dt.items.add(f);
      $("ir2-file").files = dt.files;
    } catch (err) { /* older browsers: use input directly */ }
    ir2Load();
  });
})();

/* ---------- Color ---------- */
function genPalette() {
  const rgb = hexToRgb($("pal-in").value.trim());
  if (!rgb) { $("pal-err").textContent = "Enter a valid hex color like #ff7000"; return; }
  $("pal-err").textContent = "";
  const [r, g, b] = rgb;
  const swatches = [];
  for (const t of [0.8, 0.6, 0.4, 0.2]) swatches.push(toHexStr(r + (255 - r) * t, g + (255 - g) * t, b + (255 - b) * t));
  swatches.push(toHexStr(r, g, b));
  for (const t of [0.2, 0.4, 0.6, 0.8]) swatches.push(toHexStr(r * (1 - t), g * (1 - t), b * (1 - t)));
  $("pal-out").innerHTML = swatches.map((h) =>
    `<div class="pal-swatch" style="background:${h}" title="Click to copy ${h}" onclick="navigator.clipboard.writeText('${h}');this.querySelector('span').textContent='Copied!'"><span>${h}</span></div>`).join("");
}

/* ---------- Date & Time ---------- */
function dateDiff() {
  const a = new Date($("dd2-a").value), b = new Date($("dd2-b").value);
  if (isNaN(a) || isNaN(b)) return;
  const [s, e] = a <= b ? [a, b] : [b, a];
  const days = Math.round((e - s) / 86400000);
  let y = e.getFullYear() - s.getFullYear();
  let m = e.getMonth() - s.getMonth();
  let d = e.getDate() - s.getDate();
  if (d < 0) { m--; d += new Date(e.getFullYear(), e.getMonth(), 0).getDate(); }
  if (m < 0) { y--; m += 12; }
  out("dd2-out", `<b>${days.toLocaleString()}</b> days total<br>or <b>${y}</b> years, <b>${m}</b> months, <b>${d}</b> days<br>or <b>${Math.floor(days / 7)}</b> weeks and ${days % 7} day(s)<br>or <b>${(days * 24).toLocaleString()}</b> hours`);
}

/* ---------- Batch 9+10 tools ---------- */
function dlBytes(bytes, name, type) {
  const url = URL.createObjectURL(new Blob([bytes], { type }));
  const a = document.createElement("a");
  a.href = url; a.download = name; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 4000);
}

/* PDF Merge */
let pmFiles = [];
function pmRender() {
  const el = document.getElementById("pm-list");
  el.innerHTML = pmFiles.map((f, i) =>
    `<div style="display:flex;align-items:center;gap:8px;padding:4px 0;font-size:14px">` +
    `<b style="color:var(--accent);min-width:18px">${i + 1}.</b> <span style="flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${f.name}</span>` +
    `<button class="btn ghost" style="margin:0;padding:3px 9px;font-size:12px" onclick="pmMove(${i},-1)">↑</button>` +
    `<button class="btn ghost" style="margin:0;padding:3px 9px;font-size:12px" onclick="pmMove(${i},1)">↓</button>` +
    `<button class="btn ghost" style="margin:0;padding:3px 9px;font-size:12px" onclick="pmDel(${i})">✕</button></div>`).join("");
}
function pmMove(i, d) { const j = i + d; if (j < 0 || j >= pmFiles.length) return; [pmFiles[i], pmFiles[j]] = [pmFiles[j], pmFiles[i]]; pmRender(); }
function pmDel(i) { pmFiles.splice(i, 1); pmRender(); }
document.addEventListener("change", (e) => {
  if (e.target && e.target.id === "pm-files") { pmFiles = [...e.target.files]; pmRender(); }
});
async function pdfMerge() {
  if (pmFiles.length < 2) { out("pm-out", "Select at least two PDF files."); return; }
  if (!window.PDFLib) { out("pm-out", '<span class="error">PDF library still loading — try again in a second.</span>'); return; }
  try {
    const { PDFDocument } = window.PDFLib;
    const merged = await PDFDocument.create();
    for (const f of pmFiles) {
      const src = await PDFDocument.load(await f.arrayBuffer(), { ignoreEncryption: true });
      (await merged.copyPages(src, src.getPageIndices())).forEach((p) => merged.addPage(p));
    }
    const name = (document.getElementById("pm-name").value || "merged.pdf").replace(/\.pdf$/i, "") + ".pdf";
    dlBytes(await merged.save(), name, "application/pdf");
    out("pm-out", `Merged <b>${pmFiles.length}</b> files into <b>${merged.getPageCount()}</b> pages. Your download has started.`);
  } catch (err) {
    out("pm-out", '<span class="error">Could not read a file. Make sure every file is a valid, non-encrypted PDF.</span>');
  }
}

/* PDF Split */
function parseRanges(str, max) {
  const pages = new Set();
  for (const part of str.split(",")) {
    const t = part.trim();
    if (!t) continue;
    const m = t.match(/^(\d+)-(\d+)$/);
    if (m) {
      let a = +m[1], b = +m[2];
      if (a > b) [a, b] = [b, a];
      for (let p = a; p <= b; p++) { if (p < 1 || p > max) return null; pages.add(p - 1); }
    } else if (/^\d+$/.test(t)) {
      const p = +t;
      if (p < 1 || p > max) return null;
      pages.add(p - 1);
    } else return null;
  }
  return [...pages].sort((a, b) => a - b);
}
async function pdfSplit() {
  const f = document.getElementById("ps-file").files[0];
  if (!f) { out("ps-out", "Select a PDF file first."); return; }
  if (!window.PDFLib) { out("ps-out", '<span class="error">PDF library still loading — try again in a second.</span>'); return; }
  try {
    const { PDFDocument } = window.PDFLib;
    const src = await PDFDocument.load(await f.arrayBuffer(), { ignoreEncryption: true });
    const max = src.getPageCount();
    const idx = parseRanges(document.getElementById("ps-range").value, max);
    if (!idx || !idx.length) { out("ps-out", `<span class="error">Invalid range. This file has ${max} pages — use numbers from 1 to ${max}, like 1-3,5.</span>`); return; }
    const doc = await PDFDocument.create();
    (await doc.copyPages(src, idx)).forEach((p) => doc.addPage(p));
    const name = (document.getElementById("ps-name").value || "extracted.pdf").replace(/\.pdf$/i, "") + ".pdf";
    dlBytes(await doc.save(), name, "application/pdf");
    out("ps-out", `Extracted <b>${idx.length}</b> of ${max} pages. Your download has started.`);
  } catch (err) {
    out("ps-out", '<span class="error">Could not read the file. Is it a valid, non-encrypted PDF?</span>');
  }
}

/* Image Compressor */
function imgCompress() {
  const f = document.getElementById("ic-file").files[0];
  if (!f) { out("ic-out", "Select an image first."); return; }
  const img = new Image();
  img.onload = () => {
    const maxW = parseInt(document.getElementById("ic-w").value) || img.width;
    const scale = Math.min(1, maxW / img.width);
    const c = document.createElement("canvas");
    c.width = Math.max(1, Math.round(img.width * scale));
    c.height = Math.max(1, Math.round(img.height * scale));
    c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
    const fmt = document.getElementById("ic-fmt").value;
    const q = parseInt(document.getElementById("ic-q").value) / 100;
    c.toBlob((b) => {
      if (!b) { out("ic-out", '<span class="error">Could not encode in this format — try JPEG.</span>'); return; }
      const kb1 = (f.size / 1024).toFixed(1), kb2 = (b.size / 1024).toFixed(1);
      const pct = Math.max(0, Math.round((1 - b.size / f.size) * 100));
      out("ic-out", `Original: <b>${kb1} KB</b> → Compressed: <b>${kb2} KB</b> (${pct}% smaller, ${c.width}×${c.height}px)`);
      const url = URL.createObjectURL(b);
      const pv = document.getElementById("ic-preview"); pv.src = url; pv.style.display = "block";
      const dl = document.getElementById("ic-dl"); dl.href = url; dl.style.display = "inline-flex";
      dl.download = f.name.replace(/\.\w+$/, "") + "-compressed." + (fmt === "image/png" ? "png" : fmt === "image/webp" ? "webp" : "jpg");
    }, fmt, q);
  };
  img.onerror = () => out("ic-out", '<span class="error">Could not read that image file.</span>');
  img.src = URL.createObjectURL(f);
}

/* Image Cropper */
let icrImg = null;
document.addEventListener("change", (e) => {
  if (e.target && e.target.id === "icr-file") {
    const f = e.target.files[0];
    if (!f) return;
    const img = new Image();
    img.onload = () => {
      icrImg = img;
      document.getElementById("icr-dims").textContent = `Original: ${img.width} × ${img.height} px`;
      document.getElementById("icr-w").value = img.width;
      document.getElementById("icr-h").value = img.height;
      out("icr-out", `Image loaded (${img.width}×${img.height}). Set the crop area and click Apply crop.`);
    };
    img.src = URL.createObjectURL(f);
  }
});
function imgCrop() {
  if (!icrImg) { out("icr-out", "Load an image first."); return; }
  const W = icrImg.width, H = icrImg.height;
  let x = parseInt(document.getElementById("icr-x").value) || 0;
  let y = parseInt(document.getElementById("icr-y").value) || 0;
  let w = parseInt(document.getElementById("icr-w").value) || (W - x);
  let h = parseInt(document.getElementById("icr-h").value) || (H - y);
  x = Math.max(0, Math.min(x, W - 1)); y = Math.max(0, Math.min(y, H - 1));
  w = Math.max(1, Math.min(w, W - x)); h = Math.max(1, Math.min(h, H - y));
  const c = document.createElement("canvas");
  let ow = parseInt(document.getElementById("icr-ow").value) || w;
  ow = Math.max(1, Math.min(ow, w));
  c.width = ow; c.height = Math.max(1, Math.round(h * (ow / w)));
  c.getContext("2d").drawImage(icrImg, x, y, w, h, 0, 0, c.width, c.height);
  const fmt = document.getElementById("icr-fmt").value;
  c.toBlob((b) => {
    out("icr-out", `Cropped to <b>${w}×${h}</b> from (${x}, ${y})` + (ow !== w ? `, resized to <b>${c.width}×${c.height}</b>` : "") + ".");
    const url = URL.createObjectURL(b);
    const pv = document.getElementById("icr-preview"); pv.src = url; pv.style.display = "block";
    const dl = document.getElementById("icr-dl"); dl.href = url; dl.style.display = "inline-flex";
    dl.download = "cropped." + (fmt === "image/jpeg" ? "jpg" : "png");
  }, fmt, 0.92);
}

/* Meta Tag Generator */
function metaGen() {
  const v = (id) => (document.getElementById(id).value || "").trim();
  const esc2 = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  const title = v("mt-title"), desc = v("mt-desc"), url = v("mt-url"), author = v("mt-author"), img = v("mt-img");
  const g = document.getElementById("mt-google");
  g.innerHTML = `<div style="color:#1a0dab;font-size:18px;line-height:1.3">${esc2(title || "Your page title appears here")}</div>` +
    `<div style="color:#006621;font-size:13px">${esc2(url || "https://example.com")}</div>` +
    `<div style="color:#545454;font-size:13.5px;line-height:1.45">${esc2(desc || "Your meta description appears here — aim for 140–160 characters.")}</div>`;
  const lines = [
    `<!-- Primary meta tags -->`,
    `<title>${esc2(title)}</title>`,
    `<meta name="description" content="${esc2(desc)}" />`,
    author ? `<meta name="author" content="${esc2(author)}" />` : "",
    url ? `<link rel="canonical" href="${esc2(url)}" />` : "",
    ``,
    `<!-- Open Graph / Facebook / LinkedIn -->`,
    `<meta property="og:type" content="website" />`,
    url ? `<meta property="og:url" content="${esc2(url)}" />` : "",
    `<meta property="og:title" content="${esc2(title)}" />`,
    `<meta property="og:description" content="${esc2(desc)}" />`,
    img ? `<meta property="og:image" content="${esc2(img)}" />` : "",
    ``,
    `<!-- Twitter -->`,
    `<meta name="twitter:card" content="summary_large_image" />`,
    `<meta name="twitter:title" content="${esc2(title)}" />`,
    `<meta name="twitter:description" content="${esc2(desc)}" />`,
    img ? `<meta name="twitter:image" content="${esc2(img)}" />` : "",
  ];
  document.getElementById("mt-code").value = lines.filter((l) => l !== "").join("\n");
}

/* Keyword Density Checker */
const KD_STOP = new Set(("a,an,the,and,or,but,if,then,else,when,at,by,for,with,about,against,between,into,through,during,before,after,above,below,to,from,up,down,in,out,on,off,over,under,again,further,once,here,there,all,any,both,each,few,more,most,other,some,such,no,nor,not,only,own,same,so,than,too,very,can,will,just,is,are,was,were,be,been,being,have,has,had,having,do,does,did,doing,would,should,could,of,it,its,this,that,these,those,i,you,he,she,we,they,them,his,her,their,our,your,my,me,as").split(","));
function kwDensity() {
  const raw = document.getElementById("kd-in").value;
  const stop = document.getElementById("kd-stop").checked;
  const words = raw.toLowerCase().replace(/[^\p{L}\p{N}'’\- ]/gu, " ").split(/\s+/).filter(Boolean);
  if (words.length < 10) { out("kd-out", "Paste at least a paragraph of text."); return; }
  const kept = stop ? words.filter((w) => !KD_STOP.has(w)) : words;
  const total = words.length;
  const tables = [[], [], []];
  for (let n = 1; n <= 3; n++) {
    const counts = new Map();
    for (let i = 0; i + n <= kept.length; i++) {
      const gram = kept.slice(i, i + n).join(" ");
      counts.set(gram, (counts.get(gram) || 0) + 1);
    }
    tables[n - 1] = [...counts.entries()].sort((a, b) => b[1] - a[1]).slice(0, 10);
  }
  const max1 = tables[0].length ? tables[0][0][1] : 1;
  const bar = (c) => `<div style="display:inline-block;height:9px;background:var(--grad);border-radius:5px;width:${Math.max(2, Math.round(c / max1 * 130))}px"></div>`;
  const fmt = (n) => tables[n - 1].map(([g, c]) =>
    `<div class="wf-row"><span class="wf-word" style="width:190px">${g}</span>${n === 1 ? bar(c) : ""}<span style="margin-left:auto;font-size:12.5px;color:var(--muted)">${c}× · ${(c / total * 100).toFixed(1)}%</span></div>`).join("") || "<p>—</p>";
  out("kd-out",
    `<p style="margin:0 0 10px">Total words: <b>${total}</b>${stop ? ` · analysing <b>${kept.length}</b> after stopword filter` : ""}</p>` +
    `<b>One-word phrases</b>${fmt(1)}<br><b>Two-word phrases</b>${fmt(2)}<br><b>Three-word phrases</b>${fmt(3)}`);
}

/* XML Sitemap Generator */
function sitemapGen() {
  const urls = [...new Set(document.getElementById("sm-urls").value.split(/\s+/).filter(Boolean))];
  const freq = document.getElementById("sm-freq").value;
  const prio = document.getElementById("sm-prio").value;
  const ok = urls.filter((u) => /^https?:\/\/.+\..+/.test(u));
  const skipped = urls.length - ok.length;
  const today = new Date().toISOString().slice(0, 10);
  const esc2 = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const body = ok.map((u) =>
    `  <url>\n    <loc>${esc2(u)}</loc>\n    <lastmod>${today}</lastmod>` +
    (freq ? `\n    <changefreq>${freq}</changefreq>` : "") +
    (prio ? `\n    <priority>${prio}</priority>` : "") + `\n  </url>`).join("\n");
  const xml = ok.length ? `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${body}\n</urlset>` : "";
  document.getElementById("sm-out").value = xml;
  const dl = document.getElementById("sm-dl");
  if (ok.length) {
    dl.href = URL.createObjectURL(new Blob([xml], { type: "application/xml" }));
    dl.style.display = "inline-flex";
  } else dl.style.display = "none";
  const note = document.getElementById("sm-out");
  note.placeholder = ok.length
    ? `Generated ${ok.length} URL entries${skipped ? ` · ${skipped} invalid skipped (use full https:// addresses)` : ""}`
    : "Paste at least one valid URL (starting with https://)";
}

/* Slug Generator */
function slugifyOne(t, sep, lower, stop, maxLen) {
  let s = t.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  s = s.replace(/[^A-Za-z0-9\s\-_]/g, " ").trim();
  let parts = s.split(/[\s\-_]+/).filter(Boolean);
  if (lower) parts = parts.map((p) => p.toLowerCase());
  if (stop) parts = parts.filter((p) => !KD_STOP.has(p.toLowerCase()));
  if (maxLen > 0 && parts.length) {
    const outp = [];
    let len = 0;
    for (const p of parts) {
      const add = p.length + (outp.length ? 1 : 0);
      if (len + add > maxLen) break;
      outp.push(p); len += add;
    }
    if (outp.length) parts = outp;
  }
  return parts.join(sep);
}
function slugGen() {
  const lines = document.getElementById("sl-in").value.split("\n").map((l) => l.trim()).filter(Boolean);
  if (!lines.length) { document.getElementById("sl-out").value = ""; return; }
  const sep = document.getElementById("sl-sep").value;
  const lower = document.getElementById("sl-lower").checked;
  const stop = document.getElementById("sl-stop").checked;
  const maxLen = parseInt(document.getElementById("sl-len").value) || 0;
  document.getElementById("sl-out").value = lines.map((l) => slugifyOne(l, sep, lower, stop, maxLen)).join("\n");
}

/* Invoice Generator */
function invAddRow() {
  const div = document.createElement("div");
  div.className = "row inv-row";
  div.style.marginBottom = "6px";
  div.innerHTML = `<div style="flex:3"><input type="text" placeholder="Description" oninput="invoiceRender()" /></div>` +
    `<div><input type="number" placeholder="Qty" value="1" min="0" oninput="invoiceRender()" /></div>` +
    `<div><input type="number" placeholder="Rate" min="0" step="0.01" oninput="invoiceRender()" /></div>` +
    `<div style="flex:0"><button class="btn ghost" style="margin:0;padding:9px 12px" onclick="this.closest('.inv-row').remove();invoiceRender()">✕</button></div>`;
  document.getElementById("inv-items").appendChild(div);
  invoiceRender();
}
function invItems() {
  return [...document.querySelectorAll("#inv-items .inv-row")].map((r) => {
    const inputs = r.querySelectorAll("input");
    return { d: inputs[0].value, q: parseFloat(inputs[1].value) || 0, rate: parseFloat(inputs[2].value) || 0 };
  }).filter((i) => i.d || i.q * i.rate);
}
function invoiceRender() {
  const v = (id) => (document.getElementById(id).value || "").trim();
  const items = invItems();
  const taxPct = parseFloat(v("inv-tax")) || 0;
  const sub = items.reduce((s, i) => s + i.q * i.rate, 0);
  const tax = sub * taxPct / 100;
  const money = (n) => n.toFixed(2);
  const rows = items.map((i) =>
    `<tr><td style="padding:7px 4px;border-bottom:1px solid var(--border)">${i.d || "—"}</td>` +
    `<td style="padding:7px 4px;border-bottom:1px solid var(--border);text-align:center">${i.q || ""}</td>` +
    `<td style="padding:7px 4px;border-bottom:1px solid var(--border);text-align:right">${money(i.rate)}</td>` +
    `<td style="padding:7px 4px;border-bottom:1px solid var(--border);text-align:right">${money(i.q * i.rate)}</td></tr>`).join("");
  document.getElementById("inv-print").innerHTML =
    `<div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px">` +
    `<div><div style="font-size:22px;font-weight:800;color:var(--accent)">INVOICE</div>` +
    `<div style="font-size:12px;color:var(--muted)">#${v("inv-num") || "—"}</div></div>` +
    `<div style="font-size:12.5px;color:var(--muted);text-align:right">Issued: ${v("inv-date") || "—"}<br>Due: ${v("inv-due") || "—"}</div></div>` +
    `<div style="display:flex;gap:30px;margin:18px 0;flex-wrap:wrap;font-size:13px">` +
    `<div><b>From</b><br>${v("inv-from") || "—"}<br><span style="color:var(--muted)">${v("inv-from2")}</span></div>` +
    `<div><b>To</b><br>${v("inv-to") || "—"}<br><span style="color:var(--muted)">${v("inv-to2")}</span></div></div>` +
    `<table style="width:100%;border-collapse:collapse;font-size:13.5px"><tr>` +
    `<th style="text-align:left;padding:7px 4px;border-bottom:2px solid var(--border2)">Description</th>` +
    `<th style="text-align:center;padding:7px 4px;border-bottom:2px solid var(--border2)">Qty</th>` +
    `<th style="text-align:right;padding:7px 4px;border-bottom:2px solid var(--border2)">Rate</th>` +
    `<th style="text-align:right;padding:7px 4px;border-bottom:2px solid var(--border2)">Amount</th></tr>` +
    (rows || `<tr><td colspan="4" style="padding:10px;color:var(--muted)">No line items yet.</td></tr>`) +
    `</table>` +
    `<div style="margin-top:14px;text-align:right;font-size:14px">` +
    `<div>Subtotal: <b>${money(sub)}</b></div>` +
    (taxPct ? `<div>Tax (${taxPct}%): <b>${money(tax)}</b></div>` : "") +
    `<div style="font-size:17px;margin-top:5px">Total due: <b style="color:var(--accent)">${money(sub + tax)}</b></div></div>`;
}
function invPrint() {
  const html = document.getElementById("inv-print").innerHTML;
  const w = window.open("", "_blank");
  if (!w) { alert("Allow pop-ups to print the invoice."); return; }
  w.document.write(`<!doctype html><html><head><title>Invoice</title><style>body{font-family:system-ui,sans-serif;max-width:720px;margin:30px auto;padding:0 20px;color:#1a1a1a}table{width:100%;border-collapse:collapse}th{text-align:left;border-bottom:2px solid #ccc;padding:7px 4px}td{border-bottom:1px solid #ddd;padding:7px 4px}</style></head><body>` +
    html.replace(/class="[^"]*"/g, "").replace(/var\(--[^)]+\)/g, "#1a1a1a") + `</body></html>`);
  w.document.close();
  setTimeout(() => w.print(), 250);
}

/* init invoice rows */
document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("inv-items")) { invAddRow(); invAddRow(); }
});

/* JSON to CSV Converter */
function jsonToCsv() {
  let data;
  try { data = JSON.parse(document.getElementById("j2c-in").value); }
  catch (e) { out("j2c-out", '<span class="error">Invalid JSON: ' + e.message + "</span>"); return; }
  if (!Array.isArray(data) || !data.length || typeof data[0] !== "object") {
    out("j2c-out", '<span class="error">Input must be a non-empty JSON array of objects, e.g. [{"a":1}].</span>'); return;
  }
  const q = (v) => {
    if (v === null || v === undefined) return "";
    if (typeof v === "object") v = JSON.stringify(v);
    v = String(v);
    return /[",\n]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v;
  };
  const keys = [...new Set(data.flatMap((o) => Object.keys(o)))];
  const csv = [keys.join(",")].concat(data.map((o) => keys.map((k) => q(o[k])).join(","))).join("\n");
  document.getElementById("j2c-out").value = csv;
  const dl = document.getElementById("j2c-dl");
  dl.href = URL.createObjectURL(new Blob([csv], { type: "text/csv" }));
  dl.style.display = "inline-flex";
  out("j2c-out", "");
}

/* ===================== Batch 11: advanced tools ===================== */

/* ---- QR Code Generator ---- */
let QR2_TYPE = "text";
function qr2Type(t, btn) {
  QR2_TYPE = t;
  document.querySelectorAll(".qr2-tabs .pg-tab").forEach(b => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  qr2Fields();
  qr2Gen();
}
function qr2F(id, label, ph, val) {
  return `<div><label>${label}</label><input type="text" id="${id}" placeholder="${ph}" value="${val || ""}" oninput="qr2Gen()" /></div>`;
}
function qr2Fields() {
  const el = $("qr2-fields");
  if (QR2_TYPE === "text") {
    el.innerHTML = `<label>Text or URL to encode</label><textarea id="qr-text" oninput="qr2Gen()" placeholder="https://example.com"></textarea>`;
  } else if (QR2_TYPE === "wifi") {
    el.innerHTML = `<div class="row"><div>${qr2F("qr-w-ssid", "Network name (SSID)", "MyWiFi")}</div><div>${qr2F("qr-w-pass", "Password", "\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022")}</div></div>
      <div class="row"><div><label>Security</label><select id="qr-w-sec" onchange="qr2Gen()"><option value="WPA" selected>WPA / WPA2 / WPA3</option><option value="WEP">WEP</option><option value="nopass">Open (no password)</option></select></div>
      <div><label>Hidden network</label><label class="pg-switch"><input type="checkbox" id="qr-w-hid" onchange="qr2Gen()" /><span class="pg-track"></span> Hidden SSID</label></div></div>`;
  } else if (QR2_TYPE === "email") {
    el.innerHTML = `<div class="row"><div>${qr2F("qr-e-to", "Email address", "name@example.com")}</div><div>${qr2F("qr-e-sub", "Subject (optional)", "Hello")}</div></div>
      <label>Message (optional)</label><textarea id="qr-e-body" oninput="qr2Gen()" placeholder="Write your message\u2026"></textarea>`;
  } else if (QR2_TYPE === "phone") {
    el.innerHTML = `<div class="row"><div>${qr2F("qr-p-num", "Phone number", "+15551234567")}</div></div>`;
  } else {
    el.innerHTML = `<div class="row"><div>${qr2F("qr-s-num", "Phone number", "+15551234567")}</div><div>${qr2F("qr-s-msg", "Message (optional)", "Hi!")}</div></div>`;
  }
  qr2Gen();
}
function qr2Payload() {
  const esc = (s) => (s || "").replace(/([\\;,:"])/g, "\\$1");
  if (QR2_TYPE === "wifi") {
    const ssid = ($("qr-w-ssid") || {}).value || "";
    if (!ssid) return "";
    const sec = $("qr-w-sec").value;
    const pass = ($("qr-w-pass") || {}).value || "";
    const hid = $("qr-w-hid") && $("qr-w-hid").checked ? "H;" : "";
    return `WIFI:T:${sec};S:${esc(ssid)};${sec !== "nopass" ? "P:" + esc(pass) + ";" : ""}${hid};`;
  }
  if (QR2_TYPE === "email") {
    const to = ($("qr-e-to") || {}).value || "";
    if (!to) return "";
    const sub = encodeURIComponent(($("qr-e-sub") || {}).value || "");
    const body = encodeURIComponent(($("qr-e-body") || {}).value || "");
    return `mailto:${to}?subject=${sub}&body=${body}`;
  }
  if (QR2_TYPE === "phone") {
    const n = ($("qr-p-num") || {}).value || "";
    return n ? "tel:" + n : "";
  }
  if (QR2_TYPE === "sms") {
    const n = ($("qr-s-num") || {}).value || "";
    const m = ($("qr-s-msg") || {}).value || "";
    return n ? `SMSTO:${n}:${m}` : "";
  }
  return ($("qr-text") || {}).value || "";
}
function qr2Gen() {
  const box = $("qr-box");
  if (!box) return;
  const data = qr2Payload();
  const status = $("qr2-status");
  box.innerHTML = "";
  if (!data) { if (status) status.textContent = "Fill in the fields above \u2014 the QR code updates live."; return; }
  if (typeof QRCode === "undefined") { if (status) status.textContent = "QR library still loading\u2026"; return; }
  try {
    new QRCode(box, {
      text: data,
      width: +$("qr-size").value,
      height: +$("qr-size").value,
      colorDark: $("qr-fg").value,
      colorLight: $("qr-bg").value,
      correctLevel: QRCode.CorrectLevel[$("qr-ecc").value],
    });
    if (status) status.textContent = `${data.length} characters encoded \u00b7 level ${$("qr-ecc").value} correction`;
  } catch (e) {
    if (status) status.textContent = "Too much data for one QR code \u2014 shorten the text or lower the correction level.";
  }
}
function qr2Download() {
  const c = document.querySelector("#qr-box canvas");
  const img = document.querySelector("#qr-box img");
  if (!c && !img) return;
  const a = document.createElement("a");
  let url;
  if (c) {
    const margin = +$("qr-margin").value;
    const out = document.createElement("canvas");
    const pad = margin * Math.round(c.width / 32);
    out.width = c.width + pad * 2;
    out.height = c.height + pad * 2;
    const ctx = out.getContext("2d");
    ctx.fillStyle = $("qr-bg").value;
    ctx.fillRect(0, 0, out.width, out.height);
    ctx.drawImage(c, pad, pad);
    url = out.toDataURL("image/png");
  } else {
    url = img.src;
  }
  a.href = url; a.download = "qr-code.png"; a.click();
}
function qr2CopyData(btn) {
  const data = qr2Payload();
  if (!data) return;
  (navigator.clipboard ? navigator.clipboard.writeText(data) : Promise.reject()).then(() => {
    btn.textContent = "Copied!"; setTimeout(() => { btn.textContent = "Copy QR data"; }, 1200);
  }).catch(() => {});
}
if ($("qr2-fields")) qr2Fields();

/* ---- Text Diff Checker (LCS on lines) ---- */
function dEsc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
let DF2_MODE = "lines", DF2_TIMER = null;
function df2Norm(s) {
  if ($("df2-case").checked) s = s.toLowerCase();
  if ($("df2-ws").checked) s = s.replace(/\s+/g, " ").trim();
  return s;
}
function df2Esc(s) { return escHtml(s); }
function df2LcsOps(a, b) {
  const n = a.length, m = b.length;
  const dp = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(0));
  for (let i = n - 1; i >= 0; i--)
    for (let j = m - 1; j >= 0; j--)
      dp[i][j] = a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
  const ops = [];
  let i = 0, j = 0;
  while (i < n && j < m) {
    if (a[i] === b[j]) { ops.push(["same", i, j]); i++; j++; }
    else if (dp[i + 1][j] >= dp[i][j + 1]) { ops.push(["del", i, j]); i++; }
    else { ops.push(["add", i, j]); j++; }
  }
  while (i < n) { ops.push(["del", i, j]); i++; }
  while (j < m) { ops.push(["add", i, j]); j++; }
  return ops;
}
function df2Stats(adds, dels, same) {
  const total = adds + dels + same;
  const sim = total ? Math.round(same / total * 100) : 100;
  $("df2-stats").innerHTML = `
    <div class="jf-chip df2-c-add"><b>+${adds}</b><span>added</span></div>
    <div class="jf-chip df2-c-del"><b>\u2212${dels}</b><span>removed</span></div>
    <div class="jf-chip"><b>${same}</b><span>unchanged</span></div>
    <div class="jf-chip"><b>${sim}%</b><span>similarity</span></div>`;
  $("df2-sim").style.width = sim + "%";
  $("df2-sim").className = "df2-sim-fill" + (sim >= 80 ? " hi" : sim >= 40 ? " mid" : " lo");
}
function df2Run() {
  const rawA = $("diff-a").value, rawB = $("diff-b").value;
  const out = $("diff-out");
  if (!rawA && !rawB) { out.innerHTML = '<p class="wc-empty">Paste text in both boxes \u2014 the comparison updates live.</p>'; $("df2-stats").innerHTML = ""; $("df2-sim").style.width = "0"; return; }
  let html = "", adds = 0, dels = 0, same = 0;
  if (DF2_MODE === "lines") {
    const A = rawA.split("\n"), B = rawB.split("\n");
    const ops = df2LcsOps(A.map(df2Norm), B.map(df2Norm));
    let lnA = 0, lnB = 0;
    html = ops.map(([op, i, j]) => {
      if (op === "same") { same++; lnA++; lnB++; return `<div class="dln same"><span class="dln-n">${lnA}</span>${df2Esc(A[i]) || "&nbsp;"}</div>`; }
      if (op === "del") { dels++; lnA++; return `<div class="dln del"><span class="dln-n">${lnA}</span>&minus; ${df2Esc(A[i])}</div>`; }
      adds++; lnB++; return `<div class="dln add"><span class="dln-n">${lnB}</span>+ ${df2Esc(B[j])}</div>`;
    }).join("");
  } else {
    const A = rawA.split(/(\s+)/).filter(w => w.trim() !== ""), B = rawB.split(/(\s+)/).filter(w => w.trim() !== "");
    const ops = df2LcsOps(A.map(df2Norm), B.map(df2Norm));
    html = ops.map(([op, i, j]) => {
      if (op === "same") { same++; return `<span class="dfw same">${df2Esc(A[i])}</span> `; }
      if (op === "del") { dels++; return `<span class="dfw del">${df2Esc(A[i])}</span> `; }
      adds++; return `<span class="dfw add">${df2Esc(B[j])}</span> `;
    }).join("");
    html = `<div class="df2-words">${html}</div>`;
  }
  df2Stats(adds, dels, same);
  out.innerHTML = html;
}
function df2SetMode(m, btn) {
  DF2_MODE = m;
  $("df2-m-lines").classList.toggle("active", m === "lines");
  $("df2-m-words").classList.toggle("active", m === "words");
  df2Run();
}
function df2Live() {
  clearTimeout(DF2_TIMER);
  DF2_TIMER = setTimeout(df2Run, 250);
}
if ($("diff-a")) df2Run();

/* ---- Markdown Previewer ---- */
function mdRender() {
  const src = document.getElementById("md-in").value;
  const lines = src.split("\n");
  const inline = (s) => dEsc(s)
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g, "<em>$1</em>")
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, '<a href="$2" rel="noopener">$1</a>');
  let html = "", inUl = false, inOl = false, inCode = false, codeBuf = [];
  const closeLists = () => { if (inUl) { html += "</ul>"; inUl = false; } if (inOl) { html += "</ol>"; inOl = false; } };
  for (const raw of lines) {
    if (/^```/.test(raw)) {
      if (inCode) { html += "<pre><code>" + dEsc(codeBuf.join("\n")) + "</code></pre>"; inCode = false; codeBuf = []; }
      else { closeLists(); inCode = true; }
      continue;
    }
    if (inCode) { codeBuf.push(raw); continue; }
    const h = raw.match(/^(#{1,6})\s+(.*)$/);
    if (h) { closeLists(); html += `<h${h[1].length}>${inline(h[2])}</h${h[1].length}>`; continue; }
    if (/^\s*[-*+]\s+/.test(raw)) { if (inOl) { html += "</ol>"; inOl = false; } if (!inUl) { html += "<ul>"; inUl = true; } html += `<li>${inline(raw.replace(/^\s*[-*+]\s+/, ""))}</li>`; continue; }
    if (/^\s*\d+[.)]\s+/.test(raw)) { if (inUl) { html += "</ul>"; inUl = false; } if (!inOl) { html += "<ol>"; inOl = true; } html += `<li>${inline(raw.replace(/^\s*\d+[.)]\s+/, ""))}</li>`; continue; }
    if (/^\s*(---|\*\*\*|___)\s*$/.test(raw)) { closeLists(); html += "<hr>"; continue; }
    if (/^\s*>\s?/.test(raw)) { closeLists(); html += `<blockquote>${inline(raw.replace(/^\s*>\s?/, ""))}</blockquote>`; continue; }
    if (!raw.trim()) { closeLists(); continue; }
    closeLists(); html += `<p>${inline(raw)}</p>`;
  }
  if (inCode) html += "<pre><code>" + dEsc(codeBuf.join("\n")) + "</code></pre>";
  closeLists();
  document.getElementById("md-out").innerHTML = html;
  document.getElementById("md-html").value = html;
}

/* ---- Image Watermarker ---- */
let wmImg = null;
function wmLoad() {
  const f = document.getElementById("wm-file").files[0];
  if (!f) return;
  const img = new Image();
  img.onload = () => { wmImg = img; wmDraw(); };
  img.src = URL.createObjectURL(f);
}
function wmDraw() {
  const opv = document.getElementById("wm-opv");
  if (opv) opv.textContent = document.getElementById("wm-opacity").value;
  if (!wmImg) return;
  const c = document.getElementById("wm-canvas");
  const max = 1400;
  const sc = Math.min(1, max / Math.max(wmImg.width, wmImg.height));
  c.width = Math.round(wmImg.width * sc);
  c.height = Math.round(wmImg.height * sc);
  const x = c.getContext("2d");
  x.drawImage(wmImg, 0, 0, c.width, c.height);
  const txt = document.getElementById("wm-text").value || "\u00a9";
  const pos = document.getElementById("wm-pos").value;
  const fs = Math.max(10, c.width * (+document.getElementById("wm-size").value || 4) / 100);
  const op = (+document.getElementById("wm-opacity").value || 35) / 100;
  const col = document.getElementById("wm-color").value;
  x.font = `600 ${fs}px system-ui, sans-serif`;
  x.globalAlpha = op;
  x.fillStyle = col;
  const w = x.measureText(txt).width, pad = fs * 0.6;
  const P = {
    tl: [pad, pad + fs], tc: [(c.width - w) / 2, pad + fs], tr: [c.width - w - pad, pad + fs],
    ml: [pad, c.height / 2], mc: [(c.width - w) / 2, c.height / 2], mr: [c.width - w - pad, c.height / 2],
    bl: [pad, c.height - pad], bc: [(c.width - w) / 2, c.height - pad], br: [c.width - w - pad, c.height - pad]
  };
  const p = P[pos] || P.br;
  x.fillText(txt, p[0], p[1]);
  x.globalAlpha = 1;
}
function wmSave() {
  const c = document.getElementById("wm-canvas");
  if (!c.width) return;
  c.toBlob((b) => dlBytes(b, "watermarked.png", "image/png"), "image/png");
}

/* ---- Favicon Generator ---- */
function fvGen() {
  const f = document.getElementById("fv-file").files[0];
  if (!f) return;
  const img = new Image();
  img.onload = () => {
    const sizes = [16, 32, 180, 512];
    const row = document.getElementById("fv-previews");
    let tags = "";
    row.innerHTML = "";
    sizes.forEach((s) => {
      const c = document.createElement("canvas");
      c.width = c.height = s;
      c.getContext("2d").drawImage(img, 0, 0, s, s);
      const url = c.toDataURL("image/png");
      const name = s === 180 ? "apple-touch-icon.png" : `favicon-${s}x${s}.png`;
      row.insertAdjacentHTML("beforeend",
        `<div class="fav-item"><img src="${url}" width="${Math.min(64, s)}" height="${Math.min(64, s)}"><span>${s} px</span><a class="btn ghost" download="${name}" href="${url}">Download</a></div>`);
      tags += `<link rel="icon" type="image/png" sizes="${s}x${s}" href="/${name}">\n`;
    });
    document.getElementById("fv-tags").value = tags.trim();
  };
  img.src = URL.createObjectURL(f);
}

/* ---- Base64 Image Encoder ---- */
function b64Enc() {
  const f = document.getElementById("b64-file").files[0];
  if (!f) return;
  const r = new FileReader();
  r.onload = () => {
    const uri = r.result;
    document.getElementById("b64-out").value = uri;
    document.getElementById("b64-html").value = `<img src="${uri}" alt="">`;
    document.getElementById("b64-css").value = `background-image: url(${uri});`;
    out("b64-info", `<b>${escHtml(f.name)}</b> \u2014 ${(f.size / 1024).toFixed(1)} KB \u2192 ${(uri.length / 1024).toFixed(1)} KB encoded (+${Math.round((uri.length / f.size - 1) * 100)}%)`);
  };
  r.readAsDataURL(f);
}

/* ---- Online Stopwatch (timestamp-based, drift-free) ---- */
let swAcc = 0, swRun = false, swT0 = 0, swLaps = [], swTimer = null;
function swNow() { return swAcc + (swRun ? Date.now() - swT0 : 0); }
function swFmt(ms) {
  const h = Math.floor(ms / 3600000), m = Math.floor(ms % 3600000 / 60000), s = Math.floor(ms % 60000 / 1000), cs = Math.floor(ms % 1000 / 10);
  const core = String(m).padStart(2, "0") + ":" + String(s).padStart(2, "0") + "." + String(cs).padStart(2, "0");
  return h > 0 ? h + ":" + core : core;
}
function swTick() { const el = document.getElementById("sw-display"); if (el) el.textContent = swFmt(swNow()); }
function swStart() {
  if (swRun) return;
  swRun = true; swT0 = Date.now();
  clearInterval(swTimer); swTimer = setInterval(swTick, 31);
  document.getElementById("sw-start").textContent = "Resume";
}
function swPause() {
  if (!swRun) return;
  swAcc = swNow(); swRun = false;
  clearInterval(swTimer);
  document.getElementById("sw-start").textContent = "Start";
}
function swLap() {
  const total = swNow();
  if (!total) return;
  const prev = swLaps.length ? swLaps[swLaps.length - 1].total : 0;
  swLaps.push({ split: total - prev, total });
  let h = `<table class="lap-table"><thead><tr><th>Lap</th><th>Split</th><th>Total</th></tr></thead><tbody>`;
  swLaps.slice().reverse().forEach((l, idx) => {
    h += `<tr><td>${swLaps.length - idx}</td><td>${swFmt(l.split)}</td><td>${swFmt(l.total)}</td></tr>`;
  });
  document.getElementById("sw-laps").innerHTML = h + "</tbody></table>";
}
function swReset() {
  swAcc = 0; swRun = false; swLaps = [];
  clearInterval(swTimer);
  document.getElementById("sw-display").textContent = "00:00.00";
  document.getElementById("sw-laps").innerHTML = "";
  document.getElementById("sw-start").textContent = "Start";
}

/* ---- Countdown Timer ---- */
let cdTarget = 0, cdTotal = 0, cdTimer = null;
function cdStart() {
  const d = document.getElementById("cd-date").value;
  const tm = document.getElementById("cd-time-val").value || "09:00";
  if (!d) { out("cd-msg", "<span class='error'>Pick a date first.</span>"); return; }
  cdTarget = new Date(d + "T" + tm).getTime();
  cdTotal = cdTarget - Date.now();
  if (cdTotal <= 0) { out("cd-msg", "<span class='error'>That moment is already in the past \u2014 pick a future date and time.</span>"); return; }
  clearInterval(cdTimer);
  cdTimer = setInterval(cdTick, 250);
  cdTick();
}
function cdTick() {
  const left = cdTarget - Date.now();
  const name = document.getElementById("cd-name").value;
  const label = name ? `<div class="tool-note" style="text-align:center">${escHtml(name)}</div>` : "";
  if (left <= 0) {
    clearInterval(cdTimer);
    document.getElementById("cd-units").innerHTML = label +
      `<div class="cd-unit"><b>0</b><span>Days</span></div><div class="cd-unit"><b>0</b><span>Hours</span></div><div class="cd-unit"><b>0</b><span>Minutes</span></div><div class="cd-unit"><b>0</b><span>Seconds</span></div>`;
    document.getElementById("cd-fill").style.width = "100%";
    out("cd-msg", "<b>Time is up!</b> The countdown has finished.");
    return;
  }
  const d = Math.floor(left / 86400000), h = Math.floor(left % 86400000 / 3600000),
    m = Math.floor(left % 3600000 / 60000), s = Math.floor(left % 60000 / 1000);
  document.getElementById("cd-units").innerHTML = label +
    `<div class="cd-unit"><b>${d}</b><span>Days</span></div><div class="cd-unit"><b>${h}</b><span>Hours</span></div><div class="cd-unit"><b>${m}</b><span>Minutes</span></div><div class="cd-unit"><b>${s}</b><span>Seconds</span></div>`;
  document.getElementById("cd-fill").style.width = ((1 - left / cdTotal) * 100).toFixed(2) + "%";
}

/* Render the word counter reference table on page load */
(function () {
  const el = document.getElementById("wc-table");
  if (el && !el.innerHTML) wcRefTable();
})();

/* ============ Modern custom date & time pickers (replace native) ============ */
const DP_MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"];
const DP_DOW = ["S","M","T","W","T","F","S"];
function dpISO(d) { return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); }
function attachDatePicker(id) {
  const inp = document.getElementById(id);
  if (!inp || inp.dataset.dp) return;
  inp.dataset.dp = "1"; inp.readOnly = true; inp.classList.add("dt-input");
  inp.placeholder = "Pick a date"; inp.setAttribute("autocomplete", "off");
  const wrap = document.createElement("div"); wrap.className = "dp-wrap";
  inp.parentNode.insertBefore(wrap, inp); wrap.appendChild(inp);
  const panel = document.createElement("div"); panel.className = "dp-panel"; panel.style.display = "none";
  wrap.appendChild(panel);
  let view = new Date();
  function render() {
    const y = view.getFullYear(), m = view.getMonth();
    const startDow = new Date(y, m, 1).getDay();
    const days = new Date(y, m + 1, 0).getDate();
    const today = dpISO(new Date());
    let h = '<div class="dp-head"><button type="button" class="dp-nav" data-n="-1">&lsaquo;</button><span class="dp-title">' + DP_MONTHS[m] + " " + y + '</span><button type="button" class="dp-nav" data-n="1">&rsaquo;</button></div><div class="dp-grid">';
    h += DP_DOW.map((d) => '<span class="dp-dow">' + d + "</span>").join("");
    for (let i = 0; i < startDow; i++) h += "<span></span>";
    for (let d = 1; d <= days; d++) {
      const iso = y + "-" + String(m + 1).padStart(2, "0") + "-" + String(d).padStart(2, "0");
      const cls = "dp-day" + (inp.value === iso ? " dp-sel" : "") + (iso === today ? " dp-today" : "");
      h += '<button type="button" class="' + cls + '" data-d="' + d + '">' + d + "</button>";
    }
    panel.innerHTML = h + '</div><div class="dp-foot"><button type="button" class="dp-clear">Clear</button></div>';
  }
  inp.addEventListener("click", () => {
    if (inp.value) { const p = inp.value.split("-"); view = new Date(+p[0], +p[1] - 1, 1); }
    render();
    panel.style.display = panel.style.display === "none" ? "block" : "none";
  });
  panel.addEventListener("click", (e) => {
    const b = e.target.closest("button"); if (!b) return;
    const fire = () => { inp.dispatchEvent(new Event("input")); inp.dispatchEvent(new Event("change")); };
    if (b.classList.contains("dp-nav")) { view = new Date(view.getFullYear(), view.getMonth() + +b.dataset.n, 1); render(); }
    else if (b.classList.contains("dp-clear")) { inp.value = ""; render(); panel.style.display = "none"; fire(); }
    else if (b.classList.contains("dp-day")) { inp.value = dpISO(new Date(view.getFullYear(), view.getMonth(), +b.dataset.d)); render(); panel.style.display = "none"; fire(); }
  });
  document.addEventListener("click", (e) => { if (!wrap.contains(e.target)) panel.style.display = "none"; });
  render();
}
function attachTimePicker(dispId, hiddenId, def) {
  const inp = document.getElementById(dispId), hid = document.getElementById(hiddenId);
  if (!inp || !hid || inp.dataset.tp) return;
  inp.dataset.tp = "1"; inp.readOnly = true; inp.classList.add("dt-input");
  inp.placeholder = "Pick a time"; inp.setAttribute("autocomplete", "off");
  const wrap = document.createElement("div"); wrap.className = "dp-wrap";
  inp.parentNode.insertBefore(wrap, inp); wrap.appendChild(inp);
  const panel = document.createElement("div"); panel.className = "dp-panel"; panel.style.display = "none";
  wrap.appendChild(panel);
  let h12 = ((+def.split(":")[0] + 11) % 12) + 1, ap = +def.split(":")[0] >= 12 ? "PM" : "AM", m = +def.split(":")[1];
  let colH = "", colM = "";
  for (let i = 1; i <= 12; i++) colH += '<button type="button" data-h="' + i + '">' + String(i).padStart(2, "0") + "</button>";
  for (let i = 0; i < 60; i++) colM += '<button type="button" data-m="' + i + '">' + String(i).padStart(2, "0") + "</button>";
  panel.innerHTML = '<div class="tp-row"><div class="tp-col">' + colH + '</div><div class="tp-col">' + colM + '</div><div class="tp-col tp-ap"><button type="button" data-ap="AM">AM</button><button type="button" data-ap="PM">PM</button></div></div>';
  function sync() {
    const h = (h12 % 12) + (ap === "PM" ? 12 : 0);
    inp.value = String(h12).padStart(2, "0") + ":" + String(m).padStart(2, "0") + " " + ap;
    hid.value = String(h).padStart(2, "0") + ":" + String(m).padStart(2, "0");
    panel.querySelectorAll("[data-h]").forEach((b) => b.classList.toggle("tp-on", +b.dataset.h === h12));
    panel.querySelectorAll("[data-m]").forEach((b) => b.classList.toggle("tp-on", +b.dataset.m === m));
    panel.querySelectorAll("[data-ap]").forEach((b) => b.classList.toggle("tp-on", b.dataset.ap === ap));
  }
  inp.addEventListener("click", () => { panel.style.display = panel.style.display === "none" ? "block" : "none"; });
  panel.addEventListener("click", (e) => {
    const b = e.target.closest("button"); if (!b) return;
    if (b.dataset.h !== undefined && b.dataset.h !== "") h12 = +b.dataset.h;
    else if (b.dataset.m !== undefined && b.dataset.m !== "") { m = +b.dataset.m; panel.style.display = "none"; }
    else if (b.dataset.ap) { ap = b.dataset.ap; panel.style.display = "none"; }
    sync();
  });
  document.addEventListener("click", (e) => { if (!wrap.contains(e.target)) panel.style.display = "none"; });
  sync();
}
function initPickers() {
  ["cd-date", "inv-date", "inv-due", "age-dob", "dd2-a", "dd2-b", "rd-a", "rd-b", "ad-date", "dw-date", "wn-date", "bd-a", "bd-b"].forEach(function (id) { if ($(id)) attachDatePicker(id); });
  attachTimePicker("cd-time", "cd-time-val", "09:00");
  if ($("hr-s")) attachTimePicker("hr-s", "hr-sv", "09:00");
  if ($("hr-e")) attachTimePicker("hr-e", "hr-ev", "17:30");
  if ($("mt-time")) attachTimePicker("mt-time", "mt-tv", "09:00");
}
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initPickers);
else initPickers();

/* ===================== Batch 12: advanced tools ===================== */

/* ---- Password Strength Checker ---- */
const PW_COMMON = ["password", "123456", "qwerty", "letmein", "admin", "welcome", "iloveyou", "monkey", "dragon", "football", "abc123", "111111", "summer", "winter"];
function pwSecFmt(sec) {
  if (sec < 1) return "instantly";
  const mins = sec / 60, h = mins / 60, d = h / 24, y = d / 365;
  if (y > 1e9) return "billions of years";
  if (y > 1000) return Math.round(y).toLocaleString() + " years";
  if (y > 1) return Math.round(y) + " years";
  if (d > 1) return Math.round(d) + " days";
  if (h > 1) return Math.round(h) + " hours";
  if (mins > 1) return Math.round(mins) + " minutes";
  return Math.round(sec) + " seconds";
}
function pwCheck() {
  const pw = document.getElementById("pw-in").value;
  let classes = 0;
  if (/[a-z]/.test(pw)) classes++;
  if (/[A-Z]/.test(pw)) classes++;
  if (/[0-9]/.test(pw)) classes++;
  if (/[^A-Za-z0-9]/.test(pw)) classes++;
  const pool = { 0: 0, 1: 26, 2: 52, 3: 62, 4: 95 }[classes] || 0;
  const bits = pw ? Math.round(pw.length * Math.log2(pool || 2)) : 0;
  const sec = bits ? Math.pow(2, bits - 1) / 1e10 : 0;
  const lower = pw.toLowerCase();
  const issues = [];
  if (pw.length < 12) issues.push("Shorter than 12 characters \u2014 length is the cheapest entropy.");
  if (!/[A-Z]/.test(pw)) issues.push("No uppercase letters.");
  if (!/[0-9]/.test(pw)) issues.push("No digits.");
  if (!/[^A-Za-z0-9]/.test(pw)) issues.push("No symbols.");
  if (/(.)\1{2,}/.test(pw)) issues.push("Contains repeated characters.");
  if (/(012|123|234|345|456|567|678|789|abc|bcd|cde|def|qwer|asdf)/i.test(pw)) issues.push("Contains a sequence or keyboard walk.");
  if (PW_COMMON.some((c) => lower.includes(c))) issues.push("Contains a commonly leaked word.");
  const score = Math.max(0, Math.min(100, bits * 1.4 - issues.length * 8));
  const fill = document.getElementById("pw-fill");
  fill.style.width = score + "%";
  fill.style.background = score < 40 ? "var(--err)" : score < 70 ? "#fbbf24" : "var(--ok)";
  document.getElementById("pw-stats").innerHTML =
    `<div class="stat"><b>${bits}</b><span>Entropy (bits)</span></div>
     <div class="stat"><b>${pool}</b><span>Charset pool</span></div>
     <div class="stat"><b>${pwSecFmt(sec)}</b><span>Offline crack time</span></div>
     <div class="stat"><b>${pw.length}</b><span>Length</span></div>`;
  document.getElementById("pw-out").innerHTML = issues.length
    ? "<b>To improve:</b><ul>" + issues.map((i) => "<li>" + escHtml(i) + "</li>").join("") + "</ul>"
    : (pw ? "<b>Excellent.</b> No structural weaknesses detected \u2014 pair it with two-factor authentication." : "");
}

/* ---- Cron Expression Explainer ---- */
const CRON_DOW = { sun: 0, mon: 1, tue: 2, wed: 3, thu: 4, fri: 5, sat: 6 };
const CRON_MON = { jan: 1, feb: 2, mar: 3, apr: 4, may: 5, jun: 6, jul: 7, aug: 8, sep: 9, oct: 10, nov: 11, dec: 12 };
const CRON_DOW_NAMES = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const CRON_MON_NAMES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
function cronParseField(f, min, max, nameMap) {
  const set = new Set();
  for (const part of f.split(",")) {
    let body = part, step = 1;
    if (part.includes("/")) { const [a, b] = part.split("/"); body = a; step = parseInt(b, 10); }
    let lo, hi;
    const norm = (x) => { const xl = x.trim().toLowerCase(); return nameMap && nameMap[xl] !== undefined ? nameMap[xl] : parseInt(x, 10); };
    if (body === "*") { lo = min; hi = max; }
    else if (body.includes("-")) { const [l, r] = body.split("-"); lo = norm(l); hi = norm(r); }
    else { lo = norm(body); hi = part.includes("/") ? max : lo; }
    if (isNaN(lo) || isNaN(hi) || isNaN(step) || step < 1 || lo < min || hi > max || lo > hi) throw new Error(part);
    for (let i = lo; i <= hi; i += step) set.add(i);
  }
  return set;
}
function cronSetLabel(set, min, max, names) {
  if (set.size === max - min + 1) return "every " + names.unit;
  const arr = [...set].sort((a, b) => a - b);
  const list = arr.slice(0, 10).map((v) => names.fmt ? names.fmt(v) : v).join(", ");
  return (names.prefix || "") + list + (arr.length > 10 ? " \u2026 (" + arr.length + " values)" : "");
}
function cronExplain() {
  const v = document.getElementById("cr-in").value.trim();
  const parts = v.split(/\s+/);
  const el = document.getElementById("cr-out"), nextEl = document.getElementById("cr-next");
  nextEl.innerHTML = "";
  if (!v) { el.innerHTML = ""; return; }
  if (parts.length !== 5) { el.innerHTML = "<span class='error'>Enter exactly 5 fields: minute, hour, day-of-month, month, day-of-week.</span>"; return; }
  try {
    const M = cronParseField(parts[0], 0, 59);
    const H = cronParseField(parts[1], 0, 23);
    const DOM = cronParseField(parts[2], 1, 31);
    const MON = cronParseField(parts[3], 1, 12, CRON_MON);
    const DOW = cronParseField(parts[4], 0, 6, CRON_DOW);
    const rows = [
      ["Minute", cronSetLabel(M, 0, 59, { unit: "minute" })],
      ["Hour", cronSetLabel(H, 0, 23, { unit: "hour" })],
      ["Day of month", cronSetLabel(DOM, 1, 31, { unit: "day", prefix: "day " })],
      ["Month", cronSetLabel(MON, 1, 12, { unit: "month", fmt: (v) => CRON_MON_NAMES[v - 1] })],
      ["Day of week", cronSetLabel(DOW, 0, 6, { unit: "day of week", fmt: (v) => CRON_DOW_NAMES[v] })],
    ];
    if (parts[2] !== "*" && parts[4] !== "*") rows.push(["Note", "Both day fields are restricted \u2014 the job runs when EITHER matches (standard cron OR rule)."]);
    el.innerHTML = `<table class="wc-table"><tbody>` + rows.map(([k, val]) => `<tr><th>${k}</th><td>${escHtml(val)}</td></tr>`).join("") + `</tbody></table>`;
    const domR = parts[2] !== "*", dowR = parts[4] !== "*";
    const d = new Date();
    d.setSeconds(0, 0); d.setMinutes(d.getMinutes() + 1);
    const runs = [];
    for (let i = 0; i < 366 * 24 * 60 && runs.length < 5; i++) {
      const domOk = DOM.has(d.getDate()), dowOk = DOW.has(d.getDay());
      const dayOk = domR && dowR ? (domOk || dowOk) : (domOk && dowOk);
      if (M.has(d.getMinutes()) && H.has(d.getHours()) && MON.has(d.getMonth() + 1) && dayOk) runs.push(new Date(d));
      d.setMinutes(d.getMinutes() + 1);
    }
    nextEl.innerHTML = runs.length
      ? "<ul>" + runs.map((r) => "<li>" + r.toLocaleString() + "</li>").join("") + "</ul>"
      : "No future runs \u2014 the fields describe a moment that never occurs.";
  } catch (err) {
    el.innerHTML = "<span class='error'>Invalid value in field: " + escHtml(String(err.message)) + "</span>";
  }
}

/* ---- CSS Gradient Generator ---- */
function grDraw() {
  const c1 = document.getElementById("gr-c1").value, c2 = document.getElementById("gr-c2").value, a = document.getElementById("gr-ang").value;
  document.getElementById("gr-angv").textContent = a;
  document.getElementById("gr-prev").style.background = `linear-gradient(${a}deg, ${c1}, ${c2})`;
  document.getElementById("gr-out").value = `background: linear-gradient(${a}deg, ${c1}, ${c2});`;
}

/* ---- Box Shadow Generator ---- */
function bsDraw() {
  const g = (id) => document.getElementById(id);
  const x = g("bs-x").value, y = g("bs-y").value, bl = g("bs-bl").value, sp = g("bs-sp").value;
  g("bs-xv").textContent = x; g("bs-yv").textContent = y; g("bs-blv").textContent = bl; g("bs-spv").textContent = sp;
  const opv = g("bs-op").value; g("bs-opv").textContent = opv;
  const n = parseInt(g("bs-color").value.slice(1), 16);
  const v = (g("bs-inset").checked ? "inset " : "") + `${x}px ${y}px ${bl}px ${sp}px rgba(${(n >> 16) & 255}, ${(n >> 8) & 255}, ${n & 255}, ${(opv / 100).toFixed(2)})`;
  g("bs-box").style.boxShadow = v;
  g("bs-out").value = `box-shadow: ${v};`;
}

/* ---- Text to Speech ---- */
let ttsVoices = [];
function ttsLoad() {
  if (!("speechSynthesis" in window)) return;
  ttsVoices = speechSynthesis.getVoices();
  const sel = document.getElementById("tts-voice");
  if (sel) sel.innerHTML = ttsVoices.map((v, i) => `<option value="${i}">${escHtml(v.name)} (${escHtml(v.lang)})</option>`).join("");
}
if ("speechSynthesis" in window) { ttsLoad(); speechSynthesis.onvoiceschanged = ttsLoad; }
function ttsPlay() {
  if (!("speechSynthesis" in window)) { out("tts-msg", "<span class='error'>Your browser does not support speech synthesis.</span>"); return; }
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(document.getElementById("tts-in").value);
  const v = ttsVoices[+document.getElementById("tts-voice").value];
  if (v) u.voice = v;
  u.rate = +document.getElementById("tts-rate").value;
  u.pitch = +document.getElementById("tts-pitch").value;
  speechSynthesis.speak(u);
}
function ttsStop() { if ("speechSynthesis" in window) speechSynthesis.cancel(); }

/* ---- Typing Speed Test ---- */
const TY_WORDS = "the of and to in is you that it he was for on are as with his they at be this have from or one had by word but not what all were we when your can said there use an each which she do how their if will up other about out many then them these so some her would make like him into time has look two more write go see number no way could people my than first water been call who oil its now find long down day did get come made may part".split(" ");
let tyList = [], tyIdx = 0, tyStart = 0, tyDone = false, tyErrChars = 0, tyTyped = 0;
function tyRender() {
  document.getElementById("ty-words").innerHTML = tyList
    .map((w, i) => `<span class="ty-w${i < tyIdx ? " ty-done" : i === tyIdx ? " ty-act" : ""}">${w}</span>`)
    .join(" ");
}
function tyNew() {
  tyList = Array.from({ length: 25 }, () => TY_WORDS[Math.floor(Math.random() * TY_WORDS.length)]);
  tyIdx = 0; tyStart = 0; tyDone = false; tyErrChars = 0; tyTyped = 0;
  tyRender();
  document.getElementById("ty-in").value = "";
  document.getElementById("ty-stats").innerHTML = "";
}
function tyInput() {
  const inp = document.getElementById("ty-in");
  if (tyDone) return;
  if (!tyStart) tyStart = Date.now();
  const v = inp.value;
  if (v.endsWith(" ")) {
    const word = v.trim();
    tyTyped += word.length + 1;
    if (word !== tyList[tyIdx]) tyErrChars += word.length + 1;
    tyIdx++;
    inp.value = "";
    if (tyIdx >= tyList.length) { tyDone = true; tyRender(); tyFinish(); return; }
  }
  tyRender();
}
function tyFinish() {
  const mins = (Date.now() - tyStart) / 60000;
  const correct = Math.max(0, tyTyped - tyErrChars);
  const wpm = mins > 0 ? Math.round(correct / 5 / mins) : 0;
  const acc = tyTyped ? Math.round(100 * correct / tyTyped) : 0;
  document.getElementById("ty-stats").innerHTML =
    `<div class="stat"><b>${wpm}</b><span>Words per minute</span></div>
     <div class="stat"><b>${acc}%</b><span>Accuracy</span></div>
     <div class="stat"><b>${((Date.now() - tyStart) / 1000).toFixed(1)}s</b><span>Time</span></div>`;
}

/* ---- Pomodoro Timer ---- */
const PO_LEN = { focus: 25 * 60000, short: 5 * 60000, long: 15 * 60000 };
let poPhase = "focus", poEnd = 0, poTimer = null, poCount = 0, poLeft = 0, poRun = false;
function poFmt(ms) {
  const s = Math.max(0, Math.ceil(ms / 1000));
  return String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
}
function poLabel() { return poPhase === "focus" ? "Focus session" : poPhase === "short" ? "Short break" : "Long break"; }
function poTick() {
  const left = poEnd - Date.now();
  if (left <= 0) { poNext(); return; }
  document.getElementById("po-display").textContent = poFmt(left);
}
function poNext() {
  if (poPhase === "focus") {
    poCount++;
    poPhase = poCount % 4 === 0 ? "long" : "short";
    document.getElementById("po-count").textContent = "Completed focus sessions: " + poCount;
  } else poPhase = "focus";
  poEnd = Date.now() + PO_LEN[poPhase];
  document.getElementById("po-mode").textContent = poLabel();
  poTick();
}
function poToggle() {
  const btn = document.getElementById("po-start");
  if (poRun) {
    poLeft = poEnd - Date.now();
    clearInterval(poTimer); poRun = false; btn.textContent = "Resume";
  } else {
    poEnd = Date.now() + (poLeft > 0 ? poLeft : PO_LEN[poPhase]);
    clearInterval(poTimer); poTimer = setInterval(poTick, 250); poRun = true; btn.textContent = "Pause";
  }
}
function poSkip() {
  if (poRun) poEnd = Date.now();
  else { poLeft = 0; poNext(); }
}
function poReset() {
  clearInterval(poTimer);
  poRun = false; poPhase = "focus"; poCount = 0; poLeft = 0;
  document.getElementById("po-display").textContent = "25:00";
  document.getElementById("po-mode").textContent = "Focus session";
  document.getElementById("po-count").textContent = "Completed focus sessions: 0";
  document.getElementById("po-start").textContent = "Start";
}

/* ---- URL Parser ---- */
function urlParse() {
  const v = document.getElementById("up-in").value.trim();
  const el = document.getElementById("up-out");
  if (!v) { el.innerHTML = ""; return; }
  let u;
  try { u = new URL(v); }
  catch (e) { el.innerHTML = "<span class='error'>Not a valid absolute URL \u2014 include the https:// part.</span>"; return; }
  const rows = [
    ["Protocol", u.protocol.replace(":", "")],
    ["Username", u.username || "\u2014"],
    ["Password", u.password ? "(present)" : "\u2014"],
    ["Hostname", u.hostname],
    ["Port", u.port || (u.protocol === "https:" ? "443 (default)" : "80 (default)")],
    ["Path", u.pathname],
    ["Origin", u.origin],
    ["Fragment", u.hash ? u.hash.slice(1) : "\u2014"],
  ];
  let params = "";
  if (u.search) {
    const entries = [...u.searchParams.entries()];
    params = "<label>Query parameters (decoded)</label>" + entries
      .map(([k, val]) => `<div class="up-param"><b>${escHtml(k)}</b> = ${escHtml(val)}</div>`).join("");
  }
  el.innerHTML = `<table class="wc-table"><tbody>` + rows.map(([k, val]) => `<tr><th>${k}</th><td>${escHtml(String(val))}</td></tr>`).join("") + `</tbody></table>` + params;
}

/* Initial render for tools that need it */
(function () {
  if (document.getElementById("gr-prev")) grDraw();
  if (document.getElementById("bs-box")) bsDraw();
  if (document.getElementById("ty-words")) tyNew();
})();

/* ================= MEGA engines (converters, calculators, text, color, random, date) ================= */
function _n(id) { var el = $(id); if (!el) return null; var v = parseFloat(el.value); return isNaN(v) ? null : v; }
function _v(id) { var el = $(id); return el ? el.value.trim() : ""; }
function nfmt(v, d) {
  if (v === null || v === undefined || !isFinite(v)) return "\u2014";
  if (d === undefined) d = 2;
  var a = Math.abs(v);
  if (a !== 0 && (a < 0.001 || a >= 1e12)) return v.toExponential(4);
  return v.toLocaleString(undefined, { maximumFractionDigits: d });
}
function dISO(d) { return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); }
function pISO(s) { var p = s.split("-"); return new Date(+p[0], +p[1] - 1, +p[2]); }
function gcdJS(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) { var t = b; b = a % b; a = t; } return a; }

/* ---------- Unit converter engine (window.UC_CONF) ---------- */
function ucConv(v, k, f) {
  if (k === "c2f") return v * 9 / 5 + 32;
  if (k === "f2c") return (v - 32) * 5 / 9;
  if (k === "c2k") return v + 273.15;
  if (k === "f2k") return (v - 32) * 5 / 9 + 273.15;
  return v * f;
}
function ucInvV(v, k, f) {
  if (k === "c2f") return (v - 32) * 5 / 9;
  if (k === "f2c") return v * 9 / 5 + 32;
  if (k === "c2k") return v - 273.15;
  if (k === "f2k") return (v - 273.15) * 9 / 5 + 32;
  return v / f;
}
function ucRun() {
  var c = window.UC_CONF; if (!c) return;
  var a = $("uc-in"), b = $("uc-out"); if (!a || !b) return;
  var v = parseFloat(a.value);
  if (isNaN(v)) { b.value = ""; ucTable(); return; }
  b.value = c.d === "b" ? nfmt(ucInvV(v, c.k, c.f), 6) : nfmt(ucConv(v, c.k, c.f), 6);
  ucTable();
}
function ucTable() {
  var c = window.UC_CONF; if (!c) return;
  var t = $("uc-table"); if (!t) return;
  var vals = [1, 2, 5, 10, 25, 50, 100, 250, 500, 1000];
  var la = c.d === "a" ? c.fl : c.tl, lb = c.d === "a" ? c.tl : c.fl;
  var h = "<tr><th>" + escHtml(la) + "</th><th>" + escHtml(lb) + "</th></tr>";
  for (var i = 0; i < vals.length; i++) {
    var x = vals[i];
    var y = c.d === "a" ? ucConv(x, c.k, c.f) : ucInvV(x, c.k, c.f);
    h += "<tr><td>" + nfmt(x, 2) + "</td><td><b>" + nfmt(y, 4) + "</b></td></tr>";
  }
  t.innerHTML = h;
}
function ucSwap() {
  var c = window.UC_CONF; if (!c) return;
  var fl = $("uc-fl"), tl = $("uc-tl"); if (!fl || !tl) return;
  var tmp = fl.textContent; fl.textContent = tl.textContent; tl.textContent = tmp;
  c.d = c.d === "a" ? "b" : "a";
  var a = $("uc-in"), b = $("uc-out");
  if (b.value !== "" && !isNaN(parseFloat(b.value.replace(/,/g, "")))) a.value = b.value.replace(/,/g, "");
  ucRun();
}
function ucCopy() { var b = $("uc-out"); if (b && b.value) copyText(b.value, $("uc-copy")); }

/* ---------- Calculator engine (22 tools) ---------- */
function si() { var p = _n("si-p"), r = _n("si-r"), t = _n("si-t");
  if (p === null || r === null || t === null) { out("si-out", "Fill in all three fields."); return; }
  var i = p * r * t / 100;
  out("si-out", "Interest: <b>" + nfmt(i) + "</b><br>Total amount: <b>" + nfmt(p + i) + "</b><br>Interest per year: " + nfmt(t ? i / t : 0)); }
function avg() { var raw = _v("avg-n"); if (!raw) { out("avg-out", "Enter some numbers first."); return; }
  var parts = raw.split(/[\n,;]+/).map(parseFloat).filter(function (x) { return !isNaN(x); });
  if (!parts.length) { out("avg-out", "No valid numbers found.", "err"); return; }
  var s = 0; for (var i = 0; i < parts.length; i++) s += parts[i];
  out("avg-out", "Average: <b>" + nfmt(s / parts.length, 4) + "</b><br>Sum: " + nfmt(s, 4) + " &nbsp;\u00b7&nbsp; Count: " + parts.length + " &nbsp;\u00b7&nbsp; Min: " + nfmt(Math.min.apply(null, parts), 4) + " &nbsp;\u00b7&nbsp; Max: " + nfmt(Math.max.apply(null, parts), 4)); }
function sqrt() { var v = _n("sqrt-n"); if (v === null) { out("sqrt-out", "Enter a number."); return; }
  if (v < 0) { out("sqrt-out", "Negative numbers have no real square root (they need complex numbers).", "err"); return; }
  var r = Math.sqrt(v);
  out("sqrt-out", "\u221a" + nfmt(v, 6) + " = <b>" + nfmt(r, 6) + "</b><br>Check: " + nfmt(r, 6) + " \u00d7 " + nfmt(r, 6) + " = " + nfmt(r * r, 6)); }
function pow() { var b = _n("pw-b"), e = _n("pw-e"); if (b === null || e === null) { out("pow-out", "Enter both base and exponent."); return; }
  var r = Math.pow(b, e);
  if (!isFinite(r)) { out("pow-out", "Result is too large to represent.", "err"); return; }
  out("pow-out", nfmt(b, 6) + "<sup>" + nfmt(e, 6) + "</sup> = <b>" + nfmt(r, 6) + "</b>" + (e < 0 ? "<br><span class=\"dim\">Negative exponent: one over the positive power.</span>" : "")); }
function cirA() { var r = _n("cir-r"); if (r === null) { out("cirA-out", "Enter a radius."); return; }
  out("cirA-out", "Area = \u03c0 \u00d7 r\u00b2 = <b>" + nfmt(Math.PI * r * r, 4) + "</b> square units<br>(diameter " + nfmt(2 * r, 4) + ", circumference " + nfmt(2 * Math.PI * r, 4) + ")"); }
function cirC() { var r = _n("ccm-r"); if (r === null) { out("cirC-out", "Enter a radius."); return; }
  out("cirC-out", "Circumference = 2\u03c0r = <b>" + nfmt(2 * Math.PI * r, 4) + "</b> units<br>(area " + nfmt(Math.PI * r * r, 4) + ")"); }
function triA() { var b = _n("tri-b"), h = _n("tri-h"); if (b === null || h === null) { out("triA-out", "Enter base and height."); return; }
  out("triA-out", "Area = \u00bd \u00d7 " + nfmt(b) + " \u00d7 " + nfmt(h) + " = <b>" + nfmt(0.5 * b * h, 4) + "</b> square units"); }
function rectA() { var w = _n("rec-w"), h = _n("rec-h"); if (w === null || h === null) { out("rectA-out", "Enter width and height."); return; }
  out("rectA-out", "Area = <b>" + nfmt(w * h, 4) + "</b> square units<br>Perimeter = " + nfmt(2 * (w + h), 4) + " units"); }
function facCalc() { var n = _n("fac-n"); if (n === null || n < 0 || Math.floor(n) !== n) { out("facCalc-out", "Enter a whole number \u2265 0.", "err"); return; }
  if (n > 170) { out("facCalc-out", "170! is the largest factorial JavaScript can represent \u2014 try a smaller n.", "err"); return; }
  var r = 1; for (var i = 2; i <= n; i++) r *= i;
  out("facCalc-out", n + "! = <b>" + nfmt(r, 6) + "</b>" + (n > 20 ? "<br><span class=\"dim\">(" + r.toExponential(6).split("e")[0] + " \u00d7 10^" + r.toExponential(6).split("e")[1] + ")</span>" : "")); }
function gcdCalc() { var a = _n("gcd-a"), b = _n("gcd-b"); if (a === null || b === null || !a || !b) { out("gcdCalc-out", "Enter two non-zero whole numbers.", "err"); return; }
  a = Math.round(Math.abs(a)); b = Math.round(Math.abs(b));
  var g = gcdJS(a, b), l = (a / g) * b;
  out("gcdCalc-out", "GCD(" + a + ", " + b + ") = <b>" + g + "</b><br>LCM(" + a + ", " + b + ") = <b>" + nfmt(l, 0) + "</b>"); }
function primeCalc() { var v = _n("pr-n"); if (v === null || Math.floor(v) !== v || v < 2) { out("primeCalc-out", "Enter a whole number \u2265 2.", "err"); return; }
  var f = 0; for (var i = 2; i * i <= v; i++) { if (v % i === 0) { f = i; break; } }
  if (f) out("primeCalc-out", nfmt(v, 0) + " is <b>not prime</b> \u2014 it equals " + f + " \u00d7 " + (v / f));
  else out("primeCalc-out", nfmt(v, 0) + " is <b>prime</b> \u2014 divisible only by 1 and itself."); }
function n2wCalc() { var v = _n("n2w-n"); if (v === null || Math.floor(v) !== v) { out("n2wCalc-out", "Enter a whole number.", "err"); return; }
  out("n2wCalc-out", "<b>" + escHtml(n2wWords(v)) + "</b>" + (v < 0 ? "<br><span class=\"dim\">(negative \u2014 keep the minus in the written form)</span>" : "")); }
function n2wWords(num) {
  var ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
  var tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
  function u1000(n) { var s = ""; if (n >= 100) { s += ones[Math.floor(n / 100)] + " hundred"; n %= 100; if (n) s += " and "; }
    if (n >= 20) { s += tens[Math.floor(n / 10)]; if (n % 10) s += "-" + ones[n % 10]; } else if (n > 0) s += ones[n]; return s; }
  if (num === 0) return "zero";
  var neg = num < 0; num = Math.abs(num);
  var groups = [[1e12, "trillion"], [1e9, "billion"], [1e6, "million"], [1e3, "thousand"]];
  var s = "";
  for (var i = 0; i < groups.length; i++) { if (num >= groups[i][0]) { var q = Math.floor(num / groups[i][0]); s += u1000(q) + " " + groups[i][1]; num %= groups[i][0]; if (num) s += s ? " " : ""; } }
  if (num) s += (s ? " " : "") + u1000(num);
  return (neg ? "minus " : "") + s;
}
function quadCalc() { var a = _n("quad-a"), b = _n("quad-b"), c = _n("quad-c");
  if (a === null || b === null || c === null) { out("quadCalc-out", "Fill in a, b and c.", "err"); return; }
  if (a === 0) { out("quadCalc-out", "a = 0 makes this linear: root x = " + nfmt(-c / b, 6)); return; }
  var d = b * b - 4 * a * c;
  if (d > 0) { var r1 = (-b + Math.sqrt(d)) / (2 * a), r2 = (-b - Math.sqrt(d)) / (2 * a);
    out("quadCalc-out", "Discriminant: " + nfmt(d, 4) + " &gt; 0 \u2192 two real roots<br><b>x\u2081 = " + nfmt(r1, 6) + "</b> &nbsp;\u00b7&nbsp; <b>x\u2082 = " + nfmt(r2, 6) + "</b>"); }
  else if (d === 0) out("quadCalc-out", "Discriminant = 0 \u2192 one repeated root<br><b>x = " + nfmt(-b / (2 * a), 6) + "</b>");
  else out("quadCalc-out", "Discriminant " + nfmt(d, 4) + " &lt; 0 \u2192 no real roots (complex: " + nfmt(-b / (2 * a), 4) + " \u00b1 " + nfmt(Math.sqrt(-d) / (2 * a), 4) + "i)"); }
function arCalc() { var w = _n("ar-w"), h = _n("ar-h"), nw = _n("ar-nw");
  if (w === null || h === null || !w || !h) { out("arCalc-out", "Enter the original width and height.", "err"); return; }
  if (nw === null) { var nh = null; out("arCalc-out", "Ratio is " + gcdJS(Math.round(w), Math.round(h)) + ":" + (Math.round(h) / gcdJS(Math.round(w), Math.round(h))) + " \u2014 enter a new width or height to scale."); return; }
  var r = h / w;
  out("arCalc-out", "At " + nfmt(nw, 2) + " wide the height is <b>" + Math.round(nw * r) + " px</b><br>Ratio: " + (w / gcdJS(Math.round(w), Math.round(h))).toFixed(0) + ":" + (h / gcdJS(Math.round(w), Math.round(h))).toFixed(0)); }
function pmCalc() { var rev = _n("pm-rev"), cost = _n("pm-cost");
  if (rev === null || cost === null || !rev) { out("pmCalc-out", "Enter revenue and cost.", "err"); return; }
  var p = rev - cost;
  out("pmCalc-out", "Profit: <b>" + nfmt(p) + "</b><br>Margin: <b>" + nfmt(p / rev * 100) + "%</b> of price<br>Markup: " + nfmt(cost ? p / cost * 100 : 0) + "% on cost"); }
function logCalc() { var x = _n("log-x"), b = _n("log-b");
  if (x === null || b === null || x <= 0 || b <= 0 || b === 1) { out("logCalc-out", "Enter a positive number and a positive base \u2260 1.", "err"); return; }
  out("logCalc-out", "log<sub>" + nfmt(b, 4) + "</sub>(" + nfmt(x, 6) + ") = <b>" + nfmt(Math.log(x) / Math.log(b), 6) + "</b>"); }
function hrsCalc() { var s = _v("hr-sv"), e = _v("hr-ev");
  if (!s || !e) { out("hrsCalc-out", "Pick both a start and an end time.", "err"); return; }
  var sp = s.split(":"), ep = e.split(":");
  var mins = (+ep[0] * 60 + +ep[1]) - (+sp[0] * 60 + +sp[1]);
  if (mins < 0) mins += 1440;
  var br = _n("hr-br") || 0; mins -= br; if (mins < 0) mins = 0;
  out("hrsCalc-out", "<b>" + Math.floor(mins / 60) + "h " + String(mins % 60).padStart(2, "0") + "m</b> &nbsp;=&nbsp; " + (mins / 60).toFixed(2) + " decimal hours" + (br ? " <span class=\"dim\">(after a " + br + " min break)</span>" : "")); }
function fuelCalc() { var d = _n("fc-d"), e = _n("fc-e"), p = _n("fc-p");
  if (d === null || e === null || p === null) { out("fuelCalc-out", "Fill in distance, consumption and price.", "err"); return; }
  var l = d * e / 100;
  out("fuelCalc-out", "Fuel used: <b>" + nfmt(l) + " L</b><br>Trip cost: <b>" + nfmt(l * p) + "</b><br>Cost per km: " + nfmt(p * e / 100, 3)); }
function cbrtCalc() { var v = _n("cbrt-n"); if (v === null) { out("cbrtCalc-out", "Enter a number."); return; }
  var r = Math.cbrt(v);
  out("cbrtCalc-out", "\u221b" + nfmt(v, 6) + " = <b>" + nfmt(r, 6) + "</b><br>Check: " + nfmt(r, 6) + "\u00b3 = " + nfmt(r * r * r, 6)); }
function pctChCalc() { var o = _n("pc-old"), n2 = _n("pc-new");
  if (o === null || n2 === null || o === 0) { out("pctChCalc-out", "Enter both values (old value can't be zero).", "err"); return; }
  var ch = (n2 - o) / o * 100;
  out("pctChCalc-out", "Change: <b>" + (ch >= 0 ? "+" : "") + nfmt(ch) + "%</b><br>Difference: " + nfmt(n2 - o) + " &nbsp;\u00b7&nbsp; " + (ch >= 0 ? "increase" : "decrease")); }
function hypCalc() { var a = _n("hy-a"), b = _n("hy-b"); if (a === null || b === null) { out("hypCalc-out", "Enter both sides.", "err"); return; }
  var c = Math.sqrt(a * a + b * b);
  out("hypCalc-out", "Hypotenuse c = <b>" + nfmt(c, 6) + "</b><br>Check: " + nfmt(a) + "\u00b2 + " + nfmt(b) + "\u00b2 = " + nfmt(a * a + b * b, 4)); }
function ratioCalc() { var a = _n("rs-a"), b = _n("rs-b"); if (a === null || b === null || !a || !b) { out("ratioCalc-out", "Enter two non-zero numbers.", "err"); return; }
  var g = gcdJS(Math.round(a), Math.round(b));
  out("ratioCalc-out", "<b>" + Math.round(a / g) + " : " + Math.round(b / g) + "</b><br>Decimal: " + (a / b).toFixed(4) + " &nbsp;\u00b7&nbsp; Simplified by GCD " + g); }

/* ---------- Text engine (window.TX_CONF) ---------- */
var TX_ACC = { "\u00e1":"a","\u00e0":"a","\u00e2":"a","\u00e4":"a","\u00e3":"a","\u00e5":"a","\u00e9":"e","\u00e8":"e","\u00ea":"e","\u00eb":"e","\u00ed":"i","\u00ec":"i","\u00ee":"i","\u00ef":"i","\u00f3":"o","\u00f2":"o","\u00f4":"o","\u00f6":"o","\u00f5":"o","\u00fa":"u","\u00f9":"u","\u00fb":"u","\u00fc":"u","\u00f1":"n","\u00e7":"c","\u00fd":"y","\u0161":"s","\u017e":"z" };
function txRun() {
  var c = window.TX_CONF; if (!c) return;
  var t = $("tx-in").value; if ($("tx-in") === null) return;
  var r = "", i, lines, m;
  switch (c.op) {
    case "spaces":
      r = t.replace(/[ \t]+/g, " ").split("\n").map(function (l) { return l.trim(); }).join("\n").replace(/\n{3,}/g, "\n\n");
      break;
    case "linebreaks":
      r = t.split(/\n+/).map(function (l) { return l.trim(); }).filter(Boolean).join(" ");
      break;
    case "specialchars":
      r = t.replace(/[\u00c0-\u024f]/g, function (ch) { var lo = ch.toLowerCase(); var rep = TX_ACC[lo]; if (rep) return ch === lo ? rep : rep.toUpperCase(); return ch; })
           .replace(/[^A-Za-z0-9\s]/g, "");
      break;
    case "prefixsuffix":
      var pre = _v("tx-pre"), suf = _v("tx-suf");
      r = t.split("\n").filter(function (l) { return l.trim() !== ""; }).map(function (l) { return pre + l + suf; }).join("\n");
      break;
    case "emails":
      m = t.match(/[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}/g) || [];
      var seen = {}; var outl = [];
      for (i = 0; i < m.length; i++) { var k = m[i].toLowerCase(); if (!seen[k]) { seen[k] = 1; outl.push(m[i]); } }
      r = outl.length ? outl.join("\n") : "No email addresses found.";
      break;
    case "numbers":
      m = t.match(/-?\d+(?:\.\d+)?/g) || [];
      r = m.length ? m.join("\n") : "No numbers found.";
      break;
    case "urls":
      m = t.match(/https?:\/\/[^\s<>"')\]]+/g) || [];
      m = m.map(function (u) { return u.replace(/[.,;:!]+$/, ""); });
      var su = {}; var ou = [];
      for (i = 0; i < m.length; i++) { if (!su[m[i]]) { su[m[i]] = 1; ou.push(m[i]); } }
      r = ou.length ? ou.join("\n") : "No URLs found.";
      break;
    case "occurrences":
      var f = _v("tx-find");
      if (!f) { r = "Type the text to count in the field above."; break; }
      var cnt = 0, idx = 0, hay = t.toLowerCase(), needle = f.toLowerCase();
      while ((idx = hay.indexOf(needle, idx)) !== -1) { cnt++; idx += needle.length; }
      r = "\u201c" + f + "\u201d appears " + cnt + (cnt === 1 ? " time" : " times") + " in " + t.trim().split(/\s+/).filter(Boolean).length + " words of text.";
      break;
    case "columns":
      var d = _v("tx-delim") || ",";
      r = t.split("\n").filter(function (l) { return l.trim() !== ""; }).map(function (l) { return l.split(d).map(function (x2) { return x2.trim(); }).join("\t"); }).join("\n");
      break;
    case "join":
      var sep = ($("tx-sep") && $("tx-sep").value) || ", ";
      r = t.split("\n").filter(function (l) { return l.trim() !== ""; }).join(sep);
      break;
    case "linenumbers":
      lines = t.split("\n");
      r = lines.map(function (l, j) { return (j + 1) + ". " + l; }).join("\n");
      break;
    case "truncate":
      var len = _n("tx-len"); if (len === null || len < 1) { r = "Set a maximum character length first."; break; }
      r = t.length > len ? t.slice(0, Math.max(0, len - 1)) + "\u2026" : t;
      break;
    case "swapcase":
      r = t.replace(/[A-Za-z]/g, function (ch) { return ch === ch.toUpperCase() ? ch.toLowerCase() : ch.toUpperCase(); });
      break;
    case "altcase":
      var up = true;
      r = t.replace(/[A-Za-z]/g, function (ch) { var o = up ? ch.toUpperCase() : ch.toLowerCase(); up = !up; return o; });
      break;
    case "removenumbers":
      r = t.replace(/\d/g, "");
      break;
    default: r = t;
  }
  $("tx-out").value = r;
}
function txCopyOut() { var o = $("tx-out"); if (o && o.value) copyText(o.value); }
function txClear() { if ($("tx-in")) $("tx-in").value = ""; if ($("tx-out")) $("tx-out").value = ""; }

/* ---------- Color engine ---------- */
function cxParseHex(s) {
  s = (s || "").trim().replace(/^#/, "");
  if (/^[0-9a-fA-F]{3}$/.test(s)) s = s[0] + s[0] + s[1] + s[1] + s[2] + s[2];
  if (!/^[0-9a-fA-F]{6}$/.test(s)) return null;
  return { r: parseInt(s.slice(0, 2), 16), g: parseInt(s.slice(2, 4), 16), b: parseInt(s.slice(4, 6), 16), hex: "#" + s.toLowerCase() };
}
function cxToHex(r, g, b) {
  function h2(x) { return Math.round(Math.max(0, Math.min(255, x))).toString(16).padStart(2, "0"); }
  return "#" + h2(r) + h2(g) + h2(b);
}
function cxRgbToHsl(r, g, b) {
  r /= 255; g /= 255; b /= 255;
  var mx = Math.max(r, g, b), mn = Math.min(r, g, b), h = 0, s = 0, l = (mx + mn) / 2;
  if (mx !== mn) {
    var d = mx - mn;
    s = l > 0.5 ? d / (2 - mx - mn) : d / (mx + mn);
    if (mx === r) h = ((g - b) / d + (g < b ? 6 : 0));
    else if (mx === g) h = (b - r) / d + 2;
    else h = (r - g) / d + 4;
    h *= 60;
  }
  return { h: Math.round(h), s: Math.round(s * 100), l: Math.round(l * 100) };
}
function cxLum(r, g, b) {
  function ch(c) { c /= 255; return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); }
  return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b);
}
function cxMix(hex, target, amt) {
  var c = cxParseHex(hex); if (!c) return null;
  return cxToHex(c.r + (target.r - c.r) * amt, c.g + (target.g - c.g) * amt, c.b + (target.b - c.b) * amt);
}
function cxCopyVal(v, el) { copyText(v, el); }
function cxShades() {
  var hex = _v("sh-in"); var box = $("sh-out"); if (!box) return;
  var c = cxParseHex(hex);
  if (!c) { box.innerHTML = '<span class="dim">Enter a valid hex color like #e05e00.</span>'; return; }
  var white = { r: 255, g: 255, b: 255 }, black = { r: 0, g: 0, b: 0 };
  var h = "";
  for (var i = 5; i >= 1; i--) { var hx = cxMix(hex, white, i / 6); h += '<div class="shade-cell" style="background:' + hx + '" onclick="cxCopyVal(\'' + hx + '\', this)" title="' + hx + ' \u2014 click to copy"><span>' + hx + '</span></div>'; }
  h += '<div class="shade-cell base" style="background:' + c.hex + '" onclick="cxCopyVal(\'' + c.hex + '\', this)" title="' + c.hex + ' \u2014 click to copy"><span>' + c.hex + '</span></div>';
  for (i = 1; i <= 5; i++) { var hd = cxMix(hex, black, i / 6); h += '<div class="shade-cell" style="background:' + hd + '" onclick="cxCopyVal(\'' + hd + '\', this)" title="' + hd + ' \u2014 click to copy"><span>' + hd + '</span></div>'; }
  box.innerHTML = h;
}
function cxComp() {
  var hex = _v("cp-in"); var o = $("cp-out"), p = $("cp-prev");
  var c = cxParseHex(hex);
  if (!c) { if (o) o.innerHTML = '<span class="dim">Enter a valid hex color.</span>'; return; }
  var hsl = cxRgbToHsl(c.r, c.g, c.b);
  function hslHex(h2, s, l) {
    s /= 100; l /= 100;
    function f(n) { var k = (n + h2 / 30) % 12; var a = s * Math.min(l, 1 - l); return l - a * Math.max(-1, Math.min(k - 3, 9 - k, 1)); }
    return cxToHex(f(0) * 255, f(8) * 255, f(4) * 255);
  }
  var comp = hslHex((hsl.h + 180) % 360, hsl.s, hsl.l);
  var sp1 = hslHex((hsl.h + 150) % 360, hsl.s, hsl.l);
  var sp2 = hslHex((hsl.h + 210) % 360, hsl.s, hsl.l);
  o.innerHTML = "Complement: <b>" + comp + "</b> &nbsp;\u00b7&nbsp; Split: " + sp1 + " and " + sp2;
  p.innerHTML = '<div class="shade-cell" style="background:' + c.hex + '" onclick="cxCopyVal(\'' + c.hex + '\', this)" title="' + c.hex + '"><span>' + c.hex + '</span></div>'
    + '<div class="shade-cell" style="background:' + comp + '" onclick="cxCopyVal(\'' + comp + '\', this)" title="' + comp + '"><span>' + comp + '</span></div>'
    + '<div class="shade-cell" style="background:' + sp1 + '" onclick="cxCopyVal(\'' + sp1 + '\', this)" title="' + sp1 + '"><span>' + sp1 + '</span></div>'
    + '<div class="shade-cell" style="background:' + sp2 + '" onclick="cxCopyVal(\'' + sp2 + '\', this)" title="' + sp2 + '"><span>' + sp2 + '</span></div>';
}
function cxContrast() {
  var fg = cxParseHex(_v("ct-fg")), bg = cxParseHex(_v("ct-bg"));
  var o = $("ct-out"), p = $("ct-prev");
  if (!fg || !bg) { if (o) o.innerHTML = '<span class="dim">Enter two valid hex colors.</span>'; return; }
  var l1 = cxLum(fg.r, fg.g, fg.b), l2 = cxLum(bg.r, bg.g, bg.b);
  var ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
  function pass(v, th) { return v >= th ? '<span class="pass">Pass</span>' : '<span class="fail">Fail</span>'; }
  o.innerHTML = "Contrast ratio: <b>" + ratio.toFixed(2) + ":1</b><br>"
    + "AA normal text (4.5:1): " + pass(ratio, 4.5) + " &nbsp;\u00b7&nbsp; AA large text (3:1): " + pass(ratio, 3)
    + "<br>AAA normal (7:1): " + pass(ratio, 7) + " &nbsp;\u00b7&nbsp; AAA large (4.5:1): " + pass(ratio, 4.5);
  p.style.color = fg.hex; p.style.background = bg.hex;
}
function cxRandom() {
  var hx = cxToHex(Math.floor(Math.random() * 256), Math.floor(Math.random() * 256), Math.floor(Math.random() * 256));
  var c = cxParseHex(hx), hsl = cxRgbToHsl(c.r, c.g, c.b);
  out("rn-out", "<b>" + hx + "</b> &nbsp;\u00b7&nbsp; rgb(" + c.r + ", " + c.g + ", " + c.b + ") &nbsp;\u00b7&nbsp; hsl(" + hsl.h + ", " + hsl.s + "%, " + hsl.l + "%)");
  $("rn-prev").style.background = hx;
}
function cxInvert() {
  var c = cxParseHex(_v("iv-in")); var o = $("iv-out"), p = $("iv-prev");
  if (!c) { if (o) o.innerHTML = '<span class="dim">Enter a valid hex color.</span>'; return; }
  var inv = cxToHex(255 - c.r, 255 - c.g, 255 - c.b);
  o.innerHTML = "Inverted: <b>" + inv + "</b> &nbsp;\u00b7&nbsp; rgb(" + (255 - c.r) + ", " + (255 - c.g) + ", " + (255 - c.b) + ")";
  p.innerHTML = '<div class="shade-cell" style="background:' + c.hex + '" title="' + c.hex + '"><span>' + c.hex + '</span></div>'
    + '<div class="shade-cell" style="background:' + inv + '" onclick="cxCopyVal(\'' + inv + '\', this)" title="' + inv + '"><span>' + inv + '</span></div>';
}
function cxGray() {
  var c = cxParseHex(_v("gs-in")); var o = $("gs-out"), p = $("gs-prev");
  if (!c) { if (o) o.innerHTML = '<span class="dim">Enter a valid hex color.</span>'; return; }
  var y = Math.round(0.299 * c.r + 0.587 * c.g + 0.114 * c.b);
  var g = cxToHex(y, y, y);
  o.innerHTML = "Grayscale: <b>" + g + "</b> &nbsp;\u00b7&nbsp; luminance level " + y + "/255";
  p.innerHTML = '<div class="shade-cell" style="background:' + c.hex + '" title="' + c.hex + '"><span>' + c.hex + '</span></div>'
    + '<div class="shade-cell" style="background:' + g + '" onclick="cxCopyVal(\'' + g + '\', this)" title="' + g + '"><span>' + g + '</span></div>';
}
function cxHex() {
  var c = cxParseHex(_v("cx-in")); var o = $("cx-out"), p = $("cx-prev");
  if (!c) { if (o) o.innerHTML = '<span class="dim">Enter a valid hex color.</span>'; return; }
  if (p) p.style.background = c.hex;
  if (o) o.innerHTML = "RGB: <b>rgb(" + c.r + ", " + c.g + ", " + c.b + ")</b><br>Channels: R " + c.r + " &nbsp;\u00b7&nbsp; G " + c.g + " &nbsp;\u00b7&nbsp; B " + c.b;
}
function cxRgb() { var r = _n("cr-r"), g = _n("cr-g"), b = _n("cr-b"); var o = $("cr-out"), p = $("cr-prev");
  if (r === null || g === null || b === null) { if (o) o.innerHTML = '<span class="dim">Enter all three channels.</span>'; return; }
  var hx = cxToHex(r, g, b); if (p) p.style.background = hx;
  if (o) o.innerHTML = "HEX: <b>" + hx + "</b>"; }
function cxHexHsl() { var c = cxParseHex(_v("ch-in")); var o = $("ch-out"), p = $("ch-prev");
  if (!c) { if (o) o.innerHTML = '<span class="dim">Enter a valid hex color.</span>'; return; }
  var hsl = cxRgbToHsl(c.r, c.g, c.b); if (p) p.style.background = c.hex;
  if (o) o.innerHTML = "HSL: <b>hsl(" + hsl.h + ", " + hsl.s + "%, " + hsl.l + "%)</b><br>Hue " + hsl.h + "\u00b0 &nbsp;\u00b7&nbsp; Saturation " + hsl.s + "% &nbsp;\u00b7&nbsp; Lightness " + hsl.l + "%"; }
function cxRgbHsl() { var r = _n("rh-r"), g = _n("rh-g"), b = _n("rh-b"); var o = $("rh-out"), p = $("rh-prev");
  if (r === null || g === null || b === null) { if (o) o.innerHTML = '<span class="dim">Enter all three channels.</span>'; return; }
  var hsl = cxRgbToHsl(r, g, b); if (p) p.style.background = cxToHex(r, g, b);
  if (o) o.innerHTML = "HSL: <b>hsl(" + hsl.h + ", " + hsl.s + "%, " + hsl.l + "%)</b>"; }
function cxCopy(kind) {
  if (kind === "rgb") { var c = cxParseHex(_v("cx-in")); if (c) copyText("rgb(" + c.r + ", " + c.g + ", " + c.b + ")"); }
  else if (kind === "hex") { var r = _n("cr-r"), g = _n("cr-g"), b = _n("cr-b"); if (r !== null && g !== null && b !== null) copyText(cxToHex(r, g, b)); }
  else if (kind === "hsl") { var t = $("ch-out") || $("rh-out"); if (t) { var m = t.innerHTML.match(/hsl\([^)]+\)/); if (m) copyText(m[0]); } }
  else if (kind === "all") { var t2 = $("rn-out"); if (t2) copyText(t2.textContent); }
}

/* ---------- Random engine ---------- */
var RN_WORDS = "time,year,people,way,day,man,thing,woman,life,child,world,school,state,family,student,group,country,problem,hand,part,place,case,week,company,system,program,question,work,government,number,night,point,home,water,room,mother,area,money,story,fact,month,lot,right,study,book,eye,job,word,business,issue,side,kind,head,house,service,friend,father,power,hour,game,line,end,member,law,car,city,name,team,minute,idea,body,back,parent,face,others,level,office,door,health,person,art,war,history,party,result,change,morning,reason,research,girl,guy,moment,air,teacher,force,education".split(",");
var RN_COUNTRIES = ["Argentina|South America","Australia|Oceania","Austria|Europe","Belgium|Europe","Brazil|South America","Canada|North America","Chile|South America","China|Asia","Colombia|South America","Croatia|Europe","Czechia|Europe","Denmark|Europe","Egypt|Africa","Estonia|Europe","Finland|Europe","France|Europe","Germany|Europe","Greece|Europe","Hungary|Europe","Iceland|Europe","India|Asia","Indonesia|Asia","Ireland|Europe","Israel|Asia","Italy|Europe","Japan|Asia","Kenya|Africa","Latvia|Europe","Lithuania|Europe","Malaysia|Asia","Mexico|North America","Morocco|Africa","Netherlands|Europe","New Zealand|Oceania","Nigeria|Africa","Norway|Europe","Peru|South America","Philippines|Asia","Poland|Europe","Portugal|Europe","Romania|Europe","Saudi Arabia|Asia","Singapore|Asia","Slovakia|Europe","Slovenia|Europe","South Africa|Africa","South Korea|Asia","Spain|Europe","Sweden|Europe","Switzerland|Europe","Thailand|Asia","Turkey|Asia","Ukraine|Europe","United Arab Emirates|Asia","United Kingdom|Europe","United States|North America","Uruguay|South America","Vietnam|Asia"];
var RN_QUOTES = [["Simplicity is the ultimate sophistication.","Leonardo da Vinci"],["The best way to predict the future is to invent it.","Alan Kay"],["Well begun is half done.","Aristotle"],["Make it work, make it right, make it fast.","Kent Beck"],["Quality is not an act, it is a habit.","Aristotle"],["What we know is a drop, what we don't know is an ocean.","Isaac Newton"],["The details are not the details. They make the design.","Charles Eames"],["Talk is cheap. Show me the code.","Linus Torvalds"],["Perfection is achieved when there is nothing left to take away.","Antoine de Saint-Exup\u00e9ry"],["The scariest moment is always just before you start.","Stephen King"],["First, solve the problem. Then, write the code.","John Johnson"],["Everything should be made as simple as possible, but not simpler.","Albert Einstein"],["Practice does not make perfect. Only perfect practice makes perfect.","Vince Lombardi"],["Small deeds done are better than great deeds planned.","Peter Marshall"],["If I had nine hours to chop a tree, I'd spend the first six sharpening my axe.","Abraham Lincoln"],["It always seems impossible until it is done.","Nelson Mandela"]];
function rnLetter() { var n = Math.min(50, Math.max(1, _n("rl-n") || 5)); var up = ($("rl-case") && $("rl-case").value === "U");
  var s = []; for (var i = 0; i < n; i++) { var ch = String.fromCharCode(97 + Math.floor(Math.random() * 26)); s.push(up ? ch.toUpperCase() : ch); }
  out("rl-out", "<b>" + s.join(" &nbsp; ") + "</b>"); }
function rnWord() { var n = Math.min(20, Math.max(1, _n("rw-n") || 3)); var s = [];
  for (var i = 0; i < n; i++) s.push(RN_WORDS[Math.floor(Math.random() * RN_WORDS.length)]);
  out("rw-out", "<b>" + s.join(" &nbsp;\u00b7&nbsp; ") + "</b>"); }
function rnDate() { var a = _v("rd-a"), b = _v("rd-b");
  if (!a || !b) { out("rd-out", "Pick both a start and an end date.", "err"); return; }
  var t1 = pISO(a).getTime(), t2 = pISO(b).getTime();
  if (t2 < t1) { var tmp = t1; t1 = t2; t2 = tmp; }
  var d = new Date(t1 + Math.floor(Math.random() * (t2 - t1 + 86400000)));
  var days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
  out("rd-out", "<b>" + dISO(d) + "</b><br>" + days[d.getDay()] + ", " + d.toLocaleDateString(undefined, { year: "numeric", month: "long", day: "numeric" })); }
function rnShuffle() { var t = $("ls-in"); if (!t) return;
  var arr = t.value.split("\n").filter(function (l) { return l.trim() !== ""; });
  if (!arr.length) { $("ls-out").value = "Enter some list items first."; return; }
  for (var i = arr.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp; }
  $("ls-out").value = arr.join("\n"); }
function rnPick() { var t = $("np-in"); if (!t) return;
  var arr = t.value.split("\n").filter(function (l) { return l.trim() !== ""; });
  var k = Math.max(1, _n("np-n") || 1);
  if (!arr.length) { out("np-out", "Enter some names first.", "err"); return; }
  if (k > arr.length) k = arr.length;
  var pool = arr.slice();
  var win = [];
  for (var i = 0; i < k; i++) { var j = Math.floor(Math.random() * pool.length); win.push(pool[j]); pool.splice(j, 1); }
  out("np-out", "<b>" + escHtml(win.join(" \u00b7 ")) + "</b>" + (k > 1 ? "<br><span class=\"dim\">" + k + " winners from " + arr.length + " entries</span>" : "")); }
function rnYesNo() { out("yn-out", Math.random() < 0.5 ? "YES" : "NO", "huge-res"); }
function rnTeams() { var t = $("ts-in"); if (!t) return;
  var arr = t.value.split("\n").filter(function (l) { return l.trim() !== ""; });
  var k = Math.max(2, _n("ts-n") || 2);
  if (arr.length < k) { out("ts-out", "You need at least as many names as teams.", "err"); return; }
  for (var i = arr.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp; }
  var teams = []; for (i = 0; i < k; i++) teams.push([]);
  for (i = 0; i < arr.length; i++) teams[i % k].push(arr[i]);
  var h = "";
  for (i = 0; i < k; i++) h += "<div class=\"team-box\"><b>Team " + (i + 1) + "</b><br>" + escHtml(teams[i].join(", ")) + "</div>";
  out("ts-out", h); }
function rnLottery() { var n = Math.max(1, Math.min(20, _n("lt-n") || 6)); var mx = Math.max(2, _n("lt-max") || 59);
  if (n > mx) { out("lt-out", "You can't draw " + n + " unique numbers from a range of " + mx + ".", "err"); return; }
  var pool = []; for (var i = 1; i <= mx; i++) pool.push(i);
  var pick = [];
  for (i = 0; i < n; i++) { var j = Math.floor(Math.random() * pool.length); pick.push(pool[j]); pool.splice(j, 1); }
  pick.sort(function (a, b) { return a - b; });
  out("lt-out", "<b>" + pick.join(" \u00b7 ") + "</b>"); }
function rnCountry() { var p = RN_COUNTRIES[Math.floor(Math.random() * RN_COUNTRIES.length)].split("|");
  out("co-out", "<b>" + p[0] + "</b><br><span class=\"dim\">" + p[1] + "</span>"); }
function rnQuote() { var q = RN_QUOTES[Math.floor(Math.random() * RN_QUOTES.length)];
  out("qt-out", "\u201c" + q[0] + "\u201d<br><span class=\"dim\">\u2014 " + q[1] + "</span>"); }

/* ---------- Date engine ---------- */
function dtAddDays() { var d = _v("ad-date"), n = _n("ad-n");
  if (!d || n === null) { out("ad-out", "Pick a date and enter a number of days.", "err"); return; }
  var r = pISO(d); r.setDate(r.getDate() + n);
  var days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
  out("ad-out", "<b>" + dISO(r) + "</b><br>" + days[r.getDay()] + ", " + r.toLocaleDateString(undefined, { year: "numeric", month: "long", day: "numeric" })); }
function dtDow() { var d = _v("dw-date");
  if (!d) { out("dw-out", "Pick a date first.", "err"); return; }
  var r = pISO(d); var days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
  var start = new Date(r.getFullYear(), 0, 1);
  var doy = Math.floor((r - start) / 86400000) + 1;
  out("dw-out", "<b>" + days[r.getDay()] + "</b><br>" + r.toLocaleDateString(undefined, { year: "numeric", month: "long", day: "numeric" }) + " &nbsp;\u00b7&nbsp; day " + doy + " of " + r.getFullYear()); }
function dtWeekNum() { var d = _v("wn-date");
  if (!d) { out("wn-out", "Pick a date first.", "err"); return; }
  var r = pISO(d);
  var t = new Date(Date.UTC(r.getFullYear(), r.getMonth(), r.getDate()));
  var day = (t.getUTCDay() + 6) % 7;
  t.setUTCDate(t.getUTCDate() - day + 3);
  var firstThu = new Date(Date.UTC(t.getUTCFullYear(), 0, 4));
  var fd = (firstThu.getUTCDay() + 6) % 7;
  firstThu.setUTCDate(firstThu.getUTCDate() - fd + 3);
  var wk = 1 + Math.round((t - firstThu) / (7 * 86400000));
  out("wn-out", "<b>Week " + wk + "</b> of " + t.getUTCFullYear() + "<br><span class=\"dim\">ISO-8601 numbering (weeks start Monday; week 1 holds the first Thursday)</span>"); }
function dtLeap() { var y = _n("lp-y");
  if (y === null || Math.floor(y) !== y) { out("lp-out", "Enter a whole year.", "err"); return; }
  var isL = (y % 4 === 0 && y % 100 !== 0) || (y % 400 === 0);
  var why = isL ? ((y % 400 === 0 && y % 100 === 0) ? "divisible by 400, so the century exception does not apply" : "divisible by 4 and not by 100") : ((y % 100 === 0) ? "a century year not divisible by 400" : "not divisible by 4");
  var next = [];
  var yy = y;
  while (next.length < 5) { yy++; if ((yy % 4 === 0 && yy % 100 !== 0) || yy % 400 === 0) next.push(yy); }
  out("lp-out", y + " is <b>" + (isL ? "a leap year" : "not a leap year") + "</b> \u2014 " + why + ".<br>February " + y + ": " + (isL ? 29 : 28) + " days<br>Next leap years: " + next.join(", ")); }
function dtS2Hms() { var s = _n("s2-sec");
  if (s === null || s < 0) { out("s2-out", "Enter a number of seconds (0 or more).", "err"); return; }
  s = Math.round(s);
  var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = s % 60;
  out("s2-out", "<b>" + h + ":" + String(m).padStart(2, "0") + ":" + String(sec).padStart(2, "0") + "</b><br>" + nfmt(h, 0) + " hours &nbsp;\u00b7&nbsp; " + m + " minutes &nbsp;\u00b7&nbsp; " + sec + " seconds"); }
function dtHms2S() { var h = _n("h2-h"), m = _n("h2-m"), s = _n("h2-s");
  if (h === null || m === null || s === null) { out("h2-out", "Enter all three fields (0 is fine).", "err"); return; }
  out("h2-out", "<b>" + nfmt(h * 3600 + m * 60 + s, 0) + "</b> seconds"); }
function dtMilitary() { var t = _v("mt-tv");
  if (!t) { out("mt-out", "Pick a time first.", "err"); return; }
  var p = t.split(":"), h = +p[0], m = +p[1];
  var ap = h >= 12 ? "PM" : "AM";
  var h12 = h % 12; if (h12 === 0) h12 = 12;
  out("mt-out", "<b>" + t + "</b> in 24-hour time = <b>" + h12 + ":" + String(m).padStart(2, "0") + " " + ap + "</b> in 12-hour time"); }
function dtMilRev() { var t = _v("mt24");
  var o = $("mt-out2"); if (!o) return;
  var m = t.match(/^\s*(\d{1,2}):(\d{2})\s*$/);
  if (!m) { o.innerHTML = '<span class="dim">Enter 24-hour time as HH:MM, e.g. 21:15.</span>'; return; }
  var h = +m[1], mi = +m[2];
  if (h > 23 || mi > 59) { o.innerHTML = '<span class="dim">Hours 0\u201323, minutes 0\u201359.</span>'; return; }
  var ap = h >= 12 ? "PM" : "AM";
  var h12 = h % 12; if (h12 === 0) h12 = 12;
  o.innerHTML = "<b>" + t + "</b> = <b>" + h12 + ":" + String(mi).padStart(2, "0") + " " + ap + "</b>"; }
function dtBizDays() { var a = _v("bd-a"), b = _v("bd-b");
  if (!a || !b) { out("bd-out", "Pick both dates.", "err"); return; }
  var d1 = pISO(a), d2 = pISO(b);
  if (d2 < d1) { var tmp = d1; d1 = d2; d2 = tmp; }
  var biz = 0, cal = Math.round((d2 - d1) / 86400000);
  var cur = new Date(d1);
  for (var i = 0; i < cal; i++) { var dow = cur.getDay(); if (dow !== 0 && dow !== 6) biz++; cur.setDate(cur.getDate() + 1); }
  out("bd-out", "<b>" + biz + " business days</b> (Mon\u2013Fri) between " + a + " and " + b + "<br>Calendar span: " + cal + " days &nbsp;\u00b7&nbsp; Weekend days: " + (cal - biz)); }

/* ---------- MEGA init ---------- */
(function () {
  if ($("uc-in") && window.UC_CONF) {
    $("uc-in").addEventListener("input", ucRun);
    if ($("uc-swap")) $("uc-swap").addEventListener("click", ucSwap);
    if ($("uc-copy")) $("uc-copy").addEventListener("click", ucCopy);
    ucRun();
  }
  if ($("cx-in")) cxHex();
  if ($("cr-r")) cxRgb();
  if ($("ch-in")) cxHexHsl();
  if ($("rh-r")) cxRgbHsl();
  if ($("sh-in")) cxShades();
  if ($("cp-in")) cxComp();
  if ($("ct-fg")) cxContrast();
  if ($("iv-in")) cxInvert();
  if ($("gs-in")) cxGray();
  var today = new Date();
  function setD(id, d) { var el = $(id); if (el && !el.value) el.value = dISO(d); }
  setD("rd-a", new Date(today.getFullYear(), 0, 1));
  setD("rd-b", new Date(today.getFullYear(), 11, 31));
  setD("ad-date", today);
  setD("dw-date", today);
  setD("wn-date", today);
  setD("bd-a", new Date(today.getFullYear(), today.getMonth(), 1));
  setD("bd-b", today);
  if ($("sl-time")) attachTimePicker("sl-time", "sl-tv", "07:00");
})();

/* ---------- MEGA3: advanced calculators ---------- */
function drawLineChart(cv, series, labels) {
  if (!cv) return;
  var ctx = cv.getContext("2d");
  var W = cv.width, H = cv.height, pad = 44, pw = W - pad - 16, ph = H - 30 - 20;
  ctx.clearRect(0, 0, W, H);
  var css = getComputedStyle(document.documentElement);
  var txt = (css.getPropertyValue("--muted") || "#8b93a7").trim();
  var line = (css.getPropertyValue("--accent") || "#ff7a1a").trim();
  var grid = (css.getPropertyValue("--border") || "rgba(255,255,255,.08)").trim();
  var max = Math.max.apply(null, series), min = Math.min.apply(null, series);
  if (max === min) max = min + 1;
  ctx.strokeStyle = grid; ctx.fillStyle = txt; ctx.font = "11px sans-serif"; ctx.lineWidth = 1;
  for (var g = 0; g <= 4; g++) {
    var gy = 20 + ph - (ph * g) / 4;
    ctx.beginPath(); ctx.moveTo(pad, gy); ctx.lineTo(pad + pw, gy); ctx.stroke();
    ctx.fillText(nfmt(max - ((max - min) * g) / 4, 0), 4, gy + 4);
  }
  ctx.strokeStyle = line; ctx.lineWidth = 2.5; ctx.beginPath();
  for (var i = 0; i < series.length; i++) {
    var x = pad + (pw * i) / (series.length - 1);
    var y = 20 + ph - ((series[i] - min) / (max - min)) * ph;
    if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
  }
  ctx.stroke();
  ctx.fillStyle = line;
  for (var j = 0; j < series.length; j++) {
    var px = pad + (pw * j) / (series.length - 1);
    var py = 20 + ph - ((series[j] - min) / (max - min)) * ph;
    ctx.beginPath(); ctx.arc(px, py, 3, 0, Math.PI * 2); ctx.fill();
  }
  ctx.fillStyle = txt;
  var step = Math.ceil(labels.length / 6);
  for (var k = 0; k < labels.length; k += step) {
    var lx = pad + (pw * k) / (series.length - 1);
    ctx.fillText(labels[k], Math.min(lx, W - 30), H - 6);
  }
}
function ci() {
  var p = _n("ci-p"), m = _n("ci-m"), r = _n("ci-r"), y = _n("ci-y"), n = _n("ci-f") || 12;
  if (p === null || r === null || y === null) { out("ci-out", "Enter an initial amount, a rate and a number of years.", "result warn"); return; }
  m = m || 0;
  var i = r / 100 / n, months = Math.round(y * 12), bal = p, series = [], labels = [];
  for (var mo = 1; mo <= months; mo++) {
    bal = bal * (1 + i) + m;
    if (mo % 12 === 0) { series.push(bal); labels.push("Yr " + mo / 12); }
  }
  var contrib = p + m * months, interest = bal - contrib;
  out("ci-out", "<b>Final balance: " + nfmt(bal) + "</b><br>Total contributions: " + nfmt(contrib) + " &nbsp;\u00b7&nbsp; Interest earned: <b>" + nfmt(interest) + "</b> (" + nfmt((interest / Math.max(contrib, 0.01)) * 100, 1) + "% growth)");
  drawLineChart($("ci-chart"), series, labels);
}
function am() {
  var P = _n("am-a"), rp = _n("am-r"), y = _n("am-y");
  if (P === null || rp === null || y === null) { out("am-out", "Enter loan amount, rate and term.", "result warn"); return; }
  var r = rp / 100 / 12, n = Math.round(y * 12), pay;
  if (r === 0) pay = P / n; else pay = P * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1);
  var bal = P, totInt = 0, rows = "", yearInt = 0, yearPrin = 0;
  for (var mo = 1; mo <= n; mo++) {
    var intM = bal * r, prM = pay - intM;
    bal = Math.max(0, bal - prM); totInt += intM; yearInt += intM; yearPrin += prM;
    if (mo % 12 === 0 || mo === n) {
      rows += "<tr><td>Year " + Math.ceil(mo / 12) + "</td><td>" + nfmt(pay * (mo % 12 === 0 ? 12 : mo % 12)) + "</td><td>" + nfmt(yearInt) + "</td><td>" + nfmt(yearPrin) + "</td><td>" + nfmt(bal) + "</td></tr>";
      yearInt = 0; yearPrin = 0;
    }
  }
  out("am-out", "<b>Monthly payment: " + nfmt(pay) + "</b><br>Total paid: " + nfmt(pay * n) + " &nbsp;\u00b7&nbsp; Total interest: <b>" + nfmt(totInt) + "</b>");
  $("am-table").innerHTML = "<table class='uc-table'><thead><tr><th>Period</th><th>Paid</th><th>Interest</th><th>Principal</th><th>Balance</th></tr></thead><tbody>" + rows + "</tbody></table>";
}
function cal() {
  var age = _n("cal-age"), h = _n("cal-h"), w = _n("cal-w"), sex = _v("cal-sex"), act = parseFloat(_v("cal-act")) || 1.2;
  if (age === null || h === null || w === null) { out("cal-out", "Enter age, height and weight.", "result warn"); return; }
  var bmr = 10 * w + 6.25 * h - 5 * age + (sex === "m" ? 5 : -161);
  var tdee = bmr * act;
  out("cal-out", "<b>BMR: " + nfmt(bmr, 0) + " kcal/day</b><br>TDEE (maintenance): <b>" + nfmt(tdee, 0) + " kcal/day</b><br>Lose ~0.5 kg/wk: " + nfmt(tdee - 500, 0) + " &nbsp;\u00b7&nbsp; Gain ~0.5 kg/wk: " + nfmt(tdee + 500, 0));
}
function bf() {
  var sex = _v("bf-sex"), h = _n("bf-h"), neck = _n("bf-neck"), waist = _n("bf-waist"), hip = _n("bf-hip");
  if (h === null || neck === null || waist === null || (sex === "f" && hip === null)) { out("bf-out", "Enter height, neck and waist" + (sex === "f" ? " and hip measurements." : "."), "result warn"); return; }
  var bf;
  if (sex === "m") {
    if (waist - neck <= 0) { out("bf-out", "Waist must be larger than neck for the formula.", "result warn"); return; }
    bf = 495 / (1.0324 - 0.19077 * Math.log10(waist - neck) + 0.15456 * Math.log10(h)) - 450;
  } else {
    if (waist + hip - neck <= 0) { out("bf-out", "Check the measurements \u2014 waist + hip must exceed neck.", "result warn"); return; }
    bf = 495 / (1.29579 - 0.35004 * Math.log10(waist + hip - neck) + 0.221 * Math.log10(h)) - 450;
  }
  var cat = bf < 6 ? "Essential fat" : bf < 14 ? "Athletic" : bf < 18 ? "Fit" : bf < 25 ? "Average" : "Above average";
  if (sex === "f") cat = bf < 14 ? "Essential fat" : bf < 21 ? "Athletic" : bf < 25 ? "Fit" : bf < 32 ? "Average" : "Above average";
  out("bf-out", "<b>Estimated body fat: " + nfmt(bf, 1) + "%</b><br>Category: " + cat + " &nbsp;\u00b7&nbsp; Lean mass: about " + nfmt(100 - bf, 1) + "% of body weight");
}
function orm() {
  var w = _n("orm-w"), r = _n("orm-r");
  if (w === null || r === null || r < 1) { out("orm-out", "Enter the weight and reps (at least 1).", "result warn"); return; }
  if (r > 12) { out("orm-out", "Use a set of 12 reps or fewer \u2014 higher-rep sets do not predict a 1RM reliably.", "result warn"); return; }
  var epley = w * (1 + r / 30), brz = w * 36 / (37 - r), avg = (epley + brz) / 2;
  var pcts = [95, 90, 85, 80, 75, 70, 65, 60], rows = "";
  for (var i = 0; i < pcts.length; i++) {
    var load = avg * pcts[i] / 100;
    rows += "<tr><td>" + pcts[i] + "%</td><td>" + nfmt(load, 1) + " kg</td><td>" + (pcts[i] >= 90 ? "1\u20133 reps" : pcts[i] >= 80 ? "4\u20136 reps" : pcts[i] >= 70 ? "8\u201312 reps" : "12+ reps (endurance)") + "</td></tr>";
  }
  out("orm-out", "<b>Estimated 1RM: " + nfmt(avg, 1) + " kg</b><br>Epley: " + nfmt(epley, 1) + " &nbsp;\u00b7&nbsp; Brzycki: " + nfmt(brz, 1));
  $("orm-table").innerHTML = "<table class='uc-table'><thead><tr><th>% of 1RM</th><th>Load</th><th>Typical reps</th></tr></thead><tbody>" + rows + "</tbody></table>";
}
function pace() {
  var d = _n("pace-d"), h = _n("pace-h") || 0, m = _n("pace-m") || 0, s = _n("pace-s") || 0;
  if (d === null || d <= 0 || (h + m + s) === 0) { out("pace-out", "Enter a distance and a finish time.", "result warn"); return; }
  var tot = h * 3600 + m * 60 + s;
  var spk = tot / d, spm = spk * 1.609344, kmh = 3600 / spk;
  function fmtPace(sec) { var mm = Math.floor(sec / 60), ss = Math.round(sec % 60); if (ss === 60) { mm++; ss = 0; } return mm + ":" + String(ss).padStart(2, "0"); }
  out("pace-out", "<b>Pace: " + fmtPace(spk) + " /km</b> &nbsp;\u00b7&nbsp; " + fmtPace(spm) + " /mile<br>Speed: " + nfmt(kmh, 2) + " km/h (" + nfmt(kmh / 1.609344, 2) + " mph)<br>Predicted 10K at this pace: " + fmtPace(spk * 10 / 60) + " min \u2014 " + fmtPace(spk * 10) + " total");
}
function be() {
  var f = _n("be-f"), p = _n("be-p"), v = _n("be-v");
  if (f === null || p === null || v === null) { out("be-out", "Enter fixed costs, price and variable cost.", "result warn"); return; }
  var margin = p - v;
  if (margin <= 0) { out("be-out", "Price per unit must exceed variable cost per unit \u2014 with this margin no volume ever breaks even.", "result warn"); return; }
  var units = Math.ceil(f / margin);
  out("be-out", "<b>Break-even: " + nfmt(units, 0) + " units</b> &nbsp;\u00b7&nbsp; Revenue needed: " + nfmt(units * p) + "<br>Margin per unit: " + nfmt(margin) + " (" + nfmt(margin / p * 100, 1) + "% of price)");
}
function roi() {
  var ini = _n("roi-i"), fin = _n("roi-f"), y = _n("roi-y");
  if (ini === null || fin === null || ini <= 0) { out("roi-out", "Enter an initial investment and final value.", "result warn"); return; }
  var roi = (fin - ini) / ini * 100;
  var extra = "";
  if (y !== null && y > 0 && fin > 0) {
    var cagr = (Math.pow(fin / ini, 1 / y) - 1) * 100;
    extra = "<br>Annualized (CAGR): <b>" + nfmt(cagr, 2) + "% per year</b> over " + nfmt(y, 1) + " years";
  }
  out("roi-out", "<b>ROI: " + nfmt(roi, 2) + "%</b><br>Net gain/loss: " + nfmt(fin - ini) + extra);
}
function up() {
  var pa = _n("up-pa"), sa = _n("up-sa"), pb = _n("up-pb"), sb = _n("up-sb");
  if (pa === null || sa === null || sa <= 0 || pb === null || sb === null || sb <= 0) { out("up-out", "Enter price and size (same unit) for both products.", "result warn"); return; }
  var ua = pa / sa, ub = pb / sb;
  var cheap = ua < ub ? "Product A" : ub < ua ? "Product B" : null;
  var sav = cheap ? Math.abs(ua - ub) / Math.max(ua, ub) * 100 : 0;
  out("up-out", "<b>A: " + nfmt(ua, 3) + " per unit</b> &nbsp;\u00b7&nbsp; B: " + nfmt(ub, 3) + " per unit<br>" + (cheap ? "<b>" + cheap + " is cheaper</b> \u2014 you save " + nfmt(sav, 1) + "% per unit." : "Both cost the same per unit."));
}
function gr() {
  var c = _n("gr-c"), w = _n("gr-w"), d = _n("gr-d");
  if (c === null || w === null || d === null || w <= 0 || w > 100) { out("gr-out", "Enter current grade, exam weight (1\u2013100%) and target.", "result warn"); return; }
  var need = (d - c * (1 - w / 100)) / (w / 100);
  if (need <= 0) out("gr-out", "\ud83c\udf89 <b>Target already secured!</b> Even a 0 on the final leaves you at " + nfmt(c * (1 - w / 100), 1) + "%.");
  else if (need > 100) out("gr-out", "<b>Not reachable:</b> you would need " + nfmt(need, 1) + "% on the final. Best possible overall grade: " + nfmt(c * (1 - w / 100) + 100 * (w / 100), 1) + "%.");
  else out("gr-out", "<b>You need " + nfmt(need, 1) + "% on the final</b> to reach an overall " + nfmt(d, 1) + "%.");
}
function ec() {
  var w = _n("ec-w"), h = _n("ec-h"), d = _n("ec-d") || 365, p = _n("ec-p");
  if (w === null || h === null || p === null) { out("ec-out", "Enter watts, hours per day and price per kWh.", "result warn"); return; }
  var kwhDay = w / 1000 * h, costDay = kwhDay * p;
  var kwhYear = kwhDay * d;
  out("ec-out", "<b>" + nfmt(kwhDay, 2) + " kWh/day \u2192 " + nfmt(costDay) + " per day</b><br>Monthly: " + nfmt(costDay * 30.4) + " &nbsp;\u00b7&nbsp; Yearly: <b>" + nfmt(costDay * d) + "</b> (" + nfmt(kwhYear, 0) + " kWh)");
}
function sleep() {
  var tv = _v("sl-tv") || "07:00";
  var parts = tv.split(":"), wake = (+parts[0]) * 60 + (+parts[1]);
  var rows = "", times = [];
  for (var c = 6; c >= 3; c--) {
    var t = wake - (c * 90 + 15);
    while (t < 0) t += 1440;
    var hh = Math.floor(t / 60) % 24, mm = t % 60;
    var ampm = hh < 12 ? "AM" : "PM", h12 = hh % 12 === 0 ? 12 : hh % 12;
    var label = h12 + ":" + String(mm).padStart(2, "0") + " " + ampm;
    times.push(label);
    rows += "<tr><td>" + c + " cycles</td><td>" + (c * 1.5) + " h sleep</td><td><b>" + label + "</b></td></tr>";
  }
  $("sleep-out").innerHTML = "<b>Bedtimes for a " + tv + " wake-up</b> (includes 15 min to fall asleep)<table class='uc-table' style='margin-top:10px'><thead><tr><th>Cycles</th><th>Sleep</th><th>Bedtime</th></tr></thead><tbody>" + rows + "</tbody></table>";
}
