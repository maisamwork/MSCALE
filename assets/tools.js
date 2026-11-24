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

let BM2_UNITS = "metric";
function bm2Units(u, btn) {
  BM2_UNITS = u;
  $("bm2-metric").classList.toggle("active", u === "metric");
  $("bm2-imperial").classList.toggle("active", u === "imperial");
  $("bm2-metric-pane").style.display = u === "metric" ? "block" : "none";
  $("bm2-imperial-pane").style.display = u === "imperial" ? "block" : "none";
  bmiCalc();
}
function bm2Cat(bmi) {
  if (bmi < 18.5) return { lab: "Underweight", cls: "pct2-down", note: "Below the healthy range \u2014 consider nutrient-dense meals and strength training." };
  if (bmi < 25) return { lab: "Normal weight", cls: "", note: "Healthy range \u00b7 keep doing what you are doing." };
  if (bmi < 30) return { lab: "Overweight", cls: "pct2-up", note: "Slightly above the healthy range \u2014 small daily deficits add up." };
  return { lab: "Obese", cls: "pct2-down2", note: "Well above the healthy range \u2014 a doctor can help you plan safely." };
}
function bmiCalc() {
  let w, hM;
  if (BM2_UNITS === "metric") {
    w = parseFloat($("bmi-w").value);
    hM = parseFloat($("bmi-h").value) / 100;
  } else {
    w = parseFloat($("bm2-wlb").value) * 0.45359237;
    hM = (parseFloat($("bm2-ft").value) * 12 + (parseFloat($("bm2-in").value) || 0)) * 0.0254;
  }
  if (!w || !hM || hM < 0.5) { $("bmi-big").innerHTML = "\u2014"; $("bm2-marker").style.left = "0"; $("bmi-out").innerHTML = ""; $("bm2-healthy").innerHTML = ""; return; }
  const bmi = w / (hM * hM);
  const cat = bm2Cat(bmi);
  $("bmi-big").innerHTML = `${bmi.toFixed(1)}<span class="pct2-big-sub">Body Mass Index</span>`;
  const pct = Math.max(0, Math.min(100, (bmi - 15) / 25 * 100));
  $("bm2-marker").style.left = pct + "%";
  $("bmi-out").innerHTML = `<b class="${cat.cls}">${cat.lab}</b><span>${cat.note}</span>`;
  const loW = 18.5 * hM * hM, hiW = 24.9 * hM * hM;
  const f = (kg) => BM2_UNITS === "metric" ? kg.toFixed(1) + " kg" : (kg / 0.45359237).toFixed(1) + " lb";
  $("bm2-healthy").innerHTML = `<span class="pct2-chip">Healthy weight for your height: <b>${f(loW)} \u2013 ${f(hiW)}</b></span>`;
}
if ($("bmi-w")) bmiCalc();

function ageCalc() {
  const dobV = $("age-dob").value;
  if (!dobV) return;
  const hidden = ($("ag2-on") || {}).dataset && $("ag2-on").dataset.date;
  const dob = new Date(dobV + "T00:00:00");
  const on = hidden ? new Date(hidden + "T00:00:00") : new Date();
  if (isNaN(dob) || isNaN(on) || on < dob) return;
  let y = on.getFullYear() - dob.getFullYear(), m2 = on.getMonth() - dob.getMonth(), d = on.getDate() - dob.getDate();
  if (d < 0) { m2--; d += new Date(on.getFullYear(), on.getMonth(), 0).getDate(); }
  if (m2 < 0) { y--; m2 += 12; }
  const msTot = Math.max(0, on - dob), days = Math.floor(msTot / 86400000);
  $("ag2-big").innerHTML = y + ' <span class="pct2-big-sub-inline">years</span> ' + m2 + ' <span class="pct2-big-sub-inline">months</span> ' + d + ' <span class="pct2-big-sub-inline">days</span>';
  $("ag2-months").textContent = (y * 12 + m2).toLocaleString();
  $("ag2-weeks").textContent = Math.floor(days / 7).toLocaleString();
  $("ag2-days").textContent = days.toLocaleString();
  $("ag2-hours").textContent = (days * 24).toLocaleString();
  const mins = $("ag2-mins");
  if (mins) mins.textContent = (days * 1440).toLocaleString();
  let nb = new Date(on.getFullYear(), dob.getMonth(), dob.getDate());
  if (nb < on) nb = new Date(on.getFullYear() + 1, dob.getMonth(), dob.getDate());
  const toNb = Math.ceil((nb - on) / 86400000);
  $("ag2-next").textContent = toNb + " day" + (toNb === 1 ? "" : "s") + " (" + nb.toLocaleDateString(undefined, { month: "short", day: "numeric" }) + ", " + nb.toLocaleDateString(undefined, { weekday: "long" }) + ")";
  $("ag2-dow").textContent = dob.toLocaleDateString(undefined, { weekday: "long" });
  const chips = $("ag2-chips");
  if (chips) chips.innerHTML =
    '<span class="jf-chip"><b>' + (msTot / 1000).toLocaleString(undefined, { maximumFractionDigits: 0 }) + "</b>seconds alive</span>" +
    '<span class="jf-chip"><b>' + y + "y " + m2 + "m</b>exact</span>" +
    '<span class="jf-chip"><b>' + Math.round(days / 365.25 * 10) / 10 + "</b>decimal years</span>" +
    '<span class="jf-chip"><b>' + Math.floor(on.getFullYear() - dob.getFullYear()) + "</b>birthdays so far</span>";
  const mile = $("ag2-mile");
  if (mile) {
    const marks = [
      { at: 1000, label: "1,000 days" }, { at: 5000, label: "5,000 days" },
      { at: 10000, label: "10,000 days" }, { at: 20000, label: "20,000 days" },
      { at: Math.round(1e9 / 86400), label: "1 billion seconds" },
      { at: 1000 * 365.25, label: "1,000,000 hours (approx)" }
    ];
    const items = marks
      .filter((k) => k.at > days)
      .slice(0, 4)
      .map((k) => {
        const when = new Date(dob.getTime() + k.at * 86400000);
        const inDays = Math.ceil((when - on) / 86400000);
        return '<span class="jf-chip"><b>' + k.label + "</b>" + inDays.toLocaleString() + " d \u00b7 " + when.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" }) + "</span>";
      });
    mile.innerHTML = items.join("") || '<span class="jf-chip ok"><b>all in</b>every listed milestone is behind you</span>';
  }
}
function ag2Today() { const el = $("ag2-on"); if (el) { el.value = ""; delete el.dataset.date; } ageCalc(); }
function ag2Copy(btn) {
  const get = (id) => ($(id) || {}).textContent || "";
  const t = "Age: " + (document.getElementById("ag2-big") || {}).textContent.trim() +
    " \u00b7 Total days: " + get("#ag2-days").replace(/[,\u00a0]/g, "").trim() +
    " \u00b7 Next birthday: " + get("#ag2-next").trim();
  copyText(t, btn);
}
if ($("age-dob")) ageCalc();

function emiCalc() {
  const P = parseFloat($("emi-p").value), rRate = parseFloat($("emi-r").value) / 100 / 12;
  let n = parseInt($("emi-n").value) * 12;
  const extra = parseFloat($("emi-x").value) || 0;
  const big = $("ln2-big");
  if (!big) return;
  if (!P || isNaN(rRate) || !n || n <= 0) { big.innerHTML = "\u2014"; const c = $("ln2-chips"); if (c) c.innerHTML = ""; return; }
  const emi = rRate === 0 ? P / n : P * rRate * Math.pow(1 + rRate, n) / (Math.pow(1 + rRate, n) - 1);
  const pay = emi + extra;
  // base loan totals (no prepayment)
  const total0 = emi * n, int0 = total0 - P;
  // amortize with the actual payment (incl. extra) for real payoff time + interest
  let bal = P, m = 0, intX = 0;
  const rows = [];
  let yInt = 0, yPrin = 0;
  const cap = n + 600;
  if (pay <= P * rRate) {
    big.innerHTML = '<span class="error">Payment must exceed the monthly interest (' + (P * rRate).toFixed(2) + ')</span>';
    const c = $("ln2-chips"); if (c) c.innerHTML = "";
    const t = $("ln2-table"); if (t) t.innerHTML = "";
    const b = $("ln2-bars"); if (b) b.innerHTML = "";
    return;
  }
  while (bal > 0.005 && m < cap) {
    const int = bal * rRate;
    const prin = Math.min(pay - int, bal);
    bal -= prin;
    intX += int; yInt += int; yPrin += prin;
    m++;
    if (m % 12 === 0 || bal <= 0.005) {
      rows.push([Math.ceil(m / 12), yPrin, yInt, Math.max(0, bal)]);
      yInt = 0; yPrin = 0;
    }
  }
  const totalX = pay * m, intXsave = int0 - intX;
  const ms = (mm) => Math.floor(mm / 12) + "y " + Math.round(mm % 12) + "mo";
  big.innerHTML = emi.toFixed(2) + '<span class="pct2-big-sub">monthly payment \u00b7 ' + n + " payments</span>";
  const chips = $("ln2-chips");
  if (chips) {
    let h =
      '<span class="jf-chip"><b>' + totalX.toFixed(0) + "</b>total paid</span>" +
      '<span class="jf-chip"><b>' + intX.toFixed(0) + "</b>total interest</span>" +
      '<span class="jf-chip"><b>' + ms(m) + "</b>payoff time</span>" +
      '<span class="jf-chip"><b>' + Math.round((totalX / 12) * 100) / 100 + "</b>per year</span>";
    if (extra > 0) {
      h += '<span class="jf-chip ok"><b>' + ms(Math.max(0, n - m)) + "</b>earlier</span>" +
        '<span class="jf-chip ok"><b>' + Math.round(intXsave).toLocaleString() + "</b>interest saved</span>";
    }
    chips.innerHTML = h;
  }
  const max = Math.max(P, intX, 1);
  const bars = $("ln2-bars");
  if (bars) bars.innerHTML =
    '<div class="ci2-bar-row"><span>Principal</span><div class="wc-bar"><div class="wc-bar-fill" style="width:' + (P / (P + intX) * 100).toFixed(1) + '%"></div></div><b>' + (P / (P + intX) * 100).toFixed(1) + "%</b></div>" +
    '<div class="ci2-bar-row"><span>Interest</span><div class="wc-bar"><div class="wc-bar-fill near" style="width:' + (intX / (P + intX) * 100).toFixed(1) + '%"></div></div><b>' + (intX / (P + intX) * 100).toFixed(1) + "%</b></div>";
  const note = $("ln2-pay");
  if (note) note.textContent = extra > 0
    ? "You pay " + pay.toFixed(2) + "/month \u2014 clears the loan in " + ms(m) + " instead of " + ms(n) + " and saves " + Math.round(intXsave).toLocaleString() + " in interest."
    : "Pay a little extra each month to see how much faster the loan clears.";
  EM2_ROWS = rows.map(([y, p, i2, b]) => [y, p, i2, b]);
  EM2_META = { amount: P, rate: rRate * 1200, emi: emi, pay: pay, months: m, interest: intX };
  const t = $("ln2-table");
  if (t) {
    let h = '<table class="wc-table"><thead><tr><th>Year</th><th>Principal paid</th><th>Interest paid</th><th>Balance left</th></tr></thead><tbody>';
    const show = rows.slice(0, 50);
    h += show.map(([y, p, i2, b]) => "<tr><td>" + y + "</td><td><b>" + p.toFixed(0) + "</b></td><td style=\"color:#f59e0b\">" + i2.toFixed(0) + "</td><td>" + b.toFixed(0) + "</td></tr>").join("");
    if (rows.length > 50) h += '<tr><td colspan="4" style="color:var(--soft)">&mdash; " + (rows.length - 50) + " more years in the CSV \u2014</td></tr>';
    h += "</tbody></table>";
    t.innerHTML = h;
  }
}
function ln2Term(y) { if ($("emi-n")) $("emi-n").value = String(y); emiCalc(); }
function ln2Csv() {
  if (!EM2_ROWS.length) return;
  const meta = EM2_META;
  let csv = "Loan amount," + meta.amount + "\nInterest rate %/year," + meta.rate + "\nMonthly payment," + meta.pay + "\nPayoff months," + meta.months + "\nTotal interest," + meta.interest.toFixed(2) + "\n\nYear,Principal paid,Interest paid,Balance left\n";
  csv += EM2_ROWS.map(([y, p, i2, b]) => [y, p.toFixed(2), i2.toFixed(2), b.toFixed(2)].join(",")).join("\n");
  dlBytes(csv, "loan-schedule.csv", "text/csv");
}
function ln2Copy(btn) {
  const t = "Monthly payment: " + (parseFloat($("emi-p").value) ? $("ln2-big").textContent.trim() : "\u2014");
  copyText(t, btn);
}
let EM2_ROWS = [], EM2_META = {};
if ($("emi-p")) emiCalc();

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

let CV2_MODE = "upper";
function cv2Set(m, btn) {
  CV2_MODE = m;
  btn.parentNode.querySelectorAll(".lr2-type").forEach((b) => b.classList.remove("active"));
  btn.classList.add("active");
  cv2Run();
}
function cv2Run() {
  const t = $("case-in").value;
  let r = t;
  if (CV2_MODE === "upper") r = t.toUpperCase();
  if (CV2_MODE === "lower") r = t.toLowerCase();
  if (CV2_MODE === "title") r = t.toLowerCase().replace(/\b\w/g, (c) => c.toUpperCase());
  if (CV2_MODE === "sentence") r = t.toLowerCase().replace(/(^\s*\w|[.!?]\s+\w)/g, (c) => c.toUpperCase());
  if (CV2_MODE === "camel") r = t.toLowerCase().replace(/[^a-z0-9]+(.)/g, (_, c) => c.toUpperCase()).replace(/^(.)/, (c) => c.toLowerCase());
  if (CV2_MODE === "pascal") r = t.toLowerCase().replace(/(^|[^a-z0-9]+)(.)/g, (_, __, c) => c.toUpperCase()).replace(/[^a-zA-Z0-9]/g, "");
  if (CV2_MODE === "snake") r = t.trim().toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_|_$/g, "");
  if (CV2_MODE === "kebab") r = t.trim().toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
  $("cv2-out").value = r;
  const words = (t.trim().match(/\S+/g) || []).length;
  const lines = t ? t.split("\n").length : 0;
  $("cv2-stats").innerHTML =
    '<span class="jf-chip"><b>' + t.length + "</b>characters</span>" +
    '<span class="jf-chip"><b>' + words + "</b>words</span>" +
    '<span class="jf-chip"><b>' + lines + "</b>lines</span>";
}
function cv2Copy(btn) {
  const v = $("cv2-out").value;
  if (!v) return;
  navigator.clipboard.writeText(v).catch(() => {});
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy result"), 1200);
}
function cv2Swap() { $("case-in").value = $("cv2-out").value; cv2Run(); }
if ($("case-in")) cv2Run();

function dedupeLines() {
  const inEl = $("dd-in");
  if (!inEl || !$("dd2-out")) return;
  const ci = $("dd-case").checked, trim = $("dd-trim").checked;
  const noEmpty = $("dd2-noempty").checked, doSort = $("dd2-sort").checked;
  const seen = new Set(), res = [];
  for (const raw of inEl.value.split("\n")) {
    const line = trim ? raw.trim() : raw;
    const key = ci ? line.toLowerCase() : line;
    if (noEmpty && line.trim() === "") continue;
    if (!seen.has(key)) { seen.add(key); res.push(line); }
  }
  const out = doSort ? res.slice().sort((a, b) => a.localeCompare(b)).join("\n") : res.join("\n");
  $("dd2-out").value = out;
  const inputLines = inEl.value.split("\n").length;
  $("dd2-stats").innerHTML =
    '<span class="jf-chip"><b>' + inputLines + "</b>input lines</span>" +
    '<span class="jf-chip"><b>' + res.length + "</b>unique</span>" +
    '<span class="jf-chip"><b>' + (inputLines - res.length) + "</b>removed</span>";
}
function dd2Copy(btn) {
  $("dd2-out").value ? navigator.clipboard.writeText($("dd2-out").value).catch(() => {}) : 0;
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy result"), 1200);
}
function dd2Use() { $("dd-in").value = $("dd2-out").value; dedupeLines(); }
if ($("dd-in")) dedupeLines();

let RV2_MODE = "chars";
function reverseText(mode, btn) {
  RV2_MODE = mode;
  if (btn && btn.parentNode) btn.parentNode.querySelectorAll(".lr2-type").forEach((b) => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  const t = $("rev-in").value;
  if (!$("rev-out")) return;
  let r = t;
  if (mode === "chars") r = [...t].reverse().join("");
  if (mode === "words") r = t.split(/\s+/).reverse().join(" ");
  if (mode === "lines") r = t.split("\n").reverse().join("\n");
  if (mode === "each") r = t.split("\n").map((l) => [...l].reverse().join("")).join("\n");
  $("rev-out").value = r;
  const words = (t.trim().match(/\S+/g) || []).length;
  $("rv2-stats").innerHTML =
    '<span class="jf-chip"><b>' + t.length + "</b>characters</span>" +
    '<span class="jf-chip"><b>' + words + "</b>words</span>" +
    '<span class="jf-chip"><b>' + (t ? t.split("\n").length : 0) + "</b>lines</span>" +
    '<span class="jf-chip"><b>' + escHtml(mode) + "</b>mode</span>";
}
function rv2Copy(btn) {
  if (!$("rev-out").value) return;
  navigator.clipboard.writeText($("rev-out").value).catch(() => {});
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy result"), 1200);
}
function rv2Swap() { $("rev-in").value = $("rev-out").value; reverseText(RV2_MODE); }
if ($("rev-in")) reverseText("chars");

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

let B64_MODE = "enc";
function b64Mode(m) {
  B64_MODE = m;
  $("b64-enc").classList.toggle("active", m === "enc");
  $("b64-dec").classList.toggle("active", m === "dec");
  b64Live();
}
function b64Live() {
  if (!$("b64-out")) return;
  const t = $("b64-in").value, url = $("b64-urlsafe").checked;
  const err = $("b64-err");
  err.style.display = "none";
  let r = "";
  try {
    if (B64_MODE === "enc") {
      let s = btoa(String.fromCharCode(...new TextEncoder().encode(t)));
      if (url) s = s.replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
      r = s;
    } else {
      let s = t.trim().replace(/-/g, "+").replace(/_/g, "/");
      while (s.length % 4) s += "=";
      r = new TextDecoder().decode(Uint8Array.from(atob(s), (c) => c.charCodeAt(0)));
    }
  } catch (e) { err.textContent = "That is not valid Base64 \u2014 check for stray characters."; err.style.display = "block"; }
  $("b64-out").value = r;
  const ib = new TextEncoder().encode(t).length, ob = new TextEncoder().encode(r).length;
  $("b64-stats").innerHTML =
    '<span class="jf-chip"><b>' + ib + "</b>input bytes</span>" +
    '<span class="jf-chip"><b>' + ob + "</b>output bytes</span>" +
    '<span class="jf-chip"><b>' + (B64_MODE === "enc" && ib ? "+" + Math.round((ob - ib) / ib * 100) + "%" : B64_MODE === "enc" ? "0%" : "\u2014") + "</b>size change</span>" +
    '<span class="jf-chip"><b>' + (url ? "URL-safe" : "standard") + "</b>alphabet</span>";
}
function b64Swap() {
  $("b64-in").value = $("b64-out").value;
  b64Mode(B64_MODE === "enc" ? "dec" : "enc");
}
function b64Copy(btn) {
  const v = $("b64-out").value;
  if (!v) return;
  navigator.clipboard.writeText(v).catch(() => {});
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy output"), 1200);
}
function b64Download() {
  const v = $("b64-out").value;
  if (!v) return;
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([v], { type: "text/plain" }));
  a.download = B64_MODE === "enc" ? "base64-encoded.txt" : "base64-decoded.txt";
  a.click();
}
function b64Sample() { b64Mode("enc"); $("b64-in").value = "Hello MSCALE Tools! Everything runs in your browser."; b64Live(); }
if ($("b64-in")) b64Mode("enc");

let UE2_MODE = "enc";
function ue2Mode(m) {
  UE2_MODE = m;
  $("ue2-enc").classList.toggle("active", m === "enc");
  $("ue2-dec").classList.toggle("active", m === "dec");
  ue2Live();
}
function ue2Live() {
  if (!$("url-out")) return;
  const t = $("url-in").value;
  const err = $("ue2-err");
  err.style.display = "none";
  let r = "";
  try {
    if (UE2_MODE === "enc") r = $("ue2-uri").checked ? encodeURI(t) : encodeURIComponent(t);
    else r = decodeURIComponent(t.replace(/\+/g, " "));
  } catch (e) { err.textContent = "Malformed percent-encoding \u2014 stray % without two hex digits?"; err.style.display = "block"; }
  $("url-out").value = r;
  $("ue2-stats").innerHTML =
    '<span class="jf-chip"><b>' + t.length + "</b>chars in</span>" +
    '<span class="jf-chip"><b>' + r.length + "</b>chars out</span>" +
    '<span class="jf-chip"><b>' + (t ? Math.round(r.length / Math.max(t.length, 1) * 100) + "%" : "\u2014") + "</b>of original</span>" +
    '<span class="jf-chip"><b>' + (UE2_MODE === "enc" ? "encoding" : "decoding") + "</b>mode</span>";
}
function ue2Swap() { $("url-in").value = $("url-out").value; ue2Mode(UE2_MODE === "enc" ? "dec" : "enc"); }
function ue2Copy(btn) {
  if (!$("url-out").value) return;
  navigator.clipboard.writeText($("url-out").value).catch(() => {});
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy output"), 1200);
}
function ue2Sample() { ue2Mode("enc"); $("url-in").value = "https://example.com/search?q=hello world&cats=big+cats&price=$10"; ue2Live(); }
if ($("url-in")) ue2Mode("enc");

let UU2_LIST = [];
function uu2Fmt(u) {
  $("uu2-upper") && $("uu2-upper").checked && (u = u.toUpperCase());
  $("uu2-nohyphen") && $("uu2-nohyphen").checked && (u = u.replace(/-/g, ""));
  $("uu2-braces") && $("uu2-braces").checked && (u = "{" + u + "}");
  return u;
}
function uuidRegen() {
  if (!$("uuid-out") || !UU2_LIST.length) return;
  $("uuid-out").innerHTML = UU2_LIST.map((u) => '<button type="button" class="uu2-row" data-uuid="' + uu2Fmt(u) + '" onclick="uu2Click(this)"><code>' + uu2Fmt(u) + "</code></button>").join("");
}
function uu2Click(btn) {
  navigator.clipboard.writeText(btn.dataset.uuid).catch(() => {});
  const c = btn.querySelector("code");
  if (c) { const oldU = c.textContent; c.textContent = "Copied!"; setTimeout(() => (c.textContent = btn.dataset.uuid), 1200); }
}
function uuidGen() {
  const n = Math.min(parseInt($("uuid-n").value) || 1, 100);
  UU2_LIST = Array.from({ length: n }, () => crypto.randomUUID());
  uuidRegen();
}
function uu2CopyAll(btn) {
  if (!UU2_LIST.length) return;
  navigator.clipboard.writeText(UU2_LIST.map(uu2Fmt).join("\n")).catch(() => {});
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy all"), 1200);
}
if ($("uuid-n")) uuidGen();

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

let TM2_UNIT = "s";
function tm2Unit(u) {
  TM2_UNIT = u;
  $("tm2-s").classList.toggle("active", u === "s");
  $("tm2-ms").classList.toggle("active", u === "ms");
}
function tm2Now() {
  $("ts-in").value = TM2_UNIT === "s" ? Math.floor(Date.now() / 1000) : Date.now();
  tm2Run();
}
function tm2Random() {
  const lo = new Date(2000, 0, 1).getTime(), hi = Date.now();
  const t = Math.floor(lo + Math.random() * (hi - lo));
  $("ts-in").value = TM2_UNIT === "s" ? Math.floor(t / 1000) : t;
  tm2Run();
}
function tm2Type(d) {
  const t = $("ts-in").value.trim();
  if (!t) return;
  const ms = /^\d{11,}$/.test(t) ? parseInt(t) : parseInt(t) * 1000;
  const dd = new Date(ms);
  if (isNaN(dd)) { $("tm2-iso").textContent = "Invalid timestamp"; $("tm2-utc").textContent = $("tm2-local").textContent = $("tm2-dow").textContent = $("tm2-rel").textContent = "\u2014"; $("tm2-stats").innerHTML = ""; return; }
  const diff = dd - new Date();
  const ad = Math.abs(diff);
  const rel = diff < 0
    ? (ad < 3600000 ? Math.round(ad / 60000) + " min ago" : ad < 86400000 ? Math.round(ad / 3600000) + " h ago" : Math.floor(ad / 86400000).toLocaleString() + " days ago")
    : (ad < 3600000 ? "in " + Math.round(ad / 60000) + " min" : ad < 86400000 ? "in " + Math.round(ad / 3600000) + " h" : "in " + Math.floor(ad / 86400000).toLocaleString() + " days");
  $("tm2-iso").textContent = dd.toISOString();
  $("tm2-utc").textContent = dd.toUTCString();
  $("tm2-local").textContent = dd.toString();
  $("tm2-dow").textContent = dd.toLocaleDateString(undefined, { weekday: "long", year: "numeric", month: "long", day: "numeric" });
  $("tm2-rel").textContent = rel;
  $("tm2-stats").innerHTML =
    '<span class="jf-chip"><b>' + t.length + "</b>digits</span>" +
    '<span class="jf-chip"><b>' + (/^\d{11,}$/.test(t) ? "milliseconds" : "seconds") + "</b>detected</span>" +
    '<span class="jf-chip"><b>' + Math.round(ms / 1000) + "</b>seconds</span>";
}
function tm2Run() { if ($("ts-in")) tm2Type(); }
function tm2Date() {
  const d = new Date($("ts-date").value);
  if (isNaN(d)) { $("tm2-dstat").innerHTML = ""; return; }
  $("tm2-dstat").innerHTML =
    '<span class="jf-chip"><b>' + Math.floor(d.getTime() / 1000) + "</b>seconds</span>" +
    '<span class="jf-chip"><b>' + d.getTime() + "</b>milliseconds</span>" +
    '<span class="jf-chip"><b>' + d.toISOString().slice(0, 19).replace("T", " ") + "Z</b>UTC</span>";
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
function rgbToHsv(r, g, b) {
  r /= 255; g /= 255; b /= 255;
  const max = Math.max(r, g, b), min = Math.min(r, g, b), d = max - min;
  let h = 0;
  if (d) {
    if (max === r) h = ((g - b) / d + (g < b ? 6 : 0)) / 6;
    else if (max === g) h = ((b - r) / d + 2) / 6;
    else h = ((r - g) / d + 4) / 6;
  }
  return [Math.round(h * 360), Math.round((max ? d / max : 0) * 100), Math.round(max * 100)];
}
function rgbToCmyk(r, g, b) {
  const rr = r / 255, gg = g / 255, bb = b / 255;
  const k = 1 - Math.max(rr, gg, bb);
  if (k === 1) return [0, 0, 0, 100];
  return [Math.round((1 - rr - k) / (1 - k) * 100), Math.round((1 - gg - k) / (1 - k) * 100), Math.round((1 - bb - k) / (1 - k) * 100), Math.round(k * 100)];
}
function hslToRgb(h, s, l) {
  s /= 100; l /= 100;
  const k = (n) => (n + h / 30) % 12;
  const a = s * Math.min(l, 1 - l);
  const f = (n) => l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1)));
  return [Math.round(f(0) * 255), Math.round(f(8) * 255), Math.round(f(4) * 255)];
}
function cc2Copy(txt, el) {
  (navigator.clipboard ? navigator.clipboard.writeText(txt) : Promise.reject()).then(() => {
    const old = el.textContent;
    el.classList.add("cc2-copied");
    el.textContent = "Copied!";
    setTimeout(() => { el.classList.remove("cc2-copied"); el.textContent = old; }, 1100);
  }).catch(() => {});
}
function colorConvert() {
  const raw = $("col-in").value.trim();
  const rgb = hexToRgb(raw);
  if (!rgb) { $("col-err").textContent = "Enter a valid hex color like #34d399"; return; }
  $("col-err").textContent = "";
  const [r, g, b] = rgb;
  const [h, s, l] = rgbToHsl(r, g, b);
  const [hv, sv, vv] = rgbToHsv(r, g, b);
  const [c, m, y, k] = rgbToCmyk(r, g, b);
  const hex = toHexStr(r, g, b);
  $("col-cc").value = hex.toLowerCase().slice(0, 7);
  const comp = hslToRgb((h + 180) % 360, s, l);
  $("col-swatch").style.background = hex;
  $("cc2-comp").style.background = toHexStr(...comp);
  $("cc2-comp").title = "Complementary: " + toHexStr(...comp);
  const fmts = [
    ["HEX", hex],
    ["RGB", `rgb(${r}, ${g}, ${b})`],
    ["HSL", `hsl(${h}, ${s}%, ${l}%)`],
    ["HSV", `hsv(${hv}, ${sv}%, ${vv}%)`],
    ["CMYK", `cmyk(${c}%, ${m}%, ${y}%, ${k}%)`],
  ];
  $("col-out").innerHTML = fmts.map(([name, val]) =>
    `<button class="cc2-fmt" onclick="cc2Copy('${val.replace(/'/g, "\\'")}', this)"><span class="cc2-fmt-name">${name}</span><span class="cc2-fmt-val">${val}</span></button>`).join("");
}
function cc2FromPicker() { $("col-in").value = $("col-cc").value; colorConvert(); }
function cc2Random() {
  const h = Math.floor(Math.random() * 360), s = 45 + Math.floor(Math.random() * 50), l = 35 + Math.floor(Math.random() * 40);
  $("col-in").value = toHexStr(...hslToRgb(h, s, l));
  colorConvert();
}
if ($("col-in")) colorConvert();

/* ---------- Random ---------- */
let RN2_LAST = [];
function rn2Rand(min, max) {
  const range = max - min + 1;
  const a = new Uint32Array(1);
  crypto.getRandomValues(a);
  return min + (a[0] % range);
}
function randNums() {
  const min = parseInt($("rn-min").value), max = parseInt($("rn-max").value);
  const count = Math.min(parseInt($("rn-count").value) || 1, 1000);
  const unique = $("rn-unique").checked;
  if (isNaN(min) || isNaN(max) || max < min) { $("rn2-big").innerHTML = '<span class="error">Check min &le; max</span>'; $("rn-out").innerHTML = ""; RN2_LAST = []; return; }
  const span = max - min + 1;
  if (unique && span < count) { $("rn2-big").innerHTML = '<span class="error">Range too small for ' + count + " unique values</span>"; $("rn-out").innerHTML = ""; RN2_LAST = []; return; }
  const set = new Set(), res = [];
  while (res.length < count) {
    const v = rn2Rand(min, max);
    if (!unique || !set.has(v)) { if (unique) set.add(v); res.push(v); }
  }
  RN2_LAST = res;
  rn2Render();
}
function rn2Render() {
  if (!$("rn2-big")) return;
  const vals = $("rn2-sort").checked ? RN2_LAST.slice().sort((a, b) => a - b) : RN2_LAST;
  const pad = $("rn2-justify") && $("rn2-justify").checked;
  const fmt = (v) => pad ? String(v).padStart(String(Math.max(Math.abs(parseInt($("rn-min").value)), Math.abs(parseInt($("rn-max").value)))).length, "0") : String(v);
  const sum = vals.reduce((a, b) => a + b, 0);
  const avg = vals.length ? sum / vals.length : 0;
  $("rn2-big").innerHTML = vals.length === 1 ? String(vals[0]) : vals.length + '<span class="pct2-big-sub">numbers &middot; avg ' + (Math.round(avg * 100) / 100) + "</span>";
  $("rn-out").innerHTML = vals.map((v) => '<span class="jf-chip"><b>' + fmt(v) + "</b></span>").join("");
  if (vals.length > 1) {
    $("rn2-stats").innerHTML =
      '<span class="jf-chip"><b>' + vals.length + "</b>count</span>" +
      '<span class="jf-chip"><b>' + fmt(Math.min(...vals)) + "</b>min</span>" +
      '<span class="jf-chip"><b>' + fmt(Math.max(...vals)) + "</b>max</span>" +
      '<span class="jf-chip"><b>' + sum.toLocaleString() + "</b>sum</span>" +
      '<span class="jf-chip"><b>' + (Math.round(avg * 100) / 100) + "</b>average</span>";
  } else $("rn2-stats").innerHTML = "";
}
function rn2Copy(btn) {
  if (!RN2_LAST.length) return;
  navigator.clipboard.writeText(RN2_LAST.join(", ")).catch(() => {});
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy all"), 1200);
}
if ($("rn-min")) randNums();

let CF2_HIST = [];
function cf2Best() { return parseInt(localStorage.getItem("mscale-cf2-best") || "0", 10) || 0; }
function flipCoin() {
  const n = Math.min(parseInt($("coin-n").value) || 1, 1000);
  if (!$("cf2-big")) return;
  const flips = Array.from({ length: n }, () => (crypto.getRandomValues(new Uint8Array(1))[0] & 1 ? "Tails" : "Heads"));
  CF2_HIST = flips.concat(CF2_HIST).slice(0, 12);
  const heads = flips.filter((f) => f === "Heads").length;
  const tails = n - heads;
  // streak across this flip batch (single face runs)
  let streak = 1, best = 1;
  for (let i = 1; i < flips.length; i++) {
    streak = flips[i] === flips[i - 1] ? streak + 1 : 1;
    best = Math.max(best, streak);
  }
  if (n === 1) {
    best = 1;
    if (CF2_HIST[1] === flips[0]) { /* tie into previous batch visually only */ }
  }
  const savedBest = cf2Best();
  if (best > savedBest) { CF2_BEST = best; localStorage.setItem("mscale-cf2-best", String(best)); }
  else CF2_BEST = savedBest;
  $("cf2-big").innerHTML = n === 1
    ? (flips[0] === "Heads" ? "\u{1F95E} Heads" : "\u{1F40A} Tails")
    : (heads + '<span class="pct2-big-sub">heads &middot; ' + tails + " tails</span>");
  const hp = n ? heads / n * 100 : 0;
  $("cf2-bars").innerHTML =
    '<div class="ci2-bar-row"><span>Heads</span><div class="wc-bar"><div class="wc-bar-fill" style="width:' + hp.toFixed(1) + '%"></div></div><b>' + heads + " (" + hp.toFixed(0) + "%)</b></div>" +
    '<div class="ci2-bar-row"><span>Tails</span><div class="wc-bar"><div class="wc-bar-fill near" style="width:' + (100 - hp).toFixed(1) + '%"></div></div><b>' + tails + " (" + (100 - hp).toFixed(0) + "%)</b></div>";
  $("cf2-stats").innerHTML =
    '<span class="jf-chip"><b>' + n + "</b>flips</span>" +
    '<span class="jf-chip"><b>' + (best || 0) + "</b>run streak</span>" +
    '<span class="jf-chip"><b>' + CF2_BEST + "</b>personal best</span>" +
    '<span class="jf-chip"><b>' + (Math.abs(hp - 50) < 2 && n > 30 ? "fair" : n > 30 ? "&plusmn;dev" : "\u2014") + "</b>vs 50/50</span>";
  $("cf2-hist").innerHTML = CF2_HIST.slice(0, 12).map((f, i) => '<span class="jf-chip' + (i === 0 ? '" style="border-color:var(--accent)' : "") + '"><b>' + (f === "Heads" ? "H" : "T") + "</b></span>").join("");
}
function cf2Clear() { CF2_HIST = []; if ($("cf2-hist")) $("cf2-hist").innerHTML = '<p style="color:var(--soft);font-size:13px">Flip to build a history</p>'; }

let DR2_HIST = [];
function rollDice() {
  const count = Math.min(parseInt($("dice-n").value) || 1, 20);
  const sides = parseInt($("dice-sides").value) || 6;
  const mod = parseInt($("dr2-mod").value) || 0;
  if (!$("dr2-big")) return;
  const rolls = Array.from({ length: count }, () => 1 + Math.floor(Math.random() * sides));
  const sum = rolls.reduce((a, b) => a + b, 0);
  const total = sum + mod;
  DR2_HIST = [{ rolls: rolls.slice(), total, sides, mod }].concat(DR2_HIST).slice(0, 6);
  const natMax = rolls.every((r) => r === sides);
  const natMin = rolls.every((r) => r === 1);
  $("dr2-big").innerHTML = (natMax ? "\u{1F451} " : natMin ? "\u{1F4A9} " : "") + (total.toLocaleString()) +
    '<span class="pct2-big-sub">' + count + "d" + sides + (mod ? (mod > 0 ? "+" + mod : mod) : "") + (count > 1 ? " &middot; sum &middot; avg " + (Math.round(sum / count * 10) / 10) : "") + "</span>";
  $("dice-out").innerHTML = '<span class="jf-stats" style="justify-content:center">' + rolls.map((r) =>
    '<span class="jf-chip"' + (r === sides ? ' style="border-color:#f59e0b"' : r === 1 ? ' style="border-color:var(--err)"' : "") + '><b>' + r + "</b></span>").join("") + "</span>";
  $("dr2-stats").innerHTML =
    '<span class="jf-chip"><b>1\u2013' + sides + "</b>per die</span>" +
    '<span class="jf-chip"><b>' + count + "</b>dice</span>" +
    '<span class="jf-chip"><b>' + sum + "</b>pips</span>" +
    '<span class="jf-chip"><b>' + (count * sides + mod) + "</b>max possible</span>" +
    '<span class="jf-chip"><b>' + (Math.round((count * (sides + 1) / 2 + mod) * 10) / 10) + "</b>expected</span>";
  $("dr2-hist").innerHTML = DR2_HIST.map((h) =>
    '<span class="jf-chip"><b>' + h.rolls.join("+") + (h.mod ? (h.mod > 0 ? "+" + h.mod : h.mod) : "") + "=" + h.total + '</b> ' + h.rolls.length + "d" + h.sides + "</span>").join("");
}

/* ---------- shared helpers ---------- */
function escHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
function toHexStr(r, g, b) {
  return "#" + [r, g, b].map((v) => Math.max(0, Math.min(255, Math.round(v))).toString(16).padStart(2, "0")).join("").toUpperCase();
}

/* ---------- Calculators ---------- */
function dc2Pre(v) { $("disc-off").value = v; discountCalc(); }
function discountCalc() {
  const price = parseFloat($("disc-p").value), off = parseFloat($("disc-off").value);
  const tax = parseFloat($("disc-tax").value) || 0;
  if (!$("dc2-big")) return;
  $("dc2-table").innerHTML = "";
  if (isNaN(price) || isNaN(off)) { $("dc2-big").innerHTML = "&mdash;"; $("dc2-bars").innerHTML = ""; return; }
  const saved = price * off / 100;
  const after = price - saved;
  const withTax = after * (1 + tax / 100);
  const origTax = price * (1 + tax / 100);
  $("dc2-big").innerHTML = (Math.round(withTax * 100) / 100).toFixed(2) +
    '<span class="pct2-big-sub">you pay &middot; save ' + (Math.round(saved * 100) / 100).toFixed(2) + (tax ? " &middot; incl " + tax + "% tax" : "") + "</span>";
  const denom = Math.max(price, 1);
  $("dc2-bars").innerHTML =
    '<div class="ci2-bar-row"><span>You pay</span><div class="wc-bar"><div class="wc-bar-fill" style="width:' + (after / denom * 100).toFixed(1) + '%"></div></div><b>' + (Math.round(after * 100) / 100).toFixed(2) + "</b></div>" +
    '<div class="ci2-bar-row"><span>You save</span><div class="wc-bar"><div class="wc-bar-fill near" style="width:' + (saved / denom * 100).toFixed(1) + '%"></div></div><b>' + (Math.round(saved * 100) / 100).toFixed(2) + "</b></div>" +
    (tax ? '<div class="ci2-bar-row"><span>With tax</span><div class="wc-bar"><div class="wc-bar-fill over" style="width:' + (Math.min(withTax, origTax) / denom * 100).toFixed(1) + '%"></div></div><b>' + (Math.round(withTax * 100) / 100).toFixed(2) + "</b></div>" : "");
  let rows = "";
  for (const o of [5, 10, 15, 20, 25, 30, 50, 70]) {
    const a = price * (1 - o / 100);
    const f = a * (1 + tax / 100);
    rows += `<tr><td>${o}%</td><td>${a.toFixed(2)}</td><td>${o === off ? "<b>" + f.toFixed(2) + "</b>" : f.toFixed(2)}</td><td>${(price - a).toFixed(2)}</td></tr>`;
  }
  $("dc2-table").innerHTML = '<table class="wc-table"><thead><tr><th>Discount</th><th>After discount</th>' + (tax ? "<th>After + tax</th>" : "") + "<th>You save</th></tr></thead><tbody>" + rows + "</tbody></table>";
}

function tp2Rate(r) { $("tip-pct").value = r; tipCalc(); }
function tipCalc() {
  const bill = parseFloat($("tip-bill").value), pct = parseFloat($("tip-pct").value);
  const people = Math.max(1, parseInt($("tip-people").value) || 1);
  if (isNaN(bill) || isNaN(pct)) { ["tp2-tip", "tp2-total", "tp2-per-tip", "tp2-per-total"].forEach(id => { if ($(id)) $(id).textContent = "\u2014"; }); return; }
  const tip = bill * pct / 100;
  const total = bill + tip;
  $("tp2-tip").textContent = tip.toFixed(2);
  $("tp2-total").textContent = total.toFixed(2);
  $("tp2-per-tip").textContent = (tip / people).toFixed(2);
  $("tp2-per-total").textContent = (total / people).toFixed(2);
}

if ($("tip-bill")) tipCalc();

function ci2Series(P, r, t, n, monthly) {
  const periodRate = r / 100 / n;
  const periods = Math.round(t * n);
  const contribPerPeriod = monthly * (n / 12);
  let bal = P, contributed = P;
  const yearly = [];
  for (let i = 1; i <= periods; i++) {
    bal = bal * (1 + periodRate) + contribPerPeriod;
    contributed += contribPerPeriod;
    if (i % n === 0 || i === periods) {
      const year = Math.ceil(i / n);
      if (!yearly.length || yearly[yearly.length - 1].year !== year) yearly.push({ year, bal, contributed });
    }
  }
  return { bal, contributed, interest: bal - contributed, yearly };
}
function ci2F(n) { return n.toLocaleString(undefined, { maximumFractionDigits: 2 }); }
function ci2Live() {
  const P = parseFloat($("ci-p").value), r = parseFloat($("ci-r").value);
  const t = parseFloat($("ci-t").value), n = parseInt($("ci-n").value);
  const monthly = parseFloat($("ci-monthly").value) || 0;
  if (isNaN(P) || isNaN(r) || isNaN(t) || !n || t <= 0) { $("ci2-big").innerHTML = "\u2014"; return; }
  const { bal, contributed, interest, yearly } = ci2Series(P, r, t, n, monthly);
  $("ci2-big").innerHTML = `${ci2F(bal)}<span class="pct2-big-sub">future value after ${t} year${t === 1 ? "" : "s"}</span>`;
  const max = Math.max(bal, contributed, 1);
  $("ci2-bars").innerHTML = `
    <div class="ci2-bar-row"><span>Total value</span><div class="wc-bar"><div class="wc-bar-fill" style="width:100%"></div></div><b>${ci2F(bal)}</b></div>
    <div class="ci2-bar-row"><span>You contributed</span><div class="wc-bar"><div class="wc-bar-fill near" style="width:${(contributed / max * 100).toFixed(1)}%"></div></div><b>${ci2F(contributed)}</b></div>
    <div class="ci2-bar-row"><span>Interest earned</span><div class="wc-bar"><div class="wc-bar-fill" style="width:${(interest / max * 100).toFixed(1)}%;background:#22c55e"></div></div><b>${ci2F(interest)}</b></div>`;
  const freqs = [[1, "Yearly"], [4, "Quarterly"], [12, "Monthly"], [365, "Daily"]];
  $("ci2-freq").innerHTML = freqs.map(([fn, name]) => {
    const v = ci2Series(P, r, t, fn, monthly).bal;
    return `<span class="pct2-chip">${name}: <b>${ci2F(v)}</b></span>`;
  }).join("");
  const yr = yearly.slice(0, 60);
  $("ci2-table").innerHTML = `<table class="wc-table"><thead><tr><th>Year</th><th>Balance</th><th>Contributed</th><th>Interest</th></tr></thead><tbody>` +
    yr.map((row) => `<tr><td>${row.year}</td><td><b>${ci2F(row.bal)}</b></td><td>${ci2F(row.contributed)}</td><td style="color:#22c55e">+${ci2F(row.bal - row.contributed)}</td></tr>`).join("") +
    `</tbody></table>`;
}
if ($("ci-p")) ci2Live();

let TX2_DIR = "add";
function tx2Dir(d, btn) {
  TX2_DIR = d;
  $("tx2-add").classList.toggle("active", d === "add");
  $("tx2-remove").classList.toggle("active", d === "remove");
  $("tx2-amt-label").textContent = d === "add" ? "Net amount (before tax)" : "Gross amount (incl. tax)";
  tx2Run();
}
function tx2Rate(r) { $("tax-rate").value = r; tx2Run(); }
function tx2Run() {
  const amt = parseFloat($("tax-amt").value), rate = parseFloat($("tax-rate").value);
  const big = $("tx2-big");
  if (isNaN(amt) || isNaN(rate)) { big.innerHTML = "\u2014"; $("tx2-net").textContent = $("tx2-tax").textContent = $("tx2-gross").textContent = "\u2014"; return; }
  let net, tax, gross;
  if (TX2_DIR === "add") { net = amt; tax = net * rate / 100; gross = net + tax; }
  else { gross = amt; net = gross / (1 + rate / 100); tax = gross - net; }
  big.innerHTML = `Tax: <span class="pct2-up">${tax.toFixed(2)}</span><span class="pct2-big-sub">${TX2_DIR === "add" ? `on ${net.toFixed(2)} at ${rate}%` : `inside ${gross.toFixed(2)} at ${rate}%`}</span>`;
  $("tx2-net").textContent = net.toFixed(2);
  $("tx2-tax").textContent = tax.toFixed(2);
  $("tx2-gross").textContent = gross.toFixed(2);
}
if ($("tax-amt")) tx2Run();

/* ---------- Text ---------- */
let FR2_ORIG = null, FR2_RE = null;
function fr2Run() {
  const text = $("fr-in").value, find = $("fr-find").value;
  if (!$("fr2-preview")) return;
  const words = (text.trim().match(/\S+/g) || []).length;
  let re = null;
  if (find) {
    try { re = new RegExp($("fr-regex").checked ? find : find.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), ($("fr-case").checked ? "" : "i") + "g"); }
    catch (e) {
      $("fr2-stats").innerHTML = '<span class="error">Invalid regular expression</span>';
      $("fr2-preview").innerHTML = ""; FR2_RE = null; return;
    }
  }
  FR2_RE = re;
  let matches = 0;
  if (re) { matches = (text.match(re) || []).length; }
  $("fr2-stats").innerHTML =
    '<span class="jf-chip"><b>' + matches + "</b>matches</span>" +
    '<span class="jf-chip"><b>' + words + "</b>words</span>" +
    '<span class="jf-chip"><b>' + text.length + "</b>characters</span>";
  if (!find) { $("fr2-preview").innerHTML = escHtml(text).slice(0, 5000) || '<span style="color:var(--soft)">Paste text above</span>'; return; }
  let html = "", idx = 0, m, n = 0;
  re.lastIndex = 0;
  while ((m = re.exec(text)) !== null && n < 2000) {
    html += escHtml(text.slice(idx, m.index)) + '<mark class="fr2-m">' + escHtml(m[0]) + "</mark>";
    idx = m.index + (m[0].length || 1);
    n++;
    if (!m[0].length) re.lastIndex++;
  }
  html += escHtml(text.slice(idx));
  $("fr2-preview").innerHTML = html.slice(0, 300000) || '<span style="color:var(--soft)">Paste text above</span>';
}
function fr2All(btn) {
  if (!FR2_RE || !$("fr-find").value) return;
  FR2_ORIG = $("fr-in").value;
  $("fr-in").value = FR2_ORIG.replace(FR2_RE, $("fr-repl").value);
  fr2Run();
  btn.textContent = "Replaced!";
  setTimeout(() => (btn.textContent = "Replace all"), 1200);
}
function fr2Undo() { if (FR2_ORIG !== null) { $("fr-in").value = FR2_ORIG; FR2_ORIG = null; fr2Run(); } }
function fr2Copy(btn) {
  navigator.clipboard.writeText($("fr-in").value).catch(() => {});
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy text"), 1200);
}
if ($("fr-in")) fr2Run();

let TS2_MODE = "az";
function ts2Mode(m, btn) {
  TS2_MODE = m;
  if (btn && btn.parentNode) btn.parentNode.querySelectorAll(".lr2-type").forEach((b) => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  ts2Run();
}
function ts2Run() {
  const inEl = $("sort-in");
  if (!inEl || !$("ts2-out")) return;
  const ci = $("ts2-ci").checked;
  const key = (s) => (ci ? s.toLowerCase() : s);
  let out = inEl.value.split("\n");
  if (TS2_MODE === "shuffle") {
    for (let i = out.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [out[i], out[j]] = [out[j], out[i]]; }
  } else if (TS2_MODE === "rev") out.reverse();
  else {
    out.sort((a, b) => {
      if (TS2_MODE === "az") return key(a).localeCompare(key(b));
      if (TS2_MODE === "za") return key(b).localeCompare(key(a));
      if (TS2_MODE === "len") return a.length - b.length || key(a).localeCompare(key(b));
      if (TS2_MODE === "len2") return b.length - a.length || key(a).localeCompare(key(b));
      if (TS2_MODE === "nat") return key(a).localeCompare(key(b), undefined, { numeric: true });
      return 0;
    });
  }
  if ($("ts2-noempty").checked) out = out.filter((l) => l.trim() !== "");
  if ($("ts2-dedupe").checked) {
    const s = new Set();
    out = out.filter((l) => { const k = ci ? l.toLowerCase() : l; if (s.has(k)) return false; s.add(k); return true; });
  }
  $("ts2-out").value = out.join("\n");
  $("ts2-stats").innerHTML =
    '<span class="jf-chip"><b>' + inEl.value.split("\n").length + "</b>lines in</span>" +
    '<span class="jf-chip"><b>' + out.length + "</b>lines out</span>" +
    '<span class="jf-chip"><b>' + out.join("").length + "</b>characters</span>";
}
function ts2Copy(btn) {
  $("ts2-out").value ? navigator.clipboard.writeText($("ts2-out").value).catch(() => {}) : 0;
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy result"), 1200);
}
function ts2Download() {
  const v = $("ts2-out").value;
  if (!v) return;
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([v], { type: "text/plain" }));
  a.download = "sorted-lines.txt";
  a.click();
}
function ts2Use() { $("sort-in").value = $("ts2-out").value; ts2Run(); }
if ($("sort-in")) ts2Run();

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

const WF2_STOP = new Set("the a an and or but of to in on at for with by from as is are was were be been being it its this that these those i you he she they we us our your his her them not no do does did done have has had having will would can could should shall may might must about into over under after before between during through than then when where which who whom why how all also any both each few more most other some such only own same so too very just don now one two".split(" "));
let WF2_TOPN = 10;
function wf2Top(n) {
  WF2_TOPN = n;
  [10, 25, 50].forEach((k) => $("wf2-top-" + k).classList.toggle("active", k === n));
  wordFreq();
}
function wordFreq() {
  const inEl = $("wf-in");
  if (!inEl || !$("wf-out")) return;
  const stopOn = $("wf2-stop").checked, caseSens = $("wf2-case").checked, pairs = $("wf2-pairs").checked;
  const text = inEl.value;
  const allWords = text.match(/[A-Za-z\u00c0-\u00ff0-9']+/g) || [];
  let tokens = (caseSens ? allWords : allWords.map((w) => w.toLowerCase()));
  const seq = tokens.filter((w) => w.length > 1 && (!stopOn || !WF2_STOP.has(w)));
  const sentences = (text.match(/[^.!?]+[.!?]+/g) || []).length;
  const avg = allWords.length ? (allWords.join("").replace(/'/g, "").length / allWords.length) : 0;
  $("wf2-stats").innerHTML =
    '<span class="jf-chip"><b>' + allWords.length + "</b>words</span>" +
    '<span class="jf-chip"><b>' + seq.length + "</b>" + (pairs ? "phrases" : "kept") + "</span>" +
    '<span class="jf-chip"><b>' + new Set(seq).size + "</b>unique</span>" +
    '<span class="jf-chip"><b>' + sentences + "</b>sentences</span>" +
    '<span class="jf-chip"><b>' + avg.toFixed(1) + "</b>avg length</span>";
  let items = pairs ? [] : seq;
  if (pairs) for (let i = 0; i < seq.length - 1; i++) items.push(seq[i] + " " + seq[i + 1]);
  const freq = {};
  for (const it of items) freq[it] = (freq[it] || 0) + 1;
  const top = Object.entries(freq).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])).slice(0, WF2_TOPN);
  if (!top.length) { $("wf-out").innerHTML = '<p style="color:var(--soft)">Paste text above to see the most frequent words</p>'; return; }
  const max = top[0][1];
  $("wf-out").innerHTML = top.map(([w, c]) =>
    '<div class="wf-row"><span class="wf-word">' + escHtml(w) + '</span><span class="wf-bar" style="width:' + Math.max(2, Math.round(c / max * 100)) + '%"></span><b>' + c + '</b><span class="wf-pct">' + (c / items.length * 100).toFixed(1) + '%</span></div>').join("");
}
if ($("wf-in")) wordFreq();

/* ---------- Developer ---------- */
let HG2_COPIED = null;
function hg2Click(btn) {
  if (!btn.dataset.hash) return;
  navigator.clipboard.writeText(btn.dataset.hash).catch(() => {});
  const c = btn.querySelector("code");
  if (c) { c.textContent = "Copied!"; setTimeout(() => (c.textContent = btn.dataset.hash), 1200); }
}
async function hashGen() {
  const t = $("hash-in").value;
  if (!$("hash-out")) return;
  const algos = [];
  if ($("hg2-s1").checked) algos.push("SHA-1");
  if ($("hg2-s256").checked) algos.push("SHA-256");
  if ($("hg2-s384").checked) algos.push("SHA-384");
  if ($("hg2-s512").checked) algos.push("SHA-512");
  if (!t || !algos.length) { $("hash-out").innerHTML = ""; return; }
  const data = new TextEncoder().encode(t);
  let html = "";
  for (const a of algos) {
    const d = await crypto.subtle.digest(a, data);
    const hex = [...new Uint8Array(d)].map((b) => b.toString(16).padStart(2, "0")).join("");
    const bits = { "SHA-1": 160, "SHA-256": 256, "SHA-384": 384, "SHA-512": 512 }[a];
    html += '<button type="button" class="hg2-row" data-hash="' + hex + '" onclick="hg2Click(this)"><span><b>' + a + '</b><i>' + bits + '-bit</i></span><code>' + hex + "</code></button>";
  }
  $("hash-out").innerHTML = html;
}
if ($("hash-in")) hashGen();

let JW2_PAYLOAD = "";
function jw2Hi(json) {
  return escHtml(json).replace(/("(?:[^"\\]|\\.)*")(\s*:)/g, '<span class="jf-key">$1</span>$2')
    .replace(/: ("(?:[^"\\]|\\.)*")/g, ': <span class="jf-str">$1</span>')
    .replace(/: (\d+(?:\.\d+)?)/g, ': <span class="jf-num">$1</span>')
    .replace(/: (true|false)/g, ': <span class="jf-bool">$1</span>')
    .replace(/: (null)/g, ': <span class="jf-null">$1</span>');
}
function jwtDecode() {
  if (!$("jwt-out")) return;
  const token = $("jwt-in").value.trim();
  const parts = token.split(".");
  if (!token) { $("jwt-out").innerHTML = ""; $("jw2-stats").innerHTML = ""; JW2_PAYLOAD = ""; return; }
  if (parts.length < 2) { $("jwt-out").innerHTML = '<span class="error">A JWT has three dot-separated parts &mdash; header.payload.signature</span>'; $("jw2-stats").innerHTML = ""; return; }
  const dec = (s) => { s = s.replace(/-/g, "+").replace(/_/g, "/"); while (s.length % 4) s += "="; return new TextDecoder().decode(Uint8Array.from(atob(s), (c) => c.charCodeAt(0))); };
  try {
    const ho = JSON.parse(dec(parts[0])), p = JSON.parse(dec(parts[1]));
    JW2_PAYLOAD = JSON.stringify(p, null, 2);
    let expChip = "";
    if (p.exp) {
      const e = new Date(p.exp * 1000);
      const diff = Math.floor((e - new Date()) / 1000);
      const days = Math.floor(Math.abs(diff) / 86400);
      if (diff > 0) {
        const yrs = (diff / 31557600).toFixed(1);
        expChip = '<span class="jf-chip"><b>valid</b>expires in ' + (Number(yrs) >= 1 ? yrs + " years" : Math.floor(diff / 86400) + " days") + '</span><span class="jf-chip"><b>' + e.toISOString().slice(0, 10) + "</b>expiry date</span>";
      } else {
        expChip = '<span class="jf-chip"><b>EXPIRED</b>' + days.toLocaleString() + " days ago</span>";
      }
    }
    $("jw2-stats").innerHTML =
      '<span class="jf-chip"><b>' + escHtml(String(ho.alg || "\u2014")) + "</b>algorithm</span>" +
      '<span class="jf-chip"><b>' + Object.keys(p).length + "</b>payload keys</span>" +
      '<span class="jf-chip"><b>' + escHtml(String(p.sub || "\u2014")) + "</b>subject</span>" +
      expChip +
      '<span class="jf-chip"><b>not verified</b>signature</span>';
    $("jwt-out").innerHTML = '<b>HEADER</b>\n' + jw2Hi(JSON.stringify(ho, null, 2)) + '\n\n<b>PAYLOAD</b>\n' + jw2Hi(JSON.stringify(p, null, 2)) + (parts[2] ? '\n\n<b>SIGNATURE</b>\n' + escHtml(parts[2]) + "\n<i>Signature validity is NOT checked in the browser \u2014 verify server-side.</i>" : "");
  } catch (e) { $("jwt-out").innerHTML = '<span class="error">Invalid JWT: ' + escHtml(e.message) + "</span>"; }
}
function jw2Copy(btn) {
  if (!JW2_PAYLOAD) return;
  navigator.clipboard.writeText(JW2_PAYLOAD).catch(() => {});
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy payload JSON"), 1200);
}
function jw2Sample() { $("jwt-in").value = document.getElementById("jwt-in").placeholder; jwtDecode(); }
if ($("jwt-in")) jwtDecode();

const RE2_PRESETS = {
  email: ["\\b[\\w.+-]+@[\\w-]+\\.[\\w.]+\\b", "gi"],
  url: ["https?://[^\\s\"'<>]+", "gi"],
  date: ["\\b\\d{4}-\\d{2}-\\d{2}\\b", "g"],
  hex: ["#[0-9a-f]{3,8}\\b", "gi"],
  num: ["-?\\d+(?:\\.\\d+)?", "g"],
  ip: ["\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b", "g"]
};
function re2Pre(k) {
  $("re-pattern").value = RE2_PRESETS[k][0];
  $("re-flags").value = RE2_PRESETS[k][1];
  regexTest();
}
function regexTest() {
  const text = $("re-text").value;
  if (!$("re-out")) return;
  $("re2-stats").innerHTML = "";
  let re;
  try {
    re = new RegExp($("re-pattern").value, $("re-flags").value.includes("g") ? $("re-flags").value : $("re-flags").value + "g");
  } catch (e) {
    $("re2-stats").innerHTML = '<span class="error">Invalid regex: ' + escHtml(e.message) + "</span>";
    $("re-out").textContent = ""; $("re-groups").textContent = ""; return;
  }
  const matches = [...text.matchAll(re)].slice(0, 500);
  $("re2-stats").innerHTML =
    '<span class="jf-chip"><b>' + matches.length + "</b>matches</span>" +
    '<span class="jf-chip"><b>' + text.length + "</b>chars</span>" +
    '<span class="jf-chip"><b>' + escHtml("/" + $("re-pattern").value + "/" + $("re-flags").value + "/") + "</b>pattern</span>";
  let html = "", last = 0;
  for (const m of matches) {
    if (m.index > last) html += escHtml(text.slice(last, m.index));
    html += '<mark class="fr2-m">' + escHtml(m[0]) + "</mark>";
    last = m.index + (m[0].length || 1);
  }
  html += escHtml(text.slice(last));
  $("re-out").innerHTML = html || "<span style='color:var(--soft)'>(no matches yet)</span>";
  $("re-groups").innerHTML = matches.slice(0, 20).map((m, i) =>
    '<div class="uu2-row" data-uuid="">' + `<b>#${i + 1}</b> <code>${escHtml(JSON.stringify(m[0]))}</code>` + (m.length > 1 ? " groups: " + m.slice(1).map((g) => escHtml(JSON.stringify(g))).join(", ") : "") + "</div>").join("");
}
if ($("re-text")) regexTest();

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
let CJ2_DELIM = ",";
function cj2Delim(d, btn) {
  CJ2_DELIM = d === "tb" ? "\t" : d;
  (btn.parentNode || document).querySelectorAll && btn.parentNode.querySelectorAll(".uc2-cat").forEach((b) => b.classList.remove("active"));
  btn.classList.add("active");
  csvToJson();
}
function cj2Typed(v) {
  const t = $("cj2-trim").checked ? v.trim() : v;
  if (!$("cj2-types").checked) return t;
  if (t === "") return null;
  if (/^-?\d+$/.test(t) && t.length < 16) return parseInt(t);
  if (/^-?\d*\.\d+$/.test(t)) return parseFloat(t);
  if (/^(true|false)$/i.test(t)) return t.toLowerCase() === "true";
  if (/^(null|nil)$/i.test(t)) return null;
  return t;
}
function csvToJson() {
  const inEl = $("csv-in");
  if (!inEl || !$("csv-out")) return;
  const delim = CJ2_DELIM === "tab" ? "\t" : CJ2_DELIM;
  const rows = csvParseRows(inEl.value, delim);
  if (!rows.length) { $("csv-out").value = ""; $("cj2-stats").innerHTML = '<span class="jf-chip"><b>0</b>rows</span>'; return; }
  const hasHeader = $("cj2-header").checked;
  const headers = hasHeader ? rows[0].map((h, i) => (h.trim() || "column_" + (i + 1))) : rows[0].map((_, i) => "column_" + (i + 1));
  const dataRows = hasHeader ? rows.slice(1) : rows;
  const out = dataRows.filter((r) => r.some((c) => (c || "").trim() !== "")).map((r) => Object.fromEntries(headers.map((h, i) => [h, cj2Typed(r[i] ?? "")])));
  const pretty = JSON.stringify(out, null, 2);
  $("csv-out").value = pretty;
  const nNum = out.flatMap((o) => Object.values(o)).filter((v) => typeof v === "number").length;
  $("cj2-stats").innerHTML =
    '<span class="jf-chip"><b>' + out.length + "</b>rows</span>" +
    '<span class="jf-chip"><b>' + headers.length + "</b>columns</span>" +
    '<span class="jf-chip"><b>' + new TextEncoder().encode(pretty).length + "</b>bytes</span>" +
    '<span class="jf-chip"><b>' + nNum + "</b>typed values</span>";
}
function cj2Copy(btn) {
  if (!$("csv-out").value) return;
  navigator.clipboard.writeText($("csv-out").value).catch(() => {});
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy JSON"), 1200);
}
function cj2Download() {
  if (!$("csv-out").value) return;
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([$("csv-out").value], { type: "application/json" }));
  a.download = "data.json";
  a.click();
}
if ($("csv-in")) csvToJson();

let HE2_MODE = "enc";
function he2Mode(m) {
  HE2_MODE = m;
  $("he2-enc").classList.toggle("active", m === "enc");
  $("he2-dec").classList.toggle("active", m === "dec");
  he2Live();
}
function he2Live() {
  if (!$("henc-out")) return;
  const t = $("henc-in").value;
  let r = "";
  if (HE2_MODE === "enc") {
    r = t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    if ($("he2-quotes").checked) r = r.replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  } else {
    r = t.replace(/&lt;/g, "<").replace(/&gt;/g, ">")
      .replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&#0?39;/g, "'")
      .replace(/&nbsp;/g, " ")
      .replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCodePoint(parseInt(h, 16)))
      .replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(parseInt(d, 10)))
      .replace(/&amp;/g, "&");
  }
  $("henc-out").value = r;
  $("he2-stats").innerHTML =
    '<span class="jf-chip"><b>' + t.length + "</b>chars in</span>" +
    '<span class="jf-chip"><b>' + r.length + "</b>chars out</span>" +
    '<span class="jf-chip"><b>' + (HE2_MODE === "enc" ? "entities" : "unescaped") + "</b>mode</span>";
}
function he2Swap() { $("henc-in").value = $("henc-out").value; he2Mode(HE2_MODE === "enc" ? "dec" : "enc"); }
function he2Copy(btn) {
  if (!$("henc-out").value) return;
  navigator.clipboard.writeText($("henc-out").value).catch(() => {});
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy output"), 1200);
}
if ($("henc-in")) he2Mode("enc");

/* ---------- Converters ---------- */
let NB2_FROM = 10;
function nb2Base(b, btn) {
  NB2_FROM = b;
  document.querySelectorAll("#nb2-bases .uc2-cat").forEach((c) => {
    const on = parseInt(c.dataset.b) === b;
    c.classList.toggle("active", on);
  });
  baseConvert();
}
function baseConvert() {
  if (!$("nb2-b2")) return;
  const v = $("nb-in").value.trim().replace(/^0[bxo]/i, "");
  const re = { 2: /^[01]+$/, 8: /^[0-7]+$/, 10: /^\d+$/, 16: /^[0-9a-fA-F]+$/, 36: /^[0-9a-zA-Z]+$/ }[NB2_FROM];
  if (!re || !re.test(v)) { ["nb2-b2","nb2-b8","nb2-b10","nb2-b16","nb2-b32","nb2-b36"].forEach((id) => { $(id).textContent = "\u2014"; }); $("nb2-stats").innerHTML = ""; return; }
  const n = parseInt(v, NB2_FROM);
  if (isNaN(n)) return;
  $("nb2-b2").textContent = n.toString(2);
  $("nb2-b8").textContent = n.toString(8);
  $("nb2-b10").textContent = n.toString(10);
  $("nb2-b16").textContent = n.toString(16).toUpperCase();
  $("nb2-b32").textContent = n.toString(32).toUpperCase();
  $("nb2-b36").textContent = n.toString(36).toUpperCase();
  const bits = Math.max(1, n.toString(2).length);
  $("nb2-stats").innerHTML =
    '<span class="jf-chip"><b>' + bits + "</b>bits</span>" +
    '<span class="jf-chip"><b>' + Math.ceil(bits / 8) + "</b>bytes</span>" +
    '<span class="jf-chip"><b>' + n.toString(16).length + "</b>hex digits</span>" +
    '<span class="jf-chip"><b>' + n.toLocaleString() + "</b>decimal</span>";
}
function nb2Copy() {
  if (!$("nb2-b10").textContent || $("nb2-b10").textContent === "\u2014") return;
  const all = "BIN: " + $("nb2-b2").textContent + "\nOCT: " + $("nb2-b8").textContent + "\nDEC: " + $("nb2-b10").textContent + "\nHEX: " + $("nb2-b16").textContent;
  navigator.clipboard.writeText(all).catch(() => {});
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
function romanConvert(mode) { ro2Live(); }
function ro2Live() {
  if (!$("ro2-big")) return;
  const v = $("roman-in").value.trim();
  if (!v) { $("ro2-big").innerHTML = "&mdash;"; $("ro2-break").innerHTML = ""; return; }
  if (/^\d+$/.test(v)) {
    const n = parseInt(v);
    if (n < 1 || n > 3999) { $("ro2-big").innerHTML = '<span class="error">Numbers run 1 &ndash; 3999</span>'; $("ro2-break").innerHTML = ""; return; }
    const r = arabicToRoman(n);
    const parts = [];
    let rest = n;
    [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]].forEach(([val, sym]) => {
      while (rest >= val) { parts.push(sym + "=" + val); rest -= val; }
    });
    $("ro2-big").innerHTML = `${n.toLocaleString()} <span class="pct2-big-sub-inline">=</span> <b>${r}</b>`;
    $("ro2-break").innerHTML = parts.map((p) => '<span class="jf-chip"><b>' + p.split("=")[0] + "</b>" + p.split("=")[1] + "</span>").join("");
  } else {
    const n = romanToArabic(v);
    if (isNaN(n) || n < 1) { $("ro2-big").innerHTML = '<span class="error">Invalid Roman numeral (I&ndash;MMMCMXCIX)</span>'; $("ro2-break").innerHTML = ""; return; }
    $("ro2-big").innerHTML = `<b>${escHtml(v.toUpperCase())}</b> <span class="pct2-big-sub-inline">=</span> ${n.toLocaleString()}`;
    $("ro2-break").innerHTML = '<span class="jf-chip"><b>canonical</b>' + arabicToRoman(n) + "</span>";
  }
}
function ro2Copy(btn) {
  const t = $("ro2-big").textContent.trim();
  if (!t || t === "\u2014") return;
  navigator.clipboard.writeText(t).catch(() => {});
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy result"), 1200);
}
if ($("roman-in")) ro2Live();

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
let PG2_MODE = "shades", PG2_COLORS = [];
function pg2Hsl() { const rgb = hexToRgb($("pal-in").value.trim()); if (!rgb) return null; return rgbToHsl(...rgb); }
function pg2Mode(m, btn) {
  PG2_MODE = m;
  ["shades", "comp", "analog", "triad", "tetrad", "mono"].forEach(k => $("pg2-m-" + k).classList.toggle("active", k === m));
  genPalette();
}
function pg2Palette() {
  const hsl = pg2Hsl();
  if (!hsl) return null;
  const [h, s, l] = hsl;
  if (PG2_MODE === "shades") {
    const out = [];
    for (const t of [0.8, 0.6, 0.4, 0.2]) out.push(hslToRgb(h, s, Math.min(100, l + (100 - l) * t)));
    out.push(hslToRgb(h, s, l));
    for (const t of [0.2, 0.4, 0.6, 0.8]) out.push(hslToRgb(h, s, l * (1 - t)));
    return out;
  }
  if (PG2_MODE === "comp") return [hslToRgb(h, s, l), hslToRgb((h + 180) % 360, s, l), hslToRgb(h, Math.max(0, s - 30), Math.min(95, l + 25)), hslToRgb((h + 180) % 360, s, Math.max(15, l - 25)), hslToRgb(h, Math.max(10, s - 60), 92)];
  if (PG2_MODE === "analog") return [(h + 330) % 360, (h + 345) % 360, h, (h + 15) % 360, (h + 30) % 360].map(x => hslToRgb(x % 360, s, l));
  if (PG2_MODE === "triad") return [h, (h + 120) % 360, (h + 240) % 360].flatMap(x => [hslToRgb(x, s, l), hslToRgb(x, s, Math.min(95, l + 25))]);
  if (PG2_MODE === "tetrad") return [h, (h + 90) % 360, (h + 180) % 360, (h + 270) % 360].map(x => hslToRgb(x, s, l)).flatMap(c => [c, hslToRgb(...rgbToHsl(...c), Math.min(95, l + 22))]).slice(0, 8);
  return [5, 20, 35, 50, 65, 80, 95].map(x => hslToRgb(h, s, x));
}
function genPalette() {
  const raw = $("pal-in").value.trim();
  const rgb = hexToRgb(raw);
  if (!rgb) { $("pal-err").textContent = "Enter a valid hex color like #ff7000"; return; }
  $("pal-err").textContent = "";
  $("pal-cc").value = toHexStr(...rgb).toLowerCase().slice(0, 7);
  const cols = pg2Palette();
  if (!cols) return;
  PG2_COLORS = cols.map((c) => toHexStr(...c));
  const lum = (hex) => { const [r, g, b] = hexToRgb(hex); return (0.299 * r + 0.587 * g + 0.114 * b) / 255; };
  $("pal-out").innerHTML = PG2_COLORS.map((hx) =>
    `<button class="pal-swatch" style="background:${hx};color:${lum(hx) > 0.6 ? "#111827" : "#ffffff"}" title="Click to copy ${hx}" onclick="cc2Copy('${hx}', this)"><span>${hx}</span></button>`).join("");
}
function pg2FromPicker() { $("pal-in").value = $("pal-cc").value; genPalette(); }
function pg2Random() {
  const h = Math.floor(Math.random() * 360), s = 45 + Math.floor(Math.random() * 50), l = 35 + Math.floor(Math.random() * 40);
  $("pal-in").value = toHexStr(...hslToRgb(h, s, l));
  genPalette();
}
function pg2CopyCss(btn) {
  if (!PG2_COLORS.length) return;
  const css = ":root {\n" + PG2_COLORS.map((c, i) => `  --color-${i + 1}: ${c};`).join("\n") + "\n}";
  (navigator.clipboard ? navigator.clipboard.writeText(css) : Promise.reject()).then(() => {
    btn.textContent = "CSS copied!"; setTimeout(() => { btn.textContent = "Copy CSS variables"; }, 1200);
  }).catch(() => {});
}
function pg2CopyTailwind(btn) {
  if (!PG2_COLORS.length) return;
  const names = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900"];
  const n = PG2_COLORS.length;
  const js = `colors: {\n  brand: {\n` + PG2_COLORS.map((c, i) => `    ${names[Math.round(i * 9 / Math.max(1, n - 1))]}: "${c}",`).join("\n") + `\n  },\n}`;
  (navigator.clipboard ? navigator.clipboard.writeText(js) : Promise.reject()).then(() => {
    btn.textContent = "Tailwind copied!"; setTimeout(() => { btn.textContent = "Copy Tailwind config"; }, 1200);
  }).catch(() => {});
}
if ($("pal-in")) genPalette();

/* ---------- Date & Time ---------- */
function dateDiff() {
  const a = new Date($("dd2-a").value), b = new Date($("dd2-b").value);
  if (!$("dd2-big")) return;
  $("dd2-big").innerHTML = "&mdash;"; $("dd2-ymd").textContent = $("dd2-wd").textContent = $("dd2-biz").textContent = $("dd2-hours").textContent = $("dd2-mins").textContent = "\u2014";
  $("dd2-dowchips").innerHTML = "";
  if (isNaN(a) || isNaN(b)) return;
  const inc = $("dd2-inc").checked;
  const [st, en] = a <= b ? [a, b] : [b, a];
  const enAdj = inc ? new Date(en.getFullYear(), en.getMonth(), en.getDate() + 1) : en;
  const days = Math.round((enAdj - st) / 86400000);
  if (days < 0) return;
  let y = enAdj.getFullYear() - st.getFullYear();
  let m = enAdj.getMonth() - st.getMonth();
  let d = enAdj.getDate() - st.getDate();
  if (d < 0) { m--; d += new Date(enAdj.getFullYear(), enAdj.getMonth(), 0).getDate(); }
  if (m < 0) { y--; m += 12; }
  const dowS = st.toLocaleDateString(undefined, { weekday: "long" });
  const dowE = en.toLocaleDateString(undefined, { weekday: "long" });
  $("dd2-big").innerHTML = days.toLocaleString() + '<span class="pct2-big-sub">days total</span>';
  $("dd2-dowchips").innerHTML =
    '<span class="jf-chip"><b>' + dowS + '</b>starts on</span>' +
    '<span class="jf-chip"><b>' + dowE + '</b>ends on</span>';
  const ymd = (y ? y + " year" + (y === 1 ? "" : "s") + ", " : "") + (m ? m + " month" + (m === 1 ? "" : "s") + ", " : "") + d + " day" + (d === 1 ? "" : "s");
  $("dd2-ymd").textContent = ymd;
  $("dd2-wd").textContent = Math.floor(days / 7).toLocaleString() + " week(s) + " + (days % 7) + " day(s)";
  let biz = 0;
  const cap = Math.min(days, 200000);
  for (let i = 0; i < cap; i++) {
    const dd = new Date(st.getFullYear(), st.getMonth(), st.getDate() + i);
    const w = dd.getDay();
    if (w !== 0 && w !== 6) biz++;
  }
  $("dd2-biz").textContent = days > 200000 ? "> 200k (too many to count)" : biz.toLocaleString() + " weekdays";
  $("dd2-hours").textContent = (days * 24).toLocaleString();
  $("dd2-mins").textContent = (days * 24 * 60).toLocaleString();
}

/* ---------- Batch 9+10 tools ---------- */
function dlBytes(bytes, name, type) {
  const url = URL.createObjectURL(new Blob([bytes], { type }));
  const a = document.createElement("a");
  a.href = url; a.download = name; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 4000);
}

/* PDF Merge */
let pmFiles = [], pm2Pages = [];
function pmRender() {
  const el = document.getElementById("pm-list");
  if (!el) return;
  el.innerHTML = pmFiles.map((f, i) => {
    const pg = pm2Pages[i];
    const pgTxt = pg === undefined ? "counting\u2026" : pg === null || pg === "?" ? "?" : pg + (pg === 1 ? " page" : " pages");
    return `<div class="pm2-row">` +
      `<b style="color:var(--accent);min-width:20px">${i + 1}.</b>` +
      `<span class="pm2-name">${escHtml(f.name)}</span>` +
      `<span class="pm2-meta">${(f.size / 1024).toFixed(0)} KB \u00b7 ${pgTxt}</span>` +
      `<button class="btn ghost" style="margin:0;padding:3px 9px;font-size:12px" onclick="pmMove(${i},-1)" aria-label="Move up">\u2191</button>` +
      `<button class="btn ghost" style="margin:0;padding:3px 9px;font-size:12px" onclick="pmMove(${i},1)" aria-label="Move down">\u2193</button>` +
      `<button class="btn ghost" style="margin:0;padding:3px 9px;font-size:12px" onclick="pmDel(${i})" aria-label="Remove">\u2715</button></div>`;
  }).join("");
  const st = document.getElementById("pm2-stats");
  if (st) {
    const kb = pmFiles.reduce((s, f) => s + f.size, 0) / 1024;
    const known = pm2Pages.filter((p) => typeof p === "number");
    st.innerHTML = pmFiles.length
      ? '<span class="jf-chip"><b>' + pmFiles.length + "</b>files</span>" +
        '<span class="jf-chip"><b>' + (known.length ? "~" + known.reduce((a, b) => a + b, 0) : "\u2014") + "</b>total pages</span>" +
        '<span class="jf-chip"><b>' + kb.toFixed(0) + " KB</b>combined size</span>"
      : "";
  }
}
async function pm2Count(f) {
  try {
    if (!window.PDFLib) return null;
    const doc = await window.PDFLib.PDFDocument.load(await f.arrayBuffer(), { ignoreEncryption: true });
    return doc.getPageCount();
  } catch (e) { return null; }
}
async function pm2Added() {
  pm2Pages = [];
  pmRender();
  for (let i = 0; i < pmFiles.length; i++) {
    pm2Pages[i] = await pm2Count(pmFiles[i]);
    pmRender();
  }
}
function pm2Drop(ev) {
  bi2Undrag(ev);
  const files = [...((ev.dataTransfer && ev.dataTransfer.files) || [])].filter((f) => f.type === "application/pdf" || /\.pdf$/i.test(f.name));
  if (!files.length) { out("pm-out", "<span class='error'>Only PDF files can be merged.</span>"); return; }
  pmFiles = pmFiles.concat(files);
  pm2Added();
  out("pm-out", "");
}
function pm2Clear() { pmFiles = []; pm2Pages = []; pmRender(); out("pm-out", "List cleared \u2014 drop PDFs to start again."); }
function pmMove(i, d) { const j = i + d; if (j < 0 || j >= pmFiles.length) return; [pmFiles[i], pmFiles[j]] = [pmFiles[j], pmFiles[i]]; [pm2Pages[i], pm2Pages[j]] = [pm2Pages[j], pm2Pages[i]]; pmRender(); }
function pmDel(i) { pmFiles.splice(i, 1); pm2Pages.splice(i, 1); pmRender(); }
document.addEventListener("change", (e) => {
  if (e.target && e.target.id === "pm-files") { pmFiles = [...e.target.files]; pm2Added(); }
});
async function pdfMerge() {
  if (pmFiles.length < 2) { out("pm-out", "Select at least two PDF files."); return; }
  if (!window.PDFLib) { out("pm-out", '<span class="error">PDF library still loading \u2014 try again in a second.</span>'); return; }
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
    const m = t.match(/^(\d+)\s*-\s*(\d+)$/);
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
let PS2_MODE = 0, ps2Doc = null, ps2File = null;
function ps2Mode(i, btn) {
  PS2_MODE = i;
  document.querySelectorAll(".lr2-types .lr2-type").forEach((b) => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  const rw = document.getElementById("ps2-range-wrap"), nw = document.getElementById("ps2-n-wrap");
  if (rw) rw.style.display = i === 0 ? "block" : "none";
  if (nw) nw.style.display = i === 1 ? "block" : "none";
}
async function ps2Load() {
  const f = document.getElementById("ps-file").files[0];
  if (!f) return;
  ps2File = f; ps2Doc = null;
  out("ps-out", "Reading PDF\u2026");
  out("ps2-stats", "");
  try {
    if (!window.PDFLib) throw new Error("lib loading");
    ps2Doc = await window.PDFLib.PDFDocument.load(await f.arrayBuffer(), { ignoreEncryption: true });
    out("ps2-stats",
      '<span class="jf-chip"><b>' + ps2Doc.getPageCount() + "</b>pages</span>" +
      '<span class="jf-chip"><b>' + (f.size / 1024).toFixed(0) + " KB</b>file</span>" +
      '<span class="jf-chip"><b>' + escHtml(f.name) + "</b></span>");
    out("ps-out", "");
    ps2Check();
  } catch (err) {
    out("ps-out", '<span class="error">Could not read that PDF' + (String(err.message).indexOf("lib") === 0 ? " \u2014 the library is still loading, try again in a second." : ". Is it a valid, non-encrypted file?") + '</span>');
  }
}
function ps2Check() {
  const info = document.getElementById("ps2-range-info");
  if (!info) return;
  const total = ps2Doc ? ps2Doc.getPageCount() : 0;
  if (PS2_MODE === 1) {
    const n = Math.max(1, parseInt(document.getElementById("ps-n").value) || 1);
    info.innerHTML = total ? '<span class="jf-chip"><b>' + Math.ceil(total / n) + "</b>output files</span>" +
      '<span class="jf-chip"><b>' + n + "</b>pages each</span>" : "";
    return;
  }
  const spec = document.getElementById("ps-range").value.trim();
  if (!total) { info.innerHTML = ""; return; }
  if (!spec) { info.innerHTML = '<span class="jf-chip"><b>' + total + "</b>pages (all)</span>"; return; }
  const idx = parseRanges(spec, total);
  info.innerHTML = idx
    ? '<span class="jf-chip"><b>' + idx.length + "</b>pages kept</span>"
    : '<span class="jf-chip jf-chip-bad"><b>invalid</b>range \u2014 use 1 to ' + total + "</span>";
}
function ps2Drop(ev) {
  bi2Undrag(ev);
  const f = ((ev.dataTransfer && ev.dataTransfer.files) || [])[0];
  if (!f) return;
  if (!(f.type === "application/pdf" || /\.pdf$/i.test(f.name))) { out("ps-out", "<span class='error'>That is not a PDF file.</span>"); return; }
  const inp = document.getElementById("ps-file");
  Object.defineProperty(inp, "files", { value: [f], configurable: true });
  ps2Load();
}
document.addEventListener("change", (e) => {
  if (e.target && e.target.id === "ps-file") ps2Load();
});
async function pdfSplit() {
  if (!ps2File) { out("ps-out", "Select a PDF file first."); return; }
  if (!window.PDFLib) { out("ps-out", '<span class="error">PDF library still loading \u2014 try again in a second.</span>'); return; }
  try {
    const { PDFDocument } = window.PDFLib;
    if (!ps2Doc) ps2Doc = await PDFDocument.load(await ps2File.arrayBuffer(), { ignoreEncryption: true });
    const max = ps2Doc.getPageCount();
    const base = (document.getElementById("ps-name").value || "extracted").replace(/\.pdf$/i, "");
    const multi = document.getElementById("ps2-multi");
    if (multi) multi.innerHTML = "";
    if (PS2_MODE === 0) {
      const spec = document.getElementById("ps-range").value.trim();
      const idx = spec ? parseRanges(spec, max) : Array.from({ length: max }, (_, i) => i);
      if (!idx || !idx.length) { out("ps-out", `<span class="error">Invalid range. This file has ${max} pages \u2014 use numbers from 1 to ${max}, like 1-3,5.</span>`); return; }
      const doc = await PDFDocument.create();
      (await doc.copyPages(ps2Doc, idx)).forEach((p) => doc.addPage(p));
      dlBytes(await doc.save(), base + ".pdf", "application/pdf");
      out("ps-out", `Extracted <b>${idx.length}</b> of ${max} pages. Your download has started.`);
    } else {
      const n = Math.max(1, parseInt(document.getElementById("ps-n").value) || 1);
      const links = [];
      for (let start = 0, part = 1; start < max; start += n, part++) {
        const idx = Array.from({ length: Math.min(n, max - start) }, (_, i) => start + i);
        const doc = await PDFDocument.create();
        (await doc.copyPages(ps2Doc, idx)).forEach((p) => doc.addPage(p));
        const bytes = await doc.save();
        const url = URL.createObjectURL(new Blob([bytes], { type: "application/pdf" }));
        links.push(`<a class="btn ghost" download="${base}-part${part}.pdf" href="${url}">Download part ${part} \u00b7 pages ${start + 1}\u2013${start + idx.length}</a>`);
      }
      out("ps-out", `Split <b>${max}</b> pages into <b>${links.length}</b> files \u2014 download each below.`);
      if (multi) multi.innerHTML = links.join("<br>");
      else links.forEach((l) => out("ps-out", l));
    }
  } catch (err) {
    out("ps-out", '<span class="error">Could not read the file. Is it a valid, non-encrypted PDF?</span>');
  }
}

/* Image Compressor */
let IC2_IMG = null, IC2_FILE = null;
function ic2Load(f) {
  if (!f) return;
  IC2_FILE = f;
  const img = new Image();
  img.onload = () => { IC2_IMG = img; imgCompress(); };
  img.src = URL.createObjectURL(f);
}
function ic2Fmt(v, btn) {
  const sel = document.getElementById("ic-fmt");
  if (sel) sel.value = v;
  document.querySelectorAll(".ic2-fmts .ir2-preset").forEach((b) => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  imgCompress();
}
function ic2Drop(ev) {
  bi2Undrag(ev);
  const f = ((ev.dataTransfer && ev.dataTransfer.files) || [])[0];
  if (!f) return;
  if (!/^image\//.test(f.type)) { out("ic-out", "<span class='error'>That is not an image file.</span>"); return; }
  const inp = document.getElementById("ic-file");
  Object.defineProperty(inp, "files", { value: [f], configurable: true });
  ic2Load(f);
}
document.addEventListener("change", (e) => {
  if (e.target && e.target.id === "ic-file") ic2Load(e.target.files[0]);
});
function imgCompress() {
  if (!IC2_IMG || !IC2_FILE) { out("ic-out", "Select an image to compress."); return; }
  const img = IC2_IMG, f = IC2_FILE;
  const maxW = parseInt(document.getElementById("ic-w").value) || img.width;
  const scale = Math.min(1, maxW / img.width);
  const c = document.createElement("canvas");
  c.width = Math.max(1, Math.round(img.width * scale));
  c.height = Math.max(1, Math.round(img.height * scale));
  c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
  const fmt = document.getElementById("ic-fmt").value;
  const q = parseInt(document.getElementById("ic-q").value) / 100;
  c.toBlob((b) => {
    if (!b) { out("ic-out", '<span class="error">Could not encode in this format \u2014 try JPEG.</span>'); return; }
    const kb = (z) => (z / 1024).toFixed(1) + " KB";
    const saved = Math.round((1 - b.size / f.size) * 100);
    out("ic-out", `${c.width}\u00d7${c.height}px \u00b7 saved <b>${saved}%</b> \u00b7 quality ${Math.round(q * 100)}%`);
    const st = document.getElementById("ic2-stats");
    if (st) st.innerHTML =
      '<span class="jf-chip"><b>' + kb(f.size) + "</b>original</span>" +
      '<span class="jf-chip"><b>' + kb(b.size) + "</b>compressed</span>" +
      '<span class="jf-chip"><b>' + (saved > 0 ? saved + "% smaller" : "no gain \u2014 try WebP or a lower quality") + "</b></span>" +
      '<span class="jf-chip"><b>' + c.width + "\u00d7" + c.height + "</b>pixels</span>";
    const cmp = document.getElementById("ic2-compare");
    const a = document.getElementById("ic2-a"), bz = document.getElementById("ic2-b");
    const au = URL.createObjectURL(f), bu = URL.createObjectURL(b);
    if (a) a.src = au;
    if (bz) bz.src = bu;
    const asz = document.getElementById("ic2-asz"), bsz = document.getElementById("ic2-bsz"), sv = document.getElementById("ic2-save");
    if (asz) asz.textContent = kb(f.size);
    if (bsz) bsz.textContent = kb(b.size);
    if (sv) { sv.textContent = saved > 0 ? "\u2212" + saved + "%" : "\u00b1" + Math.abs(saved) + "%"; sv.style.color = saved > 0 ? "var(--ok)" : "var(--err)"; }
    if (cmp) cmp.style.display = "flex";
    const dl = document.getElementById("ic-dl");
    if (dl) {
      if (dl.dataset.url) URL.revokeObjectURL(dl.dataset.url);
      dl.dataset.url = bu;
      dl.href = bu;
      dl.style.display = "inline-flex";
      dl.download = f.name.replace(/\.\w+$/, "") + "-compressed." + (fmt === "image/png" ? "png" : fmt === "image/webp" ? "webp" : "jpg");
    }
  }, fmt, q);
}

/* Image Cropper */
let icrImg = null;
function icrLoad() {
  const f = document.getElementById("icr-file").files[0];
  if (!f) return;
  const img = new Image();
  img.onload = () => {
    icrImg = img;
    const el = document.getElementById("icr-imgel");
    if (el) { el.src = URL.createObjectURL(f); el.style.display = "block"; }
    const dims = document.getElementById("icr-dims");
    if (dims) dims.innerHTML = '<span class="jf-chip"><b>' + img.width + "\u00d7" + img.height + "</b>pixels</span>" +
      '<span class="jf-chip"><b>' + (f.size / 1024).toFixed(0) + " KB</b>file</span>" +
      '<span class="jf-chip"><b>drag on the image</b>to select</span>';
    document.getElementById("icr-w").value = "";
    document.getElementById("icr-h").value = "";
    document.getElementById("icr-ow").value = "";
    icr2Draw();
    out("icr-out", "Image loaded. Drag a selection on it, or type the crop area.");
  };
  img.src = URL.createObjectURL(f);
}
function icr2Drop(ev) {
  bi2Undrag(ev);
  const f = ((ev.dataTransfer && ev.dataTransfer.files) || [])[0];
  if (!f) return;
  if (!/^image\//.test(f.type)) { out("icr-out", "<span class='error'>That is not an image file.</span>"); return; }
  const inp = document.getElementById("icr-file");
  Object.defineProperty(inp, "files", { value: [f], configurable: true });
  icrLoad();
}
document.addEventListener("change", (e) => {
  if (e.target && e.target.id === "icr-file") icrLoad();
});
function icr2Pre(ratio, btn) {
  if (!icrImg) return;
  const W = icrImg.width, H = icrImg.height;
  document.querySelectorAll(".ir2-presets .ir2-preset").forEach((b) => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  let w = W, h = H;
  if (ratio > 0) {
    h = Math.round(W / ratio);
    if (h > H) { h = H; w = Math.round(H * ratio); }
  }
  document.getElementById("icr-x").value = ratio ? Math.max(0, Math.round((W - w) / 2)) : 0;
  document.getElementById("icr-y").value = ratio ? Math.max(0, Math.round((H - h) / 2)) : 0;
  document.getElementById("icr-w").value = ratio ? w : "";
  document.getElementById("icr-h").value = ratio ? h : "";
  document.getElementById("icr-ow").value = "";
  icr2Draw();
}
function icr2Draw() {
  const el = document.getElementById("icr-imgel"), box = document.getElementById("icr-box");
  if (!el || !box || !icrImg || !el.clientWidth) { if (box) box.style.display = "none"; return; }
  const W = icrImg.width, H = icrImg.height;
  let x = parseInt(document.getElementById("icr-x").value) || 0;
  let y = parseInt(document.getElementById("icr-y").value) || 0;
  let w = parseInt(document.getElementById("icr-w").value) || (W - x);
  let h = parseInt(document.getElementById("icr-h").value) || (H - y);
  x = Math.max(0, Math.min(x, W - 1)); y = Math.max(0, Math.min(y, H - 1));
  w = Math.max(1, Math.min(w, W - x)); h = Math.max(1, Math.min(h, H - y));
  const sx = el.clientWidth / W, sy = el.clientHeight / H;
  box.style.display = "block";
  box.style.left = x * sx + "px";
  box.style.top = y * sy + "px";
  box.style.width = w * sx + "px";
  box.style.height = h * sy + "px";
}
let icr2DragOn = null;
function icr2Down(ev) {
  const el = document.getElementById("icr-imgel");
  if (!el || !icrImg) return;
  ev.preventDefault();
  const rect = el.getBoundingClientRect();
  const sx = icrImg.width / rect.width;
  const sy = icrImg.height / rect.height;
  const d = { x: Math.max(0, Math.round((ev.clientX - rect.left) * sx)), y: Math.max(0, Math.round((ev.clientY - rect.top) * sy)), rect, sx, sy };
  document.getElementById("icr-x").value = d.x;
  document.getElementById("icr-y").value = d.y;
  document.getElementById("icr-w").value = "0";
  document.getElementById("icr-h").value = "0";
  icr2DragOn = d;
  icr2Move(ev);
}
function icr2Move(ev) {
  if (!icr2DragOn) return;
  const d = icr2DragOn;
  const cx = Math.min(d.rect.width, Math.max(0, ev.clientX - d.rect.left));
  const cy = Math.min(d.rect.height, Math.max(0, ev.clientY - d.rect.top));
  const x2 = Math.round(cx * d.sx), y2 = Math.round(cy * d.sy);
  document.getElementById("icr-x").value = Math.min(d.x, x2);
  document.getElementById("icr-y").value = Math.min(d.y, y2);
  document.getElementById("icr-w").value = Math.abs(x2 - d.x);
  document.getElementById("icr-h").value = Math.abs(y2 - d.y);
  icr2Draw();
}
document.addEventListener("mousemove", icr2Move);
document.addEventListener("mouseup", () => { if (icr2DragOn) { icr2DragOn = null; imgCrop(); } });
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
    out("icr-out", `Cropped to <b>${w}\u00d7${h}</b> from (${x}, ${y})` + (ow !== w ? `, resized to <b>${c.width}\u00d7${c.height}</b>` : "") + ".");
    const url = URL.createObjectURL(b);
    const pv = document.getElementById("icr-preview"); pv.src = url; pv.style.display = "block";
    const dl = document.getElementById("icr-dl"); dl.href = url; dl.style.display = "inline-flex";
    dl.download = "cropped." + (fmt === "image/jpeg" ? "jpg" : "png");
  }, fmt, 0.92);
}

/* Meta Tag Generator */
let mt2IO = ["", "", "", ""], mt2Idx = 3;
function metaGen() {
  const v = (id) => { const el = document.getElementById(id); return el ? (el.value || "").trim() : ""; };
  const esc2 = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  const title = v("mt-title"), desc = v("mt-desc"), url = v("mt-url"), author = v("mt-author"), img = v("mt-img");
  const g = document.getElementById("mt-google");
  if (g) g.innerHTML = `<div style="color:#1a0dab;font-size:18px;line-height:1.3">${esc2(title || "Your page title appears here")}</div>` +
    `<div style="color:#006621;font-size:13px">${esc2(url || "https://example.com")}</div>` +
    `<div style="color:#545454;font-size:13.5px;line-height:1.45">${esc2(desc || "Your meta description appears here \u2014 aim for 140\u2013160 characters.")}</div>`;
  const st = document.getElementById("mt2-stats");
  if (st) {
    const tCl = title.length > 60 ? "jf-chip-bad" : "";
    const dCl = desc.length > 160 ? "jf-chip-bad" : "";
    st.innerHTML =
      `<span class="jf-chip ${tCl}"><b>${title.length}</b>title chars (30\u201360 ideal)</span>` +
      `<span class="jf-chip ${dCl}"><b>${desc.length}</b>description chars (70\u2013160 ideal)</span>`;
  }
  const soc = document.getElementById("mt2-social");
  if (soc) soc.innerHTML =
    (img ? `<div class="mt2-img" style="background-image:url('${esc2(img)}')"></div>`
         : `<div class="mt2-img" style="background:linear-gradient(135deg,#ff7000,#7c3aed)"></div>`) +
    `<div class="mt2-body"><span class="mt2-url">${esc2(url || "example.com")}</span>` +
    `<b>${esc2(title || "Your page title appears here")}</b>` +
    `<span>${esc2(desc || "The social share card preview appears here once you add a description.")}</span></div>`;
  const basic = [
    `<!-- Primary meta tags -->`,
    `<title>${esc2(title)}</title>`,
    `<meta name="description" content="${esc2(desc)}" />`,
    author ? `<meta name="author" content="${esc2(author)}" />` : "",
    url ? `<link rel="canonical" href="${esc2(url)}" />` : ""
  ].filter(Boolean);
  const og = [
    `<!-- Open Graph / Facebook / LinkedIn -->`,
    `<meta property="og:type" content="website" />`,
    url ? `<meta property="og:url" content="${esc2(url)}" />` : "",
    `<meta property="og:title" content="${esc2(title)}" />`,
    `<meta property="og:description" content="${esc2(desc)}" />`,
    img ? `<meta property="og:image" content="${esc2(img)}" />` : ""
  ].filter(Boolean);
  const tw = [
    `<!-- Twitter -->`,
    `<meta name="twitter:card" content="summary_large_image" />`,
    `<meta name="twitter:title" content="${esc2(title)}" />`,
    `<meta name="twitter:description" content="${esc2(desc)}" />`,
    img ? `<meta name="twitter:image" content="${esc2(img)}" />` : ""
  ].filter(Boolean);
  mt2IO = [basic.join("\n"), og.join("\n"), tw.join("\n"), basic.concat([""], og, [""], tw).join("\n")];
  mt2Show();
}
function mt2Tab(i, btn) {
  mt2Idx = i;
  document.querySelectorAll(".uc2-cats .uc2-cat").forEach((b) => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  mt2Show();
}
function mt2Show() {
  const t = document.getElementById("mt-code");
  if (t) t.value = mt2IO[mt2Idx] || "";
}
if (document.getElementById("mt-code")) metaGen();


/* Keyword Density Checker */
const KD_STOP = new Set(("a,an,the,and,or,but,if,then,else,when,at,by,for,with,about,against,between,into,through,during,before,after,above,below,to,from,up,down,in,out,on,off,over,under,again,further,once,here,there,all,any,both,each,few,more,most,other,some,such,no,nor,not,only,own,same,so,than,too,very,can,will,just,is,are,was,were,be,been,being,have,has,had,having,do,does,did,doing,would,should,could,of,it,its,this,that,these,those,i,you,he,she,we,they,them,his,her,their,our,your,my,me,as").split(","));
function kwDensity() {
  const raw = document.getElementById("kd-in").value;
  if (!$("kd-out")) return;
  const stop = $("kd-stop").checked;
  const words = raw.toLowerCase().replace(/[^\p{L}\p{N}'\u2019\- ]/gu, " ").split(/\s+/).filter(Boolean);
  if (words.length < 10) { $("kd-out").innerHTML = '<p style="color:var(--soft)">Paste at least a paragraph of text.</p>'; $("kd2-stats").innerHTML = ""; return; }
  const kept = stop ? words.filter((w) => !KD_STOP.has(w)) : words;
  const total = words.length;
  const unique = new Set(words).size;
  const sentences = (raw.match(/[^.!?]+[.!?]+/g) || []).length;
  const readMin = Math.max(1, Math.round(total / 220));
  $("kd2-stats").innerHTML =
    '<span class="jf-chip"><b>' + total + "</b>words</span>" +
    '<span class="jf-chip"><b>' + unique + "</b>unique</span>" +
    '<span class="jf-chip"><b>' + sentences + "</b>sentences</span>" +
    '<span class="jf-chip"><b>~' + readMin + " min</b>reading time</span>";
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
  const cls = (d) => d > 5 ? "over" : d > 2.5 ? "near" : "";
  const bar = (c, d) => '<div class="wc-bar"><div class="wc-bar-fill ' + cls(d) + '" style="width:' + Math.max(2, Math.round(c / max1 * 100)) + '%"></div></div>';
  const fmt = (n) => tables[n - 1].map(([g, c]) => {
    const d = c / total * 100;
    return '<div class="wf-row"><span class="wf-word" style="width:190px">' + escHtml(g) + "</span>" + bar(c, d) + "<b>" + c + "&times;</b><span class=\"wf-pct\">" + d.toFixed(1) + "%</span></div>";
  }).join("") || "<p>\u2014</p>";
  $("kd-out").innerHTML =
    "<b>One-word phrases</b>" + fmt(1) + "<br><b>Two-word phrases</b>" + fmt(2) + "<br><b>Three-word phrases</b>" + fmt(2 === 2 ? 3 : 3);
}

/* XML Sitemap Generator */
function sitemapGen() {
  const lines = document.getElementById("sm-urls").value.split("\n").map((l) => l.trim()).filter(Boolean);
  if (!document.getElementById("sm-out")) return;
  const useLm = !document.getElementById("sm-use-lastmod") || document.getElementById("sm-use-lastmod").checked;
  const lmIn = document.getElementById("sm-lastmod");
  const lm = useLm && lmIn && /^\d{4}-\d{2}-\d{2}/.test(lmIn.value || "") ? lmIn.value.slice(0, 10) : new Date().toISOString().slice(0, 10);
  const freq = document.getElementById("sm-freq").value;
  const prio = document.getElementById("sm-prio").value;
  const seen = new Set(), ok = [], bad = [];
  let dups = 0;
  for (const u of lines) {
    if (!/^https?:\/\/.+\..+/.test(u)) { bad.push(u); continue; }
    const key = u.replace(/\/+$/, "") || u;
    if (seen.has(key)) { dups++; continue; }
    seen.add(key);
    ok.push(u);
  }
  const esc2 = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  const body = ok.map((u) =>
    `  <url>\n    <loc>${esc2(u)}</loc>\n    <lastmod>${lm}</lastmod>` +
    (freq ? `\n    <changefreq>${freq}</changefreq>` : "") +
    (prio ? `\n    <priority>${prio}</priority>` : "") + `\n  </url>`).join("\n");
  const xml = ok.length ? `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${body}\n</urlset>` : "";
  document.getElementById("sm-out").value = xml;
  const st = document.getElementById("sm2-stats");
  if (st) st.innerHTML =
    '<span class="jf-chip"><b>' + ok.length + "</b>valid URLs</span>" +
    '<span class="jf-chip"><b>' + bad.length + "</b>invalid skipped</span>" +
    '<span class="jf-chip"><b>' + dups + "</b>duplicates removed</span>";
  const badd = document.getElementById("sm2-bad");
  if (badd) badd.innerHTML = bad.length
    ? "<b>Lines that were skipped (need full https:// addresses):</b><ul>" + bad.slice(0, 8).map((b) => "<li>" + escHtml(b) + "</li>").join("") + "</ul>"
    : "";
  const dl = document.getElementById("sm-dl");
  if (dl) {
    if (ok.length) {
      if (dl.dataset.url) URL.revokeObjectURL(dl.dataset.url);
      dl.dataset.url = URL.createObjectURL(new Blob([xml], { type: "application/xml" }));
      dl.href = dl.dataset.url;
      dl.style.display = "inline-flex";
    } else dl.style.display = "none";
  }
}
function sm2Robots(btn) {
  const first = (document.getElementById("sm-urls").value.split("\n").map((l) => l.trim()).find((u) => /^https?:\/\//.test(u)) || "https://example.com").replace(/\/+$/, "");
  navigator.clipboard.writeText("Sitemap: " + first + "/sitemap.xml").catch(() => {});
  if (btn) { const old = btn.textContent; btn.textContent = "Copied!"; setTimeout(() => (btn.textContent = old), 1200); }
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
let SL2_SEP = "-";
function sl2Sep(s, btn) {
  SL2_SEP = s;
  document.querySelectorAll(".ir2-presets .ir2-preset").forEach((b) => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  slugGen();
}
function slugGen() {
  const lines = document.getElementById("sl-in").value.split("\n").map((l) => l.trim()).filter(Boolean);
  const st = document.getElementById("sl2-stats");
  if (st) {
    const lens = lines.map((l) => l.length);
    const avg = lens.length ? Math.round(lens.reduce((a, b) => a + b, 0) / lens.length) : 0;
    st.innerHTML =
      '<span class="jf-chip"><b>' + lines.length + "</b>titles</span>" +
      '<span class="jf-chip"><b>' + avg + "</b>avg char</span>" +
      '<span class="jf-chip"><b>' + (lens.length ? Math.max(...lens) : 0) + "</b>longest</span>";
  }
  if (!lines.length) { document.getElementById("sl-out").value = ""; return; }
  const lower = document.getElementById("sl-lower").checked;
  const stop = document.getElementById("sl-stop").checked;
  const maxLen = parseInt(document.getElementById("sl-len").value) || 0;
  const outs = lines.map((l) => slugifyOne(l, SL2_SEP, lower, stop, maxLen));
  document.getElementById("sl-out").value = outs.join("\n");
  if (st) st.innerHTML +=
    '<span class="jf-chip"><b>' + outs.filter(Boolean).length + "</b>slugs</span>";
}
function sl2Sample() {
  const ta = document.getElementById("sl-in");
  if (!ta) return;
  ta.value = "10 Tips for Better Sleep\nCaf\u00e9 Culture in Z\u00fcrich: The Full Story!\nHow to Bake Sourdough Bread at Home in 2025";
  slugGen();
}
function sl2Download() {
  const v = document.getElementById("sl-out").value;
  if (v) dlBytes(v, "slugs.txt", "text/plain");
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
let JC2_DELIM = ",";
function jc2Delim(d, btn) {
  JC2_DELIM = d === "tb" ? "\t" : d;
  btn.parentNode.querySelectorAll(".uc2-cat").forEach((b) => b.classList.remove("active"));
  btn.classList.add("active");
  jsonToCsv();
}
function jc2Q(v) {
  if (v === null || v === undefined) return "";
  if (typeof v === "object") v = JSON.stringify(v);
  v = String(v);
  return /[",\n]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v;
}
function jsonToCsv() {
  const inEl = document.getElementById("j2c-in");
  if (!inEl || !document.getElementById("j2c-out")) return;
  $("j2c-out").value = "";
  $("jc2-stats").innerHTML = "";
  let data;
  try { data = JSON.parse(inEl.value); }
  catch (e) { $("jc2-stats").innerHTML = '<span class="error">Invalid JSON: ' + escHtml(String(e.message).slice(0, 80)) + "</span>"; return; }
  if (!Array.isArray(data) || !data.length || typeof data[0] !== "object") {
    $("jc2-stats").innerHTML = '<span class="error">Input must be a non-empty JSON array of objects.</span>'; return;
  }
  const keys = [...new Set(data.flatMap((o) => Object.keys(o)))];
  const csv = [keys.map(jc2Q).join(JC2_DELIM)].concat(data.map((o) => keys.map((k) => jc2Q(o[k])).join(JC2_DELIM))).join("\n");
  $("j2c-out").value = csv;
  $("jc2-stats").innerHTML =
    '<span class="jf-chip"><b>' + data.length + "</b>rows</span>" +
    '<span class="jf-chip"><b>' + keys.length + "</b>columns</span>" +
    '<span class="jf-chip"><b>' + new TextEncoder().encode(csv).length + "</b>bytes</span>";
}
function jc2Copy(btn) {
  if (!$("j2c-out").value) return;
  navigator.clipboard.writeText($("j2c-out").value).catch(() => {});
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy CSV"), 1200);
}
function jc2Download() {
  const v = $("j2c-out").value;
  if (!v) return;
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([v], { type: "text/csv" }));
  a.download = "data.csv";
  a.click();
}
if ($("j2c-in")) jsonToCsv();

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
/* ---- Markdown previewer extras ---- */
let MD2_VIEW = 0;
function md2Wrap(before, after) {
  const ta = document.getElementById("md-in");
  if (!ta) return;
  const s = ta.selectionStart, e = ta.selectionEnd, t = ta.value;
  ta.value = t.slice(0, s) + before + t.slice(s, e) + after + t.slice(e);
  ta.selectionStart = s + before.length; ta.selectionEnd = e + before.length;
  ta.focus(); mdRender();
}
function md2Line(prefix) {
  const ta = document.getElementById("md-in");
  if (!ta) return;
  const s = ta.selectionStart, t = ta.value;
  const ls = t.lastIndexOf("\n", s - 1) + 1;
  ta.value = t.slice(0, ls) + prefix + t.slice(ls);
  ta.selectionStart = ta.selectionEnd = s + prefix.length;
  ta.focus(); mdRender();
}
function md2View(i, btn) {
  MD2_VIEW = i;
  document.querySelectorAll(".lr2-types .lr2-type").forEach((b) => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  const col = document.getElementById("md2-prev-col"), out = document.getElementById("md-out"), ta = document.getElementById("md-html");
  if (col) col.style.display = i === 0 ? "block" : "none";
  if (ta) ta.style.display = i === 1 ? "block" : "none";
}
function md2Stats() {
  const t = document.getElementById("md-in").value;
  const el = document.getElementById("md2-stats");
  if (!el) return;
  const words = (t.trim().match(/\S+/g) || []).length;
  const readMin = Math.max(1, Math.round(words / 200));
  el.innerHTML =
    '<span class="jf-chip"><b>' + words + "</b>words</span>" +
    '<span class="jf-chip"><b>' + t.length + "</b>characters</span>" +
    '<span class="jf-chip"><b>' + (t ? t.split("\n").length : 0) + "</b>lines</span>" +
    '<span class="jf-chip"><b>~' + (words ? readMin : 0) + " min</b>reading time</span>";
}
function md2Download() {
  const html = document.getElementById("md-html").value;
  if (!html) return;
  dlBytes('<!doctype html>\n<html><head><meta charset="utf-8"><title>Markdown export</title><style>body{font-family:system-ui,sans-serif;max-width:760px;margin:40px auto;padding:0 18px;line-height:1.6}code{background:rgba(127,127,127,.15);padding:1px 5px;border-radius:4px}pre code{display:block;padding:12px}blockquote{border-left:3px solid #ccc;margin:0;padding-left:14px;color:#555}</style></head><body>\n' + html + "\n</body></html>", "markdown-export.html", "text/html");
}
function md2Sample() {
  const ta = document.getElementById("md-in");
  if (!ta) return;
  ta.value = "# Launch checklist\n\nShip the **landing page**, then verify these three things:\n\n- Form works with `@example.com` addresses\n- The *hero image* loads as WebP\n- Lighthouse score is above `90`\n\n1. Preview\n2. Publish\n3. Share\n\n> Ship small, ship often.\n\nRead the [full guide](https://example.com/launch).";
  mdRender(); md2Stats();
}
function md2Clear() {
  const ta = document.getElementById("md-in");
  if (!ta) return;
  ta.value = ""; mdRender(); md2Stats();
}
if (document.getElementById("md-out")) md2Stats();


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
let fv2Img = null, fv2IO = ["", "", ""], fv2Idx = 0;
const FV2_SIZES = [[16, "favicon-16x16.png"], [32, "favicon-32x32.png"], [48, "favicon-48x48.png"], [64, "favicon-64x64.png"], [96, "favicon-96x96.png"], [128, "favicon-128x128.png"], [180, "apple-touch-icon.png"], [192, "favicon-192.png"], [256, "favicon-256.png"], [512, "favicon-512.png"]];
function fvGen() {
  const f = document.getElementById("fv-file").files[0];
  if (!f) return;
  const img = new Image();
  img.onload = () => { fv2Img = img; fv2Render(); };
  img.src = URL.createObjectURL(f);
}
function fv2Redraw() { fv2Render(); }
function fv2Render() {
  const row = document.getElementById("fv-previews");
  if (!row || !fv2Img || !fv2Img.width) return;
  const bg = document.getElementById("fv-bg").value;
  row.innerHTML = "";
  FV2_SIZES.forEach(([s, name]) => {
    const c = document.createElement("canvas");
    c.width = c.height = s;
    const x = c.getContext("2d");
    x.fillStyle = bg; x.fillRect(0, 0, s, s);
    x.drawImage(fv2Img, 0, 0, s, s);
    const url = c.toDataURL("image/png");
    const v = Math.min(72, Math.max(24, Math.round(s / 2)));
    row.insertAdjacentHTML("beforeend",
      `<div class="fv2-item"><img src="${url}" width="${v}" height="${v}" alt="${name} preview"><b>${s}\u00d7${s}</b><span>${name}</span><a class="btn ghost" download="${name}" href="${url}">Download</a></div>`);
  });
  const c32 = document.createElement("canvas");
  c32.width = c32.height = 32;
  const x32 = c32.getContext("2d");
  x32.fillStyle = bg; x32.fillRect(0, 0, 32, 32);
  x32.drawImage(fv2Img, 0, 0, 32, 32);
  const u32 = c32.toDataURL("image/png");
  const tab = document.getElementById("fv-tab");
  if (tab) tab.src = u32;
  fv2IO = [
    '<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">\n' +
    '<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">\n' +
    '<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">\n' +
    '<link rel="manifest" href="/site.webmanifest">',
    '{\n  "name": "Your site",\n  "short_name": "Site",\n  "icons": [\n    { "src": "/favicon-192.png", "sizes": "192x192", "type": "image/png" },\n    { "src": "/favicon-512.png", "sizes": "512x512", "type": "image/png" }\n  ],\n  "theme_color": "#ffffff",\n  "background_color": "#ffffff",\n  "display": "standalone"\n}',
    '<?xml version="1.0" encoding="utf-8"?>\n<browserconfig>\n  <msapplication>\n    <tile>\n      <square150x150logo src="/favicon-192.png"/>\n      <TileColor>#' + (document.getElementById("fv-bg").value.slice(1) || "ffffff") + '</TileColor>\n    </tile>\n  </msapplication>\n</browserconfig>'
  ];
  fv2Show();
}
function fv2Tab(i, btn) {
  fv2Idx = i;
  document.querySelectorAll(".uc2-cats .uc2-cat").forEach((b) => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  fv2Show();
}
function fv2Show() {
  const t = document.getElementById("fv-tags");
  if (t) t.value = fv2IO[fv2Idx] || "";
}
/* ---- Base64 Image Encoder ---- */
function b64Enc() {
  const f = document.getElementById("b64-file").files[0];
  if (!f) return;
  bi2Load(f);
}
function bi2Load(f) {
  const r = new FileReader();
  r.onload = () => {
    const uri = String(r.result);
    document.getElementById("b64-out").value = uri;
    document.getElementById("b64-html").value = `<img src="${uri}" alt="">`;
    document.getElementById("b64-css").value = `background-image: url(${uri});`;
    const img = new Image();
    img.onload = () => {
      const kb = (b) => (b < 1024 ? b + " B" : (b / 1024).toFixed(1) + " KB");
      const pct = f.size ? Math.round((uri.length / f.size - 1) * 100) : 0;
      const info = document.getElementById("b64-info");
      if (info) info.innerHTML =
        '<span class="jf-chip"><b>' + img.width + "\u00d7" + img.height + "</b>pixels</span>" +
        '<span class="jf-chip"><b>' + kb(f.size) + "</b>file</span>" +
        '<span class="jf-chip"><b>' + kb(uri.length) + "</b>data URI \u003cspan\u003e(+" + pct + "%)</span></span>";
      const warn = document.getElementById("bi2-warn");
      if (warn) warn.innerHTML = uri.length > 100 * 1024
        ? "<b>Heads up:</b> this data URI is over 100 KB \u2014 for anything this large, hosting the image as a normal file usually parses faster and is cacheable. Data URIs shine for small icons and inline sprites."
        : "";
    };
    img.src = uri;
    const prev = document.getElementById("bi2-img");
    if (prev) prev.src = uri;
  };
  r.readAsDataURL(f);
}
function bi2Txt() {
  const v = document.getElementById("b64-out").value;
  if (v) dlBytes(v, "image-data-uri.txt", "text/plain");
}
function bi2Drag(ev) { ev.preventDefault(); const d = document.getElementById("bi2-drop"); if (d) d.classList.add("bi2-over"); }
function bi2Undrag(ev) { ev.preventDefault(); const d = document.getElementById("bi2-drop"); if (d) d.classList.remove("bi2-over"); }
function bi2Drop(ev) {
  bi2Undrag(ev);
  const f = ev.dataTransfer && ev.dataTransfer.files && ev.dataTransfer.files[0];
  if (!f) return;
  bi2Load(f);
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
function swRender() {
  const chips = document.getElementById("sw-chips");
  const laps = document.getElementById("sw-laps");
  if (!laps) return;
  const exp = document.getElementById("sw2-export");
  if (exp) exp.style.display = swLaps.length ? "flex" : "none";
  const splits = swLaps.map((l) => l.split);
  const best = splits.length > 1 ? Math.min(...splits) : null;
  const worst = splits.length > 1 ? Math.max(...splits) : null;
  if (chips) {
    const avg = splits.length ? splits.reduce((a, b) => a + b, 0) / splits.length : 0;
    chips.innerHTML =
      '  <span class="jf-chip"><b>' + swLaps.length + "</b>laps</span>" +
      '  <span class="jf-chip"><b>' + (best !== null ? swFmt(best) : "\u2014") + "</b>best lap</span>" +
      '  <span class="jf-chip"><b>' + (worst !== null ? swFmt(worst) : "\u2014") + "</b>slowest</span>" +
      '  <span class="jf-chip"><b>' + (splits.length ? swFmt(avg) : "\u2014") + "</b>average</span>";
  }
  if (!swLaps.length) { laps.innerHTML = ""; return; }
  let h = '<table class="lap-table"><thead><tr><th>Lap</th><th>Split</th><th>Total</th></tr></thead><tbody>';
  swLaps.slice().reverse().forEach((l, idx) => {
    const n = swLaps.length - idx;
    const isBest = splits.length > 1 && l.split === best;
    const isWorst = splits.length > 1 && l.split === worst;
    const cls = (isBest ? "sw2-best" : "") + (isWorst && !isBest ? " sw2-worst" : "");
    h += `<tr class="${cls} bordered"><td>${n}</td><td>${swFmt(l.split)}</td><td>${swFmt(l.total)}</td></tr>`;
  });
  laps.innerHTML = h + "</tbody></table>";
}
function swLap() {
  const total = swNow();
  if (!total) return;
  const prev = swLaps.length ? swLaps[swLaps.length - 1].total : 0;
  swLaps.push({ split: total - prev, total });
  swRender();
}
function swReset() {
  swAcc = 0; swRun = false; swLaps = [];
  clearInterval(swTimer);
  document.getElementById("sw-display").textContent = "00:00.00";
  const btn = document.getElementById("sw-start");
  if (btn) btn.textContent = "Start";
  swRender();
}
function sw2Copy(btn) {
  if (!swLaps.length) return;
  const txt = swLaps.map((l, i) => "Lap " + (i + 1) + "\t" + swFmt(l.split) + "\t" + swFmt(l.total)).join("\n");
  navigator.clipboard.writeText(txt).catch(() => {});
  if (btn) { const old = btn.textContent; btn.textContent = "Copied!"; setTimeout(() => (btn.textContent = old), 1200); }
}
function sw2Csv() {
  if (!swLaps.length) return;
  const csv = "lap,split,total\n" + swLaps.map((l, i) => (i + 1) + "," + (l.split / 1000).toFixed(2) + "," + (l.total / 1000).toFixed(2)).join("\n");
  dlBytes(csv, "stopwatch-laps.csv", "text/csv");
}
document.addEventListener("keydown", (e) => {
  if (!document.getElementById("sw-display")) return;
  const t = e.target, tag = ((t && t.tagName) || "").toLowerCase();
  if (tag === "input" || tag === "textarea" || tag === "button" || tag === "select") return;
  if (e.code === "Space") { e.preventDefault(); if (swRun) swPause(); else swStart(); }
  else if (e.code === "KeyL") { if (swRun) swLap(); }
});
if (document.getElementById("sw-display")) swRender();

/* ---- Countdown Timer ---- */
let cdTarget = 0, cdTotal = 0, cdTimer = null, cd2Last = null;
function cdStart() {
  const d = document.getElementById("cd-date").value;
  const tm = document.getElementById("cd-time-val").value || "09:00";
  if (!d) { out("cd-msg", "<span class='error'>Pick a date first.</span>"); return; }
  cdTarget = new Date(d + "T" + tm).getTime();
  cdTotal = cdTarget - Date.now();
  if (cdTotal <= 0) { out("cd-msg", "<span class='error'>That moment is already in the past \u2014 pick a future date and time.</span>"); return; }
  cd2Last = [d, tm];
  clearInterval(cdTimer);
  cdTimer = setInterval(cdTick, 250);
  const t = new Date(cdTarget);
  const names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  out("cd2-tstat",
    '<span class="jf-chip"><b>' + t.toLocaleString() + "</b>target moment</span>" +
    '<span class="jf-chip"><b>' + names[t.getDay()] + "</b>day of week</span>" +
    '<span class="jf-chip"><b>~' + Math.max(1, Math.round(cdTotal / 3600000)) + " h</b>from now</span>");
  out("cd-msg", "");
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
    const ago = -left;
    const agoTxt = ago < 60000 ? Math.round(ago / 1000) + " s" : Math.round(ago / 60000) + " min";
    out("cd-msg", `<b>Time is up!</b> Finished <b>${agoTxt}</b> ago \u2014 <a style="cursor:pointer;text-decoration:underline" onclick="cd2Arm()">restart</a>`);
    const snd = document.getElementById("cd2-sound");
    if (snd && snd.checked) cd2Bip();
    return;
  }
  const d = Math.floor(left / 86400000), h = Math.floor(left % 86400000 / 3600000),
    m = Math.floor(left % 3600000 / 60000), s = Math.floor(left % 60000 / 1000);
  document.getElementById("cd-units").innerHTML = label +
    `<div class="cd-unit"><b>${d}</b><span>Days</span></div><div class="cd-unit"><b>${h}</b><span>Hours</span></div><div class="cd-unit"><b>${m}</b><span>Minutes</span></div><div class="cd-unit"><b>${s}</b><span>Seconds</span></div>`;
  document.getElementById("cd-fill").style.width = ((1 - left / cdTotal) * 100).toFixed(2) + "%";
}
function cd2Bip() {
  try {
    const a = new (window.AudioContext || window.webkitAudioContext)();
    [0, 0.35, 0.7].forEach((t) => {
      const o = a.createOscillator(), gn = a.createGain();
      o.connect(gn); gn.connect(a.destination);
      o.frequency.value = 880; o.type = "sine";
      gn.gain.setValueAtTime(0.0001, a.currentTime + t);
      gn.gain.exponentialRampToValueAtTime(0.25, a.currentTime + t + 0.02);
      gn.gain.exponentialRampToValueAtTime(0.0001, a.currentTime + t + 0.28);
      o.start(a.currentTime + t); o.stop(a.currentTime + t + 0.3);
    });
  } catch (e) {}
}
function cd2Apply(t) {
  const dv = document.getElementById("cd-date"), tv = document.getElementById("cd-time-val");
  const iso = t.getFullYear() + "-" + String(t.getMonth() + 1).padStart(2, "0") + "-" + String(t.getDate()).padStart(2, "0");
  const tm = String(t.getHours()).padStart(2, "0") + ":" + String(t.getMinutes()).padStart(2, "0");
  dv.value = iso;
  if (tv) tv.value = tm;
  cdStart();
}
function cd2PreMin(mins) { cd2Apply(new Date(Date.now() + mins * 60000)); }
function cd2Tonight() {
  const t = new Date(); t.setHours(18, 0, 0, 0);
  if (t.getTime() <= Date.now()) t.setDate(t.getDate() + 1);
  cd2Apply(t);
}
function cd2NY() { cd2Apply(new Date(new Date().getFullYear() + 1, 0, 1, 0, 0, 0)); }
function cd2Arm() { if (cd2Last) { document.getElementById("cd-date").value = cd2Last[0]; document.getElementById("cd-time-val").value = cd2Last[1]; cdStart(); } }

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
  ["cd-date", "inv-date", "inv-due", "age-dob", "dd2-a", "dd2-b", "rd-a", "rd-b", "ad-date", "dw-date", "wn-date", "bd-a", "bd-b", "sm-lastmod"].forEach(function (id) { if ($(id)) attachDatePicker(id); });
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
  if (!document.getElementById("pw-fill")) return;
  const comp = {
    lower: (pw.match(/[a-z]/g) || []).length,
    upper: (pw.match(/[A-Z]/g) || []).length,
    digits: (pw.match(/[0-9]/g) || []).length,
    symbols: (pw.match(/[^A-Za-z0-9]/g) || []).length
  };
  let classes = 0;
  if (comp.lower) classes++;
  if (comp.upper) classes++;
  if (comp.digits) classes++;
  if (comp.symbols) classes++;
  const pool = { 0: 0, 1: 26, 2: 52, 3: 62, 4: 95 }[classes] || 0;
  const bits = pw ? Math.round(pw.length * Math.log2(pool || 2)) : 0;
  const sec = bits ? Math.pow(2, bits - 1) / 1e10 : 0;
  const lower = pw.toLowerCase();
  const issues = [];
  if (pw.length < 12) issues.push("Shorter than 12 characters \u2014 length is the cheapest entropy.");
  if (!comp.upper) issues.push("No uppercase letters.");
  if (!comp.digits) issues.push("No digits.");
  if (!comp.symbols) issues.push("No symbols.");
  if (/(.)\1{2,}/.test(pw)) issues.push("Contains repeated characters.");
  if (/(012|123|234|345|456|567|678|789|abc|bcd|cde|def|qwer|asdf)/i.test(pw)) issues.push("Contains a sequence or keyboard walk.");
  const seqlen = 0;
  if (PW_COMMON.some((c) => lower.includes(c))) issues.push("Contains a commonly leaked word.");
  const score = Math.max(0, Math.min(100, bits * 1.4 - issues.length * 8));
  const fill = document.getElementById("pw-fill");
  fill.style.width = score + "%";
  fill.style.background = score < 40 ? "var(--err)" : score < 70 ? "#fbbf24" : "var(--ok)";
  document.getElementById("pw-stats").innerHTML =
    `<div class="stat"><b>${comp.lower}</b><span>Lowercase</span></div>` +
    `<div class="stat"><b>${comp.upper}</b><span>Uppercase</span></div>` +
    `<div class="stat"><b>${comp.digits}</b><span>Digits</span></div>` +
    `<div class="stat"><b>${comp.symbols}</b><span>Symbols</span></div>` +
    `<div class="stat"><b>${bits}</b><span>Entropy bits</span></div>` +
    `<div class="stat"><b>${pwSecFmt(sec)}</b><span>Crack time</span></div>`;
  const checks = [
    ["At least 8 characters", pw.length >= 8],
    ["12+ characters recommended", pw.length >= 12],
    ["Uppercase letter", comp.upper > 0],
    ["Lowercase letter", comp.lower > 0],
    ["Digit", comp.digits > 0],
    ["Symbol", comp.symbols > 0],
    ["No triple repeats", !/(.)\1{2,}/.test(pw)],
    ["No sequences / keyboard walks", !/(012|123|234|345|456|567|678|789|abc|bcd|cde|def|qwer|asdf)/i.test(pw)],
    ["Nothing commonly leaked", !PW_COMMON.some((c) => lower.includes(c))]
  ];
  const box = document.getElementById("pw2-checks");
  if (box) box.innerHTML = checks.map(([t, ok]) =>
    `<div class="pw2-item ${ok ? "pw2-ok" : "pw2-no"}"><span class="pw2-dot"></span>${t}</div>`).join("");
  const out = document.getElementById("pw-out");
  if (out) out.innerHTML = issues.length
    ? "<b>To improve:</b><ul>" + issues.map((i) => "<li>" + escHtml(i) + "</li>").join("") + "</ul>"
    : (pw ? "<b>Excellent.</b> No structural weaknesses detected \u2014 pair it with two-factor authentication." : "");
}
function pw2Mask(btn) {
  const inp = document.getElementById("pw-in");
  if (!inp) return;
  const hidden = inp.type === "text";
  inp.type = hidden ? "password" : "text";
  if (btn) btn.textContent = hidden ? "Show" : "Hide";
  inp.focus();
}
if (document.getElementById("pw-in")) pwCheck();


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
  if (!document.getElementById("cr-out")) return;
  const parts = v.split(/\s+/);
  const el = document.getElementById("cr-out"), nextEl = document.getElementById("cr-next"), sumEl = document.getElementById("cr2-sum");
  if (nextEl) nextEl.innerHTML = "";
  if (sumEl) sumEl.innerHTML = "";
  if (!v) { el.innerHTML = ""; return; }
  if (parts.length !== 5) { el.innerHTML = "<span class='error'>Enter exactly 5 fields: minute, hour, day-of-month, month, day-of-week.</span>"; return; }
  try {
    const M = cronParseField(parts[0], 0, 59);
    const H = cronParseField(parts[1], 0, 23);
    const DOM = cronParseField(parts[2], 1, 31);
    const MON = cronParseField(parts[3], 1, 12, CRON_MON);
    const DOW = cronParseField(parts[4], 0, 6, CRON_DOW);
    if (sumEl) {
      const perDay = M.size * H.size;
      const domR = parts[2] !== "*", dowR = parts[4] !== "*";
      const daysPerWeek = domR && !dowR ? DOM.size : !domR && dowR ? DOW.size : domR && dowR ? DOM.size + DOW.size : 7;
      sumEl.innerHTML =
        '<span class="jf-chip"><b>' + perDay + "</b>runs per day</span>" +
        '<span class="jf-chip"><b>' + perDay * daysPerWeek + "</b>runs per week</span>" +
        (domR && dowR ? '<span class="jf-chip"><b>OR rule</b>day fields combined</span>' : "");
    }
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
function cr2Pre(expr) {
  const inp = document.getElementById("cr-in");
  if (!inp) return;
  inp.value = expr;
  cronExplain();
}


let cg2TypeI = 0, cg2Stops = [{ c: "#ff7000", p: 0 }, { c: "#7c3aed", p: 100 }];
function grDraw() { cg2Sync(); }
function cg2Sync() {
  const g = (id) => document.getElementById(id);
  if (!g("gr-prev") || !g("gr-out")) return;
  const a = +(g("gr-ang") ? g("gr-ang").value : 135);
  const av = document.getElementById("gr-angv");
  if (av) av.textContent = a;
  if (g("cg2-ang-wrap")) g("cg2-ang-wrap").style.display = cg2TypeI === 1 ? "none" : "flex";
  const list = cg2Stops.slice().sort((p, q) => p.p - q.p || (p.c < q.c ? -1 : 1)).map((s) => `${s.c} ${s.p}%`).join(", ");
  let css;
  if (cg2TypeI === 0) css = `linear-gradient(${a}deg, ${list})`;
  else if (cg2TypeI === 1) css = `radial-gradient(circle at center, ${list})`;
  else css = `conic-gradient(from ${a}deg, ${list})`;
  g("gr-prev").style.background = css;
  g("gr-out").value = `background: ${css};`;
}
function cg2Type(i, btn) {
  cg2TypeI = i;
  document.querySelectorAll(".lr2-types .lr2-type").forEach((b) => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  cg2Sync();
}
function cg2Seed() {
  const wrap = document.getElementById("cg2-stops");
  if (!wrap) return;
  wrap.innerHTML = cg2Stops.map((s, i) =>
    `<div class="cg2-stop">
      <input type="color" value="${s.c.length === 7 ? s.c : "#ffffff"}" oninput="cg2StopColor(${i}, this.value)">
      <input type="range" min="0" max="100" value="${s.p}" oninput="cg2StopPos(${i}, this.value, this)">
      <b>${s.p}%</b>
      <button type="button" class="btn ghost cg2-del" onclick="cg2DelStop(${i})" title="Remove stop" aria-label="Remove stop">&#10005;</button>
    </div>`).join("");
}
function cg2StopColor(i, v) { cg2Stops[i].c = v; cg2Sync(); }
function cg2StopPos(i, v, el) {
  cg2Stops[i].p = +v;
  const b = el.parentNode.querySelector("b");
  if (b) b.textContent = v + "%";
  cg2Sync();
}
function cg2DelStop(i) {
  if (cg2Stops.length <= 2) return;
  cg2Stops.splice(i, 1);
  cg2Seed(); cg2Sync();
}
function cg2AddStop() {
  if (cg2Stops.length >= 6) return;
  const cols = cg2Stops.map((s) => s.c);
  const next = ["#f59e0b", "#06b6d4", "#22c55e", "#ec4899"].find((c) => !cols.includes(c)) || "#64748b";
  cg2Stops.push({ c: next, p: 50 });
  cg2Seed(); cg2Sync();
}
function cg2Set(cols, ang) {
  cg2Stops = cols.map((c, i) => ({ c, p: Math.round(i * 100 / (cols.length - 1)) }));
  cg2Seed();
  const a = document.getElementById("gr-ang");
  if (a) a.value = ang;
  cg2Sync();
}
function cg2Random() {
  const pals = [["#f97316", "#7c3aed"], ["#06b6d4", "#3b82f6"], ["#22c55e", "#14b8a6"], ["#ec4899", "#f43f5e"], ["#eab308", "#ef4444"], ["#0ea5e9", "#8b5cf6"], ["#ef4444", "#f97316", "#eab308"], ["#14b8a6", "#3b82f6", "#8b5cf6"]];
  const p = pals[Math.floor(Math.random() * pals.length)];
  cg2Set(p, Math.floor(Math.random() * 360));
}
function cg2Tail(btn) {
  const t = document.getElementById("gr-out");
  if (!t) return;
  const css = t.value.replace(/^background: /, "").replace(/;$/, "");
  const cls = "bg-[" + css.replace(/ /g, "_") + "]";
  navigator.clipboard.writeText(cls).catch(() => {});
  if (btn) { const old = btn.textContent; btn.textContent = "Copied!"; setTimeout(() => (btn.textContent = old), 1200); }
}


function bsDraw() {
  const g = (id) => document.getElementById(id);
  if (!g("bs-box") || !g("bs-out")) return;
  const x = g("bs-x").value, y = g("bs-y").value, bl = g("bs-bl").value, sp = g("bs-sp").value;
  g("bs-xv").textContent = x; g("bs-yv").textContent = y; g("bs-blv").textContent = bl; g("bs-spv").textContent = sp;
  const opv = g("bs-op").value; g("bs-opv").textContent = opv;
  const n = parseInt(g("bs-color").value.slice(1), 16);
  const v = (g("bs-inset").checked ? "inset " : "") + `${x}px ${y}px ${bl}px ${sp}px rgba(${(n >> 16) & 255}, ${(n >> 8) & 255}, ${n & 255}, ${(opv / 100).toFixed(2)})`;
  g("bs-box").style.boxShadow = v;
  g("bs-out").value = `box-shadow: ${v};`;
}
function bs2Pre(x, y, bl, sp, col, op, inset) {
  const g = (id) => document.getElementById(id);
  if (!g("bs-box")) return;
  g("bs-x").value = x; g("bs-y").value = y; g("bs-bl").value = bl; g("bs-sp").value = sp;
  g("bs-color").value = col; g("bs-op").value = op;
  g("bs-inset").checked = !!inset;
  bsDraw();
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
function ttsStats() {
  const t = document.getElementById("tts-in").value;
  if (!document.getElementById("tts-stats")) return;
  const words = (t.trim().match(/\S+/g) || []).length;
  const rate = Math.max(0.5, parseFloat(document.getElementById("tts-rate").value) || 1);
  const mins = words / (150 * rate);
  const eta = words ? (mins < 1 ? Math.max(1, Math.round(mins * 60)) + "s" : mins.toFixed(1) + " min") : "\u2014";
  document.getElementById("tts-stats").innerHTML =
    '<span class="jf-chip"><b>' + words + "</b>words</span>" +
    '<span class="jf-chip"><b>' + t.length + "</b>characters</span>" +
    '<span class="jf-chip"><b>' + eta + "</b>est. speak time</span>";
}
function ttsPlay() {
  if (!("speechSynthesis" in window)) { out("tts-msg", "<span class='error'>Your browser does not support speech synthesis.</span>"); return; }
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(document.getElementById("tts-in").value);
  const v = ttsVoices[+document.getElementById("tts-voice").value];
  if (v) u.voice = v;
  u.rate = +document.getElementById("tts-rate").value;
  u.pitch = +document.getElementById("tts-pitch").value;
  const p = document.getElementById("tts-pause");
  if (p) p.textContent = "Pause";
  speechSynthesis.speak(u);
}
function ttsPause() {
  if (!("speechSynthesis" in window)) return;
  const btn = document.getElementById("tts-pause");
  if (speechSynthesis.paused) { speechSynthesis.resume(); if (btn) btn.textContent = "Pause"; }
  else if (speechSynthesis.speaking) { speechSynthesis.pause(); if (btn) btn.textContent = "Resume"; }
}
function ttsStop() { if ("speechSynthesis" in window) speechSynthesis.cancel(); const b = document.getElementById("tts-pause"); if (b) b.textContent = "Pause"; }
function ttsSample() {
  const el = document.getElementById("tts-in");
  el.value = "Welcome to MSCALE Tools! This free text to speech reader uses the voices already installed on your device. Adjust the speed and pitch, then press Speak again to compare.";
  ttsStats();
}
if (document.getElementById("tts-in")) ttsStats();
/* ---- Typing Speed Test ---- */
const TY_WORDS = "the of and to in is you that it he was for on are as with his they at be this have from or one had by word but not what all were we when your can said there use an each which she do how their if will up other about out many then them these so some her would make like him into time has look two more write go see number no way could people my than first water been call who oil its now find long down day did get come made may part".split(" ");
let tyList = [], tyIdx = 0, tyStart = 0, tyDone = false, tyErrWords = 0, tyTypedWords = 0, tyCorrectWords = 0;
let ty2Sec = 30, ty2Tick = null, ty2End = 0;
function tyRender() {
  document.getElementById("ty-words").innerHTML = tyList
    .map((w, i) => `<span class="ty-w${i < tyIdx ? " ty-done" : i === tyIdx ? " ty-act" : ""}">${w}</span>`)
    .join(" ");
}
function ty2Dur(sec, btn) {
  ty2Sec = sec;
  document.querySelectorAll(".ty2-dur").forEach(b => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  ty2New();
}
function ty2Best() {
  try { return parseInt(localStorage.getItem("mscale-tybest-" + ty2Sec)) || 0; } catch (e) { return 0; }
}
function ty2BestShow() {
  const b = ty2Best();
  document.getElementById("ty2-best").textContent = b ? `Your best at ${ty2Sec}s: ${b} WPM` : "";
}
function ty2TimerDisp() {
  const left = ty2End ? Math.max(0, (ty2End - Date.now()) / 1000) : ty2Sec;
  document.getElementById("ty2-timer").textContent = tyDone ? "0.0" : left.toFixed(1);
  document.getElementById("ty2-timer").classList.toggle("ty2-low", ty2End > 0 && left < 5 && !tyDone);
}
function ty2New() {
  tyList = Array.from({ length: 200 }, () => TY_WORDS[Math.floor(Math.random() * TY_WORDS.length)]);
  tyIdx = 0; tyStart = 0; tyDone = false; tyErrWords = 0; tyTypedWords = 0; tyCorrectWords = 0;
  clearInterval(ty2Tick);
  ty2End = 0;
  tyRender();
  document.getElementById("ty-in").value = "";
  document.getElementById("ty-stats").innerHTML = "";
  document.getElementById("ty2-live").innerHTML = "";
  ty2TimerDisp();
  ty2BestShow();
}
function ty2Live() {
  const mins = tyStart ? (Date.now() - tyStart) / 60000 : 0;
  const wpm = mins > 0 ? Math.round(tyCorrectWords / 5 / mins) : 0;
  const acc = tyTypedWords ? Math.round(100 * tyCorrectWords / tyTypedWords) : 100;
  document.getElementById("ty2-live").innerHTML =
    `<div class="stat"><b>${wpm}</b><span>WPM</span></div>
     <div class="stat"><b>${acc}%</b><span>Accuracy</span></div>
     <div class="stat"><b>${tyIdx}</b><span>Words</span></div>`;
}
function tyInput() {
  const inp = document.getElementById("ty-in");
  if (tyDone) return;
  if (!tyStart) {
    tyStart = Date.now();
    ty2End = tyStart + ty2Sec * 1000;
    ty2Tick = setInterval(() => {
      ty2TimerDisp();
      ty2Live();
      if (Date.now() >= ty2End) ty2Finish();
    }, 100);
  }
  const v = inp.value;
  if (v.endsWith(" ")) {
    const word = v.trim();
    if (!word) { inp.value = ""; return; }
    tyTypedWords++;
    if (word === tyList[tyIdx]) tyCorrectWords++;
    else tyErrWords++;
    tyIdx++;
    inp.value = "";
    if (tyIdx >= tyList.length) { ty2Finish(); return; }
  }
  tyRender();
  ty2Live();
}
function ty2Finish() {
  if (tyDone) return;
  tyDone = true;
  clearInterval(ty2Tick);
  ty2TimerDisp();
  const secs = tyStart ? (Math.min(Date.now(), ty2End) - tyStart) / 1000 : 0;
  const mins = secs / 60;
  const wpm = mins > 0 ? Math.round(tyCorrectWords / 5 / mins) : 0;
  const acc = tyTypedWords ? Math.round(100 * tyCorrectWords / tyTypedWords) : 0;
  let bestNote = "";
  try {
    const key = "mscale-tybest-" + ty2Sec;
    const best = parseInt(localStorage.getItem(key)) || 0;
    if (wpm > best) { localStorage.setItem(key, String(wpm)); bestNote = " \u00b7 New personal best!"; }
  } catch (e) {}
  document.getElementById("ty-stats").innerHTML =
    `<div class="stat"><b>${wpm}</b><span>Words per minute</span></div>
     <div class="stat"><b>${acc}%</b><span>Accuracy</span></div>
     <div class="stat"><b>${tyCorrectWords}</b><span>Correct words</span></div>
     <div class="stat"><b>${tyErrWords}</b><span>Wrong words</span></div>
     <div class="stat"><b>${secs.toFixed(1)}s</b><span>Time</span></div>
     <div class="stat"><b>${(tyCorrectWords / Math.max(1, secs)).toFixed(1)}</b><span>WPM raw (words/sec)</span></div>`;
  document.getElementById("ty2-live").innerHTML = `<p class="ty2-done">${wpm > 0 ? `Done \u2014 ${wpm} WPM at ${acc}% accuracy${bestNote}` : "Time's up \u2014 type a few words next time!"}</p>`;
  ty2BestShow();
}

/* ---- Pomodoro Timer ---- */
const PO_LEN = { focus: 25 * 60000, short: 5 * 60000, long: 15 * 60000 };
let poPhase = "focus", poEnd = 0, poTimer = null, poCount = 0, poLeft = 0, poRun = false, PO_CYCLE = 0;
function poFmt(ms) {
  const s = Math.max(0, Math.ceil(ms / 1000));
  return String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
}
function poLabel() { return poPhase === "focus" ? "Focus session" : poPhase === "short" ? "Short break" : "Long break"; }
function poDots() {
  const dots = document.getElementById("po-dots");
  if (dots) dots.innerHTML = [1, 2, 3, 4].map((i) => '<span class="jf-chip"><b>' + (PO_CYCLE % 4 >= i % 4 || (PO_CYCLE % 4 === 0 && PO_CYCLE > 0 && i === 4) ? "\u25CF" : "\u25CB") + "</b>cycle " + i + "</span>").join("");
}
function poTick() {
  const el = document.getElementById("po-display");
  const left = Math.max(0, poEnd - Date.now());
  const total = PO_LEN[poPhase] || 1;
  if (el) el.textContent = poFmt(left);
  const prog = document.getElementById("po-prog");
  if (prog) prog.style.width = Math.min(100, Math.round((total - left) / total * 100)) + "%";
  if (left <= 0 && poRun) { poNext(); return; }
}
function poBeep() {
  const want = document.getElementById("po-sound");
  if (want && !want.checked) return;
  try {
    const ac = new (window.AudioContext || window.webkitAudioContext)();
    const o = ac.createOscillator(), g = ac.createGain();
    o.connect(g); g.connect(ac.destination);
    o.frequency.value = 880; g.gain.value = 0.08;
    o.start(); o.stop(ac.currentTime + 0.18);
    setTimeout(() => { try { o.frequency.value = 660; o.start(); o.stop(ac.currentTime + 0.22); } catch (e) {} }, 240);
  } catch (e) {}
}
function poNext() {
  if (poPhase === "focus") {
    poCount++;
    PO_CYCLE++;
    poCountEl();
    try { const t = parseInt(localStorage.getItem("mscale-pomo-total") || "0", 10) || 0; localStorage.setItem("mscale-pomo-total", String(t + 1)); } catch (e) {}
    poPhase = PO_CYCLE % 4 === 0 ? "long" : "short";
  } else poPhase = "focus";
  poEnd = Date.now() + PO_LEN[poPhase];
  document.getElementById("po-mode").textContent = poLabel();
  poBeep();
  poTick();
}
function poCountEl() {
  const el = document.getElementById("po-count");
  if (el) el.innerHTML = "Completed focus sessions: <b>" + poCount + "</b>" + (localStorage.getItem("mscale-pomo-total") ? " <span style='color:var(--soft)'>&middot; all-time " + localStorage.getItem("mscale-pomo-total") + "</span>" : "");
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
  else { poLeft = 0; poEnd = Date.now(); poNext(); }
}
function poReset() {
  clearInterval(poTimer);
  poRun = false; poPhase = "focus"; poCount = 0; poLeft = 0; poEnd = 0; PO_CYCLE = 0;
  document.getElementById("po-display").textContent = poFmt(PO_LEN.focus);
  document.getElementById("po-mode").textContent = "Focus session";
  poCountEl();
  document.getElementById("po-start").textContent = "Start";
  const prog = document.getElementById("po-prog");
  if (prog) prog.style.width = "0%";
  poDots();
}
function poShow(phase, btn) {
  if (btn && btn.parentNode) btn.parentNode.querySelectorAll(".lr2-type").forEach((b) => b.classList.remove("active"));
  if (btn) btn.classList.add("active");
  clearInterval(poTimer);
  poRun = false; poPhase = phase; poLeft = 0;
  document.getElementById("po-mode").textContent = poLabel();
  document.getElementById("po-display").textContent = poFmt(PO_LEN[phase]);
  document.getElementById("po-start").textContent = "Start";
  const prog = document.getElementById("po-prog");
  if (prog) prog.style.width = "0%";
}
function poSetLen() {
  const f = Math.max(1, parseInt(document.getElementById("po-focus-len").value) || 25);
  const s = Math.max(1, parseInt(document.getElementById("po-short-len").value) || 5);
  const l = Math.max(1, parseInt(document.getElementById("po-long-len").value) || 15);
  PO_LEN.focus = f * 60000; PO_LEN.short = s * 60000; PO_LEN.long = l * 60000;
  if (!poRun && !poLeft) { poEnd = 0; poShowInit(); }
}
function poShowInit() {
  document.getElementById("po-display").textContent = poFmt(PO_LEN[poPhase]);
}
if (document.getElementById("po-display")) { poCountEl(); poDots(); }

/* ---- URL Parser ---- */
function up2CopyJson(btn) {
  const v = document.getElementById("up-in").value.trim();
  let u;
  try { u = new URL(v); } catch (e) { return; }
  const params = {};
  u.searchParams.forEach((val, k) => { params[k] = val; });
  const obj = {
    href: u.href, protocol: u.protocol.replace(":", ""), username: u.username || null,
    hostname: u.hostname, port: u.port || null, pathname: u.pathname,
    search: u.search || null, hash: u.hash ? u.hash.slice(1) : null, params
  };
  const txt = JSON.stringify(obj, null, 2);
  navigator.clipboard.writeText(txt).catch(() => {});
  const el = document.getElementById("up2-json");
  if (el) el.innerHTML = escHtml(txt);
  btn.textContent = "Copied!";
  setTimeout(() => (btn.textContent = "Copy as JSON"), 1200);
}
function urlParse() {
  const v = document.getElementById("up-in").value.trim();
  const el = document.getElementById("up-out");
  if (!el) return;
  if (!v) { el.innerHTML = ""; if (document.getElementById("up2-stats")) document.getElementById("up2-stats").innerHTML = ""; return; }
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
    ["Path segments", u.pathname.split("/").filter(Boolean).length],
    ["Origin", u.origin],
    ["Fragment", u.hash ? u.hash.slice(1) : "\u2014"],
  ];
  let params = "";
  if (u.search) {
    const entries = [...u.searchParams.entries()];
    params = "<label>Query parameters (decoded \u2014 click to copy the value)</label>" + entries
      .map(([k, val], i) => '<button type="button" class="uu2-row" data-uuid="' + escHtml(val).replace(/"/g, "&quot;") + '" onclick="up2Copy(this)"><b>' + escHtml(k) + "</b> = <code>" + escHtml(val) + "</code></button>").join("");
  }
  el.innerHTML = '<table class="wc-table"><tbody>' + rows.map(([k, val]) => `<tr><th>${k}</th><td>${escHtml(String(val))}</td></tr>`).join("") + "</tbody></table>" + params;
  const st = document.getElementById("up2-stats");
  if (st) st.innerHTML =
    '<span class="jf-chip"><b>' + ([...u.searchParams.keys()].length) + "</b>params</span>" +
    '<span class="jf-chip"><b>' + v.length + "</b>chars</span>" +
    '<span class="jf-chip"><b>' + (u.protocol === "https:" ? "secure" : "NOT secure") + "</b>scheme</span>";
}
function up2Copy(btn) {
  if (!btn.dataset.uuid) return;
  navigator.clipboard.writeText(btn.dataset.uuid).catch(() => {});
  const c = btn.querySelector("code");
  if (c) { c.textContent = "Copied!"; setTimeout(() => (c.textContent = btn.dataset.uuid), 1200); }
}

/* Initial render for tools that need it */
(function () {
  if (document.getElementById("gr-prev")) { cg2Seed(); cg2Sync(); }
  if (document.getElementById("bs-box")) bsDraw();
  if (document.getElementById("ty-words")) ty2New();
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


/* ---------- File hashing (Hash Generator) ---------- */
function hf2Algos() {
  var out = [];
  [["1", "SHA-1"], ["256", "SHA-256"], ["384", "SHA-384"], ["512", "SHA-512"]].forEach(function (a) {
    var el = document.getElementById("hg2-s" + a[0]);
    if (el && el.checked) out.push(a);
  });
  return out;
}
function hf2Digest(bytes, algo) {
  return crypto.subtle.digest("SHA-" + algo, bytes).then(function (h) {
    return Array.from(new Uint8Array(h)).map(function (b) { return b.toString(16).padStart(2, "0"); }).join("");
  });
}
let HF2_LAST = {};
async function hf2File(f) {
  const box = document.getElementById("hg2-fout"), stats = document.getElementById("hg2-fstats");
  if (!box) return;
  if (!f) return;
  const algos = hf2Algos();
  if (!algos.length) { box.innerHTML = "<span class='error'>Tick at least one algorithm above.</span>"; return; }
  box.innerHTML = "Hashing <b>" + escHtml(f.name) + "</b>\u2026";
  try {
    const buf = await f.arrayBuffer();
    HF2_LAST = {};
    for (const [n, label] of algos) HF2_LAST[label] = await hf2Digest(buf, n);
    const size = (f.size / 1024).toFixed(1) + " KB";
    if (stats) stats.innerHTML =
      '<span class="jf-chip"><b>' + escHtml(f.name) + "</b>" + size + '</span>' +
      '<span class="jf-chip"><b>' + algos.length + "</b>hashes</span>" +
      '<span class="jf-chip"><b>local</b>never uploaded</span>';
    box.innerHTML = Object.entries(HF2_LAST).map(function (e) {
      return '<div class="hg2-row"><b>' + e[0] + '</b><code class="clickable" onclick="copyText(this.textContent,this)' + '">' + e[1] + "</code></div>";
    }).join("");
    hf2Check();
  } catch (e) {
    box.innerHTML = "<span class='error'>Could not read that file.</span>";
  }
}
function hf2Drop(ev) { bi2Undrag(ev); const f = ((ev.dataTransfer && ev.dataTransfer.files) || [])[0]; if (f) hf2File(f); }
function hf2Pick() { const inp = document.getElementById("hg2-file"); if (inp) inp.click(); }
function hf2Check() {
  const wob = document.getElementById("hg2-fout");
  if (!wob || wob.querySelector(".error")) {
    if (wob) wob.innerHTML = wob.innerHTML; /* keep */
  }
  const want = (document.getElementById("hg2-expect").value || "").trim().toLowerCase();
  if (!want) {
    const stats = document.getElementById("hg2-fstats");
    if (stats && HF2_LAST && Object.keys(HF2_LAST).length) {
      const c = stats.querySelector(".jf-chip-bad, .jf-chip.ok");
      if (c) c.remove();
    }
    return;
  }
  Object.entries(HF2_LAST).forEach(function (e) {
    if (e[1] === want) wob.insertAdjacentHTML("afterbegin", '<div class="jf-stats" style="margin:0 0 6px"><span class="jf-chip ok"><b>MATCH</b>' + e[0] + " verified \u2014 the file is bit-for-bit identical.</span></div>");
  });
}
/* ---------- Color contrast + tint/shade ramps (Color Converter) ---------- */
function cc2Parse(colStr) {
  const s = (colStr || "").trim().toLowerCase();
  let m = s.match(/^#([0-9a-f]{6})$/);
  if (m) return [parseInt(m[1].slice(0, 2), 16), parseInt(m[1].slice(2, 4), 16), parseInt(m[1].slice(4, 6), 16)];
  m = s.match(/^#([0-9a-f]{3})$/);
  if (m) return m[1].split("").map(function (c) { return parseInt(c + c, 16); });
  m = s.match(/^rgba?\((\d+)[,\s]+(\d+)[,\s]+(\d+)/);
  if (m) return [+m[1], +m[2], +m[3]];
  return null;
}
function cc2Lum(rgb) {
  const lin = rgb.map(function (v) {
    const c = v / 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2];
}
function cc2Ratio(fg, bg) {
  const a = cc2Lum(fg), b = cc2Lum(bg);
  return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
}
function cc2CcChip(ratio, label) {
  const aa = ratio >= 4.5, aaa = ratio >= 7;
  const cls = !aa ? "jf-chip-bad" : aaa ? "ok" : "";
  return '<span class="jf-chip ' + cls + '"><b>' + ratio.toFixed(1) + ":1</b>on " + label + (aaa ? " \u00b7 AAA" : aa ? " \u00b7 AA" : " \u00b7 fails AA") + "</span>";
}
function cc2Extras() {
  const rgb = cc2Parse(($("col-in") || {}).value);
  if (!rgb) return;
  const wrap = document.getElementById("cc2-contrast");
  if (wrap) {
    const rw = cc2Ratio(rgb, [255, 255, 255]), rb = cc2Ratio(rgb, [0, 0, 0]);
    wrap.innerHTML = cc2CcChip(rw, "white") + cc2CcChip(rb, "black") +
      '<span class="jf-chip"><b>' + (rw >= rb ? "white" : "black") + "</b>best text on this colour</span>";
  }
  const ramps = document.getElementById("cc2-ramps");
  if (ramps) {
    const mix = function (t, other) {
      return rgb.map(function (v, i) { return Math.round(v + (other[i] - v) * t).toString(16).padStart(2, "0"); });
    };
    const hex2 = function (rg) { return "#" + rg.map(function (x) { return (Number(x).toString(16).padStart(2, "0")); }).join(""); };
    const hexStr = function (parts) { return "#" + parts.join(""); };
    let h = "";
    [0.8, 0.6, 0.4, 0.2].forEach(function (t) { h += '<button type="button" class="cc2-swatch" style="background:' + hexStr(mix(t, [255, 255, 255])) + '" data-c="' + hexStr(mix(t, [255, 255, 255])) + '" onclick="copyText(this.dataset.c,this)" title="Tint ' + Math.round(t * 100) + '%"></button>'; });
    h += '<button type="button" class="cc2-swatch" style="background:' + hex2(rgb) + '" data-c="' + hex2(rgb) + '" onclick="copyText(this.dataset.c,this)" title="Base"></button>';
    [0.2, 0.4, 0.6, 0.8].forEach(function (t) { h += '<button type="button" class="cc2-swatch" style="background:' + hexStr(mix(t, [0, 0, 0])) + '" data-c="' + hexStr(mix(t, [0, 0, 0])) + '" onclick="copyText(this.dataset.c,this)" title="Shade ' + Math.round(t * 100) + '%"></button>'; });
    ramps.innerHTML = h;
  }
}
(function () {
  const old = colorConvert;
  colorConvert = function () { old(); cc2Extras(); };
  const oldPick = cc2FromPicker;
  cc2FromPicker = function () { oldPick(); cc2Extras(); };
  const oldRand = cc2Random;
  cc2Random = function () { oldRand(); cc2Extras(); };
  cc2Extras();
})();


/* ---------- DT2: shared upgrades for the date micro-tools (overrides the originals above) ---------- */
function dt2Chip(b, label, bad) { return '<span class="jf-chip' + (bad ? " jf-chip-bad" : "") + '"><b>' + b + "</b>" + label + "</span>"; }
function dt2IsoWeek(d) {
  var t = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
  var dow = (t.getUTCDay() + 6) % 7;
  t.setUTCDate(t.getUTCDate() - dow + 3);
  var ft = new Date(Date.UTC(t.getUTCFullYear(), 0, 4));
  var fd = (ft.getUTCDay() + 6) % 7;
  ft.setUTCDate(ft.getUTCDate() - fd + 3);
  return { year: t.getUTCFullYear(), week: 1 + Math.round((t - ft) / (7 * 86400000)) };
}
function dt2Ins(date) {
  var wrap = document.getElementById("dt2-ins");
  if (!wrap || !date || isNaN(date)) return;
  var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  var doy = Math.floor((date - new Date(date.getFullYear(), 0, 1)) / 86400000) + 1;
  var iso = dt2IsoWeek(date);
  var now = new Date();
  var base = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  var tgt = new Date(date.getFullYear(), date.getMonth(), date.getDate());
  var rel = Math.round((tgt - base) / 86400000);
  var relTxt = rel === 0 ? "today" : rel > 0 ? "in " + rel.toLocaleString() + " d" : Math.abs(rel).toLocaleString() + " d ago";
  var q = "Q" + (Math.floor(date.getMonth() / 3) + 1);
  wrap.innerHTML =
    dt2Chip(days[date.getDay()], "weekday") +
    dt2Chip(doy.toLocaleString(), "day of year") +
    dt2Chip("W" + iso.week + " " + iso.year, "ISO week") +
    dt2Chip(relTxt, "from today") +
    dt2Chip(q, "quarter");
}
function dt2InsDur(seconds) {
  var wrap = document.getElementById("dt2-ins");
  if (!wrap || seconds === null || seconds === undefined || isNaN(seconds) || seconds < 0) return;
  seconds = Math.round(seconds);
  wrap.innerHTML =
    dt2Chip((seconds / 3600).toFixed(2), "decimal hours") +
    dt2Chip((seconds / 60).toFixed(1), "minutes") +
    dt2Chip((seconds / 28800).toFixed(2), "8-h workdays") +
    dt2Chip(seconds.toLocaleString(), "total seconds");
}
function dt2Copy(id, btn) { var el = $(id); if (el) copyText(el.textContent.replace(/\s+/g, " ").trim(), btn); }
function ad2Pre(n) { if ($("ad-n")) $("ad-n").value = String(n); dtAddDays(); }
function dw2Pre(offset) { var d = new Date(); d.setDate(d.getDate() + offset); if ($("dw-date")) $("dw-date").value = dISO(d); dtDow(); }
function wn2Off(offset) { var d = new Date(); d.setDate(d.getDate() + offset); if ($("wn-date")) $("wn-date").value = dISO(d); dtWeekNum(); }
function lp2Pre(y) { if ($("lp-y")) $("lp-y").value = String(y); dtLeap(); }
function s2Pre(s) { if ($("s2-sec")) $("s2-sec").value = String(s); dtS2Hms(); }
function h2Pre(h, m, s) { if ($("h2-h")) $("h2-h").value = String(h); if ($("h2-m")) $("h2-m").value = String(m); if ($("h2-s")) $("h2-s").value = String(s); dtHms2S(); }
function mt2Preset(v) { if ($("mt-tv")) $("mt-tv").value = v; if ($("mt-time")) $("mt-time").value = v; dtMilitary(); }
function mt2Now() { var d = new Date(); mt2Preset(String(d.getHours()).padStart(2, "0") + ":" + String(d.getMinutes()).padStart(2, "0")); }
function bd2Pre(mode) {
  var t = new Date(), a, b;
  if (mode === "month") { a = new Date(t.getFullYear(), t.getMonth(), 1); b = new Date(t.getFullYear(), t.getMonth() + 1, 0); }
  else if (mode === "q") { var q0 = Math.floor(t.getMonth() / 3) * 3; a = new Date(t.getFullYear(), q0, 1); b = new Date(t.getFullYear(), q0 + 3, 0); }
  else { a = new Date(t); b = new Date(t); b.setDate(b.getDate() + 30); }
  if ($("bd-a")) $("bd-a").value = dISO(a);
  if ($("bd-b")) $("bd-b").value = dISO(b);
  dtBizDays();
}
function dt2MilChips(v) {
  var m = (v || "").match(/^\s*(\d{1,2}):(\d{2})\s*$/);
  if (!m || +m[1] > 23 || +m[2] > 59) return;
  var h = +m[1], mi = +m[2];
  dt2Ins(new Date(2000, 0, 2, h, mi, 0));
}

function dtAddDays() {
  var d = _v("ad-date"), n = _n("ad-n");
  if (!d || n === null) { out("ad-out", "Pick a date and enter a number of days.", "err"); if (document.getElementById("dt2-ins")) document.getElementById("dt2-ins").innerHTML = ""; return; }
  var r = pISO(d); r.setDate(r.getDate() + n);
  var skip = document.getElementById("ad2-wk") && document.getElementById("ad2-wk").checked && (r.getDay() === 0 || r.getDay() === 6);
  var note = "";
  if (skip) { note = r.getDay() === 6 ? "<br><span class=\"dim\">Landed on a Saturday \u2014 moved to Monday.</span>" : "<br><span class=\"dim\">Landed on a Sunday \u2014 moved to Monday.</span>"; r.setDate(r.getDay() === 6 ? r.getDate() + 2 : r.getDate() + 1); }
  var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  out("ad-out", "<b>" + dISO(r) + "</b><br>" + days[r.getDay()] + ", " + r.toLocaleDateString(undefined, { year: "numeric", month: "long", day: "numeric" }) + note);
  dt2Ins(r);
}
function dtDow() {
  var d = _v("dw-date");
  if (!d) { out("dw-out", "Pick a date first.", "err"); return; }
  var r = pISO(d);
  var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  var start = new Date(r.getFullYear(), 0, 1);
  var doy = Math.floor((r - start) / 86400000) + 1;
  out("dw-out", "<b>" + days[r.getDay()] + "</b><br>" + r.toLocaleDateString(undefined, { year: "numeric", month: "long", day: "numeric" }) + " &nbsp;\u00b7&nbsp; day " + doy + " of " + r.getFullYear());
  dt2Ins(r);
}
function dtWeekNum() {
  var d = _v("wn-date");
  if (!d) { out("wn-out", "Pick a date first.", "err"); return; }
  var r = pISO(d);
  var iso = dt2IsoWeek(r);
  var mon = new Date(r); mon.setDate(mon.getDate() - ((mon.getDay() + 6) % 7));
  var sun = new Date(mon); sun.setDate(sun.getDate() + 6);
  var pct = Math.round(iso.week / 52.14 * 100);
  out("wn-out", "<b>Week " + iso.week + "</b> of " + iso.year + "<br><span class=\"dim\">ISO-8601 (weeks start Monday; week 1 holds the first Thursday) \u00b7 begins " + dISO(mon) + ", ends " + dISO(sun) + " \u00b7 " + pct + "% through the year</span>");
  dt2Ins(r);
}
function dtLeap() {
  var y = _n("lp-y");
  if (y === null || Math.floor(y) !== y) { out("lp-out", "Enter a whole year.", "err"); if (document.getElementById("dt2-ins")) document.getElementById("dt2-ins").innerHTML = ""; return; }
  var isL = (y % 4 === 0 && y % 100 !== 0) || (y % 400 === 0);
  var why = isL ? ((y % 400 === 0 && y % 100 === 0) ? "divisible by 400, so the century exception does not apply" : "divisible by 4 and not by 100") : ((y % 100 === 0) ? "a century year not divisible by 400" : "not divisible by 4");
  var next = [];
  var yy = y;
  while (next.length < 5) { yy++; if ((yy % 4 === 0 && yy % 100 !== 0) || yy % 400 === 0) next.push(yy); }
  out("lp-out", y + " is <b>" + (isL ? "a leap year" : "not a leap year") + "</b> \u2014 " + why + ".<br>February " + y + ": " + (isL ? 29 : 28) + " days<br>Next leap years: " + next.join(", "));
  var wrap = document.getElementById("dt2-ins");
  if (wrap) {
    var chips = dt2Chip(isL ? 366 : 365, "days in " + y);
    if (isL) chips += dt2Chip("Feb 29, " + y, "extra day");
    else chips += dt2Chip(next[0], "next leap year");
    wrap.innerHTML = chips;
  }
}
function dtS2Hms() {
  var s = _n("s2-sec");
  if (s === null || s < 0) { out("s2-out", "Enter a number of seconds (0 or more).", "err"); if (document.getElementById("dt2-ins")) document.getElementById("dt2-ins").innerHTML = ""; return; }
  s = Math.round(s);
  var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = s % 60;
  out("s2-out", "<b>" + h + ":" + String(m).padStart(2, "0") + ":" + String(sec).padStart(2, "0") + "</b><br>" + nfmt(h, 0) + " hours &nbsp;\u00b7&nbsp; " + m + " minutes &nbsp;\u00b7&nbsp; " + sec + " seconds");
  dt2InsDur(s);
}
function dtHms2S() {
  var h = _n("h2-h"), m = _n("h2-m"), s = _n("h2-s");
  if (h === null || m === null || s === null) { out("h2-out", "Enter all three fields (0 is fine).", "err"); if (document.getElementById("dt2-ins")) document.getElementById("dt2-ins").innerHTML = ""; return; }
  var tot = h * 3600 + m * 60 + s;
  out("h2-out", "<b>" + nfmt(tot, 0) + "</b> seconds");
  dt2InsDur(tot);
}
function dtMilitary() {
  var t = _v("mt-tv");
  if (!t) { out("mt-out", "Pick a time first.", "err"); return; }
  var p = t.split(":"), h = +p[0], m = +p[1];
  var ap = h >= 12 ? "PM" : "AM";
  var h12 = h % 12; if (h12 === 0) h12 = 12;
  out("mt-out", "<b>" + t + "</b> in 24-hour time = <b>" + h12 + ":" + String(m).padStart(2, "0") + " " + ap + "</b> in 12-hour time");
  dt2MilChips(t);
}
function dtMilRev() {
  var t = _v("mt24");
  var o = $("mt-out2"); if (!o) return;
  var m = t.match(/^\s*(\d{1,2}):(\d{2})\s*$/);
  if (!m) { o.innerHTML = '<span class="dim">Enter 24-hour time as HH:MM, e.g. 21:15.</span>'; return; }
  var h = +m[1], mi = +m[2];
  if (h > 23 || mi > 59) { o.innerHTML = '<span class="dim">Hours 0\u201323, minutes 0\u201359.</span>'; return; }
  var ap = h >= 12 ? "PM" : "AM";
  var h12 = h % 12; if (h12 === 0) h12 = 12;
  o.innerHTML = "<b>" + t + "</b> = <b>" + h12 + ":" + String(mi).padStart(2, "0") + " " + ap + "</b>";
}
function dtBizDays() {
  var a = _v("bd-a"), b = _v("bd-b");
  if (!a || !b) { out("bd-out", "Pick both dates.", "err"); if (document.getElementById("dt2-ins")) document.getElementById("dt2-ins").innerHTML = ""; return; }
  var d1 = pISO(a), d2 = pISO(b);
  if (d2 < d1) { var tmp = d1; d1 = d2; d2 = tmp; }
  var biz = 0, cal = Math.round((d2 - d1) / 86400000);
  var cur = new Date(d1);
  for (var i = 0; i < cal; i++) { var dow = cur.getDay(); if (dow !== 0 && dow !== 6) biz++; cur.setDate(cur.getDate() + 1); }
  out("bd-out", "<b>" + biz + " business days</b> (Mon\u2013Fri) between " + a + " and " + b + "<br>Calendar span: " + cal + " days &nbsp;\u00b7&nbsp; Weekend days: " + (cal - biz));
  var wrap = document.getElementById("dt2-ins");
  if (wrap) {
    var weeks = cal / 7;
    wrap.innerHTML =
      dt2Chip(weeks.toFixed(1), "weeks in span") +
      dt2Chip(cal > 0 ? (biz / weeks).toFixed(1) : "\u2014", "business days / week") +
      dt2Chip(biz > 0 ? Math.ceil(biz / 5) : 0, "working weeks (5-day)");
  }
}


/* ---------- TX2: shared upgrades for the text engine tools ---------- */
var TX2_SAMPLE = "Meeting notes 2026-11-21:\nBudget  review  postponed  to  January (that is  42  days away).\nContact:  ana.torres@example.com  or  +44 20 7946 0958.\nDocs live at https://example.com/roadmap and http://github.com/example/repo.\nCosts:  1,250.50 +  340  +  12.5  GBP \u2014 still  under the 2,000 cap.\nAttendees: Ana, Bruno, Chen, Dalia.\nNote the  trailing double space  above and this  line with  lots of  extra  spaces.";
function tx2Count(t) {
  var words = (t.match(/\S+/g) || []).length;
  var lines = t === "" ? 0 : t.split("\n").length;
  return { w: words, c: t.length, l: lines };
}
function tx2Chip(b, label, ok) { return '<span class="jf-chip' + (ok ? " ok" : "") + '"><b>' + b + "</b>" + label + "</span>"; }
function tx2Stats() {
  var st = document.getElementById("tx2-stats");
  if (!st || !$("tx-in")) return;
  var i = $("tx-in").value, o = $("tx-out") ? $("tx-out").value : "";
  if (!i.trim()) { st.innerHTML = ""; return; }
  var ci = tx2Count(i), co = tx2Count(o);
  var diff = i.length - o.length;
  var diffTxt = diff > 0 ? diff.toLocaleString() + " chars removed" : diff < 0 ? "+" + Math.abs(diff).toLocaleString() + " chars added" : "same length";
  st.innerHTML =
    tx2Chip(ci.w.toLocaleString(), "words in") +
    tx2Chip(ci.c.toLocaleString(), "chars in") +
    tx2Chip(ci.l.toLocaleString(), "lines in") +
    tx2Chip(co.w.toLocaleString(), "words out") +
    tx2Chip(co.l.toLocaleString(), "lines out") +
    tx2Chip(diffTxt, diff > 0 ? "shorter" : "longer", diff > 0);
}
function tx2Run2() { if (window.TX_CONF) { txRun(); tx2Stats(); } }
function tx2Sample() {
  if (!$("tx-in")) return;
  $("tx-in").value = TX2_SAMPLE;
  tx2Run2();
}
function tx2Swap() {
  if (!$("tx-in")) return;
  var o = $("tx-out") ? $("tx-out").value : "";
  if (!o) return;
  $("tx-in").value = o;
  if ($("tx-out")) $("tx-out").value = "";
  tx2Run2();
}
function tx2Download() {
  var o = $("tx-out");
  if (!o || !o.value) return;
  dlBytes(o.value, "result.txt", "text/plain");
}
(function () {
  var LIVE = ["tx-in", "tx-pre", "tx-suf", "tx-find", "tx-delim", "tx-sep", "tx-len"];
  document.addEventListener("input", function (e) {
    var id = e && e.target && e.target.id;
    if (!id || LIVE.indexOf(id) === -1) return;
    if (id !== "tx-in" && !window.TX_CONF) return;
    clearTimeout(window.__tx2t);
    window.__tx2t = setTimeout(tx2Run2, 220);
  });
})();


/* ---------- CX2: shared upgrades for the color engine tools ---------- */
function cx2Current() {
  var c = cxParseHex(_v("cx-in") || _v("ch-in") || _v("sh-in") || _v("cp-in") || _v("iv-in") || _v("gs-in") || _v("ct-fg") || "");
  if (c) return [c.r, c.g, c.b];
  var r = _n("cr-r"), g = _n("cr-g"), b = _n("cr-b");
  if (r === null && _n("rh-r") !== null) { r = _n("rh-r"); g = _n("rh-g"); b = _n("rh-b"); }
  if (typeof r !== "number" || typeof g !== "number" || typeof b !== "number") return null;
  var cl = function (x) { return Math.max(0, Math.min(255, Math.round(x))); };
  return [cl(r), cl(g), cl(b)];
}
function cx2ToHsl(rgb) {
  var r = rgb[0] / 255, g = rgb[1] / 255, b = rgb[2] / 255;
  var mx = Math.max(r, g, b), mn = Math.min(r, g, b), h = 0, s = 0, l = (mx + mn) / 2, d = mx - mn;
  if (d) {
    s = l > 0.5 ? d / (2 - mx - mn) : d / (mx + mn);
    if (mx === r) h = ((g - b) / d + (g < b ? 6 : 0));
    else if (mx === g) h = (b - r) / d + 2;
    else h = (r - g) / d + 4;
    h = Math.round(h * 60);
  }
  return [h, Math.round(s * 100), Math.round(l * 100)];
}
function cx2Ins() {
  var wrap = document.getElementById("cx2-ins");
  if (!wrap) return;
  var rgb = cx2Current();
  if (!rgb) { wrap.innerHTML = ""; return; }
  var lum = Math.round(cc2Lum(rgb) * 255);
  var rw = cc2Ratio(rgb, [255, 255, 255]), rb = cc2Ratio(rgb, [0, 0, 0]);
  var hsl = cx2ToHsl(rgb);
  var best = rw >= rb ? "white" : "black";
  var bestR = Math.max(rw, rb);
  var verdict = bestR >= 7 ? "AAA" : bestR >= 4.5 ? "AA" : bestR >= 3 ? "large text only" : "avoid text";
  wrap.innerHTML =
    dt2Chip(hsl.join(", "), "hsl") +
    dt2Chip(lum + "/255", "luminance") +
    cc2CcChip(rw, "white") +
    cc2CcChip(rb, "black") +
    dt2Chip(best + " \u00b7 " + verdict, "best text");
}
function cx2Copy(fmt, btn) {
  var rgb = cx2Current();
  if (!rgb) return;
  var txt;
  if (fmt === "rgb") txt = "rgb(" + rgb.join(", ") + ")";
  else if (fmt === "hsl") txt = "hsl(" + cx2ToHsl(rgb).join(", ") + ")";
  else txt = "--brand-color: " + cxToHex(rgb[0], rgb[1], rgb[2]) + ";";
  copyText(txt, btn);
}
function cx2Random(hid, fn) {
  var hexarr = crypto.getRandomValues(new Uint8Array(3));
  var hex = "#";
  for (var i = 0; i < 3; i++) hex += hexarr[i].toString(16).padStart(2, "0");
  var el = $(hid);
  if (el) el.value = hex;
  try { if (typeof window[fn] === "function") window[fn](); else eval(fn + "()"); } catch (e) {}
  cx2Ins();
}
(function () {
  var IDS = ["cx-in", "cr-r", "cr-g", "cr-b", "ch-in", "rh-r", "rh-g", "rh-b", "sh-in", "cp-in", "ct-fg", "ct-bg", "iv-in", "gs-in"];
  document.addEventListener("input", function (e) {
    var id = e && e.target && e.target.id;
    if (!id || IDS.indexOf(id) === -1) return;
    clearTimeout(window.__cx2t);
    window.__cx2t = setTimeout(cx2Ins, 180);
  });
})();

/* ---------- RN2: shared upgrades for the random engine tools ---------- */
var RN2_N = 0;
var RN2_YN = [0, 0];
function rn2Chip(b, label) { return '<span class="jf-chip"><b>' + b + "</b>" + label + "</span>"; }
function rn2CopyRes(id, btn) {
  var el = $(id);
  if (!el) return;
  var t = el.tagName === "TEXTAREA" ? el.value : el.textContent;
  t = String(t || "").replace(/\s+/g, " ").trim();
  if (t) copyText(t, btn);
}
function rn2Redraw() {
  var st = document.getElementById("rn2-stats");
  if (!st) return;
  var d = new Date();
  var h = String(d.getHours()).padStart(2, "0") + ":" + String(d.getMinutes()).padStart(2, "0") +
    ":" + String(d.getSeconds()).padStart(2, "0");
  var items = [[String(RN2_N), "draws this visit"], [h, "last draw"]];
  if (document.getElementById("yn-out")) {
    items.push([String(RN2_YN[0]), "yes answers"], [String(RN2_YN[1]), "no answers"]);
  }
  st.innerHTML = items.map(function (it) { return rn2Chip(it[0], it[1]); }).join("");
}
function rn2After() {
  RN2_N++;
  var el = document.getElementById("yn-out");
  if (el) {
    var t = (el.textContent || "").toLowerCase();
    if (/\byes\b/.test(t)) RN2_YN[0]++;
    else if (/\bno\b/.test(t)) RN2_YN[1]++;
  }
  rn2Redraw();
}
[["rnLetter", "rl-out"], ["rnWord", "rw-out"], ["rnDate", "rd-out"], ["rnShuffle", "ls-out"],
 ["rnPick", "np-out"], ["rnYesNo", "yn-out"], ["rnTeams", "ts-out"], ["rnLottery", "lt-out"],
 ["rnCountry", "co-out"], ["rnQuote", "qt-out"]].forEach(function (pair) {
  var orig = window[pair[0]] || eval(pair[0]);
  if (typeof orig !== "function") return;
  window[pair[0]] = function () { orig(); rn2After(); };
});
document.addEventListener("keydown", function (e) {
  if (!e || e.code !== "Space") return;
  var tn = e.target && e.target.tagName;
  if (["INPUT", "TEXTAREA", "SELECT", "BUTTON"].indexOf(tn) !== -1) return;
  if (!document.getElementById("yn-out")) return;
  e.preventDefault();
  rnYesNo();
});


/* ---------- CB2: shared upgrades for the calculator engine (22 tools) ---------- */
var CB2_N = 0;
var CB2_FNS = ["si", "avg", "sqrt", "pow", "cirA", "cirC", "triA", "rectA", "facCalc", "gcdCalc",
  "primeCalc", "n2wCalc", "quadCalc", "arCalc", "pmCalc", "logCalc", "hrsCalc", "fuelCalc",
  "cbrtCalc", "pctChCalc", "hypCalc", "ratioCalc"];
function cb2Stamp() {
  var d = new Date();
  return String(d.getHours()).padStart(2, "0") + ":" + String(d.getMinutes()).padStart(2, "0") +
    ":" + String(d.getSeconds()).padStart(2, "0");
}
function cb2After() {
  CB2_N++;
  var st = document.getElementById("cb2-meta");
  if (st) st.innerHTML = rn2Chip(String(CB2_N), "calculations this visit") + rn2Chip(cb2Stamp(), "last update");
}
CB2_FNS.forEach(function (fn) {
  var orig = window[fn] || eval(fn);
  if (typeof orig !== "function") return;
  window[fn] = function () { orig(); cb2After(); };
});
function cb2Copy(fn, btn) {
  var el = document.getElementById(fn + "-out");
  if (!el) return;
  var t = String(el.textContent || "").replace(/\s+/g, " ").trim();
  if (t && t !== "Fill in the fields to see the result.") copyText(t, btn);
}
function cb2Reset() {
  document.querySelectorAll(".panel input, .panel select").forEach(function (el) {
    if (el.type === "checkbox" || el.type === "radio") { el.checked = false; return; }
    el.value = "";
  });
  if (typeof window.CB2_FN === "string" && typeof window[window.CB2_FN] === "function") window[window.CB2_FN]();
}
(function () {
  document.addEventListener("input", function (e) {
    var tn = e && e.target && e.target.tagName;
    if (tn !== "INPUT" && tn !== "SELECT") return;
    if (typeof window.CB2_FN !== "string") return;
    clearTimeout(window.__cb2t);
    window.__cb2t = setTimeout(function () { window[window.CB2_FN](); }, 250);
  });
  document.addEventListener("keydown", function (e) {
    if (!e || e.key !== "Enter") return;
    if (!e.target || e.target.tagName !== "INPUT") return;
    if (typeof window.CB2_FN !== "string") return;
    e.preventDefault();
    window[window.CB2_FN]();
  });
})();

/* ---------- UC2: preset values for the unit-converter engine (36 tools) ---------- */
function ucPreset(v) {
  var a = $("uc-in");
  if (!a) return;
  a.value = String(v);
  ucRun();
}


/* ---------- F15: copy/export finishers on standalone pro tools ---------- */
var BM2_LAST = "", CI2_ROWS = null, CI2_SUM = "", UC2_TXT = "", DR2_LAST = "", CF2_LAST = "";
/* BMI */
(function () {
  var o = bmiCalc;
  bmiCalc = function () {
    o();
    var el = $("bmi-big");
    if (!el) return;
    var m = (el.textContent || "").match(/-?\d+(\.\d+)?/);
    if (!m) { BM2_LAST = ""; return; }
    var parts = ["BMI " + m[0]];
    var st = $("bmi-out"), hy = $("bm2-healthy");
    if (st && st.textContent) parts.push(st.textContent.replace(/\s+/g, " ").trim());
    if (hy && hy.textContent) parts.push(hy.textContent.replace(/\s+/g, " ").trim());
    BM2_LAST = parts.join(" \u00b7 ");
  };
})();
function bm2Copy(btn) { if (BM2_LAST) copyText(BM2_LAST, btn); }
/* Compound interest */
(function () {
  var o = ci2Live;
  ci2Live = function () {
    o();
    var el = $("ci2-big");
    if (!el) return;
    var txt = (el.textContent || "").trim();
    if (!txt || txt === "\u2014") { CI2_ROWS = null; CI2_SUM = ""; return; }
    var P = parseFloat($("ci-p").value), r = parseFloat($("ci-r").value), t = parseFloat($("ci-t").value);
    var n = parseInt($("ci-n").value), monthly = parseFloat($("ci-monthly").value) || 0;
    if (isNaN(P) || isNaN(r) || isNaN(t) || !n || t <= 0) { CI2_ROWS = null; CI2_SUM = ""; return; }
    var s = ci2Series(P, r, t, n, monthly);
    CI2_ROWS = s.yearly.map(function (row) {
      return [row.year, +row.bal.toFixed(2), +row.contributed.toFixed(2), +(row.bal - row.contributed).toFixed(2)];
    });
    CI2_SUM = "Future value " + ci2F(s.bal) + " after " + t + " years \u00b7 contributed " + ci2F(s.contributed) +
      " \u00b7 interest " + ci2F(s.interest) + " \u00b7 " + P.toLocaleString() + " at " + r + "%" +
      (monthly ? ", +" + monthly + "/month" : "");
  };
})();
function ci2Copy(btn) { if (CI2_SUM) copyText(CI2_SUM, btn); }
function ci2Csv() {
  if (!CI2_ROWS || !CI2_ROWS.length) return;
  var csv = "Year,Balance,Contributed,Interest\n" + CI2_ROWS.map(function (r) { return r.join(","); }).join("\n");
  dlBytes(csv, "compound-interest-growth.csv", "text/csv");
}
/* Universal unit converter */
(function () {
  var o = uc2Run;
  uc2Run = function () {
    o();
    var el = $("uc2-big");
    if (!el) return;
    var t = (el.textContent || "").trim();
    UC2_TXT = (t && t !== "\u2014") ? t : "";
  };
})();
function uc2Copy(btn) { if (UC2_TXT) copyText(UC2_TXT, btn); }
/* Dice roller */
(function () {
  var o = rollDice;
  rollDice = function () {
    o();
    var h = (typeof DR2_HIST !== "undefined" && DR2_HIST && DR2_HIST[0]) ? DR2_HIST[0] : null;
    if (!h) return;
    DR2_LAST = h.rolls.length + "d" + h.sides + (h.mod ? (h.mod > 0 ? "+" + h.mod : String(h.mod)) : "") +
      " \u2192 " + h.rolls.join(", ") + " \u00b7 total " + h.total;
  };
})();
function dr2Copy(btn) { if (DR2_LAST) copyText(DR2_LAST, btn); }
/* Coin flipper */
(function () {
  var o = flipCoin;
  flipCoin = function () {
    o();
    var el = $("cf2-big");
    if (!el) return;
    var t = (el.textContent || "").trim();
    CF2_LAST = (t && t !== "\u2014") ? t.replace(/^[^A-Za-z0-9]+/, "") : "";
  };
})();
function cf2Copy(btn) { if (CF2_LAST) copyText(CF2_LAST, btn); }
/* Invoice */
function invCopy(btn) {
  var el = document.getElementById("inv-print");
  if (!el) return;
  var t = (el.textContent || "").replace(/[ \t]+/g, " ").trim();
  if (t) copyText(t, btn);
}


/* ---------- M3: shared finisher for the 12 mega3 advanced calculators ---------- */
var M3_N = 0;
var M3_FNS = ["ci", "am", "cal", "bf", "orm", "pace", "be", "roi", "up", "gr", "ec", "sleep"];
function m3After() {
  M3_N++;
  var st = document.getElementById("m3-stats");
  if (!st) return;
  var d = new Date();
  var h = String(d.getHours()).padStart(2, "0") + ":" + String(d.getMinutes()).padStart(2, "0") +
    ":" + String(d.getSeconds()).padStart(2, "0");
  st.innerHTML = '<span class="jf-chip"><b>' + M3_N + "</b>calculations this visit</span>" +
    '<span class="jf-chip"><b>' + h + "</b>last update</span>";
}
M3_FNS.forEach(function (fn) {
  var orig = window[fn] || eval(fn);
  if (typeof orig !== "function") return;
  window[fn] = function () { orig(); m3After(); };
});
function m3Copy(btn) {
  var fn = window.M3_FN;
  if (typeof fn !== "string") return;
  var el = document.getElementById(fn + "-out");
  if (!el) return;
  var t = String(el.textContent || "").replace(/\s+/g, " ").trim();
  if (t) copyText(t, btn);
}
(function () {
  document.addEventListener("input", function (e) {
    var tn = e && e.target && e.target.tagName;
    if (tn !== "INPUT" && tn !== "SELECT") return;
    if (typeof window.M3_FN !== "string") return;
    clearTimeout(window.__m3t);
    window.__m3t = setTimeout(function () { if (typeof window[window.M3_FN] === "function") window[window.M3_FN](); }, 250);
  });
  document.addEventListener("keydown", function (e) {
    if (!e || e.key !== "Enter") return;
    if (!e.target || e.target.tagName !== "INPUT") return;
    if (typeof window.M3_FN !== "string") return;
    e.preventDefault();
    if (typeof window[window.M3_FN] === "function") window[window.M3_FN]();
  });
})();


/* ---------- F17: copy finishers on still-thin finance + diff tools ---------- */
var DC2_SUM = "", PC2_SUM = "";
function f17Ent(s) {
  return String(s).replace(/&middot;/g, "\u00b7").replace(/&nbsp;/g, " ").replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">").replace(/&quot;/g, "\\x22").replace(/&amp;/g, "&");
}
function f17Sub(el) {
  if (!el) return "";
  return f17Ent((el.innerHTML || "")
    .replace(/\s*<span[^>]*class="pct2-big-sub"[^>]*>/g, " \u2014 ")
    .replace(/<[^>]*>/g, "").replace(/\s+/g, " ").trim());
}
function f17Clean(el) {
  if (!el) return "";
  var t = (el.textContent || "").trim();
  return (t && t !== "\u2014") ? t : "";
}
/* Discount */
(function () {
  var o = discountCalc;
  discountCalc = function () {
    o();
    DC2_SUM = f17Clean($("dc2-big")) ? f17Sub($("dc2-big")) : "";
  };
})();
function dc2Copy(btn) { if (DC2_SUM) copyText(DC2_SUM, btn); }
/* Tip */
function tp2Copy(btn) {
  var t = f17Clean($("tp2-tip")), tot = f17Clean($("tp2-total"));
  if (!t) return;
  copyText("Tip " + t + " \u00b7 Total " + tot + " \u00b7 Per person: tip " + f17Clean($("tp2-per-tip")) +
    ", total " + f17Clean($("tp2-per-total")), btn);
}
/* GST / VAT */
function gst2Copy(btn) {
  var net = f17Clean($("tx2-net"));
  if (!net) return;
  var dir = $("tx2-add") && $("tx2-add").classList && $("tx2-add").classList.contains("active") ? "added to" : "removed from";
  copyText("Tax " + f17Clean($("tx2-tax")) + " (18% style rate " + ($("tax-rate") ? $("tax-rate").value : "?") + "% " + dir + "): net " +
    net + ", gross " + f17Clean($("tx2-gross")), btn);
}
/* Percentage calculator */
(function () {
  var o = pct2Run;
  pct2Run = function () {
    o();
    var big = $("pct2-big");
    PC2_SUM = (big && f17Clean(big)) ? f17Sub(big) : "";
  };
})();
function pc2Copy(btn) { if (PC2_SUM) copyText(PC2_SUM, btn); }
/* Text diff */
function df2Copy(btn) {
  var t = f17Clean($("df2-stats"));
  if (t) copyText(t, btn);
}
/* ---------- M4: batch 18 new tools (tz3 timezone, mo3 morse, st3 statistics,
   sd3 speed/distance/time, fc3 fractions, gp3 GPA, dp3 depreciation, wq3 water) ---------- */
function m4Num(id) {
  var v = String($(id).value || "").trim();
  return (v === "" || !isFinite(+v)) ? null : +v;
}
function m4Pad(n) { return String(n).padStart(2, "0"); }
function m4Hms(ms) {
  var d = new Date(ms);
  return m4Pad(d.getUTCHours()) + ":" + m4Pad(d.getUTCMinutes());
}

/* --- tz3: IANA-accurate time zone converter --- */
function tz3Off(tz, ms) {
  try {
    var p = new Intl.DateTimeFormat("en-US", { timeZone: tz, hour12: false, year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit" }).formatToParts(new Date(ms));
    var g = {};
    p.forEach(function (x) { g[x.type] = x.value; });
    if (!g.year) return null;
    var asUTC = Date.UTC(+g.year, +g.month - 1, +g.day, (+g.hour) % 24, +g.minute, +g.second);
    return (asUTC - Math.floor(ms / 1000) * 1000) / 60000;
  } catch (e) { return null; }
}
function tz3() {
  var o = $("tz3-out");
  var f = String($("tz3-f").value || ""), t = String($("tz3-t").value || "");
  if (!f || !t) { o.innerHTML = "Pick two cities to convert between."; return; }
  var fT = f.split("/").pop().replace(/_/g, " "), tT = t.split("/").pop().replace(/_/g, " ");
  var v = String($("tz3-dt").value || "").replace("T", " ").trim();
  var utc;
  if (!v) {
    utc = Date.now();
  } else {
    var m = v.split(/[- :]/).map(Number);
    if (m.length < 5 || m.some(function (x) { return isNaN(x); })) {
      o.innerHTML = "Enter a valid date and time, or leave the field blank to convert the current moment.";
      return;
    }
    var base = Date.UTC(m[0], m[1] - 1, m[2], m[3], m[4], m[5] || 0);
    utc = base;
    for (var i = 0; i < 3; i++) {
      var off0 = tz3Off(f, utc);
      if (off0 === null) { o.innerHTML = "Unknown city selected."; return; }
      utc = base - off0 * 60000;
    }
  }
  var foff = tz3Off(f, utc), toff = tz3Off(t, utc);
  if (foff === null || toff === null) { o.innerHTML = "Unknown city selected."; return; }
  var dS = new Date(utc + foff * 60000), dT = new Date(utc + toff * 60000);
  var diff = toff - foff;
  var diffTxt = diff === 0 ? "same clock time" : Math.abs(diff / 60) + " h " + (diff > 0 ? "ahead" : "behind");
  var dsKey = Date.UTC(dS.getUTCFullYear(), dS.getUTCMonth(), dS.getUTCDate());
  var dtKey = Date.UTC(dT.getUTCFullYear(), dT.getUTCMonth(), dT.getUTCDate());
  var shift = Math.round((dtKey - dsKey) / 86400000);
  var dayTxt = shift === 0 ? "same day" : (shift > 0 ? "+" + shift + " day" : shift + " day");
  var timeStr = m4Hms(utc + toff * 60000);
  var dateStr = m4Pad(dT.getUTCDate()) + "/" + m4Pad(dT.getUTCMonth() + 1) + "/" + dT.getUTCFullYear();
  o.innerHTML = "<b>" + timeStr + "</b> in " + tT + " when it is <b>" + m4Hms(utc + foff * 60000) + "</b> in " + fT +
    "<span class='jf-chip'><b>" + dateStr + "</b>target date</span>" +
    "<span class='jf-chip'><b>" + diffTxt + "</b>difference</span>" +
    "<span class='jf-chip'><b>" + tz3Fmt(foff) + "</b>" + fT + " offset</span>" +
    "<span class='jf-chip'><b>" + tz3Fmt(toff) + "</b>" + tT + " offset</span>" +
    (shift === 0 ? "" : "<span class='jf-chip'><b>" + dayTxt + "</b>" + dateStr + "</span>");
}
function tz3Fmt(z) {
  var s = z < 0 ? "\u2212" : "+", a = Math.abs(z), h = Math.floor(a / 60), m = Math.round(a % 60);
  return "UTC" + s + h + (m ? ":" + m4Pad(m) : "");
}

/* --- mo3: morse code translator --- */
var MO3_E = { "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
  "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",
  "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
  "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
  "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--", "'": ".----.",
  "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
  "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.", "@": ".--.-." };
var MO3_D = {};
Object.keys(MO3_E).forEach(function (k) { MO3_D[MO3_E[k]] = k; });
var MO3_MORSE = "", MO3_PLAIN = "", MO3_KIND = "e";
function mo3() {
  var o = $("mo3-out");
  var s = String($("mo3-in").value || "");
  if (!s.trim()) { o.innerHTML = "Type text above, or paste Morse code (dots, dashes, spaces \u2014 use / or | between words)."; return; }
  var isMorse = /[\.\-]/.test(s) && !/[A-Za-z0-9]/.test(s.replace(/[/.|]/g, ""));
  var i, outArr;
  if (isMorse) {
    var words = s.replace(/\|/g, "/").trim().split(/\s*\/\s*/);
    var plain = [];
    for (i = 0; i < words.length; i++) {
      var ls = words[i].split(/\s+/).filter(Boolean).map(function (tok) { return MO3_D[tok] || "?"; }).join("");
      plain.push(ls);
    }
    MO3_PLAIN = plain.join(" ");
    MO3_MORSE = s.replace(/\|/g, "/").trim().split(/\s*\/\s*/).map(function (w) { return w.split(/\s+/).filter(Boolean).join(" "); }).join(" / ");
    MO3_KIND = "d";
    o.innerHTML = "<b>" + escHtml(MO3_PLAIN) + "</b><span class='jf-chip'><b>" + MO3_MORSE.split(" ").length + "</b>signals</span><span class='jf-chip'><b>" + MO3_PLAIN.split(/\s+/).length + "</b>words decoded</span>";
  } else {
    var mwords = s.toUpperCase().split(/\s+/);
    var marr = [];
    for (i = 0; i < mwords.length; i++) {
      if (!mwords[i]) continue;
      var enc = mwords[i].split("").map(function (ch) { return MO3_E[ch] !== undefined ? MO3_E[ch] : "?"; }).join(" ");
      marr.push(enc);
    }
    MO3_MORSE = marr.join(" / ");
    MO3_PLAIN = s.toUpperCase().trim().split(/\s+/).join(" ");
    MO3_KIND = "e";
    var units = MO3_MORSE.replace(/[^.\- ]/g, "").length * 1 + (MO3_MORSE.match(/\-/g) || []).length * 2;
    o.innerHTML = "<b>" + escHtml(MO3_MORSE) + "</b><span class='jf-chip'><b>" + (MO3_MORSE.match(/[.\-]/g) || []).length + "</b>signals</span><span class='jf-chip'><b>~" + Math.ceil(units * 0.06) + " s</b>to key at 20 wpm</span>";
  }
}
function mo3Swap() {
  if (MO3_MORSE && MO3_KIND === "e") $("mo3-in").value = MO3_MORSE;
  else if (MO3_PLAIN) $("mo3-in").value = MO3_PLAIN;
  mo3();
}
function mo3Play(btn) {
  var m = MO3_KIND === "e" ? MO3_MORSE : MO3_MORSE;
  if (!m) return;
  var AC = window.AudioContext || window.webkitAudioContext;
  if (!AC) { btn.textContent = "Audio unsupported"; return; }
  try {
    var ctx = new AC(), u = 0.09, t = ctx.currentTime + 0.08;
    var osc = ctx.createOscillator(), gain = ctx.createGain(), total = 0;
    osc.frequency.value = 600; gain.gain.value = 0.0001;
    osc.connect(gain); gain.connect(ctx.destination);
    m.split("").forEach(function (ch) {
      if (ch === ".") { gain.gain.setTargetAtTime(0.25, t, 0.005); t += u; gain.gain.setTargetAtTime(0.0001, t, 0.005); t += u; }
      else if (ch === "-") { gain.gain.setTargetAtTime(0.25, t, 0.005); t += u * 3; gain.gain.setTargetAtTime(0.0001, t, 0.005); t += u; }
      else if (ch === " ") { t += u * 2; }
      else if (ch === "/") { t += u * 5; }
    });
    total = t - ctx.currentTime;
    osc.start(); osc.stop(ctx.currentTime + total + 0.1);
    if (btn) { btn.textContent = "Playing\u2026"; setTimeout(function () { btn.textContent = "Play audio"; }, total * 1000); }
  } catch (e) { if (btn) btn.textContent = "Audio unsupported"; }
}

/* --- st3: descriptive statistics --- */
function st3Q(a, p) {
  var i = (a.length - 1) * p, lo = Math.floor(i), hi = Math.ceil(i);
  return a[lo] + (a[hi] - a[lo]) * (i - lo);
}
function st3() {
  var o = $("st3-out");
  var tok = String($("st3-in").value || "").match(/-?(?:\d+\.?\d*|\.\d+)(?:e[+-]?\d+)?/gi) || [];
  var a = tok.map(Number).filter(function (x) { return isFinite(x); });
  if (!a.length) { o.innerHTML = "Enter at least one number \u2014 separate with spaces, commas or new lines."; return; }
  var s = a.slice().sort(function (x, y) { return x - y; });
  var n = a.length, sum = a.reduce(function (p, c) { return p + c; }, 0), mean = sum / n;
  var med = n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2;
  var varP = a.reduce(function (p, c) { return p + (c - mean) * (c - mean); }, 0) / n;
  var varS = n > 1 ? a.reduce(function (p, c) { return p + (c - mean) * (c - mean); }, 0) / (n - 1) : 0;
  var q1 = st3Q(s, 0.25), q3 = st3Q(s, 0.75);
  var f6 = function (x) { return (Math.round(x * 1e6) / 1e6).toString(); };
  var counts = {}, best = [], bestC = 1;
  a.forEach(function (x) {
    var k = f6(x);
    counts[k] = (counts[k] || 0) + 1;
    if (counts[k] > bestC) bestC = counts[k];
  });
  if (bestC > 1) best = Object.keys(counts).filter(function (k) { return counts[k] === bestC; });
  o.innerHTML = "<b>Mean " + f6(mean) + "</b> \u00b7 median <b>" + f6(med) + "</b> \u00b7 sample sd <b>" + f6(Math.sqrt(varS)) + "</b>" +
    "<span class='jf-chip'><b>" + n + "</b>values</span><span class='jf-chip'><b>" + f6(sum) + "</b>sum</span>" +
    "<span class='jf-chip'><b>" + f6(s[0]) + "</b>minimum</span><span class='jf-chip'><b>" + f6(s[n - 1]) + "</b>maximum</span>" +
    "<span class='jf-chip'><b>" + f6(s[n - 1] - s[0]) + "</b>range</span>" +
    "<span class='jf-chip'><b>" + (best.length ? best.join(", ") : "none") + "</b>mode</span>" +
    "<span class='jf-chip'><b>" + f6(q1) + "</b>Q1 (25%)</span><span class='jf-chip'><b>" + f6(q3) + "</b>Q3 (75%)</span>" +
    "<span class='jf-chip'><b>" + f6(q3 - q1) + "</b>interquartile range</span>" +
    "<span class='jf-chip'><b>" + f6(varP) + "</b>variance (population)</span>" +
    "<span class='jf-chip'><b>" + f6(varS) + "</b>variance (sample)</span>";
}

/* --- sd3: speed / distance / time --- */
function sd3() {
  var o = $("sd3-out"), mode = String($("sd3-m").value || "speed");
  var d = m4Num("sd3-d"), s = m4Num("sd3-s"), t = m4Num("sd3-t");
  var f6 = function (x) { return (Math.round(x * 1e4) / 1e4).toString(); };
  var r, label;
  if (mode === "speed") {
    if (d === null || d <= 0 || t === null || t <= 0) { o.innerHTML = "Enter a positive distance and a positive time to solve for speed."; return; }
    r = d / t; label = "Speed " + f6(r) + " km/h";
  } else if (mode === "distance") {
    if (s === null || s <= 0 || t === null || t < 0) { o.innerHTML = "Enter a positive speed and a time (hours) to solve for distance."; return; }
    r = s * t; label = "Distance " + f6(r) + " km";
  } else {
    if (d === null || d <= 0 || s === null || s <= 0) { o.innerHTML = "Enter a positive distance and a positive speed to solve for time."; return; }
    r = d / s; label = "Time " + Math.floor(r) + " h " + m4Pad(Math.round((r - Math.floor(r)) * 60)) + " min";
  }
  var chips = "";
  if (mode === "speed") {
    chips = "<span class='jf-chip'><b>" + f6(r / 1.609344) + "</b>mph</span><span class='jf-chip'><b>" + f6(r / 3.6) + "</b>m/s</span><span class='jf-chip'><b>" + f6(60 / r) + "</b>min per km</span>";
  } else if (mode === "distance") {
    chips = "<span class='jf-chip'><b>" + f6(r * 1000) + "</b>metres</span><span class='jf-chip'><b>" + f6(r / 1.609344) + "</b>miles</span>";
  } else {
    chips = "<span class='jf-chip'><b>" + f6(r) + "</b>hours (decimal)</span><span class='jf-chip'><b>" + f6(r * 60) + "</b>minutes</span>";
  }
  o.innerHTML = "<b>" + label + "</b>" + chips;
}

/* --- fc3: fraction arithmetic --- */
function fc3Gcd(x, y) { x = Math.abs(x); y = Math.abs(y); while (y) { var t = x % y; x = y; y = t; } return x || 1; }
function fc3() {
  var o = $("fc3-out");
  var a = m4Num("fc3-a"), b = m4Num("fc3-b"), c = m4Num("fc3-c"), d = m4Num("fc3-d"), op = String($("fc3-op").value || "+");
  if (a === null || b === null || c === null || d === null) { o.innerHTML = "Fill in all four boxes (numerators and denominators)."; return; }
  if (b === 0 || d === 0) { o.innerHTML = "Denominators cannot be zero \u2014 a number divided by nothing is undefined."; return; }
  var num = 0, den = 1, opTxt = "+";
  if (op === "+") { num = a * d + c * b; den = b * d; opTxt = "+"; }
  else if (op === "-") { num = a * d - c * b; den = b * d; opTxt = "\u2212"; }
  else if (op === "*") { num = a * c; den = b * d; opTxt = "\u00d7"; }
  else { num = a * d; den = b * c; opTxt = "\u00f7"; }
  if (den === 0) { o.innerHTML = "Cannot divide by a zero fraction \u2014 that is undefined."; return; }
  if (den < 0) { num = -num; den = -den; }
  var g = fc3Gcd(num, den), rn = num / g, rd = den / g;
  var dec = (num / den), whole = Math.trunc(rn / rd), rem = Math.abs(rn % rd);
  var mixTxt = (rd !== 1 && Math.abs(rn) > rd && rem !== 0) ? " \u00b7 as a mixed number: " + whole + " " + Math.abs(rem) + "/" + rd : "";
  o.innerHTML = "<b>" + a + "/" + b + " " + opTxt + " " + c + "/" + d + " = " + rn + (rd === 1 ? "" : "/" + rd) + "</b>" +
    "<span class='jf-chip'><b>" + dec.toFixed(4).replace(/0+$/, "").replace(/\.$/, "") + "</b>decimal</span>" +
    (g > 1 ? "<span class='jf-chip'><b>" + num + "/" + den + "</b>before reducing (GCD " + g + ")</span>" : "<span class='jf-chip'><b>1</b>already lowest terms</span>") +
    mixTxt;
}

/* --- gp3: weighted GPA --- */
var GP3_ADD_HTML = '<div class="row gp3-row"><div><input class="in" type="text" placeholder="Course name (optional)" aria-label="Course" autocomplete="off"></div><div><select class="gp3-g" aria-label="Grade (4.0 scale)"><option value="4">A (4.0)</option><option value="3.7">A- (3.7)</option><option value="3.3">B+ (3.3)</option><option value="3">B (3.0)</option><option value="2.7">B- (2.7)</option><option value="2.3">C+ (2.3)</option><option value="2">C (2.0)</option><option value="1.7">C- (1.7)</option><option value="1.3">D+ (1.3)</option><option value="1">D (1.0)</option><option value="0">F (0.0)</option></select></div><div><input class="in gp3-cre" type="number" step="any" min="0" value="3" aria-label="Credits" autocomplete="off"></div><div><button type="button" class="btn ghost" onclick="gp3Del(this)" aria-label="Remove course">&times;</button></div></div>';
function gp3() {
  var o = $("gp3-out");
  var rows = document.querySelectorAll(".gp3-row") || [];
  var qp = 0, cre = 0, n = 0;
  Array.prototype.forEach.call(rows, function (row) {
    var gEl = row.querySelector(".gp3-g"), cEl = row.querySelector(".gp3-cre");
    if (!gEl || !cEl) return;
    var g = parseFloat(gEl.value), cr = parseFloat(cEl.value);
    if (isFinite(g) && isFinite(cr) && cr > 0) { qp += g * cr; cre += cr; n++; }
  });
  if (!n) { o.innerHTML = "Add at least one course with a grade and credit hours."; return; }
  var gpa = qp / cre;
  o.innerHTML = "<b>GPA " + gpa.toFixed(2) + "</b> on the 4.0 scale" +
    "<span class='jf-chip'><b>" + n + "</b>courses counted</span>" +
    "<span class='jf-chip'><b>" + (Math.round(cre * 100) / 100) + "</b>total credits</span>" +
    "<span class='jf-chip'><b>" + (Math.round(qp * 100) / 100) + "</b>quality points</span>" +
    (gpa >= 3.6 ? "<span class='jf-chip jf-chip-bad'><b>strong</b>standing</span>" : "<span class='jf-chip'><b>keep going</b>standing</span>");
}
function gp3Add() {
  var c = $("gp3-rows");
  if (c) c.insertAdjacentHTML("beforeend", GP3_ADD_HTML);
  gp3();
}
function gp3Del(b) {
  var r = b.closest ? b.closest(".gp3-row") : (b.parentNode && b.parentNode.parentNode);
  if (r && r.parentNode) r.parentNode.removeChild(r);
  gp3();
}

/* --- dp3: depreciation schedule --- */
function dp3() {
  var o = $("dp3-out"), tbl = $("dp3-table");
  var c = m4Num("dp3-c"), s = m4Num("dp3-s"), y = m4Num("dp3-y"), m = String($("dp3-m").value || "sl");
  if (c === null || c <= 0 || s === null || s < 0 || y === null || Math.floor(y) !== y || y < 1) {
    o.innerHTML = "Enter a positive cost, a non-negative salvage value and a whole number of years (1 or more).";
    if (tbl) tbl.innerHTML = "";
    return;
  }
  if (s > c) { o.innerHTML = "Salvage value cannot exceed the asset cost."; if (tbl) tbl.innerHTML = ""; return; }
  var rows = "<thead><tr><th>Year</th><th>Depreciation</th><th>Accumulated</th><th>Book value</th></tr></thead><tbody>";
  var bv = c, acc = 0, first = 0;
  for (var k = 1; k <= y; k++) {
    var dep;
    if (m === "ddb") {
      dep = Math.min(bv - s, bv * (2 / y));
    } else {
      dep = (c - s) / y;
    }
    if (k === y && m === "sl") dep = c - s - acc;
    dep = Math.round(dep * 100) / 100;
    if (k === 1) first = dep;
    acc += dep; bv -= dep;
    if (bv < s) { bv = s; }
    rows += "<tr><td>" + k + "</td><td>" + dep.toFixed(2) + "</td><td>" + acc.toFixed(2) + "</td><td>" + bv.toFixed(2) + "</td></tr>";
  }
  rows += "</tbody>";
  o.innerHTML = "<b>" + (m === "ddb" ? "Double declining balance" : "Straight line") + ":</b> first-year depreciation " + first.toFixed(2) +
    "<span class='jf-chip'><b>" + (c - s > 0 ? ((c - s) / y).toFixed(2) : "0.00").toString() + "</b>per year (straight-line ref)</span>" +
    "<span class='jf-chip'><b>" + (c - s).toFixed(2) + "</b>total depreciated</span>" +
    "<span class='jf-chip'><b>" + bv.toFixed(2) + "</b>final book value</span>";
  if (tbl) tbl.innerHTML = rows;
}

/* --- wq3: daily water intake --- */
function wq3() {
  var o = $("wq3-out");
  var w = m4Num("wq3-w"), x = m4Num("wq3-x"), cl = String($("wq3-cl").value || "mild");
  if (w === null || w <= 0) { o.innerHTML = "Enter your body weight in kilograms (a positive number)."; return; }
  if (x === null || x < 0) x = 0;
  var ml = w * 33 + Math.floor(x / 30) * 500 + (x % 30 >= 15 ? 250 : 0);
  var climTxt = "";
  if (cl === "hot") { ml = ml * 1.12; climTxt = "<span class='jf-chip'><b>+12%</b>hot-climate allowance</span>"; }
  ml = Math.round(ml / 10) * 10;
  o.innerHTML = "<b>" + (ml / 1000).toFixed(2) + " L</b> of fluid per day" +
    "<span class='jf-chip'><b>" + Math.round(ml / 240) + "</b>US cups (240 ml)</span>" +
    "<span class='jf-chip'><b>" + Math.round(ml / 250) + "</b>glasses (250 ml)</span>" +
    "<span class='jf-chip'><b>" + Math.round(ml / 0.355) + "</b>remaining per waking hour (16 h)</span>" + climTxt;
}

/* wire the batch-18 engines into the shared M3 finisher (live recalc + copy + counter) */
["tz3", "mo3", "st3", "sd3", "fc3", "gp3", "dp3", "wq3"].forEach(function (fn) {
  var orig = window[fn] || eval(fn);
  if (typeof orig !== "function") return;
  window[fn] = function () { orig(); m3After(); };
});
/* ---------- M5: batch 19 new tools (sc2 sci-calc, wh2 wheel, if2 inflation,
   zs2 z-score, bn2 text-binary, iw2 ideal-weight, mc2 macros, rt2 reading-time) ---------- */
function m5Num(id) {
  var v = String($(id).value || "").trim();
  return (v === "" || !isFinite(+v)) ? null : +v;
}

/* --- sc2: scientific calculator --- */
var SC2_FNS = { sin: 1, cos: 1, tan: 1, asin: 1, acos: 1, atan: 1, ln: 1, log: 1, sqrt: 1, abs: 1 };
var SC2_PRE = { "+": 1, "-": 1, "*": 2, "/": 2, "u": 3, "^": 4 };
function sc2Erf(x) {
  var s = x < 0 ? -1 : 1; x = Math.abs(x);
  var a1 = 0.254829592, a2 = -0.284496736, a3 = 1.421413741, a4 = -1.453152027, a5 = 1.061405429, p = 0.3275911;
  var t = 1 / (1 + p * x);
  return s * (1 - ((((a5 * t + a4) * t + a3) * t + a2) * t + a1) * t * Math.exp(-x * x));
}
function sc2Eval(s, mode) {
  var D = mode === "rad" ? 1 : Math.PI / 180;
  var toks = s.match(/\d+\.?\d*(?:[eE][+-]?\d+)?|\.\d+(?:[eE][+-]?\d+)?|[A-Za-z]+|\S/g) || [];
  var out = [], ops = [], prev = null, i, t;
  for (i = 0; i < toks.length; i++) {
    t = toks[i];
    if (/^[\d.]/.test(t)) { out.push(+t); prev = "n"; }
    else if (/^[A-Za-z]+$/.test(t)) {
      var low = t.toLowerCase();
      if (low === "pi" || low === "\u03c0") { out.push(Math.PI); prev = "n"; }
      else if (low === "e") { out.push(Math.E); prev = "n"; }
      else if (SC2_FNS[low]) { ops.push(low); prev = "f"; }
      else throw new Error("unknown name: " + t);
    } else if (t === "(") { ops.push("("); prev = "("; }
    else if (t === ")") {
      while (ops.length && ops[ops.length - 1] !== "(") out.push(ops.pop());
      if (!ops.length) throw new Error("unbalanced brackets");
      ops.pop();
      if (ops.length && SC2_FNS[ops[ops.length - 1]]) out.push(ops.pop());
      prev = "n";
    }
    else if (t === "%") { out.push("%"); prev = "n"; }
    else if (t in SC2_PRE) {
      var op = t;
      if (op === "-" && (prev === null || prev === "o" || prev === "(" || prev === "f")) op = "u";
      if (op === "+" && (prev === null || prev === "o" || prev === "(")) continue;
      var rightAssoc = (op === "^" || op === "u");
      while (ops.length && ops[ops.length - 1] !== "(" &&
             (SC2_PRE[ops[ops.length - 1]] > SC2_PRE[op] ||
              (SC2_PRE[ops[ops.length - 1]] === SC2_PRE[op] && !rightAssoc))) {
        out.push(ops.pop());
      }
      ops.push(op); prev = "o";
    } else throw new Error("unexpected: " + t);
  }
  while (ops.length) {
    var o = ops.pop();
    if (o === "(") throw new Error("unbalanced brackets");
    out.push(o);
  }
  var st = [], k, a, b;
  for (k = 0; k < out.length; k++) {
    var tk = out[k];
    if (typeof tk === "number") { st.push(tk); continue; }
    if (tk === "u") { a = st.pop(); st.push(-a); }
    else if (tk === "%") { a = st.pop(); st.push(a / 100); }
    else if (tk === "+") { b = st.pop(); a = st.pop(); st.push(a + b); }
    else if (tk === "-") { b = st.pop(); a = st.pop(); st.push(a - b); }
    else if (tk === "*") { b = st.pop(); a = st.pop(); st.push(a * b); }
    else if (tk === "/") { b = st.pop(); a = st.pop(); st.push(a / b); }
    else if (tk === "^") { b = st.pop(); a = st.pop(); st.push(Math.pow(a, b)); }
    else if (SC2_FNS[tk]) {
      a = st.pop();
      if (tk === "sin") st.push(Math.sin(a * D));
      else if (tk === "cos") st.push(Math.cos(a * D));
      else if (tk === "tan") st.push(Math.tan(a * D));
      else if (tk === "asin") st.push(Math.asin(a) / D);
      else if (tk === "acos") st.push(Math.acos(a) / D);
      else if (tk === "atan") st.push(Math.atan(a) / D);
      else if (tk === "ln") st.push(Math.log(a));
      else if (tk === "log") st.push(Math.log10 ? Math.log10(a) : Math.log(a) / Math.LN10);
      else if (tk === "sqrt") st.push(Math.sqrt(a));
      else if (tk === "abs") st.push(Math.abs(a));
    }
  }
  if (st.length !== 1 || !isFinite(st[0])) throw new Error("not a finite result");
  return st[0];
}
var SC2_HIST = [];
function sc2() {
  var o = $("sc2-out");
  var s = String($("sc2-d").value || "")
    .replace(/\u00d7/g, "*").replace(/\u00f7/g, "/").replace(/\u2212/g, "-")
    .replace(/\u221a/g, "sqrt").replace(/\u03c0/g, "pi").trim();
  if (!s) { o.innerHTML = "Type an expression or tap the keypad."; return; }
  try {
    var r = sc2Eval(s, String($("sc2-m").value) === "rad" ? "rad" : "deg");
    var shown = Math.abs(r) >= 1e12 || (Math.abs(r) < 1e-9 && r !== 0) ? r.toExponential(6) : String(Math.round(r * 1e10) / 1e10);
    SC2_HIST.unshift(s + " = " + shown);
    SC2_HIST = SC2_HIST.slice(0, 5);
    o.innerHTML = "<b>" + shown + "</b>";
    var h = $("sc2-hist");
    if (h) h.innerHTML = SC2_HIST.slice(1).map(function (x) {
      return "<span class='jf-chip'><b>" + escHtml(x.split(" = ")[1]) + "</b>" + escHtml(x.split(" = ")[0]) + "</span>";
    }).join("");
  } catch (e) {
    o.innerHTML = "Cannot parse that expression \u2014 check brackets and operators (" + escHtml(String(e.message || e)) + ").";
  }
}
function sc2K(t) {
  var inp = $("sc2-d");
  if (!inp) return;
  if (t === "AC") inp.value = "";
  else if (t === "\u232b") inp.value = String(inp.value).replace(/.{1}$/, "").replace(/sin$/i, "").replace(/cos$/i, "").replace(/tan$/i, "").replace(/log$/i, "").replace(/sqrt$/i, "");
  else inp.value = String(inp.value) + t;
  sc2();
}

/* --- wh2: spin the wheel --- */
var WH2_ROT = 0, WH2_HIST = [], WH2_W = "";
function wh2Opts() {
  var seen = {}, arr = [];
  String($("wh2-in").value || "").split("\n").forEach(function (s) {
    s = s.trim();
    if (s && !seen[s]) { seen[s] = 1; arr.push(s); }
  });
  return arr;
}
function wh2WinnerAll(rot, n) {
  var seg = (Math.PI * 2) / n;
  var p = (1.5 * Math.PI - rot) % (Math.PI * 2);
  if (p < 0) p += Math.PI * 2;
  return Math.min(n - 1, Math.floor(p / seg));
}
function wh2Draw() {
  var cv = $("wh2-canvas");
  if (!cv || !cv.getContext) return;
  var ctx = cv.getContext("2d");
  if (!ctx) return;
  var opts = wh2Opts(), n = opts.length, w = cv.width, h = cv.height, cx = w / 2, cy = h / 2, R = Math.min(cx, cy) - 6;
  ctx.clearRect(0, 0, w, h);
  for (var i = 0; i < n; i++) {
    var a0 = i * (Math.PI * 2) / n + WH2_ROT, a1 = (i + 1) * (Math.PI * 2) / n + WH2_ROT;
    ctx.beginPath(); ctx.moveTo(cx, cy); ctx.arc(cx, cy, R, a0, a1); ctx.closePath();
    ctx.fillStyle = "hsl(" + Math.round(i * 360 / n) + ", 70%, " + (i % 2 ? 62 : 48) + "%)";
    ctx.fill(); ctx.strokeStyle = "#1d2230"; ctx.stroke();
  }
  ctx.fillStyle = "#f5f7fa"; ctx.font = "bold " + Math.max(11, Math.round(R / 9)) + "px sans-serif";
  ctx.textAlign = "right"; ctx.textBaseline = "middle";
  for (i = 0; i < n; i++) {
    var mid = (i + 0.5) * (Math.PI * 2) / n + WH2_ROT;
    ctx.save(); ctx.translate(cx, cy); ctx.rotate(mid);
    ctx.fillText(opts[i].slice(0, 14), R - 12, 0);
    ctx.restore();
  }
  ctx.beginPath(); ctx.arc(cx, cy, 14, 0, Math.PI * 2); ctx.fillStyle = "#ff7000"; ctx.fill();
  ctx.beginPath(); ctx.moveTo(cx - 10, 2); ctx.lineTo(cx + 10, 2); ctx.lineTo(cx, 26); ctx.closePath();
  ctx.fillStyle = "#ff7000"; ctx.fill();
}
function wh2Spin(btn) {
  var opts = wh2Opts();
  var o = $("wh2-out");
  if (opts.length < 2) { if (o) o.innerHTML = "Add at least two options, one per line."; return; }
  var start = WH2_ROT, target = start + Math.PI * 2 * (5 + Math.random() * 3), t0 = null, DUR = 3800;
  if (btn) btn.disabled = true;
  function frame(ts) {
    if (!t0) t0 = ts;
    var k = Math.min(1, (ts - t0) / DUR), e = 1 - Math.pow(1 - k, 3);
    WH2_ROT = start + (target - start) * e;
    wh2Draw();
    if (k < 1) requestAnimationFrame(frame);
    else {
      if (btn) btn.disabled = false;
      var idx = wh2WinnerAll(WH2_ROT, opts.length);
      WH2_W = opts[idx];
      var o2 = $("wh2-out");
      if (o2) {
        o2.innerHTML = "<b>\u{1F3AF} " + escHtml(WH2_W) + "</b>";
        var hist = $("wh2-hist");
        WH2_HIST.unshift(WH2_W);
        WH2_HIST = WH2_HIST.slice(0, 8);
        if (hist) hist.innerHTML = "<span class='jf-chip'><b>" + WH2_HIST.length + "</b>spins this visit</span>" +
          WH2_HIST.slice(0, 5).map(function (w2, j) { return "<span class='jf-chip'><b>" + (j + 1) + "</b>" + escHtml(w2) + "</span>"; }).join("");
      }
    }
  }
  requestAnimationFrame(frame);
}
function wh2Copy(btn) {
  if (WH2_W) copyText(WH2_W, btn);
}

/* --- if2: inflation --- */
function if2() {
  var o = $("if2-out");
  var m = m5Num("if2-m"), r = m5Num("if2-r"), y = m5Num("if2-y"), mo = String($("if2-mo").value || "fwd");
  if (m === null || m <= 0 || r === null || r < 0 || y === null || y <= 0) {
    o.innerHTML = "Enter a positive amount, a non-negative rate and a positive number of years."; return;
  }
  var f = Math.pow(1 + r / 100, y);
  var v = mo === "bwd" ? m / f : m * f;
  o.innerHTML = "<b>" + v.toFixed(2) + "</b> " + (mo === "bwd" ? "in today's money" : "in " + Math.round(y) + " years") +
    "<span class='jf-chip'><b>" + f.toFixed(4) + "</b>total multiplier</span>" +
    "<span class='jf-chip'><b>" + ((f - 1) * 100).toFixed(1) + "%</b>cumulative inflation</span>" +
    "<span class='jf-chip'><b>" + (mo === "bwd" ? (m - v).toFixed(2) + " lost" : (v - m).toFixed(2) + " needed above " + m.toFixed(2)) + "</b>gap</span>";
}

/* --- zs2: z-score --- */
function zs2() {
  var o = $("zs2-out");
  var x = m5Num("zs2-x"), mu = m5Num("zs2-mu"), sd = m5Num("zs2-sd");
  if (x === null || mu === null || sd === null || sd <= 0) {
    o.innerHTML = "Enter your value, the mean and a positive standard deviation."; return;
  }
  var z = (x - mu) / sd;
  var phi = 0.5 * (1 + sc2Erf(z / Math.SQRT2));
  var pPct = phi * 100;
  o.innerHTML = "<b>z = " + z.toFixed(2) + "</b>" +
    "<span class='jf-chip'><b>" + pPct.toFixed(2) + "%</b>score at or below</span>" +
    "<span class='jf-chip'><b>" + (100 - pPct).toFixed(2) + "%</b>score higher</span>" +
    "<span class='jf-chip'><b>" + (2 * (1 - phi) * 100).toFixed(2) + "%</b>in two-tailed tail beyond |z|</span>";
}

/* --- bn2: text <-> binary --- */
function bn2ByteBits(b) {
  var s = b.toString(2);
  while (s.length < 8) s = "0" + s;
  return s;
}
function bn2() {
  var o = $("bn2-out"), meta = $("bn2-meta");
  var s = String($("bn2-in").value || ""), m = String($("bn2-m").value || "tobin");
  if (!o) return;
  try {
    if (m === "totext") {
      var clean = s.replace(/[^01]/g, "");
      if (!clean.length) { o.value = ""; if (meta) meta.innerHTML = "<span class='jf-chip'><b>0</b>bits decoded</span>"; return; }
      var pad = (8 - clean.length % 8) % 8;
      clean = "0".repeat(pad) + clean;
      var bytes = new Uint8Array(clean.length / 8);
      for (var i = 0; i < bytes.length; i++) bytes[i] = parseInt(clean.substr(i * 8, 8), 2);
      var txt = new TextDecoder().decode(bytes);
      o.value = txt;
      if (meta) meta.innerHTML = "<span class='jf-chip'><b>" + bytes.length + "</b>bytes decoded</span><span class='jf-chip'><b>" + txt.length + "</b>characters</span>";
    } else {
      var bs = new TextEncoder().encode(s);
      var groups = [];
      for (var j = 0; j < bs.length; j++) groups.push(bn2ByteBits(bs[j]));
      o.value = groups.join(" ");
      if (meta) meta.innerHTML = "<span class='jf-chip'><b>" + bs.length + "</b>bytes encoded</span><span class='jf-chip'><b>" + bs.length * 8 + "</b>bits</span>";
    }
  } catch (e) {
    o.value = "";
    if (meta) meta.innerHTML = "<span class='jf-chip jf-chip-bad'><b>error</b>cannot decode that byte sequence</span>";
  }
}
function bn2Swap() {
  var o = $("bn2-out");
  if (o && o.value) { $("bn2-in").value = o.value; bn2(); }
}

/* --- iw2: ideal weight --- */
function iw2() {
  var o = $("iw2-out");
  var h = m5Num("iw2-h"), g = String($("iw2-g").value || "m");
  if (h === null || h <= 0) { o.innerHTML = "Enter a positive height in centimetres."; return; }
  var inch = h / 2.54, over = Math.max(0, inch - 60);
  var D = g === "f" ? 45.5 + 2.3 * over : 50 + 2.3 * over;
  var Ro = g === "f" ? 49 + 1.7 * over : 52 + 1.9 * over;
  var Mi = g === "f" ? 53.1 + 1.36 * over : 56.2 + 1.41 * over;
  var Ha = g === "f" ? 45.5 + 2.2 * over : 48 + 2.7 * over;
  var m2 = Math.pow(h / 100, 2);
  var lo = 18.5 * m2, hi = 24.9 * m2;
  o.innerHTML = "<b>Devine " + D.toFixed(1) + " kg</b>" +
    "<span class='jf-chip'><b>" + Ro.toFixed(1) + "</b>Robinson kg</span>" +
    "<span class='jf-chip'><b>" + Mi.toFixed(1) + "</b>Miller kg</span>" +
    "<span class='jf-chip'><b>" + Ha.toFixed(1) + "</b>Hamwi kg</span>" +
    "<span class='jf-chip'><b>" + lo.toFixed(1) + "\u2013" + hi.toFixed(1) + "</b>healthy BMI range kg</span>";
}

/* --- mc2: macros --- */
function mc2() {
  var o = $("mc2-out");
  var c = m5Num("mc2-c"), g = String($("mc2-g").value || "bal");
  if (c === null || c <= 0) { o.innerHTML = "Enter a positive daily calorie target."; return; }
  var SPLIT = { bal: [30, 40, 30], hp: [40, 30, 30], lc: [40, 20, 40] };
  var sp = SPLIT[g] || SPLIT.bal;
  var p = c * sp[0] / 100 / 4, cb = c * sp[1] / 100 / 4, ft = c * sp[2] / 100 / 9;
  o.innerHTML = "<b>" + Math.round(p) + " g protein</b>" +
    "<span class='jf-chip'><b>" + Math.round(cb) + "</b>g carbs</span>" +
    "<span class='jf-chip'><b>" + Math.round(ft) + "</b>g fat</span>" +
    "<span class='jf-chip'><b>" + sp.join("/") + "</b>P/C/F split</span>" +
    "<span class='jf-chip'><b>" + Math.round(p * 4) + "</b>kcal from protein</span>";
}

/* --- rt2: reading time --- */
function rt2() {
  var o = $("rt2-out");
  var s = String($("rt2-in").value || "");
  var words = (s.match(/[A-Za-z0-9'\u2019-]+/g) || []).length;
  var chars = s.trim().length;
  if (!words) { o.innerHTML = "Paste some text above to estimate its reading time."; return; }
  var wpm = +String($("rt2-s").value || "200") || 200;
  var mins = words / wpm;
  var mm = Math.floor(mins), ss = Math.round((mins - mm) * 60);
  if (ss === 60) { mm++; ss = 0; }
  o.innerHTML = "<b>" + mm + " min " + m4Pad(ss) + " s</b> at " + wpm + " wpm" +
    "<span class='jf-chip'><b>" + words + "</b>words</span>" +
    "<span class='jf-chip'><b>" + chars + "</b>characters</span>" +
    "<span class='jf-chip'><b>" + (words / 130).toFixed(1) + "</b>minutes spoken</span>" +
    "<span class='jf-chip'><b>" + (words / 300).toFixed(1) + "</b>printed pages</span>";
}

/* wire the batch-19 engines into the shared M3 finisher */
function wh2() { wh2Draw(); }
["sc2", "wh2", "if2", "zs2", "bn2", "iw2", "mc2", "rt2"].forEach(function (fn) {
  var orig = null;
  try { orig = window[fn] || eval(fn); } catch (e) { orig = null; }
  if (typeof orig !== "function") return;
  window[fn] = function () { orig(); m3After(); };
});
/* ---------- M6: batch 20 new tools (pf2, wg2, rs2, rp2, gc2, sn2, ke2, lc2) ---------- */
function m6Num(id) {
  var v = String($(id).value || "").trim();
  return (v === "" || !isFinite(+v)) ? null : +v;
}

/* --- pf2: prime factorization --- */
function pf2() {
  var o = $("pf2-out");
  var n = m6Num("pf2-n");
  if (n === null || Math.floor(n) !== n || n < 2) {
    o.innerHTML = "Enter a whole number of 2 or more (up to one trillion)."; return;
  }
  if (n > 1e12) { o.innerHTML = "Numbers above one trillion are rejected so the answer is always exact."; return; }
  var x = n, f = [], lim = Math.sqrt(x);
  for (var p = 2; p <= lim; p += (p === 2 ? 1 : 2)) {
    var e = 0;
    while (x % p === 0) { x /= p; e++; }
    if (e) { f.push([p, e]); lim = Math.sqrt(x); }
  }
  if (x > 1) f.push([x, 1]);
  var fac = f.map(function (d) { return d[0] + (d[1] > 1 ? "^" + d[1] : ""); }).join(" \u00d7 ");
  var div = f.reduce(function (a, d) { return a * (d[1] + 1); }, 1);
  var isPri = f.length === 1 && f[0][1] === 1;
  var opt = f.map(function (d) { return d[0] + (d[1] > 1 ? "^" + d[1] : ""); });
  o.innerHTML = isPri
    ? "<b>" + n + " is prime</b><span class='jf-chip'><b>itself</b>only divisors: 1 and " + n + "</span>"
    : "<b>" + n + " = " + fac + "</b>" +
      "<span class='jf-chip'><b>" + div + "</b>divisors</span>" +
      "<span class='jf-chip'><b>" + f.length + "</b>distinct primes</span>" +
      "<span class='jf-chip'><b>" + nfmt(f.map(function (d) { return Math.pow(d[0], d[1]); }).reduce(function (a, b) { return a + b; }, 0)) + "</b>sum of prime powers</span>" +
      "<span class='jf-chip'><b>" + (div % 2 === 0 ? "not" : "yes") + "</b>perfect square?</span>";
}

/* --- wg2: hourly wage --- */
function wg2() {
  var o = $("wg2-out");
  var r = m6Num("wg2-r"), h = m6Num("wg2-h"), ot = m6Num("wg2-o"), om = m6Num("wg2-m");
  if (r === null || r < 0 || h === null || h < 0) { o.innerHTML = "Enter a non-negative hourly rate and hours."; return; }
  if (ot === null || ot < 0) ot = 40;
  if (om === null || om <= 0) om = 1.5;
  var regH = Math.min(h, ot), otH = Math.max(0, h - ot);
  var reg = r * regH, otp = r * om * otH, wk = reg + otp;
  o.innerHTML = "<b>" + wk.toFixed(2) + "</b> gross this week" +
    "<span class='jf-chip'><b>" + reg.toFixed(2) + "</b>regular pay (" + regH + " h)</span>" +
    "<span class='jf-chip'><b>" + otp.toFixed(2) + "</b>overtime pay (" + otH + " h \u00d7 " + om + " rate)</span>" +
    "<span class='jf-chip'><b>" + (wk * 52).toFixed(0) + "</b>per year (52 wk)</span>" +
    "<span class='jf-chip'><b>" + (wk * 52 / 12).toFixed(0) + "</b>per month</span>" +
    "<span class='jf-chip'><b>" + (wk * 52 / 26).toFixed(0) + "</b>per fortnight</span>";
}

/* --- rs2: random strings (crypto) --- */
function rs2Sets() {
  var U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", L = "abcdefghijklmnopqrstuvwxyz", Dg = "0123456789", S = "!@#$%^&*-_=+?";
  var pool = "";
  if ($("rs2-up").checked) pool += U;
  if ($("rs2-low").checked) pool += L;
  if ($("rs2-dig").checked) pool += Dg;
  if ($("rs2-sym").checked) pool += S;
  if ($("rs2-amb").checked) pool = pool.replace(/[0O1lI|]/g, "");
  return pool;
}
function rs2() {
  var o = $("rs2-out");
  var ln = m6Num("rs2-l"), cnt = m6Num("rs2-c"), pool = rs2Sets();
  ln = ln === null ? 20 : Math.max(1, Math.min(256, Math.round(ln)));
  cnt = cnt === null ? 10 : Math.max(1, Math.min(200, Math.round(cnt)));
  if (!pool.length) { o.value = ""; $("rs2-l").value = ln; $("rs2-c").value = cnt;
    return void 0; }
  var total = ln * cnt, buf = new Uint32Array(total), i, j, lines = [];
  var C = window.crypto || globalThis.crypto;
  for (var off = 0; off < total; off += 16384) C.getRandomValues(buf.subarray(off, Math.min(total, off + 16384)));
  for (i = 0; i < cnt; i++) {
    var s = "";
    for (j = 0; j < ln; j++) s += pool[buf[i * ln + j] % pool.length];
    lines.push(s);
  }
  o.value = lines.join("\n");
  var bits = Math.round(ln * Math.log2(pool.length) * cnt);
  $("rs2-l").value = ln; $("rs2-c").value = cnt;
  o.title = bits + " bits of entropy";
}

/* --- rp2: text repeater --- */
function rp2() {
  var o = $("rp2-out"), meta = $("rp2-meta");
  var s = String($("rp2-in").value || ""), t = m6Num("rp2-t");
  var sv = String($("rp2-s").value || "");
  var sep = sv === "nl" ? "\n" : (sv === "custom" ? String($("rp2-x").value || "") : sv);
  var num = $("rp2-num").checked;
  if (t === null || t < 1) t = 1;
  t = Math.min(10000, Math.round(t));
  if (!s) {
    if (o) o.value = "";
    if (meta) meta.innerHTML = "<span class='jf-chip'><b>0</b>characters out</span>";
    return;
  }
  var parts = [];
  for (var i = 0; i < t; i++) parts.push((num ? (i + 1) + ". " : "") + s);
  var res = parts.join(sep);
  o.value = res;
  if (meta) {
    var kb = res.length / 1024;
    meta.innerHTML = "<span class='jf-chip'><b>" + t + "</b>copies</span>" +
      "<span class='jf-chip'><b>" + res.length + "</b>characters out" + (kb > 1 ? " (" + kb.toFixed(1) + " KB)" : "") + "</span>" +
      "<span class='jf-chip'><b>" + (num ? "numbered" : (sep === "\n" ? "new lines" : (sep === "" ? "glued" : JSON.stringify(sep)))) + "</b>joined with</span>";
  }
}

/* --- gc2: coordinate converter --- */
function gc2Parse(v) {
  v = String(v || "").trim().replace(/,/g, " ").replace(/[°\u00b0]/g, " ").replace(/['\u2032\u2019]/g, " ").replace(/["\u2033\u201d]/g, " ");
  var parts = v.split(/\s+/).filter(Boolean);
  if (!parts.length) return null;
  if (parts.length === 1) { var d = parseFloat(parts[0]); return isFinite(d) ? d : null; }
  var deg = parseFloat(parts[0]), min = parseFloat(parts[1] || 0), sec = parseFloat(parts[2] || 0);
  if (!isFinite(deg)) return null;
  if (!isFinite(min)) min = 0;
  if (!isFinite(sec)) sec = 0;
  var sign = deg < 0 ? -1 : 1;
  return sign * (Math.abs(deg) + min / 60 + sec / 3600);
}
function gc2FmtDMS(v, pos, neg) {
  var s = v < 0 ? neg : pos, a = Math.abs(v);
  var deg = Math.floor(a), mfull = (a - deg) * 60, min = Math.floor(mfull), sec = (mfull - min) * 60;
  return deg + "\u00b0 " + min + "\u2032 " + sec.toFixed(1) + "\u2033 " + s;
}
function gc2() {
  var o = $("gc2-out");
  var lat = gc2Parse($("gc2-lat").value), lon = gc2Parse($("gc2-lon").value);
  if (lat === null || lon === null) { o.innerHTML = "Enter both a latitude and a longitude (decimal, or degrees minutes seconds)."; return; }
  if (Math.abs(lat) > 90) { o.innerHTML = "Latitude must be within \u00b190\u00b0 \u2014 " + lat.toFixed(4) + " is outside the possible range."; return; }
  if (Math.abs(lon) > 180) { o.innerHTML = "Longitude must be within \u00b1180\u00b0 \u2014 " + lon.toFixed(4) + " is outside the possible range."; return; }
  o.innerHTML = "<b>" + lat.toFixed(6) + ", " + lon.toFixed(6) + "</b>" +
    "<span class='jf-chip'><b>" + gc2FmtDMS(lat, "N", "S") + "</b>latitude DMS</span>" +
    "<span class='jf-chip'><b>" + gc2FmtDMS(lon, "E", "W") + "</b>longitude DMS</span>" +
    "<span class='jf-chip'><b>" + Math.floor(Math.abs(lat)) + "\u00b0 " + ((Math.abs(lat) - Math.floor(Math.abs(lat))) * 60).toFixed(3) + "\u2032 " + (lat >= 0 ? "N" : "S") + "</b>lat DDM</span>" +
    "<span class='jf-chip'><b>" + Math.floor(Math.abs(lon)) + "\u00b0 " + ((Math.abs(lon) - Math.floor(Math.abs(lon))) * 60).toFixed(3) + "\u2032 " + (lon >= 0 ? "E" : "W") + "</b>lon DDM</span>" +
    "<span class='jf-chip'><b>~" + Math.round(111320 * Math.cos(lat * Math.PI / 180)) + "</b>metres per degree of longitude here</span>";
}

/* --- sn2: scientific notation --- */
var SN2_SI = [["y", 1e-24], ["z", 1e-21], ["a", 1e-18], ["f", 1e-15], ["p", 1e-12], ["n", 1e-9],
  ["\u00b5", 1e-6], ["m", 1e-3], ["", 1], ["k", 1e3], ["M", 1e6], ["G", 1e9], ["T", 1e12], ["P", 1e15], ["E", 1e18]];
function sn2Num(v) {
  v = String(v || "").trim().replace(/\u00d7\s*10\s*\^?/gi, "e").replace(/\s+/g, "");
  var m = v.match(/^([+-]?(?:\d+\.?\d*|\.\d+))([eE]([+-]?\d+))?$/);
  if (!m) return null;
  var base = parseFloat(m[1]), ex = m[3] ? parseInt(m[3], 10) : 0;
  return base * Math.pow(10, ex);
}
function sn2() {
  var o = $("sn2-out");
  var v = sn2Num($("sn2-in").value);
  if (v === null) { o.innerHTML = "Enter a number \u2014 plain (0.00000031), scientific (3.1e-7) or with a \u00d710^ part."; return; }
  if (v === 0) { o.innerHTML = "<b>0</b><span class='jf-chip'><b>0</b>zero is its own notation</span>"; return; }
  var ex = Math.floor(Math.log10(Math.abs(v)));
  var mant = Number((v / Math.pow(10, ex)).toPrecision(7));
  if (Math.abs(mant) >= 10) { mant /= 10; ex += 1; }
  var engEx = Math.floor(ex / 3) * 3;
  var engMant = Math.abs(v) / Math.pow(10, engEx);
  var si = SN2_SI[0];
  for (var i = 0; i < SN2_SI.length; i++) if (engEx >= Math.log10(SN2_SI[i][1])) si = SN2_SI[i];
  var siVal = v / si[1];
  o.innerHTML = "<b>" + mant + " \u00d7 10^" + ex + "</b>" +
    "<span class='jf-chip'><b>" + (Math.abs(engMant) >= 100 ? engMant.toFixed(0) : engMant.toPrecision(4).replace(/\.?0+$/, "")) + " \u00d7 10^" + engEx + "</b>engineering</span>" +
    "<span class='jf-chip'><b>" + (Math.abs(siVal) >= 1000 ? siVal.toExponential(2) : siVal.toPrecision(4).replace(/\.?0+$/, "")) + " " + si[0] + "</b>SI prefix</span>" +
    "<span class='jf-chip'><b>" + ex + "</b>order of magnitude</span>";
}

/* --- ke2: caffeine decay --- */
function ke2() {
  var o = $("ke2-out");
  var mg = m6Num("ke2-mg"), hl = m6Num("ke2-hl"), el = m6Num("ke2-el");
  if (mg === null || mg <= 0 || hl === null || hl <= 0 || el === null || el < 0) {
    o.innerHTML = "Enter a positive dose and half-life, and hours elapsed (0 or more)."; return;
  }
  var rem = mg * Math.pow(0.5, el / hl);
  var chips = "";
  for (var k = 1; k <= 4; k++) {
    var t = el + k * hl;
    chips += "<span class='jf-chip'><b>" + (mg * Math.pow(0.5, k)).toFixed(1) + "</b>after " + t.toFixed(0) + " h</span>";
  }
  var cutoff = null;
  for (var h = el; h <= el + 24; h += 0.5) {
    if (mg * Math.pow(0.5, (h - el) / hl) < 50) { cutoff = h; break; }
  }
  o.innerHTML = "<b>" + rem.toFixed(1) + " mg</b> still in your system" +
    "<span class='jf-chip'><b>" + (100 * Math.pow(0.5, el / hl)).toFixed(1) + "%</b>of the dose left</span>" +
    (cutoff !== null && rem >= 50 ? "<span class='jf-chip'><b>" + (cutoff - el).toFixed(1) + " h</b>until under 50 mg</span>" :
      (rem < 50 ? "<span class='jf-chip jf-chip-bad'><b>already</b>under 50 mg now</span>" : "")) + chips;
}

/* --- lc2: Luhn checker --- */
function lc2() {
  var o = $("lc2-out");
  var s = String($("lc2-in").value || "").trim().replace(/[\s-]/g, "");
  if (!/^[0-9Xx]{1,25}$/.test(s)) {
    o.innerHTML = "Enter digits only (2 to 25 of them). Use one X for the unknown check digit."; return;
  }
  if (/[Xx]/.test(s)) {
    if (s.replace(/[^Xx]/g, "").length > 1) { o.innerHTML = "Only one X is supported."; return; }
    var base = s.replace(/[Xx]/, "0");
    var need = (10 - lc2Total(base) % 10) % 10;
    o.innerHTML = "<b>check digit = " + need + "</b>" +
      "<span class='jf-chip'><b>" + base.slice(0, -1) + need + "</b>completed string is then valid</span>" +
      "<span class='jf-chip'><b>yes</b>one typo is caught</span>";
    return;
  }
  var tot = lc2Total(s), ok = tot % 10 === 0;
  o.innerHTML = "<b>" + (ok ? "VALID" : "check digit fails") + "</b>" +
    "<span class='jf-chip'><b>" + tot + "</b>checksum total (mod 10 = " + tot % 10 + ")</span>" +
    "<span class='jf-chip'><b>" + s.length + "</b>digits</span>";
}
function lc2Total(s) {
  var sum = 0, dbl = false;
  for (var i = s.length - 1; i >= 0; i--) {
    var d = +s[i];
    if (dbl) { d *= 2; if (d > 9) d -= 9; }
    sum += d;
    dbl = !dbl;
  }
  return sum;
}

/* wire the batch-20 engines into the shared M3 finisher */
["pf2", "wg2", "rs2", "rp2", "gc2", "sn2", "ke2", "lc2"].forEach(function (fn) {
  var orig = null;
  try { orig = window[fn] || eval(fn); } catch (e) { orig = null; }
  if (typeof orig !== "function") return;
  window[fn] = function () { orig(); m3After(); };
});
/* ---------- M7: batch 21 new tools (cm2, mg2, an2, fe2, fl2, rd2, rc2, dl2) ---------- */
function m7Num(id) {
  var v = String($(id).value || "").trim();
  return (v === "" || !isFinite(+v)) ? null : +v;
}
function m7Money(n) {
  return n.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

/* --- cm2: commission calculator --- */
function cm2() {
  var o = $("cm2-out");
  var s = m7Num("cm2-s"), r = m7Num("cm2-r"), y = m7Num("cm2-y");
  if (s === null || s < 0 || r === null || r < 0) {
    o.innerHTML = "Enter a non-negative sale price and commission rate."; return;
  }
  if (y === null || y < 0) y = 100;
  if (y > 100) y = 100;
  var com = s * r / 100;
  var mine = com * y / 100, house = com - mine;
  o.innerHTML = "<b>" + m7Money(com) + "</b> gross commission" +
    "<span class='jf-chip'><b>" + m7Money(mine) + "</b>your share (" + y + "% of the commission)</span>" +
    "<span class='jf-chip'><b>" + m7Money(house) + "</b>house/others keep (" + (100 - y) + "%)</span>" +
    "<span class='jf-chip'><b>" + m7Money(mine * 12) + "</b>your share if this deal repeated monthly</span>" +
    (s > 0 ? "<span class='jf-chip'><b>" + (com / s * 100).toFixed(2) + "%</b>effective rate on the sale</span>" : "");
}

/* --- mg2: meeting cost --- */
function mg2() {
  var o = $("mg2-out");
  var n = m7Num("mg2-n"), r = m7Num("mg2-r"), d = m7Num("mg2-d"), w = m7Num("mg2-w");
  if (n === null || n < 1 || r === null || r < 0 || d === null || d <= 0) {
    o.innerHTML = "Enter the attendee count, an hourly cost and a length in minutes."; return;
  }
  if (w === null || w < 0) w = 1;
  var hrs = d / 60, cost = n * r * hrs;
  o.innerHTML = "<b>" + m7Money(cost) + "</b>per meeting" +
    "<span class='jf-chip'><b>" + nfmt(cost * w, 0) + "</b>per week (" + w + "\u00d7)</span>" +
    "<span class='jf-chip'><b>" + nfmt(cost * w * 46, 0) + "</b>per year (46 working weeks)</span>" +
    "<span class='jf-chip'><b>" + nfmt(n * hrs, 1) + " h</b>person-hours consumed per meeting</span>" +
    "<span class='jf-chip'><b>" + nfmt(n * hrs * w * 46, 0) + " h</b>person-hours per year</span>";
}

/* --- an2: angle converter --- */
function an2() {
  var o = $("an2-out");
  var v = m7Num("an2-v");
  var u = String($("an2-u").value || "deg");
  if (v === null) { o.innerHTML = "Enter a numeric angle value."; return; }
  var F = { "deg": 1, "rad": 180 / Math.PI, "gon": 0.9, "turn": 360, "amin": 1 / 60, "asec": 1 / 3600 };
  var deg = v * F[u];
  var rad = deg * Math.PI / 180;
  var piForm = null;
  if (Math.abs(rad / Math.PI - Math.round(rad / Math.PI * 2) / 2) < 1e-9) {
    var h = Math.round(rad / Math.PI * 2) / 2;
    piForm = (h === 0 ? "0" : (h === 1 ? "\u03c0" : (Math.abs(h) < 1 ? (Math.abs(h) === 0.5 ? "\u03c0/2" : (Math.abs(h) === 0.25 ? "\u03c0/4" : (Math.abs(h) === 0.75 ? "3\u03c0/4" : ""))) : h + "\u03c0"))) + (h < 0 ? " (negative)" : "");
  }
  o.innerHTML = "<b>" + nfmt(deg, 4) + "\u00b0</b> degrees" +
    "<span class='jf-chip'><b>" + rad.toPrecision(6).replace(/0+$/, "").replace(/\.$/, "") + " rad</b>radians" + (piForm ? " (" + piForm + ")" : "") + "</span>" +
    "<span class='jf-chip'><b>" + nfmt(deg / 0.9, 4) + "</b>gradians (gon)</span>" +
    "<span class='jf-chip'><b>" + nfmt(deg / 360, 4) + "</b>turns</span>" +
    "<span class='jf-chip'><b>" + nfmt(deg * 60, 0) + "\u2032</b>arcminutes</span>" +
    "<span class='jf-chip'><b>" + nfmt(deg * 3600, 0) + "\u2033</b>arcseconds</span>";
}

/* --- fe2: fuel economy converter --- */
function fe2() {
  var o = $("fe2-out");
  var v = m7Num("fe2-v");
  var u = String($("fe2-u").value || "us");
  if (v === null || v < 0) { o.innerHTML = "Enter a non-negative fuel economy value."; return; }
  var TO_KML = { "us": 1.60934 / 3.78541, "uk": 1.60934 / 4.54609, "kml": 1 };
  var kml = u === "l100" ? 100 / v : v * TO_KML[u];
  o.innerHTML = "<b>" + (100 / kml).toFixed(2) + " L/100 km</b>" +
    "<span class='jf-chip'><b>" + kml.toFixed(2) + "</b>km/L</span>" +
    "<span class='jf-chip'><b>" + (kml / (1.60934 / 3.78541)).toFixed(2) + "</b>mpg (US)</span>" +
    "<span class='jf-chip'><b>" + (kml / (1.60934 / 4.54609)).toFixed(2) + "</b>mpg (UK, imperial)</span>" +
    "<span class='jf-chip'><b>" + (100 * 1.60934 / 3.78541).toFixed(3) + " \u00f7 mpg US</b>quick rule gives L/100 km</span>";
}

/* --- fl2: Flesch reading level --- */
function fl2Syl(word) {
  var w = word.toLowerCase().replace(/[^a-z]/g, "");
  if (!w) return 0;
  var g = w.match(/[aeiouy]+/g);
  var n = g ? g.length : 0;
  if (n > 1 && /e$/.test(w)) n--;
  return Math.max(1, n);
}
function fl2() {
  var o = $("fl2-out");
  var t = String($("fl2-in").value || "").trim();
  if (!t) { o.innerHTML = "Paste some text \u2014 a paragraph or the whole article \u2014 and it is scored instantly."; return; }
  var sents = t.split(/[.!?\u2026]+(?:\s|$)/).filter(Boolean);
  var words = t.match(/[A-Za-z\u00c0-\u024f'-]+/g) || [];
  var syl = 0;
  for (var i = 0; i < words.length; i++) syl += fl2Syl(words[i]);
  if (!sents.length || !words.length) { o.innerHTML = "Not enough text to score \u2014 add at least one full sentence."; return; }
  var wps = words.length / sents.length, spw = syl / words.length;
  var fre = 206.835 - 1.015 * wps - 84.6 * spw;
  var fk = 0.39 * wps + 11.8 * spw - 15.59;
  var label = fre >= 90 ? "very easy" : fre >= 80 ? "easy" : fre >= 70 ? "fairly easy" :
    fre >= 60 ? "plain English (standard)" : fre >= 50 ? "fairly difficult" : fre >= 30 ? "difficult" : "very confusing";
  o.innerHTML = "<b>" + fre.toFixed(1) + "</b> Flesch Reading Ease \u2014 " + label +
    "<span class='jf-chip'><b>" + (fk < 0 ? 0 : fk.toFixed(1)) + "</b>Flesch\u2013Kincaid grade level</span>" +
    "<span class='jf-chip'><b>" + words.length + "</b>words</span>" +
    "<span class='jf-chip'><b>" + sents.length + "</b>sentences</span>" +
    "<span class='jf-chip'><b>" + wps.toFixed(1) + "</b>words per sentence (aim \u2264 20)</span>" +
    "<span class='jf-chip'><b>" + nfmt(spw, 2) + "</b>syllables per word</span>";
}

/* --- rd2: random decimals (crypto) --- */
function rd2() {
  var o = $("rd2-out");
  var mn = m7Num("rd2-min"), mx = m7Num("rd2-max"), d = m7Num("rd2-d"), c = m7Num("rd2-c");
  if (mn === null || mx === null) { o.innerHTML = "Enter a minimum and a maximum for the range."; return; }
  if (mx <= mn) { o.innerHTML = "The maximum must be greater than the minimum."; return; }
  d = d === null ? 2 : Math.max(0, Math.min(8, Math.round(d)));
  c = c === null ? 10 : Math.max(1, Math.min(200, Math.round(c)));
  var buf = new Uint32Array(c);
  (window.crypto || globalThis.crypto).getRandomValues(buf);
  var lines = [], lo = Infinity, hi = -Infinity, sum = 0, i, val;
  for (i = 0; i < c; i++) {
    val = mn + (mx - mn) * buf[i] / 4294967296;
    val = +val.toFixed(d);
    lines.push(val.toFixed(d));
    if (val < lo) lo = val;
    if (val > hi) hi = val;
    sum += val;
  }
  o.value = lines.join("\n");
  o.title = c + " uniform draws from " + mn + " to " + mx + " at " + d + " decimals";
  var meta = $("rd2-meta");
  if (meta) meta.innerHTML = "<span class='jf-chip'><b>" + nfmt(lo, d) + "</b>lowest draw</span>" +
    "<span class='jf-chip'><b>" + nfmt(hi, d) + "</b>highest draw</span>" +
    "<span class='jf-chip'><b>" + nfmt(sum / c, d + 2) + "</b>mean of the draws</span>";
}

/* --- rc2: recipe scaler --- */
function rc2Frac(v) {
  var whole = Math.floor(Math.abs(v)), frac = Math.abs(v) - whole;
  var e = Math.round(frac * 8), sign = v < 0 ? "\u2212" : "";
  if (e >= 8) { whole += 1; e = 0; }
  function g(a, b) { return b ? g(b, a % b) : a; }
  var dd = 8 / g(e || 8, 8), nn = (e || 0) * dd / 8;
  var f = (whole ? sign + whole : "") + (e ? (whole ? " " : sign) + nn + "/" + dd : "");
  return f || "0";
}
function rc2() {
  var o = $("rc2-out");
  var org = m7Num("rc2-o"), nw = m7Num("rc2-n");
  var t = String($("rc2-in").value || "").trim();
  if (!t) { o.innerHTML = "Paste your ingredient lines \u2014 one per row, amount first."; return; }
  if (org === null || org <= 0 || nw === null || nw <= 0) { o.innerHTML = "Enter the original servings and the desired servings (both positive)."; return; }
  var k = nw / org, lines = t.split("\n"), out = [], changed = 0;
  for (var i = 0; i < lines.length; i++) {
    var L = lines[i];
    var m = L.match(/^\s*(\d+(?:\.\d+)?)(?:\s+(\d+)\s*\/\s*(\d+))?\s+(.*)$/);
    if (!m) { out.push(L); continue; }
    var amt = +m[1] + (m[2] ? (+m[2]) / (+m[3]) : 0);
    if (!isFinite(amt) || amt <= 0) { out.push(L); continue; }
    changed++;
    out.push(rc2Frac(amt * k) + " " + m[4]);
  }
  if (!changed) { o.innerHTML = "No amounts recognised \u2014 each line should start with the quantity (e.g. \u201c2 1/2 cups flour\u201d)."; return; }
  o.value = out.join("\n");
  var meta = $("rc2-meta");
  if (meta) meta.innerHTML = "<span class='jf-chip'><b>" + nfmt(k, 4) + "\u00d7</b>scale factor</span>" +
    "<span class='jf-chip'><b>" + changed + "</b>quantities rescaled</span>";
}

/* --- dl2: dilution solver --- */
function dl2() {
  var o = $("dl2-out");
  var c1 = m7Num("dl2-c1"), v1 = m7Num("dl2-v1"), c2 = m7Num("dl2-c2"), v2 = m7Num("dl2-v2");
  var solve = String($("dl2-s").value || "v2");
  if (solve === "v1") {
    if (c1 === null || c1 <= 0 || c2 === null || c2 <= 0 || v2 === null || v2 <= 0) { o.innerHTML = "Fill C\u2081, C\u2082 and V\u2082 with positive numbers to solve for V\u2081."; return; }
    var r1 = c2 * v2 / c1;
    o.innerHTML = "<b>" + nfmt(r1, 4) + "</b> V\u2081 (volume of stock needed)" +
      "<span class='jf-chip'><b>" + nfmt(v2 - r1, 4) + "</b>solvent to add</span>" +
      "<span class='jf-chip'><b>" + nfmt(v2 / r1, 2) + "\u00d7</b>dilution factor</span>";
    return;
  }
  if (solve === "v2") {
    if (c1 === null || c1 <= 0 || c2 === null || c2 <= 0 || v1 === null || v1 <= 0) { o.innerHTML = "Fill C\u2081, C\u2082 and V\u2081 with positive numbers to solve for V\u2082."; return; }
    var r2 = c1 * v1 / c2;
    o.innerHTML = "<b>" + nfmt(r2, 4) + "</b> V\u2082 (final volume)" +
      "<span class='jf-chip'><b>" + nfmt(r2 - v1, 4) + "</b>solvent to add</span>" +
      "<span class='jf-chip'><b>" + nfmt(r2 / v1, 2) + "\u00d7</b>dilution factor</span>";
    return;
  }
  if (solve === "c1") {
    if (c2 === null || c2 <= 0 || v1 === null || v1 <= 0 || v2 === null || v2 <= 0) { o.innerHTML = "Fill C\u2082, V\u2081 and V\u2082 with positive numbers to solve for C\u2081."; return; }
    o.innerHTML = "<b>" + nfmt(c2 * v2 / v1, 4) + "</b> C\u2081 (stock concentration needed)" +
      "<span class='jf-chip'><b>" + nfmt(v2 / v1, 2) + "\u00d7</b>dilution factor</span>";
    return;
  }
  if (c1 === null || c1 <= 0 || v1 === null || v1 <= 0 || v2 === null || v2 <= 0) { o.innerHTML = "Fill C\u2081, V\u2081 and V\u2082 with positive numbers to solve for C\u2082."; return; }
  o.innerHTML = "<b>" + nfmt(c1 * v1 / v2, 4) + "</b> C\u2082 (resulting concentration)" +
    "<span class='jf-chip'><b>" + nfmt(v2 / v1, 2) + "\u00d7</b>dilution factor</span>";
}

/* wire the batch-21 engines into the shared M3 finisher */
["cm2", "mg2", "an2", "fe2", "fl2", "rd2", "rc2", "dl2"].forEach(function (fn) {
  var orig = null;
  try { orig = window[fn] || eval(fn); } catch (e) { orig = null; }
  if (typeof orig !== "function") return;
  window[fn] = function () { orig(); m3After(); };
});
/* ---------- M8: batch 22 new tools (th2, ss2, ab2, pv2, pt2, bt2, st2, vd2) ---------- */

/* --- th2: take-home pay --- */
function th2() {
  var o = $("th2-out");
  var g = m7Num("th2-g"), p = m7Num("th2-p"), t = m7Num("th2-t");
  if (g === null || g < 0 || p === null || t === null || p < 0 || t < 0) {
    o.innerHTML = "Enter non-negative gross pay, deduction percent and tax rate."; return;
  }
  var pre = g * p / 100, taxable = Math.max(0, g - pre), tax = taxable * t / 100, net = g - tax - pre;
  o.innerHTML = "<b>" + m7Money(net) + "</b> take-home per year" +
    "<span class='jf-chip'><b>" + m7Money(net / 12) + "</b>per month</span>" +
    "<span class='jf-chip'><b>" + m7Money(net / 52) + "</b>per week</span>" +
    "<span class='jf-chip'><b>" + m7Money(pre) + "</b>pre-tax deductions</span>" +
    "<span class='jf-chip'><b>" + m7Money(tax) + "</b>tax on " + m7Money(taxable) + " of taxable pay</span>" +
    (g > 0 ? "<span class='jf-chip'><b>" + ((g - net) / g * 100).toFixed(1) + "%</b>effective total deduction</span>" : "");
}

/* --- ss2: sample size --- */
function ss2() {
  var o = $("ss2-out"), meta = $("ss2-meta");
  var p = m7Num("ss2-p"), m = m7Num("ss2-m"), v = m7Num("ss2-v");
  if (p === null || p <= 0 || p >= 100 || m === null || m <= 0 || m >= 100) {
    o.innerHTML = "Enter a baseline rate and a minimum detectable lift, both strictly between 0 and 100."; return;
  }
  var pp = p / 100, d = pp * m / 100;
  var n = 7.84 * 2 * pp * (1 - pp) / (d * d);
  n = Math.ceil(n / 10) * 10;
  o.innerHTML = "<b>" + nfmt(n, 0) + "</b> visitors needed per variant" +
    "<span class='jf-chip'><b>" + nfmt(n * 2, 0) + "</b>total across both variants</span>" +
    "<span class='jf-chip'><b>" + nfmt(p * m / 100, 2) + "%</b>absolute change being detected</span>";
  if (v !== null && v > 0) {
    var days = (n * 2) / v;
    meta.innerHTML = "<span class='jf-chip'><b>" + days.toFixed(1) + " days</b>to run at " + nfmt(v, 0) + " visitors/day</span>";
  }
}

/* --- ab2: split-test significance --- */
function ab2Phi(z) {
  var t = 1 / (1 + 0.2316419 * Math.abs(z));
  var d = 0.3989423 * Math.exp(-z * z / 2);
  var p = d * t * (0.319381530 + t * (-0.356563782 + t * (1.781477937 + t * (-1.821255978 + t * 1.330274429))));
  return z >= 0 ? 1 - p : p;
}
function ab2() {
  var o = $("ab2-out");
  var va = m7Num("ab2-va"), ca = m7Num("ab2-ca"), vb = m7Num("ab2-vb"), cb = m7Num("ab2-cb");
  if (va === null || va <= 0 || vb === null || vb <= 0 || ca === null || ca < 0 || cb === null || cb < 0 || ca > va || cb > vb) {
    o.innerHTML = "Enter visitor counts (positive) and conversions between 0 and the visitor count."; return;
  }
  var pa = ca / va, pb = cb / vb;
  var pooled = (ca + cb) / (va + vb);
  var se = Math.sqrt(pooled * (1 - pooled) * (1 / va + 1 / vb));
  var z = se > 0 ? (pb - pa) / se : 0;
  var pv = 2 * (1 - ab2Phi(Math.abs(z)));
  var sig = pv < 0.05;
  var lift = pa > 0 ? (pb - pa) / pa * 100 : null;
  o.innerHTML = "<b>" + (sig ? "SIGNIFICANT" : "not conclusive") + "</b> at the 95% confidence level" +
    "<span class='jf-chip'><b>" + (pa * 100).toFixed(2) + "% \u2192 " + (pb * 100).toFixed(2) + "%</b>conversion rate A \u2192 B</span>" +
    "<span class='jf-chip'><b>" + z.toFixed(2) + "</b>z-score</span>" +
    "<span class='jf-chip'><b>" + (pv * 100).toFixed(1) + "%</b>p-value (" + (sig ? "under" : "over") + " 5%)</span>" +
    (lift !== null ? "<span class='jf-chip'><b>" + (lift >= 0 ? "+" : "") + (lift >= 0 ? lift.toFixed(1) : lift.toFixed(1)) + "%</b>relative lift for B</span>" : "") +
    "<span class='jf-chip'><b>" + (sig ? "ship it" : "keep testing") + "</b>verdict</span>";
}

/* --- pv2: pond volume --- */
function pv2() {
  var o = $("pv2-out");
  var l = m7Num("pv2-l"), w = m7Num("pv2-w"), d = m7Num("pv2-d");
  var shape = String($("pv2-s").value || "rect");
  if (l === null || l <= 0 || d === null || d <= 0) { o.innerHTML = "Enter a positive length (or diameter) and depth in feet."; return; }
  var cuft;
  if (shape === "circ") {
    cuft = Math.PI * (l / 2) * (l / 2) * d;
  } else {
    if (w === null || w <= 0) { o.innerHTML = "Enter a positive width for a rectangular pond."; return; }
    cuft = l * w * d;
  }
  var gal = cuft * 7.48052, lit = cuft * 28.3168;
  o.innerHTML = "<b>" + nfmt(lit, 0) + " L</b>(" + nfmt(gal, 0) + " US gal)" +
    "<span class='jf-chip'><b>" + nfmt(cuft, 1) + " ft\u00b3</b>cubic feet of water</span>" +
    "<span class='jf-chip'><b>" + nfmt(lit / 1000, 2) + " m\u00b3</b>cubic metres</span>" +
    "<span class='jf-chip'><b>" + nfmt(shape === "circ" ? Math.PI * (l / 2) * (l / 2) : l * w, 1) + " ft\u00b2</b>surface area</span>" +
    "<span class='jf-chip'><b>" + nfmt(lit / 4000, 2) + " h</b>pump hours for one full turnover at 4,000 L/h</span>";
}

/* --- pt2: paint coverage --- */
function pt2() {
  var o = $("pt2-out");
  var l = m7Num("pt2-l"), w = m7Num("pt2-w"), h = m7Num("pt2-h");
  var dd = m7Num("pt2-d"), nn = m7Num("pt2-n"), c = m7Num("pt2-c");
  if (l === null || l <= 0 || w === null || w <= 0 || h === null || h <= 0) {
    o.innerHTML = "Enter positive room length, width and wall height in metres."; return;
  }
  if (dd === null || dd < 0) dd = 0;
  if (nn === null || nn < 0) nn = 0;
  if (c === null || c < 1) c = 1;
  var walls = 2 * (l + w) * h - dd * 1.8 - nn * 1.2;
  if (walls <= 0) { o.innerHTML = "Doors and windows are larger than the walls \u2014 check the dimensions."; return; }
  var litres = walls * c / 10;
  var cans = Math.ceil(litres / 4);
  o.innerHTML = "<b>" + nfmt(litres, 2) + " L</b>of paint for " + c + (c === 1 ? " coat" : " coats") +
    "<span class='jf-chip'><b>" + nfmt(walls, 1) + " m\u00b2</b>paintable wall area (openings removed)</span>" +
    "<span class='jf-chip'><b>" + cans + "</b>4 L cans to buy (rounded up)</span>" +
    "<span class='jf-chip'><b>" + nfmt(litres / cans, 2) + " L</b>leftover from the last can" + "</span>";
}

/* --- bt2: BTU calculator --- */
function bt2() {
  var o = $("bt2-out");
  var l = m7Num("bt2-l"), w = m7Num("bt2-w"), np = m7Num("bt2-n");
  var s = String($("bt2-s").value || "avg"), k = String($("bt2-k").value || "no");
  if (l === null || l <= 0 || w === null || w <= 0) { o.innerHTML = "Enter positive room length and width in metres."; return; }
  var sqft = l * w * 10.7639;
  var btu = sqft * 20;
  if (s === "sunny") btu *= 1.1;
  if (s === "shade") btu *= 0.9;
  if (np !== null && np > 2) btu += (np - 2) * 600;
  if (k === "yes") btu += 4000;
  o.innerHTML = "<b>" + nfmt(Math.round(btu), 0) + " BTU/h</b>air conditioner size for this room" +
    "<span class='jf-chip'><b>" + (btu / 3412.14).toFixed(2) + " kW</b>metric equivalent</span>" +
    "<span class='jf-chip'><b>" + nfmt(l * w, 1) + " m\u00b2</b>floor area (" + nfmt(sqft, 0) + " ft\u00b2)</span>" +
    "<span class='jf-chip'><b>" + nfmt(Math.round(btu) * 0.75, 0) + "</b>BTU if mostly heating instead of cooling</span>";
}

/* --- st2: screen time --- */
function st2() {
  var o = $("st2-out");
  var p = m7Num("st2-p"), c = m7Num("st2-c"), t = m7Num("st2-t"), g = m7Num("st2-g"), a = m7Num("st2-a");
  if (p === null && c === null && t === null && g === null) { o.innerHTML = "Enter at least one screen's daily hours."; return; }
  var day = (p || 0) + (c || 0) + (t || 0) + (g || 0);
  var yr = day * 365;
  o.innerHTML = "<b>" + nfmt(day, 1) + " h</b>of screens per typical day" +
    "<span class='jf-chip'><b>" + nfmt(day * 7, 1) + " h</b>per week</span>" +
    "<span class='jf-chip'><b>" + nfmt(yr, 0) + " h</b>per year</span>" +
    "<span class='jf-chip'><b>" + nfmt(yr / 24, 1) + " full days</b>the annual hours as 24-hour days</span>" +
    (a !== null && a > 0 && a < 80 ? "<span class='jf-chip'><b>" + nfmt(day * 365 * (80 - a) / 24 / 365, 1) + " years</b>waking years at this pace until age 80</span>" : "");
}

/* --- vd2: voltage drop --- */
var VD2_CM = { "14": 4110, "12": 6530, "10": 10380, "8": 16510, "6": 26240, "4": 41740, "2": 66360, "0": 105600, "00": 133100, "000": 167800, "0000": 211600 };
function vd2() {
  var o = $("vd2-out");
  var i = m7Num("vd2-i"), l = m7Num("vd2-l");
  var g = String($("vd2-g").value || "14"), m = String($("vd2-m").value || "cu"), v = m7Num("vd2-v");
  if (i === null || i <= 0 || l === null || l <= 0 || v === null || v <= 0) { o.innerHTML = "Enter positive current, distance and system voltage."; return; }
  var K = m === "al" ? 21.2 : 12.9;
  var cm = VD2_CM[g] || 4110;
  var vd = 2 * K * i * l / cm;
  var pct = vd / v * 100;
  var verdict = pct <= 3 ? "good \u2014 under 3%" : pct <= 5 ? "borderline \u2014 over 3%" : "too much \u2014 over 5%, go bigger wire or shorter run";
  o.innerHTML = "<b>" + vd.toFixed(2) + " V</b>dropped across the run" +
    "<span class='jf-chip'><b>" + (v - vd).toFixed(2) + " V</b>arrives at the load</span>" +
    "<span class='jf-chip'><b>" + pct.toFixed(2) + "%</b>of supply voltage lost</span>" +
    "<span class='jf-chip" + (pct > 3 ? " jf-chip-bad" : "") + "><b>" + (pct <= 3 ? "pass" : "flag") + "</b>" + verdict + "</span>" +
    "<span class='jf-chip'><b>" + nfmt(cm, 0) + " CM</b>circular mils of " + (m === "al" ? "aluminium" : "copper") + " conductor</span>";
}

/* wire the batch-22 engines into the shared M3 finisher */
["th2", "ss2", "ab2", "pv2", "pt2", "bt2", "st2", "vd2"].forEach(function (fn) {
  var orig = null;
  try { orig = window[fn] || eval(fn); } catch (e) { orig = null; }
  if (typeof orig !== "function") return;
  window[fn] = function () { orig(); m3After(); };
});
/* ---------- M9: batch 23 new tools (kc2, sg2, sb2, ov2, be2, sf3, kb2, sa2) ---------- */

/* --- kc2: calories burned (MET) --- */
function kc2() {
  var o = $("kc2-out");
  var met = +String($("kc2-a").value || "3.5"), w = m7Num("kc2-w"), m = m7Num("kc2-m");
  if (w === null || w <= 0 || m === null || m <= 0) { o.innerHTML = "Enter a positive body weight and duration."; return; }
  var kcal = met * 3.5 * w / 200 * m;
  var perMin = kcal / m;
  o.innerHTML = "<b>" + kcal.toFixed(1) + " kcal</b>burned in " + nfmt(m, 0) + " minutes" +
    "<span class='jf-chip'><b>" + perMin.toFixed(1) + "</b>kcal per minute</span>" +
    "<span class='jf-chip'><b>" + nfmt(perMin * 60, 0) + "</b>kcal if kept up a full hour</span>" +
    "<span class='jf-chip'><b>" + nfmt(met, 1) + " MET</b>activity intensity from the compendium table</span>" +
    "<span class='jf-chip'><b>" + nfmt(kcal / 7.7, 0) + " g</b>carbohydrate-equivalent refuel</span>";
}

/* --- sg2: slope grade --- */
function sg2() {
  var o = $("sg2-out");
  var r = m7Num("sg2-r"), rn = m7Num("sg2-n"), gIn = m7Num("sg2-g");
  if (r === null && gIn === null) { o.innerHTML = "Enter a rise and run, or leave rise blank and enter a grade to reverse-solve."; return; }
  if (gIn !== null) {
    if (rn === null || rn <= 0) { o.innerHTML = "Enter the run to reverse-solve the rise from a grade."; return; }
    r = rn * gIn / 100;
    o.innerHTML = "<b>" + nfmt(r, 4) + "</b> rise over a run of " + nfmt(rn, 2) +
      "<span class='jf-chip'><b>" + gIn + "%</b>the grade you entered</span>";
    return;
  }
  if (rn === null || rn <= 0) { o.innerHTML = "The run must be a positive number."; return; }
  var pct = r / rn * 100, deg = Math.atan(r / rn) * 180 / Math.PI, ratio = rn / Math.abs(r || 1e-9);
  o.innerHTML = "<b>" + pct.toFixed(2) + "%</b> grade" +
    "<span class='jf-chip'><b>" + deg.toFixed(2) + "\u00b0</b>angle from horizontal</span>" +
    "<span class='jf-chip'><b>1 : " + nfmt(ratio, 1) + "</b>rise-in-run ratio</span>" +
    (pct > 0 && pct <= 8.33 ? "<span class='jf-chip'><b>pass</b>within the 1 : 12 accessible-ramp limit</span>" : "<span class='jf-chip jf-chip-bad'><b>steep</b>exceeds the 1 : 12 accessible-ramp limit</span>");
}

/* --- sb2: split bill --- */
function sb2() {
  var o = $("sb2-out");
  var b = m7Num("sb2-b"), t = m7Num("sb2-t"), p = m7Num("sb2-p");
  if (b === null || b < 0 || t === null || t < 0 || p === null || p < 1) {
    o.innerHTML = "Enter a non-negative bill and tip, and at least one person."; return;
  }
  var tip = b * t / 100, total = b + tip, per = total / p;
  var ceilShare = Math.ceil(per * 100) / 100;
  o.innerHTML = "<b>" + m7Money(per) + "</b>per person" +
    "<span class='jf-chip'><b>" + m7Money(tip) + "</b>tip money (" + t + "%)</span>" +
    "<span class='jf-chip'><b>" + m7Money(total) + "</b>grand total with tip</span>" +
    (per !== ceilShare ? "<span class='jf-chip'><b>" + m7Money(ceilShare) + "</b>if each rounds up (" + m7Money(ceilShare * p - total) + " overage)</span>" : "<span class='jf-chip'><b>even</b>splits to the cent, nothing to round</span>");
}

/* --- ov2: overtime pay, tiered --- */
function ov2() {
  var o = $("ov2-out");
  var r = m7Num("ov2-r"), h = m7Num("ov2-h"), t = m7Num("ov2-t"), x = m7Num("ov2-x");
  if (r === null || r < 0 || h === null || h < 0 || t === null || t < 0) { o.innerHTML = "Enter a non-negative rate, hours and overtime threshold."; return; }
  if (x === null || x <= t) x = Math.max(t + 10, 60);
  var regH = Math.min(h, t);
  var ot1H = Math.max(0, Math.min(h, x) - t);
  var ot2H = Math.max(0, h - x);
  var reg = r * regH, ot1 = r * 1.5 * ot1H, ot2 = r * 2 * ot2H;
  o.innerHTML = "<b>" + m7Money(reg + ot1 + ot2) + "</b> gross for the week" +
    "<span class='jf-chip'><b>" + m7Money(reg) + "</b>regular pay (" + regH + " h)</span>" +
    "<span class='jf-chip'><b>" + m7Money(ot1) + "</b>time-and-a-half (" + ot1H + " h \u00d7 1.5)</span>" +
    "<span class='jf-chip'><b>" + m7Money(ot2) + "</b>double time (" + ot2H + " h \u00d7 2)</span>" +
    "<span class='jf-chip'><b>" + m7Money((reg + ot1 + ot2) / h) + "</b>blended effective rate per hour</span>";
}

/* --- be2: break-even --- */
function be2() {
  var o = $("be2-out");
  var f = m7Num("be2-f"), p = m7Num("be2-p"), v = m7Num("be2-v"), mo = m7Num("be2-m");
  if (f === null || f < 0 || p === null || p < 0 || v === null || v < 0) { o.innerHTML = "Enter non-negative costs and price."; return; }
  var margin = p - v;
  if (margin <= 0) { o.innerHTML = "Price is at or below variable cost \u2014 no volume can break even. Raise the price or cut unit cost first."; return; }
  var units = f / margin;
  o.innerHTML = "<b>" + nfmt(units, 0) + " units</b>to break even" +
    "<span class='jf-chip'><b>" + m7Money(units * p) + "</b>revenue at break-even</span>" +
    "<span class='jf-chip'><b>" + m7Money(margin) + "</b>margin each sale contributes</span>" +
    (mo !== null && mo > 0 ? "<span class='jf-chip'><b>" + nfmt(units / mo, 1) + " months</b>at " + nfmt(mo, 0) + " sales a month</span>" : "") +
    (f === 0 ? "<span class='jf-chip'><b>0</b>no fixed costs \u2014 profitable from unit one</span>" : "");
}

/* --- sf3: square footage --- */
function sf3() {
  var o = $("sf3-out");
  var l = m7Num("sf3-l"), w = m7Num("sf3-w"), c = m7Num("sf3-c"), x = m7Num("sf3-x");
  if (l === null || l <= 0 || w === null || w <= 0) { o.innerHTML = "Enter positive length and width in feet."; return; }
  var area = l * w;
  var parts = "<b>" + nfmt(area, 1) + " ft\u00b2</b>(" + nfmt(area * 0.092903, 1) + " m\u00b2)";
  if (c !== null && c >= 0) {
    if (x === null || x < 0) x = 0;
    var cost = area * c * (1 + x / 100);
    parts += "<span class='jf-chip'><b>" + m7Money(area * c) + "</b>cost at " + m7Money(c) + " per ft\u00b2</span>" +
      (x > 0 ? "<span class='jf-chip'><b>" + m7Money(cost) + "</b>with " + x + "% waste added</span>" : "");
  }
  o.innerHTML = parts;
}

/* --- kb2: keyboard test --- */
var KB2_SEEN = {}, KB2_COUNT = 0;
function kb2Key(e) {
  var k = e.key, code = e.code, kc = e.keyCode;
  var live = $("kb2-live");
  var label = k;
  if (e.ctrlKey && k !== "Control") label = "Ctrl + " + label;
  if (e.altKey && k !== "Alt") label = "Alt + " + label;
  if (e.shiftKey && k.length > 1 && k !== "Shift") label = "Shift + " + label;
  live.innerHTML = "<b>" + (label.length > 1 ? label : label.toUpperCase()) + "</b>" +
    "<span class='jf-chip'><b>" + code + "</b>event.code</span>" +
    "<span class='jf-chip'><b>" + kc + "</b>keyCode</span>" +
    "<span class='jf-chip'><b>" + (e.repeat ? "yes" : "no") + "</b>auto-repeat</span>";
  if (!KB2_SEEN[code || k]) { KB2_SEEN[code || k] = 1; KB2_COUNT++; }
  var meta = $("kb2-meta");
  if (meta) meta.innerHTML = "<span class='jf-chip'><b>" + KB2_COUNT + "</b>distinct keys detected so far</span>";
  var log = $("kb2-log");
  if (log) log.innerHTML = k + (kc ? "  (" + kc + ")" : "") + "\n" + log.innerHTML;
}
document.addEventListener("keydown", kb2Key);

/* --- sa2: secret santa --- */
function sa2() {
  var o = $("sa2-out"), meta = $("sa2-meta");
  var names = String($("sa2-in").value || "").split("\n").map(function (s) { return s.trim(); }).filter(Boolean);
  var uniq = {};
  for (var i = 0; i < names.length; i++) {
    var key = names[i].toLowerCase();
    if (uniq[key]) { o.innerHTML = "Duplicate name: \u201c" + names[i] + "\u201d \u2014 each person must appear once."; return; }
    uniq[key] = 1;
  }
  if (names.length < 3) { o.innerHTML = "Enter at least three names, one per line."; return; }
  var n = names.length, buf = new Uint32Array(n);
  (window.crypto || globalThis.crypto).getRandomValues(buf);
  for (var j = n - 1; j > 0; j--) {
    var k2 = buf[j] % (j + 1), tmp = names[j]; names[j] = names[k2]; names[k2] = tmp;
  }
  var lines = [];
  for (var g = 0; g < n; g++) lines.push(names[g] + " \u2192 " + names[(g + 1) % n]);
  o.innerHTML = lines.join("<br>");
  if (meta) meta.innerHTML = "<span class='jf-chip'><b>" + n + "</b>participants</span>" +
    "<span class='jf-chip'><b>" + n + "</b>gifts given, one each</span>" +
    "<span class='jf-chip'><b>crypto</b>shuffle source (no self-draws possible)</span>";
}

/* wire the batch-23 engines into the shared M3 finisher */
["kc2", "sg2", "sb2", "ov2", "be2", "sf3", "kb2", "sa2"].forEach(function (fn) {
  var orig = null;
  try { orig = window[fn] || eval(fn); } catch (e) { orig = null; }
  if (typeof orig !== "function") return;
  window[fn] = function () { orig(); m3After(); };
});
/* ---------- M10: batch 24 new tools (tc2, ip2, bf2, rg2, ce2, pa2, ba2, hr2) ---------- */

/* --- tc2: time card --- */
function tc2() {
  var o = $("tc2-out");
  var r = m7Num("tc2-r"), t = m7Num("tc2-t"), total = 0, i, v;
  for (i = 1; i <= 5; i++) { v = m7Num("tc2-d" + i); total += v === null ? 0 : Math.max(0, v); }
  if (t === null || t < 0) t = 40;
  if (r === null || r < 0) { o.innerHTML = "Enter your hourly rate."; return; }
  var regH = Math.min(total, t), otH = Math.max(0, total - t);
  var pay = r * regH + 1.5 * r * otH;
  o.innerHTML = "<b>" + m7Money(pay) + "</b>for a " + nfmt(total, 1) + "-hour week" +
    "<span class='jf-chip'><b>" + nfmt(regH, 1) + " h</b>regular hours</span>" +
    (otH > 0 ? "<span class='jf-chip'><b>" + nfmt(otH, 1) + " h</b>overtime (paid 1.5\u00d7)</span>" : "<span class='jf-chip'><b>0 h</b>no overtime this week</span>") +
    "<span class='jf-chip'><b>" + m7Money(pay * 2) + "</b>if next week repeats (fortnight)</span>" +
    "<span class='jf-chip'><b>" + m7Money(pay * 13) + "</b>a full quarter at this pace</span>" +
    (total === 0 ? "<span class='jf-chip jf-chip-bad'><b>empty</b>no hours entered</span>" : "");
}

/* --- ip2: subnet calculator --- */
function ip2Fmt(i32) {
  return ((i32 >>> 24) & 255) + "." + ((i32 >>> 16) & 255) + "." + ((i32 >>> 8) & 255) + "." + (i32 & 255);
}
function ip2() {
  var o = $("ip2-out");
  var s = String($("ip2-in").value || "").trim();
  var m = s.match(/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})(?:\s*\/\s*(\d{1,2}))?$/);
  if (!m) { o.innerHTML = "Enter an IPv4 address with an optional /prefix \u2014 for example 192.168.10.5/26."; return; }
  var a = [+m[1], +m[2], +m[3], +m[4]], pfx = m[5] === undefined ? 24 : +m[5];
  if (a[0] > 255 || a[1] > 255 || a[2] > 255 || a[3] > 255) { o.innerHTML = "Each octet must be 0\u2013255 \u2014 " + s + " is not an IPv4 address."; return; }
  if (pfx < 0 || pfx > 32) { o.innerHTML = "The CIDR prefix must be 0\u201332."; return; }
  var ip = ((a[0] << 24) | (a[1] << 16) | (a[2] << 8) | a[3]) >>> 0;
  var mask = pfx === 0 ? 0 : (0xFFFFFFFF << (32 - pfx)) >>> 0;
  var wild = (~mask) >>> 0;
  var net = (ip & mask) >>> 0, bcast = (net | wild) >>> 0;
  var hosts = pfx >= 31 ? (pfx === 32 ? 1 : 2) : Math.pow(2, 32 - pfx) - 2;
  var bits = "";
  for (var i = 0; i < 32; i++) bits += (i < pfx ? "1" : "0");
  var priv = (a[0] === 10 || (a[0] === 172 && a[1] >= 16 && a[1] <= 31) || (a[0] === 192 && a[1] === 168) || a[0] === 127 || (a[0] === 169 && a[1] === 254));
  var rng = pfx >= 31 ? "n/a (\u00d731+) \u2014 usable range collapses on /31 and /32" : ip2Fmt(net + 1) + " \u2192 " + ip2Fmt(bcast - 1);
  o.innerHTML = "<b>" + ip2Fmt(net) + "/" + pfx + "</b>network" +
    "<span class='jf-chip'><b>" + ip2Fmt(mask) + "</b>subnet mask</span>" +
    "<span class='jf-chip'><b>" + ip2Fmt(wild) + "</b>wildcard</span>" +
    "<span class='jf-chip'><b>" + ip2Fmt(bcast) + "</b>broadcast</span>" +
    "<span class='jf-chip'><b>" + nfmt(hosts, 0) + "</b>usable hosts</span>" +
    "<span class='jf-chip'><b>" + rng + "</b>usable range</span>" +
    (priv ? "<span class='jf-chip'><b>private</b>" + s.split("/")[0] + " is not routable on the public internet</span>" : "<span class='jf-chip'><b>public</b>routable address space</span>") +
    "<span class='jf-chip' style='font-family:monospace'><b style='font-size:9px'>" + bits + "</b>" + pfx + " mask bits</span>";
}

/* --- bf2: board feet --- */
function bf2() {
  var o = $("bf2-out");
  var q = m7Num("bf2-q"), t = m7Num("bf2-t"), w = m7Num("bf2-w"), l = m7Num("bf2-l"), c = m7Num("bf2-c");
  if (q === null || q < 1 || t === null || t <= 0 || w === null || w <= 0 || l === null || l <= 0) {
    o.innerHTML = "Enter a piece count of 1+ and positive thickness, width and length."; return;
  }
  var per = t * w * l / 12, total = per * q;
  var parts = "<b>" + nfmt(total, 2) + " BF</b>(" + nfmt(q, 0) + " pieces \u00d7 " + nfmt(per, 2) + " each)" +
    "<span class='jf-chip'><b>" + nfmt(total * 0.00236, 3) + " m\u00b3</b>cubic metres mills quote</span>" +
    "<span class='jf-chip'><b>" + nfmt(l * 12 * w * t * q / 1728, 2) + " ft\u00b3</b>solid cubic feet</span>";
  if (c !== null && c >= 0) parts += "<span class='jf-chip'><b>" + m7Money(total * c) + "</b>order cost at " + m7Money(c) + " per BF</span>";
  o.innerHTML = parts;
}

/* --- rg2: ring size --- */
function rg2() {
  var o = $("rg2-out");
  var d = m7Num("rg2-d"), u = m7Num("rg2-u");
  if (u !== null && u > 0) d = 11.63 + 0.8128 * u;
  if (d === null || d <= 0) { o.innerHTML = "Enter a positive inside diameter in mm, or a US ring size."; return; }
  var us = (d - 11.63) / 0.8128, circ = Math.PI * d;
  var uk = Math.round((us - 1) * 2) / 2 + 0.5;
  o.innerHTML = "<b>" + nfmt(us, 1) + " US</b>ring size" +
    "<span class='jf-chip'><b>" + nfmt(uk, 1) + " UK (approx)</b>British sizing runs half below US</span>" +
    "<span class='jf-chip'><b>" + nfmt(circ, 1) + " mm</b>inside circumference \u2014 the EU/French scale</span>" +
    "<span class='jf-chip'><b>" + nfmt(d, 2) + " mm</b>inside diameter</span>" +
    (us < 3.5 || us > 14 ? "<span class='jf-chip jf-chip-bad'><b>unusual</b>outside the standard 4\u201313 ring range \u2014 double-check the measurement</span>" : "");
}

/* --- ce2: caesar cipher --- */
function ce2Shift(text, k) {
  var out = "", i, ch, code;
  for (i = 0; i < text.length; i++) {
    ch = text[i];
    code = text.charCodeAt(i);
    if (code >= 65 && code <= 90) ch = String.fromCharCode((code - 65 + k + 26) % 26 + 65);
    else if (code >= 97 && code <= 122) ch = String.fromCharCode((code - 97 + k + 26) % 26 + 97);
    out += ch;
  }
  return out;
}
function ce2() {
  var o = $("ce2-out");
  var t = String($("ce2-in").value || ""), k = m7Num("ce2-s");
  var dir = String($("ce2-d").value || "enc");
  if (!t.trim()) { o.innerHTML = "Type the text to shift \u2014 punctuation and digits pass through unchanged."; return; }
  if (k === null || k < 1 || k > 25) { o.innerHTML = "The shift must be between 1 and 25."; return; }
  var res = ce2Shift(t, dir === "enc" ? k : -k);
  o.innerHTML = "<b style='font-family:monospace'>" + res.replace(/</g, "&lt;") + "</b>" +
    "<span class='jf-chip'><b>" + (dir === "enc" ? "+" : "\u2212") + k + "</b>shift applied, case preserved</span>" +
    "<span class='jf-chip'><b>" + t.replace(/</g, "&lt;").length + "</b>characters in</span>";
}
function ce2Brute() {
  var o = $("ce2-out");
  var t = String($("ce2-in").value || "").trim();
  if (!t) { o.innerHTML = "Type the message first, then tap brute force."; return; }
  var lines = [];
  for (var k = 1; k <= 25; k++) lines.push("shift " + String(k).padStart(2, " ") + ": " + ce2Shift(t, -k));
  o.innerHTML = "<b>All 25 decodings of \u201c" + t.replace(/</g, "&lt;") + "\u201d</b><br>" +
    lines.map(function (l) { return l.replace(/</g, "&lt;"); }).join("<br>");
}

/* --- pa2: palindrome checker --- */
function pa2() {
  var o = $("pa2-out");
  var t = String($("pa2-in").value || "").trim();
  if (!t) { o.innerHTML = "Paste a word, phrase or sentence \u2014 punctuation and case are stripped automatically."; return; }
  var clean = t.toLowerCase().replace(/[^a-z0-9]/g, "");
  if (!clean) { o.innerHTML = "No letters or numbers left after cleaning \u2014 is this text just punctuation?"; return; }
  var rev = clean.split("").reverse().join("");
  var isPal = clean === rev;
  o.innerHTML = "<b>" + (isPal ? "PALINDROME" : "not a palindrome") + "</b>" +
    "<span class='jf-chip'><b>" + clean + "</b>after cleaning (this is what was compared)</span>" +
    "<span class='jf-chip'><b>" + clean.length + "</b>characters compared</span>" +
    (isPal ? "<span class='jf-chip'><b>" + Math.floor(clean.length / 2) + "</b>mismatches allowed: zero in both directions</span>" : "<span class='jf-chip jf-chip-bad'><b>differs</b>from at least one reversed character</span>");
}

/* --- ba2: BAC (Widmark) --- */
function ba2() {
  var o = $("ba2-out");
  var d = m7Num("ba2-d"), w = m7Num("ba2-w"), h = m7Num("ba2-h");
  var sex = String($("ba2-s").value || "m");
  if (d === null || d < 0 || w === null || w <= 0 || h === null || h < 0) {
    o.innerHTML = "Enter non-negative drinks and hours, and a positive weight."; return;
  }
  var r = sex === "f" ? 0.55 : 0.68;
  var grams = d * 14;
  var bac = Math.max(0, grams / (w * 1000 * r) * 100 - 0.015 * h);
  var verdict = bac >= 0.08 ? "over the US 0.08 limit" : bac >= 0.05 ? "over many 0.05 limits" : "below 0.05";
  var toZero = bac / 0.015;
  o.innerHTML = "<b>" + bac.toFixed(3) + "%</b>estimated BAC (Widmark)" +
    "<span class='jf-chip" + (bac >= 0.05 ? " jf-chip-bad" : "") + "><b>" + verdict + "</b>driving is not safe or legal at or over the limit</span>" +
    "<span class='jf-chip'><b>" + nfmt(toZero, 1) + " h</b>elimination time to reach 0.000 at \u22120.015/h</span>" +
    "<span class='jf-chip'><b>" + nfmt(grams, 0) + " g</b>alcohol consumed (" + nfmt(d, 1) + " standard drinks \u00d7 14 g)</span>" +
    "<span class='jf-chip'><b>r = " + r + "</b>body-water factor used</span>";
}

/* --- hr2: heart rate zones --- */
function hr2() {
  var o = $("hr2-out");
  var a = m7Num("hr2-a"), r = m7Num("hr2-r");
  if (a === null || a < 10 || a > 100 || r === null || r < 30 || r > 120) {
    o.innerHTML = "Enter a realistic age (10\u2013100) and resting heart rate (30\u2013120 bpm)."; return;
  }
  var max = 220 - a, reserve = max - r;
  var Z = [[50, 60, "Z1", "recovery"], [60, 70, "Z2", "easy / fat-burn"], [70, 80, "Z3", "aerobic tempo"], [80, 90, "Z4", "threshold"], [90, 100, "Z5", "VO2 max"]];
  var rows = "";
  for (var i = 0; i < Z.length; i++) {
    rows += "<span class='jf-chip'><b>" + Z[i][2] + " " + Math.round(reserve * Z[i][0] / 100 + r) + "\u2013" + Math.round(reserve * Z[i][1] / 100 + r) +
      " bpm</b>" + Z[i][3] + " (" + Z[i][0] + "\u2013" + Z[i][1] + "%)</span>";
  }
  o.innerHTML = "<b>" + max + " bpm</b>estimated maximum (220 \u2212 age)" +
    "<span class='jf-chip'><b>" + reserve + " bpm</b>heart-rate reserve (max \u2212 resting)</span>" + rows;
}

/* wire the batch-24 engines into the shared M3 finisher */
["tc2", "ip2", "bf2", "rg2", "ce2", "pa2", "ba2", "hr2"].forEach(function (fn) {
  var orig = null;
  try { orig = window[fn] || eval(fn); } catch (e) { orig = null; }
  if (typeof orig !== "function") return;
  window[fn] = function () { orig(); m3After(); };
});
/* ---------- M11: batch 25 new tools (sh3, tv2, ck2, cq2, mr2, sp3, to2, sa3) ---------- */

/* --- sh3: shoe size --- */
function sh3() {
  var o = $("sh3-out");
  var cm = m7Num("sh3-c"), u = m7Num("sh3-u");
  if (u !== null && u > 0) cm = (u + 22) * 2.54 / 3;
  if (cm === null || cm <= 0) { o.innerHTML = "Enter a positive foot length in cm, or a US men's size."; return; }
  var inches = cm / 2.54, uk = 3 * inches - 23, usM = uk + 1, usW = uk + 2, eu = uk + 33;
  o.innerHTML = "<b>" + usM.toFixed(1) + " US (men's)</b>from a " + nfmt(cm, 1) + " cm foot" +
    "<span class='jf-chip'><b>" + usW.toFixed(1) + "</b>US women's</span>" +
    "<span class='jf-chip'><b>" + uk.toFixed(1) + "</b>UK</span>" +
    "<span class='jf-chip'><b>" + eu.toFixed(1) + "</b>EU (approx)</span>" +
    "<span class='jf-chip'><b>" + inches.toFixed(2) + " in</b>foot length in inches</span>" +
    "<span class='jf-chip'><b>" + (cm * 10) + " mm</b>Mondopoint (ski boots)</span>";
}

/* --- tv2: TV viewing distance --- */
function tv2() {
  var o = $("tv2-out");
  var d = m7Num("tv2-d"), res = String($("tv2-r").value || "4k"), me = m7Num("tv2-m");
  if (d === null || d < 10) { o.innerHTML = "Enter a screen diagonal of at least 10 inches."; return; }
  var F = { "4k": [1.0, 1.5], "8k": [0.8, 1.2], "1080": [1.5, 2.5], "720": [2.0, 3.0] };
  var f = F[res] || F["4k"];
  var name = res === "4k" ? "4K" : res === "8k" ? "8K" : res;
  var mn = d * f[0] / 12, mx = d * f[1] / 12, thx = d * 1.37 / 12;
  var widthIn = d * 16 / Math.sqrt(337);
  var angleTxt = "";
  var verdict = "";
  if (me !== null && me > 0) {
    var ang = 2 * Math.atan((widthIn / 12 / 2) / me) * 180 / Math.PI;
    var ok = me >= mn && me <= mx;
    verdict = "<span class='jf-chip" + (ok ? "" : " jf-chip-bad") + "'><b>" + (ok ? "perfect" : (me < mn ? "too close" : "too far")) + "</b>at " + nfmt(me, 1) + " ft for " + name + "</span>";
    angleTxt = "<span class='jf-chip'><b>" + ang.toFixed(0) + "\u00b0</b>your current field of view</span>";
  }
  o.innerHTML = "<b>" + mn.toFixed(1) + "\u2013" + mx.toFixed(1) + " ft</b>comfortable distance for " + d + "\u2033 " + name +
    "<span class='jf-chip'><b>" + thx.toFixed(1) + " ft</b>THX 40\u00b0 cinema recommendation</span>" +
    "<span class='jf-chip'><b>" + nfmt(widthIn, 1) + " in</b>actual screen width</span>" +
    angleTxt + verdict;
}

/* --- ck2: cooking measurement --- */
function ck2() {
  var o = $("ck2-out");
  var dens = +String($("ck2-i").value || "125") / 240;
  var v = m7Num("ck2-v");
  var unit = String($("ck2-u").value || "cup");
  var ML = { "cup": 240, "tbsp": 15, "tsp": 5, "ml": 1, "floz": 29.5735 };
  if (v === null || v < 0) { o.innerHTML = "Enter a non-negative amount."; return; }
  var ml = v * ML[unit];
  var g = ml * dens;
  o.innerHTML = "<b>" + nfmt(g, 1) + " g</b>(" + nfmt(g / 28.3495, 1) + " oz)" +
    "<span class='jf-chip'><b>" + nfmt(ml, 1) + " ml</b>volume converted</span>" +
    "<span class='jf-chip'><b>" + nfmt(ml / 240, 2) + "</b>cups</span>" +
    "<span class='jf-chip'><b>" + nfmt(ml / 15, 1) + "</b>tablespoons</span>" +
    "<span class='jf-chip'><b>" + nfmt(ml / 5, 1) + "</b>teaspoons</span>" +
    "<span class='jf-chip'><b>" + nfmt(dens * 240, 0) + " g/cup</b>density used for this ingredient</span>";
}

/* --- cq2: commute cost --- */
function cq2() {
  var o = $("cq2-out");
  var d = m7Num("cq2-d"), g = m7Num("cq2-g"), p = m7Num("cq2-p"), w = m7Num("cq2-w"), toll = m7Num("cq2-t"), pk = m7Num("cq2-k");
  if (d === null || d <= 0 || g === null || g <= 0 || p === null || p < 0) { o.innerHTML = "Enter a positive distance and mpg, and a non-negative fuel price."; return; }
  if (w === null || w < 1) w = 5;
  if (toll === null || toll < 0) toll = 0;
  if (pk === null || pk < 0) pk = 0;
  var dayFuel = 2 * d / g * p, day = dayFuel + toll, week = day * w;
  var month = week * 4.33 + pk, year = week * 52 + pk * 12;
  o.innerHTML = "<b>" + m7Money(day) + "</b>per driving day" +
    "<span class='jf-chip'><b>" + m7Money(dayFuel) + "</b>fuel alone (two trips, " + nfmt(2 * d, 0) + " miles \u00f7 " + g + " mpg)</span>" +
    "<span class='jf-chip'><b>" + m7Money(week) + "</b>per week (" + w + " days)</span>" +
    "<span class='jf-chip'><b>" + m7Money(month) + "</b>per month (incl. " + m7Money(pk) + " parking)</span>" +
    "<span class='jf-chip jf-chip-bad'><b>" + m7Money(year) + "</b>per year \u2014 the real number</span>" +
    "<span class='jf-chip'><b>" + m7Money(year / (w * 52)) + "</b>effective cost of every working day</span>";
}

/* --- mr2: mileage reimbursement --- */
function mr2() {
  var o = $("mr2-out");
  var m = m7Num("mr2-m"), r = m7Num("mr2-r");
  if (m === null || m < 0 || r === null || r < 0) { o.innerHTML = "Enter non-negative miles and a rate per mile."; return; }
  var claim = m * r;
  o.innerHTML = "<b>" + m7Money(claim) + "</b>for " + nfmt(m, 0) + " miles at " + m7Money(r) + " per mile" +
    "<span class='jf-chip'><b>" + m7Money(claim * 12) + "</b>if this repeats all twelve months</span>" +
    "<span class='jf-chip'><b>" + m7Money(m * 52 / 12 * r) + "</b>if these are weekly miles instead</span>" +
    (r < 0.55 ? "<span class='jf-chip jf-chip-bad'><b>low</b>below recent IRS standard rates \u2014 check yours</span>" : "<span class='jf-chip'><b>in range</b>of recent IRS standard rates</span>");
}

/* --- sp3: study plan --- */
function sp3() {
  var o = $("sp3-out");
  var subs = String($("sp3-in").value || "").split("\n").map(function (s) { return s.trim(); }).filter(Boolean);
  var e = String($("sp3-e").value || "").trim(), slots = m7Num("sp3-s");
  if (!subs.length) { o.innerHTML = "List at least one subject, one per line."; return; }
  if (!/^\d{4}-\d{2}-\d{2}$/.test(e)) { o.innerHTML = "Pick an exam date (YYYY-MM-DD)."; return; }
  var p = e.split("-"), exam = new Date(+p[0], +p[1] - 1, +p[2]);
  var days = Math.ceil((exam - new Date()) / 86400000);
  if (days < 1) { o.innerHTML = "The exam date has already passed \u2014 pick a future date."; return; }
  if (slots === null || slots < 1) slots = 2;
  var plan = [], n = subs.length, k = 0, dd, dd2, daySubs, s;
  for (var i = 0; i < days; i++) {
    dd = new Date(exam.getTime() - (days - 1 - i) * 86400000);
    dd2 = dd.getFullYear() + "-" + String(dd.getMonth() + 1).padStart(2, "0") + "-" + String(dd.getDate()).padStart(2, "0");
    daySubs = [];
    for (s = 0; s < slots; s++) daySubs.push(subs[k++ % n]);
    plan.push("Day " + (i + 1) + " (" + dd2 + "): " + daySubs.join(", "));
  }
  o.innerHTML = "<b>" + days + " days \u00d7 " + slots + " slots = " + (days * slots) + " sessions</b>before " + e + "<br>" +
    plan.join("<br>");
}

/* --- to2: TOTP (RFC 6238) --- */
function to2B32(s) {
  s = String(s || "").replace(/[\s=.\-]/g, "").toUpperCase();
  var A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567", bits = 0, val = 0, out = [];
  for (var i = 0; i < s.length; i++) {
    var idx = A.indexOf(s[i]);
    if (idx < 0) return null;
    val = (val << 5) | idx;
    bits += 5;
    if (bits >= 8) { out.push((val >>> (bits - 8)) & 255); bits -= 8; }
  }
  return out;
}
async function to2() {
  var o = $("to2-out");
  var k = to2B32($("to2-k").value);
  if (!k || !k.length) { o.innerHTML = "Paste a base32 secret \u2014 letters A\u2013Z and digits 2\u20137; spaces are stripped."; return; }
  var d = +String($("to2-d").value || "6"), period = +String($("to2-p").value || "30");
  var atS = String($("to2-at").value || "").trim();
  var t0 = (atS !== "" && isFinite(+atS)) ? +atS : Math.floor(Date.now() / 1000);
  var ctr = Math.floor(t0 / period);
  var key = new Uint8Array(k);
  var mac = await crypto.subtle.importKey("raw", key, { name: "HMAC", hash: "SHA-1" }, false, ["sign"]);
  function enc(n) {
    var a = new Uint8Array(8);
    for (var i = 7; i >= 0; i--) { a[i] = n % 256; n = Math.floor(n / 256); }
    return a;
  }
  async function codeFor(c) {
    var sig = new Uint8Array(await crypto.subtle.sign("HMAC", mac, enc(c)));
    var off = sig[sig.length - 1] & 0xf;
    var bin = ((sig[off] & 0x7f) << 24) | (sig[off + 1] << 16) | (sig[off + 2] << 8) | sig[off + 3];
    var num = bin % Math.pow(10, d) + "";
    while (num.length < d) num = "0" + num;
    return num;
  }
  var cur = await codeFor(ctr), nxt = await codeFor(ctr + 1);
  var remaining = period - (t0 % period);
  o.innerHTML = "<b>" + cur + "</b>valid right now" +
    "<span class='jf-chip'><b>" + remaining + " s</b>until the next window</span>" +
    "<span class='jf-chip'><b>" + nxt + "</b>next code</span>" +
    "<span class='jf-chip'><b>" + ctr + "</b>time counter (unix \u00f7 " + period + ")</span>" +
    "<span class='jf-chip'><b>" + k.length + " bytes</b>decoded from base32</span>";
}

/* --- sa3: salary to hourly --- */
function sa3() {
  var o = $("sa3-out");
  var a = m7Num("sa3-a"), h = m7Num("sa3-h"), w = m7Num("sa3-w"), r = m7Num("sa3-r");
  if (h === null || h <= 0 || w === null || w <= 0) { o.innerHTML = "Enter positive hours per week and weeks per year."; return; }
  if (r !== null && r > 0) a = r * h * w;
  if (a === null || a < 0) { o.innerHTML = "Enter an annual salary, or an hourly rate to reverse-convert."; return; }
  var hourly = a / (h * w);
  o.innerHTML = "<b>" + m7Money(hourly) + "</b>per hour" +
    "<span class='jf-chip'><b>" + m7Money(hourly * h) + "</b>per day (" + h + " h)</span>" +
    "<span class='jf-chip'><b>" + m7Money(a / w) + "</b>per week</span>" +
    "<span class='jf-chip'><b>" + m7Money(a / 12) + "</b>per month</span>" +
    "<span class='jf-chip'><b>" + m7Money(a) + "</b>annual total</span>" +
    "<span class='jf-chip'><b>" + nfmt(h * w, 0) + " h</b>paid hours in the year</span>";
}

/* wire the batch-25 engines into the shared M3 finisher */
["sh3", "tv2", "ck2", "cq2", "mr2", "sp3", "sa3"].forEach(function (fn) {
  var orig = null;
  try { orig = window[fn] || eval(fn); } catch (e) { orig = null; }
  if (typeof orig !== "function") return;
  window[fn] = function () { orig(); m3After(); };
});
["to2"].forEach(function (fn) {
  var orig = null;
  try { orig = window[fn] || eval(fn); } catch (e) { orig = null; }
  if (typeof orig !== "function") return;
  window[fn] = function () { return orig().then(function () { m3After(); }); };
});



/* --- M12: batch-26 engines (ca2 ev2 wi2 hi2 dp2 na2 tp3 sd2) --- */

/* --- ca2: CAGR --- */
function ca2() {
  var o = $("ca2-out");
  var b = m7Num("ca2-b"), e = m7Num("ca2-e"), y = m7Num("ca2-y");
  if (b === null || b <= 0 || e === null || e < 0 || y === null || y <= 0) { o.innerHTML = "Enter a positive start value, an end value and a positive number of years."; return; }
  var r = Math.pow(e / b, 1 / y) - 1;
  var dbl = r > 0 ? (Math.log(2) / Math.log(1 + r)).toFixed(1) + " years \u2014 the rule of 72 checks this as " + nfmt(72 / (r * 100), 1) : "\u2014";
  o.innerHTML = "<b>" + (r * 100).toFixed(2) + "%</b>compound annual growth over " + nfmt(y, 0) + " years" +
    "<span class='jf-chip" + (r <= 0 ? " jf-chip-bad" : "") + "'><b>" + nfmt(e / b, 2) + "+\u00d7</b>total growth multiple</span>" +
    (e > b ? "<span class='jf-chip'><b>" + nfmt(e - b, 0) + "</b>money gained</span>"
           : "<span class='jf-chip jf-chip-bad'><b>" + nfmt(b - e, 0) + "</b>money lost</span>") +
    "<span class='jf-chip'><b>" + dbl + "</b>years to double at this rate</span>" +
    (r > 0 ? "<span class='jf-chip'><b>" + nfmt(e * Math.pow(1 + r, y), 0) + "</b>if the same rate holds another " + nfmt(y, 0) + " years</span>" : "");
}

/* --- ev2: EV charging cost --- */
function ev2() {
  var o = $("ev2-out");
  var b = m7Num("ev2-b"), c = m7Num("ev2-c"), t = m7Num("ev2-t"), p = m7Num("ev2-p"), e = m7Num("ev2-e");
  if (b === null || b <= 0 || c === null || t === null || p === null || p < 0 || e === null || e <= 0) { o.innerHTML = "Enter battery kWh, both charge percentages, a non-negative price and positive efficiency."; return; }
  c = Math.min(100, Math.max(0, c)); t = Math.min(100, Math.max(0, t));
  if (t <= c) { o.innerHTML = "The target charge must be above the current charge."; return; }
  var kwh = b * (t - c) / 100, cost = kwh * p, miles = kwh * e;
  o.innerHTML = "<b>" + m7Money(cost) + "</b>for this charge (" + nfmt(kwh, 1) + " kWh delivered)" +
    "<span class='jf-chip'><b>" + nfmt(miles, 0) + " mi</b>of range added</span>" +
    "<span class='jf-chip'><b>" + m7Money(100 / e * p) + "</b>per 100 miles \u2014 compare with petrol</span>" +
    "<span class='jf-chip'><b>" + nfmt(e / p, 1) + "</b>miles per dollar</span>" +
    "<span class='jf-chip'><b>" + m7Money(b * p) + "</b>a full 0\u2013100% charge</span>" +
    "<span class='jf-chip'><b>" + nfmt(t - c, 0) + "%</b>of the battery moved</span>";
}

/* --- wi2: wind chill (NWS formula) --- */
function wi2() {
  var o = $("wi2-out");
  var t = m7Num("wi2-t"), v = m7Num("wi2-v");
  if (t === null || v === null || v < 0) { o.innerHTML = "Enter an air temperature and a non-negative wind speed."; return; }
  var wc = t;
  var valid = t <= 50 && v >= 3;
  if (valid) { var f = Math.pow(v, 0.16); wc = 35.74 + 0.6215 * t - 35.75 * f + 0.4275 * t * f; }
  var risk = wc <= -48 ? "in 5 minutes" : wc <= -32 ? "in 10 minutes" : wc <= -19 ? "in 30 minutes" : "low at this reading";
  var bad = wc <= -19;
  o.innerHTML = "<b>" + wc.toFixed(1) + "\u00b0F</b>feels like in the wind" +
    "<span class='jf-chip'><b>" + nfmt((wc - 32) / 1.8, 1) + "\u00b0C</b>same feel in Celsius</span>" +
    (valid ? "<span class='jf-chip" + (bad ? " jf-chip-bad" : "") + "'><b>" + risk + "</b>frostbite risk on exposed skin</span>"
           : "<span class='jf-chip jf-chip-bad'><b>no chill</b>wind chill is undefined above 50\u00b0F or below 3 mph \u2014 showing the air temperature</span>") +
    "<span class='jf-chip'><b>" + nfmt((t - 32) / 1.8, 1) + "\u00b0C</b>actual air temperature</span>" +
    "<span class='jf-chip'><b>" + nfmt(t - wc, 1) + "\u00b0F</b>taken off you by the wind</span>";
}

/* --- hi2: heat index (NWS equation) --- */
function hi2() {
  var o = $("hi2-out");
  var t = m7Num("hi2-t"), r = m7Num("hi2-r");
  if (t === null || r === null || r < 0 || r > 100) { o.innerHTML = "Enter a temperature and a humidity between 0 and 100%."; return; }
  var hi = t;
  var valid = t >= 80 && r >= 40;
  if (valid) {
    hi = -42.379 + 2.04901523 * t + 10.14333127 * r - 0.22475541 * t * r
       - 0.00683783 * t * t - 0.05481717 * r * r + 0.00122874 * t * t * r
       + 0.00085282 * t * r * r - 0.00000199 * t * t * r * r;
  }
  var band = hi >= 125 ? ["extreme danger", true] : hi >= 103 ? ["danger", true] : hi >= 90 ? ["extreme caution", true] : hi >= 80 ? ["caution", false] : ["no heat stress", false];
  o.innerHTML = "<b>" + hi.toFixed(1) + "\u00b0F</b>heat index \u2014 what your body actually fights" +
    "<span class='jf-chip" + (band[1] ? " jf-chip-bad" : "") + "'><b>" + band[0] + "</b>official risk band</span>" +
    "<span class='jf-chip'><b>" + nfmt((hi - 32) / 1.8, 1) + "\u00b0C</b>same heat in Celsius</span>" +
    "<span class='jf-chip'><b>" + nfmt(hi - t, 1) + "\u00b0F</b>added by humidity</span>" +
    (valid ? "" : "<span class='jf-chip jf-chip-bad'><b>out of range</b>the official equation applies from 80\u00b0F and 40% humidity \u2014 showing the air temperature</span>");
}

/* --- dp2: debt payoff planner (snowball vs avalanche, month simulation) --- */
function dp2Sort(lines, strat) {
  var a = lines.slice();
  if (strat === "snowball") a.sort(function (x, y) { return x.bal - y.bal || y.apr - x.apr; });
  else a.sort(function (x, y) { return y.apr - x.apr || x.bal - y.bal; });
  return a;
}
function dp2Run(lines, strat, extra) {
  var ds = dp2Sort(lines, strat), interest = 0, closed = [], n = 0, m, k;
  for (m = 0; m < 600; m++) {
    var budget = extra;
    for (k = 0; k < ds.length; k++) if (ds[k].bal > 0) {
      var acc = ds[k].bal * ds[k].apr / 12; ds[k].bal += acc; interest += acc;
    }
    for (k = 0; k < ds.length; k++) if (ds[k].bal > 0) {
      var pay = Math.min(ds[k].min, ds[k].bal);
      ds[k].bal -= pay; budget += ds[k].min - pay;
    }
    for (k = 0; k < ds.length && budget > 0.004; k++) if (ds[k].bal > 0) {
      var x = Math.min(budget, ds[k].bal); ds[k].bal -= x; budget -= x;
    }
    n = m + 1;
    var anyOpen = false;
    for (k = 0; k < ds.length; k++) {
      if (ds[k].bal <= 0.005 && !closed[k]) { ds[k].bal = 0; closed[k] = n; }
      if (ds[k].bal > 0) anyOpen = true;
    }
    if (!anyOpen) break;
  }
  var order = ds.map(function (d, k2) { return closed[k2] ? d.name + " closed in month " + closed[k2] : d.name + " not cleared"; }).join(", ");
  return { months: n, interest: interest, order: order, stalled: ds.some(function (d) { return d.bal > 0; }) };
}
function dp2Parse() {
  var raw = String($("dp2-l").value || "").split(/[\n;]+/), lines = [];
  for (var i = 0; i < raw.length; i++) {
    var s = raw[i].trim(); if (!s) continue;
    var parts = s.replace(/\u2212/g, "-").split(/[\s,;\t]+/).map(parseFloat);
    if (parts.length < 3 || !isFinite(parts[0]) || !isFinite(parts[1]) || !isFinite(parts[2]) || parts[0] < 0 || parts[2] <= 0) continue;
    lines.push({ name: "debt " + (lines.length + 1), bal: parts[0], apr: parts[1] > 1 ? parts[1] / 100 : parts[1], min: parts[2] });
  }
  return lines;
}
function dp2() {
  var o = $("dp2-out");
  var lines = dp2Parse();
  var strat = String($("dp2-s").value || "avalanche");
  var x = m7Num("dp2-x"); if (x === null || x < 0) x = 0;
  if (!lines.length) { o.innerHTML = "List at least one debt as: balance, APR, minimum payment."; return; }
  var run = dp2Run(lines.map(function (d) { return { name: d.name, bal: d.bal, apr: d.apr, min: d.min }; }), strat, x);
  var other = strat === "snowball" ? "avalanche" : "snowball";
  var run2 = dp2Run(lines.map(function (d) { return { name: d.name, bal: d.bal, apr: d.apr, min: d.min }; }), other, x);
  if (run.stalled) {
    o.innerHTML = "<b>Stalled</b>the payments never cover the interest \u2014 raise the extra or the minimums before anything clears.";
    return;
  }
  var save = run.interest - run2.interest;
  o.innerHTML = "<b>" + run.months + " months</b>to debt-free (" + strat + ", " + m7Money(x) + " extra)" +
    "<span class='jf-chip jf-chip-bad'><b>" + m7Money(run.interest) + "</b>total interest paid</span>" +
    "<span class='jf-chip'><b>" + escHtml(run.order) + "</b>payoff order</span>" +
    "<span class='jf-chip'><b>" + run2.months + " months / " + m7Money(run2.interest) + "</b>if you switched to " + other + "</span>" +
    (Math.abs(save) >= 0.5 ? "<span class='jf-chip'><b>" + m7Money(Math.abs(save)) + "</b>" + (save > 0 ? "interest " + other + " saves you" : "interest you save over " + other) + "</span>" : "<span class='jf-chip'><b>tie</b>both orderings cost the same here</span>");
}

/* --- na2: anagram checker --- */
function na2Clean(s) {
  return String(s || "").toLowerCase().replace(/[^a-z0-9]/g, "").split("").sort().join("");
}
function na2() {
  var o = $("na2-out");
  var a = String($("na2-a").value || ""), b = String($("na2-b").value || "");
  var ca = na2Clean(a), cb = na2Clean(b);
  if (!ca || !cb) { o.innerHTML = "Enter two words or phrases, ignoring spaces and punctuation."; return; }
  if (ca === cb) {
    o.innerHTML = "<b>True anagram</b>" + escHtml(a.trim()) + " and " + escHtml(b.trim()) + " share every letter" +
      "<span class='jf-chip'><b>" + ca.length + "</b>letters on each side</span>" +
      "<span class='jf-chip'><b>" + escHtml(ca) + "</b>shared letters, sorted</span>";
    return;
  }
  var map = {}, i, ch, countsB = {}, diffA = [], diffB = [], common = 0;
  for (i = 0; i < ca.length; i++) map[ca[i]] = (map[ca[i]] || 0) + 1;
  for (i = 0; i < cb.length; i++) countsB[cb[i]] = (countsB[cb[i]] || 0) + 1;
  for (ch in map) if (countsB[ch]) common += Math.min(map[ch], countsB[ch]);
  for (ch in map) if (map[ch] - (countsB[ch] || 0) > 0) diffA.push(ch + "\u00d7" + (map[ch] - (countsB[ch] || 0)));
  for (ch in countsB) if ((countsB[ch] || 0) - (map[ch] || 0) > 0) diffB.push(ch + "\u00d7" + (countsB[ch] - (map[ch] || 0)));
  var pct = Math.round(200 * common / (ca.length + cb.length));
  o.innerHTML = "<b>Not an anagram</b>\u2014 " + pct + "% of the letters match" +
    (diffA.length ? "<span class='jf-chip jf-chip-bad'><b>" + escHtml(diffA.join(" ")) + "</b>in " + escHtml(a.trim()) + " but missing from the other</span>" : "") +
    (diffB.length ? "<span class='jf-chip jf-chip-bad'><b>" + escHtml(diffB.join(" ")) + "</b>in " + escHtml(b.trim()) + " but missing from the other</span>" : "") +
    "<span class='jf-chip'><b>" + escHtml(ca) + "</b>first side, sorted</span>" +
    "<span class='jf-chip'><b>" + escHtml(cb) + "</b>second side, sorted</span>";
}

/* --- tp3: tap tempo --- */
var TP3_T = window.TP3_T = window.TP3_T || [];
function tp3Tap() { TP3_T.push(Date.now()); while (TP3_T.length > 8) TP3_T.shift(); tp3Calc(); }
function tp3Reset() { TP3_T.length = 0; $("tp3-out").innerHTML = ""; }
function tp3Calc() {
  var o = $("tp3-out");
  if (TP3_T.length < 2) { if (TP3_T.length === 1) o.innerHTML = "Keep tapping \u2014 1 tap so far."; return; }
  var i, sum = 0, mn = Infinity, mx = -Infinity;
  for (i = 1; i < TP3_T.length; i++) { var d = TP3_T[i] - TP3_T[i - 1]; sum += d; if (d < mn) mn = d; if (d > mx) mx = d; }
  var avg = sum / (TP3_T.length - 1), bpm = 60000 / avg;
  o.innerHTML = "<b>" + bpm.toFixed(1) + " BPM</b>from the last " + TP3_T.length + " taps" +
    "<span class='jf-chip'><b>" + nfmt(60000 / bpm, 0) + " ms</b>per beat</span>" +
    "<span class='jf-chip'><b>" + nfmt(avg, 0) + " ms</b>average gap between taps</span>" +
    "<span class='jf-chip'><b>" + nfmt(mx - mn, 0) + " ms</b>tap spread \u2014 over 40 ms means tap tighter</span>";
}

/* --- sd2: sleep debt --- */
function sd2() {
  var o = $("sd2-out");
  var need = m7Num("sd2-n");
  if (need === null || need <= 0 || need > 14) { o.innerHTML = "Enter a per-night sleep need between 1 and 14 hours."; return; }
  var parts = String($("sd2-h").value || "").split(/[,;\s]+/).filter(Boolean).map(parseFloat).filter(isFinite).slice(0, 7);
  if (!parts.length) { o.innerHTML = "Enter the hours you slept, separated by commas."; return; }
  var n = parts.length, sum = 0, mn = parts[0], mx = parts[0], i;
  for (i = 0; i < n; i++) { sum += parts[i]; if (parts[i] < mn) mn = parts[i]; if (parts[i] > mx) mx = parts[i]; }
  var debt = Math.max(0, n * need - sum);
  var recover = debt / 1.5;
  o.innerHTML = (debt > 0 ? "<b>" + nfmt(debt, 1) + " h in debt</b>across " + n + " nights vs a " + need + " h need"
                          : "<b>No sleep debt</b>across " + n + " nights \u2014 you banked " + nfmt(sum - n * need, 1) + " h spare") +
    "<span class='jf-chip'><b>" + nfmt(sum / n, 1) + " h</b>average per night</span>" +
    "<span class='jf-chip'><b>" + nfmt(mn, 1) + " h</b>worst night</span>" +
    "<span class='jf-chip'><b>" + nfmt(mx, 1) + " h</b>best night</span>" +
    (debt > 0 ? "<span class='jf-chip jf-chip-bad'><b>" + nfmt(recover, 1) + " nights</b>to repay at +1.5 h extra per catch-up night</span>"
              : "<span class='jf-chip'><b>earned</b>a sleep surplus \u2014 protect the routine</span>") +
    "<span class='jf-chip'><b>" + nfmt(sum, 1) + " h</b>slept in total</span>";
}

/* wire the batch-26 engines into the shared M3 finisher */
["ca2", "ev2", "wi2", "hi2", "dp2", "na2", "tp3Calc", "sd2"].forEach(function (fn) {
  var orig = null;
  try { orig = window[fn] || eval(fn); } catch (e) { orig = null; }
  if (typeof orig !== "function") return;
  window[fn] = function () { orig(); m3After(); };
});
