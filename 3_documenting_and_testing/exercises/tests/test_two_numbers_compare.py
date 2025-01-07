#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for two_numbers_compare function.

Test categories:
    - Standard cases: Typical integers with different relationships.
    - Edge cases: Negative numbers.
"""

import unittest

from ..two_numbers_compare import two_numbers_compare


class TestTwoNumbersCompare(unittest.TestCase):
    """Test the two_numbers_compare function"""

    # Standard Cases
    def test_minimal_input(self):
        """Should return 0 for 0 inputs"""
        self.assertEqual(two_numbers_compare(0, 0), 0)

    def test_a_smaller_than_b(self):
        """Should return the smaller number when a < b"""
        self.assertEqual(two_numbers_compare(3, 5), 3)

    def test_a_greater_than_b(self):
        """Should return the smaller number when a > b"""
        self.assertEqual(two_numbers_compare(7, 2), 2)

    def test_a_equal_b(self):
        """Should return their sum when a == b"""
        self.assertEqual(two_numbers_compare(10, 10), 20)

    # Edge Cases
    def test_negative_positive(self):
        """Should handle a negative, b positive"""
        self.assertEqual(two_numbers_compare(-7, 5), -7)

    def test_positive_negative(self):
        """Should handle a positive, b negative"""
        self.assertEqual(two_numbers_compare(5, -3), -3)

    def test_negative_negative(self):
        """Should handle negative numbers correctly"""
        self.assertEqual(two_numbers_compare(-3, -5), -5)
