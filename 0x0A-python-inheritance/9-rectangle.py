#!/usr/bin/python3
"""
This module series contains a class and some inheritance
"""


class BaseGeometry:
    """
    A class containing a number of methods:
    area() throws an Exception
    integer_validator() validates that a value is of type int
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an int
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must greater than 0".format(name))
        else:
            return value


class Rectangle(BaseGeometry):
    """
    Class that is a subclass if the BaseGeometry class
    """

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle]" + " {}/{}".format(self.__width, self.__height)
