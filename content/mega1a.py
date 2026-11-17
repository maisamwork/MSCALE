# -*- coding: utf-8 -*-
import re, json
_WCRE = re.compile(r"[A-Za-z0-9'\u2019\-]+")

def _fmt(x):
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    s = f"{x:.6f}".rstrip("0").rstrip(".")
    return s

def _cnv(v, kind, fac, rev=False):
    if kind == "c2f":
        return (v - 32) * 5 / 9 if rev else v * 9 / 5 + 32
    if kind == "f2c":
        return v * 9 / 5 + 32 if rev else (v - 32) * 5 / 9
    if kind == "c2k":
        return v - 273.15 if rev else v + 273.15
    if kind == "f2k":
        return (v - 273.15) * 9 / 5 + 32 if rev else (v - 32) * 5 / 9 + 273.15
    return v / fac if rev else v * fac

CONV = [
("km-to-miles","Kilometers","km","Miles","mi","lin",0.621371,
 "Convert kilometers to miles instantly for travel, running and mapping",
 ["trip planning and route estimates","running and cycling distances","reading US road signs abroad","fuel and travel budgeting"],
 "The US and UK measure roads in miles while most of the world uses kilometers, so mixing them up can shift an arrival estimate by hours."),
("miles-to-km","Miles","mi","Kilometers","km","lin",1.609344,
 "Convert miles to kilometers for maps, runs and international travel",
 ["understanding US distance signs","comparing race distances","GPS and fitness data","vehicle range checks"],
 "Race distances are the classic trap: a marathon is 26.2 miles but 42.195 kilometers, and rounding at the wrong step distorts pace plans."),
("cm-to-inches","Centimeters","cm","Inches","in","lin",0.393701,
 "Convert centimeters to inches for shopping, crafts and specifications",
 ["online clothing and shoe sizes","furniture and TV dimensions","DIY and craft measurements","product spec sheets"],
 "Screen and furniture sizes are advertised in inches in most stores worldwide, while building codes and patterns are written in centimeters."),
("inches-to-cm","Inches","in","Centimeters","cm","lin",2.54,
 "Convert inches to centimeters exactly, using the 1959 treaty definition",
 ["school and homework problems","converting US product sizes","workshop and sewing plans","medical height records"],
 "Since 1959 the inch is defined as exactly 2.54 cm, yet many people still remember an old rounded value and drift off on larger numbers."),
("meters-to-feet","Meters","m","Feet","ft","lin",3.28084,
 "Convert meters to feet for construction, aviation and everyday heights",
 ["room and building dimensions","aviation altitude figures","human height comparisons","sports field layouts"],
 "Aviation worldwide uses feet for altitude while most ground measurements are metric, so pilots and engineers convert constantly."),
("feet-to-meters","Feet","ft","Meters","m","lin",0.3048,
 "Convert feet to meters with the exact 0.3048 factor",
 ["metric building plans","athletics track and field","land and room descriptions","science coursework"],
 "US property listings quote square feet and room sizes in feet, while architects abroad need meters — a wrong factor ruins a floor plan."),
("mm-to-inches","Millimeters","mm","Inches","in","lin",0.0393701,
 "Convert millimeters to inches for machining, 3D printing and hardware",
 ["3D printing and CNC work","screw and bolt sizes","camera sensor sizes","jewelry and watch sizing"],
 "Engineering drawings are metric almost everywhere, but tools and hardware in the US are imperial, so a 6 mm part meets a 1/4 inch slot."),
("yards-to-meters","Yards","yd","Meters","m","lin",0.9144,
 "Convert yards to meters for sports, fabric and landscaping",
 ["football and golf distances","fabric and textile buying","gardening and landscaping","swimming pool lengths"],
 "American football fields are measured in yards while nearly every other sport uses meters, and fabric is sold by the yard in the US only."),
("meters-to-km","Meters","m","Kilometers","km","lin",0.001,
 "Convert meters to kilometers for distances, runs and mapping",
 ["running and hiking logs","road and pipeline lengths","map scale work","GPS coordinate offsets"],
 "It is a simple 1000-step ladder, yet typos are common when moving the decimal point by hand across long strings of digits."),
("kg-to-lbs","Kilograms","kg","Pounds","lbs","lin",2.20462,
 "Convert kilograms to pounds for fitness, shipping and travel",
 ["gym and weight training","airline baggage limits","medical and vet records","package shipping costs"],
 "US gym plates and baggage limits are in pounds while medical charts worldwide use kilograms — mixing them can double a dose or a fee."),
("lbs-to-kg","Pounds","lbs","Kilograms","kg","lin",0.45359237,
 "Convert pounds to kilograms with the exact treaty factor",
 ["dosing and medical charts","luggage weight checks","wrestling and boxing classes","food packaging"],
 "Medication dosing is calculated in kilograms; entering a pound figure as kilograms is a documented cause of serious dosing errors."),
("grams-to-ounces","Grams","g","Ounces","oz","lin",0.03527396,
 "Convert grams to ounces for cooking, nutrition and postage",
 ["baking recipes","nutrition labels","coffee and tea portions","postal weight limits"],
 "Recipes from Europe list grams while US measuring cups and scales read ounces — converting halfway through a bake ruins texture."),
("ounces-to-grams","Ounces","oz","Grams","g","lin",28.349523,
 "Convert ounces to grams for recipes, labels and lab work",
 ["US recipe conversion","food logging and macros","supplement scoops","small package weights"],
 "An avoirdupois ounce is 28.35 grams, but a troy ounce (gold, silver) is 31.10 — using the wrong one misprices precious metals badly."),
("stone-to-kg","Stone","st","Kilograms","kg","lin",6.35029318,
 "Convert stone to kilograms for UK weight records",
 ["UK body weight figures","medical forms abroad","fitness progress tracking","sports weight categories"],
 "Body weight in the UK and Ireland is quoted in stone, which confuses everyone else — 12 stone is 76.2 kg, not 12 kg of anything."),
("celsius-to-fahrenheit","Celsius","\u00b0C","Fahrenheit","\u00b0F","c2f",None,
 "Convert Celsius to Fahrenheit for weather, ovens and thermostats",
 ["weather forecasts and travel","oven and recipe temperatures","thermostat settings","science homework"],
 "Oven dials in the US show Fahrenheit while European recipes list Celsius; 180 \u00b0C is 356 \u00b0F, and guessing 350 works only by luck."),
("fahrenheit-to-celsius","Fahrenheit","\u00b0F","Celsius","\u00b0C","f2c",None,
 "Convert Fahrenheit to Celsius instantly for weather and cooking",
 ["US weather reports","recipe temperature conversion","pool and spa settings","lab protocols"],
 "Subtracting 30 and halving is a rough party trick, not a conversion — it is off by 4 degrees at room temperature and worse at extremes."),
("celsius-to-kelvin","Celsius","\u00b0C","Kelvin","K","c2k",None,
 "Convert Celsius to Kelvin for physics and chemistry",
 ["gas law calculations","thermodynamics homework","material science data","astronomy figures"],
 "Kelvin has no degree sign and no negative values; writing 25 K instead of 298.15 K in a report is a 273-fold error."),
("fahrenheit-to-kelvin","Fahrenheit","\u00b0F","Kelvin","K","f2k",None,
 "Convert Fahrenheit to Kelvin through the exact two-step formula",
 ["US lab data in SI units","engineering coursework","cryogenics references","climate data sets"],
 "The two-step path (F to C, then C to K) is where sign errors creep in — the tool applies the combined formula in one move."),
("mph-to-kmh","Miles per hour","mph","Kilometers per hour","km/h","lin",1.609344,
 "Convert mph to km/h for driving abroad and vehicle specs",
 ["rental cars abroad","speedometer comparisons","cycling speed data","weather wind reports"],
 "US speed limits are in mph while cameras and maps in most countries use km/h — 60 mph is 96.6 km/h, not 60."),
("kmh-to-mph","Kilometers per hour","km/h","Miles per hour","mph","lin",0.621371,
 "Convert km/h to mph for US travel and spec sheets",
 ["driving in the US","treadmill and bike metrics","wind speed warnings","vehicle import paperwork"],
 "European cars show km/h; US roads post mph. Estimating 'divide by two' is 20 percent off at highway speeds."),
("knots-to-kmh","Knots","kn","Kilometers per hour","km/h","lin",1.852,
 "Convert knots to km/h for marine and aviation use",
 ["sailing and boating forecasts","flight planning","ferry timetables","wind warnings"],
 "A knot is one nautical mile per hour — about 15 percent faster than a land mile per hour — so treating them as equal distorts ETAs."),
("gb-to-mb","Gigabytes","GB","Megabytes","MB","data",1024,
 "Convert gigabytes to megabytes using the binary 1024 convention",
 ["file and folder sizes","download and quota checks","RAM and storage specs","backup planning"],
 "Operating systems count 1024 MB per GB while drive boxes say 1000 — that gap is why a '1 TB' disk shows about 931 GB."),
("mb-to-kb","Megabytes","MB","Kilobytes","KB","data",1024,
 "Convert megabytes to kilobytes for file sizes and limits",
 ["email attachment limits","web page weight budgets","image size targets","legacy file formats"],
 "Upload forms quote limits in KB while file managers show MB; being off by a factor of 1024 means a rejected upload."),
("tb-to-gb","Terabytes","TB","Gigabytes","GB","data",1024,
 "Convert terabytes to gigabytes for storage planning",
 ["NAS and server capacity","backup sizing","video project storage","cloud plan comparison"],
 "Marketing uses decimal terabytes and systems use binary gibibytes; planning a 4 TB array with the wrong convention loses capacity."),
("liters-to-gallons","Liters","L","US gallons","gal","lin",0.264172,
 "Convert liters to US gallons for fuel and liquids",
 ["fuel economy comparisons","paint and pool volumes","drink and tank sizes","chemical mixing"],
 "US mpg and UK mpg are not comparable because the gallons differ by 20 percent — always check which gallon a figure assumes."),
("gallons-to-liters","US gallons","gal","Liters","L","lin",3.785412,
 "Convert US gallons to liters for recipes, fuel and tanks",
 ["US recipe conversion","fuel tank capacity","aquarium sizing","irrigation planning"],
 "A US gallon is 3.785 L but an imperial gallon is 4.546 L; importing a recipe or spec without converting misjudges volume badly."),
("ml-to-fluid-ounces","Milliliters","ml","US fluid ounces","fl oz","lin",0.033814,
 "Convert milliliters to US fluid ounces for drinks and dosing",
 ["cocktail and coffee recipes","medicine doses","perfume bottle sizes","baby formula prep"],
 "US fluid ounces measure volume, not weight — 8 fl oz of honey does not weigh 8 ounces, and medicine cups depend on this difference."),
("cups-to-ml","US cups","cup","Milliliters","ml","lin",236.588,
 "Convert US cups to milliliters for accurate baking",
 ["American recipes","nutrition label serving sizes","sauce and batter scaling","kitchen scale work"],
 "The US legal cup is 236.588 ml but metric cups sold in Europe are 250 ml — a 6 percent difference that shows in delicate bakes."),
("sqft-to-sqm","Square feet","sq ft","Square meters","m\u00b2","lin",0.09290304,
 "Convert square feet to square meters for property and plans",
 ["apartment listings","flooring and paint estimates","office space leasing","solar panel layouts"],
 "The factor is squared (0.3048\u00b2), not 0.3048 — using the length factor overstates area by more than ten times."),
("sqm-to-sqft","Square meters","m\u00b2","Square feet","sq ft","lin",10.76391042,
 "Convert square meters to square feet for real estate and design",
 ["reading US property ads","material ordering","gym and studio layouts","warehouse planning"],
 "European listings quote m\u00b2 while US tenants think in sq ft; 90 m\u00b2 is about 969 sq ft, and rough doubling guesses mislead."),
("acres-to-hectares","Acres","ac","Hectares","ha","lin",0.40468564,
 "Convert acres to hectares for land and farm planning",
 ["farm and plot sizing","forestry management","property development","agricultural subsidies"],
 "An acre is 4,046.86 m\u00b2 and a hectare 10,000 m\u00b2 — assuming they are 'about the same' misstates land area by 2.5 times."),
("minutes-to-hours","Minutes","min","Hours","hr","lin",0.0166666667,
 "Convert minutes to hours for timesheets and planning",
 ["work timesheets","meeting and call logs","flight and train durations","study tracking"],
 "7.5 hours is a duration, but 7:50 is a clock time — writing one when you mean the other corrupts payroll and schedules."),
("hours-to-minutes","Hours","hr","Minutes","min","lin",60,
 "Convert hours to minutes for schedules and billing",
 ["billing in minute increments","recipe and process timing","workout intervals","service level targets"],
 "Decimal hours (2.75) and clock notation (2:45) get confused; billing systems usually want one or the other, never mixed."),
("minutes-to-seconds","Minutes","min","Seconds","sec","lin",60,
 "Convert minutes to seconds for timers and testing",
 ["workout and tabata timers","script and animation timing","chemical reaction logs","speed test sampling"],
 "A 90-second interval is 5400 milliseconds in some tools and 1.5 minutes in others — unit slips break timers and tests alike."),
("days-to-hours","Days","d","Hours","hr","lin",24,
 "Convert days to hours for deadlines and capacity planning",
 ["project deadlines","battery and uptime specs","travel itineraries","SLA Response windows"],
 "A calendar day with daylight saving can be 23 or 25 hours, but a duration day is always exactly 24 — know which one you need."),
("weeks-to-days","Weeks","wk","Days","d","lin",7,
 "Convert weeks to days for schedules and sprints",
 ["sprint and release planning","rental and booking periods","pregnancy and medical timelines","subscription trials"],
 "Sprint planning says 2 weeks, HR says 10 business days — calendar days and working days differ by roughly 40 percent."),
]

