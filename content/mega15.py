# -*- coding: utf-8 -*-
"""Batch 28 module B: 31 more flagship tools (converters, text, dev, math, hobby)."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA15 = {}
CONTENT15 = {}

ADV15 = []

ADV15.append(("pressure-converter", "Pressure Converter", "Converters",
 "kPa, psi, bar, atm and mmHg converted in one panel",
 "Tyres quote psi, weather maps quote millibars, medicine quotes mmHg, and chemistry quotes atmospheres \u2014 the same pressure wearing four costumes. Enter one value and its unit, and this converter answers the full set at once against the exact SI factors, so a tyre gauge and a forecast finally speak the same language.",
 "psi = kPa \u00f7 6.894757; bar = kPa \u00f7 100; atm = kPa \u00f7 101.325; mmHg = kPa \u00f7 0.133322",
 "101.325 kPa is the standard atmosphere: 14.696 psi, 1.013 bar, 760 mmHg \u2014 one reading, four dialects",
 ["tyre and bike pressure checks","plumbing and HVAC readings","diving and scuba tables","recipes and lab work"],
 "Gauge pressure excludes the atmosphere already around you; absolute includes it \u2014 tyre gauges read gauge by convention. Sea-level weather of 1013 mb is one bar almost exactly.",
 "pc2",
 _f("pc2-v", "Value", "101.325") + _sel("pc2-u", "From unit", [("kPa", "kilopascals (kPa)"), ("psi", "psi"), ("bar", "bar"), ("atm", "atmospheres (atm)"), ("mmHg", "mmHg / torr"), ("MPa", "megapascals (MPa)")]) +
 '''<button class="btn" onclick="pc2()">Convert pressure</button>
  <div id="pc2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("energy-converter", "Energy Converter", "Converters",
 "Joules, calories, kWh and BTU converted from one field",
 "Food labels use calories, electricity bills use kWh, gym machines use joules, and American heating quotes BTU \u2014 each with different magnitudes that invite tenfold errors. Enter a value with its unit, and this converter answers the whole energy family with the exact conversion constants, plus the human-scale translations.",
 "1 kcal = 4184 J; 1 kWh = 3,600,000 J = 860,421 small calories; 1 BTU = 1055.06 J",
 "one food calorie (kcal) is 4.184 kJ \u2014 and a kWh would boil about 28 kettles, not heat one room once",
 ["diet and nutrition labels","electricity bill unit checks","physics homework conversions","heating and HVAC sizing"],
 "Food calories are kilocalories despite the small-c print \u2014 a thousandfold gap. kWh measures energy; kW measures power; confusing them inflates quotes by the hours factor.",
 "en2",
 _f("en2-v", "Value", "1") + _sel("en2-u", "From unit", [("kWh", "kilowatt-hours (kWh)"), ("J", "joules (J)"), ("kJ", "kilojoules (kJ)"), ("cal", "small calories (cal)"), ("kcal", "food Calories (kcal)"), ("Wh", "watt-hours (Wh)"), ("BTU", "BTU")]) +
 '''<button class="btn" onclick="en2()">Convert energy</button>
  <div id="en2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("power-converter", "Power Converter", "Converters",
 "Watts, kilowatts and horsepower side by side with BTU per hour",
 "Car engines quote horsepower, heaters quote BTU per hour, and electricians quote watts \u2014 three systems for one quantity. Enter a power value and unit, and this converter answers the full set with metric and mechanical horsepower both shown, because those two are not the same number either.",
 "1 mechanical hp = 745.699872 W; 1 metric hp = 735.49875 W; 1 BTU/h = 0.293071 W",
 "1000 watts is 1.341 mechanical horsepower \u2014 and a bar heater drawing it throws 3412 BTU per hour",
 ["engine and motor spec comparisons","heater and air-conditioner sizing","generator and solar planning","appliance running-cost math"],
 "Mechanical (745.70) and metric (735.50) horsepower differ by 1.4% \u2014 enough to fudge a spec-sheet comparison. Power times hours is what you actually pay for on the bill.",
 "pw3",
 _f("pw3-v", "Power", "1000") + _sel("pw3-u", "From unit", [("W", "watts (W)"), ("kW", "kilowatts (kW)"), ("hp", "mechanical horsepower"), ("ps", "metric horsepower (PS)"), ("btuh", "BTU per hour")]) +
 '''<button class="btn" onclick="pw3()">Convert power</button>
  <div id="pw3-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("force-converter", "Force Converter", "Converters",
 "Newtons, pounds-force and kilograms-force without the classic mix-up",
 "Engineering quotes newtons, gym plates quote kilograms, and US specs quote pounds-force \u2014 and kg is a mass, not a force, which is where a hundred conversions go wrong. Enter force with its unit and this converter answers all of them, stating the g-annoyance honestly.",
 "1 kgf = 9.80665 N; 1 lbf = 4.4482216 N; 1 dyne = 0.00001 N",
 "100 newtons is 10.20 kgf \u2014 not 100, because kg assumes the pull of Earth's gravity on the mass",
 ["engineering homework and drafts","climbing-gear load ratings","torque and extension-spring specs","funfair g-force comparisons"],
 "Kilograms-force is a convenience unit: it equals mass only at standard gravity. On the Moon your weight reading halves while your kgf spec does not \u2014 springs obey newtons.",
 "fc2",
 _f("fc2-v", "Force", "100") + _sel("fc2-u", "From unit", [("N", "newtons (N)"), ("kN", "kilonewtons (kN)"), ("lbf", "pounds-force (lbf)"), ("kgf", "kilograms-force (kgf)"), ("dyn", "dynes")]) +
 '''<button class="btn" onclick="fc2()">Convert force</button>
  <div id="fc2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("volume-converter", "Volume Converter", "Converters",
 "Litres, cups, pints, quarts and gallons in a single answer set",
 "Recipes, paint tins, fuel tanks and milk jugs switch between litres and US customary measures with no warning. Enter a volume with its unit, and this converter answers the whole set \u2014 including the cup that American and metric cookbooks disagree about by definition.",
 "1 US gallon = 3.785411784 L = 4 quarts = 8 pints = 16 cups; 1 US cup = 0.24 L",
 "a US gallon is 3.79 litres \u2014 the imperial gallon would have been 4.55, and older British recipes notice the gap",
 ["cooking and baking conversions","paint and garden-chemical coverage","fuel and tank sizing","lab and aquarium dosing"],
 "These are US units: imperial pints and gallons are roughly 20% bigger, and UK cups in older books can mean anything from 240\u2013284 ml. Check which side of the Atlantic the recipe grew up on.",
 "vl2",
 _f("vl2-v", "Volume", "3.785411784") + _sel("vl2-u", "From unit", [("l", "litres (L)"), ("galus", "US gallons"), ("qtus", "US quarts"), ("ptus", "US pints"), ("cup", "US cups"), ("flozus", "US fluid ounces"), ("ml", "millilitres (mL)"), ("m3", "cubic metres")]) +
 '''<button class="btn" onclick="vl2()">Convert volume</button>
  <div id="vl2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("meters-per-second-converter", "Meters per Second Converter", "Converters",
 "Speed in m/s, km/h, mph, knots and feet per second together",
 "Physics wants m/s, road signs want km/h or mph, sailing wants knots, and aviation weather says feet per second. Enter one speed, and this converter answers all five with the exact fixed definitions \u2014 and flags the wind-scale intuition a knot quietly carries.",
 "m/s = km/h \u00f7 3.6 = mph \u00f7 2.23694 = knots \u00f7 2.23694\u2026 exactly: 1 knot = 0.514444 m/s",
 "100 km/h is 27.78 m/s or 62.14 mph \u2014 and the divide-by-3.6 shortcut lands the physics answer instantly",
 ["running and cycling pace tracking","physics problem setup","sailing and aviation winds","athletics record comparisons"],
 "The 3.6 constant is exact (3600 seconds per hour); mph needs 2.23694. Strong winds climb the Beaufort scale \u2014 26 knots is a gale, 13.8 m/s.",
 "ms2",
 _f("ms2-v", "Speed", "100") + _sel("ms2-u", "From unit", [("kmh", "km/h"), ("mps", "meters per second (m/s)"), ("kmh", "km/h"), ("mph", "mph"), ("kn", "knots"), ("ftps", "feet per second")]) +
 '''<button class="btn" onclick="ms2()">Convert speed</button>
  <div id="ms2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("data-transfer-time", "Data Transfer Time Calculator", "Calculators",
 "How long any file size takes at any internet speed",
 "A ten-gigabyte backup is thirteen minutes on gigabit fibre and thirteen hours on the office line \u2014 the same file, sixteen different afternoons. Enter the file size and the connection speed, pick your units, and this calculator converts bits and bytes honestly (the \u00d78 most calculators forget) and returns the hours, minutes and seconds.",
 "seconds = size(MB) \u00d7 8 \u00f7 speed(Mbps); bytes hold 8 bits and drive speeds are quoted in bits",
 "10 GB over 100 Mbps takes 800 seconds \u2014 13 minutes 20 seconds, not the 100 seconds the byte\u2215bit mix-up suggests",
 ["backup and migration planning","streaming and upload estimates","server bandwidth budgeting","choosing between ISP plans"],
 "Speeds advertise megabits; files live in megabytes \u2014 the \u00d78 divider explains every 'slow download'. Real throughput runs 10\u201330% under the headline after overheads.",
 "dt3",
 _f("dt3-s", "Data size", "10") + _sel("dt3-su", "Size unit", [("GB", "gigabytes (GB)"), ("MB", "megabytes (MB)"), ("TB", "terabytes (TB)"), ("KiB", "gibibytes (GiB)")]) + _f("dt3-sp", "Connection speed (Mbps)", "100") +
 '''<button class="btn" onclick="dt3()">Time the transfer</button>
  <div id="dt3-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("car-fuel-comparison", "Car Fuel Comparison Calculator", "Calculators",
 "Two cars, one commute \u2014 the honest annual fuel cost gap",
 "The pleasing number on a spec sheet hides in gallons: a 25 mpg car and a 35 mpg one differ by a weekend getaway every month. Enter the annual miles, fuel price and both cars' mpg, and this calculator totals each car's gallons and annual cost, then names the saving and what a decade of it buys.",
 "gallons = miles \u00f7 mpg; cost = gallons \u00d7 price; saving = costA \u2212 costB",
 "12,000 miles at $3.60 costs $1,728 in the 25-mpg car against $1,234 in the 35-mpg one \u2014 $493.71 a year, $4,937 per decade",
 ["used-car purchase decisions","hybrid and EV cost maths","family second-car debates","commute route and carpool choices"],
 "Fix one commute and vary the car, not both \u2014 improvements compound in gallons, which is where the money lives. Efficiency shrinks in cold weather and short trips; the sticker assumes neither.",
 "cf3",
 _f("cf3-m", "Annual miles driven", "12000") + _f("cf3-p", "Fuel price ($/gallon)", "3.60") + _f("cf3-a", "Car A fuel economy (mpg)", "25") + _f("cf3-b", "Car B fuel economy (mpg)", "35") +
 '''<button class="btn" onclick="cf3()">Compare the cars</button>
  <div id="cf3-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("unicode-escape", "Unicode Escape Converter", "Text Tools",
 "Text to \\uXXXX escapes and back, including emoji code points",
 "Every JSON file, JavaScript string and config value can hide text as \\u escapes \u2014 and debugging means reading both. Paste text or escapes, choose the direction, and this converter answers with the escaped form (including \\u{...} for emoji beyond the basic plane) or the decoded original, non-destructively.",
 "escape = \\uXXXX (4 hex digits) or \\u{XXXXX} for code points above U+FFFF; decode reverses both",
 "\\u0041\\u0042\\u0043 decodes to ABC, and the emoji \\ud83d\\ude00 demystifies into its U+1F600 code point",
 ["JSON and API payload debugging","source-control encoding fixes","localization string files","teaching encodings step by step"],
 "Surrogate pairs appear as two \\u escapes once encoded naively; prefer the \\u{1F600} form for emoji. Escapes are case-insensitive hex, so \\u00E9 and \\u00e9 encode the same letter.",
 "un2",
 '<div class="row"><div><label for="un2-in">Text \\u2014 or escapes to decode</label><textarea id="un2-in" rows="3" placeholder="Paste here">ABC</textarea></div></div><div class="row"><div><label for="un2-m">Direction</label><select id="un2-m"><option value="e">Encode to \\uXXXX</option><option value="d">Decode \\uXXXX</option></select></div></div>' +
 '''<button class="btn" onclick="un2()">Run the conversion</button>
  <div id="un2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("nato-phonetic", "NATO Phonetic Alphabet Converter", "Text Tools",
 "Spell any word over the phone exactly as pilots and ATC do",
 "M for em, N for en: two letters that sound identical cost hours of customer-service misery. The NATO alphabet solves it by giving every letter one unmissable word. Type any string and this converter spells it NATO-style, digits included, so call-centre scripts and radio checks leave nothing to luck.",
 "Letter maps to its one-word code word (A\u2192Alfa \u2026 Z\u2192Zulu); digits map to number words (5\u2192Fife)",
 "\"AB3\" spells Alfa Bravo Three \u2014 over a bad phone line the two nearer the front sound inescapably distinct",
 ["phone-based account verification","radio and air-traffic checks","serial-number callouts","reception and IT helpdesks"],
 "The spellings are official: Alfa and Juliett, with but one T and two Ls. Punctuation is skipped, so mixed codes stay clean and copy-pasteable.",
 "np2",
 '<div class="row"><div><label for="np2-in">Text to spell</label><input type="text" id="np2-in" value="AB3" autocomplete="off" /></div></div>' +
 '''<button class="btn" onclick="np2()">Spell it phonetically</button>
  <div id="np2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("stopwords-remover", "Stopwords Remover", "Text Tools",
 "Strip the filler words and see the content that remains",
 "Search indexes, keyword tools and topic models all begin the same way: delete the words that appear everywhere and mean nothing alone. Paste your text, and this remover filters a 130-word English stopword list, then reports exactly what was kept, what was dropped and the ratio \u2014 so you can tune density per output.",
 "words \u2260 stopwords survive; kept% = (remaining \u00f7 original) \u00d7 100 on whitespace word count",
 "\"the cat sat on the mat\" loses four of six words \u2014 what remains, 'cat sat mat', is the whole searchable content",
 ["SEO keyword density passes","pre-processing text for search","headline and title tightening","chatbot and corpus cleanup"],
 "Stopword lists are editorial: 'new', 'own' and 'time' are on some and matter for product copy. Keep the original in a file \u2014 removal loses tone that no index ever restores.",
 "st5",
 '<div class="row"><div><label for="st5-in">Text to filter</label><textarea id="st5-in" rows="4">the quick brown fox jumps over the lazy dog and the fox is very quick indeed</textarea></div></div>' +
 '''<button class="btn" onclick="st5()">Remove stopwords</button>
  <div id="st5-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("duplicate-word-finder", "Duplicate Word Finder", "Text Tools",
 "Locate the words your edits repeated without noticing",
 "Edited prose doubles words in ways the eye forgives but dictionaries punish: 'the the', names typed twice, product terms multiplying through a paragraph. Paste text, and this finder counts every word's frequency, reports one or more repeats sorted by count, and flags them for cleanup.",
 "count map over lowercased words; repeats listed with frequencies, highest first",
 "\"the cat sat with the dog near the bowl\" finds the appearing three times \u2014 and those edits read flawlessly aloud",
 ["proofreading long documents","SEO copy cleanup","documentation lint passes","chatbot transcript checks"],
 "Matching ignores case and punctuation, so 'The' and 'the' are the same word \u2014 usually what you want for catch-up passes. Deliberate repetition in headlines is a style choice, not an error.",
 "dw2",
 '<div class="row"><div><label for="dw2-in">Text to check</label><textarea id="dw2-in" rows="4">the cat sat with the dog near the bowl where the dog ate</textarea></div></div>' +
 '''<button class="btn" onclick="dw2()">Find duplicates</button>
  <div id="dw2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("vowel-counter", "Vowel Counter", "Text Tools",
 "Per-vowel counts, totals and vowel density of any text",
 "Vowel density shapes how language sounds: poems, brand names and pangram games all live on it. Paste text, and this counter returns each vowel's count, the total, letter-count share as a percentage, plus the consonant count for symmetry.",
 "count each of a, e, i, o, u case-insensitively; density = vowels \u00f7 (vowels + consonants) \u00d7 100",
 "\"hello world\" holds 3 vowels of 10 letters \u2014 30% vowel density, right on English's typical 36\u201340 low side",
 ["haiku and poetry meter checks","brand-name sound symbolism","puzzle and pangram design","language-learning drills"],
 "Y is counted as a consonant here; adjust by hand for riddle grading. Accented letters (\u00e9, \u00fc) are not vowels in this count unless you paste them pre-normalised.",
 "vo2",
 '<div class="row"><div><label for="vo2-in">Text to count</label><textarea id="vo2-in" rows="3" placeholder="Paste text">hello world</textarea></div></div>' +
 '''<button class="btn" onclick="vo2()">Count the vowels</button>
  <div id="vo2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("chmod-calculator", "Chmod Calculator", "Developer Tools",
 "File permissions between numeric 755 and readable rwx notation",
 "Permissions are one octal digit per role, but every beginner has typed 600 where 644 was meant and locked themselves out. Pick read, write, execute per role, and this calculator answers the numeric code, the symbolic rwx string, and the plain-English verdict \u2014 with common presets one click away.",
 "digit = read(4) + write(2) + execute(1) per owner, group, other; code = three digits in order",
 "755 reads rwxr-xr-x: the owner can write, everyone runs it \u2014 the web-server default that 600 would break",
 ["Web-server file fixes","shell-script permission checks","SSH key preparation (600)","ci pipelines and deploys"],
 "Directories need execute to open at all, so folder patterns differ from file patterns. Private keys ride at 600 and SSH refuses anything looser \u2014 the preset buttons know this.",
 "ch3",
 _sel("ch3-o", "Owner", [("7", "7 \u2014 read+write+execute"), ("6", "6 \u2014 read+write"), ("5", "5 \u2014 read+execute"), ("4", "4 \u2014 read only"), ("0", "0 \u2014 none")]) +
 _sel("ch3-g", "Group", [("5", "5 \u2014 read+execute"), ("7", "7 \u2014 read+write+execute"), ("6", "6 \u2014 read+write"), ("4", "4 \u2014 read only"), ("0", "0 \u2014 none")]) +
 _sel("ch3-t", "Others", [("5", "5 \u2014 read+execute"), ("4", "4 \u2014 read only"), ("7", "7 \u2014 read+write+execute"), ("6", "6 \u2014 read+write"), ("0", "0 \u2014 none")]) +
 '''<button class="btn" onclick="ch3()">Compute permissions</button>
  <div id="ch3-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("ascii-value-finder", "ASCII Value Finder", "Developer Tools",
 "Characters to decimal, hex and binary codes \u2014 and straight back",
 "Half of string debugging is discovering what the character actually is: space, tab, curly quote, zero-width something. Type a character and this finder answers the decimal code point, hexadecimal, binary, and the C-style escape; type a number and it answers with the character, bidirectionally.",
 "decimal = char.codePointAt(0); hex = toString(16); binary = toString(2), Unicode past 127 included",
 "'A' is 65 = 0x41 = 01000001 \u2014 and \u20ac lands at 8364, past the ASCII table entirely",
 ["debugging invisible characters","teaching binary and hex","serialization format checks","password and token inspection"],
 "ASCII is the 0\u2013127 band; everything above is Unicode and multiplies into UTF-8 bytes in files. The first 32 values are control characters that never print \u2014 this tool names them.",
 "as2",
 '<div class="row"><div><label for="as2-c">Character(s) to inspect</label><input type="text" id="as2-c" value="A" maxlength="8" autocomplete="off" /></div><div><label for="as2-n">Or a number to decode</label><input type="number" id="as2-n" value="65" autocomplete="off" /></div></div>' +
 '''<button class="btn" onclick="as2()">Look it up</button>
  <div id="as2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("http-status-code-explainer", "HTTP Status Code Explainer", "Developer Tools",
 "Any response code: its name, category and what actually caused it",
 "A 402 in the logs, a 307 from the CDN, a 429 nobody can reproduce \u2014 status codes are a language of few characters and long arguments. Type a code, and this explainer returns the official name, the request/response/pay category, typical causes and the first debugging move.",
 "codes class as 1xx informational, 2xx success, 3xx redirect, 4xx client error, 5xx server error",
 "404 is Not Found in the client-error class \u2014 the resource never did exist, unlike 410 Gone, which concedes it once did",
 ["API debugging and log reviews","redirect and CDN troubleshooting","teaching web fundamentals","status-monitor alert triage"],
 "Read the class first, then the specific code: a 502 is the proxy blaming the app behind it, so the fix lives on the upstream server, not in the configuration.",
 "hs2",
 _f("hs2-c", "Status code", "404") +
 '''<button class="btn" onclick="hs2()">Explain the code</button>
  <div id="hs2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("mac-address-tool", "MAC Address Tool", "Developer Tools",
 "Reformat, validate and inspect any hardware MAC address",
 "Device inventories render the same 48-bit address five different ways, and matching them by eye fails predictably. Paste a MAC in any common format, and this tool validates it, answers colon, hyphen and dot forms in both cases, and reads the locally-administered and multicast bits from the first octet.",
 "hex pairs validated against 12 digits + 5 separators of any mix; bit 1 of byte 0 flags multicast, bit 2 local",
 "aabbccddeeff normalizes to AA:BB:CC:DD:EE:FF \u2014 and byte AA's low bit says unicast, second bit says burned-in",
 ["network device inventory merges","DHCP reservation tables","Wi-Fi filtering policies","IoT hardware debugging"],
 "Randomized MAC addresses on phones rotate every network, so inventory matches should quote the hardware address, not whatever the phone displayed last. Bits count left to right from the top octet.",
 "ma2",
 '<div class="row"><div><label for="ma2-in">MAC address (any format)</label><input type="text" id="ma2-in" value="aabbccddeeff" autocomplete="off" /></div></div>' +
 '''<button class="btn" onclick="ma2()">Normalize it</button>
  <div id="ma2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("semver-comparator", "Semver Comparator", "Developer Tools",
 "Which version is newer, compared rule by rule with reasoning",
 "Version strings order by integers, not alphabet: 1.10.0 outranks 1.9.5 precisely because string sorters get it wrong. Enter two versions, and this comparator answers which one wins, the rule that decided it, and how each of major, minor and patch sits \u2014 including pre-release tags that sort below everything.",
 "compare major, then minor, then patch numerically; a release beats any pre-release of the same triple",
 "1.10.0 wins over 1.9.5 on the minor field \u2014 and 2.0.0-rc.1 loses to plain 2.0.0 by pre-release rule",
 ["npm and pip dependency decisions","release-note ordering","compatibility gate scripts","changelog alphabetization fixes"],
 "Prerelease identifiers compare lexically after numeric fields; an absent pre-release sorts higher \u2014 that is why rc builds never match production. Missing patch counts as zero.",
 "sv2",
 _f("sv2-a", "Version A", "1.10.0") + _f("sv2-b", "Version B", "1.9.5") +
 '''<button class="btn" onclick="sv2()">Compare versions</button>
  <div id="sv2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("json-to-query-string", "JSON to Query String Converter", "Developer Tools",
 "JSON objects into URL-safe query strings with keys sorted",
 "Query strings are a flat, URL-encoded stringly representation of what JSON models cleanly \u2014 and hand-building them is where percents get double-encoded. Paste a JSON object, and this converter answers the query string with proper percent-encoding, sorted keys for deterministic URLs, and the reverse decode check.",
 "each key\u2192value joins as key=value with encodeURIComponent; pairs join on & after key sorting",
 "{\"a\":\"1\",\"b\":\"x y\"} becomes a=1&b=x%20y \u2014 the space encodes, the ampersand stays structural",
 ["building API request URLs from fixtures","sharing filter states in links","webhook signature replay tests","spreadsheet-to-API pipelines"],
 "Nested objects flatten to JSON strings by design \u2014 flat query strings have no tree. Sort keys when a signature check hashes the URL; percent-encoding twice will corrupt it silently.",
 "jq2",
 '<div class="row"><div><label for="jq2-in">JSON object</label><textarea id="jq2-in" rows="4">{"a":"1","b":"x y","c":"a&b"}</textarea></div></div>' +
 '''<button class="btn" onclick="jq2()">Build the query string</button>
  <div id="jq2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("user-agent-parser", "User Agent Parser", "Developer Tools",
 "Browser, engine, operating system and device from any user agent",
 "Analytics rely on parsing user agents, and every analytics dashboard builder ultimately ships the same regex ladder. Paste a UA string, and this parser answers the browser with version, the rendering engine, the operating system, the device class and whether it is a bot \u2014 all client-side.",
 "match ordered regexes: edge/opr/version-first for chromium forks, then firefox, safari, msie; os against nt/mac/android/iphone",
 "a Chrome-on-Windows string parses Chrome, engine Blink, OS Windows, desktop \u2014 while Edg in the same string must be caught before Chrome wins",
 ["analytics dashboard debugging","bot filtering in log pipelines","support-ticket environment triage","detection test fixtures"],
 "Order matters: Chromium forks UA-spoof as Chrome, so check Edge and Opera tokens first. UA strings are client-controlled and freely lied about \u2014 screen with feature detection where it counts.",
 "ua2",
 '<div class="row"><div><label for="ua2-in">User agent string</label><textarea id="ua2-in" rows="3">Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36</textarea></div></div>' +
 '''<button class="btn" onclick="ua2()">Parse the UA</button>
  <div id="ua2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("anchor-link-generator", "Anchor Link Generator", "Text Tools",
 "Markdown headings turned into jump links with GitHub-style ids",
 "Long documents need table-of-contents links, and heading-to-anchor slugging has unwritten rules: lowercase, punctuation stripped, spaces to hyphens. Paste markdown or plain headings, and this generator answers each heading's anchor id, ready-to-paste markdown links and the id attributes to set in HTML.",
 "slug = lowercase, strip punctuation apart from hyphens, spaces\u2192hyphens (GitHub heading rule)",
 "\"## Getting Started!\" anchors to #getting-started \u2014 and the generated list jumps readers straight to it",
 ["long readme tables of contents","blog post navigation blocks","documentation site templates","course handout web versions"],
 "Duplicate headings get -1, -2 suffixes on GitHub; keep names unique to stay portable. Emoji and accented characters slug differently across renderers \u2014 test where the doc will live.",
 "al2",
 '<div class="row"><div><label for="al2-in">Headings (markdown or plain), one per line</label><textarea id="al2-in" rows="4"># Introduction\n## Getting Started!\n### Advanced Settings</textarea></div></div>' +
 '''<button class="btn" onclick="al2()">Generate anchors</button>
  <div id="al2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("percent-error", "Percent Error Calculator", "Calculators",
 "Measured versus accepted value with the error percent and sign",
 "Experiments are judged on percent error, not raw difference \u2014 a gram off means differently at scales and quarries. Enter your measured value and the accepted or true one, and this calculator returns the absolute difference, the percent error, and the signed bias showing which way the technique misses.",
 "error = measured \u2212 true; percent error = |measured \u2212 true| \u00f7 |true| \u00d7 100",
 "measuring 9.8 against accepted 9.81 misses by 0.01 \u2014 0.10%, comfortably inside school-lab tolerance",
 ["physics and chemistry lab reports","instrument calibration logs","forecast accuracy reviews","target-versus-actual reporting"],
 "Percent error needs a nonzero accepted value \u2014 near zero it explodes and absolute difference is the saner metric. Sign the error when bias matters; report magnitude when precision does.",
 "pe2",
 _f("pe2-m", "Measured (experimental) value", "9.8") + _f("pe2-t", "Accepted (true) value", "9.81") +
 '''<button class="btn" onclick="pe2()">Compute the error</button>
  <div id="pe2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("proportion-calculator", "Proportion Calculator", "Calculators",
 "The fourth member of any a:b :: c:x ratio, solved via cross-multiplication",
 "Recipes scale, maps shrink and currency pairs move on one relationship: two equal ratios share an unknown member. Enter the three knowns of a:b :: c:x, and this calculator cross-multiplies and solves for x \u2014 with the cross product shown so the setup is checkable.",
 "a:b :: c:x means a\u00d7x = b\u00d7c, so x = (b \u00d7 c) \u00f7 a",
 "2:3 :: 6:x solves to x = (3 \u00d7 6) \u00f7 2 = 9 \u2014 the same 1.5 scaling both pairs keep",
 ["recipe and mixture scaling","map and scale drawings","chemistry dilution homework","camera settings and framing"],
 "Ratios need consistent unit pairs: miles-to-gallons versus km-to-litres will invert silently. Zero first terms make the proportion undefined; the tool refuses them rather than divide.",
 "po2",
 _f("po2-a", "a (first term of pair A)", "2") + _f("po2-b", "b (second term of pair A)", "3") + _f("po2-c", "c (first term of pair B)", "6") +
 '''<button class="btn" onclick="po2()">Solve for x</button>
  <div id="po2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("remainder-calculator", "Remainder Calculator", "Calculators",
 "Quotient and remainder from any division, negatives handled honestly",
 "Division answers two questions at once, and programming languages disagree about one of them: how negatives round. Enter dividend and divisor, and this calculator returns the quotient, the remainder, the decimal expansion, and shows both the truncated and floored conventions side by side.",
 "quotient q and remainder r with a = q\u00d7b + r; Euclidean convention keeps 0 \u2264 r &lt; |b|",
 "17 \u00f7 5 leaves 3 remainder 2 \u2014 while \u221217 \u00f7 5 differs by language: \u22122 in truncated JavaScript, 3 remainder 2 in Euclidean",
 ["modular arithmetic homework","even/odd and cyclic grouping logic","hash bucketing checks","cross-language bug hunts"],
 "JavaScript's % follows the sign of the dividend; Python's follows the divisor \u2014 the same expression flips sign crossing languages. Clock arithmetic is the intuition: remainders wrap.",
 "rm2",
 _f("rm2-a", "Dividend", "17") + _f("rm2-b", "Divisor", "5") +
 '''<button class="btn" onclick="rm2()">Divide it out</button>
  <div id="rm2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("linear-equation-solver", "Linear Equation Solver", "Calculators",
 "Instant solution for any ax + b = cx + d form equation",
 "Two straight lines in disguise cross at one x \u2014 and fussing signs during rearrangement is where algebra homework loses marks. Fill in the four constants of ax + b = cx + d, and this solver isolates x step by step, shows the rearranged form, and refuses parallel lines by name.",
 "ax + b = cx + d rearranges to (a \u2212 c)x = d \u2212 b, so x = (d \u2212 b) \u00f7 (a \u2212 c) when the lines differ",
 "2x + 3 = 5x + 9 collapses to \u22123x = 6, so x = \u22122 \u2014 substituting back verifies both sides at 1",
 ["algebra homework verification","slope-intercept intersection checks","teaching rearrangement steps","spreadsheet break-even setups"],
 "The solver refuses a = c with b \u2260 d \u2014 identical slopes and different intercepts never meet, so no x exists. Fractions survive exactly here; decimals round only at display.",
 "le2",
 _f("le2-a", "a (coefficient of x, left)", "2") + _f("le2-b", "b (constant, left)", "3") + _f("le2-c", "c (coefficient of x, right)", "5") + _f("le2-d", "d (constant, right)", "9") +
 '''<button class="btn" onclick="le2()">Solve the equation</button>
  <div id="le2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("geometric-mean", "Geometric Mean Calculator", "Calculators",
 "The average that multiplies: growth rates, ratios and returns",
 "A stock up 50% then down 50% averages to zero by arithmetic while decisively losing you money \u2014 ratios need the mean that multiplies. Paste a list of positive numbers, and this calculator returns the geometric mean, the arithmetic contrast, and the count processed.",
 "GM = (x\u2081 \u00d7 x\u2082 \u2026 \u00d7 x\u2099)^(1/n), computed in log space for numerical stability",
 "2, 8 and 4 give a geometric mean of 4.00 against an arithmetic 4.67 \u2014 the multiplicative reading of growth",
 ["investment return averaging","ratio and index aggregation","scientific measurement sets","growth-series comparisons"],
 "Zeros and negatives break the geometric mean \u2014 screen the series first. It never exceeds the arithmetic mean, equality only when every value matches, a law worth trusting as a sanity check.",
 "gm2",
 '<div class="row"><div><label for="gm2-in">Positive numbers, separated by spaces or commas</label><textarea id="gm2-in" rows="3">2 8 4</textarea></div></div>' +
 '''<button class="btn" onclick="gm2()">Average multiplicatively</button>
  <div id="gm2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("nth-root-calculator", "Nth Root Calculator", "Calculators",
 "Any root of any number, with even-root and imaginary caveats",
 "Squares get a button; cubes, fifths and tenths deserve one too. Enter the number and the root, and this calculator evaluates with the power expression, reports the exact decimal, and refuses \u2014 with an explanation \u2014 the even roots of negative numbers that demand complex arithmetic.",
 "result = x^(1/n); even n with x &lt; 0 is complex, so declined; odd n inverts the sign of x",
 "27^(1/3) is exactly 3, and 1024^(1/10) is 2 \u2014 the same power button mathematicians wrote logarithm tables from",
 ["algebra and precalculus homework","engineering dimension checks","geometric-mean crosschecks","teaching inverse powers"],
 "Roots of order beyond about 15 lose meaning at display precision anyway; compare against exponent notation when it matters. Negative results are exact only for odd roots \u2014 even ones are where calculators lie historically.",
 "nr2",
 _f("nr2-x", "Number (x)", "27") + _f("nr2-n", "Root (n)", "3") +
 '''<button class="btn" onclick="nr2()">Take the root</button>
  <div id="nr2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("bakers-percentage", "Baker's Percentage Calculator", "Calculators",
 "Any dough scaled, every ingredient expressed against the flour",
 "Bakers never write a recipe in grams for one batch; they write percentages against flour, so scaling stays one multiplication. Enter your flour weight and hydration, salt and yeast percentages, and this calculator answers the grams for each plus total dough weight \u2014 and scales any real recipe inversely.",
 "flour = 100%; hydration% = water \u00f7 flour; salt \u2248 2%, yeast \u2248 1% of flour weight",
 "500 g flour at 65% hydration, 2% salt and 1% yeast takes 325 g water, 10 g salt, 5 g yeast \u2014 840 g of dough",
 ["bread and pizza dough scaling","converting recipes between batch sizes","hydration tuning experiments","sourdough feeding schedules"],
 "High hydration makes wetter, open crumb \u2014 beginner loaves do well nearer 60\u201365%. Ingredients never sum with flour to more than the percentages say, so check your arithmetic once.",
 "bk2",
 _f("bk2-f", "Flour weight (g)", "500") + _f("bk2-h", "Hydration (%)", "65") + _f("bk2-s", "Salt (%)", "2") + _f("bk2-y", "Yeast (%)", "1") +
 '''<button class="btn" onclick="bk2()">Scale the dough</button>
  <div id="bk2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("roast-timer", "Roast Timer Calculator", "Calculators",
 "Oven minutes and rest time for any roast, by weight and cut",
 "Overcooked Sunday roasts are weighing errors: minutes per kilogram times the bird plus a standing allowance, not instinct. Choose the roast and enter the weight, and this timer answers total oven time, a safe internal pull temperature, and the resting window that redistributes the juices.",
 "oven minutes = weight (kg) \u00d7 minutes-per-kg for the cut + standing overhead; rest 15\u201320 minutes",
 "a 3 kg chicken at 45 min/kg plus 20 overhead roasts 155 minutes \u2014 two hours 35, then rests 15 before carving",
 ["Sunday and holiday roasts","meat thermometer scheduling","oven timezone coordination for sides","freezer-to-oven defrost planning"],
 "Times assume a preheated oven and room-temperature meat from the fridge an hour out; stuffed birds add weight unexpectedly. A probe beats arithmetic at the endgame \u2014 trust the thermometer.",
 "rs3",
 _f("rs3-w", "Roast weight (kg)", "3") + _sel("rs3-m", "Roast type", [("chicken", "Whole chicken \u2014 45 min/kg + 20"), ("beef", "Beef (medium) \u2014 55 min/kg + 20"), ("pork", "Pork \u2014 45 min/kg + 25"), ("lamb", "Lamb leg \u2014 60 min/kg + 25"), ("turkey", "Turkey \u2014 40 min/kg + 30")]) +
 '''<button class="btn" onclick="rs3()">Time the roast</button>
  <div id="rs3-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("wallpaper-estimator", "Wallpaper Estimator", "Calculators",
 "Rolls needed for a room, pattern repeat included honestly",
 "Underestimating wallpaper costs a second trip that may never match the batch \u2014 dye lots wander. Enter room dimensions and roll length, set a pattern waste percentage, and this estimator returns usable wall area, roll coverage, and the rolls to buy with the waste margin already priced in.",
 "wall area = perimeter \u00d7 height; rolls = ceiling(area \u00d7 (1 + waste%) \u00f7 (roll length \u00d7 width))",
 "a 5\u00d74 m room, 2.8 m high, covers 50.4 m\u00b2 \u2014 ten 10 m rolls of 0.53 m width, eleven once a pattern is matched",
 ["home renovation shopping lists","accent-wall and stairwell jobs","quote-checking against decorators","rental refresh budgets"],
 "Batch numbers matter: buy everything from one dye lot in the same trip, returns included. Windows and doors can be ignored \u2014 the paper offcuts cover trims and errors better than optimism does.",
 "we2",
 _f("we2-l", "Room length (m)", "5") + _f("we2-w", "Room width (m)", "4") + _f("we2-h", "Wall height (m)", "2.8") + _f("we2-r", "Roll length (m)", "10") + _sel("we2-wa", "Pattern waste", [("0", "Plain \u2014 no extra"), ("15", "Striped \u2014 +15%"), ("25", "Large pattern \u2014 +25%")]) +
 '''<button class="btn" onclick="we2()">Estimate the rolls</button>
  <div id="we2-out" class="result" aria-live="polite"></div>'''))

ADV15.append(("landscape-coverage", "Landscape Coverage Calculator", "Calculators",
 "Soil, mulch or gravel volume, bag count and tonnage from any area",
 "Nobody second-guesses mulch until the truck arrives short bags or the delivery weighs double the budget. Enter the area, the depth in centimetres, bag size and material density, and this calculator answers the cubic metres, the number of bags, and the tonnage the delivery actually brings.",
 "volume m\u00b3 = area m\u00b2 \u00d7 depth m; bags = ceiling(volume \u00d7 1000 \u00f7 bag litres); tonnes = volume \u00d7 density",
 "20 m\u00b2 at 10 cm depth needs 2.0 m\u00b3 \u2014 67 bags of 30 L, or about 3.0 tonnes loose at typical mulch density",
 ["mulch and bark spread jobs","gravel paths and driveways","raised bed soil filling","landscape delivery cost checks"],
 "Settle and compaction eat depth \u2014 loose mulch spreads thin after rain, so a 10% overage is wisdom, not waste. Densities vary: gravel is triple bark, and weighs double on the invoice.",
 "lp2",
 _f("lp2-a", "Area to cover (m\u00b2)", "20") + _f("lp2-d", "Depth (cm)", "10") + _f("lp2-b", "Bag size (litres)", "30") + _f("lp2-t", "Material density (tonnes/m\u00b3)", "1.5") +
 '''<button class="btn" onclick="lp2()">Cover the ground</button>
  <div id="lp2-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV15:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA15[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'''<div class="panel">{extra}{tail}</div>''',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT15[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
