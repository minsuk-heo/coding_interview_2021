"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true
"""


def isIsomorphic(s: str, t: str) -> bool:
    d1 = {}
    d2 = {}

    for i, ch in enumerate(s):
        if ch not in d1:
            d1[ch] = [i]
        else:
            d1[ch].append(i)

    for i, ch in enumerate(t):
        if ch not in d2:
            d2[ch] = [i]
        else:
            d2[ch].append(i)

    if len(d1) == len(d2):
        for item in d1.values():
            if item not in d2.values():
                return False
        return True
    else:
        return False

print(isIsomorphic("egg","add"))
print(isIsomorphic("foo","bar"))
print(isIsomorphic("paper","title"))