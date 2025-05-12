import unittest
from app.utils import clean_text

class TestUtils(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("  Hello\nWorld  "), "Hello World")

if __name__ == "__main__":
    unittest.main()
