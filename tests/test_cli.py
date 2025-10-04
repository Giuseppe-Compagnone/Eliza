# tests/test_cli.py
import unittest
from unittest.mock import patch
from src.engine.script_loader import ScriptLoader
from src.engine.interpreter import ElizaInterpreter
from src.cli.terminal import main

class TestCLI(unittest.TestCase):
    @patch("builtins.input", side_effect=["I am sad", "bye"])
    @patch("builtins.print")
    def test_cli_conversation(self, mock_print, mock_input):
        main()
        # controlla che siano state stampate almeno due risposte
        self.assertTrue(mock_print.call_count >= 2)

if __name__ == "__main__":
    unittest.main()