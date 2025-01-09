"""Sort Numbers

Write a function that takes in a list of numbers
It will return a new list with the same numbers from lowest to highets
-> this function does not have side effects

"""


def sort_numbers(numbers: list) -> list:
    """Returns a new list with numbers sorted from lowest to highest.

    Parameters:
        numbers (list): a list of numbers

    Returns -> list: a new list with the numbers sorted in ascending order

    Raises:
        AssertionError: if the input is not a list of numbers

    >>> sort_numbers([5, 2, 9, 1])
    [1, 2, 5, 9]
    >>> sort_numbers([3.5, 2.1, -1, 0])
    [-1, 0, 2.1, 3.5]
    >>> sort_numbers([])
    []
    """

    assert isinstance(numbers, list), "numbers must be a list"
    assert all(
        isinstance(n, (int, float)) for n in numbers
    ), "all elements must be numbers"

    return sorted(numbers)
