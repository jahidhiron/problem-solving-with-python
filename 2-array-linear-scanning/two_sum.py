"""
Module to find two numbers in a list that sum up to a target value.
Includes a function `two_sum` and example usage.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two indices of numbers in the list that add up to the target value.
    Time complexity: O(n^2) — brute force approach.

    :param nums: List of integers.
    :param target: Target sum.
    :return: List containing the indices of the two numbers that add up to the target.
    """

    for i, hold in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if hold + nums[j] == target:
                return [i, j]

    return []


def two_sum_opt(nums: list[int], target: int) -> list[int]:
    """
    Find two indices of numbers in the list that add up to the target value.
    Time complexity: O(n) — brute force approach.

    :param nums: List of integers.
    :param target: Target sum.
    :return: List containing the indices of the two numbers that add up to the target.
    """
    visited = {}

    for i, _ in enumerate(nums):
        complement = target - nums[i]
        if complement in visited:
            return [visited[complement], i]
        visited[nums[i]] = i

    return []


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    visited = {}
    for i in range(0, len(nums)):
        compliment = target - nums[i]
        print(visited)
        if compliment in visited:
            return [visited[compliment], i]
        visited[compliment] = i

    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))       # Output: [0, 1]
    print(two_sum([3, 2, 4], 6))            # Output: [1, 2]

    print(two_sum_opt([7, 11, 15, 2], 9))   # Output: [0, 3]
    print(two_sum_opt([3, 2, 4], 6))        # Output: [1, 2]
    print(twoSum([3, 2, 4], 6))        # Output: [1, 2]
