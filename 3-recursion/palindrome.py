def is_palindrome(s, left, right):
    """
    Check if the given string is a palindrome using recursion.

    A palindrome is a string that reads the same forwards and backwards.

    :param s: The string to check
    :return: True if s is a palindrome, False otherwise
    """
    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return is_palindrome(s, left + 1, right - 1)


def check_palindrome(s):
    """
    Check if the given string is a palindrome and print the result.

    :param s: The string to check
    """
    if is_palindrome(s, 0, len(s) - 1):
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')


if __name__ == "__main__":
    STR1 = "racecar"
    check_palindrome(STR1)  # Output: "racecar" is a palindrome.

    STR2 = "hello"
    check_palindrome(STR2)  # Output: "hello" is not a palindrome.
