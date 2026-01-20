import re
from typing import List, Union

from .digit_formatter import to_english_number, to_odia_digits

ODIA_NUM_PATTERN = r"[୦-୯][୦-୯,.]*[୦-୯]|[୦-୯]"
ENG_NUM_PATTERN = r"[0-9][0-9,.]*[0-9]|[0-9]"


def extract_odia_numbers(
    text: str, as_english: bool = False
) -> List[Union[str, int, float]]:
    """
    Finds all Odia numerals in a block of text (including with commas and decimals).

    Args:
        text  (str): The string to search.
        as_english (bool): If True, converts found Odia numbers into English ints/floats.

    Returns:
        A list of identified numbers.
    """
    matches = re.findall(ODIA_NUM_PATTERN, text)

    if not as_english:
        return matches

    results = []
    for match in matches:
        try:
            results.append(to_english_number(match))
        except (ValueError, TypeError):
            continue
    return results


def _odia_to_eng_callback(match):
    token = match.group()
    try:
        return str(to_english_number(token))
    except (ValueError, TypeError):
        return token


def _eng_to_odia_callback(match):
    token = match.group()
    return to_odia_digits(token)


def replace_numbers(text: str, to_english: bool = False) -> str:
    """
    Swaps numbers in a string between Odia and English scripts.

    Args:
        text: The text containing numbers to be replaced.
        to_english: If True, converts Odia -> English.
                    If False (default), converts English -> Odia.
    """

    if to_english:
        return re.sub(ODIA_NUM_PATTERN, _odia_to_eng_callback, text)
    else:
        return re.sub(ENG_NUM_PATTERN, _eng_to_odia_callback, text)
