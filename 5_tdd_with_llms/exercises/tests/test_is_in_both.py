#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_in_both function.
Contains tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: item in both, item in one, item in none
    - Edge cases: Empty lists
    - Defensive tests: invalid inputs

"""

import unittest
from ..is_in_both import is_in_both


class TestIsInBoth(unittest.TestCase):
    """Test the is_in_both function"""

    # Standard Tests
    def test_item_in_both_lists(self):
        """It should return True if the item is in both lists"""
        self.assertTrue(is_in_both("apple", ["apple", "banana"], ["apple", "cherry"]))

    def test_item_in_one_list_only(self):
        """It should return False if the item is in only one list"""
        self.assertFalse(is_in_both("banana", ["apple", "banana"], ["apple", "cherry"]))

    def test_item_in_neither_list(self):
        """It should return False if the item is in neither list"""
        self.assertFalse(is_in_both("orange", ["apple", "banana"], ["cherry", "grape"]))

    # Edge Tests
    def test_empty_lists(self):
        """It should return False if both lists are empty"""
        self.assertFalse(is_in_both("apple", [], []))

    def test_empty_list1(self):
        """It should return False if the first list is empty"""
        self.assertFalse(is_in_both("apple", [], ["apple", "cherry"]))

    def test_empty_list2(self):
        """It should return False if the second list is empty"""
        self.assertFalse(is_in_both("apple", ["apple", "banana"], []))

    # Defensive Tests
    def test_item_not_a_string(self):
        """It should raise an AssertionError if the item is not a string"""
        with self.assertRaises(AssertionError):
            is_in_both(123, ["apple", "banana"], ["apple", "cherry"])

    def test_list1_not_a_list(self):
        """It should raise an AssertionError if the first argument is not a list"""
        with self.assertRaises(AssertionError):
            is_in_both("apple", "not_a_list", ["apple", "cherry"])

    def test_list2_not_a_list(self):
        """It should raise an AssertionError if the second argument is not a list"""
        with self.assertRaises(AssertionError):
            is_in_both("apple", ["apple", "banana"], "not_a_list")
