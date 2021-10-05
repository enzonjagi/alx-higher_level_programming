#!/usr/bin/python3
"""
A real rectangle module
"""


class Rectangle:
    """
    A class in python3 that is
    Inclusive of the area and perimeter
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiate"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                    print("{}".format(self.print_symbol), end="")
                print()

    def __str__(self):
        if (self.width == 0) or (self.height == 0):
            return("")
        else:
            for i in range(self.height):
                for j in range(self.width):
                    print("{}".format(self.print_symbol), end="")
                print()
            return ("")

    def __repr__(self):
        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) and isinstance(rect_2, Rectangle):
            if(rect_1.area() >= rect_2.area()):
                return rect_1
            else:
                return rect_2
        elif not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