DOMAIN = {}
for s in ("km-to-miles","miles-to-km","cm-to-inches","inches-to-cm","meters-to-feet","feet-to-meters","mm-to-inches","yards-to-meters","meters-to-km"):
    DOMAIN[s] = "length"
for s in ("kg-to-lbs","lbs-to-kg","grams-to-ounces","ounces-to-grams","stone-to-kg"):
    DOMAIN[s] = "weight"
for s in ("celsius-to-fahrenheit","fahrenheit-to-celsius","celsius-to-kelvin","fahrenheit-to-kelvin"):
    DOMAIN[s] = "temp"
for s in ("mph-to-kmh","kmh-to-mph","knots-to-kmh"):
    DOMAIN[s] = "speed"
for s in ("gb-to-mb","mb-to-kb","tb-to-gb"):
    DOMAIN[s] = "data"
for s in ("liters-to-gallons","gallons-to-liters","ml-to-fluid-ounces","cups-to-ml"):
    DOMAIN[s] = "volume"
for s in ("sqft-to-sqm","sqm-to-sqft","acres-to-hectares"):
    DOMAIN[s] = "area"
for s in ("minutes-to-hours","hours-to-minutes","minutes-to-seconds","days-to-hours","weeks-to-days"):
    DOMAIN[s] = "time"

