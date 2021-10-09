"""
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.

Input: s = "a", t = ""
Output: true

Input: s = "", t = "A"
Output: true

"""


def isOneEditDistance(s: 'str', t: 'str') -> 'bool':
    ns, nt = len(s), len(t)

    # Ensure that s is shorter than t.
    if ns > nt:
        return isOneEditDistance(t, s)

    # The strings are NOT one edit away distance
    # if the length diff is more than 1.
    if nt - ns > 1:
        return False

    for i in range(ns):
        if s[i] != t[i]:
            # if strings have the same length
            if ns == nt:
                return s[i + 1:] == t[i + 1:]
            # if strings have different lengths
            else:
                return s[i:] == t[i + 1:]

    # If there is no diffs on ns distance
    # the strings are one edit away only if
    # t has one more character.
    return ns + 1 == nt