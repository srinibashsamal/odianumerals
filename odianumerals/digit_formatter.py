from typing import Union

from .constants import ENG_DIGITS, ODIA_DIGITS
from .internal_utils import _validate_and_format


def to_odia_digits(number: Union[str, int, float]) -> str:
    """
    Convert English digits into Odia digit symbols.

    Examples:
        123     -> ୧୨୩
        123.45  -> ୧୨୩.୪୫

    Args:
        number (Union[str, int, float]): Numeric input

    Returns:
        str: Odia digit string
    """
    num_str = _validate_and_format(number)
    return "".join(ODIA_DIGITS.get(ch, ch) for ch in num_str)


def to_english_number(number_str: str) -> Union[int, float]:
    """
    Convert Odia digits back into English numeric values.

    Args:
        number_str (str): Odia digit string

    Returns:
        Union[int, float]: Parsed numeric value in English

    Raises:
        ValueError: If conversion fails
    """
    clean_value = str(number_str).replace(",", "")
    english_value = "".join(ENG_DIGITS.get(ch, ch) for ch in clean_value)

    try:
        return float(english_value) if "." in english_value else int(english_value)
    except ValueError:
        raise ValueError(f"Unable to convert '{number_str}' to a numeric value.")


def format_indian_style(
    number: Union[str, int, float], use_odia_digits: bool = False
) -> str:
    """
    Format numbers using the Indian comma system (Thousands, Lakhs & Crores).

    Example:
        1000000 -> 10,00,000

    Args:
        number (Union[str, int, float]): Input number
        use_odia_digits (bool): Convert output digits to Odia. Defaults to False

    Returns:
        str: Formatted number string
    """
    num_str = _validate_and_format(number)

    if "." in num_str:
        integer_part, fractional_part = num_str.split(".")
    else:
        integer_part, fractional_part = num_str, ""

    if len(integer_part) <= 3:
        formatted = integer_part
    else:
        last_three = integer_part[-3:]
        remaining = integer_part[:-3]
        groups = [remaining[max(i - 2, 0) : i] for i in range(len(remaining), 0, -2)][
            ::-1
        ]
        formatted = ",".join(groups + [last_three])

    result = f"{formatted}.{fractional_part}" if fractional_part else formatted

    if use_odia_digits:
        return "".join(ODIA_DIGITS.get(ch, ch) for ch in result)

    return result
