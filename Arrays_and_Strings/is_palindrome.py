"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""


def isPalindrome(x: int) -> bool:
    x_str = str(x)
    if len(x_str) == 1:
        return True

    if x_str[0] == "-":
        return False

    if x_str == x_str[::-1]:
        return True
    else:
        return False

print(isPalindrome(121))