#!/usr/bin/python3
"""
same as the.task.1 with requests module
"""

if __name__ == '__main__':
    import requests
    import sys
    ree = requests.get(sys.argv[1])
    print(ree.headers.get('X-Request-Id'))
