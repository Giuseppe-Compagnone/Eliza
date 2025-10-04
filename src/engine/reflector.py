"""
reflector.py
-------------
This module implements pronoun reflection
used in the original ELIZA chatbot (Weizenbaum, 1966).
"""

import re

def reflect(fragment: str,reflections:dict[str,str]) -> str:
    """
    Reflects pronouns in a given text fragment.
    Handles punctuation and capitalization more robustly.
    """
    # Split into words and punctuation
    tokens = re.findall(r"[\w']+|[.,!?;]", fragment)

    reflected_tokens = []
    for token in tokens:
        lower = token.lower()
        if lower in reflections:
            replacement = reflections[lower]
            # Preserve capitalization if the original was capitalized
            if token[0].isupper():
                replacement = replacement.capitalize()
            reflected_tokens.append(replacement)
        else:
            reflected_tokens.append(token)

    # Join tokens with spaces (fix spacing for punctuation)
    text = " ".join(reflected_tokens)
    text = re.sub(r"\s+([.,!?;])", r"\1", text)  # remove space before punctuation
    return text