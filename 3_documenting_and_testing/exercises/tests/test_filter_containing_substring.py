#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the filter_containing_substring function.

Test categories:
    - Standard cases: Matching and non-matching substrings.
"""

import unittest

from ..filter_containing_substring import filter_containing_substring


class TestFilterContainingSubstring(unittest.TestCase):
    """Test filter_containing_substring function"""

    # Standard Cases
    def test_single_match(self):
        """Should return a list with one string containing the substring"""
        self.assertEqual(
            filter_containing_substring(["apple", "banana", "cherry"], "ana"),
            ["banana"],
        )

    def test_multiple_matches(self):
        """Should return all strings containing the substring"""
        self.assertEqual(
            filter_containing_substring(["cat", "caterpillar", "bat"], "cat"),
            ["cat", "caterpillar"],
        )

    def test_no_matches(self):
        """Should return an empty list when no string contains the substring"""
        self.assertEqual(
            filter_containing_substring(["dog", "horse", "rabbit"], "cat"), []
        )

    def test_minimal_input_list(self):
        """"""
        self.assertEqual(filter_containing_substring([], []), [])

    def test_minimal_input_string(self):
        """"""
        self.assertEqual(filter_containing_substring("", ""), [])
