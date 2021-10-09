"""
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"
"""


def longestPalindrome(s: str) -> str:
    def expand(mid1, mid2, s):
        nonlocal res
        left = mid1
        right = mid2
        while left > -1 and right < len(s) and s[left] == s[right]:
            if len(res) < right - left + 1:
                res = s[left:right + 1]
            left -= 1
            right += 1

    res = ""
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    for i in range(len(s)):
        if i + 1 == len(s):
            expand(i, i, s)
        else:
            expand(i, i, s)
            expand(i, i + 1, s)
    return res


print(longestPalindrome("abba"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("a"))