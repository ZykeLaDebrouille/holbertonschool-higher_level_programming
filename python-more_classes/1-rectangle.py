#!/usr/bin/python3
"""Module for a class Rectangle"""


class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, height=0):
        """Initalization of instance attrib"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method private instance attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError(" width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method private instance attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError(" width must be >= 0")
        self.__height = value
