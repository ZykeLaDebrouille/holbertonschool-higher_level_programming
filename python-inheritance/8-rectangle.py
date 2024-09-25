#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle inherit from BaseGeometry"""
    def __init__(self, width, height):
        """Initatilise private atrrib width and height"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
