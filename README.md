# odianumerals

[![Python Version](https://img.shields.io/pypi/pyversions/odianumerals)](https://pypi.org/project/odianumerals/)
[![PyPI version](https://img.shields.io/pypi/v/odianumerals.svg)](https://pypi.org/project/odianumerals/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Source-black?logo=github)](https://github.com/srinibashsamal/odianumerals)
![Project Status](https://img.shields.io/badge/status-active-success)

**odianumerals** is a linguistically accurate and extensible Python library for working with **Odia numerals and number expressions**.  
It supports modern and classical Odia numbering systems, currency representation, ordinals, and natural-language mathematical expressions.

Built with a strong focus on **Indian numbering conventions** and **Odia linguistic correctness**, this library is suitable for NLP, education, localization, and digital humanities projects.

---

## 🚀 Features

- **Digit Conversion**
  - English ↔ Odia digit transformation
  - Decimal and formatted numeric support

- **Number to Words (Odia)**
  - Integer and decimal conversion
  - Indian scale: Thousand, Lakh, Crore
  - Grammatically accurate Odia word formation

- **Number to Words (English – Indian System)**
  - English number words using Lakh/Crore grouping

- **Classical Barnabodha System**
  - Traditional Odia large-number units  
    (Ayuta, Niyuta, Koti, Arbuda, etc.)

- **Ordinal Numbers**
  - Ordinal numerals: `1 → ୧ମ`, `2 → ୨ୟ`
  - Ordinal words: `1st → ପ୍ରଥମ`, `2nd → ଦ୍ୱିତୀୟ`

- **Currency Representation**
  - Tanka–Paisa conversion
  - Accurate fractional handling

- **Mathematical Expressions**
  - Human-readable Odia sentences for arithmetic operations

- **NLP Utilities**
  - Detect, replace, and normalize numerals inside text blocks

---

## 📦 Installation

```bash
pip install odianumerals
```

## 🛠 Usage Examples

### Digit Conversion and Cardinal Words

```python
import odianumerals as odi

# Script Conversion
print(odi.to_odia_digits(1234.50))
# Output: ୧୨୩୪.୫୦

# Odia Word Representation
print(odi.to_odia_words(150000))
# Output: ଏକ ଲକ୍ଷ ପଚାଶ ହଜାର

# English (Indian Scale) Words
print(odi.to_english_words(125000))
# Output: one lakh twenty-five thousand
```

### Ordinals and Currency

```python
# Numeric Ordinals (Supports 'or' or 'od')
print(odi.to_ordinal_numeral(1, lang="or"))
# Output: ୧ମ

# Word-based Ordinals
print(odi.to_ordinal_words(2, lang="or"))
# Output: ଦ୍ୱିତୀୟ

# Monetary Formatting
print(odi.to_odia_currency(105.75))
# Output: ଏକ ଶହ ପାଞ୍ଚ ଟଙ୍କା ସତୁରୀ ପଇସା
```

### Classical and Mathematical Logic

```python
# Classical Barnabodha System
print(odi.to_odia_barnabodha_words(10000))
# Output: ଏକ ଅୟୁତ (One Ayuta)
```

### Mathematical Expressions

```python
# Math in Words
print(odi.calculate_and_express(10, "+", 5))
# Output: ଦଶ ମିଶାଣ ପାଞ୍ଚ ସମାନ ପନ୍ଦର

```

## 🎯 Use Cases

- **Odia NLP**: Text normalization and pre-processing for AI models.
- **FinTech**: Generating human-readable invoices and receipts in Odia.
- **Education**: Building math and linguistic e-learning tools for Odisha.
- **Localization**: Adapting global software for the Odia-speaking demographic.

## ✍️ Author

**Srinibash Samal**  
_A dedicated tool for Odia Language Technology._

## 🤝 Contributing

Contributions are welcome! If you find a bug or have a feature request,
please open an issue on the [GitHub repository](https://github.com/srinibashsamal/odianumerals).

## 🗺️ Roadmap

- Enhanced decimal pronunciation rules
- Pluralization support for linguistic accuracy
- Text-to-speech friendly output modes
- Expanded Barnabodha unit coverage
- Integration helpers for popular NLP pipelines

## 📜 License

This project is released under the **MIT License**.

Made with ❤️ for the [Odia](https://en.wikipedia.org/wiki/Odia_language) language
