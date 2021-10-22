#!/usr/bin/python3
"""Square module
This module contains:
A Square Class that inherits from Rectangle
a Square is a Rectangle with the same width and height
"""

from rectangle import Rectangle


class Square(Rectangle):
    """The Square Class
    This Class inherits from the Rectangle Class
    and class super() on all its parent's attributes
    """

    def __init__(self, size, width, height, x=0, y=0, id=None):
        """Instantiation
        This happens via calling super() on the Parent Class
        """
        super().__init__(width, height, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        """The size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """string method
        This overrrides the default string method
        """
        return ("[Square] (" +
                str(self.id) + ") " +
                str(self.__x) + "/" +
                str(self.__y) + " - " +
                str(self.__width))

    def update(self, *args, **kwargs):
        """The args and kwargs version of the Square"""
        """Assigns arguments to attributes
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 3:
                    self.x = j
                elif i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            elif "size" in kwargs:
                self.size = kwargs["size"]
            elif "x" in kwargs:
                self.x = kwargs["x"]
            elif "y" in kwargs:
                self.width = kwargs["y"]

    def to_dictionary(self):
        """Dictionary representation of the square"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y

        return dic
