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
        self.__width = value
