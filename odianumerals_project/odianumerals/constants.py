"""
constants.py
===========

Odia numbers, names, and traditional counting systems.

This file collects commonly used data related to Odia numerals in one place.
It includes how numbers are written in Odia, how they are pronounced, and how
large numbers are traditionally named using the Barnabodha system.

What you'll find here
---------------------
• Odia digit symbols (୦–୯) and their English equivalents (0-9)
• Cardinal number names (0-100) in:
  - Odia script
  - Standard Romanization
  - Simple Roman (easy-to-type) form
• Common modern units like ଶହ, ହଜାର, ଲକ୍ଷ, କୋଟି
• Traditional large-number names used in Barnabodha
• Approximate English meanings for reference
• Words used for decimals
• Ordinal numbers (first, second, third, etc.)
• Commonly used fractions such as half, quarter, and three-quarters

How this module is meant to be used
-----------------------------------
This is a data-only module. It doesn't perform any calculations by itself.
Other parts of the project (like number-to-word converters, Odia digit
formatters, or transliteration tools) can import and use this data as needed.

Sources
-------
- Odia Barnabodha
  https://www.odiaportal.in/2015/09/Download-Chhabila-Madhu-Barnabodha-Odia-eBook-PDF.html
- Wikipedia (Odia Numerals)
  https://en.wikipedia.org/wiki/Odia_numerals
- Learn Oriya Blog
  https://learnoriya.blogspot.com/2012/03/english-number-system-in-oriya-language.html

Compiled & curated by: Srinibash Samal
"""

# ---------------------------------------------------------------------
# Odia Digit Symbols (0–9)
# ---------------------------------------------------------------------

ODIA_DIGITS = {
    "0": "୦",
    "1": "୧",
    "2": "୨",
    "3": "୩",
    "4": "୪",
    "5": "୫",
    "6": "୬",
    "7": "୭",
    "8": "୮",
    "9": "୯",
}

# Reverse mapping: Odia digit → English digit
ENG_DIGITS = {odia: eng for eng, odia in ODIA_DIGITS.items()}

