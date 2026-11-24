/* ===================== M28 SECTION: batch 28 engines (mega14 + mega15) ===================== */

/* --- M14 finance engines --- */
function ay2() {
  var o = $("ay2-out"); var r = _n("ay2-r"); var n = parseFloat(_v("ay2-n")); var dir = _v("ay2-d");
  if (!o) return;
  if (r === null || r < 0 || !(n > 0)) { o.innerHTML = "Enter a non-negative rate and valid compounding frequency."; return; }
  if (dir === "a") {
    var apy = (Math.pow(1 + r / 100 / n, n) - 1) * 100;
    o.innerHTML = "<b>" + nfmt(apy, 2) + "%</b> effective yield (APY) on a " + nfmt(r, 2) + "% nominal rate compounded " + n + " times a year" +
      "<span class='jf-chip'><b>" + nfmt(r / n, 4) + "%</b>rate per period</span>" +
      "<span class='jf-chip'><b>" + nfmt((Math.pow(1 + r / 100 / n, n) - 1) * 100 - r, 2) + " pts</b>compounding adds over the flat rate</span>" +
      "<span class='jf-chip'><b>" + nfmt(Math.pow(1 + r / 100 / n, n), 4) + "</b>year-end multiple of principal</span>";
    return;
  }
  var apr = (Math.pow(1 + r / 100, 1 / n) - 1) * n * 100;
  o.innerHTML = "<b>" + nfmt(apr, 2) + "%</b> nominal rate (APR) that compounds " + n + " times a year into a real " + nfmt(r, 2) + "% APY" +
    "<span class='jf-chip'><b>" + nfmt(apr / n, 4) + "%</b>rate per period</span>" +
    "<span class='jf-chip'><b>" + nfmt(r - apr, 2) + " pts</b>compounding adds over the flat rate</span>";
}

function vg2() {
  var o = $("vg2-out"); var g = _n("vg2-g"), s = _n("vg2-s"), r = _n("vg2-r"), y = _n("vg2-y");
  if (!o) return;
  if (g === null || g <= 0) { o.innerHTML = "Enter the goal amount (more than zero)."; return; }
  if (s === null || s < 0) s = 0;
  if (y === null || y <= 0) { o.innerHTML = "Enter the years to reach the goal (more than zero)."; return; }
  var n = 12, rn = (r === null ? 0 : r / 100 / n), months = Math.round(y * 12);
  var fv = s * Math.pow(1 + rn, months);
  var gap = Math.max(0, g - fv);
  var dep = rn > 0 ? gap * rn / (Math.pow(1 + rn, months) - 1) : gap / months;
  o.innerHTML = "<b>" + m7Money(dep) + "</b>per month" + (r !== null && r > 0 ? " with interest working" : "") +
    "<span class='jf-chip'><b>" + m7Money(fv) + "</b>your existing savings grow to by then</span>" +
    "<span class='jf-chip'><b>" + m7Money(gap) + "</b>remaining gap to close</span>" +
    "<span class='jf-chip'><b>" + m7Money(dep * months) + "</b>total you deposit over " + months + " months</span>" +
    (fv >= g ? "<span class='jf-chip jf-chip-bad'>Goal already reached \u2014 savings alone get you there</span>" : "");
}

function ci3() {
  var o = $("ci3-out"); var b = _n("ci3-b"), apr = _n("ci3-a"), p = _n("ci3-p");
  if (!o) return;
  if (b === null || b <= 0) { o.innerHTML = "Enter the balance owed (more than zero)."; return; }
  if (apr === null || apr < 0) apr = 0;
  if (p === null || p <= 0) { o.innerHTML = "Enter the monthly payment."; return; }
  var r = apr / 100 / 12;
  if (p <= b * r) { o.innerHTML = "The payment " + m7Money(p) + " does not cover the first month's interest (" + m7Money(b * r) + ") \u2014 the balance never shrinks. Raise the payment."; return; }
  var months = 0, interest = 0, bal = b;
  while (bal > 0 && months < 600) { interest += bal * r; bal = bal * (1 + r) - p; months++; }
  var d = new Date(Date.now() + months * 30.44 * 86400000);
  o.innerHTML = "<b>" + months + " months</b>to clear " + m7Money(b) + " at " + nfmt(apr, 1) + "% APR paying " + m7Money(p) + " monthly" +
    "<span class='jf-chip'><b>" + m7Money(interest) + "</b>total interest paid</span>" +
    "<span class='jf-chip'><b>" + m7Money(b + interest) + "</b>all-in cost of the debt</span>" +
    "<span class='jf-chip'><b>" + d.toLocaleDateString("en-US", { month: "short", year: "numeric" }) + "</b>projected payoff month</span>" +
    "<span class='jf-chip'><b>last payment smaller</b>the final month bills only what is left</span>";
}

function ra3() {
  var o = $("ra3-out"); var i = _n("ra3-i"); var rule = parseFloat(_v("ra3-r"));
  if (!o) return;
  if (i === null || i <= 0) { o.innerHTML = "Enter your gross annual income."; return; }
  var rent = i * rule / 100 / 12;
  o.innerHTML = "<b>" + m7Money(rent) + "</b>per month is the " + rule + "% cap on " + m7Money(i) + " gross income" +
    "<span class='jf-chip'><b>" + m7Money(i * rule / 100) + "</b>annual housing budget at the same rule</span>" +
    "<span class='jf-chip'><b>" + m7Money(i / 12 - rent) + "</b>per month left after rent (pre-tax)</span>" +
    "<span class='jf-chip'><b>" + m7Money(i / 40) + "</b>monthly rent the landlord 40\u00d7 income screen allows</span>" +
    (rule > 30 ? "<span class='jf-chip jf-chip-bad'>Above 30% \u2014 savings, not just comfort, get squeezed</span>" : "");
}

function ie2() {
  var o = $("ie2-out"); var p = _n("ie2-p"), r = _n("ie2-r"), f = _n("ie2-f"), y = _n("ie2-y");
  if (!o) return;
  if (p === null || p <= 0) { o.innerHTML = "Enter the portfolio value."; return; }
  if (r === null) r = 0;
  if (f === null) f = 0;
  if (y === null || y <= 0) { o.innerHTML = "Enter the years invested."; return; }
  var gross = p * Math.pow(1 + r / 100, y);
  var net = p * Math.pow(1 + (r - f) / 100, y);
  var drag = gross - net;
  o.innerHTML = "<b>" + m7Money(net) + "</b>after " + nfmt(f, 2) + "% fees over " + nfmt(y, 0) + " years \u2014 vs " + m7Money(gross) + " with none" +
    "<span class='jf-chip jf-chip-bad'><b>" + m7Money(drag) + "</b>wealth the fee deletes</span>" +
    "<span class='jf-chip'><b>" + nfmt(drag / gross * 100, 1) + "%</b>of the fee-free pot gone</span>" +
    "<span class='jf-chip'><b>" + m7Money(drag / y) + "</b>per year on average \u2014 not a rounding error</span>";
}

