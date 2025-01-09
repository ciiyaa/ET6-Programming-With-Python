#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_in_one function.
Contains tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: item in only one, item in both, item in none

"""

import unittest
from ..is_in_one import is_in_one


class TestIsInOne(unittest.TestCase):
    """Test the is_in_one function"""

    def test_item_in_only_one_list(self):
        """It should return True if the item is in only one list"""
        self.assertTrue(is_in_one("apple", ["apple", "banana"], ["cherry", "grape"]))

    def test_item_in_both_lists(self):
        """It should return False if the item is in both lists"""
        self.assertFalse(is_in_one("banana", ["apple", "banana"], ["banana", "cherry"]))

    def test_item_in_neither_list(self):
        """It should return False if the item is in neither list"""
        self.assertFalse(is_in_one("orange", ["apple", "banana"], ["cherry", "grape"]))