# ---------------------------------------------------------------------
# Odia Cardinal Numbers (0–100)
# Format:
# number -> (Odia Script, Standard Romanization, Simplified Romanization)
# ---------------------------------------------------------------------
NUM_DATA = {
    0: ("ଶୂନ", "śūna", "suna"),
    # 0: ("ଶୂନ୍ୟ", "śūnya", "sunya"),
    1: ("ଏକ", "eka", "ek"),
    2: ("ଦୁଇ", "dui", "dui"),
    3: ("ତିନି", "tini", "tini"),
    4: ("ଚାରି", "cāri", "chari"),
    5: ("ପାଞ୍ଚ", "pāñca", "pancha"),
    6: ("ଛଅ", "chha'a", "chha"),
    7: ("ସାତ", "sāta", "sata"),
    8: ("ଆଠ", "āṭha", "atha"),
    9: ("ନଅ", "na'a", "naa"),
    10: ("ଦଶ", "daśa", "dasha"),
    11: ("ଏଗାର", "egāra", "egar"),
    12: ("ବାର", "bāra", "bara"),
    13: ("ତେର", "tera", "tera"),
    14: ("ଚଉଦ", "cauda", "chauda"),
    15: ("ପନ୍ଦର", "pandara", "pandara"),
    16: ("ଷୋହଳ", "ṣohaḷa", "sohala"),
    17: ("ସତର", "satara", "satara"),
    18: ("ଅଠର", "aṭhara", "athara"),
    19: ("ଉଣେଇଶି", "uṇeiśi", "unaisha"),
    20: ("କୋଡ଼ିଏ", "koṛie", "kodiye"),
    21: ("ଏକୋଇଶି", "ekōiśi", "ekoishi"),
    22: ("ବାଇଶି", "bāiśi", "baishi"),
    23: ("ତେଇଶି", "teiśi", "teishi"),
    24: ("ଚବିଶି", "cabiśi", "chabishi"),
    25: ("ପଚିଶି", "paciśi", "pachishi"),
    26: ("ଛବିଶି", "chabiśi", "chhabishi"),
    27: ("ସତେଇଶି", "sateiśi", "sataishi"),
    28: ("ଅଠେଇଶି", "aṭheiśi", "athaishi"),
    29: ("ଅଣତିରିଶି", "aṇatiriśi", "anatirishi"),
    30: ("ତିରିଶ", "tiriśa", "tirishi"),
    31: ("ଏକତିରିଶି", "ekatiriśi", "ektirishi"),
    32: ("ବତିଶି", "batiśi", "batishi"),
    33: ("ତେତିଶି", "tetiśi", "tetishi"),
    34: ("ଚଉତିରିଶି", "cautiriśi", "chautirishi"),
    35: ("ପଞ୍ଚତିରିଶି", "pañcatiriśi", "panchatirishi"),
    36: ("ଛତିଶି", "chatiśi", "chhatishi"),
    37: ("ସଇଁତିରିଶି", "saiñtiriśi", "saitirishi"),
    38: ("ଅଠତିରିଶି", "aṭhatiriśi", "athatirishi"),
    39: ("ଅଣଚାଳିଶି", "aṇacāḷiśi", "anachalishi"),
    40: ("ଚାଳିଶ", "cāḷiśa", "chalishi"),
    41: ("ଏକଚାଳିଶି", "ekacāḷiśi", "ekchalishi"),
    42: ("ବୟାଳିଶି", "bayāḷiśi", "bayalishi"),
    43: ("ତେୟାଳିଶି", "teyāḷiśi", "teyalishi"),
    44: ("ଚଉରାଳିଶି", "caurāḷiśi", "chauralishi"),
    45: ("ପଞ୍ଚଚାଳିଶି", "pañcacāḷiśi", "panchachalishi"),
    46: ("ଛୟାଳିଶି", "chayāḷiśi", "chayalishi"),
    47: ("ସତଚାଳିଶି", "satacāḷiśi", "satachalishi"),
    48: ("ଅଠଚାଳିଶି", "aṭhacāḷiśi", "athachalishi"),
    49: ("ଅଣଚାଶ", "aṇacāśa", "anachasha"),
    50: ("ପଚାଶ", "pacāśa", "pachasha"),
    51: ("ଏକାବନ", "ekābana", "ekaban"),
    52: ("ବାଉନ", "bāuna", "bauna"),
    53: ("ତେପନ", "tepana", "tepana"),
    54: ("ଚଉବନ", "caubana", "chaubana"),
    55: ("ପଞ୍ଚାବନ", "pañcābana", "panchabana"),
    56: ("ଛପନ", "chapana", "chhapana"),
    57: ("ସତାବନ", "satābana", "satabana"),
    58: ("ଅଠାବନ", "aṭhābana", "athabana"),
    59: ("ଅଣଷଠି", "aṇaṣaṭhi", "anashathi"),
    60: ("ଷାଠିଏ", "ṣāṭhie", "shathiye"),
    61: ("ଏକଷଠି", "ekaṣaṭhi", "ekashathi"),
    62: ("ବାଷଠି", "bāṣaṭhi", "bashathi"),
    63: ("ତେଷଠି", "teṣaṭhi", "teshathi"),
    64: ("ଚଉଷଠି", "cauṣaṭhi", "chaushathi"),
    65: ("ପଞ୍ଚଷଠି", "pañcaṣaṭhi", "panchashathi"),
    66: ("ଛଅଷଠି", "cha'aṣaṭhi", "chhashathi"),
    67: ("ସତଷଠି", "sataṣaṭhi", "satashathi"),
    68: ("ଅଠଷଠି", "aṭhaṣaṭhi", "athashathi"),
    69: ("ଅଣସ୍ତରି", "aṇastari", "anastari"),
    70: ("ସତୁରି/ସତୁରୀ", "saturi/saturī", "saturi"),
    71: ("ଏକସ୍ତରି", "ekastari", "ekastari"),
    72: ("ବାସ୍ତରି", "bāstari", "bastari"),
    73: ("ତେସ୍ତରି", "testari", "testari"),
    74: ("ଚଉସ୍ତରି", "caustari", "chaustari"),
    75: ("ପଞ୍ଚସ୍ତରି", "pañcastari", "panchastari"),
    76: ("ଛଅସ୍ତରି", "cha'astari", "chhastari"),
    77: ("ସତସ୍ତରି", "satastari", "satastari"),
    78: ("ଅଠସ୍ତରି", "aṭhastari", "athastari"),
    79: ("ଅଣାଅଶୀ", "aṇāaśī", "anaashi"),
    80: ("ଅଶୀ", "aśī", "ashi"),
    81: ("ଏକାଅଶୀ", "ekāaśī", "ekaashi"),
    82: ("ବୟାଅଶୀ", "bayāaśī", "bayaashi"),
    83: ("ତେୟାଅଶୀ", "teyāaśī", "teyaashi"),
    84: ("ଚଉରାଅଶୀ", "caurāaśī", "chauraashi"),
    85: ("ପଞ୍ଚାଅଶୀ", "pañcāaśī", "panchaashi"),
    86: ("ଛୟାଅଶୀ", "chayāaśī", "chhayaashi"),
    87: ("ସତାଅଶୀ", "satāaśī", "sataashi"),
    88: ("ଅଠାଅଶୀ", "aṭhāaśī", "athaashi"),
    89: ("ଅଣାନବେ", "aṇānabe", "ananabe"),
    90: ("ନବେ/ନବ୍ବେ", "nabe/nabbe", "nabe"),
    91: ("ଏକାନବେ", "ekānabe", "ekanabe"),
    92: ("ବୟାନବେ", "bayānabe", "bayanabe"),
    93: ("ତେୟାନବେ", "teyānabe", "teyanabe"),
    94: ("ଚଉରାନବେ", "caurānabe", "chauranabe"),
    95: ("ପଞ୍ଚାନବେ", "pañcānabe", "panchanabe"),
    96: ("ଛୟାନବେ", "chayānabe", "chhayanabe"),
    97: ("ସତାନବେ", "satānabe", "satanabe"),
    98: ("ଅଠାନବେ", "aṭhānabe", "athanabe"),
    99: ("ଅନେଶୋତ", "aneśota", "aneshata"),
    100: ("ଶହେ", "śahe", "shahe"),
}
# ---------------------------------------------------------------------
# Common Large Number Units (Modern Usage)
# ---------------------------------------------------------------------

