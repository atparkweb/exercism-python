"""
Guido's Gorgeous Lasagna
"""
EXPECTED_BAKE_TIME_MINUTES = 40
PREPARATION_TIME_MINUTES = 2


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME_MINUTES'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME_MINUTES`.
    """
    return (EXPECTED_BAKE_TIME_MINUTES - elapsed_bake_time)


def preparation_time_in_minutes(number_of_layers: int):
    """Calculate preparation time in minutes.
    :param number_of_layers: int
    :return: int - Total preparation time

    Function that takes a number of layers to make and returns the number of minutes
    required to prepare the layers.
    """
    return PREPARATION_TIME_MINUTES * number_of_layers

