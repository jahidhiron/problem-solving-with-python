"""
Module: subsequence_generator

This module provides a function to generate and print all possible subsequences 
of a given list using recursion with backtracking.

A subsequence is a sequence that can be derived from another sequence by deleting 
some or no elements without changing the order of the remaining elements.

Example:
    >>> from subsequence_generator import all_subsequence
    >>> arr = [1, 2, 3]
    >>> all_subsequence(arr, 0, [])
    [1, 2, 3]
    [1, 2]
    [1, 3]
    [1]
    [2, 3]
    [2]
    [3]
    []
"""

def all_subsequence(arr, index, sub_arr):
    """
    Recursively generates and prints all subsequences of a given list.

    At each recursive step, the function explores two possibilities:
        1. Include the current element in the subsequence.
        2. Exclude the current element from the subsequence.

    Parameters:
        arr (list): The list from which subsequences are generated.
        index (int): The current index in `arr` being considered.
        sub_arr (list): The current subsequence being built.

    Returns:
        None
        This function prints each generated subsequence directly.

    Example:
        >>> arr = [1, 2, 3]
        >>> all_subsequence(arr, 0, [])
        [1, 2, 3]
        [1, 2]
        [1, 3]
        [1]
        [2, 3]
        [2]
        [3]
        []
    """
    if index == len(arr):
        print(sub_arr)
        return

    # Include current element
    sub_arr.append(arr[index])
    all_subsequence(arr, index + 1, sub_arr)

    # Exclude current element (backtrack)
    sub_arr.pop()
    all_subsequence(arr, index + 1, sub_arr)


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3]
    all_subsequence(arr, 0, [])
