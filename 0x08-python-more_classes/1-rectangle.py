#!/usr/bin/python3
"""
The Real definition of a rectangle
Just a module; check class for more info
"""


class Rectangle:
    """
    A class in python3 that is
    Inclusive of the area and perimeter
    """

    def __init__(self, width=0, height=0):
        """Instantiate"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width__)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width__ = value

    @property
    def height(self):
        return (self.__height__)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height__ = value


if __name__ == '__main__':
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
