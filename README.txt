# 📚 Citation Verification Module for Nepali Law AI Chatbot

A plug-and-play module designed to verify legal citations in AI-generated responses using a reference corpus of Nepali laws. Just feed in the AI output and your legal document corpus — the module handles extraction, verification, and cleaning.

---

## 🚀 Features

- Extracts legal citations from text (e.g., `Section 88`, `Article 12`)
- Matches against your legal corpus (exact or fuzzy)
- Flags unverified or misrepresented citations
- Rewrites or removes invalid legal statements
- FastAPI endpoint for easy integration with any chatbot

---

## 📦 Folder Structure

```
citation-verification-module/
├── app/
│   ├── __init__.py       # Initialization file for the app package
│   ├── config.py         # Configuration for corpus and settings
│   ├── extractor.py      # Extract legal citations from text
│   ├── matcher.py        # Match citations with corpus
│   ├── rewriter.py       # Rewrites or removes unverified citations
│   └── verify.py         # Main logic for citation verification
├── api/
│   └── main.py           # FastAPI wrapper for serving the API
├── tests/
│   └── test_verify.py    # Sample test for citation verification
├── run.py                # Launch the API locally
├── requirements.txt      # Dependencies
└── README.md             # Documentation for the module
```

---

## 🛠️ Installation

```bash
git clone https://github.com/your-org/citation-verification-module.git
cd citation-verification-module
pip install -r requirements.txt
```

---

## ⚙️ Usage

### 🔍 Programmatic (Python)

```python
from app.verify import verify_output

ai_text = "According to Section 88 of the Civil Code, this is allowed."
corpus = {"Section 88"}
cleaned_text = verify_output(ai_text, corpus)
print(cleaned_text)
```

---

### 🌐 API

#### ▶️ Run the Server

```bash
python run.py
```

#### 🧪 Test Endpoint

`POST /verify`

**Request:**
```json
{
  "text": "According to Section 88 of the Civil Code, this is allowed."
}
```

**Response:**
```json
{
  "cleaned": "According to the relevant legal provision, this is allowed."
}
```

---

## 📁 Config

Modify the `app/config.py` file to point to your own corpus or load from Elasticsearch later.

```python
CORPUS_PATH = "path/to/legal_corpus"
```

---

## 📌 Notes

- You can extend `matcher.py` to use Elasticsearch or FAISS for fuzzy legal lookup.
- Add a UI or dashboard for legal experts to review flagged responses (optional).

---

## 📃 License

MIT License. Free to use, adapt, and extend.

---

## 👨‍💻 Made for

This is a part of a larger AI Legal Assistant trained specifically on **Nepali Laws** 🇳🇵. The citation verification module ensures legally accurate responses for users.

---
