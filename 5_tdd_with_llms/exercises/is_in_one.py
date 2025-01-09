"""Is in one

Write a function that takes in a string and two lists of strings.
It will return true if the item is in _only one_ of the lists.

"""


def is_in_one(item: str, list1: list, list2: list) -> bool:
    """The function returns True if the item is in only one of the lists.

    Parameters:
        item (str): the item to check
        list1 (list): the first list of strings
        list2 (list): the second list of strings

    Returns:
        bool -> True if the item is in only one of the lists, False otherwise

    Raises:
        AssertionError: if the item is not a string
        AssertionError: if list1 is not a list
        AssertionError: if list2 is not a list
    >>> is_in_one("Toyota", ["Toyota", "Ford"], ["Cadillac", "Audi"])
    True

    >>> is_in_one("Ford", ["Toyota", "Ford"], ["Ford", "Cadillac"])
    False

    >>> is_in_one("BMW", ["Toyota", "Ford"], ["Cadillac", "Audi"])
    False
    """
    assert isinstance(item, str), "item must be a string"
    assert isinstance(list1, list), "list1 must be a list"
    assert isinstance(list2, list), "list2 must be a list"

    return (item in list1) != (item in list2)
