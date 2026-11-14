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