function sl3() {
  var o = $("sl3-out"); var old = _n("sl3-o"), nw = _n("sl3-n"), cpi = _n("sl3-c");
  if (!o) return;
  if (old === null || old <= 0) { o.innerHTML = "Enter the old salary (more than zero)."; return; }
  if (nw === null) { o.innerHTML = "Enter the new salary."; return; }
  if (cpi === null) cpi = 0;
  var pct = (nw - old) / old * 100;
  var real = ((nw / old) / (1 + cpi / 100) - 1) * 100;
  var today = nw / (1 + cpi / 100);
  o.innerHTML = "<b>" + nfmt(pct, 2) + "%</b>raise, worth a real " + nfmt(real, 2) + "% after " + nfmt(cpi, 1) + "% inflation" +
    "<span class='jf-chip'><b>" + m7Money(today) + "</b>new salary in today's money</span>" +
    "<span class='jf-chip'><b>" + m7Money(nw - old) + "</b>extra per year, nominal</span>" +
    (real < 0 ? "<span class='jf-chip jf-chip-bad'>CPI beats the raise \u2014 buying power shrank " + nfmt(Math.abs(real), 2) + "%</span>" : "<span class='jf-chip'><b>ahead of CPI</b>the raise buys more goods than last year</span>");
}

function va2() {
  var o = $("va2-out"); var rt = _n("va2-r"), mo = _n("va2-m"), used = _n("va2-u");
  if (!o) return;
  if (rt === null || rt <= 0) { o.innerHTML = "Enter the accrual rate (days per month)."; return; }
  if (mo === null || mo <= 0) { o.innerHTML = "Enter the months worked."; return; }
  if (used === null || used < 0) used = 0;
  var earned = rt * mo, bal = earned - used;
  o.innerHTML = "<b>" + nfmt(bal, 1) + " days</b>of PTO in the bank right now" +
    "<span class='jf-chip'><b>" + nfmt(earned, 1) + "</b>earned over " + nfmt(mo, 0) + " months</span>" +
    "<span class='jf-chip'><b>" + nfmt(used, 1) + "</b>already used (" + nfmt(earned > 0 ? used / earned * 100 : 0, 0) + "%)</span>" +
    "<span class='jf-chip'><b>" + nfmt(rt, 2) + "+1 days</b>the next month adds one more</span>" +
    (bal < 0 ? "<span class='jf-chip jf-chip-bad'>Overdrawn \u2014 borrowed days against the year ahead</span>" : "");
}

function dn2() {
  var o = $("dn2-out"); var p = _n("dn2-p"), s = _n("dn2-s"), m = _n("dn2-m");
  if (!o) return;
  if (p === null || p <= 0) { o.innerHTML = "Enter the home price."; return; }
  if (s === null || s < 0) s = 0;
  var pct = s / p * 100, target = p * 0.2, extra = Math.max(0, target - s);
  var pmi = pct < 20 ? (p - s) * 0.005 / 12 : 0;
  var mts = (m !== null && m > 0 && extra > 0) ? Math.ceil(extra / m) : 0;
  o.innerHTML = "<b>" + nfmt(pct, 1) + "%</b>down (" + m7Money(s) + " of " + m7Money(p) + ")" +
    "<span class='jf-chip " + (pmi > 0 ? "jf-chip-bad" : "") + "'><b>" + (pmi > 0 ? m7Money(pmi) + "/month" : "none \u2014 over 20%") + "</b>estimated PMI at 0.5%/yr</span>" +
    "<span class='jf-chip'><b>" + m7Money(target) + "</b>is the 20% escape line</span>" +
    (extra > 0 ? "<span class='jf-chip'><b>" + m7Money(extra) + "</b>still needed</span>" + (mts > 0 ? "<span class='jf-chip'><b>" + mts + " months</b>at " + m7Money(m) + " saved monthly</span>" : "") : "<span class='jf-chip'><b>PMI cleared</b>no more mortgage insurance owed</span>");
}

function mp2pmt(principal, ar, yrs) {
  var rr = ar / 100 / 12, nn = yrs * 12;
  return principal * rr / (1 - Math.pow(1 + rr, -nn));
}
function mp2() {
  var o = $("mp2-out"); var l = _n("mp2-l"), r = _n("mp2-r"), pts = _n("mp2-p"), cut = _n("mp2-c"), y = _n("mp2-y");
  if (!o) return;
  if (l === null || l <= 0) { o.innerHTML = "Enter the loan amount."; return; }
  if (r === null || r <= 0 || y === null || y <= 0) { o.innerHTML = "Enter the base rate and loan term."; return; }
  if (pts === null) pts = 0; if (cut === null) cut = 0;
  var cost = l * pts / 100, newRate = Math.max(0.1, r - cut);
  var base = mp2pmt(l, r, y), after = mp2pmt(l, newRate, y), save = base - after;
  var be = save > 0 ? cost / save : null;
  o.innerHTML = "<b>" + (be !== null ? nfmt(be, 1) + " months" : "never") + "</b>to break even on " + nfmt(pts, 2) + " point(s) costing " + m7Money(cost) +
    "<span class='jf-chip'><b>" + m7Money(base) + "</b>monthly payment at " + nfmt(r, 2) + "%</span>" +
    "<span class='jf-chip'><b>" + m7Money(after) + "</b>after the cut to " + nfmt(newRate, 2) + "%</span>" +
    "<span class='jf-chip'><b>" + m7Money(save) + "</b>saved per month</span>" +
    "<span class='jf-chip'><b>" + (save > 0 ? m7Money(save * y * 12 - cost) : "\u2014") + "</b>net saving if you keep the loan " + nfmt(y, 0) + " years</span>" +
    (be !== null && be > y * 12 ? "<span class='jf-chip jf-chip-bad'>Break-even outlives the loan term \u2014 points cannot win here</span>" : "");
}

function fr3() {
  var o = $("fr3-out"); var t = _n("fr3-i"), e = _n("fr3-e"), b = _n("fr3-b"), h = _n("fr3-h"), w = _n("fr3-w");
  if (!o) return;
  if (t === null) { o.innerHTML = "Enter the target income."; return; }
  if (e === null) e = 0;
  if (b === null || b <= 0 || b > 100) { o.innerHTML = "Enter the billable share as a percent (1\u2013100)."; return; }
  if (h === null || h <= 0 || w === null || w <= 0) { o.innerHTML = "Enter hours per week and working weeks per year."; return; }
  var bill = h * (b / 100) * w, rate = (t + e) / bill;
  o.innerHTML = "<b>" + m7Money(rate) + " /hour</b>charges out a " + m7Money(t) + " income with " + m7Money(e) + " expenses" +
    "<span class='jf-chip'><b>" + nfmt(bill, 0) + " h</b>billable hours per year at " + nfmt(b, 0) + "% of " + nfmt(h, 0) + "\u00d7" + nfmt(w, 0) + "</span>" +
    "<span class='jf-chip'><b>" + m7Money(rate * h) + "</b>per full week</span>" +
    "<span class='jf-chip'><b>" + m7Money(rate * 8) + "</b>per 8-hour day</span>" +
    "<span class='jf-chip'><b>" + m7Money((t + e) / w) + "</b>per week all-in \u2014 the number to actually invoice</span>";
}

