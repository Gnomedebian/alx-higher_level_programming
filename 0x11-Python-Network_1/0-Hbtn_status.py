#!/Usr/Bin/Python3

"""Fetche Https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("Https://alx-intranet.hbtn.io/status") as res:
        body = res.read()
        print("Body response:")
        print("\t- Type: {}".format(type(body)))
        print("\t- Content: {}".format(body))
        print("\t- Utf8 Content: {}".format(body.decode("utf-8")))
