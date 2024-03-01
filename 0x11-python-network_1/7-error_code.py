#!/usr/bin/python3
'''task 0: fetch data'''

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f'Error code: {response.status_code}')
    else:
        print(response.text)
