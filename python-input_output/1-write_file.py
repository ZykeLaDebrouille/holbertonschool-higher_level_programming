#!/usr/bin/python3
"""This module countain a function to write in a file"""
# Write to a file


def write_file(filename="", text=""):
    """Function that write in the file the text
            and return the number of character"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
