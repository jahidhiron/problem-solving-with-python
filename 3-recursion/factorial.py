"""
Recursive Factorial Module

This module defines a simple recursive function to calculate the factorial
of a given positive integer `n`.

Functions:
    factorial(n): Returns the factorial of `n` calculated recursively.

Example:
    >>> factorial(4)
    24
"""


def factorial(n):
    """
    Recursively calculates the factorial of a given positive integer `n`.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of `n`. Returns 1 if n is 0 or 1.

    Example:
        >>> factorial(4)
        24
        # Because 4 * 3 * 2 * 1 = 24
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(4))  # Output: 24