DOM = {
"length": {
 "ctx": "Length is the most converted measurement in everyday life because the world never agreed on a single system. The metric system, built around the meter, is official almost everywhere, while the United States still measures in inches, feet and miles. Anyone who shops online, follows a workout plan, reads a foreign pattern or works with international drawings meets both systems in the same week. A dedicated {fn} to {tn} converter removes the mental arithmetic and the risk of a slipped decimal point.",
 "w3": "The modern definitions are exact by international agreement: since 1959 the inch has been defined as exactly 2.54 centimeters, and every other length unit used here follows from that treaty value. That is why the factor this tool applies is a clean defined constant rather than a rounded approximation \u2014 converting {fs} to {ts} with it matches what engineering references and standards bodies publish.",
 "prac": "you are cutting a shelf to size and the plan quotes {n1} {fnl} while your tape measure and software work in {tnl}. Enter {n1}, read {r1} {ts}, and you can mark the cut line without pausing to look up a formula. Tap the swap button and the same figure converts back the other way in one click.",
 "n1": 10, "n2": 5,
 "mis": [
  "Confusing similar-looking unit abbreviations. The classic slip is treating a symbol as interchangeable with its neighbor \u2014 always check the label above the input box before trusting the result.",
  "Rounding before converting. If you round the {fs} value first, the error carries through to the {ts} result. Enter the full value you have and round only the final answer."],
 "faq": [
  ("Is this {fn} to {tn} conversion exact?", "Yes. The tool uses the internationally agreed definition of both units, so the result is exact up to the display precision. The {fs} to {ts} factor is a defined constant, not a measurement."),
  ("Why do some websites show a slightly different factor?", "Some sites round the conversion factor to fewer decimal places to keep results short. That is fine for rough estimates but drifts on large values. This tool keeps full precision internally and only rounds the displayed digits.")],
},
"weight": {
 "ctx": "Weight conversions matter most where two systems meet: cooking, shipping, fitness and medicine. Recipes from Europe list grams while US packages list ounces; airlines quote baggage in kilograms while travelers think in pounds; gym plates are labeled in both. The {fn} to {tn} converter on this page handles those everyday cases instantly, using the exact internationally agreed factors rather than rounded shortcuts.",
 "w3": "Since 1959 the pound has been defined as exactly 0.45359237 kilograms, which makes every weight conversion on this page a matter of clean multiplication. The gram, the ounce and the stone all derive from that same agreement, so converting {fs} to {ts} here matches the values printed on scientific references and customs paperwork.",
 "prac": "you are preparing a recipe that lists {n1} {fnl} but your scale reads {tnl}. Enter {n1}, read {r1} {ts}, and you can weigh ingredients straight away without stopping to search for the formula. The swap button converts the answer back if you need to double-check.",
 "n1": 70, "n2": 2.5,
 "mis": [
  "Mixing up weight and volume. Fluid ounces measure volume while ounces measure weight \u2014 a cup of flour does not weigh the same as a cup of sugar. Convert weight with weight units only.",
  "Entering the value in the wrong box. The label above each input shows its unit; if the direction is backwards, press the swap button instead of retyping the number."],
 "faq": [
  ("How precise is the {fs} to {ts} result?", "The converter computes at full floating-point precision and displays up to six meaningful decimals. For cooking or luggage that is far beyond what any scale reads, and for shipping it matches carrier rounding practice."),
  ("Does this tool work for precious metals?", "Only for standard avoirdupois units. Gold and silver are traded in troy ounces, which are about 10 percent heavier than ordinary ounces \u2014 never use a kitchen conversion for bullion pricing.")],
},
"temp": {
 "ctx": "Temperature is the one measurement where conversion is not a simple multiplication, because Celsius and Fahrenheit were built around different reference points and Kelvin starts at absolute zero. Weather reports, oven settings, lab protocols and thermostat apps all assume one scale, so a reliable {fn} to {tn} converter saves you from the classic off-by-a-lot errors that mental arithmetic produces.",
 "w3": "The formulas are fixed by definition: the Celsius and Fahrenheit scales intersect at \u221240 degrees, water freezes at 0 \u00b0C and 32 \u00b0F, and Kelvin is Celsius shifted so that 0 K is absolute zero. This tool applies those exact formulas in both directions, which is why \u221240 converts to \u221240 and body temperature lands on the familiar numbers you expect.",
 "prac": "a recipe written for {n1} {fnl} needs to run in an oven or thermostat marked in {tnl}. Enter {n1} and the converter shows {r1} {ts} \u2014 set the dial to that and the baking chemistry behaves exactly as the author intended.",
 "n1": 25, "n2": 98,
 "mis": [
  "Forgetting the offset. {fs} is not converted by multiplying alone \u2014 the freezing-point offset must be applied in the right order. The tool handles the order for you.",
  "Reversing the formulas. Adding 32 where you should subtract it produces a plausible-looking number that is wrong by dozens of degrees. Sanity-check against known points like freezing or body temperature."],
 "faq": [
  ("Why does \u221240 convert to itself?", "Because the Celsius and Fahrenheit scales intersect at \u221240 degrees: \u221240 \u00b0C is exactly \u221240 \u00b0F. It is the one temperature where no offset separates the two scales, and a quick way to check any converter is working."),
  ("When should I use Kelvin instead of Celsius?", "Kelvin is the scientific standard because it starts at absolute zero and has no negative values. Use it for physics, chemistry and thermal calculations; use Celsius or Fahrenheit for weather, cooking and everyday settings.")],
},
"speed": {
 "ctx": "Speed conversions appear whenever travel crosses a border: road trips in the United States post miles per hour while maps and cameras elsewhere use kilometers per hour, runners talk about pace, and sailors and pilots use knots. The {fn} to {tn} converter gives an instant answer so you can match local speed limits and expectations without doing arithmetic at highway speed.",
 "w3": "The factors come straight from the length definitions: the international mile is exactly 1.609344 kilometers and the nautical mile is exactly 1.852 kilometers, tied to the shape of the Earth. Because those constants are exact, converting {fs} to {ts} here agrees with official signage conversions and navigation software to the displayed precision.",
 "prac": "you are planning a road trip where the rental car shows {n1} {fnl} on the dashboard but the road signs are posted in {tnl}. Enter {n1}, read {r1} {ts}, and you can hold a legal, safe speed without guessing.",
 "n1": 60, "n2": 100,
 "mis": [
  "Treating knots like miles per hour. A knot is one nautical mile per hour and is about 15 percent faster than a land mile per hour \u2014 mixing them visibly distorts travel-time estimates.",
  "Converting distance but not speed, or the other way round. If your map switched to kilometers, your speed figure must switch too, or arrival estimates will be systematically wrong."],
 "faq": [
  ("How do I estimate {fs} to {ts} in my head?", "A useful approximation is to multiply by 1.6 and accept a little error \u2014 60 mph is about 96 to 97 km/h. The exact factor is 1.609344, which this tool applies so you never have to guess."),
  ("Do pilots and sailors really use knots?", "Yes. Aviation and marine navigation use knots because one nautical mile corresponds to one minute of latitude, which simplifies chart work. This tool converts knots to kilometers per hour whenever you need a land-based comparison.")],
},
"data": {
 "ctx": "Digital storage is quoted in units that look interchangeable but are not. Drive makers use decimal gigabytes, operating systems display binary units, and hosting plans mix both. The {fn} to {tn} converter uses the binary convention \u2014 one unit equals 1024 of the smaller unit \u2014 which is what file managers and memory specifications actually use, so the numbers here match what your computer reports.",
 "w3": "Under the binary convention used by operating systems, each step up multiplies by 1024: 1024 kilobytes make a megabyte and 1024 megabytes make a gigabyte. Standards bodies also define decimal units with a multiplier of 1000, which is why a \u201c500 GB\u201d drive shows less in Windows. For {fs} to {ts} questions about files and memory, the 1024-based answer matches your screen.",
 "prac": "you are checking whether a {n1} {fnl} download fits inside a plan or folder that is capped in {tnl}. Enter {n1}, read {r1} {ts}, and you know immediately whether the file fits or needs splitting.",
 "n1": 5, "n2": 750,
 "mis": [
  "Assuming 1000 instead of 1024. File sizes, RAM and quotas inside operating systems follow the 1024-based ladder; using 1000 understates every conversion.",
  "Confusing bits and bytes. Download speeds are usually quoted in megabits (Mb) while file sizes are megabytes (MB) \u2014 eight times apart. Check the case of the b before converting."],
 "faq": [
  ("Why does my 1 TB drive show about 931 GB?", "Drive makers use decimal terabytes (10 to the 12th bytes) while the operating system displays binary gibibytes (1024-based). Dividing 10 to the 12th by 1024 cubed gives about 931 binary gigabytes \u2014 both numbers describe the same physical drive."),
  ("Is a megabyte 1000 or 1024 kilobytes?", "It depends on context: storage marketing defines 1,000,000 bytes, while operating systems and memory traditionally use 1024 \u00d7 1024. This tool follows the 1024 convention that matches what file managers show.")],
},
"volume": {
 "ctx": "Volume conversions decide whether a recipe works, whether fuel money adds up and whether a shipment fits regulations. The catch is that the US and the rest of the world not only use different units \u2014 a US gallon is smaller than an imperial gallon \u2014 they also label cups and ounces differently. This {fn} to {tn} converter sticks to US customary values, the ones used in American recipes and fuel pricing.",
 "w3": "The US gallon is defined as exactly 3.785411784 liters, and the fluid ounce, cup and pint all derive from it. Because those definitions are fixed by law, converting {fs} to {ts} with this tool reproduces the values on nutrition labels and engineering tables exactly.",
 "prac": "you are scaling a recipe that calls for {n1} {fnl} but your measuring jug is marked in {tnl}. Enter {n1}, read {r1} {ts}, and you can pour to the right line with confidence instead of eyeballing a conversion mid-recipe.",
 "n1": 4, "n2": 500,
 "mis": [
  "Mixing US and imperial units. A US gallon is about 3.785 liters but an imperial (UK) gallon is about 4.546 liters \u2014 a 20 percent difference. This page converts US units.",
  "Treating a US cup as 250 milliliters. The US legal cup used in nutrition is 236.588 ml; metric measuring cups sold elsewhere are 250 ml. Recipes drift noticeably at large scales."],
 "faq": [
  ("Are US and UK gallons the same?", "No. The US gallon is 3.785 liters and the imperial gallon used in the UK is 4.546 liters \u2014 about 20 percent larger. Always check which gallon a fuel price or recipe means before converting."),
  ("What cup is this converter based on?", "The US customary cup of 236.588 milliliters, which is what American recipes and nutrition labels assume. If your recipe comes from a country using metric cups, use 250 ml per cup instead.")],
},
"area": {
 "ctx": "Area conversions come up in real estate, construction, agriculture and interior design \u2014 anywhere floor plans, land plots or material coverage cross between measurement systems. Because area units are squares of length units, the conversion factors are squared too, and that is exactly where mental arithmetic fails. The {fn} to {tn} converter applies the correct squared factor instantly.",
 "w3": "The international foot is exactly 0.3048 meters, so one square foot is exactly 0.3048 squared \u2014 about 0.09290304 square meters. The acre and hectare hang off that same system: an acre is 4,046.856 square meters and a hectare is exactly 10,000. Converting {fs} to {ts} with these constants matches survey records and planning documents.",
 "prac": "you are pricing flooring for a room listed as {n1} {fnl} but the material is sold per {tnl}. Enter {n1}, read {r1} {ts}, and you can compare quotes fairly instead of eyeballing two incompatible price tags.",
 "n1": 1200, "n2": 90,
 "mis": [
  "Using the length factor instead of the area factor. Converting square feet to square meters with 0.3048 instead of 0.092903 is off by more than a factor of ten \u2014 always convert area with squared factors.",
  "Forgetting that price per unit must be converted too. A price per square foot cannot be compared with a price per square meter until both the area and the price basis are on the same unit."],
 "faq": [
  ("Why is the area factor not just the length factor?", "Area is two-dimensional: a square foot is a foot on each side, so both side lengths must be converted and then multiplied. That squares the factor \u2014 0.3048 \u00d7 0.3048 gives 0.09290304 square meters per square foot."),
  ("How big is a hectare compared to an acre?", "A hectare is 10,000 square meters and equals about 2.471 acres. It is the standard land unit in most of the world, while acres dominate in the US and UK.")],
},
"time": {
 "ctx": "Time conversions run through everything from payroll and project planning to cooking timers and workout intervals. Unlike length or weight, the units are perfectly regular \u2014 60 seconds, 60 minutes, 24 hours, 7 days \u2014 so the arithmetic is simple, but doing it repeatedly, in your head, while busy invites slips. The {fn} to {tn} converter answers instantly and shows a reference table for common values.",
 "w3": "The relationships are exact by definition: one minute is 60 seconds, one hour is 60 minutes, one day is 24 hours and one week is 7 days, giving clean factors with no rounding at all. The only wrinkle is daylight saving time, which affects calendar arithmetic \u2014 a day can be 23 or 25 hours \u2014 but not pure duration conversion like {fs} to {ts}.",
 "prac": "you are filling in a timesheet that logs {n1} {fnl} but the billing system expects {tnl}. Enter {n1}, read {r1} {ts}, and the entry lines up with what payroll or the client expects to see.",
 "n1": 90, "n2": 48,
 "mis": [
  "Applying decimal hours to clock time. 7.5 hours is a duration; 7:50 on a clock is a different thing entirely. Convert durations here and read clock times directly.",
  "Forgetting that a workday is not 24 hours. When converting staffing or billing time, decide whether a \u201cday\u201d means 24 hours or an 8-hour workday before converting."],
 "faq": [
  ("Does daylight saving time affect this conversion?", "No. This tool converts pure durations, and a minute is 60 seconds regardless of the calendar. Daylight saving only matters when you add durations to a specific clock date."),
  ("How do I convert decimal hours to hours and minutes?", "Multiply the decimal part by 60. For example 2.75 hours is 2 hours and 0.75 \u00d7 60 = 45 minutes. The hours calculator on this site does this automatically for start and end times.")],
},
}

