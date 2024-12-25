import unittest

from ..addition import two_numbers

class TestTwoNumbers(unittest.TestCase):
    """Test the two_numbers function"""

    def test_minimal_input(self):
        """It should return 0 for two zero inputs"""
        self.assertEqual(two_numbers(0, 0), 0)
        
    def test_pos_numbers(self):
        """It should add two positive numbers and return positive"""
        self.assertEqual(two_numbers(2, 3), 5)
        
    def test_neg_numbers(self):
        """It should add two negative numbers and return negative"""
        self.assertEqual(two_numbers(-2, -3), -5)
    
    def test_mixed_numbers(self):
        """It should handle one positive and one negative number"""
        self.assertEqual(two_numbers(-2, 3), 1)
    
    def test_not_integer(self):
        """It should raise AssertionError for non-integer input"""
        with self.assertRaises(AssertionError):
            two_numbers(2, "one")
