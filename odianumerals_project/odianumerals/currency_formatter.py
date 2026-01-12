from typing import Union

import classical_converter as barnabodha
import internal_utils as util
from cardinal_converter import to_odia_words


def to_odia_currency(
    number: Union[str, int, float],
    barnabodha_style: bool = False,
    as_roman: bool = False,
    as_odilish: bool = False,
) -> str:
    """
    Convert a numeric amount into Odia currency words
    (Tanka and Paisa).

    Examples:
        10.50 -> ଦଶ ଟଙ୍କା ପଚାଶ ପଇସା
        5     -> ପାଞ୍ଚ ଟଙ୍କା
        0.70  -> ସତୁରୀ ପଇସା

    Args:
        number (Union[str, int, float]): Amount
        barnabodha_style (bool): Use classical Barnabodha system. Defaults to False.
        as_roman (bool): Romanized output. Defaults to False.
        as_odilish (bool): Odilish output. Defaults to False.

    Returns:
        str: Currency representation in words
    """
    num_str = util._validate_and_format(number)
    index = util._resolve_language_index(as_roman, as_odilish)

    tanka_label = ("ଟଙ୍କା", "ṭaṅkā", "tanka")[index]
    paisa_label = ("ପଇସା", "paisa", "paisa")[index]

    if "." in num_str:
        tanka_part, paisa_raw = num_str.split(".")
        paisa_value = int((paisa_raw + "0")[:2])
    else:
        tanka_part, paisa_value = num_str, 0

    tanka_value = int(tanka_part)

    converter = (
        barnabodha.to_odia_barnabodha_words if barnabodha_style else to_odia_words
    )

    tanka_words = converter(tanka_value, as_roman=as_roman, as_odilish=as_odilish)
    paisa_words = (
        converter(paisa_value, as_roman=as_roman, as_odilish=as_odilish)
        if paisa_value > 0
        else ""
    )

    if tanka_value == 0 and paisa_value == 0:
        return f"{tanka_words} {tanka_label}"
    if tanka_value == 0 and paisa_value > 0:
        return f"{paisa_words} {paisa_label}"
    if paisa_value > 0 and paisa_value == 0:
        return f"{tanka_words} {tanka_label}"

    return f"{tanka_words} {tanka_label} {paisa_words} {paisa_label}"
