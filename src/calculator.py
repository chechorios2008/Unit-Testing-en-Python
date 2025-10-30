def sum(a, b):
    """
    >>> sum(5, 7)
    11
    """
    return a + b


def subtract(a, b):
    return a - b


def multply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("La división por cero no esta permitida.")
    return a / b