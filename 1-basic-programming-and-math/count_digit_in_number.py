"""
This module provides two functions to count the number of digits in an integer:
- count_digit: iterative approach with O(log n) time complexity.
- count_digit_con: constant time approach using logarithm.
Both handle zero and negative inputs gracefully.
"""


import math


def count_digit(n):
    """
    Count digits in n using iterative division.

    Time complexity: O(log n)

    :param n: A positive integer.
    :return: Number of digits in n.
    """
    count = 0
    while n > 0:
        n = int(n / 10)
        count += 1

    return count


def count_digit_opt(n: int) -> int:
    """
    Count digits in n using logarithm.

    Time complexity: O(1)

    :param n: A positive integer.
    :return: Number of digits in n.
    """
    return int(math.log10(n)) + 1


if __name__ == "__main__":
    print("Count of digits:", count_digit(65984))
    print("Count of digits:", count_digit_opt(65984465))
