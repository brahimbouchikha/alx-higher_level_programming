#!/usr/bin/python3
"""Square Module"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Constractor.

        Args:
            size: size of a side of square

        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """returns the current square area."""

        return self.__size ** 2
