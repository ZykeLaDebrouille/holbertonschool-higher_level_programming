#!/usr/bin/python3
def islower(c):
    """Function check if c (character) is lowercase 97 = 'a' and 122 = 'z'
    args: c
    return: True if c is lowercase, False otherwise
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