def _extra_faqs(fn, tn):
    return [
 ("Why do I need a tool for such a simple calculation?", f"You often don't \u2014 until you are doing it a dozen times a day. Hand arithmetic with {fn.lower()} and {tn.lower()} invites small errors that compound across a document, and a tool guarantees every figure uses the same exact constant."),
 ("What if my value is very large or very small?", f"The converter handles any number your device can represent, from fractions of a {fn.lower()} to millions. Results switch to more decimal places automatically so tiny differences stay visible."),
 ("Can I convert in the other direction too?", f"Yes \u2014 press the swap button and the page becomes a {tn} to {fn} converter instantly, keeping the value you already typed."),
 ("Does the tool remember what I typed?", "No. The conversion happens in your browser's memory only; nothing is stored, logged or sent to a server, and refreshing the page clears the fields."),
 ("Is this converter free to use?", "Yes, completely \u2014 no sign-up, no limits and no ads inside the tool area. It is one of many free converters available on this site."),
 ("Can I use it offline?", "Once the page has loaded, the conversion runs entirely in your browser, so it keeps working if your connection drops."),
 ("How should I round the result?", "Keep one more decimal place than you actually need, then round at the very end. Rounding intermediate values is the most common source of drift in multi-step work."),
 ("Why does the result show more decimals than I need?", f"Precision is kept high so the value is trustworthy for any downstream use; you can simply read fewer digits. For {fn.lower()} to {tn.lower()} work where only two decimals matter, ignore the rest."),
]

