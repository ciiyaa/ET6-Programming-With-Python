"""Sum Evens and Odds

Write a function that takes a list of numbers
and returns a dictionary with sums of the even and odd numbers in the list.

"""


def sum_evens_and_odds(numbers: list) -> dict:
    """Returns a dictionary with the sums of even and odd numbers.

    Parameters:
        numbers (list): a list of numbers

    Returns -> dict: a dictionary with keys 'even' and 'odd' containing the sums of even and odd numbers

    Raises:
        AssertionError: if the input is not a list of numbers

    >>> sum_evens_and_odds([1, 2, 3, 4, 5])
    {'even': 6, 'odd': 9}
    >>> sum_evens_and_odds([0, 1, 2, 3, 4, 5, 6])
    {'even': 12, 'odd': 9}
    >>> sum_evens_and_odds([])
    {'even': 0, 'odd': 0}
    """

    evens = sum(n for n in numbers if n % 2 == 0)
    odds = sum(n for n in numbers if n % 2 != 0)

    return {"even": evens, "odd": odds}
