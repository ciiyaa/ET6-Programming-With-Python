#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the generate_sequence function.

Test categories:
    - Standard cases: Positive integers for generating sequences.
    - Edge cases: Minimal input.
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
