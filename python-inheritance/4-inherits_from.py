#!/usr/bin/python3
"""Module return True if the obj is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Fonction return True if obj is instance of a class that inherited"""
    return issubclass(obj, a_class)
