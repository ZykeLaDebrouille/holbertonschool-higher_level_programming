#!/usr/bin/python3

def uppercase(str):

    '''Function put str in UPPERCASE 97 = 'a' and 122 = 'z'
                                            -32 (to get UPPERCASE)
    args: str
    return: none
    '''
    result = ""

    for char in str:
        if 97 <= ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))

