"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


# TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the 'EXPECTED_BAKE_TIME'.
    """

    bake_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_remaining


# TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.


def preparation_time_in_minutes(lasagne_layers: int) -> int:
    """Calculate the preparation time.

    Parameters:
        lasagne_layers (int): The number of layers of the lasagne.

    Returns:
        int: The preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers in the lasagna and returns how
    many minutes it take to prepare the layers based on the 'PREPARATION_TIME'.
    """

    prep_time = PREPARATION_TIME * lasagne_layers
    return prep_time


# TODO (student): define the 'elapsed_time_in_minutes()' function below.


def elapsed_time_in_minutes(lasagne_layers: int, time_baked: int) -> int:
    """Calculate the total elapsed time.

    Parameters:
        time_baked (int): the time in minutes the lasagne has been baking.
        lasagne_layers (int): The number of layers of the lasagne.

    Returns:
        int: The total time elapsed based on the 'PREPARATION_TIME' and 'EXPECTED_BAKE_TIME'.

    Function that takes the number of layers in the lasagna and and how long the lasagne
    has been naking to calculate how many minutes have elapsed based on the
    'PREPARATION_TIME' and 'EXPECTED_BAKE_TIME.
    """

    elapsed_time = (
        preparation_time_in_minutes(lasagne_layers)
        + EXPECTED_BAKE_TIME
        - bake_time_remaining(time_baked)
    )
    return elapsed_time


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
