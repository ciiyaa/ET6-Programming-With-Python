#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the mystery_6 function.

Test categories:
    - Standard cases: Generate sequences of various lengths starting from different values.
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

    def test_generate_negative_start(self):
        """Should generate a sequence starting from a negative value"""
        self.assertEqual(generate_incremental_sequence(2, -1), [-1, 0])

    def test_minimal_input(self):
        """"""
        self.assertEqual(generate_incremental_sequence(0, 0), [])
