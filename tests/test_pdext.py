from unittest import TestCase

from potion.pdext import foo

class Tests(TestCase):
    
    def test_1(self):
        self.assertTrue(foo() == "bar")
        