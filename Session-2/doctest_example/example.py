# example.py
"""
Usage Examples:
>>> add(100, 1)
101
"""

def add(a, b):
    """
    Adds two numbers

    Usage examples:
    >>> add(5, 8)
    13
    >>> add(19, 3)
    22
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers

    Usage examples:
    >>> subtract(5, 8)
    -3
    >>> subtract(19, 3)
    16
    """
    return a - b


def divide(a, b):
    return a / b


def example_set():
    return {"a", "b", "c", "d"}


if __name__ == "__main__":
    import doctest

    doctest.testmod()
