import random


def generate_list(n, min_val, max_val):
    """
    Generates a list of numbers of a given length in a given interval and returns the result
    :param n: int - lenght of list
    :param min_val: int - min value in interval
    :param max_val: int - max value in interval
    """
    array = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        array.append(val)
    return array