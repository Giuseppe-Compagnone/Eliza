# ELIZA Chatbot – Design Overview

## 1. Introduction

ELIZA is a historic chatbot simulating a psychotherapist using pattern matching and substitution rules. This implementation recreates the classic DOCTOR script in Python with a modular design.

---

## 2. Architecture

```text
Eliza/
    ├── src/
    │ ├── engine/
    │ ├── scripts/
    │ ├── cli/
    │ └── utils/
```

### Engine (`src/engine`)

The core logic of ELIZA:

- **parser.py** – tokenizes user input, handles punctuation and sentence boundaries.
- **reflector.py** – handles pronoun substitution (e.g., “I → you”, “my → your”).
- **script_loader.py** – loads the DOCTOR script into structured data (keywords, decompositions, reassemblies, synonyms, pre/post substitutions).
- **interpreter.py** – selects the response based on matched keywords, ranks, and decomposition/reassembly rules.
- **memory.py** – stores prior user inputs and responses for “memory” rules (optional).

### Scripts (`src/scripts`)

Contains plain-text scripts defining the behavior of ELIZA. Currently:

- `doctor.txt` – the original DOCTOR script.

### CLI (`src/cli`)

Provides a command-line interface:

- `terminal.py` – loops through user input, invokes interpreter, prints responses.

### Utilities (`src/utils`)

Helper functions:

- `text_utils.py` – tokenization, normalization, punctuation handling, logging.

---

## 3. Workflow

1. **Script Loading**
   - `script_loader.py` reads `doctor.txt`, parses rules, stores them in structured objects.
2. **User Input Parsing**
   - `parser.py` tokenizes and normalizes user input.
3. **Keyword Matching**
   - `interpreter.py` searches for keywords according to rank.
4. **Decomposition & Reassembly**
   - Input is matched to decomposition patterns; responses are generated using reassembly rules and pronoun reflection.
5. **Memory Handling**
   - Certain responses may be stored for later reuse (if memory rules apply).
6. **CLI Interaction**
   - The response is printed, and loop continues until a quit word is detected.

---

## 4. Extensibility

- Additional scripts can be added to `src/scripts/`.
- The interpreter and loader are designed to accommodate new rules without changing the engine code.
- CLI can be replaced with a GUI or web interface.

---

## 5. Dependencies

- Python 3.10+ recommended.
- Standard library only (no external dependencies required).
