#!/usr/bin/python3
"""Module where we begin abstract method"""
# Abstract Animal Class and its Subclasses
# Import ABC and abstractmethod from abc module
# Define the Animal class as an abstract class
# Define the Dog and Cat classes as subclasses
from abc import ABC, abstractmethod

class Animal(ABC):
    '''This is an abstract base class for animals.'''
    @abstractmethod
    def sound(self):
        '''This method should be implemented by subclasses.'''
        pass

class Dog(Animal):
    '''This class represents a Dog.'''
    def sound(self):
        '''This method returns the sound a dog makes.'''
        return 'Bark'

class Cat(Animal):
    '''This class represents a Cat.'''
    def sound(self):
        '''This method returns the sound a cat makes.'''
        return 'Meow'
