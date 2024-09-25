#!/usr/bin/python3
"""Module return True if the obj is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    '''This function returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.'''
    return isinstance(obj, a_class) and type(obj) is not a_class
