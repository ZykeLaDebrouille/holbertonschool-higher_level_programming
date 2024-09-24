#!/usr/bin/python3
"""Module to sort a list"""


class MyList(list):
    """This is the list to sort"""
    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
