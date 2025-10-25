import unittest
from src.calculator import sum, subtract


class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(2, 3), 5, "La suma no funciona correctamente.")

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5, "La resta no funciona correctamente.")