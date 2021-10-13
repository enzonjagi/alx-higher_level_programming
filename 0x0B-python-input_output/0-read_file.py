#!/usr/bin/python3
"""
This module contains a function that
opens a text file
Reads the text file,
Prints it out to stdout
"""


def read_file(filename=""):
    """
    Executing the purpose of this module
    """

    with open(filename, mode='r', encoding='UTF8') as f:
        data = f.read()
    print(data)


if __name__ == '__main__':
    read_file("file_2")