/* --- M14 calculators --- */
function pi2() {
  var o = $("pi2-out"); var w = _n("pi2-w"); var g = parseFloat(_v("pi2-g"));
  if (!o) return;
  if (w === null || w <= 0) { o.innerHTML = "Enter your weight in kilograms."; return; }
  var target = w * g, lb = target / 2.20462;
  o.innerHTML = "<b>" + nfmt(target, 0) + " g</b>of protein a day at " + nfmt(g, 1) + " g per kg of bodyweight" +
    "<span class='jf-chip'><b>" + nfmt(target / 4, 0) + " g</b>across four meals, per meal</span>" +
    "<span class='jf-chip'><b>" + nfmt(g / 2.20462, 2) + " g</b>that goal per pound of bodyweight</span>" +
    "<span class='jf-chip'><b>" + nfmt(w * 2.2, 0) + " g cap</b>the 2.2 g/kg ceiling evidence sees no benefit past</span>" +
    (g >= 2.0 ? "<span class='jf-chip jf-chip-bad'>Aggressive-cut zone \u2014 keep protein high and train hard, or lean mass pays</span>" : "");
}

function wt2() {
  var o = $("wt2-out"); var wa = _n("wt2-w"), h = _n("wt2-h");
  if (!o) return;
  if (wa === null || wa <= 0 || h === null || h <= 0) { o.innerHTML = "Enter waist and height, both in centimetres."; return; }
  var rat = wa / h, band = rat < 0.4 ? "slim \u2014 check you are not underweight" : rat < 0.5 ? "healthy \u2014 keep doing what works" : rat < 0.6 ? "increased risk \u2014 central fat matters here" : "high risk \u2014 worth a doctor conversation";
  var beat = h * 0.5;
  o.innerHTML = "<b>" + nfmt(rat, 2) + "</b>waist-to-height ratio \u2014 " + band +
    "<span class='jf-chip'><b>" + nfmt(beat, 1) + " cm</b>the exact 0.50 line for your height</span>" +
    "<span class='jf-chip'><b>" + nfmt(h * 0.49, 1) + " cm</b>waist ceiling that keeps you in the healthy band</span>" +
    (rat >= 0.5 ? "<span class='jf-chip jf-chip-bad'>At or past 0.5 \u2014 the band cardiologists flag first</span>" : "");
}

function sc3() {
  var o = $("sc3-out"); var s = _n("sc3-s"), st = _n("sc3-st"), w = _n("sc3-w");
  if (!o) return;
  if (s === null || s <= 0) { o.innerHTML = "Enter the step count (more than zero)."; return; }
  if (st === null || st <= 0) st = 0.7;
  if (w === null || w <= 0) w = 70;
  var km = s * st / 1000, cal = km * w * 0.53;
  o.innerHTML = "<b>" + nfmt(km, 2) + " km</b>walked for <b>" + nfmt(cal, 0) + " calories</b>" +
    "<span class='jf-chip'><b>" + nfmt(km * 0.621371, 2) + " miles</b>same distance</span>" +
    "<span class='jf-chip'><b>" + nfmt(s / 10000 * 100, 0) + "%</b>of the 10,000-step benchmark</span>" +
    "<span class='jf-chip'><b>" + nfmt(cal / 9, 0) + " g</b>of fat-equivalent energy, at 9 kcal/g</span>" +
    (s >= 10000 ? "<span class='jf-chip'><b>benchmark beaten</b>the whole 10k is in the bank</span>" : "<span class='jf-chip'><b>" + nfmt(Math.ceil((10000 - s) * st / 1000 * w * 0.53), 0) + " kcal</b>still to earn past this point</span>");
}

function pk2() {
  var o = $("pk2-out"); var c = _n("pk2-c"), y = _n("pk2-y");
  if (!o) return;
  if (c === null || c <= 0 || y === null || y <= 0) { o.innerHTML = "Enter cigarettes per day and years smoked, both more than zero."; return; }
  var py = c / 20 * y;
  o.innerHTML = "<b>" + nfmt(py, 1) + " pack-years</b>(" + nfmt(c, 0) + " cigarettes/day \u00d7 " + nfmt(y, 0) + " years)" +
    "<span class='jf-chip'><b>" + nfmt(c / 20, 2) + "+ packs</b>daily pack-equivalent</span>" +
    "<span class='jf-chip'><b>" + nfmt(20 / (c / 20), 1) + " yrs</b>to reach the 20 pack-years screening line at this rate</span>" +
    (py >= 20 ? "<span class='jf-chip jf-chip-bad'>At or past 20 pack-years \u2014 screen eligibility now worth discussing</span>" : "");
}

function bp2() {
  var o = $("bp2-out"); var s = _n("bp2-s"), d = _n("bp2-d");
  if (!o) return;
  if (s === null || d === null || s < 40 || d < 20) { o.innerHTML = "Enter the systolic and diastolic readings in mmHg."; return; }
  var band, cls = "";
  if (s > 180 || d > 120) { band = "Hypertensive crisis \u2014 seek care now"; cls = " jf-chip-bad"; }
  else if (s >= 140 || d >= 90) band = "Stage 2 high blood pressure";
  else if (s >= 130 || d >= 80) band = "Stage 1 high blood pressure";
  else if (s >= 120) band = "Elevated";
  else band = "Normal";
  o.innerHTML = "<b>" + nfmt(s, 0) + "/" + nfmt(d, 0) + "</b>reads <b>" + band + "</b> under current clinic bands" +
    "<span class='jf-chip" + cls + "'><b>" + nfmt(s - d, 0) + "</b>pulse pressure (systolic minus diastolic; watch past 40)</span>" +
    "<span class='jf-chip'><b>stricter wins</b>either number alone raises the band</span>" +
    (s > 180 || d > 120 ? "<span class='jf-chip jf-chip-bad'>Crisis zone \u2014 screen again in 5 minutes, call the clinic</span>" : "");
}

