#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for sort_numbers function.
Contains tests to ensure correct functionality of the implementation.

Test categories:
    - Standard cases: lists with positive, negative, and mixed numbers

"""

import unittest
from ..sort_numbers import sort_numbers


class TestSortNumbers(unittest.TestCase):
    """Test the sort_numbers function"""

    def test_sorted_list(self):
        """It should return the same list if it's already sorted"""
        self.assertEqual(sort_numbers([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_reverse_sorted_list(self):
        """It should return a sorted list when the input is reverse sorted"""
        self.assertEqual(sort_numbers([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_unsorted_list(self):
        """It should sort an unsorted list"""
        self.assertEqual(sort_numbers([3, 1, 4, 1, 5]), [1, 1, 3, 4, 5])

    def test_negative_numbers(self):
        """It should correctly sort a list with negative numbers"""
        self.assertEqual(sort_numbers([-3, -1, -4, -2]), [-4, -3, -2, -1])

    def test_mixed_numbers(self):
        """It should correctly sort a list with mixed positive and negative numbers"""
        self.assertEqual(sort_numbers([3, -1, 4, -2]), [-2, -1, 3, 4])
