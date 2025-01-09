"""Is in

Write a function that takes in a string and two lists of strings.
It will return true if the item is in _at least one_ of the lists.

"""


def is_in(item: str, list1: list, list2: list) -> bool:
    """The function returns True if the item is in at least one of the lists.

    Parameters:
        item (str): the item to check
        list1 (list): the first list of strings
        list2 (list): the second list of strings

    Returns -> bool: True if the item is in at least one of the lists, False otherwise

    Raises:
        AssertionError: if the item is not a string
        AssertionError: if list1 is not a list
        AssertionError: if list2 is not a list

    >>> is_in("BMW", ["BMW", "Toyota"], ["Ford", "Cadillac"])
    True

    >>> is_in("Toyota", ["BMW", "Toyota"], ["Toyota", "Ford"])
    True

    >>> is_in("orange", ["BMW", "Toyota"], ["Ford", "Cadillac"])
    False
    """
    assert isinstance(item, str), "item must be a string"
    assert isinstance(list1, list), "list1 must be a list"
    assert isinstance(list2, list), "list2 must be a list"

    return item in list1 or item in list2
