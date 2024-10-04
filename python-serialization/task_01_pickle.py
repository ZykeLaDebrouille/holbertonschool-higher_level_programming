#!usr/bin/python3
"""Module countain a class CustomObject"""


class CustomObject:
    """class CustomObject"""
    def __init__(self, name, age, is_student):
        self.name = str(name)
        self.age = int(age)
        self.is_student = bool(is_student)
