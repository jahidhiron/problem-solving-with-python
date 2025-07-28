"""
Module to extract the individual digits from a integer
and return them as a list in the original order.

Contains a function `extract_digit` that splits an integer into digits.
"""


def extract_digit(n):
    """
    Extracts the digits of a integer n and returns them as a list.

    :param n: A integer.
    :return: List of digits in the order they appear in n.
    """
    digits = []

    while n > 0:
        digit = n % 10
        digits.append(digit)
        n = int(n / 10)

    digits.reverse()
    return digits


print("Digits:", extract_digit(6859))
