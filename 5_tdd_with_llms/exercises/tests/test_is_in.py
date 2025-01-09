#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_in function.
Contains tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: item in one, item in both, item in none

"""

import unittest
from ..is_in import is_in


class TestIsIn(unittest.TestCase):
    """Test the is_in function"""

    def test_item_in_one_list(self):
        """It should return True if the item is in one list"""
        self.assertTrue(is_in("apple", ["apple", "banana"], ["cherry", "grape"]))

    def test_item_in_both_lists(self):
        """It should return True if the item is in both lists"""
        self.assertTrue(is_in("banana", ["apple", "banana"], ["banana", "cherry"]))

    def test_item_in_neither_list(self):
        """It should return False if the item is in neither list"""
        self.assertFalse(is_in("orange", ["apple", "banana"], ["cherry", "grape"]))
