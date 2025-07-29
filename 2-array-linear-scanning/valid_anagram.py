"""
Anagram Checker Module

This module provides a function to determine whether two given strings are anagrams of each other.

Functions:
    is_anagram(s: str, t: str) -> bool:
        Returns True if 's' and 't' are anagrams, otherwise False.

Example:
    >>> is_anagram("listen", "silent")
    True

    >>> is_anagram("hello", "world")
    False

Usage:
    Run the module directly to see example outputs with predefined test strings.
"""


def is_anagram(s, t):
    """

    Time Complexity: O(n)
    Space Complexity: O(n)
    :type s: str
    :type t: str
    :rtype: bool
    """

    if len(s) != len(t):
        return False

    s_char_set = {}
    t_char_set = {}

    for i, v in enumerate(s):
        s_char = v
        t_char = t[i]

        s_char_set[s_char] = s_char_set.get(s_char, 0) + 1
        t_char_set[t_char] = t_char_set.get(t_char, 0) + 1

    return s_char_set == t_char_set


def is_anagram_sorting(s, t):
    """

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    :type s: str
    :type t: str
    :rtype: bool
    """

    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


def is_anagram_otp(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    if len(s) != len(t):
        return False

    s = s.lower()
    t = t.lower()

    freq_list = [0] * 26
    offset = ord('a')

    for i, v in enumerate(s):
        s_index = ord(v) - offset
        t_index = ord(t[i]) - offset

        # print(v, t[i])

        freq_list[s_index] += 1
        freq_list[t_index] -= 1

    for i in range(0, 26):
        if freq_list[i] != 0:
            return False

    return True


if __name__ == "__main__":
    STR_1 = "anagram"
    STR_2 = "nagaram"
    print(is_anagram(STR_1, STR_2))  # Output: True
    print(is_anagram_sorting(STR_1, STR_2))  # Output: True
    print(is_anagram_otp(STR_1, STR_2))  # Output: True

    STR_1 = "rat"
    STR_2 = "car"
    print(is_anagram(STR_1, STR_2))  # Output: False
    print(is_anagram_sorting(STR_1, STR_2))  # Output: False
    print(is_anagram_otp(STR_1, STR_2))  # Output: False
