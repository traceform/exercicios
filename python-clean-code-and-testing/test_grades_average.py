# Run as "python -m unittest -v test_grades_average.py" for verbose output (shows docstring, test function names)
# Run as "python test_grades_average.py -v" to run grouped tests with category headers

import unittest
from unittest.mock import patch
from grades_average import get_quantity, get_float, calculate_average

# -------------------- Test Quantity -------------------- #
class TestQuantity(unittest.TestCase):

    @patch("builtins.input", side_effect=["0", "5"])
    def test_reject_zero_then_accept_valid(self, mock_input):
        """>>> ZERO IS BLOCKED"""
        with patch("builtins.print"):
            result = get_quantity("Quantidade: ")
        self.assertEqual(result, 5)

    @patch("builtins.input", side_effect=["-1", "3"])
    def test_reject_negative_then_accept_valid(self, mock_input):
        """>>> NEGATIVE VALUES BLOCKED"""
        with patch("builtins.print"):
            result = get_quantity("Quantidade: ")
        self.assertEqual(result, 3)

    @patch("builtins.input", side_effect=["abc", "0", "-2", "7"])
    def test_reject_multiple_invalid_then_accept_valid(self, mock_input):
        """>>> MIX OF INVALID INPUTS BEFORE A VALID NUMBER"""
        with patch("builtins.print"):
            result = get_quantity("Quantidade: ")
        self.assertEqual(result, 7)

# -------------------- Test Float -------------------- #
class TestFloat(unittest.TestCase):

    @patch("builtins.input", side_effect=["True", "False", "[1,2]", "7.5"])
    def test_non_numeric_then_valid_float(self, mock_input):
        """>>> NON-NUMERIC VALUES BLOCKED"""
        with patch("builtins.print"):
            result = get_float("Nota: ")
        self.assertEqual(result, 7.5)

    @patch("builtins.input", side_effect=["a", "7"])
    def test_letter_then_valid_float(self, mock_input):
        """>>> LETTERS BLOCKED"""
        with patch("builtins.print"):
            result = get_float("Nota: ")
        self.assertEqual(result, 7.0)

    @patch("builtins.input", side_effect=["7,5", "7.5"])
    def test_comma_float_then_valid(self, mock_input):
        """>>> COMMA IS INVALID IN Python float()"""
        with patch("builtins.print"):
            result = get_float("Nota: ")
        self.assertEqual(result, 7.5)

    @patch("builtins.input", side_effect=["-1", "7"])
    def test_negative_float_then_valid(self, mock_input):
        """>>> NEGATIVE VALUES BLOCKED"""
        with patch("builtins.print"):
            result = get_float("Nota: ")
        self.assertEqual(result, 7.0)

    @patch("builtins.input", side_effect=["0"])
    def test_zero_float(self, mock_input):
        """>>> GREATER THAN 0 VALUES ALLOWED"""
        with patch("builtins.print"):
            result = get_float("Nota: ")
        self.assertEqual(result, 0.0)

# -------------------- Test Grades / Average -------------------- #
class TestGrades(unittest.TestCase):

    def test_average_normal_case(self):
        """>>> TEST AVERAGE OF NORMAL GRADES"""
        grades = [8.0, 7.0, 9.0]
        self.assertEqual(calculate_average(grades), 8.0)

    def test_average_single_grade(self):
        """>>> TEST AVERAGE WITH ONLY ONE GRADE"""
        grades = [10.0]
        self.assertEqual(calculate_average(grades), 10.0)

    def test_average_empty_list(self):
        """>>> TEST THAT EMPTY LIST RAISES ValueError"""
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_average_with_decimals(self):
        """>>> TEST AVERAGE WITH DECIMAL VALUES"""
        grades = [7.5, 8.5]
        self.assertAlmostEqual(calculate_average(grades), 8.0, places=2)

# -------------------- Run Tests -------------------- #
if __name__ == "__main__":
    print("\n===== RUNNING QUANTITY TESTS =====\n")
    unittest.TextTestRunner(verbosity=2).run(
        unittest.TestLoader().loadTestsFromTestCase(TestQuantity)
    )

    print("\n===== RUNNING FLOAT TESTS =====\n")
    unittest.TextTestRunner(verbosity=2).run(
        unittest.TestLoader().loadTestsFromTestCase(TestFloat)
    )

    print("\n===== RUNNING GRADES/AVERAGE TESTS =====\n")
    unittest.TextTestRunner(verbosity=2).run(
        unittest.TestLoader().loadTestsFromTestCase(TestGrades)
    )
