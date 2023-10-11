#!/usr/bin/python3
"""read_file method"""


def read_file(filename=""):
    """
    Method that reads and prints a text file (UTF8)
    """
    with open(filename, encoding="utf-8") as my_file_0:
        print(my_file_0.read(), end="")
