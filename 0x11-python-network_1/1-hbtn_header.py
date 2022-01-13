#!/usr/bin/python3
'''
Pythos script that sends a request
 and displays value of the X-Request-Id header variable
'''
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as resp:
    r = resp.info()

print(r.get('X-Request-Id'))