def conv_article(f):
    slug, fn, fs, tn, ts, kind, fac, short, uses, got = f
    dom = DOM[DOMAIN[slug]]
    n1, n2 = dom["n1"], dom["n2"]
    r1 = _fmt(_cnv(n1, kind, fac))
    r2 = _fmt(_cnv(n2, kind, fac, rev=True))
    ra = _fmt(_cnv(1, kind, fac))
    if kind == "lin":
        formula = f"the fixed factor {_fmt(fac)}: {fs} \u00d7 {_fmt(fac)} = {ts}"
        ftxt = f"1 {fn.lower()} equals exactly {_fmt(fac)} {tn.lower()}"
    elif kind == "c2f":
        formula = "the exact two-part formula: \u00b0F = \u00b0C \u00d7 9/5 + 32"
        ftxt = "the formula multiplies by 9/5 and adds the 32-degree freezing-point offset"
    elif kind == "f2c":
        formula = "the exact two-part formula: \u00b0C = (\u00b0F \u2212 32) \u00d7 5/9"
        ftxt = "the formula removes the 32-degree offset first, then rescales by 5/9"
    elif kind == "c2k":
        formula = "the exact offset formula: K = \u00b0C + 273.15"
        ftxt = "the formula shifts the scale so zero becomes absolute zero at \u2212273.15 \u00b0C"
    else:
        formula = "the combined exact formula: K = (\u00b0F \u2212 32) \u00d7 5/9 + 273.15"
        ftxt = "the formula rescales to Celsius and then shifts to absolute zero in one step"
    intro = [
        f"The {fn} to {tn} converter on this page gives an instant, exact answer to one of the most common unit questions there is. Type a value in either box and the other side updates as you type \u2014 no formula to remember, no rounding to manage, no page reload. It is built for {uses[0]}, {uses[1]} and {uses[2]}, and it behaves the same on a phone as on a desktop.",
        dom["ctx"].format(fn=fn, tn=tn, fs=fs, ts=ts),
        dom["w3"].format(fn=fn, tn=tn, fs=fs, ts=ts),
    ]
    how = (f"Using the converter takes seconds. Click into the {fn.lower()} box and type your value; the {tn.lower()} result appears immediately, rounded to a sensible number of decimals. "
           f"If your starting figure is in {tn.lower()} instead, press the swap button between the two boxes \u2014 the labels flip, the direction reverses and the value you already typed moves across, so nothing is re-entered. "
           f"Underneath, a reference table lists pre-computed conversions for common values such as 1, 5, 10, 25, 50 and 100, which is handy when you are comparing several figures at once. "
           "Everything runs locally in your browser, so the tool keeps working if your connection drops and nothing you type is transmitted anywhere.")
    steps = [
        f"Enter the value you want to convert in the {fn.lower()} ({fs}) input box.",
        f"Read the converted {tn.lower()} ({ts}) value in the second box \u2014 it updates as you type.",
        "Scan the reference table underneath for common values; it saves retyping when you compare several amounts.",
        f"Press the swap button to reverse direction if your starting value is actually in {tn.lower()}.",
        "Use the copy button next to the result if you need the number in a document, email or spreadsheet.",
        "Round the final answer to the precision your task actually needs \u2014 two decimals is plenty for most everyday work.",
    ]
    works = [
        f"At its core the converter applies {formula}. In plain terms, {ftxt}, so every result is deterministic: the same input always produces the same output, on any device, in any browser.",
        f"Precision is handled deliberately. The page computes with full floating-point accuracy and only rounds what it displays, so a {fs} value you check today will match one you check next week to the last shown digit. Very large results gain separators for readability, and very small ones keep enough decimals to stay meaningful.",
        "There is no server round-trip. The conversion logic is a few lines of JavaScript that run the instant you press a key, which is why the result feels immediate and why the tool is safe to use for anything private \u2014 nothing leaves your device.",
    ]
    examples = [
        (f"{_fmt(n1)} {fn} to {tn}",
         f"Enter {_fmt(n1)} in the left box. The converter applies the exact relationship and shows {r1} {ts}. This is the figure to copy into your notes \u2014 and because it came from the defined constant rather than a remembered approximation, it will agree with any reference table you check it against."),
        (f"{_fmt(n2)} {tn} back to {fn}",
         f"Press the swap button, then enter {_fmt(n2)} in the now-upper box. The tool returns {r2} {fn.lower()}, confirming the round trip: converting there and back lands on the number you started with, which is the quickest way to verify any converter is set up correctly."),
        (f"A practical {DOMAIN[slug]} example",
         f"In real work, {dom['prac'].format(fn=fn, tn=tn, fs=fs, ts=ts, fnl=fn.lower(), tnl=tn.lower(), n1=_fmt(n1), r1=r1)}"),
    ]
    mistakes = [
        dom["mis"][0].format(fn=fn, tn=tn, fs=fs, ts=ts),
        dom["mis"][1].format(fn=fn, tn=tn, fs=fs, ts=ts),
        got,
        "Typing commas, units or spaces into the input. The field expects a plain number such as 12.5 \u2014 formatted text like \u201c12,5 km\u201d will read as invalid or truncate at the comma.",
        "Trusting rounded mental math for large values. A shortcut that is fine at 10 units can be hundreds of units wrong at 10,000; use the tool whenever the figure matters.",
    ]
    tips = [
        f"Anchor it in memory: 1 {fs} = {ra} {ts}. Knowing one fixed pair lets you sanity-check any result at a glance.",
        "Use the swap button rather than retyping when you need the reverse direction \u2014 it preserves your value and eliminates transcription errors.",
        "State both units in documents (\u201c" + f"{r1} {ts} ({_fmt(n1)} {fs})" + "\u201d) so any reader can verify the figure without asking.",
        "Bookmark this page if you make this conversion regularly; loading it is faster than searching for a formula each time.",
        "On your phone, add the page to your home screen \u2014 it works like an app and needs no connection after the first load.",
        f"If a downstream system needs a specific number of decimals, round the {ts} value once, at the end, and keep the raw value in your notes.",
    ]
    faqs = [dom["faq"][0], dom["faq"][1]] + [
        ("Is the conversion the same as the one in my search engine?", "Yes \u2014 the factor is the internationally defined constant, so this tool, search engines and printed reference tables all agree. Small differences elsewhere come from rounding the factor itself, not from a different definition."),
        ("Can I use decimals and negative numbers?", "Yes. The input accepts any decimal value, and negative values are handled correctly \u2014 useful for temperature differences, altitude-style figures and accounting adjustments."),
        ("Does the tool store or send what I type?", "No. The conversion happens entirely in your browser's memory; nothing is transmitted, logged or saved, and closing the tab clears everything."),
        ("Why does the reference table stop at certain values?", "The table shows the values people look up most often. For any other value, simply type it into the input box and the exact result appears \u2014 the table is a convenience, not a limit."),
    ]
    a = {"intro": intro, "how": [how], "steps": steps, "works": works,
         "examples": examples, "mistakes": mistakes, "tips": tips, "faqs": faqs}
    return _fit(a)

