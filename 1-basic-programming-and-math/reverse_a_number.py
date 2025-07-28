"""
Module to reverse a 32-bit signed integer safely.
"""

import math


def reverse_number(n: int) -> int:
    """
    Reverses a 32-bit signed integer.
    Returns 0 if the reversed integer overflows.
    """

    result = 0
    limit_max = 2**31 - 1
    limit_min = -(2**31)
    sign = -1 if n < 0 else 1

    while n:
        last_digit = int(math.fmod(n, 10))

        if sign == 1 and (
            (
                result == int(limit_max / 10)
                and last_digit > int(math.fmod(limit_max, 10))
            )
            or (result > int(limit_max / 10))
        ):
            return 0

        if sign == -1 and (
            (
                result == int(limit_min / 10)
                and last_digit < int(math.fmod(limit_min, 10))
            )
            or (result < int(limit_min / 10))
        ):
            return 0

        result = result * 10 + last_digit
        n = int(n / 10)

    return result


if __name__ == "__main__":
    print("Reversed number:", reverse_number(8463847412))
    print("Reversed number:", reverse_number(7463847412))
    print("Reversed number:", reverse_number(7563847412))
    print("Reversed number:", reverse_number(-8463847412))
    print("Reversed number:", reverse_number(-9463847412))
    print("Reversed number:", reverse_number(-8563847412))
