# ELIZA DOCTOR Script Specification

This document defines the format and rules for the DOCTOR script used by ELIZA.

---

## 1. Script Format

The script is a plain text file with the following directives:

- **initial:**  
  Initial greeting message.

- **final:**  
  Final message when user quits.

- **quit:**  
  Words that terminate the session (e.g., "bye", "goodbye", "quit").

- **pre:**  
  Substitutions applied to input before matching (e.g., "dont" → "don't").

- **post:**  
  Substitutions applied to generated responses (e.g., "am" → "are").

- **synon:**  
  Defines synonyms for keywords (e.g., "belief" → "feel think believe").

- **key:**  
  Defines a keyword to match. Can include an optional rank for priority.

- **decomp:**  
  Decomposition pattern for a keyword. Input is matched against this pattern.

- **reasmb:**  
  Reassembly rule to generate response from a decomposition match. Can include placeholders for captured groups.

---

## 2. Directive Examples

```text
initial: How do you do. Please tell me your problem.
final: Goodbye. Thank you for talking to me.
quit: bye
quit: goodbye

pre: dont don't
pre: cant can't

post: am are
post: was were

synon: belief feel think believe

key: sad 2
  decomp: * I am sad *
    reasmb: I'm sorry to hear you are sad.
    reasmb: Do you often feel sad?

key: mother
  decomp: * I remember my mother *
    reasmb: Do you often think about your mother?
```

## 3. Parsing Rules

1. Lines starting with # are comments and ignored.

2. Whitespace is trimmed at the start and end of lines.

3. Directives are case-insensitive.

4. Decomposition patterns can use \* as a wildcard to capture any sequence of words.

5. Reassembly rules can reference captured wildcard groups.

## 4. Notes

- Keywords with higher rank are prioritized when multiple matches exist.

- Pre-substitutions are applied before keyword matching.

- Post-substitutions are applied after reassembly and before output.
