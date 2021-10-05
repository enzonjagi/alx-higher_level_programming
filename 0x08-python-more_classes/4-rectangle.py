#!/usr/bin/python3
"""
A real rectangle module
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

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if (self.width == 0) or (self.height == 0):
            return (0)
        return 2 * (self.width + self.height)

    def print(self):
        if (self.width == 0) or (self.height == 0):
            return("")
        else:
            for i in range(self.width):
                for j in range(self.height):
                    print("#", end="")
                print()

    def __str__(self):
        if (self.width == 0) or (self.height == 0):
            return("")
        else:
            for i in range(self.height):
                for j in range(self.width):
                    print("#", end="")
                print()
            return ("")

    def __repr__(self):
        return ("Rectangle(" + 
            str(self.width) + ", " + 
            str(self.height) + ")")
