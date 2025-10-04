# tests/test_script_loader.py
import unittest
from src.engine.script_loader import ScriptLoader

class TestScriptLoader(unittest.TestCase):
    def setUp(self):
        self.loader = ScriptLoader("src/scripts/doctor.txt")

    def test_load_script(self):
        data = self.loader.load_script()
        # controlla che le chiavi principali esistano
        self.assertIn("initial", data)
        self.assertIn("final", data)
        self.assertIn("keywords", data)
        self.assertIn("quit", data)

    def test_quit_words(self):
        data = self.loader.load_script()
        self.assertIn("bye", data["quit"])
        self.assertIn("quit", data["quit"])

if __name__ == "__main__":
    unittest.main()