UNITS = {
    100: ("ଶହ", "śaha", "saha"),
    1_000: ("ହଜାର", "hajāra", "hajara"),
    1_00_000: ("ଲକ୍ଷ", "lakṣa", "lakhya"),
    1_00_00_000: ("କୋଟି", "kōṭi", "koti"),
}

# ---------------------------------------------------------------------
# Traditional Large Numeric Units (Barnabodha System)
# ---------------------------------------------------------------------
# Format:
# numeric_value -> (Odia Script, Standard Romanization, Simplified Romanization)
# ---------------------------------------------------------------------

BARNABODHA_UNITS = {
    100: ("ଶତ", "śata", "shata"),
    1_000: ("ସହସ୍ର", "sahasra", "sahasra"),
    10_000: ("ଅୟୁତ", "ayuta", "ayuta"),
    1_00_000: ("ଲକ୍ଷ", "lakṣa", "lakhya"),
    10_00_000: ("ନିୟୁତ", "niyuta", "niyuta"),
    1_00_00_000: ("କୋଟି", "kōṭi", "koti"),
    10_00_00_000: ("ଅର୍ବୁଦ", "arbuda", "arbuda"),
    1_00_00_00_000: ("ବୃନ୍ଦ", "brunda", "brunda"),
    10_000_000_000: ("ଖର୍ବ", "kharba", "kharba"),
    100_000_000_000: ("ନିଖର୍ବ", "nikharba", "nikharba"),
    1_000_000_000_000: ("ଶଙ୍ଖ", "saṅkha", "shankha"),
    10_000_000_000_000: ("ପଦ୍ମ", "padma", "padma"),
    100_000_000_000_000: ("ସାଗର", "sāgara", "sagara"),
    1_000_000_000_000_000: ("ଅନ୍ତ୍ୟ", "antya", "antya"),
    10_000_000_000_000_000: ("ମଧ୍ୟ", "madhya", "madhya"),
    100_000_000_000_000_000: ("ପରାର୍ଦ୍ଧ", "parārddha", "pararddha"),
}

# ---------------------------------------------------------------------
# Approximate English Equivalents
# ---------------------------------------------------------------------


