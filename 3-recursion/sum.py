"""
Recursive Summation Module

This module defines a simple recursive function to calculate the summation
of all integers from 1 to a given non-negative integer `n`.

Functions:
    summation(n): Returns the recursive summation from 1 to n.

Example:
    >>> summation(4)
    10
"""


def summation(n):
    """
    Recursively calculates the summation of all integers from 1 to n.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The summation of integers from 1 to n. Returns 0 if n is 0.

    Example:
        >>> summation(4)
        10
        # Because 4 + 3 + 2 + 1 + 0 = 10
    """
    if n == 0:
        return 0
    return n + summation(n - 1)


if __name__ == "__main__":
    print(summation(4))  # Output: 10
