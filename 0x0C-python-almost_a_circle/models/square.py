#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class.'''

    def __init__(self, size, x=0, y=0, id=0):
        '''Constructor'''
        super().__init__(size, size,x ,y, id)

    def __str__(self):
        '''Returns srting info about this triange.'''
        return "[{}] ({}) {}/{} - {}/{}".\
               format(type(self).__name__, self.id, self.x, self.y, self.width)