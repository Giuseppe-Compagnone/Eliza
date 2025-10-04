"""
script_loader.py
----------------
Load the ELIZA DOCTOR script into structured data.
Supports initial, final, quit, pre/post substitutions, synonyms, keywords, decompositions, and reassemblies.
"""

import re
from collections import defaultdict

class ScriptLoader:
    def __init__(self, script_file: str):
        self.script_file = script_file
        self.initial = ""
        self.final = ""
        self.quit = []
        self.pre = {}
        self.post = {}
        self.synon = defaultdict(list)
        self.keywords = {}

    def load_script(self):
        current_key = None
        current_decomp = None

        with open(self.script_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Handle initial, final, quit
                if line.startswith("initial:"):
                    self.initial = line[len("initial:"):].strip()
                elif line.startswith("final:"):
                    self.final = line[len("final:"):].strip()
                elif line.startswith("quit:"):
                    self.quit.append(line[len("quit:"):].strip())

                # Handle pre/post substitutions
                elif line.startswith("pre:"):
                    parts = line[len("pre:"):].strip().split()
                    if len(parts) == 2:
                        self.pre[parts[0]] = parts[1]
                elif line.startswith("post:"):
                    parts = line[len("post:"):].strip().split()
                    if len(parts) == 2:
                        self.post[parts[0]] = parts[1]

                # Handle synonyms
                elif line.startswith("synon:"):
                    parts = line[len("synon:"):].strip().split()
                    if parts:
                        self.synon[parts[0]] = parts[1:]

                # Handle keywords
                elif line.startswith("key:"):
                    match = re.match(r"key:\s+(\w+)(?:\s+(\d+))?", line)
                    if match:
                        current_key = match.group(1)
                        rank = int(match.group(2)) if match.group(2) else 0
                        self.keywords[current_key] = {
                            "rank": rank,
                            "decompositions": []
                        }

                # Handle decomposition
                elif line.startswith("decomp:") and current_key:
                    decomp = line[len("decomp:"):].strip()
                    current_decomp = {"pattern": decomp, "reasmb": []}
                    self.keywords[current_key]["decompositions"].append(current_decomp)

                # Handle reassembly
                elif line.startswith("reasmb:") and current_decomp:
                    reasmb = line[len("reasmb:"):].strip()
                    current_decomp["reasmb"].append(reasmb)

        return {
            "initial": self.initial,
            "final": self.final,
            "quit": self.quit,
            "pre": self.pre,
            "post": self.post,
            "synon": dict(self.synon),
            "keywords": self.keywords
        }
