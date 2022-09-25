import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def testnull(self):
        self.assertEqual(english_to_french(" "), " ")  
    def test(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")  

class TestF2E(unittest.TestCase): 
    def testnull(self):
        self.assertEqual(french_to_english(" "), " ")  
    def test(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")  

unittest.main()