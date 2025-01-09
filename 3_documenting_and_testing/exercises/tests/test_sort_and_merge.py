#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the mystery_5 function.

Test categories:
    - Standard cases: Moving elements from `a` to `b`, in sorted order.
    - Edge cases: Empty lists and duplicates.
    - Defensive tests: Non-list inputs.
"""

import unittest

from ..sort_and_merge import sort_and_merge


class TestSortAndMerge(unittest.TestCase):
    """Test the sort_and_merge function"""

    # Standard Cases
    def test_merge_with_existing_sorted_b(self):
        """Should merge `a` into a pre-sorted `b`"""
        self.assertEqual(sort_and_merge([5], [0, 4]), [0, 4, 5])

    def test_merge_with_unsorted_b(self):
        """Should handle merging into an unsorted `b`"""
        self.assertEqual(sort_and_merge([3, 2], [5, 4]), [5, 4, 2, 3])

    # Edge Cases
    def test_minimal_input(self):
        """Should return an empty list when both `a` and `b` are empty"""
        self.assertEqual(sort_and_merge([], []), [])

    def test_empty_a_only(self):
        """Should return `b` unchanged when `a` is empty"""
        self.assertEqual(sort_and_merge([], [10, 20]), [10, 20])

    def test_empty_b_only(self):
        """Should return a sorted `a` when `b` is empty"""
        self.assertEqual(sort_and_merge([3, 1, 2], []), [1, 2, 3])

    def test_duplicates_in_a_and_b(self):
        """Should handle duplicates correctly"""
        self.assertEqual(sort_and_merge([2, 2, 3], [2, 3]), [2, 3, 2, 2, 3])

    # Defensive Tests
    def test_invalid_type_a_not_list(self):
        """Should raise an AssertionError if `a` is not a list"""
        with self.assertRaises(AssertionError):
            sort_and_merge("not a list", [])

    def test_invalid_type_b_not_list(self):
        """Should raise an AssertionError if `b` is not a list"""
        with self.assertRaises(AssertionError):
            sort_and_merge([], "not a list")

    def test_invalid_type_both_not_lists(self):
        """Should raise an AssertionError if neither `a` nor `b` is a list"""
        with self.assertRaises(AssertionError):
            sort_and_merge("not a list", "also not a list")
