#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(arrAy):
    """
        Function that finds a peak in a
        list of unsorted integers
    """
    if arrAy == []:
        return None
    if len(arrAy) == 1:
        return arr[0]
    if arrAy[0] >= arrAy[1]:
        return arrAy[0]
    if arrAy[len(arrAy) - 1] >= arrAy[len(arrAy) - 2]:
        return arrAy[len(arrAy) - 1]
    for i in range(1, len(arrAy) - 1):
        if arrAy[i] >= arrAy[i - 1] and arrAy[i] >= arrAy[i + 1]:
            return arrAy[i]
        