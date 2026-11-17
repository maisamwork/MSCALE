# -*- coding: utf-8 -*-
import json
from .mega1a import _fit
from .mega2a import M2DOM, m2_article, TEXT, COLOR, TXF, tx_body, col_body

RAND = [
("random-letter","Random Letter Generator","Random Generators","Draw random letters A\u2013Z, in either case, any count",
 "A random letter is the seed of a surprising number of games and drills: word games, alphabet practice, password-style challenges, brainstorming constraints ('name a brand starting with\u2026'). This generator draws unbiased letters from A to Z, in upper or lower case, as many as you need, each press independent and instant.",
 ["word games and classroom drills","brainstorming constraints","picking fair starting letters","practice and quiz generation"],
 "Each letter is drawn independently, so repeats are normal \u2014 that is what unbiased randomness looks like.",
 "A classroom vocabulary drill","Set the count to 5, press Generate, and five letters appear \u2014 students get two minutes to name a country, an animal and a food for each. Press again and the round restarts with fresh letters.",
 "letter"),
("random-word","Random Word Generator","Random Generators","Draw random common English words for games and prompts",
 "A random common word is a writing prompt, a pictionary card, a password-practice item, a brainstorming seed. This generator draws from a built-in list of the most common English words \u2014 no obscure dictionary trivia \u2014 so every result is a word people actually know and can use immediately.",
 ["creative writing prompts","party and drawing games","vocabulary practice","brainstorming warm-ups"],
 "The list is common words on purpose \u2014 if you need rare or technical vocabulary, provide your own list with the list randomizer instead.",
 "A five-minute writing prompt","Set the count to 3, press Generate, and three words appear \u2014 write for five minutes weaving all of them in. Repeat daily and the blank page never wins.",
 "word"),
("random-date","Random Date Generator","Random Generators","Pick a random date within any range you set",
 "A random date in a range is useful more often than it seems: sample records for testing, 'on this day' features, fair scheduling of inspections or reviews, and history exercises. This generator picks a uniformly random date between your start and end dates \u2014 every date in the range equally likely, boundaries included.",
 ["test data for calendars and forms","fair scheduling of audits or reviews","history and classroom exercises","sampling records for QA"],
 "Both boundary dates are included in the draw, and leap years are handled correctly \u2014 a range spanning February 29 can produce it.",
 "Generating test data for a booking form","Set the range to this year, generate ten dates, and paste them into your test suite \u2014 the form now faces a realistic spread of weekdays, weekends and month ends.",
 "date"),
("list-randomizer","List Randomizer","Random Generators","Shuffle any list into a truly random order",
 "Shuffling decides presentation orders, prize draw sequences, presentation slots and quiz question order \u2014 and doing it 'by feel' is neither fair nor convincing. Paste any list, one entry per line, and this tool returns the same entries in a fresh random order, using the Fisher\u2013Yates shuffle that professional libraries use.",
 ["prize draw and raffle order","randomizing quiz question order","assigning presentation slots","shuffling flashcards"],
 "The shuffle is unbiased Fisher\u2013Yates: every one of the possible orders is exactly equally likely, with no positional bias.",
 "Randomizing a presentation order","Paste the presenter names, press Shuffle, and read the order aloud \u2014 everyone saw the same draw, so nobody argues the sequence was rigged.",
 "shuffle"),
("random-name-picker","Random Name Picker","Random Generators","Draw one or more winners fairly from a list of names",
 "Giveaways, classroom picks, chore rosters, stand-up speaking order \u2014 anywhere a name must be chosen fairly, a visible random draw beats a pointing finger. Paste your names, say how many winners you need, and the tool draws them without repeats, showing the result large enough for a room to see.",
 ["giveaway and raffle winners","picking students in class","volunteer and chore allocation","stand-up order in meetings"],
 "Winners are drawn without replacement \u2014 the same name cannot win twice in one draw \u2014 and blank lines in the input are ignored.",
 "Drawing three winners from an entry list","Paste the entries, set winners to 3, press Pick, and three distinct names appear \u2014 screenshot the result and the draw is documented as fair.",
 "picker"),
("yes-no-decider","Yes or No Decider","Random Generators","Get an instant, unbiased yes-or-no answer",
 "Small decisions eat disproportionate time: which task first, order-in or cook, try the idea or park it. When the stakes are low and the options are two, a coin flip is the honest tool \u2014 and this is a coin flip that cannot land on its edge. Press the button, get YES or NO, and let the decision be made.",
 ["breaking decision deadlocks","quick meeting tie-breakers","personal productivity games","settling friendly arguments"],
 "Decide before pressing whether you will obey the answer \u2014 the tool's value comes from ending the loop, not from being overruled.",
 "Ending a two-option debate","Both options look fine and the meeting is stalling: press the button once, read the answer, move on. The debate cost five seconds instead of fifteen minutes.",
 "yesno"),
("random-team-splitter","Random Team Splitter","Random Generators","Split a list of people into balanced random teams",
 "Fair teams are the difference between a fun exercise and a grumble: classroom projects, sports days, hackathons, quiz nights. Paste the names, say how many teams you want, and the tool deals people out randomly and as evenly as the count allows \u2014 no captains picking, no cliques, no arguments.",
 ["classroom group work","hackathon and event teams","sports and game days","workshop breakout groups"],
 "With uneven counts, some teams get one extra member \u2014 the tool spreads the remainder so no team is more than one person heavier.",
 "Splitting a class into four groups","Paste thirty names, set teams to 4, press Split \u2014 four balanced lists appear, ready to project. Re-splitting gives a fresh arrangement if the teacher wants a remix later.",
 "teams"),
("lottery-number-generator","Lottery Number Generator","Random Generators","Draw random unique lottery numbers in any range",
 "Every number combination in a lottery is equally likely, so any pick is as good as another \u2014 but a machine-generated set avoids the human habit of clustering on birthdays, which caps picks at 31 and shares jackpots. Set how many numbers you need and the range they come from; the tool draws unique, sorted numbers instantly.",
 ["lottery and raffle picks","sweepstake number sets","random sampling for games","picking unique numbers for draws"],
 "The numbers are unique and sorted, but the draw is not cherry-picked for you \u2014 no generator improves lottery odds, and anyone claiming otherwise is selling something.",
 "A lottery line without birthday bias","Set 6 numbers from 1\u201359, press Generate, and a sorted unique line appears \u2014 including high numbers birthday-based picks would never touch.",
 "lottery"),
("random-country-generator","Random Country Generator","Random Generators","Draw a random country with its region for games and study",
 "Geography games, travel lotteries, 'cook a dish from somewhere new' challenges and quiz rounds all start with one random country. This generator draws from a built-in list of the world's countries and shows the region too, so the draw is instantly usable as a fact and a constraint.",
 ["geography games and quizzes","travel and food challenges","random research prompts","classroom icebreakers"],
 "The list covers the widely recognized sovereign states \u2014 for territories and dependencies, add your own list to a list randomizer.",
 "A cook-something-new challenge","Press Generate, get a country and its region, and the week's kitchen assignment is set \u2014 no arguing, no re-rolls without agreement.",
 "country"),
("random-quote-generator","Random Quote Generator","Random Generators","Draw a random quote for inspiration and warm-ups",
 "A good quote is a meeting opener, a journal prompt, a slide footer, a signature waiting to happen. This generator draws from a curated set of genuine, attributed quotes \u2014 no filler and no misattributed internet specials \u2014 and shows the author alongside the words.",
 ["meeting and lesson openers","journaling prompts","social media posts","presentations and newsletters"],
 "Quotes are shown with their authors \u2014 if you republish one, keep the attribution; it is both polite and accurate.",
 "Opening a team meeting","Press Generate, read the quote aloud, and give everyone thirty seconds to react \u2014 the room starts engaged instead of silent.",
 "quote"),
]