ENG_NUMBER_WORDS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    21: "twenty-one",
    22: "twenty-two",
    23: "twenty-three",
    24: "twenty-four",
    25: "twenty-five",
    26: "twenty-six",
    27: "twenty-seven",
    28: "twenty-eight",
    29: "twenty-nine",
    30: "thirty",
    31: "thirty-one",
    32: "thirty-two",
    33: "thirty-three",
    34: "thirty-four",
    35: "thirty-five",
    36: "thirty-six",
    37: "thirty-seven",
    38: "thirty-eight",
    39: "thirty-nine",
    40: "forty",
    41: "forty-one",
    42: "forty-two",
    43: "forty-three",
    44: "forty-four",
    45: "forty-five",
    46: "forty-six",
    47: "forty-seven",
    48: "forty-eight",
    49: "forty-nine",
    50: "fifty",
    51: "fifty-one",
    52: "fifty-two",
    53: "fifty-three",
    54: "fifty-four",
    55: "fifty-five",
    56: "fifty-six",
    57: "fifty-seven",
    58: "fifty-eight",
    59: "fifty-nine",
    60: "sixty",
    61: "sixty-one",
    62: "sixty-two",
    63: "sixty-three",
    64: "sixty-four",
    65: "sixty-five",
    66: "sixty-six",
    67: "sixty-seven",
    68: "sixty-eight",
    69: "sixty-nine",
    70: "seventy",
    71: "seventy-one",
    72: "seventy-two",
    73: "seventy-three",
    74: "seventy-four",
    75: "seventy-five",
    76: "seventy-six",
    77: "seventy-seven",
    78: "seventy-eight",
    79: "seventy-nine",
    80: "eighty",
    81: "eighty-one",
    82: "eighty-two",
    83: "eighty-three",
    84: "eighty-four",
    85: "eighty-five",
    86: "eighty-six",
    87: "eighty-seven",
    88: "eighty-eight",
    89: "eighty-nine",
    90: "ninety",
    91: "ninety-one",
    92: "ninety-two",
    93: "ninety-three",
    94: "ninety-four",
    95: "ninety-five",
    96: "ninety-six",
    97: "ninety-seven",
    98: "ninety-eight",
    99: "ninety-nine",
    100: "one hundred",
}

LARGE_ENG_NUMBER_WORDS = {
    1_000: "one thousand",
    100_000: "one lakh",
    10_000_000: "one crore",
}

LARGE_NUMBER_WORDS = {
    1_000: "one thousand",
    # 100_000: "one hundred thousand",
    100_000: "one lakh",
    1_000_000: "one million",
    # 10_000_000: "ten million",
    10_000_000: "one crore",
    1_000_000_000: "one billion",
    1_000_000_000_000: "one trillion",
    1_000_000_000_000_000: "one quadrillion",
}
# ---------------------------------------------------------------------
# Decimal Terminology
# ---------------------------------------------------------------------

DASHAMIK = ("ଦଶମିକ", "daśamika", "dashamika")

# ---------------------------------------------------------------------
# Odia Ordinals
# Format:
# number -> (Odia Script, Standard Romanization, Simplified Romanization)
# ---------------------------------------------------------------------
ORDINAL_DATA = {
    1: ("ପ୍ରଥମ", "prathama", "prathama"),
    2: ("ଦ୍ୱିତୀୟ", "dwitīẏa", "dwitiya"),
    3: ("ତୃତୀୟ", "tr̥tīẏa", "trutiya"),
    4: ("ଚତୁର୍ଥ", "caturtha", "chaturtha"),
    5: ("ପଞ୍ଚମ", "pañcama", "panchama"),
    6: ("ଷଷ୍ଠ", "ṣaṣṭha", "shashtha"),
    7: ("ସପ୍ତମ", "saptama", "saptama"),
    8: ("ଅଷ୍ଟମ", "aṣṭama", "ashtama"),
    9: ("ନବମ", "nabama", "nabama"),
    10: ("ଦଶମ", "daśama", "dashama"),
    11: ("ଏକାଦଶ", "ekādaśa", "ekadasha"),
    12: ("ଦ୍ୱାଦଶ", "dwādaśa", "dwadasha"),
    13: ("ତ୍ରୟୋଦଶ", "traẏodaśa", "trayodasha"),
    14: ("ଚତୁର୍ଦ୍ଦଶ", "caturddaśa", "chaturddasha"),
    15: ("ପଞ୍ଚଦଶ", "pañcadaśa", "panchadasha"),
    16: ("ଷୋଡ଼ଶ", "ṣoṛaśa", "shodasha"),
    17: ("ସପ୍ତଦଶ", "saptadaśa", "saptadasha"),
    18: ("ଅଷ୍ଟାଦଶ", "aṣtādaśa", "ashtadasha"),
    19: ("ଊନବିଂଶ", "ūnabiṁśa", "unabinsha"),
    20: ("ବିଂଶ", "biṁśa", "binsha"),
    30: ("ତ୍ରିଂଶ", "triṁśa", "trinsha"),
    40: ("ଚତ୍ୱାରିଂଶ", "catwāriṁśa", "catwarinsha"),
    50: ("ପଞ୍ଚାଶତ୍ତମ", "pañcāśattam", "panchashattam"),
    60: ("ଷଷ୍ଠିତମ", "ṣaṣṭhitama", "shashthitama"),
    70: ("ସପ୍ତତିତମ", "saptatitama", "saptatitama"),
    80: ("ଅଶୀତିତମ", "aśītitama", "ashititama"),
    90: ("ନବତିତମ", "nabatitama", "nabatitama"),
    100: ("ଶତତମ", "śatatama", "shatatama"),
    1000: ("ସହସ୍ରତମ", "sahasratama", "sahasratama"),
    100000: ("ଲକ୍ଷତମ", "makṣatama", "makshatama"),
    10000000: ("କୋଟିତମ", "koṭitama", "kotitama"),
}


