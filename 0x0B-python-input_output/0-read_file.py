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

    with open(filename, mode='r', encoding='utf-8') as f:
        read_data = f.read()
        for line in f:
            print(line)
    return read_data
