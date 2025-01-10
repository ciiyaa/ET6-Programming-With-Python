#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Use test cases, the docstring, and labels to describe this solution."""


def fibonacci(n: int, memo: dict = {}) -> int:
    """Computes the nth Fibonacci number using memoization.

    base case 1:
        n == 0  -> return 0

    base case 2:
        n == 1  -> return 1

    base case 3:
        if n in memo  -> return memo[n]

    recursive case:
        fibonacci(n)  -> fibonacci(n-1) + fibonacci(n-2)

    """
    if n == 0:  # base case 1
        return 0

    if n == 1:  # base case 2
        return 1

    if n in memo:  # base case 3
        return memo[n]

    # recursive case
    left_recursion = fibonacci(n - 1, memo)
    right_recursion = fibonacci(n - 2, memo)
    memo[n] = left_recursion + right_recursion

    return memo[n]


# --- --- --- test cases --- --- ---

# write some test cases!
print(fibonacci(0), "should be", 0)
print(fibonacci(1), "should be", 1)
print(fibonacci(2), "should be", 1)
print(fibonacci(3), "should be", 2)
print(fibonacci(10), "should be", 55)
print(fibonacci(20), "should be", 6765)
