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
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = width

        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.height = height

        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.x = x

        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
        Width getter
        gets the private instance attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Width setter
        sets the private instance attribute
        '''
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        else:
            self.__width = value

    @property
    def height(self):
        '''
        Height getter
        gets the private instance attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Height setter
        sets the private instance attribute
        '''
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        else:
            self.__height = value

    @property
    def x(self):
        '''
        x getter
        gets the private instance attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        x setter
        sets the private instance attribute
        '''
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        else:
            self.__x = value

    @property
    def y(self):
        '''
        y getter
        gets the private instance attribute
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        y setter
        sets the private instance attribute
        '''
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        else:
            self.__y = value
