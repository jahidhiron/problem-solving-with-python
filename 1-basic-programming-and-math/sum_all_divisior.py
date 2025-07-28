"""
This module contains a function to calculate the sum of divisors of a number,
along with example usage when run as a script.
"""
import math


def sum_of_divisors(n: int) -> int:
    """
    Calculate the sum of all divisors of a given number n.
    Time complexity: O(n)

    :param n: The number to find divisors for.
    :return: The sum of all divisors of n.
    """

    divisor_sum = 0
    for i in range(1,  n + 1):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum


def sum_of_divisors_opt(n: int) -> int:
    """
    Calculate the sum of all divisors of a given number n.
    Time complexity: O(sqrt(n))

    :param n: The number to find divisors for.
    :return: The sum of all divisors of n.
    """

    pivot = int(math.sqrt(n))
    divisor_sum = 0
    for i in range(1,  pivot + 1):
        if n % i == 0:
            paired_divisor = int(n / i)
            if i == paired_divisor:
                divisor_sum += i
            else:
                divisor_sum += i + paired_divisor
    return divisor_sum


if __name__ == "__main__":
    print("Sum of divisors:", sum_of_divisors(12))  # Output: 28
    print("Sum of divisors:", sum_of_divisors(28))  # Output: 56
    print("Sum of divisors:", sum_of_divisors(6))   # Output: 12

    print("Sum of divisors:", sum_of_divisors_opt(12))  # Output: 28
    print("Sum of divisors:", sum_of_divisors_opt(28))  # Output: 56
    print("Sum of divisors:", sum_of_divisors_opt(6))   # Output: 12