_EXTRA = None
def _pool():
    global _EXTRA
    if _EXTRA is None:
        _EXTRA = {}
    return _EXTRA

def _fit(a, floor=1010, ceil=1195):
    fn, tn = a.get("_fn", "value"), a.get("_tn", "value")
    while _wc(a) < floor and len(a["faqs"]) < 8:
        a["faqs"].append(_extra_faqs(fn, tn)[len(a["faqs"]) % 8])
    while _wc(a) > ceil:
        if len(a["faqs"]) > 5:
            a["faqs"].pop()
        elif len(a["tips"]) > 4:
            a["tips"].pop()
        elif len(a["mistakes"]) > 4:
            a["mistakes"].pop()
        else:
            break
    return a

def _wc(a):
    texts = list(a["intro"]) + [a["how"][0]] + list(a["steps"]) + list(a["works"])
    texts += [f"{t} {b}" for t, b in a["examples"]]
    texts += list(a.get("mistakes", []))
    texts += list(a["tips"])
    texts += [f"{q} {x}" for q, x in a["faqs"]]
    return len(_WCRE.findall(" ".join(texts)))

SWAP_SVG = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 3 4 7l4 4"/><path d="M4 7h16"/><path d="m16 21 4-4-4-4"/><path d="M20 17H4"/></svg>'

