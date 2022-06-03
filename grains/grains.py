import math

def square(number):
    if number > 64 or number < 1:
        raise ValueError('square must be between 1 and 64')

    if number == 1: return 1

    return square(number - 1) * 2


def total():
    squares = range(1, 64)
    sum = 0
    for n in squares:
        sum += square(n)

