#!/usr/bin/python3
"""
same as the.task.3 with requests model
"""

if __name__ == '__main__':
    import requests
    import sys
    ree = requests.get(sys.argv[1])
    if ree.status_code >= 400:
        print("Error code: {}".format(ree.status_code))
    else:
        print(ree.text)
