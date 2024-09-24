#!/usr/bin/python3
"""Module that return True
        if the type of obj is exactly an instance of a_class
            otherwise return False"""


def is_same_class(obj, a_class):
    """return True if obj is exactly an instance of a_class"""
    return type(obj) is a_class
