#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting and merging two lists.

Module contents:
    - sort_and_merge: Moves elements from one list to another, keeping the merged list sorted.
"""


def sort_and_merge(a: list, b: list) -> list:
    """Sorts and merges two lists by moving all elements from `a` to `b` in sorted order.

    Parameters:
        a (list): The source list.
        b (list): The destination list, where sorted elements from `a` will be appended.

    Returns -> list: The merged list `b`, containing all elements from `a` and
    its original elements, sorted.

    Raises:
        AssertionError: If `a` or `b` is not a list.

    Examples:
    >>> sort_and_merge([3, 1, 2], [])
    [1, 2, 3]
    >>> sort_and_merge([5], [0, 4])
    [0, 4, 5]
    >>> sort_and_merge([], [10, 20])
    [10, 20]
    """
    assert isinstance(a, list) and isinstance(b, list), "Both inputs must be lists"
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
