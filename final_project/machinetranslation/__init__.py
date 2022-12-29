import unittest
from translator import english_to_french
from translator import french_to_english

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        self.assertNotEqual(english_to_french(0),0)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test2(self):
        self.assertNotEqual(french_to_english(0),0)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == "__main__":
    unittest.main()
