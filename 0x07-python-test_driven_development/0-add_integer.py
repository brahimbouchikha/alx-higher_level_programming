#!/usr/bin/python3
"""Module for add_integer methode."""


def add_integer(a, b=98):
    """ Add 2 integers


    Args:
        a: the first integer.
        b: the seconde integer, default 98.
    
    Raises:
        TypeError: if a or b are not int, float

    Rerurns:
        The sum of the tow integers.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a_as_int = int(a)
    b_as_int = int(b)
    return a_as_int + b_as_int

if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integers.txt")
