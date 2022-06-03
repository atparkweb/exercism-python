import math

def square(number):
    if number > 64 or number < 1:
        raise ValueError('square must be between 1 and 64')

    if number == 1: return 1

    return square(number - 1) * 2


def total():
    pass
