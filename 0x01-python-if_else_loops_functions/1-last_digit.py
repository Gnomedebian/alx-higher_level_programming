#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = abs(number) % 10
if number < 0:
    s = -s
if s > 5:
    print(f"Last digit of {number} is {s} and is greater than 5")
elif s == 0:
    print(f"Last digit of {number} is {s} and is 0")
else:
    print(f"Last digit of {number} is {s} and is less than 6 and not 0")
