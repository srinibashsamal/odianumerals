# odianumerals

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

```bash
import odianumerals as odi

odi.to_odia_digits(1234.50)
# ୧୨୩୪.୫୦

odi.to_odia_words(150000)
# ଏକ ଲକ୍ଷ ପଚାଶ ହଜାର
```

### Ordinals and Currency

```bash
odi.to_ordinal_numeral(1, lang="or")
# ୧ମ

odi.to_ordinal_words(2, lang="or")
# ଦ୍ୱିତୀୟ

odi.to_odia_currency(105.75)
# ଏକ ଶହ ପାଞ୍ଚ ଟଙ୍କା ସତୁରୀ ପଇସା
```

### Mathematical Expressions

```bash
odi.calculate_and_express(10, "+", 5)

# ଦଶ ମିଶାଣ ପାଞ୍ଚ ସମାନ ପନ୍ଦର
```

## 🎯 Use Cases

- Odia NLP and text normalization
- Educational and e-learning platforms
- Financial and government localization
- Digital humanities research
- Voice assistants and TTS pipelines

## ✍️ Author

**Srinibash Samal**  
_A dedicated tool for Odia Language Technology._

## 🤝 Contributing

### Contributions are welcome and encouraged.

## 🗺️ Roadmap

- Enhanced decimal pronunciation rules
- Pluralization support
- Text-to-speech friendly output
- Expanded Barnabodha unit coverage
- Integration helpers for NLP pipelines

## 📜 License

This project is released under an open-source license
to promote Odia language computing and digital accessibility.

Made with ❤️ for the Odia language
