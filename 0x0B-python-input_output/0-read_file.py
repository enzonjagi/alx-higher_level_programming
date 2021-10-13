#!/usr/bin/python3
"""
This module contains a function that
opens a text file
Reads the text file,
Prints it out to stdout
"""


def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line)
