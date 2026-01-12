import random
from typing import Any, List, Sequence, Union

import cardinal_converter
import digit_formatter
import internal_utils as util


def _apply_odia_formatting(
    value: Union[int, float],
    *,
    as_words: bool = False,
    as_digits: bool = True,
    barnabodha_style: bool = False,
    **kwargs,
) -> Any:
    """
    Format a numeric value into Odia representation.

    Priority order:
    1. Odia words (standard or Barnabodha style)
    2. Odia digits
    3. Raw numeric value

    Args:
        value (int | float): Number to format.
        as_words (bool): Convert to Odia words.
        as_digits (bool): Convert to Odia digits (default).
        barnabodha_style (bool): Use Barnabodha word style.

    Returns:
        Any: Formatted value in Odia or raw number.
    """

    if as_words:
        return (
            cardinal_converter.to_barnabodha_words(value, **kwargs)
            if barnabodha_style
            else cardinal_converter.to_odia_words(value, **kwargs)
        )
    if as_digits:
        return digit_formatter.to_odia_digits(value)
    return value


def get_random_int(start: Any, end: Any, **kwargs) -> Any:
    """Generates a random integer between start and end (inclusive).
    Supports '`as_words=True`'.

    Equivalent: `random.randint()`

    Args:
        start (int): Lower bound of the range (inclusive).
        end (int): Upper bound of the range (inclusive).

    Returns:
        Any: A random integer, optionally formatted as Odia words or digits.
    """
    s = int(util._to_english_numeric(start))
    e = int(util._to_english_numeric(end))
    val = random.randint(s, e)
    return _apply_odia_formatting(val, **kwargs)


def get_random_range(start: Any, stop: Any = None, step: Any = 1, **kwargs) -> Any:
    """Generates a random integer from a specific range/step sequence.

    Equivalent: `random.randrange()`

    Args:
        start (int): Start of the range.
        stop (int, optional): End of the range (exclusive).
        step (int, optional): Step size between values. Defaults to 1.

    Returns:
        Any: A randomly selected value from the range, optionally formatted.
    """
    s = int(util._to_english_numeric(start))
    p = int(util._to_english_numeric(stop)) if stop is not None else None
    t = int(util._to_english_numeric(step))
    val = random.randrange(s, p, t)
    return _apply_odia_formatting(val, **kwargs)


def get_random_decimal(
    min_val: Any = 0.0, max_val: Any = 1.0, precision: Any = 3, **kwargs
) -> Any:
    """
    Generates a random floating-point number with a specific precision.

    Supports '`as_words=True`'.

    Equivalent: `random.random()` (if no args) or `random.uniform()`

    Args:
        min_val (Any, optional): Lower bound. Accepts Odia strings or English numbers.
        max_val (Any, optional): Upper bound. Accepts Odia strings or English numbers.
        precision (Any, optional): Number of digits after the decimal point. Defaults to 3.

    Returns:
        Any: A random float rounded to 'precision', optionally formatted.
    """
    low = float(util._to_english_numeric(min_val))
    high = float(util._to_english_numeric(max_val))
    prec = int(util._to_english_numeric(precision))

    if low == 0.0 and high == 1.0:
        val = random.random()
    else:
        val = random.uniform(low, high)

    val = round(val, prec)

    return _apply_odia_formatting(val, **kwargs)


def get_triangular_decimal(
    low: Any, high: Any, peak: Any = None, precision: Any = 3, **kwargs
) -> Any:
    """Generates a random float within a range, weighted toward a peak/mode.

    Equivalent: `random.triangular()`

    Args:
        low (float): Lower limit of the distribution.
        high (float): Upper limit of the distribution.
        peak (float, optional): Mode (most likely value) of the distribution.
        precision (Any, optional): Number of digits after the decimal point. Defaults to 3.

    Returns:
        Any: A random float following a triangular distribution,
             optionally formatted.
    """

    low_val = float(util._to_english_numeric(low))
    high_val = float(util._to_english_numeric(high))
    peak_val = float(util._to_english_numeric(peak)) if peak is not None else None
    prec = int(util._to_english_numeric(precision))

    val = random.triangular(low_val, high_val, peak_val)
    val = round(val, prec)
    return _apply_odia_formatting(val, **kwargs)


def pick_one(items: Sequence, **kwargs) -> Any:
    """Pick a single random item from a list or sequence.

    Equivalent: `random.choice()`

    Args:
        items (Sequence): A non-empty sequence of items.

    Returns:
        Any: Converts Odia numeric strings found in items
    """
    processed_items = [util._to_english_numeric(i) for i in items]
    choice = random.choice(processed_items)

    if isinstance(choice, (int, float)):
        return _apply_odia_formatting(choice, **kwargs)
    return choice


def pick_multiple(items: Sequence, count: Any = 1, **kwargs) -> List[Any]:
    """Pick multiple items from a list (with possible duplicates).

    Equivalent: `random.choices()`

    Args:
        items (Sequence): A sequence of items to choose from.
        count (int, optional): Number of items to select. Defaults to 1.

    Returns:
        List[Any]: A list of randomly selected items, with numeric values
                   optionally formatted.
    """
    k_val = int(util._to_english_numeric(count))
    processed_items = [util._to_english_numeric(i) for i in items]

    results = random.choices(processed_items, k=k_val)
    return [
        _apply_odia_formatting(v, **kwargs) if isinstance(v, (int, float)) else v
        for v in results
    ]


def pick_unique_sample(items: Sequence, count: Any, **kwargs) -> List[Any]:
    """Pick a unique subset of items from a list (no duplicates).

    Equivalent: `random.sample()`

    Args:
        items (Sequence): A sequence of items to sample from.
        count (int): Number of unique items to select.

    Raises:
        ValueError: If count exceeds the number of available items.

    Returns:
        List[Any]: A list of unique randomly selected items, with numeric values
                   optionally formatted.
    """
    k_val = int(util._to_english_numeric(count))
    processed_items = [util._to_english_numeric(i) for i in items]
    if k_val > len(processed_items):
        raise ValueError("count cannot exceed the number of available items")
    results = random.sample(processed_items, k=k_val)
    return [
        _apply_odia_formatting(v, **kwargs) if isinstance(v, (int, float)) else v
        for v in results
    ]
