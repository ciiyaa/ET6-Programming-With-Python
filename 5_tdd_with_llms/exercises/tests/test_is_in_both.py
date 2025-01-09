#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_in_both function.
Contains tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: item in both, item in one, item in none

"""

import unittest
from ..is_in_both import is_in_both


class TestIsInBoth(unittest.TestCase):
    """Test the is_in_both function"""

    def test_item_in_both_lists(self):
        """It should return True if the item is in both lists"""
        self.assertTrue(is_in_both("apple", ["apple", "banana"], ["apple", "cherry"]))

    def test_item_in_one_list_only(self):
        """It should return False if the item is in only one list"""
        self.assertFalse(is_in_both("banana", ["apple", "banana"], ["apple", "cherry"]))

    def test_item_in_neither_list(self):
        """It should return False if the item is in neither list"""
        self.assertFalse(is_in_both("orange", ["apple", "banana"], ["cherry", "grape"]))
