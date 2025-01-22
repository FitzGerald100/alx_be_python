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
        self.assertEqual(self.calc.add(0, 0), 0)


    def test_substraction(self):
        """"Testing the substraction method."""
        self.assertEqual(self.calc.substract(5, 4), 1)
        self.assertEqual(self.calc.substract(7, 9), -2)
        self.assertEqual(self.calc.substract(-5, -1), -4)


    def test_multiply(self):
        """Testing the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 3), 9)
        self.assertEqual(self.calc.multiply(-1, 3), -3)
        self.assertEqual(self.calc.multiply(0, 6), 6)


    def test_divide(self):
        """Testing the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-9, -1), 9)
        self.assertEqual(self.calc.divide(6, 0))

if __name__ == "__main__":
    unittest.main()