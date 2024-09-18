#!/usr/bin/python3
""" Module for Class square """


class Square:
    """ Simple class square """
    """ Simple class square """
    def __init__(self, size=0):
        '''Initialization '''
        if not isinstance(size, int):
            raise TypeError("size must be a integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size