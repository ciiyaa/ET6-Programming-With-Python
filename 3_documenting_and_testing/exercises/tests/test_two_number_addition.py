#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for two_number_addition function.

Test categories:
    - Standard cases: typical positive, negative, and mixed numbers
    - Edge cases: minimal inputs, zeros
    - Defensive tests: wrong input types, assertions
"""

import unittest
from ..two_number_addition import two_number_addition
class TestTwoNumberAddition(unittest.TestCase):
    """Test the two_number_addition function"""

    # Standard test cases
    def test_positive_numbers(self):
        """It should add two positive numbers and return positive"""
        self.assertEqual(two_number_addition(2, 3), 5)

    def test_negative_numbers(self):
        """It should add two negative numbers and return negative"""
        self.assertEqual(two_number_addition(-2, -3), -5)

    def test_mixed_numbers(self):
        """It should handle one positive and one negative number"""
        self.assertEqual(two_number_addition(-2, 3), 1)

    # Edge cases
    def test_minimal_input(self):
        """It should return 0 for two zero inputs"""
        self.assertEqual(two_number_addition(0, 0), 0)

    # Defensive tests
    def test_not_integer(self):
        """It should raise AssertionError for non-integer input"""
        with self.assertRaises(AssertionError):
            two_number_addition(2, "one")
