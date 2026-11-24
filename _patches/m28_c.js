
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
