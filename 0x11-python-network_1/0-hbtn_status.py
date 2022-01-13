#!/usr/bin/python3
"""A script that fetches a response in custom display"""

if __name__ == '__main__':
    from urllib import request

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        r = response.read()
        print('Body response:')
        print('\t-' + ' type: ' + str(type(r)))
        print('\t-' + ' content: ' + str(r))
        txt = r.decode('utf-8')
        print('\t-' + ' utf8 content: ' + txt)