function dl3() {
  var o = $("dl3-out"); var a = _v("dl3-a"), b = _v("dl3-b");
  if (!o) return;
  if (!a || !b) { o.innerHTML = "Pick both dates \u2014 the start and the deadline."; return; }
  var s = new Date(a + "T00:00:00"), e = new Date(b + "T00:00:00");
  if (isNaN(s) || isNaN(e)) { o.innerHTML = "Those dates did not parse \u2014 use the pickers."; return; }
  var days = Math.round((e - s) / 86400000);
  if (days < 0) { o.innerHTML = "The deadline is before the start date \u2014 " + nfmt(-days, 0) + " days already past."; return; }
  var wd = 0, p = new Date(s);
  p.setDate(p.getDate() + 1);
  for (var i = 0; i < days && i < 4000; i++) { var dow = p.getDay(); if (dow !== 0 && dow !== 6) wd++; p.setDate(p.getDate() + 1); }
  o.innerHTML = "<b>" + nfmt(days, 0) + " days</b> until " + e.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" }) +
    "<span class='jf-chip'><b>" + nfmt(wd, 0) + " working days</b>weekends excluded from the count</span>" +
    "<span class='jf-chip'><b>" + nfmt(days / 7, 1) + " weeks</b>calendar span</span>" +
    "<span class='jf-chip'><b>" + nfmt(wd > 0 ? days / wd : 0, 2) + "\u00d7</b>each working day stretches in calendar cover</span>" +
    (days === 0 ? "<span class='jf-chip jf-chip-bad'>That is today \u2014 the deadline is now</span>" : "");
}

function su2() {
  var o = $("su2-out"); var dv = _v("su2-d"), lat = _n("su2-lat"), lon = _n("su2-lon"), tz = parseFloat(_v("su2-tz"));
  if (!o) return;
  if (!dv) { o.innerHTML = "Pick a date first."; return; }
  if (lat === null || lon === null || Math.abs(lat) > 89.9) { o.innerHTML = "Enter a latitude (\u00b1 90) and longitude."; return; }
  var p = dv.split("-"), yy = parseInt(p[0], 10), mm = parseInt(p[1], 10), dd = parseInt(p[2], 10);
  var N = Math.round((Date.UTC(yy, mm - 1, dd) - Date.UTC(yy, 0, 1)) / 86400000) + 1;
  var la = lat * Math.PI / 180, zn = 90.833, lng = lon / 15;
  function su2_event(rise) {
    var t = N + ((rise ? 6 : 18) - lng) / 24;
    var M = 0.9856 * t - 3.289;
    var L = (M + 1.916 * Math.sin(M * Math.PI / 180) + 0.020 * Math.sin(2 * M * Math.PI / 180) + 282.634); L = ((L % 360) + 360) % 360;
    var RA = Math.atan(0.91764 * Math.tan(L * Math.PI / 180)) * 180 / Math.PI; RA = ((RA % 360) + 360) % 360;
    RA = (RA + (Math.floor(L / 90) * 90 - Math.floor(RA / 90) * 90)) / 15;
    var sd = 0.39782 * Math.sin(L * Math.PI / 180), cd = Math.cos(Math.asin(sd));
    var cosH = (Math.cos(zn * Math.PI / 180) - sd * Math.sin(la)) / (cd * Math.cos(la));
    if (cosH > 1) return { polar: "night" }; if (cosH < -1) return { polar: "day" };
    var H = (rise ? 360 - Math.acos(cosH) * 180 / Math.PI : Math.acos(cosH) * 180 / Math.PI) / 15;
    var T = H + RA - 0.06571 * t - 6.622;
    var UT = (((T - lng) % 24) + 24) % 24;
    return { h: ((UT + tz) % 24 + 24) % 24 };
  }
  function fm(x) { var h = Math.floor(x), m = Math.round((x - h) * 60); if (m === 60) { h = (h + 1) % 24; m = 0; } return h + ":" + String(m).padStart(2, "0"); }
  var re = su2_event(true), se = su2_event(false);
  if (re.polar || se.polar) { o.innerHTML = re.polar === "day" || se.polar === "day" ? "The sun stays above the horizon all day at this latitude and date \u2014 polar day." : "Polar night \u2014 the sun never rises here on this date."; return; }
  var dl = (se.h - re.h + 24) % 24, dlm = Math.round(dl * 60);
  o.innerHTML = "<b>Sunrise " + fm(re.h) + "</b> \u00b7 <b>Sunset " + fm(se.h) + "</b> local (UTC" + (tz >= 0 ? "+" : "") + (tz % 1 === 0 ? tz : tz) + ")" +
    "<span class='jf-chip'><b>" + Math.floor(dlm / 60) + " h " + dlm % 60 + " m</b>of daylight</span>" +
    "<span class='jf-chip'><b>" + nfmt(N, 0) + "</b>day of year</span>" +
    "<span class='jf-chip'><b>" + nfmt(dl * 15, 1) + "\u00b0</b>of sky the sun swings through</span>";
}
function jd2() {
  var o = $("jd2-out"); var d = _v("jd2-d");
  if (!o) return;
  if (!d) { o.innerHTML = "Pick a date first."; return; }
  var p = d.split("-"), jd = Date.UTC(parseInt(p[0], 10), parseInt(p[1], 10) - 1, parseInt(p[2], 10), 12) / 86400000 + 2440587.5;
  var mjd = jd - 2400000.5, doy = Math.round((Date.UTC(parseInt(p[0], 10), parseInt(p[1], 10) - 1, parseInt(p[2], 10)) - Date.UTC(parseInt(p[0], 10), 0, 1)) / 86400000) + 1;
  o.innerHTML = "<b>JDN " + nfmt(jd, 0) + "</b> for " + d + " (noon UTC)" +
    "<span class='jf-chip'><b>" + nfmt(mjd, 1) + "</b>Modified Julian Date (JDN \u2212 2400000.5)</span>" +
    "<span class='jf-chip'><b>" + nfmt(doy, 0) + "</b>fractional-day day of year</span>" +
    "<span class='jf-chip'><b>12:00 UTC</b>noon is where the JD integer turns over</span>";
}

function mn3() {
  var o = $("mn3-out"); var raw = _v("mn3-in");
  if (!o) return;
  var toks = raw.split(/[\s,;]+/), lines = [], total = 0, ok = 0;
  for (var i = 0; i < toks.length; i++) {
    if (!toks[i]) continue;
    var m = parseFloat(toks[i]);
    if (isNaN(m) || m < 0) { lines.push("<span class='jf-chip jf-chip-bad'>skipped " + escHtml(toks[i]) + "</span>"); continue; }
    var hrs = Math.floor(m / 60), mm = Math.round(m - hrs * 60);
    lines.push(nfmt(m, 2) + " min \u2192 <b>" + nfmt(m / 60, 2) + " h</b> = " + hrs + ":" + String(mm).padStart(2, "0"));
    total += m; ok++;
  }
  if (!ok) { o.innerHTML = "Enter one or more minute amounts \u2014 separated by spaces, commas or new lines."; return; }
  o.innerHTML = "<b>" + nfmt(total / 60, 2) + " h</b> combined from " + ok + " value(s)<div style='margin-top:6px;line-height:1.7'>" + lines.join("<br>") + "</div>";
}

