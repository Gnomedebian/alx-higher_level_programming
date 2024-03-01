#!/usr/bin/python3
'''The X-Request-Id Variable Found In The Header Of The Response.'''

if __name__ == "__main__":
    import sys
    import urllib.request
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as r:
        response = r.info()
        print(response.get("X-Request-Id"))