def conv_body(f):
    slug, fn, fs, tn, ts, kind, fac, short, uses, got = f
    ra = _fmt(_cnv(1, kind, fac))
    conf = json.dumps({"k": kind, "f": fac, "fl": fn + " (" + fs + ")", "tl": tn + " (" + ts + ")"})
    return f'''<div class="panel uc-panel">
  <div class="uc-note">Type a value in either box \u2014 the other updates instantly. 1 {fs} = {ra} {ts}.</div>
  <div class="uc-row">
    <div class="uc-side">
      <label class="uc-fl" for="uc-in" id="uc-fl">{fn} ({fs})</label>
      <input id="uc-in" class="in" type="number" step="any" value="1" inputmode="decimal" autocomplete="off">
    </div>
    <button id="uc-swap" class="btn ghost uc-swap" type="button" aria-label="Swap units" title="Swap units">{SWAP_SVG}</button>
    <div class="uc-side">
      <label class="uc-tl" for="uc-out" id="uc-tl">{tn} ({ts})</label>
      <input id="uc-out" class="in" type="text" readonly aria-live="polite">
    </div>
  </div>
  <div class="uc-actions"><button id="uc-copy" class="btn ghost" type="button">Copy result</button></div>
  <div class="uc-tablewrap"><table class="uc-table" id="uc-table" aria-label="Common conversions"></table></div>
</div>
<script>window.UC_CONF={conf};</script>'''
