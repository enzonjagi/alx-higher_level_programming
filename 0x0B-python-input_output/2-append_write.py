#!/usr/bin/python3
"""
This module contains a function that
Opens a text file,
Appends data to it
"""


def append_write(filename="", text=""):
    """
    Executing the purpose of this module:
    Append to a text file(add at the end)
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        append_data = f.write(text)
    return append_data