DATE2 = [
("add-days-to-date","Add Days to Date","Date & Time Tools","Add or subtract days from any date, correctly",
 "Deadlines, delivery windows, trial periods, return policies, notice periods \u2014 a huge share of date questions are 'what date is N days from X?' and the calendar's irregular months make mental math unreliable. This tool adds or subtracts any number of days from any date, respecting real month lengths and leap years, and shows the resulting weekday too.",
 ["project deadline calculation","return and trial period windows","contractual notice periods","event and travel planning"],
 "The tool counts calendar days \u2014 every day including weekends. For working-day arithmetic, use the business days calculator instead.",
 "Finding a 30-day return deadline","Pick the purchase date, enter 30, press Calculate, and the exact deadline date and its weekday appear \u2014 no counting mistakes when the window crosses a month boundary.",
 "adddays"),
("day-of-week-finder","Day of Week Finder","Date & Time Tools","Find the weekday of any date, past or future",
 "What day was the moon landing? What day does your birthday fall on next year? What day is that invoice due? The weekday of a date is the fact everyone needs and nobody can compute mentally beyond this week. This tool names the weekday for any date in the Gregorian calendar, plus the day of year for context.",
 ["checking deadlines and due days","history and trivia questions","planning around weekdays","verifying calendar entries"],
 "The Gregorian calendar is used for all dates, including years before its historical adoption \u2014 historical purists should remember older dates used Julian reckoning.",
 "Checking a birthday's weekday next year","Pick next year's date, press Find, and the weekday appears instantly \u2014 enough to know whether the party is a Friday or needs a Saturday shift.",
 "dayofweek"),
("week-number-calculator","Week Number Calculator","Date & Time Tools","Get the ISO-8601 week number of any date",
 "Week numbers run Europe's calendars: work planning, school terms, delivery schedules and factory maintenance are all quoted in 'week 37'. But week numbering has rules \u2014 week 1 is the one containing the year's first Thursday \u2014 and guessing produces off-by-one errors. This tool returns the correct ISO week number for any date.",
 ["European business planning","delivery and production schedules","school and academic calendars","reporting periods and sprints"],
 "The tool uses ISO-8601 week numbering (Monday start, first Thursday rule) \u2014 the US convention of a Sunday start with different week 1 rules will differ in edge weeks.",
 "Checking which week a delivery lands in","Pick the delivery date, press Calculate, and the ISO week number appears \u2014 quote it to a European supplier and both sides mean the same seven days.",
 "weeknumber"),
("leap-year-checker","Leap Year Checker","Date & Time Tools","Test any year for leap status, with the rule explained",
 "The leap rule has a twist most people miss: divisible by 4 is a leap year, except centuries, which must be divisible by 400 \u2014 so 2000 was a leap year but 1900 was not, and 2100 will not be. This checker applies the full rule to any year, explains which clause decided it, and lists the next leap years.",
 ["date arithmetic and testing","birthday and anniversary planning","software test cases","curiosity and teaching"],
 " century years are the trap: 2000 yes, 1900 no, 2100 no \u2014 the 'every four years' shortcut fails exactly there.",
 "Checking whether 2100 will be a leap year","Enter 2100, press Check, and the tool explains: divisible by 100 but not 400, so no \u2014 February 2100 has 28 days, and software that assumes otherwise will fail.",
 "leap"),
("seconds-to-hms","Seconds to H:M:S Converter","Date & Time Tools","Turn a raw seconds count into readable hours, minutes, seconds",
 "Durations arrive as raw seconds from APIs, logs, timers and spreadsheets \u2014 14,537 seconds means nothing to a human and everything to a machine. This converter splits any seconds count into hours, minutes and seconds, and shows the combined H:MM:SS string ready for a report or a timesheet.",
 ["reading durations from logs and APIs","converting stopwatch exports","timesheet and billing entries","media and file duration math"],
 "The tool converts pure durations \u2014 there is no clock or time zone involved, so 90 minutes is 1:30:00 regardless of when it starts.",
 "Turning a log duration into report form","Paste 14537, press Convert, and read 4:02:17 \u2014 the duration a human can check against a schedule, copied straight into the report.",
 "s2hms"),
("hms-to-seconds","H:M:S to Seconds Converter","Date & Time Tools","Convert hours, minutes and seconds into total seconds",
 "Many systems want the opposite of a readable duration: timers, API parameters, spreadsheet formulas and rate calculations all take seconds. This converter takes hours, minutes and seconds and returns the exact total \u2014 the fastest way to feed a human-form duration into a machine-form field.",
 ["setting timer and API parameters","spreadsheet duration math","rate calculations (per second)","script and animation timing"],
 "Enter zero in fields you do not need \u2014 leaving a field blank counts as zero too, but explicit zeros make the intent clear when you re-read it.",
 "Converting 1h 45m for a timer field","Enter 1, 45 and 0, press Convert, and 6300 appears \u2014 paste it into the timer parameter and the duration is exactly what you meant.",
 "hms2s"),
("military-time-converter","Military Time Converter","Date & Time Tools","Convert between 12-hour and 24-hour clock time",
 "The 24-hour clock eliminates the AM/PM ambiguity that causes missed flights and doubled meetings \u2014 but half the world lives in 12-hour time. This converter translates either way: type 2:45 PM and read 14:45, or paste 07:30 and read 7:30 AM, with the midnight and noon edge cases handled correctly.",
 ["reading timetables and itineraries","military, aviation and medical charts","international scheduling","setting devices and systems"],
 "Midnight is 00:00 in 24-hour time and 12:00 AM in 12-hour time \u2014 the two edge cases where casual conversion goes wrong.",
 "Converting a European departure time","The ticket says 21:15; enter it, convert, and read 9:15 PM \u2014 the shuttle is booked for the right half of the day.",
 "military"),
("business-days-calculator","Business Days Calculator","Date & Time Tools","Count working days between two dates, weekends excluded",
 "Contracts, SLAs, shipping estimates and payroll all run on business days \u2014 but counting them by hand across month boundaries is exactly the kind of arithmetic that goes quietly wrong. This tool counts the business days between two dates, excluding weekends, and shows the total calendar days alongside so both numbers are on record.",
 ["SLA and contract timelines","shipping and delivery estimates","payroll and invoicing periods","project milestone planning"],
 "The count excludes Saturdays and Sundays but not public holidays \u2014 holidays vary by country, so subtract them manually where they fall inside your range.",
 "Checking a 10-business-day SLA","Pick the start and due dates, press Calculate, and the business-day count appears \u2014 if it reads 10 or more, the deadline is met even though the calendar span looks longer.",
 "bizdays"),
]

