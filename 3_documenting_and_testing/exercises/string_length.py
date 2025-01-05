#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting characters in a string.

Module contents:
    - mystery_2: Accepts a string and returns its length.
"""
def string_length(a):
    """Accepts a string and returns its length, non-alphanumeric
    numbers, and spaces and valid. Returns NONE if string is empty

    Parameters:
        a: str, a string to find the length of

    Returns -> int: length of characters

    Raises:
        AssertionError: If input is not a string

    Examples:
    >>> string_length("abcd")
    4
    >>> string_length("abc12@2")
    7
    >>> string_length("a b c")
    5
    """
    assert isinstance(a,str), "Input must be a string"
    if len(a) == 0:
        return None

    return len(a)
