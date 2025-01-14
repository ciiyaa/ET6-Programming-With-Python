#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for adding two numbers.

Module contents:
    - two_number_addition: Computes and returns the sum of two integers.
"""


def two_numbers_addition(a: int, b: int) -> int:
    """Computes and returns the sum of two integers.

    Parameters:
        a (int): The first number to add
        b (int): The second number to add

    Returns -> int: the sum of a and b

    Raises:
        AssertionError: If either argument is not an integer.

    Examples:
    >>> two_numbers_addition(1, 2)
    3
    >>> two_numbers_addition(-1, -2)
    -3
    >>> two_numbers_addition(0, 5)
    5
    """
    assert isinstance(a, int), "First input must be an integer"
    assert isinstance(b, int), "Second input must be an integer"

    return a + b
