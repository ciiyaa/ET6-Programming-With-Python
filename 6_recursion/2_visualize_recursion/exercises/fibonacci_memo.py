#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Visualizing fibonacci_memo

To visualize implementation,
- use your VSCode debugger
- copy-paste the code into PythonTutor

To visualize strategy:
- run the script and read the recursion trace
- comment @trace_recursion and debug the function
or copy the function into one of these sites:
- https://www.recursionvisualizer.com
- https://recursion.vercel.app
- https://recursion-visualizer.vercel.app
- https://visualgo.net/en/recursion

"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from trace_recursion import trace_recursion


@trace_recursion
def fibonacci_memo(n: int, memo: dict = {}) -> int:
    """
    Computes the nth Fibonacci number using memoization.

    base case 1:
        If n is 0, return 0.
    base case 2:
        If n is 1, return 1.
    base case 3:
        If n is already computed in memo, return memo[n].
    recursive case:
        Compute fibonacci(n-1) and fibonacci(n-2), store their sum in memo, and return it.
    """
    if n == 0:  # base case 1
        return 0

    if n == 1:  # base case 2
        return 1

    if n in memo:  # base case 3
        return memo[n]

    # recursive case
    left_break_down = n - 1
    right_break_down = n - 2

    left_recursion = fibonacci_memo(left_break_down, memo)
    right_recursion = fibonacci_memo(right_break_down, memo)

    build_up = left_recursion + right_recursion
    memo[n] = build_up

    return memo[n]


# --- call the traced function ---

print(fibonacci_memo(0), "should be", 0)
print(fibonacci_memo(1), "should be", 1)
print(fibonacci_memo(2), "should be", 1)
print(fibonacci_memo(4), "should be", 3)
print(fibonacci_memo(6), "should be", 8)
print(fibonacci_memo(8), "should be", 21)
