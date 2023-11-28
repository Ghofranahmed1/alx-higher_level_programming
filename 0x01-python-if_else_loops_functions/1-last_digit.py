#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    num_copy = number % -10
else:
    num_copy = number % 10
if (num_copy > 5):
    print("Last digit of {number} is {num_copy} and is greater than 5")
elif (num_copy == 0):
    print("Last digit of {} is {} and is 0".format(number, num_copy))
else:
    print(f"Last digit of {number} is {num_copy} and is less than 6 and not 0")
