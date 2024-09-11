#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for in_list, num in enumerate(list):
            print("{:d}".format(num), end="")
            if in_list != len(list) - 1:
                print(" ", end="")
        print()