function pd2() {
  var o = $("pd2-out"); var l = _v("pd2-l");
  if (!o) return;
  if (!l) { o.innerHTML = "Pick the first day of the last period."; return; }
  var s = new Date(l + "T00:00:00");
  if (isNaN(s)) { o.innerHTML = "That date did not parse \u2014 use the picker."; return; }
  var due = new Date(s.getTime() + 280 * 86400000);
  var t2 = new Date(s.getTime() + 91 * 86400000), t3 = new Date(s.getTime() + 196 * 86400000);
  var now = Date.now(), wk = Math.floor((now - s.getTime()) / (7 * 86400000)), dd = Math.ceil((due.getTime() - now) / 86400000);
  o.innerHTML = "<b>" + dISO(due) + "</b>estimated due date from an LMP of " + l +
    "<span class='jf-chip'><b>week " + nfmt(Math.max(0, wk), 0) + "</b>gestational age today" + (wk >= 0 && dd >= 0 ? " (" + nfmt(dd, 0) + " days to go)" : wk < 0 ? "" : "") + "</span>" +
    "<span class='jf-chip'><b>" + dISO(t2) + "</b>trimester II opens (LMP + 91 d)</span>" +
    "<span class='jf-chip'><b>" + dISO(t3) + "</b>trimester III opens (LMP + 196 d)</span>" +
    "<span class='jf-chip'><b>4-week window</b>babies arrive 37\u201342 weeks; scans refine earliest</span>";
}

var PL3_P = [["Mercury", 0.2408467], ["Venus", 0.61519726], ["Mars", 1.8808158], ["Jupiter", 11.862615], ["Saturn", 29.447498], ["Uranus", 84.016846], ["Neptune", 164.79132]];
function pl3() {
  var o = $("pl3-out"); var a = _n("pl3-a");
  if (!o) return;
  if (a === null || a <= 0) { o.innerHTML = "Enter your Earth age in years."; return; }
  var chips = "";
  for (var i = 0; i < PL3_P.length; i++) chips += "<span class='jf-chip'><b>" + nfmt(a / PL3_P[i][1], 2) + "</b>" + PL3_P[i][0] + " years</span>";
  o.innerHTML = "<b>" + nfmt(a / PL3_P[0][1], 2) + "+</b>solar birthdays logged on Mercury \u2014 all seven planets at once below" + chips;
}

function qs2() {
  var o = $("qs2-out"); var c = _n("qs2-c"), t = _n("qs2-t");
  if (!o) return;
  if (t === null || t <= 0) { o.innerHTML = "Enter the total number of questions."; return; }
  if (c === null || c < 0) { o.innerHTML = "Enter the number of correct answers (0 or more)."; return; }
  if (c > t) { o.innerHTML = "More correct answers than questions \u2014 check the totals."; return; }
  var pct = c / t * 100, g = pct >= 90 ? "A" : pct >= 80 ? "B" : pct >= 70 ? "C" : pct >= 60 ? "D" : "F";
  o.innerHTML = "<b>" + nfmt(pct, 1) + "%</b>&nbsp;\u2192 grade <b>" + g + "</b>" +
    "<span class='jf-chip'><b>" + nfmt(100 / t, 1) + "%</b>each question is worth</span>" +
    "<span class='jf-chip'><b>" + nfmt(t - c, 0) + "</b>missed</span>" +
    (g !== "A" ? "<span class='jf-chip'><b>" + nfmt(Math.ceil(t * (g === "B" ? 0.9 : g === "C" ? 0.8 : g === "D" ? 0.7 : 0.6) - c), 0) + " more</b>correct answers to reach the next band</span>" : "<span class='jf-chip'><b>top band</b>nothing left to climb</span>");
}

/* --- M15 converter engines --- */
var PC2_F = { kPa: 1, psi: 6.894757, bar: 100, atm: 101.325, mmHg: 0.133322387415, MPa: 1000 };
function pc2() {
  var o = $("pc2-out"); var v = _n("pc2-v"); var u = _v("pc2-u");
  if (!o) return;
  if (v === null || v < 0) { o.innerHTML = "Enter a non-negative pressure value."; return; }
  var kpa = v * PC2_F[u], names = { kPa: "kilopascals", psi: "pounds/sq inch", bar: "bar", atm: "atmospheres", mmHg: "mmHg (torr)", MPa: "megapascals" };
  var chips = "", d = { kPa: 2, psi: 2, bar: 3, atm: 4, mmHg: 1, MPa: 4 };
  for (var k in PC2_F) if (k !== u) chips += "<span class='jf-chip'><b>" + nfmt(kpa / PC2_F[k], d[k]) + "</b>" + names[k] + "</span>";
  o.innerHTML = "<b>" + nfmt(kpa, 2) + " kPa</b>= " + nfmt(v, 2) + " " + names[u] + chips;
}

var EN2_F = { J: 1, kJ: 1e3, Wh: 3600, kWh: 3.6e6, cal: 4.184, kcal: 4184, BTU: 1055.06 };
function en2() {
  var o = $("en2-out"); var v = _n("en2-v"); var u = _v("en2-u");
  if (!o) return;
  if (v === null || v < 0) { o.innerHTML = "Enter a non-negative energy value."; return; }
  var j = v * EN2_F[u], names = { J: "joules", kJ: "kilojoules", Wh: "watt-hours", kWh: "kilowatt-hours", cal: "small calories", kcal: "food Calories", BTU: "BTU" };
  var d = { J: 0, kJ: 2, Wh: 1, kWh: 3, cal: 0, kcal: 2, BTU: 1 };
  var chips = "";
  for (var k in EN2_F) if (k !== u) chips += "<span class='jf-chip'><b>" + nfmt(j / EN2_F[k], d[k]) + "</b>" + names[k] + "</span>";
  o.innerHTML = "<b>" + nfmt(j / EN2_F[u], d[u]) + " " + names[u] + "</b>&nbsp;= " + nfmt(j, 0) + " J" + chips;
}

var PW3_F = { W: 1, kW: 1e3, hp: 745.699872, ps: 735.49875, btuh: 0.29307107 };
function pw3() {
  var o = $("pw3-out"); var v = _n("pw3-v"); var u = _v("pw3-u");
  if (!o) return;
  if (v === null || v < 0) { o.innerHTML = "Enter a non-negative power value."; return; }
  var w = v * PW3_F[u], names = { W: "watts", kW: "kilowatts", hp: "mechanical hp", ps: "metric PS", btuh: "BTU/hour" };
  var d = { W: 0, kW: 3, hp: 2, ps: 2, btuh: 0 };
  var chips = "";
  for (var k in PW3_F) if (k !== u) chips += "<span class='jf-chip'><b>" + nfmt(w / PW3_F[k], d[k]) + "</b>" + names[k] + "</span>";
  o.innerHTML = "<b>" + nfmt(w / PW3_F[u], d[u]) + " " + names[u] + "</b>&nbsp;= " + nfmt(w, 0) + " W" + chips +
    "<span class='jf-chip'><b>745.70 vs 735.50 W</b>mechanical vs metric horsepower \u2014 not the same number</span>";
}

