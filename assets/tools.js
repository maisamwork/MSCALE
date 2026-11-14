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
function wordCount() {
  const t = $("wc-in").value;
  const words = t.trim() ? t.trim().split(/\s+/).length : 0;
  const sentences = (t.match(/[.!?]+(\s|$)/g) || []).length;
  const paras = t.trim() ? t.trim().split(/\n\s*\n/).filter(Boolean).length : 0;
  $("wc-stats").innerHTML =
    `<div class="stat"><b>${words}</b><span>Words</span></div>
     <div class="stat"><b>${t.length}</b><span>Characters</span></div>
     <div class="stat"><b>${t.length ? t.replace(/\s/g, "").length : 0}</b><span>No spaces</span></div>
     <div class="stat"><b>${sentences}</b><span>Sentences</span></div>
     <div class="stat"><b>${paras}</b><span>Paragraphs</span></div>
     <div class="stat"><b>${Math.ceil(words / 200)}</b><span>Min read</span></div>`;
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
