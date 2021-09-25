import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase):
    """Test EnglishtoFrench function in translator.py"""
    def test1(self):
        """Use self.assert to check translation."""
        #self.assertEqual(englishToFrench(None),None) # Null test
        self.assertEqual(englishToFrench('Hello'),'Bonjour')  # Hello Test

class TestfrenchToEnglish(unittest.TestCase):
    """Test FrenchtoEnglish function in translator.py"""
    def test1(self):
        """Use self.assert to check translation."""
        #self.assertEqual(frenchToEnglish(None),None) # Null test
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')  # Bonjour Test

unittest.main()
