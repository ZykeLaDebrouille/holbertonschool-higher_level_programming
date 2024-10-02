#!/usr/bin/python3
"""This module countain a function
    that return a JSON representation of an obj(str)"""
import json
# To JSON string


def to_json_string(my_obj):
    """Function return a JSON representation of an obj(str)"""
    return json.dumps(my_obj)
