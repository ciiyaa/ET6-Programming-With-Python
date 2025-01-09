#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for count_characters function.

Test categories:
    - Standard cases: Typical strings and lists, with numbers
    - Edge cases: white-spaces, nested lists, empty strings and lists
    - Defensive tests: Numbers, Bool assertions
"""

import unittest
from ..count_characters import count_characters


class TestCountCharacters(unittest.TestCase):
    """Test the count_characters function"""

    # Standard Cases
    def test_minimal_list_input(self):
        """Should return NONE for empty lists"""
        self.assertEqual(count_characters([]), None)

    def test_minimal_string_input(self):
        """Should return NONE for empty strings"""
        self.assertEqual(count_characters(""), None)

    def test_string_length_4_chars(self):
        """Test with a string of 4 characters"""
        self.assertEqual(count_characters("abcd"), 4)

    def test_string_length_numbers(self):
        """Test with a string of numbers"""
        self.assertEqual(count_characters("12345"), 5)

    # Edge Cases:
    def test_string_length_with_spaces(self):
        """Test with a string containing spaces"""
        self.assertEqual(count_characters("hello world"), 11)

    def test_whitespace_only(self):
        """Test with a string of only whitespaces"""
        self.assertEqual(count_characters("   "), 3)

    def test_nested_lists(self):
        """Test with a list containing nested lists"""
        self.assertEqual(count_characters([[1, 2], "a", "b"]), 3)

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertIsNone(count_characters(""))

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(count_characters([]))

    # Defensive Assertions
    def test_invalid_type_int(self):
        """Test with an integer input"""
        with self.assertRaises(AssertionError):
            count_characters(123)

    def test_invalid_type_boolean_true(self):
        """Test with True as input"""
        with self.assertRaises(AssertionError):
            count_characters(True)
