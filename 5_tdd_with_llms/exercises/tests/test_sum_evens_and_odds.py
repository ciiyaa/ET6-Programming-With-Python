#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for sum_evens_and_odds function.
Contains tests to ensure correct functionality of the implementation.

Test categories:
    - Standard cases: typical lists with mixed numbers
    - Edge cases: empty list, single element lists

"""

import unittest
from ..sum_evens_and_odds import sum_evens_and_odds


class TestSumEvensAndOdds(unittest.TestCase):
    """Test the sum_evens_and_odds function"""

    # Standard Tests
    def test_mixed_numbers(self):
        """It should correctly sum even and odd numbers in a mixed list"""
        self.assertEqual(sum_evens_and_odds([1, 2, 3, 4, 5]), {"even": 6, "odd": 9})

    def test_all_evens(self):
        """It should correctly sum a list of even numbers"""
        self.assertEqual(sum_evens_and_odds([2, 4, 6, 8]), {"even": 20, "odd": 0})

    def test_all_odds(self):
        """It should correctly sum a list of odd numbers"""
        self.assertEqual(sum_evens_and_odds([1, 3, 5, 7]), {"even": 0, "odd": 16})

    # Edge Tests
    def test_empty_list(self):
        """It should return 0 sums for both even and odd in an empty list"""
        self.assertEqual(sum_evens_and_odds([]), {"even": 0, "odd": 0})

    def test_single_even(self):
        """It should correctly sum a single even number"""
        self.assertEqual(sum_evens_and_odds([4]), {"even": 4, "odd": 0})

    def test_single_odd(self):
        """It should correctly sum a single odd number"""
        self.assertEqual(sum_evens_and_odds([5]), {"even": 0, "odd": 5})

    def test_zero_in_list(self):
        """It should correctly handle a list containing zero"""
        self.assertEqual(sum_evens_and_odds([0, 1, 2]), {"even": 2, "odd": 1})