def rand_body(kind):
    if kind == "letter":
        ui = ('<div class="row"><div><label for="rl-n">How many letters</label><input type="number" id="rl-n" value="5" min="1" max="50" step="1"/></div>'
              '<div><label for="rl-case">Case</label><select id="rl-case"><option value="U">Uppercase (A\u2013Z)</option><option value="L">Lowercase (a\u2013z)</option></select></div></div>'
              '<button class="btn" onclick="rnLetter()">Generate</button>'
              '<div id="rl-out" class="result big-res" aria-live="polite"></div>')
    elif kind == "word":
        ui = ('<div class="row"><div><label for="rw-n">How many words</label><input type="number" id="rw-n" value="3" min="1" max="20" step="1"/></div></div>'
              '<button class="btn" onclick="rnWord()">Generate</button>'
              '<div id="rw-out" class="result big-res" aria-live="polite"></div>')
    elif kind == "date":
        ui = ('<div class="row"><div><label for="rd-a">From</label><input type="text" id="rd-a" class="dt-input" readonly placeholder="Pick start date"/></div>'
              '<div><label for="rd-b">To</label><input type="text" id="rd-b" class="dt-input" readonly placeholder="Pick end date"/></div></div>'
              '<button class="btn" onclick="rnDate()">Generate</button>'
              '<div id="rd-out" class="result big-res" aria-live="polite"></div>')
    elif kind == "shuffle":
        ui = ('<label for="ls-in">Your list (one entry per line)</label>'
              '<textarea id="ls-in" rows="7" placeholder="One entry per line\u2026"></textarea>'
              '<button class="btn" onclick="rnShuffle()">Shuffle list</button>'
              '<label for="ls-out">Shuffled list</label>'
              '<textarea id="ls-out" rows="7" readonly></textarea>')
    elif kind == "picker":
        ui = ('<label for="np-in">Names (one per line)</label>'
              '<textarea id="np-in" rows="7" placeholder="One name per line\u2026"></textarea>'
              '<div class="row"><div><label for="np-n">How many winners</label><input type="number" id="np-n" value="1" min="1" step="1"/></div></div>'
              '<button class="btn" onclick="rnPick()">Pick winner(s)</button>'
              '<div id="np-out" class="result big-res" aria-live="polite"></div>')
    elif kind == "yesno":
        ui = ('<button class="btn big-btn" onclick="rnYesNo()">Decide now</button>'
              '<div id="yn-out" class="result huge-res" aria-live="polite"></div>')
    elif kind == "teams":
        ui = ('<label for="ts-in">Names (one per line)</label>'
              '<textarea id="ts-in" rows="7" placeholder="One name per line\u2026"></textarea>'
              '<div class="row"><div><label for="ts-n">Number of teams</label><input type="number" id="ts-n" value="2" min="2" step="1"/></div></div>'
              '<button class="btn" onclick="rnTeams()">Split into teams</button>'
              '<div id="ts-out" class="result" aria-live="polite"></div>')
    elif kind == "lottery":
        ui = ('<div class="row"><div><label for="lt-n">How many numbers</label><input type="number" id="lt-n" value="6" min="1" max="20" step="1"/></div>'
              '<div><label for="lt-max">From 1 to</label><input type="number" id="lt-max" value="59" min="2" step="1"/></div></div>'
              '<button class="btn" onclick="rnLottery()">Draw numbers</button>'
              '<div id="lt-out" class="result big-res" aria-live="polite"></div>')
    elif kind == "country":
        ui = ('<button class="btn" onclick="rnCountry()">Draw a country</button>'
              '<div id="co-out" class="result big-res" aria-live="polite"></div>')
    else:
        ui = ('<button class="btn" onclick="rnQuote()">Draw a quote</button>'
              '<div id="qt-out" class="result big-res" aria-live="polite"></div>')
    return f'<div class="panel">{ui}</div>'

