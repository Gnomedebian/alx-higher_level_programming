#!/Usr/Bin/Python3
"""
Fetche https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen("req") as res:
        body = res.read()

    print("Body response:")
    print("\t- Type: {}".format(body.__class__))
    print("\t- Content: {}".format(body))
    print("\t- Utf8 Content: {}".format(body.decode("ascii")))
