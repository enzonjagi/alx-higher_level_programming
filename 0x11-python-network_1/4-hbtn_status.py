#!/usr/bin/python3
""" Using the Requests package
a Python script that
fetches https://intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    r = r.text
    print('\t- type: ' + str(type(r)))
    print('\t- content: ' + r)
