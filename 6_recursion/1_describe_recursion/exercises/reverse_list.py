#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Use test cases, the docstring, and labels to describe this solution."""


def reverse_list(to_reverse: list) -> list:
    """
    Reverses the items from one list into a new list without modifying the original.

    base case:
        If the list is empty, return an empty list.
    recursive case:
        Return the reverse of the rest of the list plus the first element.
    """
    if len(to_reverse) == 0:  # base case
        return []  # return an empty list

    # recursive case
    return reverse_list(to_reverse[1:]) + [to_reverse[0]]


# --- call the traced function ---

print(reverse_list([]), "should be", [])
print(reverse_list([1, 2, 3]), "should be", [3, 2, 1])
print(reverse_list([1, 2, 1]), "should be", [1, 2, 1])
print(reverse_list(["", False, None, 0]), "should be", [0, None, False, ""])
