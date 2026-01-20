"""
odianumerals
============
A comprehensive library for Odia numeral processing, including cardinal,
ordinal, classical, currency, and mathematical representations.
"""

from .cardinal_converter import to_odia_words
from .classical_converter import to_odia_barnabodha_words
from .currency_formatter import to_odia_currency
from .digit_formatter import format_indian_style, to_odia_digits
from .english_converter import number_to_words as to_english_words
from .math_logic import calculate_and_express
from .ordinal_converter import to_ordinal_numeral, to_ordinal_words
from .special_converter import (
    to_fraction_words,
    to_percentage_words,
    to_reading_sequence,
)
from .text_processor import extract_odia_numbers, replace_numbers

__version__ = "1.0.0"
__author__ = "Srinibash Samal"
