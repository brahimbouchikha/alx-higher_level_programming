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

    @property
    def size(self):
        """ Property for the size of this square.
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area."""

        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character"""

        if self.size == 0:
            print()
            return
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='')
            print()
