function $(id) { return document.getElementById(id); }
function out(id, html, cls) {
  const n = $(id);
  if (!n) return false;
  n.innerHTML = html;
  n.className = "result" + (cls ? " " + cls : "");
  return true;
}

/* ---------- Calculators ---------- */
function pctCalc() {
  const x = parseFloat($("pct-x").value), y = parseFloat($("pct-y").value);
  if (isNaN(x) || isNaN(y)) return;
  $("pct-out").innerHTML =
    `<b>${x}%</b> of <b>${y}</b> = <b>${+(x / 100 * y).toFixed(6)}</b><br>` +
    `<b>${x}</b> is <b>${y === 0 ? "∞" : +(x / y * 100).toFixed(4)}%</b> of <b>${y}</b><br>` +
    `Change from <b>${x}</b> to <b>${y}</b>: <b>${x === 0 ? "∞" : +((y - x) / Math.abs(x) * 100).toFixed(4)}%</b>`;
  $("pct-out").className = "result";
}

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
function wordCount() {
  const t = $("wc-in").value;
  const words = t.trim() ? t.trim().split(/\s+/).length : 0;
  const sentences = (t.match(/[.!?]+(\s|$)/g) || []).length;
  const paras = t.trim() ? t.trim().split(/\n\s*\n/).filter(Boolean).length : 0;
  const noSp = t.length ? t.replace(/\s/g, "").length : 0;
  const uniq = new Set((t.toLowerCase().match(/[a-z0-9'\u2019-]+/g) || [])).size;
  const avgLen = words ? (t.replace(/\s/g, "").replace(/[^\w'\u2019-]/g, "").length / words).toFixed(1) : "0";
  $("wc-stats").innerHTML =
    `<div class="stat"><b>${words}</b><span>Words</span></div>
     <div class="stat"><b>${t.length}</b><span>Characters</span></div>
     <div class="stat"><b>${noSp}</b><span>No spaces</span></div>
     <div class="stat"><b>${sentences}</b><span>Sentences</span></div>
     <div class="stat"><b>${paras}</b><span>Paragraphs</span></div>
     <div class="stat"><b>${uniq}</b><span>Unique words</span></div>
     <div class="stat"><b>${avgLen}</b><span>Avg word length</span></div>
     <div class="stat"><b>${wcDur(words, 100)}</b><span>Read · slow (100 wpm)</span></div>
     <div class="stat"><b>${wcDur(words, 230)}</b><span>Read · average (230 wpm)</span></div>
     <div class="stat"><b>${wcDur(words, 300)}</b><span>Read · fast (300 wpm)</span></div>
     <div class="stat"><b>${wcDur(words, 130)}</b><span>Speaking (130 wpm)</span></div>
     <div class="stat"><b>${wcPages(words, 250)}</b><span>Pages · Letter (250 w/p)</span></div>`;
  if (!$("wc-table").innerHTML) wcRefTable();
}

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
function jsonFormat(space) {
  try {
    const parsed = JSON.parse($("json-in").value);
    $("json-err").textContent = "";
    out("json-out", JSON.stringify(parsed, null, space), "mono");
  } catch (e) {
    $("json-err").textContent = "Invalid JSON: " + e.message;
    $("json-out").textContent = "";
  }
}

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
const UNITS = {
  length: { m: 1, km: 1000, cm: 0.01, mm: 0.001, mi: 1609.344, yd: 0.9144, ft: 0.3048, in: 0.0254, "nmi": 1852 },
  weight: { kg: 1, g: 0.001, mg: 1e-6, t: 1000, lb: 0.45359237, oz: 0.028349523, st: 6.35029318 },
  data: { B: 1, KB: 1024, MB: 1048576, GB: 1073741824, TB: 1099511627776 },
};
function unitConvert() {
  const cat = $("uc-cat").value, v = parseFloat($("uc-val").value);
  const from = $("uc-from").value, to = $("uc-to").value;
  const cats = Object.keys(UNITS);
  if (!cats.includes(cat)) return tempConvert(v, from, to);
  if (isNaN(v)) return;
  out("uc-out", `${v} ${from} = <b>${+(v * UNITS[cat][from] / UNITS[cat][to]).toPrecision(10)}</b> ${to}`);
}
function tempConvert(v, from, to) {
  if (isNaN(v)) return;
  let c = from === "°C" ? v : from === "°F" ? (v - 32) * 5 / 9 : v - 273.15;
  const r = to === "°C" ? c : to === "°F" ? c * 9 / 5 + 32 : c + 273.15;
  out("uc-out", `${v} ${from} = <b>${+r.toFixed(4)}</b> ${to}`);
}
function unitCatChange() {
  const cat = $("uc-cat").value;
  const opts = (UNITS[cat] ? Object.keys(UNITS[cat]) : ["°C", "°F", "K"]).map(
    (u) => `<option>${u}</option>`).join("");
  $("uc-from").innerHTML = opts;
  $("uc-to").innerHTML = opts;
  $("uc-to").selectedIndex = Math.min(1, opts.split("</option>").length - 2);
  unitConvert();
}

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
function genPassword() {
  const len = parseInt($("pw-len").value) || 16;
  let chars = "";
  if ($("pw-lower").checked) chars += "abcdefghijklmnopqrstuvwxyz";
  if ($("pw-upper").checked) chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  if ($("pw-digits").checked) chars += "0123456789";
  if ($("pw-symbols").checked) chars += "!@#$%^&*()-_=+[]{};:,.<>?";
  if (!chars) { out("pw-out", "Select at least one character set", "error"); return; }
  const arr = new Uint32Array(len);
  crypto.getRandomValues(arr);
  const pw = [...arr].map((n) => chars[n % chars.length]).join("");
  out("pw-out", pw, "mono");
  const entropy = Math.round(len * Math.log2(chars.length));
  const strength = entropy > 100 ? "Very strong" : entropy > 70 ? "Strong" : entropy > 45 ? "Medium" : "Weak";
  $("pw-strength").textContent = `${strength} (~${entropy} bits of entropy)`;
}

/* ---------- Color ---------- */
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
function genLorem() {
  const paras = Math.min(parseInt($("lorem-n").value) || 3, 20);
  const sentences = Math.min(parseInt($("lorem-s").value) || 4, 20);
  const rand = (a) => a[Math.floor(Math.random() * a.length)];
  const result = [];
  for (let p = 0; p < paras; p++) {
    const s = [];
    for (let i = 0; i < sentences; i++) {
      const len = 6 + Math.floor(Math.random() * 12);
      const words = Array.from({ length: len }, () => rand(LOREM_WORDS));
      s.push(words[0][0].toUpperCase() + words[0].slice(1) + " " + words.slice(1).join(" ") + ".");
    }
    result.push(s.join(" "));
  }
  out("lorem-out", result.join("\n\n"), "mono");
}

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
function imgLoaded() {
  const file = $("img-file").files[0];
  if (!file) return;
  const img = new Image();
  img.onload = () => {
    $("img-w").value = img.width;
    $("img-h").value = img.height;
    $("img-info").textContent = `Original: ${img.width}×${img.height} (${(file.size / 1024).toFixed(0)} KB)`;
  };
  img.src = URL.createObjectURL(file);
}
function resizeImage() {
  const file = $("img-file").files[0];
  if (!file) return;
  const img = new Image();
  img.onload = () => {
    const w = parseInt($("img-w").value) || img.width;
    const h = $("img-lock").checked ? Math.round(w * img.height / img.width) : (parseInt($("img-h").value) || img.height);
    const fmt = $("img-fmt").value;
    const q = parseInt($("img-q").value) / 100;
    const canvas = document.createElement("canvas");
    canvas.width = w; canvas.height = h;
    canvas.getContext("2d").drawImage(img, 0, 0, w, h);
    const url = canvas.toDataURL("image/" + fmt, q);
    $("img-preview").src = url;
    $("img-preview").style.display = "block";
    const link = $("img-download");
    link.href = url;
    link.download = "resized." + (fmt === "jpeg" ? "jpg" : fmt);
    link.style.display = "inline-block";
    $("img-info").textContent = `${img.width}×${img.height} → ${w}×${h}`;
  };
  img.src = URL.createObjectURL(file);
}

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
function qrGen() {
  const box = document.getElementById("qr-box");
  const txt = document.getElementById("qr-text").value;
  if (!txt.trim()) { box.innerHTML = "<p class='error'>Enter some text or a URL first.</p>"; return; }
  box.innerHTML = "";
  const size = +document.getElementById("qr-size").value;
  const ecc = document.getElementById("qr-ecc").value;
  new QRCode(box, { text: txt, width: size, height: size, correctLevel: QRCode.CorrectLevel[ecc] });
}
function qrDownload() {
  const c = document.querySelector("#qr-box canvas");
  const img = document.querySelector("#qr-box img");
  const url = c ? c.toDataURL("image/png") : (img ? img.src : null);
  if (!url) return;
  const a = document.createElement("a");
  a.href = url; a.download = "qr-code.png"; a.click();
}

/* ---- Text Diff Checker (LCS on lines) ---- */
function dEsc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
function diffRun() {
  const a = document.getElementById("diff-a").value.split("\n");
  const b = document.getElementById("diff-b").value.split("\n");
  const n = a.length, m = b.length;
  const dp = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(0));
  for (let i = n - 1; i >= 0; i--)
    for (let j = m - 1; j >= 0; j--)
      dp[i][j] = a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
  let i = 0, j = 0, html = "", adds = 0, dels = 0;
  while (i < n && j < m) {
    if (a[i] === b[j]) { html += `<div class="dln same">${dEsc(a[i]) || "&nbsp;"}</div>`; i++; j++; }
    else if (dp[i + 1][j] >= dp[i][j + 1]) { html += `<div class="dln del">- ${dEsc(a[i])}</div>`; i++; dels++; }
    else { html += `<div class="dln add">+ ${dEsc(b[j])}</div>`; j++; adds++; }
  }
  while (i < n) { html += `<div class="dln del">- ${dEsc(a[i])}</div>`; i++; dels++; }
  while (j < m) { html += `<div class="dln add">+ ${dEsc(b[j])}</div>`; j++; adds++; }
  const summary = `<div class="tool-note">${adds} addition${adds === 1 ? "" : "s"}, ${dels} removal${dels === 1 ? "" : "s"}, ${n + m - adds - dels} unchanged line${n + m - adds - dels === 1 ? "" : "s"}</div>`;
  document.getElementById("diff-out").innerHTML = summary + html;
}

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
  const tm = document.getElementById("cd-time").value || "00:00";
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
