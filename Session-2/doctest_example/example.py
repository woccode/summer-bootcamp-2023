# example.py


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
    return a - b


def divide(a, b):
    return a / b


def example_set():
    return {"a", "b", "c", "d"}


if __name__ == "__main__":
    import doctest

    doctest.testmod()
