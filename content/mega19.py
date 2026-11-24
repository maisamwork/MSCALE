# -*- coding: utf-8 -*-
"""Batch 29 module D: 19 flagship tools (kitchen, pets, garden, DIY)."""
from .mega1b import calc_article
from .mega3 import _f, _sel

MEGA19 = {}
CONTENT19 = {}

ADV19 = []

ADV19.append(("egg-timer", "Egg Timer Guide", "Calculators",
 "Boil times for every egg size, temperature and doneness",
 "Egg timing is a collision of size, starting temperature and altitude that recipes pretend is a fixed number. Pick the size, the fridge temperature and the target doneness, and this timer answers the minutes, the carry-over adjustment once the water returns to a boil, and the ice-bath rule that stops the grey ring.",
 "minutes scale with size: large from fridge \u2014 soft 6, medium 8, hard 10\u201312; +1 for straight from the fridge, +2 at high altitude",
 "a large fridge-cold egg at six minutes gives a jammy centre \u2014 eight makes it medium, twelve sets it fully and starts the grey rim",
 ["breakfast precision","ramen and salad prep","meal-prep batches","altitude cooking"],
 "Start timing only when the water returns to a full boil after the eggs go in \u2014 not from the switch. Ice water stops the cooking at the centre in seconds; skipping it adds another minute of carry-over heat.",
 "eg2",
 _sel("eg2-s", "Egg size", [("l", "Large \u2014 standard"), ("m", "Medium \u22121 min"), ("xl", "Extra large +30s")]) + _sel("eg2-t", "Start temp", [("f", "Straight from the fridge"), ("r", "Room temperature \u22121 min")]) + _sel("eg2-d", "Doneness", [("6", "Soft \u2014 runny yolk"), ("8", "Medium \u2014 jammy yolk"), ("11", "Hard \u2014 fully set")]) +
 '''<button class="btn" onclick="eg2()">Time the egg</button>
  <div id="eg2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("tea-steep-guide", "Tea Steep Guide", "Calculators",
 "Temperature, minutes and resteeps for every tea family",
 "Green tea scalded at boiling and black tea steeped for thirty seconds are the same mistake pointed in opposite directions. Pick the tea family and the form, and this guide answers the water temperature, the steep minutes, how many infusions the leaves will still give, and what going over buys \u2014 and ruins.",
 "green 70\u201380\u00b0C 2 min; oolong 85\u201390\u00b0C 3 min; black 95\u2013100\u00b0C 3\u20134 min; herbal 100\u00b0C 5 min; resteeps fall from the first",
 "a green steeped at 80\u00b0C for two minutes stays sweet \u2014 the same leaves at 100\u00b0C pull catechins that read as pure bitterness",
 ["loose-leaf brewing","office kettle discipline","gift-tea instructions","cold-brew conversion"],
 "Higher mountain-grown greens take heat better \u2014 adjust up a degree or two if it tastes thin. The second resteep often out-tastes the first.",
 "te2",
 _sel("te2-t", "Tea family", [("g", "Green \u2014 78\u00b0C, 2 min"), ("o", "Oolong \u2014 88\u00b0C, 3 min"), ("b", "Black \u2014 98\u00b0C, 3.5 min"), ("h", "Herbal \u2014 100\u00b0C, 5 min"), ("w", "White \u2014 75\u00b0C, 2.5 min")]) + _sel("te2-l", "Form", [("l", "Loose leaves \u2014 resteeps 3\u00d7"), ("b", "Bag \u2014 single steep")]) +
 '''<button class="btn" onclick="te2()">Steep it right</button>
  <div id="te2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("rice-ratio", "Rice Water Ratio Calculator", "Calculators",
 "The exact water ratio for every rice, scaled to any cups",
 "The finger-knuckle method travels badly across rice types, pot shapes and stoves. Pick the rice, enter the cups dry, and this calculator answers the water by cup and millilitre, the cooked yield, the servings, and the resting time off-heat that finishes the job the simmer started.",
 "white 1:1.5, jasmine 1:1.25, basmati 1:1.5 soaked, brown 1:2; cooked yield \u2248 dry \u00d7 2.5\u20133",
 "two cups of brown rice take four of water and 40 minutes \u2014 yielding about 4.8 cooked cups, six generous servings",
 ["weekday dinner rice","rice-cooker transplants","batch meal prep","cuisine-specific texture"],
 "Rinsing removes surface starch and changes nothing about the ratio \u2014 measure the same water after rinsing. Resting ten minutes off heat with the lid closed matters as much as the simmer itself.",
 "ri2",
 _sel("ri2-t", "Rice type", [("w", "White long grain \u2014 1:1.5"), ("j", "Jasmine \u2014 1:1.25"), ("b", "Basmati \u2014 1:1.5 soaked"), ("br", "Brown \u2014 1:2")]) + _f("ri2-c", "Dry cups", "2") +
 '''<button class="btn" onclick="ri2()">Measure the pot</button>
  <div id="ri2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("pasta-portion", "Pasta Portion Calculator", "Calculators",
 "Dry grams per person with pot water and salt scaled too",
 "Restaurants plate 80 grams dry per person; packets serve six on paper and nobody in particular in practice. Enter the diners and appetite level, and this calculator answers the dry pasta in grams, the boiling water the pot needs, and the salt that seasons it properly instead of cosmetically.",
 "dry = 80 g per person standard, 100 g hearty; water = 1 L per 100 g; salt = 7 g per litre",
 "four hearty diners need 400 g dry pasta, four litres of water and 28 g of salt \u2014 the pot that actually fits",
 ["family dinner planning","batch cooking nights","dinner-party portions","pantry shopping lists"],
 "The water rule keeps strands free without sticky rescues; a smaller pot with more stirring also works. Save a cup of the salted water \u2014 it binds sauce where cream would drown it.",
 "pa3",
 _f("pa3-n", "Diners", "4") + _sel("pa3-a", "Appetite", [("80", "Standard \u2014 80 g"), ("100", "Hearty \u2014 100 g"), ("60", "Side dish \u2014 60 g")]) +
 '''<button class="btn" onclick="pa3()">Portion the pot</button>
  <div id="pa3-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("overnight-oats", "Overnight Oats Builder", "Calculators",
 "Scaled oats, liquid and toppings for jars of tomorrow's breakfast",
 "Overnight oats are a ratio disguised as a recipe, which is why half the jars on the internet set like concrete. Enter the number of jars and the milk base, and this builder answers the oats, liquid, yoghurt, chia and salt in grams, plus the minimum fridge hours before the texture arrives.",
 "base per jar: 40 g oats, 100 ml milk, 40 g yoghurt, 6 g chia, pinch of salt; fridge 6+ hours",
 "four jars take 160 g oats and 400 ml milk \u2014 assembled in eight minutes, breakfast solved across four mornings",
 ["weekday breakfast batching","high-protein versions","gym-day fueling","kids' self-serve breakfasts"],
 "Steel-cut oats stay chalky overnight \u2014 rolled oats are the only reliable body; quick oats turn to paste. Chia keeps hybridising the texture: past ten grams per jar you are making pudding.",
 "oo2",
 _f("oo2-j", "Jars", "4") + _sel("oo2-m", "Milk base", [("c", "Cow's milk \u2014 classic"), ("o", "Oat drink \u2014 slightly sweeter"), ("a", "Almond \u2014 lighter body")]) +
 '''<button class="btn" onclick="oo2()">Build the jars</button>
  <div id="oo2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("air-fryer-converter", "Air Fryer Converter", "Calculators",
 "Oven recipes translated to the basket: lower heat, less time",
 "Air fryers are small convection ovens with a temper: roughly twenty degrees cooler and twenty percent faster than the oven the recipe was written for. Enter the oven temperature and time, and this converter answers the basket settings, the halfway flip mark, and when to start checking early.",
 "fryer \u00b0C = oven \u00b0C \u2212 20; fryer minutes = oven minutes \u00d7 0.8; start checking from halfway",
 "an oven bake of 200\u00b0C for 20 minutes runs in the basket at 180\u00b0C for 16 minutes \u2014 shake or flip at the eighth",
 ["frozen snack timing","converting tray-bake recipes","small-batch weeknight cooking","reheating leftovers crisply"],
 "Batter-coated and wet items fly in basket currents \u2014 weigh the lattice or line it. Fat content matters: the method reheats crisply but dries lean meats past the converted time, so check early.",
 "af2",
 _f("af2-t", "Oven temperature (\u00b0C)", "200") + _f("af2-m", "Oven time (minutes)", "20") +
 '''<button class="btn" onclick="af2()">Set the basket</button>
  <div id="af2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("slow-cooker-converter", "Slow Cooker Converter", "Calculators",
 "Oven recipes translated to low and high slow-cooker hours",
 "The slow cooker borrows recipes and repays them in hours: an oven hour is four on high or eight on low. Enter the oven time and temperature, and this converter answers both slow settings, the liquid trim the sealed pot demands, and the right moment for dairy.",
 "oven 15\u201330 min \u2192 low 4\u20136 h / high 1.5\u20132 h; 30\u201345 min \u2192 low 6\u20138 h / high 3\u20134 h; longer \u2192 low 8\u201310 h / high 4\u20136 h",
 "a one-hour oven braise becomes eight hours on low \u2014 same tenderness, a fraction of the electricity",
 ["winter batch cooking","work-morning assembly","tough-cut stew planning","holiday side dishes"],
 "Cut liquid by a third \u2014 the sealed pot evaporates nearly nothing. Dairy and fresh herbs go in the last thirty minutes, or they split and fade.",
 "do2",
 _f("do2-t", "Oven time (minutes)", "60") + _f("do2-d", "Oven temperature (\u00b0C)", "180") +
 '''<button class="btn" onclick="do2()">Convert to slow</button>
  <div id="do2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("grill-burger-time", "Grill Burger Timer", "Calculators",
 "Minutes per side and target internal temperature by thickness",
 "Burgers punish guesswork twice \u2014 raw in the middle or hockey pucks \u2014 and thickness is the variable recipes never state. Enter the patty thickness and target doneness, and this timer answers the minutes per side, the internal temperature to hit, and the rest that keeps the juices where the sear invited them.",
 "2 cm patty medium: 4\u20135 min per side toward 63\u00b0C internal; about 45 seconds more per side per extra half centimetre",
 "a 2-centimetre patty to medium runs four to five minutes a side \u2014 pull at 63\u00b0C and rest five minutes under foil",
 ["backyard burger nights","smash vs thick patty planning","food-safe doneness targets","frozen-patty adjustments"],
 "Only ground poultry demands 74\u00b0C throughout \u2014 beef at 63\u00b0C with a rest is the kitchen-safe medium. Pressing the patty with the spatula squeezes out exactly the juice you just protected; stop.",
 "gb2",
 _f("gb2-t", "Patty thickness (cm)", "2") + _sel("gb2-d", "Doneness", [("55", "Medium-rare \u2014 55\u00b0C"), ("63", "Medium \u2014 63\u00b0C"), ("71", "Well done \u2014 71\u00b0C")]) +
 '''<button class="btn" onclick="gb2()">Time the patty</button>
  <div id="gb2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("dog-age-advanced", "Dog Age Calculator", "Calculators",
 "Real canine aging by size class, not the seven-to-one myth",
 "The multiply-by-seven rule survives because it is easy, and it is wrong at both ends of a dog's life. Enter the dog's age and size class, and this calculator applies the veterinary curve \u2014 fast maturing early, slower after \u2014 plus the epigenetic logarithm labs quote, and flags the giant-breed senior threshold.",
 "size curve: year one 15, year two 24, then +5 small, +6 medium, +7 large, +9 giant per year; lab formula 16 \u00d7 ln(age) + 31",
 "a five-year-old labrador reads 45 by the size curve \u2014 and 56.8 by the DNA-methylation formula vets increasingly quote",
 ["vet appointment forms","senior-dog care planning","insurance age bands","adoption paperwork"],
 "Giant breeds cross into senior care around six \u2014 the seven-to-one arithmetic has them feeling young precisely when screenings matter. Both formulas agree on the shape and disagree politely in the middle years.",
 "da2",
 _f("da2-d", "Dog's age (years)", "5") + _sel("da2-s", "Size class", [("5", "Small (under 10 kg) \u2014 +5"), ("6", "Medium (10\u201325 kg) \u2014 +6"), ("7", "Large (25\u201340 kg) \u2014 +7"), ("9", "Giant (over 40 kg) \u2014 +9")]) +
 '''<button class="btn" onclick="da2()">Age the dog</button>
  <div id="da2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("cat-calories", "Cat Calorie Calculator", "Calculators",
 "RER-based daily calories with neuter and activity factors",
 "Cats manage weight on a knife edge \u2014 half a kilo either direction is a health event \u2014 and food bags quote feeding ranges wide enough to lose a diet in. Enter the cat's weight, life stage and food energy, and this calculator answers the resting requirement, the daily target after the multiplier, and the grams per day.",
 "RER = 70 \u00d7 weight kg^0.75; neutered adult \u00d71.2, intact \u00d71.4, weight-loss \u00d70.8, kitten \u00d72.5; grams = kcal \u00f7 kcal/kg \u00d7 1000",
 "a 4 kg neutered house cat needs about 198 kcal at rest \u2014 238 target, which is 59 g of a 4000 kcal/kg food over two meals",
 ["indoor cat weight control","multi-cat feeding plans","post-neuter adjustment","vet diet transitions"],
 "The 0.75 exponent is fate for chunky cats: heavier does not scale linearly, and free-feeding quietly wins every contest.",
 "cc3",
 _f("cc3-w", "Cat's weight (kg)", "4") + _sel("cc3-s", "Life stage", [("1.2", "Neutered adult \u2014 \u00d71.2"), ("1.4", "Intact adult \u2014 \u00d71.4"), ("0.8", "Weight-loss plan \u2014 \u00d70.8"), ("2.5", "Kitten under 6 months \u2014 \u00d72.5")]) + _f("cc3-d", "Food energy (kcal/kg)", "4000") +
 '''<button class="btn" onclick="cc3()">Feed the maths</button>
  <div id="cc3-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("aquarium-heater", "Aquarium Heater Calculator", "Calculators",
 "Heater wattage matched to tank size and room conditions",
 "Undersized heaters run flat out and still lose winter; oversized ones overshoot when thermostats stick. Enter the tank volume, room temperature and target, and this calculator answers the minimum watts by the 2.5-watt-per-gallon rule scaled to the temperature rise, the sensible upper bound, and the two-heater option for big tanks.",
 "watts = gallons \u00d7 2.5 baseline, scaled by \u0394\u00b0F; roughly double the wattage if the room drops below 60\u00b0F",
 "a 20-gallon tank in a 65\u00b0F room warming to 78\u00b0F wants about 39 watts of rule \u2014 buy the 50, or run two 25s for redundancy",
 ["tropical tank setup","winter outage planning","quarantine tank equipping","heater upgrade checks"],
 "One degree of overshoot stresses fish faster than one degree of undershoot \u2014 buy the steady size, not the fast one. Two smaller heaters at opposite ends heat evenly and survive single-failure winters.",
 "aq2",
 _f("aq2-g", "Tank gallons", "20") + _f("aq2-r", "Room temperature (\u00b0F)", "65") + _f("aq2-t", "Target water (\u00b0F)", "78") +
 '''<button class="btn" onclick="aq2()">Size the heater</button>
  <div id="aq2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("plant-watering", "Plant Watering Calculator", "Calculators",
 "Litres per session from pot size, interval and season",
 "Overwatering kills more houseplants than forgetting combined, and the pot decides the dose more than the plant does. Enter the pot diameter and depth, the interval between waterings and the season, and this calculator answers the soil volume, the litres per session \u2014 about a fifth of capacity \u2014 and the weekly total for a can marked in litres.",
 "soil litres = \u03c0 \u00d7 (d/2)\u00b2 \u00d7 depth; session = volume \u00d7 0.2 \u00d7 season factor; weekly = session \u00d7 (7 \u00f7 interval)",
 "a 20 cm-wide, 18 cm-deep pot holds 5.65 litres \u2014 water with about 1.1 litres whenever the top two knuckles dry",
 ["houseplant routines","holiday watering instructions","summer heat waves","drainage troubleshooting"],
 "The one-fifth rule assumes drainage holes; without them every number poisons the roots. Test before pouring \u2014 the knuckle test beats any calendar, and winter cuts most intervals roughly in half.",
 "pn2",
 _f("pn2-d", "Pot diameter (cm)", "20") + _f("pn2-h", "Pot depth (cm)", "18") + _f("pn2-i", "Watering interval (days)", "5") + _sel("pn2-s", "Season", [("1", "Growing season"), ("0.6", "Winter \u2014 water less")]) +
 '''<button class="btn" onclick="pn2()">Dose the can</button>
  <div id="pn2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("seed-starting", "Seed Starting Planner", "Calculators",
 "Sow and transplant dates backwards from your last frost",
 "Every seed packet states weeks before last frost as if everyone knew their date \u2014 this planner does the calendar. Enter your last-frost date and pick the crop, and it answers the sow date, the transplant window, the weeks under lights and the hardening-off week that decides whether the seedlings survive the move.",
 "sow date = last frost \u2212 crop weeks (tomato 6, pepper 8, brassica 4, lettuce 3); transplant after frost with one hardening week",
 "tomatoes for a 15 May frost start indoors by 3 April \u2014 six weeks under lights, one hardening off, planting out mid-May",
 ["spring seedling calendars","greenhouse scheduling","succession sowing plans","school garden projects"],
 "Peppers and aubergines want eight-plus weeks and warmth; starting them alongside the tomatoes wastes their head start. Count backwards from your own local date \u2014 packets print zones, your calendar prints truth.",
 "sd4",
 _f("sd4-f", "Last frost date", "2026-05-15") + _sel("sd4-c", "Crop", [("6", "Tomato \u2014 6 weeks"), ("8", "Pepper \u2014 8 weeks"), ("4", "Brassica \u2014 4 weeks"), ("3", "Lettuce \u2014 3 weeks")]) +
 '''<button class="btn" onclick="sd4()">Plan the starts</button>
  <div id="sd4-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("concrete-mix", "Concrete Mix Calculator", "Calculators",
 "Cement bags, sand and gravel from any slab volume",
 " Concrete ordering errors arrive as a cold half-slab or a surcharge for the returned truck. Enter the slab area and depth, and this calculator converts the volume through the 1:2:3 field mix into cement kilograms, bag counts, and sand and gravel volumes \u2014 plus the 10% the pour always drinks.",
 "dry volume = wet \u00d7 1.54; cement = dry \u00f7 6 \u00d7 1440 kg; sand = dry \u00f7 3; gravel = dry \u00d7 0.51 m\u00b3 per m\u00b3 dry",
 "a 4 m\u00b2 slab at 10 cm is 0.4 m\u00b3 \u2014 about 148 kg of cement, six 25-kg bags, 0.21 m\u00b3 sand and 0.31 m\u00b3 gravel",
 ["garden path pours","shed base preparation","post-hole anchoring","job-site order checks"],
 "The 1:2:3 mix suits footings and paths; structural work belongs to a supplier's graded concrete, not a shovel. Order the extra 10% \u2014 ground suction and uneven formwork eat slab depth invisibly.",
 "cm3",
 _f("cm3-a", "Slab area (m\u00b2)", "4") + _f("cm3-t", "Depth (cm)", "10") +
 '''<button class="btn" onclick="cm3()">Batch the pour</button>
  <div id="cm3-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("plywood-sheet-cut", "Plywood Sheet Cut Calculator", "Calculators",
 "Sheets needed from piece count and the cuts per sheet",
 "Cabinet plywood prices make every wasted sheet a small injury, and nesting cuts on paper beats discovering them at the saw. Enter the piece size, the sheet size and how many pieces the project needs, and this calculator answers the pieces each sheet yields in a plain grid, the sheets to buy and the waste left over.",
 "pieces per sheet = floor(sheet L \u00f7 piece L) \u00d7 floor(sheet W \u00f7 piece W); sheets = ceil(pieces \u00f7 per sheet)",
 "600 \u00d7 600 panels cut two by two from a 2440 \u00d7 1220 sheet \u2014 four along, two across, eight per sheet, so eighteen panels buy three sheets",
 ["cabinet carcass building","shelving projects","workshop material orders","CNC sheet planning"],
 "A plain grid ignores rotation and nesting \u2014 real cut lists often fit one more piece per sheet. Check grain direction before rotating pieces in your head; veneered sheets do not forgive it.",
 "py2",
 _f("py2-l", "Piece length (mm)", "600") + _f("py2-w", "Piece width (mm)", "600") + _f("py2-n", "Pieces needed", "18") + _f("py2-sl", "Sheet length (mm)", "2440") + _f("py2-sw", "Sheet width (mm)", "1220") +
 '''<button class="btn" onclick="py2()">Nest the cuts</button>
  <div id="py2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("fence-post-spacing", "Fence Post Calculator", "Calculators",
 "Post count, rail count and concrete from one fence line",
 "Fence posts follow the oldest rule in building \u2014 spacing decides everything \u2014 and fences fail exactly where that rule was approximated. Enter the run length, the post spacing and the rail rows, and this calculator answers the post total, the rail metres to buy, and the concrete each post hole wants on your bag size.",
 "posts = floor(length \u00f7 spacing) + 1; rails = (posts \u2212 1) \u00d7 rows \u00d7 spacing; one 20 kg bag per post hole",
 "a 30-metre run at 2-metre spacing takes 16 posts \u2014 60 rail-metres across two rows, and 16 bags of post mix",
 ["garden and boundary fencing","holding pen repairs","trellis and windbreak lines","quote verification"],
 "Tighten spacing to 1.8 metres when the ground is soft or the fence faces weather \u2014 extra posts cost less than one storm. Corner and gate posts carry triple load: they get concrete, not soil.",
 "fp2",
 _f("fp2-l", "Fence length (m)", "30") + _f("fp2-s", "Post spacing (m)", "2") + _f("fp2-r", "Rail rows", "2") +
 '''<button class="btn" onclick="fp2()">Line the posts</button>
  <div id="fp2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("grout-area", "Grout Area Calculator", "Calculators",
 "Kilograms of grout from tile size, joint width and depth",
 "Grout is bought by the kilo and returned by the bucket, because coverage maths hides in tile geometry. Enter the tile size, joint width, joint depth and the area, and this calculator answers the joint length per square metre, the grout volume and the kilograms the job consumes, with the standard 10% margin.",
 "joint length per m\u00b2 = 2 \u00f7 tile size m; volume = length \u00d7 joint width \u00d7 depth; kg = volume \u00d7 1.6 density",
 "300 mm tiles with 3 mm joints at 8 mm depth need about 0.26 kg per m\u00b2 \u2014 a 20 m\u00b2 floor buys 5.6 kg with margin",
 ["bathroom tiling","floor tile jobs","mosaic sheet planning","grout purchasing lists"],
 "Deep joints drink more than wide ones \u2014 the depth input outranks the width for once. Epoxy grouts cover differently; check the manufacturer's own chart before ordering anything pricier than cement-based.",
 "ga2",
 _f("ga2-t", "Tile size (mm)", "300") + _f("ga2-w", "Joint width (mm)", "3") + _f("ga2-d", "Joint depth (mm)", "8") + _f("ga2-a", "Area (m\u00b2)", "20") +
 '''<button class="btn" onclick="ga2()">Batch the grout</button>
  <div id="ga2-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("roof-pitch", "Roof Pitch Calculator", "Calculators",
 "Angle, slope and rafter length from any rise-over-run",
 "Roofers speak in twelfths, surveyors in degrees and suppliers in rafter multipliers \u2014 the same roof wearing three uniforms. Enter the rise per twelve of run, and this calculator converts pitch into angle, percentage slope, the rafter multiplier that prices the timber, and the ridge height a given building width produces.",
 "angle = atan(rise \u00f7 12); multiplier = \u221a(1 + (rise/12)\u00b2); ridge height = half-span \u00d7 rise/12",
 "a 6-in-12 pitch is 26.57\u00b0 at 50% slope \u2014 every horizontal metre of run is really 1.118 metres of timber",
 ["material quote conversions","rafter cutting layout","solar-mount angle checks","snow-load assessments"],
 "Multipliers price rafters only \u2014 hips and valleys run shallower and longer, which is why quotes exceed the simple line. Below 3-in-12, shingles become a drainage liability whatever the sales sheet says.",
 "rp3",
 _f("rp3-r", "Rise per 12 of run", "6") + _f("rp3-h", "Building width (m, optional)", "8") +
 '''<button class="btn" onclick="rp3()">Solve the roof</button>
  <div id="rp3-out" class="result" aria-live="polite"></div>'''))

ADV19.append(("stair-stringer", "Stair Stringer Calculator", "Calculators",
 "Step count, rise per step and stringer length from any drop",
 "Stairs built from round numbers walk like chores; stairs built from the total rise divided by even steps disappear underfoot. Enter the total rise and the code maximum per step, and this calculator answers the step count, the true unit rise, the tread depth it pairs with, and the stringer length to mark out.",
 "steps = ceil(total rise \u00f7 max rise); unit rise = total \u00f7 steps; stringer = \u221a(unit_rise\u00b2 + tread\u00b2) \u00d7 (steps \u2212 1) + nosing",
 "a 279 cm total rise cleared at the 17.5 cm code max takes 16 steps of 17.4 cm \u2014 every one identical, which is the safety",
 ["deck and porch stairs","basement stair rebuilds","building-code checks","loft ladder alternatives"],
 "The rule that matters is consistency: variation between steps, not their height, is what trips people. Headroom of two metres clears above the nosing line, not above the raw landing.",
 "st4",
 _f("st4-r", "Total rise (cm)", "279") + _f("st4-m", "Max rise per step (cm)", "17.5") + _f("st4-t", "Tread depth (cm)", "28") +
 '''<button class="btn" onclick="st4()">Mark the stringer</button>
  <div id="st4-out" class="result" aria-live="polite"></div>'''))

for slug, name, cat, short, about, formula, exline, uses, got, fn, extra in ADV19:
    tail = ('<div id="m3-stats" class="jf-stats" style="margin-top:12px"></div>'
            '<div class="lr2-actions" style="margin-top:6px">'
            '<button type="button" class="btn ghost" onclick="m3Copy(this)">Copy result</button></div>'
            '<script>window.M3_FN="{fn}";</script>'.format(fn=fn))
    MEGA19[slug] = {"name": name, "cat": cat, "short": short,
                    "body": f'<div class="panel">{extra}{tail}</div>',
                    "desc": f"{short}. Shows the working, runs entirely in your browser \u2014 free with no sign-up."}
    CONTENT19[slug] = calc_article((slug, name, short, about, formula, exline, uses, got, fn, extra))