var FC2_F = { N: 1, kN: 1e3, lbf: 4.4482216152605, kgf: 9.80665, dyn: 1e-5 };
function fc2() {
  var o = $("fc2-out"); var v = _n("fc2-v"); var u = _v("fc2-u");
  if (!o) return;
  if (v === null) { o.innerHTML = "Enter a force value."; return; }
  var n = v * FC2_F[u], names = { N: "newtons", kN: "kilonewtons", lbf: "pounds-force", kgf: "kilograms-force", dyn: "dynes" };
  var d = { N: 1, kN: 4, lbf: 2, kgf: 2, dyn: 0 };
  var chips = "";
  for (var k in FC2_F) if (k !== u) chips += "<span class='jf-chip'><b>" + nfmt(n / FC2_F[k], d[k]) + "</b>" + names[k] + "</span>";
  o.innerHTML = "<b>" + nfmt(n / FC2_F[u], d[u]) + " " + names[u] + "</b>&nbsp;= " + nfmt(n / 9.80665, 2) + " kg of pull on Earth" + chips;
}

var VL2_F = { l: 1, ml: 0.001, m3: 1000, galus: 3.785411784, qtus: 0.946352946, ptus: 0.473176473, cup: 0.24, flozus: 0.0295735295625 };
function vl2() {
  var o = $("vl2-out"); var v = _n("vl2-v"); var u = _v("vl2-u");
  if (!o) return;
  if (v === null || v < 0) { o.innerHTML = "Enter a non-negative volume."; return; }
  var l = v * VL2_F[u], names = { l: "litres", ml: "millilitres", m3: "cubic metres", galus: "US gallons", qtus: "US quarts", ptus: "US pints", cup: "US cups", flozus: "US fl oz" };
  var d = { l: 2, ml: 0, m3: 4, galus: 2, qtus: 2, ptus: 2, cup: 2, flozus: 1 };
  var chips = "";
  for (var k in VL2_F) if (k !== u) chips += "<span class='jf-chip'><b>" + nfmt(l / VL2_F[k], d[k]) + "</b>" + names[k] + "</span>";
  o.innerHTML = "<b>" + nfmt(l / VL2_F[u], d[u]) + " " + names[u] + "</b>" + chips;
}

var MS2_F = { mps: 1, kmh: 1 / 3.6, mph: 0.44704, kn: 0.514444, ftps: 0.3048 };
function ms2() {
  var o = $("ms2-out"); var v = _n("ms2-v"); var u = _v("ms2-u");
  if (!o) return;
  if (v === null || v < 0) { o.innerHTML = "Enter a non-negative speed."; return; }
  var m = v * MS2_F[u], names = { mps: "m/s", kmh: "km/h", mph: "mph", kn: "knots", ftps: "ft/s" };
  var d = { mps: 2, kmh: 2, mph: 2, kn: 2, ftps: 1 };
  var chips = "";
  for (var k in MS2_F) if (k !== u && k !== "mps") chips += "<span class='jf-chip'><b>" + nfmt(m / MS2_F[k], d[k]) + "</b>" + names[k] + "</span>";
  o.innerHTML = "<b>" + nfmt(m / MS2_F[u], d[u]) + " " + names[u] + "</b>&nbsp;= <b>" + nfmt(m, 2) + " m/s</b>" + chips;
}

function dt3() {
  var o = $("dt3-out"); var s = _n("dt3-s"), su = _v("dt3-su"), sp = _n("dt3-sp");
  if (!o) return;
  if (s === null || s <= 0) { o.innerHTML = "Enter the data size (more than zero)."; return; }
  if (sp === null || sp <= 0) { o.innerHTML = "Enter the connection speed in Mbps (more than zero)."; return; }
  var BY = { GB: 1e9, MB: 1e6, TB: 1e12, KiB: 1073741824 };
  var sec = s * BY[su] * 8 / (sp * 1e6);
  var t = sec < 90 ? Math.round(sec) + " s" : sec < 5400 ? Math.floor(sec / 60) + " min " + Math.round(sec % 60) + " s" : Math.floor(sec / 3600) + " h " + Math.round((sec % 3600) / 60) + " min";
  o.innerHTML = "<b>" + t + "</b>to move " + nfmt(s, 2) + " " + su + " over a " + nfmt(sp, 0) + " Mbps line" +
    "<span class='jf-chip'><b>" + nfmt(sec, 0) + " s</b>raw seconds, bits counted as 8 per byte</span>" +
    "<span class='jf-chip'><b>" + nfmt(sec * 1.15, 0) + " s</b>at a realistic 87% usable throughput</span>" +
    (su === "KiB" ? "<span class='jf-chip'><b>GiB noticed</b>binary size \u2014 7.4% more bits than decimal GB</span>" : "");
}

function cf3() {
  var o = $("cf3-out"); var m = _n("cf3-m"), p = _n("cf3-p"), a = _n("cf3-a"), b = _n("cf3-b");
  if (!o) return;
  if (m === null || m <= 0) { o.innerHTML = "Enter the annual miles driven."; return; }
  if (p === null || p <= 0) { o.innerHTML = "Enter the fuel price per gallon."; return; }
  if (a === null || a <= 0 || b === null || b <= 0) { o.innerHTML = "Enter both cars' fuel economy in mpg."; return; }
  var ga = m / a, gb = m / b, ca = ga * p, cb = gb * p, save = ca - cb;
  o.innerHTML = "<b>" + (save >= 0 ? m7Money(save) : m7Money(-save)) + "/year" + "</b>" + (save >= 0 ? "saved by car B" : "saved by car A") + " on " + nfmt(m, 0) + " miles" +
    "<span class='jf-chip'><b>Car A: " + m7Money(ca) + "</b>" + nfmt(ga, 1) + " gal at " + nfmt(a, 0) + " mpg</span>" +
    "<span class='jf-chip'><b>Car B: " + m7Money(cb) + "</b>" + nfmt(gb, 1) + " gal at " + nfmt(b, 0) + " mpg</span>" +
    "<span class='jf-chip'><b>" + m7Money(Math.abs(save) / 12) + "</b>per month difference</span>" +
    (Math.abs(a - b) < 0.5 ? "<span class='jf-chip jf-chip-bad'>Nearly identical economy \u2014 the price difference is noise</span>" : "");
}

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

