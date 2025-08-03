"""
Recursive Array Reversal Module

This module provides two methods to reverse an array in place using recursion:
1. A forward recursive approach (`reverse_array`)
2. A backtracking-style recursive approach (`reverse_array_by_back_tracking`)

Functions:
    - swap(arr, left, right): Helper for forward recursive reversal.
    - reverse_array(arr): Reverses the array using forward recursion.
    - swap_by_back_tracking(arr, left, right): Helper for backtracking reversal.
    - reverse_array_by_back_tracking(arr): Reverses the array using backtracking recursion.

Example:
    >>> arr = [1, 2, 3, 4, 5]
    >>> reverse_array(arr)
    [5, 4, 3, 2, 1]
    >>> reverse_array_by_back_tracking(arr)
    [1, 2, 3, 4, 5]
"""


def swap(arr, left, right):
    """Recursively swaps elements from both ends to reverse the array (forward recursion).

    Args:
        arr (list): The array to be reversed.
        left (int): The starting index.
        right (int): The ending index.
    """
    if left < right:
        arr[left], arr[right] = arr[right], arr[left]
        swap(arr, left + 1, right - 1)


def reverse_array(arr):
    """Reverses the elements of the array in place using forward recursion.

    Args:
        arr (list): The array to be reversed.
    """
    swap(arr, left=0, right=len(arr) - 1)
    print(arr)


def swap_by_back_tracking(arr, left, right):
    """Recursively swaps elements using backtracking to reverse the array.

    Args:
        arr (list): The array to be reversed.
        left (int): The starting index.
        right (int): The ending index.
    """
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    swap_by_back_tracking(arr, left + 1, right - 1)


def reverse_array_by_back_tracking(arr):
    """Reverses the elements of the array in place using backtracking recursion.

    Args:
        arr (list): The array to be reversed.
    """
    swap_by_back_tracking(arr, left=0, right=len(arr) - 1)
    print(arr)


if __name__ == "__main__":
    sample_array = [1, 2, 3, 4, 5]
    reverse_array(sample_array)  # Output: [5, 4, 3, 2, 1]

    sample_array1 = [1, 2, 3, 4, 5]
    reverse_array_by_back_tracking(sample_array1)  # Output: [5, 4, 3, 2, 1]
