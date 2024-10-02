#!/usr/bin/python3
"""This module countain a function
    that returns an object (Python data structure)
        represented by a JSON string."""
# From JSON string to Object
import json


def from_json_string(my_str):
    return json.loads(my_str)
