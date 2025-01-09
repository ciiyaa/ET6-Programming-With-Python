"""Is in Both

Write a function that takes in a string and two lists of strings.
It will return true if the item is in _both_ of the lists.

"""


def is_in_both(item: str, list1: list, list2: list) -> bool:
    """The function returns True if the item is in both lists.

    Parameters:
        item (str): the item to check
        list1 (list): the first list of strings
        list2 (list): the second list of strings

    Returns:
        bool: True if the item is in both lists, False otherwise


    """

    assert isinstance(item, str), "item must be a string"
    assert isinstance(list1, list), "list1 must be a list"
    assert isinstance(list2, list), "list2 must be a list"

    return item in list1 and item in list2


print(is_in_both("Banana", ["Banana", "Organe"], ["Cheery", "Banana"]))
