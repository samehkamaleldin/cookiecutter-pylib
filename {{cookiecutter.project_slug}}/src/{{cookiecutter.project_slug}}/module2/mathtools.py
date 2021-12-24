from functools import reduce
from typing import List


def sum_nums(nums_list: List[int]) -> int:
    """
    Sum a list of numbers.

    :param nums_list: List of numbers.

    :return: Sum of the numbers.
    """
    return sum(nums_list)


def product_nums(nums_list: List[int]) -> int:
    """
    Multiply a list of numbers.

    :param nums_list: List of numbers.

    :return: Product of the numbers.
    """
    return reduce(lambda x, y: x * y, nums_list)


def add_one(num: int) -> int:
    """
    Add one to a number.

    :param num: Number to add one to.

    :return: Number + 1.
    """
    return num + 1
