#!/usr/bin/python3
"""This module countain a function to write at the end in a file"""
# Append to a file


def append_write(filename="", text=""):
    """Function that write in the file the text
            and return the number of character"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
