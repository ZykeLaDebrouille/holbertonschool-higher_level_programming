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
        if not isinstance(value, int):
            raise TypeError("size must be a integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print my square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
