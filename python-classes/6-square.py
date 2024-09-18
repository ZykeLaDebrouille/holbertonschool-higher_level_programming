#!/usr/bin/python3
""" Module for Class square """


class Square:
    """ Simple class square """
    def __init__(self, size=0, position=(0, 0)):
        '''Initialization '''
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method"""
        # Check if value is a tuple
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        # Check if right amount of integers
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[0], int) and not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        # Check if positive tuple
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the area (air)"""
        return self.__size ** 2

    def my_print(self):
        """Print my square"""
        if self.size == 0:
            print("")

        else:
            if self.position[1] > 0:
                for index in range(0, self.position[1]):
                    print("")

            for firstindex in range(0, self.size):
                print(" " * self.position[0], end="")
                for secondindex in range(0, self.size):
                    print("#", end="")
                print("")
