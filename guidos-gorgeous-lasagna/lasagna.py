"""
Guido's Gorgeous Lasagna
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int):
    """Calculate preparation time in minutes.

    :param number_of_layers: int
    :return: int - Total preparation time

    Function that takes a number of layers to make and returns the number of minutes
    required to prepare the layers.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate total elapsed cooking time (prep + bake) in minutes.

    :param number_of_layers: int - layers to add to the lasagna.
    :param elapsed_bake_time: int - the number of minutes the lasagna has been baking in the oven.
    :return: int - Total number of minutes you've been cooking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
