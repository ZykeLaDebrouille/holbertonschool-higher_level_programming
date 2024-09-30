#!/usr/bin/python3
"""This module countain a function to read file """
# Read file


def read_file(filename=""):
    """_summary_
    Read file given in parameter
    Args:
        filename"".
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
    # We can check that the file has been automatically closed.
    # print(f.closed) -> True