ORDINAL_SUFFIX = ("ତମ", "tama", "tama")

# Suffixes for numeric ordinals (e.g., 1st -> ୧ମ)
ORDINAL_NUMERIC_SUFFIXES = {
    1: "ମ",  # Prathama -> 1-ma
    2: "ୟ",  # Dwitiya  -> 2-ya
    3: "ୟ",  # Trutiya  -> 3-ya
    4: "ର୍ଥ",  # Chaturtha -> 4-rtha
    5: "ମ",  # Panchama -> 5-ma
    6: "ଷ୍ଠ",  # Shashtha -> 6-shtha
    7: "ମ",  # Saptama
    8: "ମ",  # Ashtama
    9: "ମ",  # Nabama
    10: "ମ",  # Dashama
}

# Suffixes for 11th-18th (e.g., 11ଶ)
ORDINAL_NUMERIC_TEENS_SUFFIX = "ଶ"

# General fallback suffix
ORDINAL_NUMERIC_DEFAULT = "ମ"

# English Ordinal Words
ENG_ORDINAL_WORDS = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
    13: "thirteenth",
    14: "fourteenth",
    15: "fifteenth",
    16: "sixteen",
    17: "seventeenth",
    18: "eighteenth",
    19: "nineteenth",
    20: "twentieth",
    30: "thirtieth",
    40: "fortieth",
    50: "fiftieth",
    60: "sixtieth",
    70: "seventieth",
    80: "eightieth",
    90: "ninetieth",
}

FRACTIONS = {
    0.25: ("ଚଉଠ", "cauṭha", "chautha"),  # quarter
    0.5: ("ଅଧା", "adhā", "adha"),  # half
    0.75: ("ତିନିପା", "tinipā", "tinipa"),  # three-quarters
    1.5: ("ଦେଢ଼", "deṛha", "dedha"),  # one and a half
    2.5: ("ଅଢ଼େଇ", "aṛhei", "adhei"),  # two and a half
    "half_past": ("ସାଢ଼େ", "sāṛhe", "sadhe"),  # contextual (time-related)
}


# ---------------------------------------------------------------------
# Mathematical Operations
# ---------------------------------------------------------------------

# Format: (Odia Script, Standard Romanization, Simplified Romanization)
MATH_OPERATORS = {
    "+": ("ମିଶାଣ", "miśāṇa", "mishana"),
    "-": ("ଫେଡ଼ାଣ", "pheṛāṇa", "phedana"),
    "*": ("ଗୁଣନ", "guṇana", "gunana"),
    "x": ("ଗୁଣନ", "guṇana", "gunana"),
    "/": ("ହରଣ", "haraṇa", "harana"),
    "÷": ("ହରଣ", "haraṇa", "harana"),
}

MATH_EQUALS = ("ସମାନ", "samāna", "samana")

# Action-based verbs (e.g., "Five added to five")
MATH_VERBS = {
    "+": ("ମିଶାଇଲେ", "miśāile", "mishaile"),
    "-": ("ଫେଡ଼ିଲେ", "pheṛile", "phedile"),
    "*": ("ଗୁଣିଲେ", "guṇile", "gunile"),
    "x": ("ଗୁଣିଲେ", "guṇile", "gunile"),
    "/": ("ହରିଲେ", "harile", "harile"),
    "÷": ("ହରିଲେ", "harile", "harile"),
}
