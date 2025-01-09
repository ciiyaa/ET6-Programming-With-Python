#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the mystery_5 function.

Test categories:
    - Standard cases: Moving elements from `a` to `b`, in sorted order.
"""

import unittest

from ..sort_and_merge import sort_and_merge


class TestSortAndMerge(unittest.TestCase):
    """Test the sort_and_merge function"""

    # Standard Cases
    def test_sort_and_merge_empty_b(self):
        """Should merge and sort elements from `a` and empty `b`"""
        self.assertEqual(sort_and_merge([3, 1, 2], []), [1, 2, 3])

    def test_merge_with_existing_sorted_b(self):
        """Should merge `a` into a pre-sorted `b`"""
        self.assertEqual(sort_and_merge([5], [0, 4]), [0, 4, 5])

    def test_merge_with_unsorted_b(self):
        """Should handle merging into an unsorted `b`"""
        self.assertEqual(sort_and_merge([3, 2], [5, 4]), [5, 4, 2, 3])

    def test_minimal_input(self):
        self.assertEqual(sort_and_merge([], []), [])
