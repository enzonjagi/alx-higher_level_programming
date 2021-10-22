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
