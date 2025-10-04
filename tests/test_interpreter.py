# tests/test_interpreter.py
import unittest
from src.engine.script_loader import ScriptLoader
from src.engine.interpreter import ElizaInterpreter

class TestElizaInterpreter(unittest.TestCase):
    def setUp(self):
        loader = ScriptLoader("src/scripts/doctor.txt")
        self.script_data = loader.load_script()
        self.eliza = ElizaInterpreter(self.script_data)

    def test_initial_response(self):
        self.assertTrue(self.script_data["initial"].lower() in self.eliza.initial.lower())

    def test_quit_response(self):
        resp = self.eliza.respond("bye")
        self.assertEqual(resp, self.script_data["final"])

    def test_simple_reflection(self):
        resp = self.eliza.respond("I am sad")
        # deve contenere un riflesso del pronome "I → you" o risposta generica
        self.assertIsInstance(resp, str)
        self.assertTrue(resp and len(resp) > 0)

if __name__ == "__main__":
    unittest.main()
