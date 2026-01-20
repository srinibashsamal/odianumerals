from typing import Any, Union


def _to_english_numeric(val: Any) -> Any:
    """
    Checks if the input is an Odia numeric string and converts it
    to an English int or float. If it's not a numeric string,
    returns the value as-is.
    """
    if isinstance(val, str):
        try:
            import digit_formatter

            return digit_formatter.to_english_number(val)
        except (ValueError, TypeError):
            return val
    return val


def _resolve_language_index(as_roman: bool, as_odilish: bool) -> int:
    """
    Resolve the index for multilingual numeral data.

    Index mapping:
        0 -> Odia script
        1 -> Romanized Odia
        2 -> Odilish (casual English script)

    Args:
        as_roman (bool): Romanized Odia flag
        as_odilish (bool): Odilish flag

    Returns:
        int: Corresponding data index
    """
    if as_odilish:
        return 2
    if as_roman:
        return 1
    return 0


def _validate_and_format(number: Union[str, int, float]) -> str:
    """
    Validate the input and normalize it as a string.

    - Ensures the input is numeric
    - Disallows negative values
    - Preserves decimal formatting

    Args:
        number (Union[str, int, float]): Numeric input

    Returns:
        str: Normalized numeric string representation

    Raises:
        TypeError: If input is not numeric
        ValueError: If the number is negative
    """
    try:
        num_float = float(number)
        if num_float < 0:
            raise ValueError("Negative numbers are not supported.")

        # .10f handles precision up to 10 digits without scientific notation
        num_str = format(num_float, ".10f").rstrip("0").rstrip(".")

        if num_float == int(num_float):
            return str(int(num_float))

        return num_str
    except (TypeError, ValueError):
        raise TypeError(f"Invalid numeric value: {number!r}")
