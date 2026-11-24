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
