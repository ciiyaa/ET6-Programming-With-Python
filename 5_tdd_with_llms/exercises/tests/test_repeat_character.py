#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for repeat_character function.
Contains tests to ensure correct functionality of the implementation.

Test categories:
    - Standard cases: normal inputs

"""

import unittest
from ..repeat_character import repeat_character


class TestRepeatCharacter(unittest.TestCase):
    """Test the repeat_character function"""

    # Standard Cases
    def test_repeat_character_normal_case(self):
        """It should repeat the character 'l' 3 times in 'hello'"""
        self.assertEqual(repeat_character("hello", "l", 3), "hellllllo")

    def test_repeat_character_not_in_text(self):
        """It should return the original string if the character is not in the text"""
        self.assertEqual(repeat_character("hello", "x", 5), "hello")
