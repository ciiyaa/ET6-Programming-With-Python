#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_in_one function.
Contains tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: item in only one, item in both, item in none
    - Edge cases: empty lists
"""

import unittest
from ..is_in_one import is_in_one


class TestIsInOne(unittest.TestCase):
    """Test the is_in_one function"""

    # Standard Tests
    def test_item_in_only_one_list(self):
        """It should return True if the item is in only one list"""
        self.assertTrue(is_in_one("BMW", ["BMW", "Cadillac"], ["Audi", "Nissan"]))

    def test_item_in_both_lists(self):
        """It should return False if the item is in both lists"""
        self.assertFalse(
            is_in_one("Cadillac", ["BMW", "Cadillac"], ["Cadillac", "Audi"])
        )

    def test_item_in_neither_list(self):
        """It should return False if the item is in neither list"""
        self.assertFalse(is_in_one("Honda", ["BMW", "Cadillac"], ["Audi", "Nissan"]))

    # Edge Tests
    def test_empty_lists(self):
        """It should return False if both lists are empty"""
        self.assertFalse(is_in_one("BMW", [], []))

    def test_empty_list1(self):
        """It should return True if the first list is empty and the second is not"""
        self.assertTrue(is_in_one("BMW", [], ["BMW", "Audi"]))

    def test_empty_list2(self):
        """It should return True if the second list is empty and the first is not"""
        self.assertTrue(is_in_one("BMW", ["BMW", "Cadillac"], []))