def date_body(kind):
    if kind == "adddays":
        ui = ('<div class="row"><div><label for="ad-date">Start date</label><input type="text" id="ad-date" class="dt-input" readonly placeholder="Pick a date"/></div>'
              '<div><label for="ad-n">Days to add (negative to subtract)</label><input type="number" id="ad-n" value="30" step="1"/></div></div>'
              '<button class="btn" onclick="dtAddDays()">Calculate</button>'
              '<div id="ad-out" class="result" aria-live="polite"></div>')
    elif kind == "dayofweek":
        ui = ('<div class="row"><div><label for="dw-date">Date</label><input type="text" id="dw-date" class="dt-input" readonly placeholder="Pick a date"/></div></div>'
              '<button class="btn" onclick="dtDow()">Find weekday</button>'
              '<div id="dw-out" class="result" aria-live="polite"></div>')
    elif kind == "weeknumber":
        ui = ('<div class="row"><div><label for="wn-date">Date</label><input type="text" id="wn-date" class="dt-input" readonly placeholder="Pick a date"/></div></div>'
              '<button class="btn" onclick="dtWeekNum()">Get week number</button>'
              '<div id="wn-out" class="result" aria-live="polite"></div>')
    elif kind == "leap":
        ui = ('<div class="row"><div><label for="lp-y">Year</label><input type="number" id="lp-y" value="2024" step="1"/></div></div>'
              '<button class="btn" onclick="dtLeap()">Check leap year</button>'
              '<div id="lp-out" class="result" aria-live="polite"></div>')
    elif kind == "s2hms":
        ui = ('<div class="row"><div><label for="s2-sec">Total seconds</label><input type="number" id="s2-sec" value="14537" step="1"/></div></div>'
              '<button class="btn" onclick="dtS2Hms()">Convert</button>'
              '<div id="s2-out" class="result" aria-live="polite"></div>')
    elif kind == "hms2s":
        ui = ('<div class="row"><div><label for="h2-h">Hours</label><input type="number" id="h2-h" value="1" min="0" step="1"/></div>'
              '<div><label for="h2-m">Minutes</label><input type="number" id="h2-m" value="45" min="0" step="1"/></div>'
              '<div><label for="h2-s">Seconds</label><input type="number" id="h2-s" value="0" min="0" step="1"/></div></div>'
              '<button class="btn" onclick="dtHms2S()">Convert</button>'
              '<div id="h2-out" class="result" aria-live="polite"></div>')
    elif kind == "military":
        ui = ('<div class="row"><div><label for="mt-time">Time (12-hour)</label><input type="text" id="mt-time" class="dt-input" readonly placeholder="09:00"/><input type="hidden" id="mt-tv" value="09:00"/></div></div>'
              '<button class="btn" onclick="dtMilitary()">Convert to 24-hour</button>'
              '<div id="mt-out" class="result" aria-live="polite"></div>'
              '<div class="row"><div><label for="mt24">24-hour value (HH:MM)</label><input type="text" id="mt24" placeholder="21:15" autocomplete="off" oninput="dtMilRev()"/></div></div>'
              '<div id="mt-out2" class="result" aria-live="polite"></div>')
    else:
        ui = ('<div class="row"><div><label for="bd-a">Start date</label><input type="text" id="bd-a" class="dt-input" readonly placeholder="Pick start date"/></div>'
              '<div><label for="bd-b">End date</label><input type="text" id="bd-b" class="dt-input" readonly placeholder="Pick end date"/></div></div>'
              '<button class="btn" onclick="dtBizDays()">Count business days</button>'
              '<div id="bd-out" class="result" aria-live="polite"></div>')
    return f'<div class="panel">{ui}</div>'

