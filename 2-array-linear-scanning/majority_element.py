"""
majority_element.py

This module provides a function to find the majority element in a list of integers.
A majority element is defined as an element that appears more than ⌊n / 2⌋ times
in the list, where n is the length of the list.

Functions:
- majority_element(nums): Returns the majority element if it exists, otherwise 0.

Example usage:
    num_list = [3, 2, 3]
    print(majority_element(num_list))  # Output: 3

    num_list = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element(num_list))  # Output: 2
"""


def majority_element(nums):
    """
    Time complexity: O(n) — linear scanning.
    Space complexity: O(n) — using a dictionary to count occurrences.
    :type nums: List[int]
    :rtype: int
    """

    nums_count = {}

    for num in nums:
        if num not in nums_count:
            nums_count[num] = 1
        else:
            nums_count[num] += 1

    for value, count in nums_count.items():
        if count > len(nums) / 2:
            return value

    return 0


def majority_element_sorting(nums):
    """
    Time complexity: O(n log n) — sorting the list.
    Space complexity: O(n) — using a dictionary to count occurrences.
    :type nums: List[int]
    :rtype: int
    """

    sorted_nums = sorted(nums)
    mid_index = len(sorted_nums) // 2
    return sorted_nums[mid_index]


def majority_element_boyer_moor_voting_algorithm(nums):
    """
    Time complexity: O(n log n) — sorting the list.
    Space complexity: O(n) — using a dictionary to count occurrences.
    :type nums: List[int]
    :rtype: int
    """

    top_candidate = None
    count = 0

    for num in nums:
        if count == 0:
            top_candidate = num
        if top_candidate == num:
            count += 1
        else:
            count -= 1

    return top_candidate


if __name__ == "__main__":
    num_list = [3, 2, 3]
    print(majority_element(num_list))  # Output: 3

    num_list = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element(num_list))  # Output: 2

    print(majority_element_sorting(num_list))  # Output: 2

    num_list = [1, 2, 3, 2, 2, 2, 6]
    print(majority_element_boyer_moor_voting_algorithm(num_list))  # Output: 2