/* --- M15 math engines --- */
function pe2() {
  var o = $("pe2-out"); var m = _n("pe2-m"), t = _n("pe2-t");
  if (!o) return;
  if (m === null || t === null) { o.innerHTML = "Enter both the measured and the accepted value."; return; }
  if (t === 0) { o.innerHTML = "Accepted value is zero \u2014 percent error is undefined there; report the absolute difference of " + nfmt(Math.abs(m - t), 4) + " instead."; return; }
  var e = m - t, pct = Math.abs(e) / Math.abs(t) * 100, signed = e / Math.abs(t) * 100;
  o.innerHTML = "<b>" + nfmt(pct, 2) + "%</b>error between measured " + nfmt(m, 4) + " and accepted " + nfmt(t, 4) +
    "<span class='jf-chip'><b>" + nfmt(e, 4) + "</b>signed difference (negative = measured reads low)</span>" +
    "<span class='jf-chip'><b>" + nfmt(pct, 2) + "%</b>magnitude (sign ignored)</span>" +
    (pct <= 5 ? "<span class='jf-chip'><b>within 5%</b>tight by most lab-report standards</span>" : "<span class='jf-chip jf-chip-bad'>Over 5% \u2014 suspect technique or unit slips first</span>");
}

function po2() {
  var o = $("po2-out"); var a = _n("po2-a"), b = _n("po2-b"), c = _n("po2-c");
  if (!o) return;
  if (a === null || b === null || c === null) { o.innerHTML = "Fill in the three known terms a, b and c."; return; }
  if (a === 0) { o.innerHTML = "a is zero \u2014 the proportion a:b :: c:x is undefined; adjust the setup."; return; }
  var x = b * c / a;
  o.innerHTML = "<b>x = " + nfmt(x, 4) + "</b>completing " + nfmt(a, 2) + ":" + nfmt(b, 2) + " :: " + nfmt(c, 2) + ":x" +
    "<span class='jf-chip'><b>" + nfmt(b * c, 4) + "</b>cross product b\u00d7c that a\u00d7x must equal</span>" +
    "<span class='jf-chip'><b>" + nfmt(x * a, 4) + "</b>a\u00d7x \u2014 equal, so the proportion holds</span>" +
    "<span class='jf-chip'><b>" + nfmt(b / a, 4) + "</b>shared scale factor that both pairs keep</span>";
}

function rm2() {
  var o = $("rm2-out"); var a = _n("rm2-a"), b = _n("rm2-b");
  if (!o) return;
  if (a === null || b === null) { o.innerHTML = "Enter the dividend and the divisor."; return; }
  if (b === 0) { o.innerHTML = "Division by zero \u2014 no quotient or remainder exists."; return; }
  var qT = Math.trunc(a / b), rT = a - qT * b;
  var qE = Math.floor(a / b), rE = a - qE * b;
  o.innerHTML = "<b>" + nfmt(qT, 0) + " remainder " + nfmt(rT, 0) + "</b>for " + nfmt(a, 0) + " \u00f7 " + nfmt(b, 0) +
    "<span class='jf-chip'><b>" + nfmt(a / b, 4) + "</b>decimal quotient</span>" +
    (a < 0 || b < 0 ? "<span class='jf-chip jf-chip-bad'>Negatives detected \u2014 JS-style truncation gives r = " + nfmt(rT, 0) + " with q = " + nfmt(qT, 0) + "; Euclidean (always 0 \u2264 r < |b|) gives q = " + nfmt(qE, 0) + ", r = " + nfmt(rE, 0) + "</span>" : "<span class='jf-chip'><b>both agree</b>for positives, truncated and Euclidean are the same</span>") +
    "<span class='jf-chip'><b>check</b>" + nfmt(qE, 0) + "\u00d7" + nfmt(b, 0) + " + " + nfmt(rE, 0) + " = " + nfmt(qE * b + rE, 0) + "</span>";
}

function le2() {
  var o = $("le2-out"); var a = _n("le2-a"), b = _n("le2-b"), c = _n("le2-c"), d = _n("le2-d");
  if (!o) return;
  if (a === null || b === null || c === null || d === null) { o.innerHTML = "Fill in all four constants of ax + b = cx + d."; return; }
  if (a === c) {
    o.innerHTML = b === d ? "<b>Every x</b> satisfies it \u2014 both sides are the same line." : "<b>No solution</b> \u2014 equal coefficients with different constants means parallel lines that never cross.";
    return;
  }
  var x = (d - b) / (a - c);
  o.innerHTML = "<b>x = " + nfmt(x, 4) + "</b>solves " + nfmt(a, 2) + "x + " + nfmt(b, 2) + " = " + nfmt(c, 2) + "x + " + nfmt(d, 2) +
    "<span class='jf-chip'><b>" + nfmt(a - c, 2) + "x = " + nfmt(d - b, 2) + "</b>rearranged: (a\u2212c)x = d\u2212b</span>" +
    "<span class='jf-chip'><b>" + nfmt(a * x + b, 2) + " = " + nfmt(c * x + d, 2) + "</b>substituted back, both sides agree</span>";
}

function gm2() {
  var o = $("gm2-out"); var raw = _v("gm2-in");
  if (!o) return;
  var toks = raw.split(/[\s,;]+/), vals = [];
  for (var i = 0; i < toks.length; i++) { if (!toks[i]) continue; var v = parseFloat(toks[i]); if (isNaN(v)) { o.innerHTML = "This is not a number: " + escHtml(toks[i]); return; } if (v <= 0) { o.innerHTML = "All values must be positive \u2014 " + escHtml(toks[i]) + " breaks the multiplicative mean."; return; } vals.push(v); }
  if (vals.length < 2) { o.innerHTML = "Give at least two positive numbers."; return; }
  var lg = 0, sum = 0;
  for (var j = 0; j < vals.length; j++) { lg += Math.log(vals[j]); sum += vals[j]; }
  var gm = Math.exp(lg / vals.length), am = sum / vals.length;
  o.innerHTML = "<b>" + nfmt(gm, 4) + "</b>geometric mean of " + vals.length + " values" +
    "<span class='jf-chip'><b>" + nfmt(am, 4) + "</b>arithmetic mean \u2014 always the higher of the two unless values match</span>" +
    "<span class='jf-chip'><b>" + nfmt(am - gm, 4) + "</b>gap the volatility itself costs</span>" +
    (vals.length > 12 ? "<span class='jf-chip'><b>" + vals.length + " values</b>long series handled in log space</span>" : "");
}

function nr2() {
  var o = $("nr2-out"); var x = _n("nr2-x"), n = _n("nr2-n");
  if (!o) return;
  if (x === null || n === null) { o.innerHTML = "Enter the number and the root order."; return; }
  if (!Number.isInteger(n) || n < 2) { o.innerHTML = "The root order n must be a whole number of 2 or more."; return; }
  if (x < 0 && n % 2 === 0) { o.innerHTML = "Even roots of negative numbers are complex \u2014 no real " + (n === 2 ? "square" : n === 3 ? "cube" : n + "th") + " root of " + nfmt(x, 4) + " exists."; return; }
  var res = x < 0 ? -Math.pow(-x, 1 / n) : Math.pow(x, 1 / n);
  o.innerHTML = "<b>" + nfmt(res, 6) + "</b>= " + nfmt(x, 4) + " raised to 1/" + n +
    "<span class='jf-chip'><b>" + (x < 0 ? "odd root" : "positive base") + "</b>real result guaranteed" + (x < 0 ? " \u2014 sign flips with the odd root" : "") + "</span>" +
    "<span class='jf-chip'><b>" + nfmt(Math.pow(res, n), 4) + "</b>raised back to n \u2014 should return your x</span>";
}

