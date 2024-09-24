#!/usr/bin/python3
"""Module with class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry Class"""
    def area(self):
        """Raise an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Fonction to pass condition"""
        if not isinstance(value, int) or type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
