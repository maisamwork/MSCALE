# -*- coding: utf-8 -*-
"""Batch 27: eight more brand-new flagship tools, mega3-12 pattern."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA13 = {}
CONTENT13 = {}

ADV13 = []

ADV13.append(("sharpe-ratio-calculator", "Sharpe Ratio Calculator", "Finance & Business",
 "Return above the risk-free rate per unit of risk taken",
 "Two funds can post the same return while one took four times the turbulence to get there. The Sharpe ratio divides the excess return over cash by volatility, turning color return-bragging into one comparable number. Enter an annual return, the risk-free rate and the standard deviation of returns, and this calculator scores the risk-adjusted result on the standard 0.5\u20132+ quality scale.",
 "Sharpe = (return \u2212 risk-free) \u00f7 volatility; 0.5 decent, 1.0 very good, 2.0 excellent",
 "a 12% return against 3% cash and 18% volatility scores 0.50 \u2014 decent, not brilliant",
 ["comparing funds and ETFs honestly","evaluating advisor claims","portfolio strategy reviews","interview prep for finance roles"],
 "The ratio rewards smoothness: a bond ladder can out-Sharpe a hot stock fund with half the return. Use the same period for all three inputs — annual return against a daily volatility figure silently inflates the score.",
 "sr2",
 _f("sr2-r", "Portfolio return (% per year)", "12") + _f("sr2-f", "Risk-free rate (%)", "3") + _f("sr2-s", "Volatility, standard deviation (%)", "18") +
 '''<button class="btn" onclick="sr2()">Score the ratio</button>
  <div id="sr2-out" class="result" aria-live="polite"></div>'''))

ADV13.append(("runway-calculator", "Runway Calculator", "Finance & Business",
 "How many months of life are left in your cash against burn",
 "Every startup, freelancer and project has a silent clock: cash on hand \u00f7 monthly burn. Enter the two numbers, and this calculator answers the months remaining, the exact calendar date the money runs out, the weekly burn rate, and \u2014 the number founders actually need \u2014 how many extra months a burn cut buys before the next raise or revenue floor.",
 "runway months = cash \u00f7 monthly burn; a burn cut rescales the denominator, cash stays fixed",
 "50,000 against 8,500 a month is 5.9 months \u2014 cutting burn 10% stretches it by 0.7 more months",
 ["startup board and investor updates","freelancer dry-spell planning","project budget checkpoints","relocation and sabbatical budgeting"],
 "Revenue reducing burn beats cost-cutting: the same 10% cut to net burn is far easier sold than a payroll slash. Runway smooths reality — annual renewals or quarterly tax lumps make some months unfaithful; average with monthly figures.",
 "rw2",
 _f("rw2-c", "Cash on hand", "50000") + _f("rw2-b", "Monthly burn (net outflow)", "8500") + _sel("rw2-a", "Burn cut to test", [("0", "None \u2014 current course"), ("10", "Cut burn 10%"), ("20", "Cut burn 20%"), ("30", "Cut burn 30%")]) +
 '''<button class="btn" onclick="rw2()">Compute runway</button>
  <div id="rw2-out" class="result" aria-live="polite"></div>'''))

ADV13.append(("body-surface-area-calculator", "Body Surface Area Calculator", "Calculators",
 "The m\u00b2 figure clinics dose chemotherapy and enzyme charts against",
 "Drug doses for chemotherapy, burns fluid resuscitation and cardiac indexing are all written in body surface area, not weight alone. Enter height in centimetres and weight in kilograms, and this calculator returns the classic Du Bois BSA alongside the Mosteller cross-check, the daily-fluid estimate clinicians derive, and the BMI the same two numbers imply.",
 "Du Bois BSA = 0.007184 \u00d7 height^0.725 \u00d7 weight^0.425; Mosteller = \u221a(height \u00d7 weight \u00f7 3600)",
 "170 cm and 70 kg give 1.81 m\u00b2 by Du Bois and 1.82 m\u00b2 by Mosteller \u2014 formulas agree to about 1%",
 ["medical dosing cross-checks","burns-fluid awareness","fitness and performance tracking","growth-chart conversations"],
 "Du Bois and Mosteller drift apart at extreme heights; Mosteller is the usual hospital default for speed. BSA normalizes what weight alone misjudges — that is exactly why liver-indexed drugs use it instead.",
 "bu2",
 _f("bu2-h", "Height (cm)", "170") + _f("bu2-w", "Weight (kg)", "70") +
 '''<button class="btn" onclick="bu2()">Compute BSA</button>
  <div id="bu2-out" class="result" aria-live="polite"></div>'''))

ADV13.append(("dew-point-calculator", "Dew Point Calculator", "Calculators",
 "Temperature \u00d7 humidity into the dew point your body actually feels",
 "Dew point is the honest humidity measure: the temperature at which the air gives up its water as condensation \u2014 on windows, cold drinks or human skin. Enter the air temperature and relative humidity (Fahrenheit or Celsius), and this calculator applies the Magnus equation meteorologists use and places the dew point on the dry-to-oppressive scale runners and weather nerds quote.",
 "\u03b1 = ln(RH/100) + 17.625T \u00f7 (243.04 + T); dew point = 243.04\u03b1 \u00f7 (17.625 \u2212 \u03b1)",
 "25\u00b0C air at 60% humidity has a 16.7\u00b0C dew point \u2014 muggy territory even though the thermometer says fine",
 ["running and training comfort checks","condensation and mould risk","greenhouse and cellar monitoring","weather-report translation"],
 "Below 10°C dew point the air feels dry and staticky; above 21°C it feels sticky and oppressive. Cold windows fog when glass temperature drops under the dew point — not because of the room temperature.",
 "de2",
 _f("de2-t", "Air temperature", "25") + _f("de2-r", "Relative humidity (%)", "60") + _sel("de2-u", "Units", [("c", "Celsius"), ("f", "Fahrenheit")]) +
 '''<button class="btn" onclick="de2()">Compute dew point</button>
  <div id="de2-out" class="result" aria-live="polite"></div>'''))

ADV13.append(("bitwise-calculator", "Bitwise Calculator", "Developer Tools",
 "AND, OR, XOR and shifts across decimal, hex and binary at once",
 "Flag maths, permissions masks and hash mixing all live in the same few operations, yet every language renders them differently. Enter two integers in any base, pick AND, OR, XOR, NAND, NOR, XNOR, add, subtract or one of the three shifts, and this calculator answers decimal, hexadecimal and 8-bit-grouped binary together \u2014 with the shifts and unsigned quirk visible on a 32-bit stage.",
 "bitwise ops apply per bit on 32-bit integers; shifts move bits; \u003e\u003e\u003e fills with zeros",
 "12 AND 10 is 8 (1000); 1 shifted left 4 places is 16 (hex 0x10)",
 ["permission flag design","embedded register work","hash and checksum stepping","teaching binary arithmetic"],
 ">> keeps the sign bit on negatives while >>> zero-fills — screen the difference with any negative input. XOR a value twice with the same key and it returns — the playful root of stream ciphers.",
 "bw2",
 _f("bw2-a", "Value A", "12") + _f("bw2-b", "Value B", "10") + _sel("bw2-s", "Input base", [("10", "Decimal"), ("16", "Hexadecimal"), ("2", "Binary")]) + _sel("bw2-o", "Operation", [("and", "AND (&)"), ("or", "OR (|)"), ("xor", "XOR (^)"), ("nand", "NOT AND"), ("nor", "NOT OR"), ("xnor", "XNOR"), ("add", "Add"), ("sub", "Subtract"), ("shl", "Shift A left by B"), ("shr", "Shift A right by B (signed)"), ("shru", "Shift A right by B (unsigned)")]) +
 '''<button class="btn" onclick="bw2()">Apply bitwise op</button>
  <div id="bw2-out" class="result" aria-live="polite"></div>'''))

ADV13.append(("note-frequency-converter", "Note Frequency Converter", "Converters",
 "Hertz into the nearest note with cents, and notes back into Hertz",
 "Tuners think in cents while producers think in Hertz, and pitch correction needs both directions at once. Enter a frequency to get the nearest note with the number of cents it is off, or pick a note and octave to get the exact equal-temperament frequency \u2014 plus the period and the acoustic wavelength that room setups care about.",
 "12 \u00d7 log\u2082(f \u00f7 440) semitones from A4; each semitone is exactly 100 cents",
 "445 Hz is A4 sharp by 19.6 cents; C5 sits exactly on 523.25 Hz in equal temperament",
 ["tuning instruments by ear to a reference","sound-design and synth patching","mixing and sub-bass checks","physics of sound homework"],
 "A semitone is always 100 cents, but human pitch acuity peaks near 3–5 cents — screen your tuning to that. A4 = 440 Hz is the ISO reference; orchestras lean to 442–443 for brightness and re-tune the conversion.",
 "nf2",
 _sel("nf2-m", "Direction", [("hz", "Frequency \u2192 note"), ("note", "Note \u2192 frequency")]) + _f("nf2-h", "Frequency (Hz)", "445") + _sel("nf2-n", "Note", [("C", "C"), ("C#", "C\u266f"), ("D", "D"), ("D#", "D\u266f"), ("E", "E"), ("F", "F"), ("F#", "F\u266f"), ("G", "G"), ("G#", "G\u266f"), ("A", "A"), ("A#", "A\u266f"), ("B", "B")]) + _sel("nf2-o", "Octave", [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8")]) +
 '''<button class="btn" onclick="nf2()">Convert pitch</button>
  <div id="nf2-out" class="result" aria-live="polite"></div>'''))

ADV13.append(("levenshtein-distance-calculator", "Levenshtein Distance Calculator", "Text Tools",
 "How many single-letter edits stand between two strings",
 "Spellcheckers, fuzzy search, DNA comparison and cheat-finding all run on the same number: the smallest count of insertions, deletions and substitutions that turns one string into another. Enter both strings, and this calculator computes the classic dynamic-programming table distance, normalizes it into a similarity percentage, and suggests where the match stops being a typo and starts being a different word.",
 "distance = DP edit count over insertions, deletions and substitutions; similarity = 1 \u00d7 (1 \u2212 d \u00f7 longer length)",
 "\u201ckitten\u201d to \u201csitting\u201d is exactly 3 edits \u2014 57.1% similarity on a 7-letter yardstick",
 ["fuzzy search and autocomplete tuning","spellcheck custom dictionaries","duplicate detection in data cleanup","biochemistry sequence comparisons"],
 "Under 2 edits on a 6+ letter word is almost always a typo; over a third of the length is usually a different word entirely. Distance is symmetric — kitten to sitting costs the same as the reverse — screen both anyway when debugging.",
 "ld2",
 _f("ld2-a", "First string", "kitten") + _f("ld2-b", "Second string", "sitting") +
 '''<button class="btn" onclick="ld2()">Measure distance</button>
  <div id="ld2-out" class="result" aria-live="polite"></div>'''))

ADV13.append(("coffee-ratio-calculator", "Coffee Ratio Calculator", "Calculators",
 "Water, dose and ratio matched both ways for any brew method",
 "Every brewing dispute \u2014 pour-over, French press, aeropress \u2014 hides inside one ratio: water \u00f7 dose. Choose your ratio (or your bean dose), and this calculator answers both directions, converts to cups and millilitres, scales any recipe up or down, and suggests the grind size the ratio quietly assumes.",
 "dose = water \u00f7 ratio; 1:15\u20131:16 is bright pour-over, 1:17\u20131:18 balanced, coarser ratios lean softer",
 "300 g of water at 1:16 takes exactly 18.8 g of coffee \u2014 flip to dose mode and 20 g calls for 320 g of water",
 ["pour-over and aeropress dialing-in","French press and large-batch scaling","cold-batch concentrate ratios","saving half-made bags of beans"],
 "Screen one variable at a time: change ratio OR grind, never both on the same cup. ",
 "wa3",
 _f("wa3-w", "Water (grams) \u2014 or leave blank", "300") + _f("wa3-d", "Coffee dose (grams) \u2014 or leave blank", "") + _f("wa3-r", "Ratio (water per part, e.g. 16 = 1:16)", "16") +
 '''<button class="btn" onclick="wa3()">Scale the brew</button>
  <div id="wa3-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV13:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA13[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'''<div class="panel">{extra}{tail}</div>''',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT13[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
