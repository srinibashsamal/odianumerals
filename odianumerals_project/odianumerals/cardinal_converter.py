from typing import Union

import internal_utils as util
from constants import DASHAMIK, NUM_DATA, UNITS


def _format_compound_number(
    number: int,
    divisor: int,
    unit_label: str,
    as_roman: bool,
    as_odilish: bool,
) -> str:
    """
    Format large numbers recursively using Indian denominations
    such as thousand, lakh, and crore.

    Args:
        number (int): Full numeric value
        divisor (int): Denomination divisor
        unit_label (str): Unit name in selected script
        as_roman (bool): Romanized Odia flag
        as_odilish (bool): Odilish flag

    Returns:
        str: Formatted Odia number in words
    """
    quotient = number // divisor
    remainder = number % divisor

    prefix = to_odia_words(quotient, as_roman=as_roman, as_odilish=as_odilish)

    if remainder == 0:
        return f"{prefix} {unit_label}"

    suffix = to_odia_words(remainder, as_roman=as_roman, as_odilish=as_odilish)
    return f"{prefix} {unit_label} {suffix}"


def to_odia_words(
    number: Union[str, int, float],
    as_roman: bool = False,
    as_odilish: bool = False,
) -> str:
    """Convert a number to its Odia word representation.

    Supports:
    - Integers
    - Decimals
    - Indian numbering system (thousand, lakh, crore)

    Examples:
        10       -> ଦଶ
        10.5     -> ଦଶ ଦଶମିକ ପାଞ୍ଚ
        125      -> ଏକ ଶହ ପଚିଶ
        5 (as_roman=True) -> pāñca

    Args:
        number (Union[str, int, float]): The number to convert
        as_roman (bool, optional): If True, returns phonetic Romanized Odia (index 1). Defaults to False.
        as_odilish (bool, optional): If True, returns casual English-script Odia (index 2). Defaults to False.

    Returns:
        str: Odia (or Romanized Odia) word representation
    """
    num_str = util._validate_and_format(number)
    index = util._resolve_language_index(as_roman, as_odilish)

    if "." in num_str:
        integer_part, fractional_part = num_str.split(".")
        integer_words = to_odia_words(
            int(integer_part), as_roman=as_roman, as_odilish=as_odilish
        )
        decimal_word = DASHAMIK[index]
        fractional_words = [NUM_DATA[int(digit)][index] for digit in fractional_part]
        return f"{integer_words} {decimal_word} {' '.join(fractional_words)}"

    value = int(num_str)
    if value <= 100:
        return NUM_DATA[value][index]

    for unit in (10_000_000, 100_000, 1_000):
        if value >= unit:
            return _format_compound_number(
                value,
                unit,
                UNITS[unit][index],
                as_roman,
                as_odilish,
            )

    hundreds = value // 100
    remainder = value % 100

    if remainder == 0 and hundreds == 1:
        return NUM_DATA[100][index]

    prefix = to_odia_words(hundreds, as_roman=as_roman, as_odilish=as_odilish)
    suffix = (
        to_odia_words(remainder, as_roman=as_roman, as_odilish=as_odilish)
        if remainder
        else ""
    )

    return f"{prefix} {UNITS[100][index]} {suffix}".strip()


def to_roman_words(number: Union[str, int, float]) -> str:
    """Return Romanized Odia number words."""
    return to_odia_words(number, as_roman=True)


def to_odilish_words(number: Union[str, int, float]) -> str:
    """Return Odilish-style Odia number words."""
    return to_odia_words(number, as_odilish=True)


def to_barnabodha_words(
    number: Union[str, int, float],
    as_roman: bool = False,
    as_odilish: bool = False,
) -> str:
    """Delegate conversion to the classical Barnabodha system."""
    import classical_converter as barnabodha

    return barnabodha.to_odia_barnabodha_words(
        number, as_roman=as_roman, as_odilish=as_odilish
    )
