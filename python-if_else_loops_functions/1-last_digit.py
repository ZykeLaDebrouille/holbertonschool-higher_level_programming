#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = abs(number) % 10
if LastDigit == 0:
    print(f"Last digit is {LastDigit} and is 0")
elif LastDigit < 6 and LastDigit != 0:
    print(
        f"Last digit of {number} is {LastDigit} and is less then 6 and not 0")
elif LastDigit > 5:
    print(f"Last digit is {LastDigit} and is greater than 5")
