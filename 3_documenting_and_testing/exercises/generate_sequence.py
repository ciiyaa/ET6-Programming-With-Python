#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating a sequence of integers starting from 0 up to a specified length.

Module contents:
    - generate_sequence: Generates a list of integers starting from 0 up to the specified
    input.
"""


def generate_sequence(a: int) -> list:
    """Generates a list of integers starting from 0 to the specified length.

    Parameters:
        a (int): The length of the list to generate.

    Returns:
        list: A list of integers starting from 0 up to a-1.

    Raises:
        AssertionError: If input is not a non-negative integer.

    Examples:
    >>> generate_sequence(5)
    [0, 1, 2, 3, 4]
    >>> generate_sequence(0)
    []
    """
    assert isinstance(a, int) and a >= 0, "Input must be a non-negative integer"

    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b
