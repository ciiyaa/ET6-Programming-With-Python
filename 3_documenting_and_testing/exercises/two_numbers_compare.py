#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for comparing two numbers and returning a the smallest one, or their sum if equal.

Module contents:
    - two_numbers_compare: Compares two numbers and returns one of them, or
    the sum, based on the conditions.
"""


def two_numbers_compare(a: int, b: int) -> int:
    """Compares two numbers and returns:
        - the smaller number if they are not equal, or
        - their sum if they are equal.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns -> int: The smaller number, or their sum if they are equal.

    Raises:
        AssertionError: If inputs are not int.

    Examples:
    >>> two_numbers_compare(3, 5)
    3
    >>> two_numbers_compare(10, 10)
    20
    >>> two_numbers_compare(4, 2)
    2
    """
    assert isinstance(a, (int)) and isinstance(b, (int)), "Inputs must be integers"

    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