/* --- M15 hobby engines --- */
function bk2() {
  var o = $("bk2-out"); var f = _n("bk2-f"), h = _n("bk2-h"), sa = _n("bk2-s"), ye = _n("bk2-y");
  if (!o) return;
  if (f === null || f <= 0) { o.innerHTML = "Enter the flour weight (grams)."; return; }
  if (h === null) h = 65; if (sa === null) sa = 2; if (ye === null) ye = 1;
  var w = f * h / 100, sl = f * sa / 100, yv = f * ye / 100, tot = f + w + sl + yv;
  o.innerHTML = "<b>" + nfmt(tot, 0) + " g</b>total dough at " + nfmt(h, 0) + "% hydration" +
    "<span class='jf-chip'><b>" + nfmt(f, 0) + " g</b>flour = the 100% anchor</span>" +
    "<span class='jf-chip'><b>" + nfmt(w, 0) + " g</b>water (" + nfmt(h, 0) + "%)</span>" +
    "<span class='jf-chip'><b>" + nfmt(sl, 1) + " g</b>salt (" + nfmt(sa, 1) + "%)</span>" +
    "<span class='jf-chip'><b>" + nfmt(yv, 1) + " g</b>yeast (" + nfmt(ye, 1) + "%)</span>" +
    (h > 75 ? "<span class='jf-chip jf-chip-bad'>Above 75% hydration \u2014 sticky dough, wet hands and tightened proofing times</span>" : "");
}

var RS3_T = { chicken: [45, 20, 74], beef: [55, 20, 63], pork: [45, 25, 63], lamb: [60, 25, 57], turkey: [40, 30, 74] };
function rs3() {
  var o = $("rs3-out"); var w = _n("rs3-w"); var k = _v("rs3-m");
  if (!o) return;
  if (w === null || w <= 0) { o.innerHTML = "Enter the roast weight in kilograms."; return; }
  var t = RS3_T[k] || RS3_T.chicken, mins = w * t[0] + t[1];
  var hrs = Math.floor(mins / 60), rf = mins % 60;
  o.innerHTML = "<b>" + mins + " min</b>(" + hrs + " h " + rf + " min) in a preheated oven for " + nfmt(w, 1) + " kg" +
    "<span class='jf-chip'><b>" + t[0] + " min/kg + " + t[1] + "</b>per-kg pace the cut demands</span>" +
    "<span class='jf-chip'><b>" + t[2] + "\u00b0C / " + nfmt(t[2] * 9 / 5 + 32, 0) + "\u00b0F</b>internal pull temperature to watch</span>" +
    "<span class='jf-chip'><b>rest 15\u201320 min</b>juices redistribute while the table is laid</span>";
}

function we2() {
  var o = $("we2-out"); var l = _n("we2-l"), w = _n("we2-w"), h = _n("we2-h"), rl = _n("we2-r"), wa = parseFloat(_v("we2-wa"));
  if (!o) return;
  if (l === null || l <= 0 || w === null || w <= 0 || h === null || h <= 0) { o.innerHTML = "Enter the room length, width and height."; return; }
  if (rl === null || rl <= 0) rl = 10;
  if (isNaN(wa)) wa = 0;
  var rollW = 0.53, area = 2 * (l + w) * h, rollArea = rl * rollW;
  var rolls = Math.ceil(area * (1 + wa / 100) / rollArea);
  o.innerHTML = "<b>" + rolls + " rolls</b>cover a " + nfmt(l, 1) + "\u00d7" + nfmt(w, 1) + " m room at " + nfmt(h, 2) + " m high" +
    "<span class='jf-chip'><b>" + nfmt(area, 1) + " m\u00b2</b>total wall area (perimeter \u00d7 height)</span>" +
    "<span class='jf-chip'><b>" + nfmt(rollArea, 1) + " m\u00b2</b>per " + nfmt(rl, 0) + " m roll at 0.53 m wide</span>" +
    (wa > 0 ? "<span class='jf-chip'><b>+" + wa + "% margin</b>pattern matching eats offcuts \u2014 priced in</span>" : "<span class='jf-chip'><b>plain pattern</b>waste factor zero</span>") +
    "<span class='jf-chip'><b>one dye lot</b>buy every roll in the same purchase</span>";
}

function lp2() {
  var o = $("lp2-out"); var a = _n("lp2-a"), d = _n("lp2-d"), bag = _n("lp2-b"), t = _n("lp2-t");
  if (!o) return;
  if (a === null || a <= 0) { o.innerHTML = "Enter the area to cover (m\u00b2)."; return; }
  if (d === null || d <= 0) { o.innerHTML = "Enter the spreading depth (cm)."; return; }
  if (bag === null || bag <= 0) bag = 30;
  if (t === null || t <= 0) t = 1.5;
  var vol = a * d / 100, bags = Math.ceil(vol * 1000 / bag), tonnes = vol * t;
  o.innerHTML = "<b>" + bags + " bags</b> (" + nfmt(bag, 0) + " L each) or <b>" + nfmt(tonnes, 2) + " tonnes</b> loose for " + nfmt(a, 1) + " m\u00b2 at " + nfmt(d, 0) + " cm" +
    "<span class='jf-chip'><b>" + nfmt(vol, 2) + " m\u00b3</b>volume: area \u00d7 depth in metres</span>" +
    "<span class='jf-chip'><b>" + nfmt(t, 2) + " t/m\u00b3</b>density assumed for the tonnage</span>" +
    "<span class='jf-chip'><b>+10% wise</b>settle loses depth after the first rain</span>";
}

/* wire every batch-28 engine into the shared M3 finisher */
["ay2", "vg2", "ci3", "ra3", "ie2", "sl3", "va2", "dn2", "mp2", "fr3", "pi2", "wt2", "sc3", "pk2", "bp2", "dl3", "su2", "jd2", "mn3", "pd2", "pl3", "qs2", "pc2", "en2", "pw3", "fc2", "vl2", "ms2", "dt3", "cf3", "un2", "np2", "st5", "dw2", "vo2", "ch3", "as2", "hs2", "ma2", "sv2", "jq2", "ua2", "al2", "pe2", "po2", "rm2", "le2", "gm2", "nr2", "bk2", "rs3", "we2", "lp2"].forEach(function (fn) {
  var orig = null;
  try { orig = window[fn] || eval(fn); } catch (e) { orig = null; }
  if (typeof orig !== "function") return;
  window[fn] = function () { orig(); m3After(); };
});
/* ===================== END M28 SECTION ===================== */
