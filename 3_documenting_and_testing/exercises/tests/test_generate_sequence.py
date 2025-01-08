#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the generate_sequence function.

Test categories:
    - Standard cases: Positive integers for generating sequences.
    - Edge cases: Minimal input.
    - Defensive tests: Non-integer or negative inputs assertions.
"""

import unittest

from ..generate_sequence import generate_sequence


class TestGenerateSequence(unittest.TestCase):
    """Test generate_sequence function"""

    # Standard Cases
    def test_generate_sequence_length_5(self):
        """Should generate a list of 5 integers"""
        self.assertEqual(generate_sequence(5), [0, 1, 2, 3, 4])

    def test_generate_sequence_length_3(self):
        """Should generate a list of 3 integers"""
        self.assertEqual(generate_sequence(3), [0, 1, 2])

    # Edge Cases
    def test_minimal_input(self):
        """It should return an empty list for minimal input 0"""
        self.assertEqual(generate_sequence(0), [])

    # Defensive Tests
    def test_invalid_type_string(self):
        """Should raise an AssertionError for string input"""
        with self.assertRaises(AssertionError):
            generate_sequence("5")

    def test_invalid_type_float(self):
        """Should raise an AssertionError for float input"""
        with self.assertRaises(AssertionError):
            generate_sequence(5.5)

    def test_negative_input(self):
        """Should raise an AssertionError for negative input"""
        with self.assertRaises(AssertionError):
            generate_sequence(-5)