MEGA2 = {}
CONTENT2 = {}
CAT_BY_SLUG = {"text": "Text Tools", "color": "Color Tools", "random": "Random Generators", "date": "Date & Time Tools"}

for slug, name, cat, short, about, uses, got, ex_t, ex_b, op, conf, extra, ph in TEXT:
    MEGA2[slug] = {"name": name, "cat": cat, "short": short, "body": tx_body(conf or {"op": op}, extra, ph)}
    CONTENT2[slug] = m2_article((slug, name, cat, short, about, uses, got, ex_t, ex_b))

for slug, name, cat, short, about, uses, got, ex_t, ex_b, kind in COLOR:
    kind = {"color-shades-generator": "shades", "complementary-color": "complementary",
            "color-contrast-checker": "contrast", "random-color-generator": "random",
            "invert-color": "invert", "grayscale-converter": "grayscale"}.get(kind, kind)
    MEGA2[slug] = {"name": name, "cat": cat, "short": short, "body": col_body(kind)}
    CONTENT2[slug] = m2_article((slug, name, cat, short, about, uses, got, ex_t, ex_b))

for slug, name, cat, short, about, uses, got, ex_t, ex_b, kind in RAND:
    MEGA2[slug] = {"name": name, "cat": cat, "short": short, "body": rand_body(kind)}
    CONTENT2[slug] = m2_article((slug, name, cat, short, about, uses, got, ex_t, ex_b))

for slug, name, cat, short, about, uses, got, ex_t, ex_b, kind in DATE2:
    MEGA2[slug] = {"name": name, "cat": cat, "short": short, "body": date_body(kind)}
    CONTENT2[slug] = m2_article((slug, name, cat, short, about, uses, got, ex_t, ex_b))
