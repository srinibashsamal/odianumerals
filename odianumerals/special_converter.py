from typing import Union

import internal_utils as util
from cardinal_converter import to_odia_words
from constants import DASHAMIK, FRACTIONS, NUM_DATA


def to_fraction_words(
    number: Union[str, int, float], as_roman: bool = False, as_odilish: bool = False
) -> str:
    """
    Convert a floating point number into common Odia fractional terms.
    Handles special cases like 1.5 (Deṛha) and 2.5 (Aṛhei).

    Args:
        number (Union[str, int, float]): The number to convert.
    """
    index = util._resolve_language_index(as_roman, as_odilish)
    val = float(util._to_english_numeric(number))

    if val in FRACTIONS:
        return FRACTIONS[val][index]

    if val > 2.5 and val % 1 == 0.5:
        prefix = FRACTIONS["half_past"][index]
        whole_num = int(val)
        whole_word = to_odia_words(whole_num, as_roman=as_roman, as_odilish=as_odilish)
        return f"{prefix} {whole_word}"

    return to_odia_words(val, as_roman=as_roman, as_odilish=as_odilish)


def to_percentage_words(
    number: Union[str, int, float], as_roman: bool = False, as_odilish: bool = False
) -> str:
    """
    Convert a number to a percentage string in Odia.
    Example: 10 -> ଦଶ ପ୍ରତିଶତ (Dasha Pratishata)
        "୧୦" -> ଦଶ ପ୍ରତିଶତ
    """
    num_val = util._to_english_numeric(number)
    index = util._resolve_language_index(as_roman, as_odilish)
    percent_label = ("ପ୍ରତିଶତ", "pratiśata", "percent")[index]

    num_word = to_odia_words(num_val, as_roman=as_roman, as_odilish=as_odilish)
    return f"{num_word} {percent_label}"


def to_reading_sequence(
    number: Union[str, int, float], as_roman: bool = False, as_odilish: bool = False
) -> str:
    """
    Converts a number to a digit-by-digit reading sequence.
    Useful for phone numbers, account numbers, or OTPs.

    Example: 102 -> ଏକ ଶୂନ ଦୁଇ (Eka Suna Dui)
        "୧୦୨" -> ଏକ ଶୂନ ଦୁଇ
    """
    num_val = util._to_english_numeric(number)
    num_str = util._validate_and_format(num_val)
    index = util._resolve_language_index(as_roman, as_odilish)

    words = []
    for char in num_str:
        if char == ".":
            words.append(DASHAMIK[index])
        else:
            words.append(NUM_DATA[int(char)][index])

    return " ".join(words)
