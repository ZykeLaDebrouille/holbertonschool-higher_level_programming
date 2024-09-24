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


class Rectangle(BaseGeometry):
    """Class rectangle inherit from BaseGeometry"""
    def __init__(self, width, height):
        """Initatilise private atrrib width and height"""
        Rectangle.integer_validator(self, width, height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that return area"""
        return self.__width * self.__height

    def __str__(self):
        '''This method returns a string representation of the rectangle.'''
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that return area"""
        return self.__size ** 2
