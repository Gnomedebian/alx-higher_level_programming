#!/usr/bin/python3
'''Search API'''

if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    try:
        q = sys.argv[1]
    except Exception:
        q = ""
    data = {'q': q}
    response = requests.post(url, data=data)
    try:
        result = response.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print(f"[{result['id']}] {result['name']}")
    except Exception:
        print("No result")
