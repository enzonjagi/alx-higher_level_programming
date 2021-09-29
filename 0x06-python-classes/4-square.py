#!/usr/bin/python3
'''Square module with size check'''


class Square:
    '''An empty Class'''

    def __init__(self, size=0):
        '''A initialization function'''
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def area(self):
        '''Returns Area of square'''
        return(self.__size * self.__size)
