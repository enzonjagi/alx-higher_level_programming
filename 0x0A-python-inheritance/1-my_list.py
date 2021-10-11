#!/usr/bin/python3
"""
Module contains a class MyList that inherits from list
"""


class MyList(list):
    """
    A class MyList that inherits from list
    """

    def print_sorted(self):
        """
        Public instance method:
        def print_sorted(self):
        that prints the list, but sorted (ascending sort)
        You can assume that all the elements of the list
        will be of type int
        """

        new_list = self[:]
        for i in range(len(new_list) - 1):
            if new_list[i] > new_list[i + 1]:
                temp = new_list[i + 1]
                new_list[i + 1] = new_list[i]
                new_list[i] = temp
        print(new_list)
