#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for sorting and merging two lists.

Module contents:
    - sort_and_merge: Moves elements from one list to another, keeping the merged list sorted.
"""


def sort_and_merge(a, b):
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
