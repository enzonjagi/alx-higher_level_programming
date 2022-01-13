#!/usr/bin/python3
"""Decoded output
a Python script that takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""

from urllib import error


if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys

    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            data = response.read()
            data = data.decode('utf-8')
            print(data)
    except urllib.error.HTTPError as err:
        print('Error code: ' + str(err.code))
