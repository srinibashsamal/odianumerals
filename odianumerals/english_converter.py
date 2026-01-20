from typing import Union

from . import internal_utils as utils

# from .constants import ENG_NUMBER_WORDS, ENG_ORDINAL_WORDS, LARGE_ENG_NUMBER_WORDS
from .constants import ENG_NUMBER_WORDS, LARGE_ENG_NUMBER_WORDS

_SORTED_LARGE_NUMBER = sorted(LARGE_ENG_NUMBER_WORDS.keys(), reverse=True)


def integer_to_words(num: int) -> str:
    """Converts an integer to English words using the Indian system."""
    if num == 0:
        return ENG_NUMBER_WORDS[0]

    words = []
    remaining_number = num

    for unit_value in _SORTED_LARGE_NUMBER:
        if remaining_number >= unit_value:
            unit_count = remaining_number // unit_value
            remaining_number %= unit_value

            unit_count_words = integer_to_words(unit_count)
            unit_name = LARGE_ENG_NUMBER_WORDS[unit_value]

            words.append(f"{unit_count_words} {unit_name}")

    if remaining_number >= 100:
        hundreds_count = remaining_number // 100
        remaining_number %= 100

        words.append(f"{ENG_NUMBER_WORDS[hundreds_count]} hundred")

    if remaining_number > 0:
        if remaining_number in ENG_NUMBER_WORDS:
            words.append(ENG_NUMBER_WORDS[remaining_number])
        else:
            tens_value = (remaining_number // 10) * 10
            ones_value = remaining_number % 10

            words.append(
                f"{ENG_NUMBER_WORDS[tens_value]}-{ENG_NUMBER_WORDS[ones_value]}"
            )

    return " ".join(words)


def decimal_digits_to_words(decimal_part: str) -> str:
    """
    Converts decimal digits into word form.
    Example: "98" -> "nine eight"
    """
    return " ".join(ENG_NUMBER_WORDS[int(digit)] for digit in decimal_part)


def number_to_words(value: Union[int, float, str]) -> str:
    value_str = utils._validate_and_format(value)

    if "." in value_str:
        integer_part, decimal_part = value_str.split(".")
        integer_words = integer_to_words(int(integer_part))
        decimal_words = decimal_digits_to_words(decimal_part)
        return f"{integer_words} point {decimal_words}"

    return integer_to_words(int(value_str))


# print(number_to_words(23))
# # twenty-three

# print(number_to_words(23.98))
# # twenty-three point nine eight

# print(number_to_words(105))
# # one hundred five

# print(number_to_words(1_25_000))
# # one lakh twenty-five thousand

# print(number_to_words(3.14))
# # three point one four
