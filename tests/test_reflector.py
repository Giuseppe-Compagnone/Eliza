# tests/test_reflector.py
import unittest
from src.engine.reflector import reflect

class TestReflector(unittest.TestCase):
    def setUp(self):
        self.post = {
            "am": "are",
            "your": "my",
            "me": "you"
        }

    def test_reflect_simple(self):
        self.assertEqual(reflect("i am happy", self.post), "i are happy")
        self.assertEqual(reflect("your book", self.post), "my book")
        self.assertEqual(reflect("tell me", self.post), "tell you")

    def test_reflect_no_change(self):
        self.assertEqual(reflect("hello world", self.post), "hello world")

if __name__ == "__main__":
    unittest.main()
