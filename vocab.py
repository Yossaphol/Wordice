import random
vocab = {
    "able": "having the power or skill to do something",
    "accept": "to agree to receive something",
    "admit": "to confess or acknowledge",
    "after": "later in time than something else",
    "again": "one more time",
    "agree": "to have the same opinion",
    "almost": "nearly or very close to",
    "alone": "without anyone else",
    "angry": "feeling strong annoyance or displeasure",
    "apple": "a round fruit with red or green skin",
    "allow": "to permit or let something happen",
    "answer": "a reply or response to a question",
    "area": "a particular region or space",
    "army": "a large organized group of soldiers",
    "away": "at a distance from a place",
    "baby": "a very young child",
    "back": "the part of something that is furthest from the front",
    "ball": "a round object used in games or sports",
    "bank": "a financial institution that holds and manages money",
    "base": "the bottom support of something",
    "bath": "the act of washing oneself in water",
    "bear": "a large, strong mammal with thick fur",
    "beat": "to win against someone in a competition",
    "best": "of the highest quality",
    "bill": "a statement of money owed",
    "bird": "a feathered animal that flies",
    "blue": "a color that resembles the sky",
    "bring": "to carry something to a place",
    "build": "to construct or put together something",
    "busy": "occupied with tasks or activities",
    "bloomy": "dark or gloomy",
    "breach": "an act of breaking a rule or agreement",
    "briefs": "a type of close-fitting underwear",
    "brisk": "quick and energetic",
    "broker": "a person who arranges transactions between buyers and sellers",
    "candid": "truthful and straightforward",
    "censor": "to suppress or remove unacceptable parts",
    "call": "to contact someone by phone",
    "camp": "a place where people stay in tents for a short period",
    "card": "a small, flat piece of material, often used for transactions",
    "care": "the act of looking after someone or something",
    "carry": "to hold something while moving",
    "catch": "to grab and hold something",
    "check": "to examine something carefully",
    "clean": "free from dirt or impurities",
    "close": "near in distance",
    "climb": "to go upward using your hands and feet",
    "cost": "the price or amount of money required for something",
    "crop": "plants grown by farmers for food or profit",
    "dark": "having little or no light",
    "date": "the specific day of a month or year",
    "deal": "to handle or manage something",
    "deep": "extending far down from the top",
    "doctor": "a medical professional",
    "dollars": "the official currency of the United States",
    "draw": "to make a picture using lines",
    "dress": "to put clothes on oneself",
    "drink": "to take in liquid through the mouth",
    "drive": "to operate a vehicle",
    "decide": "to make a choice or judgment",
    "dinner": "the main meal of the day, usually in the evening",
    "distant": "far away in space or time",
    "doctor": "a medical professional",
    "dollars": "the official currency of the United States",
    "dance": "to move rhythmically to music",
    "drive": "to operate a vehicle",
    "drink": "to take in liquid through the mouth",
    "dress": "to put clothes on oneself",
    "dream": "a series of thoughts and images during sleep",
    "dubbed": "named or given a title",
    "eager": "enthusiastic and ready for something",
    "each": "every single one in a group",
    "early": "before the usual or expected time",
    "easy": "not difficult to do",
    "enter": "to go into a place",
    "error": "a mistake",
    "enjoys": "to take pleasure in something",
     "exceed": "to go beyond the limits",
    "exempt": "free from an obligation or duty",
    "expose": "to reveal or uncover",
    "extend": "to lengthen or increase",
    "family": "a group of related people living together",
    "famous": "well known by many people",
    "farm": "a place where crops are grown or animals are raised",
    "fast": "moving quickly",
    "fear": "a feeling of being afraid",
    "feel": "to experience an emotion or sensation",
    "file": "a collection of data or documents",
    "fill": "to make something full",
    "find": "to discover something",
    "fine": "good or satisfactory",
    "fire": "the heat and light produced by burning",
    "fish": "an animal that lives in water and has gills",
    "flat": "smooth and level without raised areas",
    "food": "something that people or animals eat",
    "foot": "the part of the leg below the ankle",
    "form": "a printed or written document",
    "free": "not costing any money",
    "from": "indicating the point in space or time at which something starts",
    "full": "containing as much as possible",
    "game": "an activity that people play for enjoyment",
    "gift": "something given to someone without payment",
    "girl": "a young female person",
    "give": "to present something to someone",
    "goal": "an aim or desired result",
    "gold": "a yellow precious metal",
    "good": "morally right or satisfactory",
    "gray": "a color between black and white",
    "great": "of high quality or very important",
    "green": "the color of grass",
    "greet": "to say hello or welcome someone",
    "grow": "to increase in size or develop",
    "half": "one of two equal parts",
    "hand": "the part of the body at the end of the arm",
    "happy": "feeling pleasure or contentment",
    "hard": "difficult to do or accomplish",
    "hate": "to feel strong dislike",
    "have": "to possess something",
    "hear": "to perceive sound with the ears",
    "heat": "the quality of being hot",
    "help": "to assist someone",
    "here": "in this place",
    "high": "at a great height",
    "hold": "to grasp or carry something",
    "home": "the place where someone lives",
    "hope": "to desire something to happen",
    "hot": "having a high temperature",
    "huge": "extremely large",
    "hasten": "to move or act quickly",
    "herald": "to announce or signal",
    "honest": "truthful and sincere",
    "illume": "to light up or brighten",
    "impact": "the effect or influence of one thing on another",
    "impart": "to pass on information or knowledge",
    "impose": "to force something on someone",
    "incite": "to encourage or stir up",
    "idea": "a thought or suggestion",
    "image": "a visual representation of something",
    "join": "to connect or unite with others",
    "job": "a paid position of employment",
    "joy": "a feeling of great happiness",
    "jump": "to push oneself into the air",
    "just": "exactly or only",
    "keep": "to hold or retain something",
    "kill": "to cause the death of something",
    "kind": "being good or helpful to others",
    "king": "a male ruler of a kingdom",
    "know": "to be aware of or familiar with something",
    "lake": "a large body of water surrounded by land",
    "land": "the solid part of the Earth’s surface",
    "last": "final in a series",
    "late": "arriving or happening after the expected time",
    "lead": "to guide or direct a group",
    "left": "the side opposite to the right",
    "less": "a smaller amount of something",
    "life": "the existence of a living being",
    "like": "to have a preference or fondness for something",
    "line": "a long, narrow mark or position",
    "list": "a series of names, items, or tasks",
    "live": "to be alive or exist",
    "load": "to put something onto or into a vehicle or container",
    "long": "measuring a great distance from end to end",
    "look": "to direct one's gaze towards something",
    "lose": "to be defeated or fail to keep something",
    "love": "a deep feeling of affection or attachment",
    "luck": "success or fortune, often by chance",
    "light": "the natural agent that makes things visible",
    "lunch": "a meal eaten in the middle of the day",
    "learn": "to acquire knowledge or skill through study or experience",
    "limit": "a restriction or boundary",
    "large": "of great size, extent, or capacity",
    "lucky": "having good fortune",
    "letter": "a written message or character in the alphabet",
    "main": "most important or principal",
    "make": "to create or produce something",
    "many": "a large number of something",
    "mark": "a visible sign or symbol",
    "meet": "to come together or encounter someone",
    "mind": "the part of a person responsible for thought and feelings",
    "miss": "to fail to hit, reach, or attend something",
    "more": "a greater amount or degree of something",
    "move": "to change position or location",
    "much": "a large amount or extent of something",
    "must": "to be required or necessary",
    "money": "a medium of exchange, typically in coins or notes",
    "march": "to walk in a rhythmic manner, often in unison",
    "month": "a period of roughly 30 days in a calendar",
    "match": "a contest or game between competitors",
    "mouse": "a small rodent or a device used to control a computer",
    "minor": "lesser in importance or size",
    "music": "vocal or instrumental sounds arranged harmoniously",
    "market": "a place where goods or services are bought and sold",
    "master": "an expert or skilled individual",
    "middle": "the center or midpoint of something",
    "moment": "a brief period of time",
    "mother": "a female parent",
    "magnet": "a material that attracts iron or steel",
    "malice": "the intention to harm others",
    "mingle": "to mix or interact with others",
    "museum": "a building where historical, cultural, or artistic items are displayed",
    "mystic": "involving mystery or supernatural phenomena",
    "name": "a word by which a person or thing is known",
    "near": "close to something in distance",
    "need": "to require something because it is essential",
    "next": "immediately following in sequence",
    "nice": "pleasant or agreeable",
    "note": "a brief written message or annotation",
    "nature": "the physical world and its features",
    "noise": "a loud or disruptive sound",
    "never": "not ever, at no time",
    "north": "the direction opposite to the south",
    "once": "at one time in the past",
    "only": "no more than, exclusively",
    "open": "to move something so that it is no longer closed",
    "order": "a command or request to do something",
    "other": "different from the one already mentioned",
    "ocean": "a large body of salt water covering much of the Earth's surface",
    "offer": "to present something for acceptance or consideration",
    "owner": "a person who possesses or controls something",
    "office": "a room or building where business or professional activities take place",
    "online": "connected to or available through the internet",
    "option": "a choice or alternative",
    "page": "a single sheet in a book, magazine, or website",
    "pair": "a set of two matching items",
    "part": "a piece or segment of something larger",
    "party": "a social gathering or celebration",
    "pass": "to move or go past something",
    "peace": "a state of tranquility or absence of conflict",
    "plan": "a detailed proposal for doing or achieving something",
    "play": "to engage in an activity for enjoyment",
    "point": "a specific location or moment in time",
    "post": "a system for sending letters or the position of a person",
    "price": "the amount of money required for a product or service",
    "prove": "to demonstrate the truth of something",
    "paint": "to apply color to a surface using a brush",
    "plant": "a living organism that grows from the ground",
    "plane": "a powered flying vehicle with wings",
    "quick": "happening with great speed",
    "quiet": "making little or no noise",
    "queen": "a female ruler of a kingdom",
    "rain": "water falling from the sky as droplets",
    "read": "to look at and comprehend written text",
    "real": "existing as a fact, not imaginary",
    "rest": "to relax or stop working",
    "ride": "to sit and travel on something, like a bicycle or horse",
    "ring": "a circular band, often made of metal, worn as jewelry",
    "road": "a path for vehicles or pedestrians to travel on",
    "room": "an enclosed space in a building",
    "ready": "fully prepared for something",
    "right": "correct or the opposite of left",
    "river": "a large natural stream of water flowing towards a sea or lake",
    "relax": "to become less tense or anxious",
    "reach": "to stretch out and touch or grasp something",
    "remain": "to stay in the same place or condition",
    "remote": "far away in distance or time",
    "people": "human beings in general or a group of individuals",
    "policy": "a set of rules or guidelines",
    "patron": "a supporter or sponsor",
    "plight": "a difficult or dangerous situation",
    "primal": "basic or fundamental",
    "pursue": "to follow or chase after",
    "query": "a question or inquiry",
    "safe": "free from harm or danger",
    "same": "identical or not different",
    "save": "to preserve or keep something for future use",
    "seat": "a place where a person can sit",
    "sell": "to exchange goods or services for money",
    "send": "to cause something to go from one place to another",
    "shop": "a place where goods are sold",
    "show": "to display or present something",
    "sign": "a symbol or gesture representing something",
    "sing": "to make musical sounds with the voice",
    "small": "little in size or amount",
    "smile": "to curve the lips upwards in expression of happiness",
    "speak": "to talk or communicate with words",
    "spend": "to use money or time on something",
    "stand": "to be in an upright position on the feet",
    "star": "a luminous celestial body",
    "stay": "to remain in a place",
    "stop": "to bring an action or movement to an end",
    "share": "to divide and distribute among others",
    "shirt": "a garment worn on the upper body",
    "study": "the act of learning or acquiring knowledge",
    "sugar": "a sweet substance used in food and drinks",
    "school": "an institution where education is provided",
    "simple": "easily understood or done",
    "sister": "a female sibling",
    "social": "relating to society or interactions with people",
    "spring": "the season following winter",
    "studio": "a room where artistic work is done",
    "sudden": "happening quickly and unexpectedly",
    "sweets": "candy or sugary food",
    "take": "to acquire possession of something",
    "team": "a group working together towards a goal",
    "tell": "to communicate information to someone",
    "test": "an assessment or trial of performance",
    "than": "used to compare two things",
    "that": "used to refer to a specific thing",
    "then": "at that time or next",
    "they": "refers to two or more people",
    "this": "used to indicate a specific thing close by",
    "time": "a measure of ongoing events",
    "told": "communicated information in the past",
    "town": "a small city or large village",
    "true": "in accordance with fact or reality",
    "turn": "to rotate or move in a different direction",
    "type": "a kind or category of things",
    "table": "a piece of furniture with a flat surface and legs",
    "train": "a vehicle that runs on rails",
    "trust": "confidence in someone or something",
    "teach": "to instruct or educate",
    "thank": "to express gratitude",
    "tiger": "a large wild cat with stripes",
    "topic": "a subject of discussion",
    "taught": "instructed or educated in the past",
    "tiger": "plural of tiger",
    "travel": "to journey from one place to another",
    "unit": "a single thing or group",
    "under": "below or beneath something",
    "usual": "normal or common",
    "uncle": "the brother of one’s parent",
    "urban": "relating to a city or town",
    "very": "to a high degree",
    "view": "the ability to see something",
    "vote": "to cast a choice in an election",
    "visit": "to go to see someone or somewhere",
    "voice": "the sound produced in a person's throat",
    "valid": "having legal force or correctness",
    "value": "the worth or importance of something",
    "wait": "to stay in one place until something happens",
    "walk": "to move on foot",
    "wall": "a vertical structure that encloses or divides",
    "want": "to desire something",
    "warm": "having a comfortably high temperature",
    "wash": "to clean with water",
    "wave": "a moving ridge on the surface of water",
    "wear": "to have clothing on",
    "weep": "to shed tears",
    "well": "in a good or satisfactory way",
    "whip": "a long cord used for striking",
    "wide": "having great extent from side to side",
    "wild": "living or growing in the natural environment",
    "will": "expressing future intention",
    "wind": "moving air",
    "wine": "an alcoholic drink made from grapes",
    "wipe": "to clean by rubbing",
    "wire": "a thin, flexible strand of metal",
    "wise": "having experience, knowledge, and good judgment",
    "wish": "to hope for something to happen",
    "wolf": "a wild carnivorous mammal",
    "wood": "the material from trees used in construction",
    "word": "a single unit of language",
    "work": "to engage in tasks or labor",
    "wrap": "to cover something by folding material around it",
    "yard": "an outdoor area near a building",
    "yawn": "to open the mouth wide from tiredness",
    "year": "a period of 12 months",
    "yoga": "a practice of physical, mental, and spiritual disciplines",
    "your": "belonging to you",
    "zero": "the number that represents no quantity",
    "zone": "an area or region defined by boundaries",
    "zoom": "to move quickly with a loud noise",
    "ache": "a dull or persistent pain",
    "aide": "a person who helps or assists",
    "ally": "a friend or partner, especially in times of conflict",
    "arch": "a curved structure",
    "aura": "an invisible quality or atmosphere surrounding something",
    "adopt": "to legally take responsibility for a child or to accept an idea",
    "alert": "a warning or call to attention",
    "anger": "a strong feeling of displeasure",
    "aside": "to one side",
    "asset": "a valuable possession or resource",
    "absorb": "to take in or soak up",
    "abrupt": "sudden or unexpected",
    "admire": "to respect or appreciate",
    "answer": "a reply to a question",
    "appeal": "a request or attraction",
    "advise": "to give recommendations or suggestions",
    "afford": "to be able to pay for something",
    "amount": "a quantity or sum",
    "anchor": "a heavy object used to keep a ship in place",
    "arrive": "to reach a destination",
    "assign": "to give someone a task or responsibility",
    "assure": "to make someone feel certain",
    "author": "a writer of a book or document",
    "beast": "a large, dangerous animal",
    "blend": "to mix things together",
    "blink": "to quickly close and open the eyes",
    "boast": "to talk with excessive pride",
    "brace": "to prepare for something or to support",
    "bark": "the sound made by a dog",
    "bash": "to hit something forcefully",
    "bead": "a small decorative object with a hole for stringing",
    "beam": "a long, sturdy piece of wood or metal",
    "bend": "to curve or change shape",
    "bias": "a tendency to favor one side unfairly",
    "blew": "moved by air (past tense of blow)",
    "boil": "to heat a liquid until it bubbles",
    "bond": "a connection or relationship between things",
    "brag": "to boast or talk with pride",
    "brew": "to make tea, coffee, or beer by mixing ingredients",
    "brow": "the area above the eyes, the forehead",
    "bulk": "a large quantity or mass",
    "bunk": "a type of bed, often stacked in layers",
    "banish": "to force someone to leave a place",
    "barrel": "a large, cylindrical container",
    "betray": "to be disloyal or treacherous",
    "bitter": "having a sharp, unpleasant taste",
    "blight": "to ruin or destroy",
    "bounce": "to move up and down after hitting a surface",
    "breeze": "a light and gentle wind",
    "burden": "a heavy load, either physical or emotional",
    "chaos": "complete disorder and confusion",
    "clash": "to fight or conflict",
    "clerk": "a person employed in an office or store",
    "crave": "to desire something intensely",
    "creep": "to move slowly and carefully",
    "curse": "to invoke harm or ill will",
    "clad": "dressed in or covered",
    "clap": "to strike hands together, usually in applause",
    "clue": "a hint or piece of evidence",
    "coal": "a black mineral used for fuel",
    "coax": "to gently persuade someone",
    "cozy": "warm and comfortable",
    "cram": "to stuff or pack tightly",
    "crew": "a group of people working together, especially on a ship or plane",
    "crux": "the most important point",
    "cult": "a system of religious worship or devotion",
    "curb": "the edge of a sidewalk or road",
    "cancel": "to stop or call off an event",
    "casual": "informal or relaxed",
    "choice": "an option or decision",
    "climax": "the most intense point in a story or event",
    "collar": "the part of a shirt around the neck",
    "comply": "to follow rules or orders",
    "convey": "to communicate or express",
    "crisis": "a time of intense difficulty or danger",
    "dealt": "handled or managed (past tense of deal)",
    "delay": "to postpone or put off",
    "dense": "closely packed or thick",
    "devil": "an evil or malevolent spirit",
    "drown": "to die by being unable to breathe underwater",
    "damp": "slightly wet or moist",
    "dart": "to move quickly or suddenly",
    "dash": "to run or move quickly",
    "dawn": "the beginning of the day or first light",
    "deft": "quick and skillful",
    "dusk": "the time just before nightfall",
    "debate": "a formal discussion or argument",
    "defend": "to protect from harm",
    "define": "to explain the meaning of a word or concept",
    "demand": "a strong request or need",
    "depart": "to leave or set off on a journey",
    "depend": "to rely on or trust",
    "detach": "to separate or remove",
    "devote": "to give time or effort to something",
    "divide": "to separate into parts",
    "drench": "to wet something completely",
    "eager": "very enthusiastic or excited",
    "elite": "the most powerful or influential group",
    "evoke": "to bring a feeling or memory to mind",
    "envy": "a feeling of jealousy",
    "exile": "to banish or send away from one's home",
    "effort": "an attempt or hard work",
    "emerge": "to come into view or become visible",
    "engage": "to involve or participate",
    "enrage": "to make extremely angry",
    "ensure": "to make certain",
    "entail": "to involve or require",
    "entice": "to attract or tempt",
    "expand": "to increase in size or scope",
    "export": "to send goods or services to another country",
    "extend": "to stretch out or make longer",
    "fend": "to defend or look after oneself",
    "feud": "a prolonged conflict or dispute",
    "flaw": "a defect or imperfection",
    "flee": "to run away from danger",
    "flip": "to turn over quickly",
    "foil": "to prevent or hinder",
    "flame": "a hot, glowing body of burning gas",
    "flock": "a group of animals, especially birds",
    "flute": "a woodwind musical instrument",
    "fraud": "deception intended to result in financial gain",
    "frown": "to furrow one's brow in disapproval",
    "famine": "a severe shortage of food",
    "fierce": "very intense or aggressive",
    "forbid": "to prohibit or refuse to allow",
    "frozen": "turned into ice or very cold",
    "gloom": "partial or total darkness",
    "gorge": "a narrow valley between hills or mountains",
    "grasp": "to seize or hold firmly",
    "greed": "an intense desire for more than is needed",
    "gaze": "to look steadily at something",
    "germ": "a microorganism that can cause disease",
    "glee": "joy or delight",
    "glow": "to emit light or warmth",
    "gnaw": "to bite or chew persistently",
    "grip": "to hold firmly",
    "grit": "small loose particles of stone or sand",
    "gather": "to collect or assemble",
    "gentle": "kind and mild in behavior",
    "gravel": "small stones, often used for roads",
    "haste": "excessive speed or urgency",
    "haunt": "to visit or appear frequently as a ghost",
    "heave": "to lift or throw something heavy",
    "hinge": "a jointed device that allows a door or lid to swing open",
    "hoard": "to collect and store a large supply",
    "horde": "a large group of people or things",
    "hover": "to stay in the air without moving",
    "haul": "to pull or drag with effort",
    "haze": "a light mist or smoke in the air",
    "heed": "to pay attention to or take notice of",
    "herb": "a plant used for flavoring or medicine",
    "hurl": "to throw with great force",
    "hazard": "a danger or risk",
    "hinder": "to delay or obstruct",
    "honest": "truthful and sincere",
    "ignore": "to refuse to notice or acknowledge",
    "impact": "the effect or influence of something",
    "import": "to bring goods or services into a country",
    "injury": "physical damage to the body",
    "insist": "to demand or assert strongly",
    "invest": "to put money into something to gain profit",
    "invite": "to ask someone to attend an event or to do something",
    "itch": "an uncomfortable sensation on the skin that makes you want to scratch",
    "jolt": "a sudden, violent movement or shock",
    "junior": "a person who is younger or of lower rank",
    "leapt": "jumped or sprang suddenly (past tense of leap)",
    "legend": "a traditional story, often regarded as historical but not verified",
    "linger": "to stay in a place longer than necessary",
    "locate": "to find the position or place of something",
    "keel": "the main structure of a ship running lengthwise along the bottom",
    "kern": "the essential part or core of something",
    "knack": "a special skill or ability",
    "lair": "a secret or private place for hiding or resting, usually for an animal",
    "lash": "to strike with a whip or stick",
    "leap": "to jump or spring a long way",
    "limb": "an arm or leg of a person or animal",
    "loom": "to appear in a large or threatening form",
    "lurk": "to stay hidden or in secret, usually with a sinister purpose",
    "lodge": "a small house or shelter, especially in the woods or for temporary use",
    "lunar": "relating to the moon",
    "marsh": "a wetland area, often with grasses or plants",
    "mimic": "to imitate or copy someone’s actions or speech",
    "mirth": "happiness or enjoyment, often shown through laughter",
    "moist": "slightly wet or damp",
    "mourn": "to express sorrow or grief, especially after someone’s death",
    "mock": "to make fun of or ridicule someone",
    "muse": "to think deeply or meditate on something",
    "mature": "fully developed, either physically or emotionally",
    "meddle": "to interfere in someone else’s business",
    "misery": "great suffering or distress",
    "modern": "relating to present times or recent developments",
    "mutual": "shared by two or more parties",
    "nest": "a structure made by birds or other animals to lay eggs or raise young",
    "numb": "lacking feeling or sensation, often due to cold or shock",
    "nerve": "a bundle of fibers that transmits signals in the body",
    "niche": "a specialized or suitable place or position",
    "noble": "having high moral qualities or status, often relating to aristocracy",
    "obese": "extremely overweight or fat",
    "ogle": "to stare at someone with strong or inappropriate interest",
    "omit": "to leave out or exclude",
    "ooze": "to slowly leak or flow out, often a thick liquid",
    "occupy": "to take control of or live in a space",
    "oppose": "to stand against or resist",
    "perk": "an additional benefit or advantage",
    "plow": "to turn over soil with a tool in preparation for planting",
    "ploy": "a clever plan or strategy, often deceptive",
    "pout": "to push one’s lips out, often in annoyance or disappointment",
    "prod": "to push or poke someone to encourage them to act",
    "prop": "to support or hold something up",
    "plead": "to beg or ask earnestly",
    "plume": "a large feather or group of feathers",
    "parent": "a father or mother",
    "people": "human beings as a group",
    "policy": "a course or principle of action adopted by an organization or individual",
    "plump": "slightly fat in a healthy way",
    "prone": "likely to do something or be affected by something",
    "permit": "to allow or authorize",
    "pursue": "to follow or chase after",
    "quell": "to suppress or put an end to something",
    "query": "a question or request for information",
    "quota": "a limited or fixed amount of something",
    "quip": "a witty or clever remark",
    "rage": "intense, uncontrolled anger",
    "reek": "to emit a strong, unpleasant smell",
    "reel": "to spin or stagger as if dizzy",
    "rend": "to tear something apart violently",
    "riot": "a violent disturbance by a crowd",
    "rust": "the reddish coating formed on metal when it corrodes",
    "rebel": "a person who resists authority or control",
    "reign": "to rule as a king or queen",
    "relay": "to pass on information or signals",
    "renew": "to make something new or to extend the duration of something",
    "revel": "to enjoy oneself in a lively and noisy way",
    "random": "made or done without method or conscious decision",
    "reckon": "to estimate or calculate",
    "reduce": "to make smaller or less",
    "reject": "to refuse to accept",
    "reveal": "to make something known or visible",
    "rescue": "to save someone from danger",
    "retail": "the sale of goods to the public in relatively small quantities",
    "retain": "to keep or hold on to something",
    "retire": "to stop working after reaching a certain age",
    "sage": "a wise person",
    "scar": "a mark left on the skin after a wound heals",
    "scum": "a layer of dirt or impurities on the surface of a liquid",
    "shed": "to discard or release",
    "shun": "to avoid or reject",
    "slay": "to kill violently",
    "slog": "to work hard or trudge through something difficult",
    "snub": "to insult or ignore someone intentionally",
    "soar": "to fly or rise high in the air",
    "spur": "to encourage or prompt",
    "stow": "to store or pack something away",
    "scorn": "to feel or express contempt or disdain",
    "scree": "a slope covered with loose stones or debris",
    "shear": "to cut or clip something",
    "shrub": "a small bush or plant",
    "siege": "a military blockade of a city or fortress",
    "sleek": "smooth, shiny, and elegant",
    "slink": "to move quietly or stealthily",
    "slope": "a surface that is inclined or slanted",
    "spare": "to have extra or in reserve",
    "spite": "a desire to harm or annoy someone",
    "squad": "a small group of people working together",
    "stark": "severe or extreme",
    "sting": "to pierce or wound with a sharp object",
    "swarm": "a large group of insects or other creatures",
    "scheme": "a plan or arrangement, often secretive or dishonest",
    "scrape": "to remove or clean by rubbing with a sharp edge",
    "seldom": "rarely or not often",
    "silent": "quiet or without sound",
    "spread": "to extend over a large area",
    "strain": "a state of tension or pressure",
    "summon": "to call or order someone to come",
    "surfer": "a person who rides ocean waves on a surfboard",
    "taint": "to contaminate or spoil",
    "throb": "to pulsate with a steady rhythm",
    "thrum": "to make a continuous low humming sound",
    "truce": "an agreement to stop fighting temporarily",
    "tame": "domesticated or under control",
    "taut": "pulled tight or tense",
    "teem": "to be full of or overflowing with something",
    "tend": "to take care of or look after",
    "torn": "ripped or damaged",
    "tempt": "to entice or attract someone to do something",
    "unfold": "to open or reveal",
    "unseen": "not seen or noticed",
    "veer": "to change direction suddenly",
    "vent": "an opening for air or gas to escape",
    "veto": "the power to reject a decision or proposal",
    "vague": "unclear or uncertain",
    "valor": "great courage in the face of danger",
    "vivid": "bright or intense",
    "vowel": "a speech sound made with the mouth open (e.g., a, e, i, o, u)",
    "weary": "very tired or fatigued",
    "wharf": "a dock or platform for ships to load or unload",
    "whisk": "to stir or beat quickly, especially eggs or cream",
    "wince": "to flinch or grimace in pain or discomfort",
    "wrath": "intense anger",
    "wade": "to walk through water or another substance",
    "wane": "to decrease in size or intensity",
    "warp": "to distort or bend out of shape",
    "weep": "to cry or shed tears",
    "wealth": "an abundance of valuable resources or material possessions",
    "wilt": "to become limp or droop",
    "wander": "to move around without a fixed course",
    "tangle": "a confused or disordered state",
    "temple": "a place of worship",
    "traced": "followed or found the origin of something",
    "upbeat": "optimistic or cheerful",
    "utmost": "the greatest or highest degree",
    "vandal": "a person who deliberately damages property",
    "velvet": "a soft fabric with a smooth, silky texture",
    "weave": "to interlace threads to form fabric",
    "wholly": "completely or entirely",
    "witty": "clever and amusing"
}

def vocab_random():
    length = len(vocab)
    ind = random.randint(1,length-1)
    en_word = list(vocab.keys())[ind]
    description = list(vocab.values())[ind]
    return en_word, description
