#!/usr/bin/python3
'''This module creates a class MyInt that inherits from int'''


class MyInt(int):
    '''class MyInt inherits from int.'''
    def __eq__(self, other):
        '''This method returns the opposite of
            the result of the == operator.'''
        return super().__ne__(other)

    def __ne__(self, other):
        '''This method returns the opposite of
            the result of the != operator.'''
        return super().__eq__(other)
