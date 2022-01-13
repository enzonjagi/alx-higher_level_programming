#!/usr/bin/python3
"""Search API
a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

from requests import exceptions


if __name__ == '__main__':
    import requests
    import sys

    q = {'q': sys.argv[1] if len(sys.argv) >= 2 else ""}
    data = requests.post('http://0.0.0.0:5000/search_user', data=q)
    res = data.text

    try:
        j = data.json()
        if j.get('id', None) is None:
            print('No result')
        else:
            print('[{}] {}'.format(j['id'], j['name']))
    except Exception:
        print('Not a valid JSON')
