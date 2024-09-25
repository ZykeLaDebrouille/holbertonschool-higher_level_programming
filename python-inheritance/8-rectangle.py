#!/usr/bin/python3
"""Module with class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry Class"""
    def area(self):
        """Raise an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Fonction to pass condition"""
        if type(value) is not int:
            raise TypeError(name  + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


class Rectangle(BaseGeometry):
    """Class rectangle inherit from BaseGeometry"""
    def __init__(self, width, height):
        """Initatilise private atrrib width and height"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
