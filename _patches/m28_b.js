
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
