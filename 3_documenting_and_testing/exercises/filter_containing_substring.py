#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for filtering a list of strings based on the presence of a specified substring.

Module contents:
    - filter_containing_substring: Filters a list of strings, returning only those that
    contain a given substring.
"""


def filter_containing_substring(a: list[str], b: str) -> list[str]:
    """Filters a list of strings, returning only those that contain a specified substring.

    Parameters:
        strings (list[str]): List of strings to filter.
        substring (str): Substring to search for in each string.

    Returns -> list[str]: A list of strings from the input list that contain the substring.

    Raises:
        AssertionError: If inputs are not of the expected types.

    Examples:
    >>> filter_containing_substring(["apple", "banana", "cherry"], "ana")
    ['banana']
    >>> filter_containing_substring(["dog", "cat", "rabbit"], "cat")
    ['cat']
    >>> filter_containing_substring(["one", "two", "three"], "")
    ['one', 'two', 'three']
    """
    assert isinstance(a, list) and all(
        isinstance(s, str) for s in a
    ), "First argument must be a list of strings"
    assert isinstance(b, str), "Second argument must be a string"
    c = []
    for d in a:
        if b in d:
            c.append(d)
    return c
