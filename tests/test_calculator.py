import unittest
from src.calculator import sum, subtract, multply, divide


class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(2, 3), 5, "La suma no funciona correctamente.")

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5, "La resta no funciona correctamente.")

    def test_multiply(self):
        assert multply(3, 2) == 6

    def test_divide(self):
        result = divide(10, 2)
        excepted = 5
        assert result == excepted