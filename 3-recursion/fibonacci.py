"""
Fibonacci Sequence Module

This module provides two recursive implementations of the Fibonacci sequence:
    1. A naive recursive approach (`fib`), which is simple but inefficient
       for large values of n due to repeated calculations.
    2. An optimized recursive approach with memoization (`fib_opt`), which
       stores computed values to avoid redundant calculations.

Functions:
    fib(n): Calculate the nth Fibonacci number using naive recursion.
    fib_opt(n): Calculate the nth Fibonacci number using memoized recursion.

The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2), for n > 1

Example:
    >>> fib(5)
    5
    >>> fib_opt(50)
    12586269025
"""


def fib(n):
    """
    Calculate the nth Fibonacci number using naive recursion.

    This method recalculates subproblems multiple times, resulting in
    exponential time complexity (O(2^n)).

    Parameters:
        n (int): The position in the Fibonacci sequence (0-indexed).
                 Must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.

    Example:
        >>> fib(5)
        5
        >>> fib(0)
        0
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def cal_fib(n, memo):
    """
    Helper function for calculating Fibonacci numbers using memoized recursion.

    Parameters:
        n (int): The position in the Fibonacci sequence (0-indexed).
        memo (dict): A dictionary to store computed Fibonacci values.

    Returns:
        int: The nth Fibonacci number.
    """
    if n in memo:
        return memo[n]

    result = cal_fib(n - 1, memo) + cal_fib(n - 2, memo)
    memo[n] = result
    return result


def fib_opt(n):
    """
    Calculate the nth Fibonacci number using recursion with memoization.

    This method stores previously computed Fibonacci numbers in a dictionary
    (`memo`) to avoid redundant calculations, achieving O(n) time complexity.

    Parameters:
        n (int): The position in the Fibonacci sequence (0-indexed).
                 Must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.

    Example:
        >>> fib_opt(5)
        5
        >>> fib_opt(50)
        12586269025
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    memo = {0: 0, 1: 1}
    return cal_fib(n, memo)


if __name__ == "__main__":
    N = 100
    # Output: The 100th Fibonacci number using optimized recursion
    print(f"The {N}th Fibonacci number is: {fib_opt(N)}")
