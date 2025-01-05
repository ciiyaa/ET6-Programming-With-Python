#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting characters in a string or a list.

Module contents:
    - count_characters: Accepts a string or list and returns its length.
"""

def count_characters(a):
    """Accepts a string or list and returns its length. If input is empty,
    returns None.

    Parameters:
        a (str | list): A string or list to find the length of.

    Returns:
        int | None: The length of the input, or None if it is empty.

    Raises:
        AssertionError: If input is not a string or list.

    Examples:
    >>> count_characters("abcd")
    4
    >>> count_characters(["a", "b", "c", 1, 2])
    5
    """
    assert isinstance(a, (str, list)), "Input must be a string or a list"

    if len(a) == 0:
        return None

    return len(a)
