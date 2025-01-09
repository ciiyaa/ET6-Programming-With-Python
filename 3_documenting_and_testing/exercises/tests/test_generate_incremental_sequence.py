#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the mystery_6 function.

Test categories:
    - Standard cases: Generate sequences of various lengths starting from different values.
    - Edge cases: Zero-length sequences, negative starting values, and large inputs.
    - Defensive tests: Non-integer inputs and invalid values.
"""

import unittest

from ..generate_incremental_sequence import generate_incremental_sequence


class TestGenerateIncrementalSequence(unittest.TestCase):
    """Test the generate_incremental_sequence function"""

    # Standard Cases
    def test_generate_sequence(self):
        """Should generate a sequence starting from `b` with `a` elements"""
        self.assertEqual(generate_incremental_sequence(3, 5), [5, 6, 7])

    def test_generate_single_element(self):
        """Should generate a single-element sequence"""
        self.assertEqual(generate_incremental_sequence(1, 0), [0])

    # Edge Cases
    def test_zero_length_sequence(self):
        """Should return an empty list when `a` is 0"""
        self.assertEqual(generate_incremental_sequence(0, 5), [])

    def test_generate_negative_start(self):
        """Should generate a sequence starting from a negative value"""
        self.assertEqual(generate_incremental_sequence(2, -1), [-1, 0])

    def test_large_input(self):
        """Should handle large values of `a`"""
        self.assertEqual(generate_incremental_sequence(5, 0), [0, 1, 2, 3, 4])

    def test_minimal_input(self):
        """Should return an empty list for minimal inputs"""
        self.assertEqual(generate_incremental_sequence(0, 0), [])

    # Defensive Tests
    def test_invalid_type_a_not_integer(self):
        """Should raise an AssertionError if `a` is not an integer"""
        with self.assertRaises(AssertionError):
            generate_incremental_sequence("string", 0)

    def test_invalid_type_b_not_integer(self):
        """Should raise an AssertionError if `b` is not an integer"""
        with self.assertRaises(AssertionError):
            generate_incremental_sequence(5, "string")

    def test_negative_a(self):
        """Should raise an AssertionError if `a` is negative"""
        with self.assertRaises(AssertionError):
            generate_incremental_sequence(-1, 0)
