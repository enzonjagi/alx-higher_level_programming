#!/usr/bin/python3
"""Post an email and displays body of the response"""
import urllib.request
import urllib.parse
import sys

data = {'email': sys.argv[2]}
email = urllib.parse.urlencode(data)
email = email.encode('ascii')
pst = urllib.request.Request(sys.argv[1], email)
with urllib.request.urlopen(pst) as response:
    decd = response.read()
    print(decd.decode('UTF-8'))
