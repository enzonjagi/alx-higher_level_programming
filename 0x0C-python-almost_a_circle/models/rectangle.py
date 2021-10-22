#!/usr/bin/python3
"""this module contains a rectangle class,
the class inherits from the Base class.
"""

from base import Base


class Rectangle(Base):
    """A rectangle class
    The class has the following private instance attributes:
    width, height, x, and y:
    each with its own setter and getter
    A constructor class calling the supper class with id,
    and assigns the private attirbutes respectively
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation
        Instantiate class attributes and call super() class,
        with id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width Getter
        Width getter that gets the private instance attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter
        Width setter
        sets the private instance attribute
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height getter
        gets the private instance attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter
        sets the private instance attribute
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter
        gets the private instance attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter
        sets the private instance attribute
        """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter
        gets the private instance attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        sets the private instance attribute
        """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """area method for a rectangle instance
        returns the area of a Rectangle Instance
        """
        return (self.__width * self.__height)

    def display(self):
        """prints the # character
        prints in stdout the Rectangle instance with the character #
        """
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))

    def __str__(self):
        """string method
        This overrrides the default string method
        """
        return ("[Rectangle] (" +
                str(self.id) + ") " +
                str(self.__x) + "/" +
                str(self.__y) + " - " +
                str(self.__width) + "/" +
                str(self.__height))

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            elif "width" in kwargs:
                self.width = kwargs["width"]
            elif "height" in kwargs:
                self.height = kwargs["height"]
            elif "x" in kwargs:
                self.x = kwargs["x"]
            elif "y" in kwargs:
                self.width = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation
        this function makes a dictionary representation of
        a Rectangle instance
        """
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y

        return dic


if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()
