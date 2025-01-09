#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the filter_containing_substring function.

Test categories:
    - Standard cases: Matching and non-matching substrings.
    - Edge cases: Empty input lists or substrings.
    - Defensive tests: Invalid input type assertions.
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

    # Edge Cases
    def test_empty_list(self):
        """Should return an empty list when the input list is empty"""
        self.assertEqual(filter_containing_substring([], "cat"), [])

    def test_empty_substring(self):
        """Should return all strings when the substring is empty"""
        self.assertEqual(
            filter_containing_substring(["one", "two", "three"], ""),
            ["one", "two", "three"],
        )

    def test_empty_list_and_substring(self):
        """Should return an empty list when both inputs are empty"""
        self.assertEqual(filter_containing_substring([], ""), [])

    # Defensive Tests
    def test_non_string_elements(self):
        """Should raise an AssertionError when the list contains non-string elements"""
        with self.assertRaises(AssertionError):
            filter_containing_substring([1, 2, 3], "1")

    def test_invalid_type_first_argument(self):
        """Should raise an AssertionError when the first argument is not a list"""
        with self.assertRaises(AssertionError):
            filter_containing_substring("not_a_list", "a")

    def test_invalid_type_second_argument(self):
        """Should raise an AssertionError when the second argument is not a string"""
        with self.assertRaises(AssertionError):
            filter_containing_substring(["apple", "banana"], 5)
