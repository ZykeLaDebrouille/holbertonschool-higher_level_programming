#!/usr/bin/python3
# CountedIterator - Keeping Track of Iteration
# Define the CountedIterator class
# Override __next__ method and implement get_count method
"""Module countain class CountedIterator"""


class CountedIterator():
    """class CountedIterator inherit from iter"""
    def __init__(self, iterable):
        '''This method initializes the iterator and count.'''
        self.iterator = iter(iterable)
        self.counter = 0


    def get_count(self):
        '''This method returns the number of items returned by the iterator.'''
        return self.counter

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item
