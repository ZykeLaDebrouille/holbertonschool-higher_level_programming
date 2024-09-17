#!/usr/bin/python3
""" Module for Class square """


class Square:
    """ Simple class square """
    def __init__(self, size=0,):
        '''Initialization '''
        self.__size = size

    def area(self):
        """Return the area (air)"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be a integer")
        if value < 0:
            raise ValueError("size must be >= 0")
