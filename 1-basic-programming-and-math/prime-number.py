import math


def prime_number(n: int) -> bool:
    """
    Check if a number is prime.

    A prime number is greater than 1 and has no divisors other than 1 and itself.
    Time complexity: O(n)

    :param n: An integer to check for primality.
    :return: True if n is prime, False otherwise.
    """
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    print("Count of factors:", count)
    return count == 2


def prime_number_optimized(n: int) -> bool:
    """
    Check if a number is prime using an optimized approach.

    This function checks divisibility only up to the square root of n,
    which reduces the number of iterations significantly.

    Time complexity: O(sqrt(n))

    :param n: An integer to check for primality.
    :return: True if n is prime, False otherwise.
    """

    pivot = int(math.sqrt(n))
    count = 0

    for i in range(1, pivot + 1):
        if n % i == 0:
            count += 1
            factor2 = int(n / i)

            print("Factors:", i, factor2)

            if factor2 != i:
                count += 1

    print("Count of factors:", count)
    return count == 2


if __name__ == "__main__":
    print("Is prime number:", prime_number(16))   # True
    print("Is prime number:", prime_number_optimized(16))   # True
    # print("Is prime number:", prime_number(2))   # True
    # print("Is prime number:", prime_number(3))   # True
    # print("Is prime number:", prime_number(4))   # False
    # print("Is prime number:", prime_number(13))  # True

    # print("Is prime number:", prime_number_optimized(2))   # True
    # print("Is prime number:", prime_number_optimized(3))   # True
    # print("Is prime number:", prime_number_optimized(4))   # False
    # print("Is prime number:", prime_number_optimized(13))  # True
