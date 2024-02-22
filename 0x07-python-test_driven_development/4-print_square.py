#!/usr/bin/python3
""" Defines a square print function """


def print_square(size):
    """  prints a square with the character #

    Args:
        size: Size lenght of the square
    Raises:
        TypeError(int): if size is not an int
        ValueError(int): if size is less than 0
        TypeError(float): if size is a float and less than 0
    """
    if not isinstance(size, int):
        raise TypeError ("size must be an integer")
    if size < 0:
        raise ValueError ("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError ("size must be an integer")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
