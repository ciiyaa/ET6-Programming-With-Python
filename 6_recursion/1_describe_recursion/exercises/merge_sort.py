#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Use test cases, the docstring, and labels to describe this solution."""


def merge_sort(numbers: list) -> list:
    """
    Sorts a list of numbers using the merge sort algorithm.

    base case:
        If the list has one or no elements, it is already sorted.
    recursive case:
        Split the list into two halves, sort each half, and merge the sorted halves.
    """
    if len(numbers) <= 1:  # base case
        return numbers  # already sorted

    mid = len(numbers) // 2
    # recursively sort the left half
    left_half = merge_sort(numbers[:mid])
    # recursively sort the right half
    right_half = merge_sort(numbers[mid:])

    return merge(left_half, right_half)


# you do not need to label this helper function
def merge(left, right):
    sorted_numbersay = []
    while left and right:
        if left[0] < right[0]:
            sorted_numbersay.append(left.pop(0))
        else:
            sorted_numbersay.append(right.pop(0))
    sorted_numbersay.extend(left or right)
    return sorted_numbersay


# --- --- --- test cases --- --- ---

print(merge_sort([]), "should be", [])
print(merge_sort([1]), "should be", [1])
print(merge_sort([3, 2, 1]), "should be", [1, 2, 3])
print(merge_sort([5, 3, 8, 4, 2]), "should be", [2, 3, 4, 5, 8])
print(merge_sort([10, -1, 2, 5, 0, 6]), "should be", [-1, 0, 2, 5, 6, 10])
