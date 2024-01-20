#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_value("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_value("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x of this triangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_value("x", value, True)
        self.__x = value

    @property
    def y(self):
        '''y of this triangle?.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_value("y", value, True)
        self.__y = value

    def validate_value(self, name, value, under=True):
        '''Methode to validate the value.'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not under and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif under and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        '''Methode that calcule the area.'''
        return self.__width * self.__height

    def display(self):
        '''Print in stdout the rectangle with #.'''
        print(("#" * self.__width + "\n") * self.__height, end="")

    def __str__(self):
        '''Returns srting info about this triange'''
        return "[{}] ({}) {}/{} - {}/{}".\
               format(type(self).__name__, self.id, self.x, self.y, self.width,
                      self.height)
