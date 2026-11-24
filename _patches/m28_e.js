
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
