#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for comparing two numbers and returning a the smallest one, or their sum if equal.

Module contents:
    - two_numbers_compare: Compares two numbers and returns one of them, or
    the sum, based on the conditions.
"""


def two_numbers_compare(a, b):
    """Compares two numbers and returns:
        - the smaller number if they are not equal, or
        - their sum if they are equal.

    Parameters:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: The smaller number, or their sum if they are equal.

    Raises:
        AssertionError: If inputs are not int or float.

    Examples:
    >>> mystery_3(3, 5)
    3
    >>> mystery_3(10, 10)
    20
    >>> mystery_3(4.5, 2.3)
    2.3
    """
    assert isinstance(a, (int, float)) and isinstance(
        b, (int, float)
    ), "Inputs must be integers or floats"

    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
