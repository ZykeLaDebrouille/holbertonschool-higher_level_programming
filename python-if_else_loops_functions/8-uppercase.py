#!/usr/bin/python3

def uppercase(str):

    '''Function put str in UPPERCASE 97 = 'a' and 122 = 'z'
                -32 (to get UPPERCASE) chr(65) is 'A' chr(90) is 'Z'.
    args: str
    return: none
    '''
    UPit = ""

    for char in str:
        if 97 <= ord(char) <= 122:
            UPit += chr(ord(char) - 32)
        else:
            UPit += char
    print("{}".format(UPit))
