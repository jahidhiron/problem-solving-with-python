"""
Module to reverse a 32-bit signed integer safely.
"""
import math


def armstrong_number(n: int) -> bool:
    """
    Check if a number is an Armstrong number.

    An Armstrong number (or narcissistic number) for a given number of digits n is an integer 
    such that the sum of its own digits each raised to the power n is equal to the number itself.

    :param n: The number to check.
    :return: True if n is an Armstrong number, False otherwise.
    """

    arms_sum = 0
    given_number = n

    while n:
        last_digit = int(math.fmod(n, 10))
        arms_sum += last_digit ** 3
        n = int(n / 10)

    return given_number == arms_sum


if __name__ == "__main__":
    print("Is Armstrong number:", armstrong_number(153))  # True
    print("Is Armstrong number:", armstrong_number(370))  # True
    print("Is Armstrong number:", armstrong_number(371))  # True
    print("Is Armstrong number:", armstrong_number(9474))  # True
    print("Is Armstrong number:", armstrong_number(123))  # False
    print("Is Armstrong number:", armstrong_number(1000))  # False
