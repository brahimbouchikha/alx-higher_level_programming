#!/usr/bin/python3
"""Square Module"""


class Square:
    """Define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constractor.

        Args:
            size: size of a side of square

        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0 or position is not a tuple of 2
            positive integers
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple) or \
                len(position) != 2 or \
                not isinstance(position[0], int) or \
                not isinstance(position[1], int) or \
                position[0] < 0 or \
                position[1] < 0:
            raise ValueError("position must be a tuple of 2 positiv integers")
        self.__position = position

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

    @property
    def position(self):
        """Property for the position of the square
        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        """
        return self.position

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise ValueError("position must be a tuple of 2 positiv integers")
        self.__position = position

    def area(self):
        """returns the current square area."""

        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character"""

        if self.size == 0:
            print()
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(self.size):
            for k in range(self.__position[0]):
                    print(" ", end="")
            for j in range(self.size):
                print("#", end='')
            print()
