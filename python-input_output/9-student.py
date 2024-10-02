#!/usr/bin/python3
""" Module countain a Student Class with a to_json method"""
# Student to JSON


class Student():
    """"class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''returns dictionary representation of student instance'''
        return self.__dict__
