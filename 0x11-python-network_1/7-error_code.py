#!/usr/bin/python3
"""Error code #1
a Python script that takes in a URL,
sends a request to the URL
and displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    import sys

    r = requests.get(sys.argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code:", r.status_code)
