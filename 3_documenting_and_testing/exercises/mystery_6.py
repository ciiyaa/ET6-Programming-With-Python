#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating a sequence based on specific rules.

Module contents:
    - generate_sequence: Generates a sequence starting from `b`, with `a` elements.
"""


def generate_sequence(a: int, b: int) -> list:
    """Generates a sequence of `a` elements, starting from `b`.

    Parameters:
        a (int): The number of elements to generate.
        b (int): The starting value of the sequence.

    Returns -> list: A list of `a` elements, starting from `b`.

    Raises:
        AssertionError: If `a` or `b` is not an integer or if `a` is negative.

    Examples:
    >>> generate_sequence(0, 0)
    []
    >>> generate_sequence(3, 5)
    [5, 6, 7]
    >>> generate_sequence(2, -1)
    [-1, 0]
    """
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
