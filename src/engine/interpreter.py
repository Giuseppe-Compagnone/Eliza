"""
interpreter.py
---------------
The main ELIZA interpreter.
Takes user input, applies preprocessing via Parser, matches keywords,
decomposes input, applies reassembly, reflection, and memory, returns output.
"""

import random
import re
from .reflector import reflect
from .parser import Parser
from .memory import Memory
from utils import clean_text

class ElizaInterpreter:
    def __init__(self, script_data):
        """
        Initialize interpreter with script data from ScriptLoader
        """
        self.initial = script_data["initial"]
        self.final = script_data["final"]
        self.quit_words = set(script_data["quit"])
        self.pre = script_data["pre"]
        self.post = script_data["post"]
        self.synon = script_data["synon"]
        self.keywords = script_data["keywords"]
        self.goto_stack = []

        # Initialize parser for pre-substitutions
        self.parser = Parser(pre_subs=self.pre)
        # Initialize memory
        self.memory = Memory(max_size=50)

    def preprocess(self, user_input):
        """
        Apply parser: cleaning + sentence splitting + pre-substitutions
        """
        return self.parser.parse(user_input)

    def match_keyword(self, user_input):
        """Return the keyword with highest rank found in input"""
        found_keywords = []
        for key, data in self.keywords.items():
            if key in user_input:
                found_keywords.append((data["rank"], key))
        if found_keywords:
            return max(found_keywords)[1]
        else:
            return "xnone"  # default fallback

    def decompose(self, keyword, user_input):
        """
        Try to match user_input against each decomposition pattern of the keyword
        Return the decomposition and matched groups
        """
        for decomp in self.keywords[keyword]["decompositions"]:
            pattern = decomp["pattern"]
            regex = re.escape(pattern).replace(r"\*", "(.*)")
            match = re.match(regex, user_input)
            if match:
                return decomp, match.groups()
        return None, None

    def reassemble(self, decomp, groups):
        """
        Select a reassembly rule and apply reflection/post substitutions
        """
        reasmb = random.choice(decomp["reasmb"])
        if reasmb.startswith("goto "):
            goto_key = reasmb.split()[1]
            self.goto_stack.append(goto_key)
            return None
        # Replace placeholders (1),(2),... and apply post/reflection
        def replace_group(match):
            idx = int(match.group(1)) - 1
            return reflect(groups[idx], self.post)
        response = re.sub(r"\((\d+)\)", replace_group, reasmb)
        return response

    def respond(self, user_input):
        """
        Generate ELIZA response to user input
        """
        user_input = clean_text(user_input)  # pulizia extra
        preprocessed = self.preprocess(user_input)

        # Handle quit
        if preprocessed in self.quit_words:
            return self.final

        # Handle goto stack
        if self.goto_stack:
            keyword = self.goto_stack.pop()
        else:
            keyword = self.match_keyword(preprocessed)

        # Try to decompose and reassemble
        decomp, groups = self.decompose(keyword, preprocessed)

        if decomp:
            response = self.reassemble(decomp, groups)
            # Remember input if pattern starts with $
            if decomp["pattern"].startswith("$"):
                self.memory.remember(preprocessed)
            if response is None and self.goto_stack:
                return self.respond(user_input)
            return response

        # No decomposition matched: try memory
        mem_response = self.memory.recall()
        if mem_response:
            return mem_response

        # Fallback to xnone
        decomp, groups = self.decompose("xnone", preprocessed)
        return self.reassemble(decomp, groups)