#!/usr/bin/python3
"""
Python script that sends a request
and displays value of the X-Request-Id header variable
"""

import urllib
import sys


with urllib.request.urlopen(sys.argv[1]) as resp:
    '''store response in a variable'''
    r = resp.info()

if __name__ == '__main__':
    print(r.get('X-Request-Id'))
