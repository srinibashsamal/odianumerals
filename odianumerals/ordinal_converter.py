import re
from typing import Union

from . import cardinal_converter as cardinal
from . import digit_formatter
from . import english_converter as english
from . import internal_utils as util
from .constants import (
    ENG_NUMBER_WORDS,
    ENG_ORDINAL_WORDS,
    ORDINAL_DATA,
    ORDINAL_NUMERIC_DEFAULT,
    ORDINAL_NUMERIC_SUFFIXES,
    ORDINAL_NUMERIC_TEENS_SUFFIX,
    ORDINAL_SUFFIX,
)


def to_odia_ordinal_numeral(number: Union[str, int, float]) -> str:
    """
    Converts a number (or English ordinal string) into an Odia numeric ordinal.
    Examples:
        1      -> ୧ମ
        "2nd"  -> ୨ୟ
        "4th"  -> ୪ର୍ଥ
        11     -> ୧୧ଶ
    """
    if isinstance(number, str):
        number = re.sub(r"(st|nd|rd|th)$", "", number, flags=re.IGNORECASE)

    try:
        val = int(util._to_english_numeric(number))
    except (ValueError, TypeError):
        raise ValueError(f"Invalid input for Odia ordinal numeral: {number}")

    if 11 <= val <= 18:
        suffix = ORDINAL_NUMERIC_TEENS_SUFFIX
    else:
        last_digit = val % 10
        suffix = ORDINAL_NUMERIC_SUFFIXES.get(
            val, ORDINAL_NUMERIC_SUFFIXES.get(last_digit, ORDINAL_NUMERIC_DEFAULT)
        )

    odia_number = digit_formatter.to_odia_digits(val)
    return f"{odia_number}{suffix}"


def to_english_ordinal_numeral(odia_ordinal: str) -> str:
    """Converts Odia numeric ordinal back to English.
    Examples:
        "୧ମ"   -> "1st"
        "୨ୟ"   -> "2nd"
        "୪ର୍ଥ"  -> "4th"
        "୧୧ଶ"  -> "11th"
    """
    if not isinstance(odia_ordinal, str):
        raise ValueError("Input must be an Odia ordinal string (e.g., '୧ମ')")

    match = re.match(r"^([୦-୯,.]+)\s*([ମୟର୍ଥଷ୍ଠଶ]*)$", odia_ordinal.strip())

    if not match:
        raise ValueError(f"Could not parse Odia ordinal: {odia_ordinal}")

    odia_digits_part = match.group(1)

    try:
        val = int(digit_formatter.to_english_number(odia_digits_part))
    except (ValueError, TypeError):
        raise ValueError(f"Invalid Odia digits in ordinal: {odia_digits_part}")

    if 11 <= (val % 100) <= 13:
        suffix = "th"
    else:
        last_digit = val % 10
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(last_digit, "th")

    return f"{val}{suffix}"


def to_ordinal_numeral(value: Union[str, int, float], lang: str) -> str:
    """Wrapper to dispatch numeric ordinal conversion based on language.

    Args:
        value (Union[str, int, float]): he ordinal to convert (e.g., "1st" or "୧ମ").
        lang (str): Target language. 'or'/'od' for Odia, 'en' for English.

    Raises:
        ValueError: If the language code is unsupported or conversion fails.

    Returns:
        str: The converted ordinal string.
    """
    lang = lang.lower().strip()
    if lang in ("or", "od"):
        return to_odia_ordinal_numeral(value)
    elif lang == "en":
        return to_english_ordinal_numeral(str(value))
    else:
        raise ValueError(
            f"\nUnsupported language: {lang!r}."
            f"\n  Supported options: 'or'/'od' for Odia, 'en' for English."
        )


def to_odia_ordinal_words(
    number: Union[str, int, float], as_roman: bool = False, as_odilish: bool = False
) -> str:
    """Convert a number into its Odia ordinal words (e.g., 1 or ୧ -> ପ୍ରଥମ).

    Args:
        number (Union[str, int, float]): The rank/number.
        as_roman (bool): Return Romanized Odia.
        as_odilish (bool): Return Odilish.
    """
    try:
        val = int(util._to_english_numeric(number))
        if val < 0:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError("Odia ordinal words require a positive integer.")

    index = util._resolve_language_index(as_roman, as_odilish)

    if val in ORDINAL_DATA:
        return ORDINAL_DATA[val][index]

    base_cardinal = cardinal.to_odia_words(
        val, as_roman=as_roman, as_odilish=as_odilish
    )
    suffix = ORDINAL_SUFFIX[index]
    return f"{base_cardinal}{suffix}"


def to_english_ordinal_words(number: Union[str, int, float]) -> str:
    """Convert number into its English ordinal words (e.g., 1 or ୧ -> first)."""
    try:
        val = int(util._to_english_numeric(number))
        if val <= 0:
            raise ValueError
    except (ValueError, TypeError):
        raise ValueError("English ordinal words require a positive integer.")

    if val in ENG_ORDINAL_WORDS:
        return ENG_ORDINAL_WORDS[val]

    if val < 100:
        tens = (val // 10) * 10
        ones = val % 10
        return f"{ENG_NUMBER_WORDS[tens]}-{ENG_ORDINAL_WORDS[ones]}"

    if val % 100 == 0:
        cardinal = english.integer_to_words(val)
        if cardinal.endswith("y"):
            return cardinal[:-1] + "ieth"
        return cardinal + "th"
    else:
        remainder = val % 100
        base_val = val - remainder
        base_words = english.integer_to_words(base_val)
        ordinal_suffix_words = to_english_ordinal_words(remainder)

        return f"{base_words} {ordinal_suffix_words}"


def to_ordinal_words(value: Union[str, int, float], to_lang: str, **kwargs) -> str:
    """Wrapper to dispatch numeric ordinal conversion based on language.

    Args:
        value (Union[str, int, float]): he ordinal to convert (e.g., "1st" or "୧ମ").
        to_lang (str): Target language. 'or'/'od' for Odia, 'en' for English.

    Raises:
        ValueError: If the language code is unsupported or conversion fails.

    Returns:
        str: The converted ordinal string.
    """
    lang = to_lang.lower().strip()
    if lang in ("or", "od"):
        return to_odia_ordinal_words(value, **kwargs)
    elif lang == "en":
        return to_english_ordinal_words(str(value))
    else:
        raise ValueError(
            f"\nUnsupported language: {lang!r}."
            f"\n  Supported options: 'or'/'od' for Odia, 'en' for English."
        )
