import re
from typing import Union

import cardinal_converter as cardinal
import internal_utils as util
from constants import MATH_EQUALS, MATH_OPERATORS, MATH_VERBS


def calculate_and_express(
    val_1: Union[str, int, float],
    operator: str,
    val2: Union[str, int, float],
    as_roman: bool = False,
    as_odilish: bool = False,
    use_verbs: bool = False,
) -> str:
    """
    Performs a math operation and returns the full expression in Odia words.

    Example: (5, "+", 2) -> "ପାଞ୍ଚ ମିଶାଣ ଦୁଇ ସମାନ ସାତ"

    Args:
        val_1, val2: Numbers to operate on.
        operator: One of '+', '-', '*', 'x', '/'.
        as_roman/as_odilish: Formatting flags.
        use_verbs: If True, uses "added to" style instead of "plus" style.
    """
    idx = util._resolve_language_index(as_roman, as_odilish)

    num_1 = util._to_english_numeric(val_1)
    num_2 = util._to_english_numeric(val2)

    if operator == "+":
        result = num_1 + num_2
    elif operator == "-":
        result = num_1 - num_2
    elif operator in ("*", "x"):
        result = num_1 * num_2
    elif operator in ("/", "÷"):
        if num_2 == 0:
            raise ZeroDivisionError("Cannot divide by zero in Odia math logic.")
        result = num_1 / num_2
    else:
        raise ValueError(f"Unsupported operator: {operator}")

    word_1 = cardinal.to_odia_words(num_1, as_roman, as_odilish)
    word_2 = cardinal.to_odia_words(num_2, as_roman, as_odilish)
    res_word = cardinal.to_odia_words(result, as_roman, as_odilish)

    op_word = MATH_VERBS[operator][idx] if use_verbs else MATH_OPERATORS[operator][idx]
    eq_word = MATH_EQUALS[idx]

    return f"{word_1} {op_word} {word_2} {eq_word} {res_word}"


def solve_expression(expression: str, **kwargs) -> str:
    """
    Parses a simple string expression like "10 + 20" and returns words.
    """

    # Match number, operator, number
    match = re.match(r"(\d+\.?\d*)\s*([\+\-\*\/x])\s*(\d+\.?\d*)", expression.strip())
    if not match:
        match = re.match(
            r"([୦-୯]+\.?[୦-୯]*)\s*([\+\-\*\/x])\s*([୦-୯]+\.?[୦-୯]*)", expression.strip()
        )

    if not match:
        raise ValueError(
            "Expression must be in format 'Number Operator Number' (e.g. 5 + 2)"
        )

    v1, op, v2 = match.groups()
    return calculate_and_express(v1, op, v2, **kwargs)
