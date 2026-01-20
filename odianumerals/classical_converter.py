from typing import Union

import internal_utils as util
from constants import BARNABODHA_UNITS, DASHAMIK, NUM_DATA

_SORTED_BARNABODHA_KEYS = sorted(BARNABODHA_UNITS.keys(), reverse=True)


def to_odia_barnabodha_words(
    number: Union[str, int, float], as_roman: bool = False, as_odilish: bool = False
) -> str:
    """
    Convert a number into its Odia word representation using the
    classical Barnabodha numeral system.

    This function supports:
    - Integers
    - Decimal numbers (Dashamik notation)
    - Classical large denominations (śata → parārddha)

    Examples:
        125       -> ଏକ ଶତ ପଚିଶ
        10_000    -> ଏକ ଅୟୁତ
        5 (as_roman=True) -> pāñca

    Args:
        number (Union[str, int, float]): Number to convert
        as_roman (bool, optional): If True, returns phonetic Romanized Odia words. Defaults to False.
        as_odilish (bool, optional): If True, returns casual English-script Odia words. Defaults to False.

    Returns:
        str: Odia number expressed in words
    """
    num_str = util._validate_and_format(number)
    index = util._resolve_language_index(as_roman, as_odilish)

    if "." in num_str:
        integer_part, fractional_part = num_str.split(".")
        integer_words = to_odia_barnabodha_words(
            int(integer_part),
            as_roman=as_roman,
            as_odilish=as_odilish,
        )
        decimal_label = DASHAMIK[index]
        fractional_words = [NUM_DATA[int(digit)][index] for digit in fractional_part]
        return f"{integer_words} {decimal_label} {' '.join(fractional_words)}"

    value = int(num_str)
    if value <= 100:
        return NUM_DATA[value][index]

    for unit_value in _SORTED_BARNABODHA_KEYS:
        if value >= unit_value:
            quotient = value // unit_value
            remainder = value % unit_value
            unit_label = BARNABODHA_UNITS[unit_value][index]
            prefix = to_odia_barnabodha_words(
                quotient,
                as_roman=as_roman,
                as_odilish=as_odilish,
            )

            if remainder == 0:
                return f"{prefix} {unit_label}"

            suffix = to_odia_barnabodha_words(
                remainder,
                as_roman=as_roman,
                as_odilish=as_odilish,
            )
            return f"{prefix} {unit_label} {suffix}"

    return NUM_DATA[value][index]


def to_roman_words(number: Union[str, int, float]) -> str:
    """
    Return Romanized Odia words using the Barnabodha system.
    """
    return to_odia_barnabodha_words(number, as_roman=True)


def to_odilish_words(number: Union[str, int, float]) -> str:
    """
    Return Odilish (English-script Odia) words using the Barnabodha system.
    """
    return to_odia_barnabodha_words(number, as_odilish=True)
