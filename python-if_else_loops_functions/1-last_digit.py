#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last = abs(number) % 10
if number < 0:
    Last = -Last
if Last == 0:
    print(f"Last digit of {number} is {Last} and is 0")
elif Last < 6 and Last != 0:
    print(
        f"Last digit of {number} is {Last} and is less then 6 and not 0")
elif Last > 5:
    print(f"Last digit of {number} is {Last} and is greater than 5")
