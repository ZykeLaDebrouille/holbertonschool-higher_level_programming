#!/usr/bin/python3
'''This module contains a class named Fish, a class named Bird, and a class named FlyingFish'''


class Fish():
    """Class represent Fish"""
    def swim(self):
        print("The fish is swimming")
    def habitat(self):
        print("The fish lives in water")

class Bird():
    """Class represent Bird"""
    def fly(self):
        print("The bird is flying")
    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    '''This class represents a FlyingFish.'''
    def fly(self):
        '''This method makes the flying fish fly.'''
        print("The flying fish is soaring!")

    def swim(self):
        '''This method makes the flying fish swim.'''
        print("The flying fish is swimming!")

    def habitat(self):
        '''This method describes the flying fish's habitat.'''
        print("The flying fish lives both in water and the sky!")
