def two_numbers(a,b):
    """
    Add two numbers and return the result

    Parameters:
        a: int, the first number to add
        b: int, the second number to add
    
    Returns -> int: the sum of a and b
    
    Raises:
        TypeError: if the arguments are not integers

    Examples:
    >>> add_two_numbers(1, 2)
    3
    >>> add_two_numbers(-1, -2)
    -3
    >>> add_two_numbers(0, 5)
    5
    """
    assert isinstance(a, int), "First input must be an integer"
    assert isinstance(b, int), "Second input must be an integer"
    
    return a + b
