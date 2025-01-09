#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for repeat_character function.
Contains tests to ensure correct functionality of the implementation.

Test categories:
    - Standard cases: normal inputs
    - Edge cases: empty inputs
"""

import unittest
from ..repeat_character import repeat_character


class TestRepeatCharacter(unittest.TestCase):
    """Test the repeat_character function"""

    # Standard Tests
    def test_repeat_character_normal_case(self):
        """It should repeat the character 'l' 3 times in 'hello'"""
        self.assertEqual(repeat_character("hello", "l", 3), "hellllllo")

    def test_repeat_character_not_in_text(self):
        """It should return the original string if the character is not in the text"""
        self.assertEqual(repeat_character("hello", "x", 5), "hello")

    # Edge Tests
    def test_empty_string(self):
        """It should return an empty string if the input text is empty"""
        self.assertEqual(repeat_character("", "a", 3), "")

    def test_zero_repetitions(self):
        """It should return the original string if repetitions is zero"""
        self.assertEqual(repeat_character("hello", "l", 0), "hello")

    def test_character_at_start(self):
        """It should repeat the character 'h' 2 times in 'hello'"""
        self.assertEqual(repeat_character("hello", "h", 2), "hhello")

    def test_character_at_end(self):
        """It should repeat the character 'o' 4 times in 'hello'"""
        self.assertEqual(repeat_character("hello", "o", 4), "helloooo")
