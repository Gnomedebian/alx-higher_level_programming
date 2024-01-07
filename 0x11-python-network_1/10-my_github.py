#!/usr/bin/python3

"""
takes your GitHub credentials (userName and passw0rd)
and uses GitHub API to display the-ID
"""

if __name__ == '__main__':
    import sys
    import requests
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    info = (username, password)
    ree = requests.get(url, auth=info)
    try:
        print(ree.json()['id'])
    except Exception:
        print('None')
