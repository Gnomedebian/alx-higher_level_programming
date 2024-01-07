#!/usr/bin/python3
"""
same as the.task.2 with requests models
"""

if __name__ == '__main__':
    import requests
    import sys
    para = {"email": sys.argv[2]}
    ree = requests.post(sys.argv[1], data=para)
    print(ree.text)
