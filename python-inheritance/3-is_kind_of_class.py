#!/usr/bin/python3
"""Module that return True
        if the type of obj is an instance of a_class
            otherwise return False"""


def is_kind_of_class(obj, a_class):
    """return True if obj is an instance of a_class"""
    return isinstance(obj, a_class)
