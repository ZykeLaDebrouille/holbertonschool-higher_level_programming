#!/usr/bin/python3
""" Module countain a function
        that returns the dictionary description
            with simple data structure (l, dict, str, int, bool)
                for JSON serialization of an object. """
# Class to JSON
def class_to_json(obj):
    '''returns dictionary description with simple data structure'''
    return obj.__dir__
