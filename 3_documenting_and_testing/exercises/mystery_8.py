#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for filtering elements containing a substring.

Module contents:
    - filter_elements_containing_substring: Filters elements containing a specific
    substring from a list.
"""


def filter_elements_containing_substring(a: list[str], b: str) -> list[str]:
    """Filters elements containing a specific substring from a list.

    Parameters:
        a (list of str): A list of strings to filter.
        b (str): The substring to look for.

    Returns -> list: A list of elements containing the substring.

    Examples:
    >>> filter_elements_containing_substring(["apple", "banana", "cherry"], "a")
    ['apple', 'banana']

    >>> filter_elements_containing_substring(["apple"], "v")
    []
    """
    assert isinstance(a, list) and all(
        isinstance(i, str) for i in a
    ), "Input must be a list of strings"
    assert isinstance(b, str), "Substring must be a string"
    c = []
    while a:
        if b in a[0]:
            c.append(a[0])
        a = a[1:]
    return c
