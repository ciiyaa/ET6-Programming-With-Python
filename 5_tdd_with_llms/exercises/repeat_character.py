"""Repeat Character

Write a function that takes in a string, a single character, and a number.
The function returns a string with each occurrence of the character repeated n times.

"""


def repeat_character(text: str, char_to_repeat: str, repetitions: int) -> str:
    """The function returns a string with each occurrence of the character repeated n times.

    Parameters:
        text (str): the input string
        char_to_repeat (str): the character to repeat
        repetitions (int): number of times to repeat the character

    Returns -> str: the modified string with the character repeated

    Raises:
        AssertionError: if the text is not a string
        AssertionError: if char_to_repeat is not a single character
        AssertionError: if repetitions is not a non-negative integer

    >>> repeat_character('hello', 'l', 3)
    'hellllllo'
    >>> repeat_character('world', 'o', 2)
    'woorld'
    >>> repeat_character('test', 'x', 5)
    'test'
    """

    assert isinstance(text, str), "text must be a string"
    assert (
        isinstance(char_to_repeat, str) and len(char_to_repeat) == 1
    ), "char_to_repeat must be a single character"
    assert (
        isinstance(repetitions, int) and repetitions >= 0
    ), "repetitions must be a non-negative integer"

    result = ""
    for char in text:
        if char == char_to_repeat:
            result += char * repetitions
        else:
            result += char
    return result
