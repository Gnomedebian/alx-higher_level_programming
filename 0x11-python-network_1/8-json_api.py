#!/usr/bin/python3

"""
take in a the letter and send a POST request to http://0.0.0.0:5000/search_user
"""

if __name__ == '__main__':
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    try:
        ar = sys.argv[1]
    except Exception:
        ar = ""
    q = {"q": ar}
    ree = requests.post(url, data=q)
    try:
        result = ree.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print("[{}] {}".format(result['id'], result['name']))
    except Exception:
        print("No result")
