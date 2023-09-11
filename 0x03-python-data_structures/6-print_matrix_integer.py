#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colu in row:
            print("{:d}".format(colu), end=" " if colu != row[-1] else "")
        print()
