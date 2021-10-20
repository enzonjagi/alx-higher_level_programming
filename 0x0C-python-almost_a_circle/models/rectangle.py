#!/usr/bin/python3
'''
this module contains a rectangle class,
that inherits from Base
'''

from base import Base


class Rectangle(Base):
    '''
    A rectangle class that has the following private instance attributes:
    width, height, x, and y:
    each with its own setter and getter

    A constructor class calling the supper class with id,
    and assigns the private attirbutes respectively
    '''

    def __init__(self, width, height, x, y, id=None):
        '''
        Instantiate class attributes and call super() class,
        with id
        '''
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Width getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Width setter
        '''
        self.__width = value

    @property
    def height(self):
        '''
        Height getter
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Height setter
        '''
        self.__height = value

    @property
    def x(self):
        '''
        x getter
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        x setter
        '''
        self.__x = value

    @property
    def y(self):
        '''
        y getter
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        y setter
        '''
        self.__y = value
