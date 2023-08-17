import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.calculator.subtract(10, 5)
        self.assertEqual(result, 5)

# if __name__ == "__main__":
#     unittest.main()
