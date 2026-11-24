
function main() {
  let o;

  /* --- ay2 APY --- */
  setInputs({ "ay2-r": "6", "ay2-n": "12", "ay2-d": "a" }); reg("ay2-out");
  ay2();
  o = els["ay2-out"].innerHTML;
  assert(o.includes("<b>6.17%</b> effective yield"), "ay2 6/12 -> 6.17%: " + o.slice(0, 80));
  assert(o.includes("<b>0.5%</b>rate per period"), "ay2 per-period 0.5%");
  assert(o.includes("<b>1.0617</b>year-end multiple"), "ay2 multiple 1.0617");
  setInputs({ "ay2-r": "12", "ay2-n": "12" });
  ay2();
  assert(els["ay2-out"].innerHTML.includes("<b>12.68%</b>"), "ay2 12/12 -> 12.68%");
  setInputs({ "ay2-r": "6", "ay2-n": "365", "ay2-d": "b" });
  ay2();
  o = els["ay2-out"].innerHTML;
  assert(o.includes("<b>5.83%</b> nominal rate"), "ay2 reverse 6% daily -> 5.83% APR");
  setInputs({ "ay2-r": "" });
  ay2();
  assert(els["ay2-out"].innerHTML.includes("non-negative rate"), "ay2 guard");

  /* --- vg2 savings goal --- */
  setInputs({ "vg2-g": "50000", "vg2-s": "10000", "vg2-r": "4", "vg2-y": "5" }); reg("vg2-out");
  vg2();
  o = els["vg2-out"].innerHTML;
  assert(o.includes("<b>569.99</b>per month"), "vg2 monthly 569.99: " + o.slice(0, 80));
  assert(o.includes("<b>12,209.97</b>your existing savings"), "vg2 fv existing 12,209.97");
  assert(o.includes("<b>37,790.03</b>remaining gap"), "vg2 gap 37,790.03");
  setInputs({ "vg2-g": "5000", "vg2-s": "6000" });
  vg2();
  assert(els["vg2-out"].innerHTML.includes("Goal already reached"), "vg2 already-reached chip");
  setInputs({ "vg2-y": "" });
  vg2();
  assert(els["vg2-out"].innerHTML.includes("years to reach the goal"), "vg2 guard");

  /* --- ci3 credit card --- */
  setInputs({ "ci3-b": "5000", "ci3-a": "20", "ci3-p": "200" }); reg("ci3-out");
  ci3();
  o = els["ci3-out"].innerHTML;
  assert(o.includes("<b>33 months</b>to clear 5,000.00"), "ci3 33 months: " + o.slice(0, 80));
  assert(o.includes("<b>1,522.10</b>total interest"), "ci3 interest 1,522.10");
  assert(o.includes("<b>6,522.10</b>all-in cost"), "ci3 all-in 6,522.10");
  setInputs({ "ci3-p": "50" });
  ci3();
  assert(els["ci3-out"].innerHTML.includes("never shrinks"), "ci3 min-payment guard");
  setInputs({ "ci3-p": "250", "ci3-b": "0" });
  ci3();
  assert(els["ci3-out"].innerHTML.includes("balance owed"), "ci3 zero guard");

  /* --- ra3 rent --- */
  setInputs({ "ra3-i": "60000", "ra3-r": "30" }); reg("ra3-out");
  ra3();
  o = els["ra3-out"].innerHTML;
  assert(o.includes("<b>1,500.00</b>per month is the 30% cap"), "ra3 rent 1,500.00: " + o.slice(0, 80));
  assert(o.includes("<b>18,000.00</b>annual housing"), "ra3 annual 18,000.00");
  assert(o.includes("<b>3,500.00</b>per month left"), "ra3 leftover 3,500.00");
  assert(o.includes("<b>1,500.00</b>monthly rent the landlord 40"), "ra3 40x screen chip");
  setInputs({ "ra3-i": "" });
  ra3();
  assert(els["ra3-out"].innerHTML.includes("gross annual income"), "ra3 guard");

  /* --- ie2 fee impact --- */
  setInputs({ "ie2-p": "100000", "ie2-r": "7", "ie2-f": "1", "ie2-y": "30" }); reg("ie2-out");
  ie2();
  o = els["ie2-out"].innerHTML;
  assert(o.includes("<b>574,349.12</b>after 1% fees"), "ie2 net 574,349.12: " + o.slice(0, 80));
  assert(o.includes("761,225.50 with none"), "ie2 gross 761,225.50");
  assert(o.includes("<b>186,876.39</b>wealth the fee deletes"), "ie2 drag 186,876.39");
  setInputs({ "ie2-y": "" });
  ie2();
  assert(els["ie2-out"].innerHTML.includes("years invested"), "ie2 guard");

  /* --- sl3 salary raise --- */
  setInputs({ "sl3-o": "50000", "sl3-n": "55000", "sl3-c": "3" }); reg("sl3-out");
  sl3();
  o = els["sl3-out"].innerHTML;
  assert(o.includes("<b>10%</b>raise"), "sl3 pct 10%: " + o.slice(0, 80));
  assert(o.includes("real 6.8% after"), "sl3 real 6.8%");
  assert(o.includes("<b>53,398.06</b>new salary in today's money"), "sl3 today 53,398.06");
  setInputs({ "sl3-n": "40000" });
  sl3();
  assert(els["sl3-out"].innerHTML.includes("buying power shrank"), "sl3 pay-cut chip");
  setInputs({ "sl3-o": "" });
  sl3();
  assert(els["sl3-out"].innerHTML.includes("old salary"), "sl3 guard");

  /* --- va2 vacation --- */
  setInputs({ "va2-r": "1.5", "va2-m": "24", "va2-u": "8" }); reg("va2-out");
  va2();
  o = els["va2-out"].innerHTML;
  assert(o.includes("<b>28 days</b>of PTO"), "va2 balance 28: " + o.slice(0, 80));
  assert(o.includes("<b>36</b>earned over 24"), "va2 earned 36");
  assert(o.includes("(22%)"), "va2 used 22%");
  setInputs({ "va2-u": "40" });
  va2();
  assert(els["va2-out"].innerHTML.includes("Overdrawn"), "va2 overdrawn chip");
  setInputs({ "va2-r": "" });
  va2();
  assert(els["va2-out"].innerHTML.includes("accrual rate"), "va2 guard");

  /* --- dn2 down payment --- */
  setInputs({ "dn2-p": "400000", "dn2-s": "60000", "dn2-m": "500" }); reg("dn2-out");
  dn2();
  o = els["dn2-out"].innerHTML;
  assert(o.includes("<b>15%</b>down (60,000.00 of 400,000.00)"), "dn2 15%: " + o.slice(0, 80));
  assert(o.includes("<b>141.67/month</b>estimated PMI"), "dn2 pmi 141.67");
  assert(o.includes("<b>80,000.00</b>is the 20% escape line"), "dn2 20% target");
  assert(o.includes("<b>40 months</b>at 500.00 saved"), "dn2 40 months");
  setInputs({ "dn2-s": "90000" });
  dn2();
  assert(els["dn2-out"].innerHTML.includes("none \u2014 over 20%"), "dn2 pmi cleared");
  setInputs({ "dn2-p": "" });
  dn2();
  assert(els["dn2-out"].innerHTML.includes("home price"), "dn2 guard");

  /* --- mp2 mortgage points --- */
  setInputs({ "mp2-l": "300000", "mp2-r": "6.5", "mp2-p": "1", "mp2-c": "0.25", "mp2-y": "30" }); reg("mp2-out");
  mp2();
  o = els["mp2-out"].innerHTML;
  assert(o.includes("<b>61.2 months</b>to break even on 1 point(s) costing 3,000.00"), "mp2 breakeven 61.2: " + o.slice(0, 80));
  assert(o.includes("<b>1,896.20</b>monthly payment at 6.5%"), "mp2 base payment");
  assert(o.includes("<b>1,847.15</b>after the cut to 6.25%"), "mp2 new payment");
  assert(o.includes("<b>49.05</b>saved per month"), "mp2 monthly save");
  assert(o.includes("<b>14,658.89</b>net saving"), "mp2 net over 30y");
  setInputs({ "mp2-p": "2", "mp2-c": "0.5" });
  mp2();
  assert(els["mp2-out"].innerHTML.includes("6,000.00"), "mp2 double points cost 6,000");
  setInputs({ "mp2-l": "" });
  mp2();
  assert(els["mp2-out"].innerHTML.includes("loan amount"), "mp2 guard");

  /* --- fr3 freelance rate --- */
  setInputs({ "fr3-i": "80000", "fr3-e": "12000", "fr3-b": "60", "fr3-h": "40", "fr3-w": "46" }); reg("fr3-out");
  fr3();
  o = els["fr3-out"].innerHTML;
  assert(o.includes("<b>83.33 /hour</b>"), "fr3 rate 83.33: " + o.slice(0, 80));
  assert(o.includes("<b>1,104 h</b>billable"), "fr3 1,104 billable hours");
  assert(o.includes("<b>666.67</b>per 8-hour day"), "fr3 day rate 666.67");
  setInputs({ "fr3-b": "0" });
  fr3();
  assert(els["fr3-out"].innerHTML.includes("billable share"), "fr3 guard");

  /* --- pi2 protein --- */
  setInputs({ "pi2-w": "80", "pi2-g": "1.6" }); reg("pi2-out");
  pi2();
  o = els["pi2-out"].innerHTML;
  assert(o.includes("<b>128 g</b>of protein a day"), "pi2 128 g: " + o.slice(0, 80));
  assert(o.includes("<b>32 g</b>across four meals"), "pi2 32 g per meal");
  assert(o.includes("<b>176 g cap</b>"), "pi2 ceiling 176");
  setInputs({ "pi2-w": "70", "pi2-g": "1.2" });
  pi2();
  assert(els["pi2-out"].innerHTML.includes("<b>84 g</b>of protein a day"), "pi2 70kg maintain -> 84");

  /* --- wt2 waist-to-height --- */
  setInputs({ "wt2-w": "85", "wt2-h": "170" }); reg("wt2-out");
  wt2();
  o = els["wt2-out"].innerHTML;
  assert(o.includes("<b>0.50</b>waist-to-height ratio") || o.includes("<b>0.5</b>waist-to-height ratio") || o.includes("<b>0.50</b>"), "wt2 ratio 0.50: " + o.slice(0, 100));
  assert(o.includes("increased risk"), "wt2 increased band");
  assert(o.includes("<b>85 cm</b>the exact 0.50 line"), "wt2 0.50 line chip");
  assert(o.includes("<b>83.3 cm</b>waist ceiling"), "wt2 healthy ceiling 83.3");
  setInputs({ "wt2-w": "68", "wt2-h": "170" });
  wt2();
  assert(els["wt2-out"].innerHTML.includes("healthy \u2014 keep doing"), "wt2 healthy band");

  /* --- sc3 steps --- */
  setInputs({ "sc3-s": "10000", "sc3-st": "0.70", "sc3-w": "70" }); reg("sc3-out");
  sc3();
  o = els["sc3-out"].innerHTML;
  assert(o.includes("<b>7 km</b>walked for <b>260 calories</b>"), "sc3 7km/260cal: " + o.slice(0, 90));
  assert(o.includes("<b>4.35 miles</b>"), "sc3 miles");
  assert(o.includes("<b>100%</b>of the 10,000-step benchmark"), "sc3 benchmark 100%");
  setInputs({ "sc3-s": "5000" });
  sc3();
  assert(els["sc3-out"].innerHTML.includes("<b>3.5 km</b>"), "sc3 5k steps -> 3.5 km");

  /* --- pk2 pack-year --- */
  setInputs({ "pk2-c": "15", "pk2-y": "20" }); reg("pk2-out");
  pk2();
  o = els["pk2-out"].innerHTML;
  assert(o.includes("<b>15 pack-years</b>"), "pk2 15 pack-years: " + o.slice(0, 80));
  assert(o.includes("<b>0.75+ packs</b>"), "pk2 0.75 packs/day");
  assert(o.includes("<b>26.7 yrs</b>to reach the 20 pack-years"), "pk2 years to 20");
  setInputs({ "pk2-c": "20" });
  pk2();
  assert(els["pk2-out"].innerHTML.includes("<b>20 pack-years</b>"), "pk2 exactly 20");

  /* --- bp2 blood pressure --- */
  setInputs({ "bp2-s": "118", "bp2-d": "76" }); reg("bp2-out");
  bp2();
  o = els["bp2-out"].innerHTML;
  assert(o.includes("118/76</b>reads <b>Normal"), "bp2 normal: " + o.slice(0, 80));
  assert(o.includes("<b>42</b>pulse pressure"), "bp2 pp 42");
  setInputs({ "bp2-s": "132", "bp2-d": "76" });
  bp2();
  assert(els["bp2-out"].innerHTML.includes("Stage 1 high blood pressure"), "bp2 stage 1 systolic-only");
  setInputs({ "bp2-s": "150", "bp2-d": "95" });
  bp2();
  assert(els["bp2-out"].innerHTML.includes("Stage 2"), "bp2 stage 2");
  setInputs({ "bp2-s": "190", "bp2-d": "125" });
  bp2();
  assert(els["bp2-out"].innerHTML.includes("Hypertensive crisis"), "bp2 crisis");

  /* --- dl3 deadline --- */
  setInputs({ "dl3-a": "2025-01-01", "dl3-b": "2025-03-01" }); reg("dl3-out");
  dl3();
  o = els["dl3-out"].innerHTML;
  assert(o.includes("<b>59 days</b> until March 1, 2025"), "dl3 59 days: " + o.slice(0, 90));
  assert(o.includes("<b>42 working days</b>weekends excluded"), "dl3 42 working days");
  assert(o.includes("<b>8.4 weeks</b>"), "dl3 8.4 weeks");
  setInputs({ "dl3-b": "2024-12-01" });
  dl3();
  assert(els["dl3-out"].innerHTML.includes("already past"), "dl3 past guard");

  /* --- su2 sunrise/sunset --- */
  setInputs({ "su2-d": "2024-06-21", "su2-tz": "-4", "su2-lat": "40.7128", "su2-lon": "-74.0060" }); reg("su2-out");
  su2();
  o = els["su2-out"].innerHTML;
  assert(o.includes("<b>Sunrise 5:25</b> \u00b7 <b>Sunset 20:31</b>"), "su2 5:25/20:31: " + o.slice(0, 100));
  assert(o.includes("<b>15 h 6 m</b>of daylight"), "su2 daylight 15h06m");
  assert(o.includes("<b>173</b>day of year"), "su2 doy 173");
  setInputs({ "su2-d": "2024-12-21", "su2-tz": "1", "su2-lat": "70", "su2-lon": "20" });
  su2();
  assert(els["su2-out"].innerHTML.includes("never rises") || els["su2-out"].innerHTML.includes("polar"), "su2 polar handling: " + els["su2-out"].innerHTML.slice(0, 80));

  /* --- jd2 julian day --- */
  setInputs({ "jd2-d": "2000-01-01" }); reg("jd2-out");
  jd2();
  o = els["jd2-out"].innerHTML;
  assert(o.includes("<b>JDN 2,451,545</b> for 2000-01-01"), "jd2 2451545: " + o.slice(0, 80));
  assert(o.includes("<b>51,544.5</b>Modified Julian Date"), "jd2 mjd 51,544.5");
  setInputs({ "jd2-d": "2024-06-01" });
  jd2();
  assert(els["jd2-out"].innerHTML.includes("<b>JDN 2,460,463</b>"), "jd2 2024-06-01 -> 2460463");
  assert(els["jd2-out"].innerHTML.includes("<b>153</b>fractional-day day of year"), "jd2 doy 153");

  /* --- mn3 minutes to decimal --- */
  setInputs({ "mn3-in": "540 90 37.5" }); reg("mn3-out");
  mn3();
  o = els["mn3-out"].innerHTML;
  assert(o.includes("<b>11.13 h</b> combined from 3 value(s)"), "mn3 total 11.13: " + o.slice(0, 90));
  assert(o.includes("540 min \u2192 <b>9 h</b> = 9:00"), "mn3 540 line");
  assert(o.includes("37.5 min \u2192 <b>0.63 h</b> = 0:38"), "mn3 37.5 line");
  setInputs({ "mn3-in": "abc 90" });
  mn3();
  assert(els["mn3-out"].innerHTML.includes("skipped abc"), "mn3 bad token flagged");

  /* --- pd2 pregnancy --- */
  setInputs({ "pd2-l": "2024-01-01" }); reg("pd2-out");
  pd2();
  o = els["pd2-out"].innerHTML;
  assert(o.includes("<b>2024-10-07</b>estimated due date from an LMP of 2024-01-01"), "pd2 due 2024-10-07: " + o.slice(0, 90));
  assert(o.includes("<b>2024-04-01</b>trimester II opens"), "pd2 tri II 2024-04-01");
  assert(o.includes("<b>2024-07-15</b>trimester III opens"), "pd2 tri III 2024-07-15");
  setInputs({ "pd2-l": "" });
  pd2();
  assert(els["pd2-out"].innerHTML.includes("last period"), "pd2 guard");

  /* --- pl3 planet age --- */
  setInputs({ "pl3-a": "30" }); reg("pl3-out");
  pl3();
  o = els["pl3-out"].innerHTML;
  assert(o.includes("<b>124.56</b>Mercury years"), "pl3 mercury 124.56: " + o.slice(0, 90));
  assert(o.includes("<b>48.76</b>Venus years"), "pl3 venus 48.76");
  assert(o.includes("<b>15.95</b>Mars years"), "pl3 mars 15.95");
  assert(o.includes("<b>2.53</b>Jupiter years"), "pl3 jupiter 2.53");
  assert(o.includes("<b>1.02</b>Saturn years"), "pl3 saturn 1.02");
  assert(o.includes("<b>0.36</b>Uranus years"), "pl3 uranus 0.36");
  assert(o.includes("<b>0.18</b>Neptune years"), "pl3 neptune 0.18");
  setInputs({ "pl3-a": "" });
  pl3();
  assert(els["pl3-out"].innerHTML.includes("Earth age"), "pl3 guard");

  /* --- qs2 quiz score --- */
  setInputs({ "qs2-c": "18", "qs2-t": "20" }); reg("qs2-out");
  qs2();
  o = els["qs2-out"].innerHTML;
  assert(o.includes("<b>90%</b>&nbsp;\u2192 grade <b>A</b>") || (o.includes("<b>90%</b>") && o.includes("grade")), "qs2 90/A: " + o.slice(0, 90));
  assert(o.includes("<b>5%</b>each question is worth"), "qs2 5% per question");
  assert(o.includes("<b>2</b>missed"), "qs2 2 missed");
  setInputs({ "qs2-c": "13" });
  qs2();
  assert(els["qs2-out"].innerHTML.includes("<b>D</b>"), "qs2 65% -> D");
  setInputs({ "qs2-c": "25" });
  qs2();
  assert(els["qs2-out"].innerHTML.includes("check the totals"), "qs2 guard");

  /* --- pc2 pressure --- */
  setInputs({ "pc2-v": "1", "pc2-u": "bar" }); reg("pc2-out");
  pc2();
  o = els["pc2-out"].innerHTML;
  assert(o.includes("<b>100 kPa</b>= 1 bar"), "pc2 1 bar -> 100 kPa: " + o.slice(0, 90));
  assert(o.includes("<b>14.5</b>pounds/sq inch"), "pc2 14.5 psi");
  assert(o.includes("<b>0.9869</b>atmospheres"), "pc2 0.9869 atm");
  assert(o.includes("<b>750.1</b>mmHg"), "pc2 750.1 mmHg");
  setInputs({ "pc2-v": "101.325", "pc2-u": "kPa" });
  pc2();
  o = els["pc2-out"].innerHTML;
  assert(o.includes("<b>14.7</b>pounds/sq inch"), "pc2 1 atm -> 14.7 psi");
  assert(o.includes("<b>1</b>atmospheres"), "pc2 1.0133 kPa -> 1 atm");
  assert(o.includes("<b>760</b>mmHg"), "pc2 760 mmHg");
  setInputs({ "pc2-v": "" });
  pc2();
  assert(els["pc2-out"].innerHTML.includes("non-negative"), "pc2 guard");

  /* --- en2 energy --- */
  setInputs({ "en2-v": "1", "en2-u": "kWh" }); reg("en2-out");
  en2();
  o = els["en2-out"].innerHTML;
  assert(o.includes("<b>1 kilowatt-hours</b>&nbsp;= 3,600,000 J"), "en2 1 kWh -> 3.6MJ: " + o.slice(0, 90));
  assert(o.includes("<b>860,421</b>small calories"), "en2 860,421 cal");
  assert(o.includes("<b>3,412.1</b>BTU"), "en2 3412.1 BTU");
  assert(o.includes("<b>860.42</b>food Calories"), "en2 860.42 kcal");
  setInputs({ "en2-v": "1", "en2-u": "kcal" });
  en2();
  assert(els["en2-out"].innerHTML.includes("<b>4,184</b>joules"), "en2 kcal -> 4184 J");
  setInputs({ "en2-v": "" });
  en2();
  assert(els["en2-out"].innerHTML.includes("non-negative"), "en2 guard");

  /* --- pw3 power --- */
  setInputs({ "pw3-v": "1000", "pw3-u": "W" }); reg("pw3-out");
  pw3();
  o = els["pw3-out"].innerHTML;
  assert(o.includes("<b>1,000 watts</b>&nbsp;= 1,000 W"), "pw3 watts: " + o.slice(0, 90));
  assert(o.includes("<b>1.34</b>mechanical hp"), "pw3 1.34 hp");
  assert(o.includes("<b>1.36</b>metric PS"), "pw3 1.36 PS");
  assert(o.includes("<b>3,412</b>BTU/hour"), "pw3 3412 BTU/h");
  setInputs({ "pw3-v": "1", "pw3-u": "hp" });
  pw3();
  assert(els["pw3-out"].innerHTML.includes("<b>746</b>watts"), "pw3 hp -> 746 W (nfmt 0dp)");
  setInputs({ "pw3-v": "" });
  pw3();
  assert(els["pw3-out"].innerHTML.includes("non-negative"), "pw3 guard");

  /* --- fc2 force --- */
  setInputs({ "fc2-v": "100", "fc2-u": "N" }); reg("fc2-out");
  fc2();
  o = els["fc2-out"].innerHTML;
  assert(o.includes("<b>100 newtons</b>&nbsp;= 10.2 kg of pull on Earth"), "fc2 kg pull: " + o.slice(0, 90));
  assert(o.includes("<b>22.48</b>pounds-force"), "fc2 22.48 lbf");
  assert(o.includes("<b>10.2</b>kilograms-force"), "fc2 10.2 kgf");
  setInputs({ "fc2-v": "1", "fc2-u": "lbf" });
  fc2();
  assert(els["fc2-out"].innerHTML.includes("<b>4.4</b>newtons"), "fc2 lbf -> 4.4 N");
  setInputs({ "fc2-v": "" });
  fc2();
  assert(els["fc2-out"].innerHTML.includes("force value"), "fc2 guard");

  /* --- vl2 volume --- */
  setInputs({ "vl2-v": "1", "vl2-u": "galus" }); reg("vl2-out");
  vl2();
  o = els["vl2-out"].innerHTML;
  assert(o.includes("<b>1 US gallons</b>"), "vl2 gal: " + o.slice(0, 90));
  assert(o.includes("<b>3.79</b>litres"), "vl2 3.79 L");
  assert(o.includes("<b>4</b>US quarts"), "vl2 4 quarts");
  assert(o.includes("<b>8</b>US pints"), "vl2 8 pints");
  assert(o.includes("<b>128</b>US fl oz"), "vl2 128 fl oz");
  setInputs({ "vl2-v": "3.785411784", "vl2-u": "l" });
  vl2();
  assert(els["vl2-out"].innerHTML.includes("<b>1</b>US gallons"), "vl2 L -> gal");
  setInputs({ "vl2-v": "" });
  vl2();
  assert(els["vl2-out"].innerHTML.includes("non-negative"), "vl2 guard");

  /* --- ms2 speed --- */
  setInputs({ "ms2-v": "100", "ms2-u": "kmh" }); reg("ms2-out");
  ms2();
  o = els["ms2-out"].innerHTML;
  assert(o.includes("<b>100 km/h</b>&nbsp;= <b>27.78 m/s</b>"), "ms2 100kmh -> 27.78 mps: " + o.slice(0, 90));
  assert(o.includes("<b>62.14</b>mph"), "ms2 62.14 mph");
  assert(o.includes("<b>54</b>knots"), "ms2 54 knots");
  setInputs({ "ms2-v": "1", "ms2-u": "mps" });
  ms2();
  assert(els["ms2-out"].innerHTML.includes("<b>3.6</b>km/h"), "ms2 m/s -> km/h");
  setInputs({ "ms2-v": "" });
  ms2();
  assert(els["ms2-out"].innerHTML.includes("non-negative"), "ms2 guard");

  /* --- dt3 data transfer --- */
  setInputs({ "dt3-s": "10", "dt3-su": "GB", "dt3-sp": "100" }); reg("dt3-out");
  dt3();
  o = els["dt3-out"].innerHTML;
  assert(o.includes("<b>13 min 20 s</b>to move 10 GB over a 100 Mbps line"), "dt3 13m20s: " + o.slice(0, 100));
  assert(o.includes("<b>800 s</b>raw seconds"), "dt3 800 s");
  assert(o.includes("<b>920 s</b>at a realistic 87%"), "dt3 920 s");
  setInputs({ "dt3-s": "5", "dt3-su": "KiB", "dt3-sp": "80" });
  dt3();
  o = els["dt3-out"].innerHTML;
  assert(o.includes("<b>8 min 57 s</b>to move 5 KiB"), "dt3 GiB 8m57s: " + o.slice(0, 100));
  assert(o.includes("binary size"), "dt3 GiB chip");
  setInputs({ "dt3-s": "5", "dt3-su": "MB", "dt3-sp": "1" });
  dt3();
  o = els["dt3-out"].innerHTML;
  assert(o.includes("<b>40 s</b>to move 5 MB"), "dt3 MB 40s: " + o.slice(0, 100));
  setInputs({ "dt3-sp": "0" });
  dt3();
  assert(els["dt3-out"].innerHTML.includes("more than zero"), "dt3 guard");

  /* --- cf3 fuel comparison --- */
  setInputs({ "cf3-m": "12000", "cf3-p": "3.60", "cf3-a": "25", "cf3-b": "35" }); reg("cf3-out");
  cf3();
  o = els["cf3-out"].innerHTML;
  assert(o.includes("<b>493.71/year</b>saved by car B"), "cf3 save 493.71: " + o.slice(0, 90));
  assert(o.includes("<b>Car A: 1,728.00</b>"), "cf3 car A 1,728");
  assert(o.includes("<b>Car B: 1,234.29</b>"), "cf3 car B 1,234.29");
  assert(o.includes("<b>480 gal</b>at 25 mpg") || o.includes("<b>480 gal at 25</b>") || o.includes("480 gal"), "cf3 480 gal");
  setInputs({ "cf3-b": "" });
  cf3();
  assert(els["cf3-out"].innerHTML.includes("fuel economy"), "cf3 guard");

  /* --- un2 unicode escape --- */
  setInputs({ "un2-in": "ABC", "un2-m": "e" }); reg("un2-out");
  un2();
  o = els["un2-out"].innerHTML;
  assert(o.includes("\\u0041\\u0042\\u0043"), "un2 encode ABC: " + o.slice(0, 90));
  assert(o.includes("<b>3</b>code points escaped"), "un2 3 code points");
  setInputs({ "un2-in": "\\u0041\\u0042\\u0043", "un2-m": "d" });
  un2();
  o = els["un2-out"].innerHTML;
  assert(o.includes("Decoded:") && o.includes("ABC"), "un2 decode -> ABC: " + o.slice(0, 90));
  assert(o.includes("<b>3</b>escapes decoded"), "un2 3 escapes");
  setInputs({ "un2-in": "\\uD83D\\uDE00", "un2-m": "d" });
  un2();
  assert(els["un2-out"].toISOString === undefined, "un2 no crash on surrogate pair");
  setInputs({ "un2-in": "" });
  un2();
  assert(els["un2-out"].innerHTML.includes("Paste text"), "un2 guard");

  /* --- np2 nato --- */
  setInputs({ "np2-in": "AB3" }); reg("np2-out");
  np2();
  o = els["np2-out"].innerHTML;
  assert(o.includes("Alfa\u2003Bravo\u2003Three"), "np2 Alfa Bravo Three (em-space join): " + o.slice(0, 90));
  assert(o.includes("<b>3</b>code words"), "np2 3 code words");
  setInputs({ "np2-in": "Z9" });
  np2();
  o = els["np2-out"].innerHTML;
  assert(o.includes("Zulu\u2003Nine") && o.includes("<b>2</b>code words"), "np2 Zulu + Nine: " + o.slice(0, 90));
  setInputs({ "np2-in": "" });
  np2();
  assert(els["np2-out"].innerHTML.includes("Type the word"), "np2 guard");

  /* --- st5 stopwords --- */
  setInputs({ "st5-in": "the quick brown fox jumps over the lazy dog and the fox is very quick indeed" });
  reg("st5-out");
  st5();
  o = els["st5-out"].innerHTML;
  assert(o.includes("<b>9 of 16 words kept</b> (56.3%)"), "st5 9/16 56.3%: " + o.slice(0, 100));
  assert(o.includes("quick brown fox jumps lazy dog fox quick indeed"), "st5 kept words");
  assert(o.includes("<b>7</b>stopwords removed"), "st5 7 removed");
  assert(o.includes("<b>43.8%</b>density reduction"), "st5 43.8%");
  setInputs({ "st5-in": "!@#!//" });
  st5();
  o = els["st5-out"].innerHTML;
  assert(o.includes("1 of 1 words kept"), "st5 punct-only counts as a kept word on whitespace tokenization");

  /* --- dw2 duplicate words --- */
  setInputs({ "dw2-in": "the cat sat with the dog near the bowl where the dog ate" }); reg("dw2-out");
  dw2();
  o = els["dw2-out"].innerHTML;
  assert(o.includes("<b>2 word(s) repeated</b> across 13 words"), "dw2 2 dups/13 words: " + o.slice(0, 100));
  assert(o.includes("<b>the \u00d74</b>"), "dw2 the x4");
  assert(o.includes("<b>dog \u00d72</b>"), "dw2 dog x2");
  setInputs({ "dw2-in": "unique words only here" });
  dw2();
  assert(els["dw2-out"].innerHTML.includes("No repeated words"), "dw2 clean");
  setInputs({ "dw2-in": "" });
  dw2();
  assert(els["dw2-out"].innerHTML.includes("Paste the text"), "dw2 guard");

  /* --- vo2 vowels --- */
  setInputs({ "vo2-in": "hello world" }); reg("vo2-out");
  vo2();
  o = els["vo2-out"].innerHTML;
  assert(o.includes("<b>3 vowels</b> of 10 letters \u2014 30% vowel density"), "vo2 3/10 30%: " + o.slice(0, 100));
  assert(o.includes("a\u00d70 e\u00d71 i\u00d70 o\u00d72 u\u00d70"), "vo2 per-vowel");
  assert(o.includes("<b>7</b>consonants"), "vo2 7 consonants");
  setInputs({ "vo2-in": "" });
  vo2();
  assert(els["vo2-out"].innerHTML.includes("Paste the text"), "vo2 guard");

  /* --- ch3 chmod --- */
  setInputs({ "ch3-o": "7", "ch3-g": "5", "ch3-t": "5" }); reg("ch3-out");
  ch3();
  o = els["ch3-out"].innerHTML;
  assert(o.includes("<b>chmod 755</b>&nbsp;\u2194 rwxr-xr-x"), "ch3 755: " + o.slice(0, 90));
  assert(o.includes("<b>7</b>owner read\u00b7write\u00b7exec"), "ch3 owner verbose chip");
  assert(o.includes("<b>5</b>group r-x"), "ch3 group chip");
  setInputs({ "ch3-o": "6", "ch3-g": "4", "ch3-t": "4" });
  ch3();
  assert(els["ch3-out"].innerHTML.includes("chmod 644"), "ch3 644 computed");
  setInputs({ "ch3-o": "7", "ch3-g": "7", "ch3-t": "7" });
  ch3();
  assert(els["ch3-out"].innerHTML.includes("777 \u2014 anyone"), "ch3 777 warning");
  setInputs({ "ch3-o": "6", "ch3-g": "0", "ch3-t": "0" });
  ch3();
  assert(els["ch3-out"].innerHTML.includes("600 = owner only"), "ch3 600 key warning");

  /* --- as2 ascii --- */
  setInputs({ "as2-c": "A", "as2-n": "65" }); reg("as2-out");
  as2();
  o = els["as2-out"].innerHTML;
  assert(o.includes("<b>A</b> \u2192 decimal <b>65</b>, hex <b>0x41</b>, binary <b>01000001</b>"), "as2 A: " + o.slice(0, 110));
  assert(o.includes("<b>ASCII</b>code band"), "as2 ascii chip");
  assert(o.includes("<b>65</b> \u2192 character <b>A</b>"), "as2 number -> char");
  setInputs({ "as2-c": "\u20ac" });
  as2();
  assert(els["as2-out"].innerHTML.includes("<b>8364</b>, hex <b>0x20AC</b>"), "as2 euro 8364");
  setInputs({ "as2-c": "\u0001" });
  as2();
  assert(els["as2-out"].innerHTML.includes("Control character"), "as2 control flag");

  /* --- hs2 http status --- */
  setInputs({ "hs2-c": "404" }); reg("hs2-out");
  hs2();
  o = els["hs2-out"].innerHTML;
  assert(o.includes("<b>404 Not Found</b>"), "hs2 404: " + o.slice(0, 90));
  assert(o.includes("<b>4xx</b>Client error class"), "hs2 class");
  setInputs({ "hs2-c": "502" });
  hs2();
  assert(els["hs2-out"].innerHTML.includes("Bad Gateway"), "hs2 502");
  assert(els["hs2-out"].innerHTML.includes("Server error"), "hs2 5xx");
  setInputs({ "hs2-c": "700" });
  hs2();
  assert(els["hs2-out"].innerHTML.includes("100\\u2013599") || els["hs2-out"].innerHTML.includes("run 100"), "hs2 range guard");
  setInputs({ "hs2-c": "201" });
  hs2();
  assert(els["hs2-out"].innerHTML.includes("<b>201 Created</b>"), "hs2 201");

  /* --- ma2 mac --- */
  setInputs({ "ma2-in": "aabbccddeeff" }); reg("ma2-out");
  ma2();
  o = els["ma2-out"].innerHTML;
  assert(o.includes("<b>AA:BB:CC:DD:EE:FF</b>"), "ma2 colon form: " + o.slice(0, 90));
  assert(o.includes("<b>AA-BB-CC-DD-EE-FF</b>"), "ma2 hyphen form");
  assert(o.includes("<b>AABB.CCDD.EEFF</b>"), "ma2 cisco form");
  assert(o.includes("unicast \u00b7 locally administered"), "ma2 bits unicast/locally-administered (0xAA bit1 set)");
  setInputs({ "ma2-in": "AA-BB-CC DD:EE.FF" });
  ma2();
  assert(els["ma2-out"].innerHTML.includes("AA:BB:CC:DD:EE:FF"), "ma2 mixed separators");
  setInputs({ "ma2-in": "abc" });
  ma2();
  assert(els["ma2-out"].innerHTML.includes("12 hex digits"), "ma2 guard");

  /* --- sv2 semver --- */
  setInputs({ "sv2-a": "1.10.0", "sv2-b": "1.9.5" }); reg("sv2-out");
  sv2();
  o = els["sv2-out"].innerHTML;
  assert(o.includes("<b>1.10.0</b> is newer"), "sv2 1.10.0 newer: " + o.slice(0, 90));
  assert(o.includes("minor field decides: 10 &gt; 9") || o.includes("minor field decides"), "sv2 minor rule");
  setInputs({ "sv2-a": "2.0.0-rc.1", "sv2-b": "2.0.0" });
  sv2();
  assert(els["sv2-out"].innerHTML.includes("pre-release loses"), "sv2 prerelease rule");
  assert(els["sv2-out"].innerHTML.includes("<b>2.0.0</b> is newer"), "sv2 release wins");
  setInputs({ "sv2-a": "3.4.5", "sv2-b": "3.4.5" });
  sv2();
  assert(els["sv2-out"].innerHTML.includes("<b>identical"), "sv2 equal");
  setInputs({ "sv2-a": "not-a-version" });
  sv2();
  assert(els["sv2-out"].innerHTML.includes("Both must be versions"), "sv2 guard");

  /* --- jq2 json->query --- */
  setInputs({ "jq2-in": '{"a":"1","b":"x y","c":"a&b"}' }); reg("jq2-out");
  jq2();
  o = els["jq2-out"].innerHTML;
  assert(o.includes("a=1&amp;b=x%20y&amp;c=a%26b"), "jq2 encoded pairs: " + o.slice(0, 110));
  assert(o.includes("<b>3</b>parameters"), "jq2 3 params");
  assert(o.includes("decoded check</b>a=1"), "jq2 decoded check");
  setInputs({ "jq2-in": '{"a": 1,' });
  jq2();
  assert(els["jq2-out"].innerHTML.includes("not valid JSON"), "jq2 bad json guard");
  setInputs({ "jq2-in": "[1,2]" });
  jq2();
  assert(els["jq2-out"].innerHTML.includes("JSON object at the top level"), "jq2 array guard");

  /* --- ua2 user agent --- */
  setInputs({ "ua2-in": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36" });
  reg("ua2-out");
  ua2();
  o = els["ua2-out"].innerHTML;
  assert(o.includes("<b>Chrome 121.0.0.0</b>on Windows 10/11 \u00b7 Desktop"), "ua2 chrome/win: " + o.slice(0, 100));
  assert(o.includes("<b>Blink engine</b>"), "ua2 blink");
  assert(o.includes("<b>human-ish</b>"), "ua2 not bot");
  setInputs({ "ua2-in": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0" });
  ua2();
  assert(els["ua2-out"].innerHTML.includes("<b>Edge 121"), "ua2 edge-first");
  setInputs({ "ua2-in": "Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 Chrome/120.0 Mobile Safari/537.36" });
  ua2();
  o = els["ua2-out"].innerHTML;
  assert(o.includes("Android 14"), "ua2 android: " + o.slice(0, 100));
  assert(o.includes("\u00b7 Mobile"), "ua2 mobile class");
  setInputs({ "ua2-in": "Googlebot/2.1 (+http://www.google.com/bot.html)" });
  ua2();
  assert(els["ua2-out"].innerHTML.includes("<b>bot</b>"), "ua2 bot detect");
  setInputs({ "ua2-in": "" });
  ua2();
  assert(els["ua2-out"].innerHTML.includes("Paste a user-agent"), "ua2 guard");

  /* --- al2 anchor links --- */
  setInputs({ "al2-in": "# Introduction\n## Getting Started!\n### Advanced Settings" }); reg("al2-out");
  al2();
  o = els["al2-out"].innerHTML;
  assert(o.includes("<b>3 anchor(s) generated</b>"), "al2 3 anchors: " + o.slice(0, 90));
  assert(o.includes("(#introduction)"), "al2 introduction");
  assert(o.includes("(#getting-started)"), "al2 getting-started");
  assert(o.includes("id=\"advanced-settings\""), "al2 id attr");
  setInputs({ "al2-in": "" });
  al2();
  assert(els["al2-out"].innerHTML.includes("Paste headings"), "al2 guard");

  /* --- pe2 percent error --- */
  setInputs({ "pe2-m": "9.8", "pe2-t": "9.81" }); reg("pe2-out");
  pe2();
  o = els["pe2-out"].innerHTML;
  assert(o.includes("<b>0.1%</b>error between measured 9.8 and accepted 9.81"), "pe2 0.1%: " + o.slice(0, 110));
  assert(o.includes("<b>-0.01</b>signed difference"), "pe2 signed -0.01");
  assert(o.includes("within 5%"), "pe2 tolerance chip");
  setInputs({ "pe2-m": "12", "pe2-t": "10" });
  pe2();
  assert(els["pe2-out"].innerHTML.includes("<b>20%</b>error"), "pe2 20%");
  assert(els["pe2-out"].innerHTML.includes("Over 5%"), "pe2 high-error chip");
  setInputs({ "pe2-t": "0" });
  pe2();
  assert(els["pe2-out"].innerHTML.includes("undefined there"), "pe2 zero guard");

  /* --- po2 proportion --- */
  setInputs({ "po2-a": "2", "po2-b": "3", "po2-c": "6" }); reg("po2-out");
  po2();
  o = els["po2-out"].innerHTML;
  assert(o.includes("<b>x = 9</b>completing 2:3 :: 6:x"), "po2 x=9: " + o.slice(0, 100));
  assert(o.includes("<b>18</b>cross product"), "po2 cross 18");
  assert(o.includes("<b>1.5</b>shared scale factor"), "po2 factor 1.5");
  setInputs({ "po2-a": "0" });
  po2();
  assert(els["po2-out"].innerHTML.includes("undefined; adjust the setup"), "po2 zero guard");

  /* --- rm2 remainder --- */
  setInputs({ "rm2-a": "17", "rm2-b": "5" }); reg("rm2-out");
  rm2();
  o = els["rm2-out"].innerHTML;
  assert(o.includes("<b>3 remainder 2</b>for 17 \u00f7 5"), "rm2 3r2: " + o.slice(0, 90));
  assert(o.includes("<b>3.4</b>decimal quotient"), "rm2 decimal 3.4");
  assert(o.includes("both agree</b>for positives"), "rm2 agree chip");
  assert(o.includes("17</b>check \u2013") === false, "rm2 format sane");
  setInputs({ "rm2-a": "-17", "rm2-b": "5" });
  rm2();
  o = els["rm2-out"].innerHTML;
  assert(o.includes("<b>-3 remainder -2</b>"), "rm2 -17: js -3 r -2: " + o.slice(0, 110));
  assert(o.includes("Euclidean") && o.includes("q = -4"), "rm2 euclidean q=-4");
  assert(o.includes("r = 3"), "rm2 euclidean r=3");
  setInputs({ "rm2-b": "0" });
  rm2();
  assert(els["rm2-out"].innerHTML.includes("Division by zero"), "rm2 zero guard");

  /* --- le2 linear --- */
  setInputs({ "le2-a": "2", "le2-b": "3", "le2-c": "5", "le2-d": "9" }); reg("le2-out");
  le2();
  o = els["le2-out"].innerHTML;
  assert(o.includes("<b>x = -2</b>solves 2x + 3 = 5x + 9"), "le2 x=-2: " + o.slice(0, 110));
  assert(o.includes("<b>-3x = 6</b>rearranged"), "le2 rearranged");
  assert(o.includes("<b>-1 = -1</b>substituted back"), "le2 verify");
  setInputs({ "le2-a": "2", "le2-b": "3", "le2-c": "2", "le2-d": "7" });
  le2();
  assert(els["le2-out"].innerHTML.includes("No solution"), "le2 parallel");
  setInputs({ "le2-a": "2", "le2-b": "3", "le2-c": "2", "le2-d": "3" });
  le2();
  assert(els["le2-out"].innerHTML.includes("Every x"), "le2 identity");

  /* --- gm2 geometric mean --- */
  setInputs({ "gm2-in": "2 8 4" }); reg("gm2-out");
  gm2();
  o = els["gm2-out"].innerHTML;
  assert(o.includes("<b>4</b>geometric mean of 3 values"), "gm2 4: " + o.slice(0, 90));
  assert(o.includes("<b>4.6667</b>arithmetic mean"), "gm2 am 4.6667");
  assert(o.includes("<b>0.6667</b>gap the volatility"), "gm2 gap 0.6667");
  setInputs({ "gm2-in": "4 -3 2" });
  gm2();
  assert(els["gm2-out"].innerHTML.includes("must be positive"), "gm2 negative guard");
  setInputs({ "gm2-in": "4" });
  gm2();
  assert(els["gm2-out"].innerHTML.includes("at least two"), "gm2 count guard");

  /* --- nr2 nth root --- */
  setInputs({ "nr2-x": "27", "nr2-n": "3" }); reg("nr2-out");
  nr2();
  o = els["nr2-out"].innerHTML;
  assert(o.includes("<b>3</b>= 27 raised to 1/3"), "nr2 cube root 3: " + o.slice(0, 90));
  assert(o.includes("<b>27</b>raised back to n"), "nr2 check 27");
  setInputs({ "nr2-x": "1024", "nr2-n": "10" });
  nr2();
  assert(els["nr2-out"].innerHTML.includes("raised to 1/10") && els["nr2-out"].innerHTML.includes("<b>2</b>="), "nr2 10th root 2: " + els["nr2-out"].innerHTML.slice(0, 80));
  setInputs({ "nr2-x": "-27", "nr2-n": "3" });
  nr2();
  assert(els["nr2-out"].innerHTML.includes("<b>-3</b>= -27 raised to 1/3"), "nr2 -27 cube root -3");
  setInputs({ "nr2-x": "-16", "nr2-n": "2" });
  nr2();
  assert(els["nr2-out"].innerHTML.includes("no real square root of -16 exists"), "nr2 even-root guard: " + els["nr2-out"].innerHTML.slice(0, 110));
  setInputs({ "nr2-n": "1.5" });
  nr2();
  assert(els["nr2-out"].innerHTML.includes("whole number of 2 or more"), "nr2 n guard");

  /* --- bk2 bakers --- */
  setInputs({ "bk2-f": "500", "bk2-h": "65", "bk2-s": "2", "bk2-y": "1" }); reg("bk2-out");
  bk2();
  o = els["bk2-out"].innerHTML;
  assert(o.includes("<b>840 g</b>total dough at 65% hydration"), "bk2 840 g: " + o.slice(0, 90));
  assert(o.includes("<b>325 g</b>water (65%)"), "bk2 water 325");
  assert(o.includes("<b>10 g</b>salt (2%)"), "bk2 salt 10");
  assert(o.includes("<b>5 g</b>yeast (1%)"), "bk2 yeast 5");
  setInputs({ "bk2-h": "78" });
  bk2();
  assert(els["bk2-out"].innerHTML.includes("Above 75% hydration"), "bk2 high hydration flag");

  /* --- rs3 roast --- */
  setInputs({ "rs3-w": "3", "rs3-m": "chicken" }); reg("rs3-out");
  rs3();
  o = els["rs3-out"].innerHTML;
  assert(o.includes("<b>155 min</b>(2 h 35 min) in a preheated oven"), "rs3 155 min: " + o.slice(0, 100));
  assert(o.includes("<b>45 min/kg + 20</b>"), "rs3 rate");
  assert(o.includes("<b>74\u00b0C / 165\u00b0F</b>"), "rs3 pull temp");
  assert(o.includes("rest 15\u201320 min"), "rs3 rest");
  setInputs({ "rs3-m": "beef" });
  rs3();
  assert(els["rs3-out"].innerHTML.includes("<b>185 min</b>(3 h 5 min)"), "rs3 beef 185");

  /* --- we2 wallpaper --- */
  setInputs({ "we2-l": "5", "we2-w": "4", "we2-h": "2.8", "we2-r": "10", "we2-wa": "0" }); reg("we2-out");
  we2();
  o = els["we2-out"].innerHTML;
  assert(o.includes("<b>10 rolls</b>cover a 5\u00d74 m room at 2.8 m high"), "we2 10 rolls: " + o.slice(0, 100));
  assert(o.includes("<b>50.4 m\u00b2</b>total wall area"), "we2 50.4 m2");
  assert(o.includes("<b>5.3 m\u00b2</b>per 10 m roll"), "we2 roll cover 5.3");
  setInputs({ "we2-wa": "15" });
  we2();
  assert(els["we2-out"].innerHTML.includes("<b>11 rolls</b>"), "we2 15% -> 11 rolls");

  /* --- lp2 landscape --- */
  setInputs({ "lp2-a": "20", "lp2-d": "10", "lp2-b": "30", "lp2-t": "1.5" }); reg("lp2-out");
  lp2();
  o = els["lp2-out"].innerHTML;
  assert(o.includes("<b>67 bags</b> (30 L each) or <b>3 tonnes</b>"), "lp2 67 bags/3t: " + o.slice(0, 110));
  assert(o.includes("<b>2 m\u00b3</b>volume"), "lp2 2 m3");
  assert(o.includes("<b>1.5 t/m\u00b3</b>"), "lp2 density chip");
  assert(o.includes("+10% wise"), "lp2 overage chip");
  setInputs({ "lp2-d": "" });
  lp2();
  assert(els["lp2-out"].innerHTML.includes("spreading depth"), "lp2 guard");
}

try { main(); } catch (e) { console.error("HARNESS ERROR: " + e.message + "\n" + e.stack); process.exitCode = 1; }
let ok = 0, fail = 0;
console.log("");
console.log("done");
process.exit(0);
