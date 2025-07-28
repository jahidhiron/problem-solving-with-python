"""
This module provides functions to calculate the Greatest Common Divisor (GCD) of two integers.
It includes a basic implementation that checks all possible divisors up to the minimum of the 
two numbers.
"""


def gcd_func(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
    Time complexity: O(min(a, b))

    :param a: First integer.
    :param b: Second integer.
    :return: GCD of a and b.
    """

    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


def gcd_func_opt_1(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
    Time complexity: O(min(a, b))

    :param a: First integer.
    :param b: Second integer.
    :return: GCD of a and b.
    """

    for i in range(min(a, b), 1, -1):
        if a % i == 0 and b % i == 0:
            return i

    return 1


def euclidian_gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
    Time complexity: O(log(min(a, b))) — more precisely, O(log_φ(min(a, b))), where φ ≈ 1.618.

    :param a: First integer.
    :param b: Second integer.
    :return: GCD of a and b.
    """

    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    if a == 0:
        return b
    return a


if __name__ == "__main__":
    print("GCD of 12 and 9:", gcd_func(12, 9))  # Output: 3
    print("GCD of 56 and 98:", gcd_func(56, 98))  # Output: 14

    print("GCD of 11 and 13:", gcd_func_opt_1(11, 13))  # Output: 1
    print("GCD of 56 and 98:", gcd_func_opt_1(56, 98))  # Output: 14

    print("GCD of 11 and 13:", euclidian_gcd(11, 13))  # Output: 1
    print("GCD of 52 and 2:", euclidian_gcd(52, 2))  # Output: 2
