import unittest
from modules.calculator import *

class TestCalculator(unittest.TestCase):

    def setUp(self):
        pass

    def test_addition(self):
        self.assertEqual(6, addition(2, 4))

    def test_subtraction(self):
        self.assertEqual(4, subtraction(10, 6))

    def test_multiplication(self):
        self.assertEqual(15, multiplication(3, 5))

    def test_division(self):
        self.assertEqual(3, division(21, 7))