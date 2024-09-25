#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that return area"""
        return self.__size ** 2

    def __str__(self):
        '''This method returns a string representation of the square.'''
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
