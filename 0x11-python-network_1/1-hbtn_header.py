#!/usr/bin/python3
"""Takes URL sends request and displays value of X-Request-Id"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as resp:
    '''store response in a variable'''
    print(resp.info().get('X-Request-Id'))
