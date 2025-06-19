import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(1, 4), -3)
        self.assertEqual(self.calc.subtract(-1, -4), 3)

    def test_multiplication(self):
        sefl.assertEqual(self.calc.multiply(2, 5), 10)
        sefl.assertEqual(self.calc.multiply(2, -5), -10)
        self.assertEqual(self.calc.multiply('2', 5), "Error: connot multiply string in number")

    def test_division(self):
        self.assertEqual(self.calc.divide(2, 0), "Error: connot divide by zero.")
        self.assertEqual(self.calc.divide(2, 2), 1)
