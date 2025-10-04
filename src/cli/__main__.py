# src/cli/__main__.py
"""
Entrypoint for ELIZA CLI.
Allows running the chatbot using `python -m src.cli`.
"""

from .terminal import main  # importa la funzione main dal terminale

if __name__ == "__main__":
    main()