#!/usr/bin/python3
"""My Github!
a Python script that takes your GitHub credentials
(username and password)
and uses the GitHub API to display your id
"""
from requests.api import head


if __name__ == '__main__':
    import requests
    import sys

    u_name = sys.argv[1]
    p_token = sys.argv[2]
    headers = {
        'Authorization': 'token {}'.format(p_token),
        'Accept': 'application/vnd.github.v3+json',
    }

    response = requests.get('http://api.github.com/user', headers=headers)
    print(response.json().get('id', 'None'))
