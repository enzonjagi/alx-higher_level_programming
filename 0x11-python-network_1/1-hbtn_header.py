#!/usr/bin/python3
"""Python script that displays value of X-Request-Id header variable"""

import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as resp:
    '''store response in a variable'''
    r = resp.info()

print(r.get('X-Request-Id'))
