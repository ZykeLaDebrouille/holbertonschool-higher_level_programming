#!/usr/bin/python3
"""Module to add an attribute"""


def add_attribute(obj, name, value):
    """Function that add an attrib if it possbile"""
    if hasattr(obj, __dict__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
