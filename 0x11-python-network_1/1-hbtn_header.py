#!/usr/bin/python3
"""sends request and displays value of X-Request-Id"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as resp:
    print(resp.info().get('X-Request-Id'))
