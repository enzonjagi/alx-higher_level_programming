#!/usr/bin/python3
'''Square module with size check'''


class Square:
    '''An empty Class'''

    def __init__(self, size=0):
        '''A initialization function'''

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
