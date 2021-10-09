"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longestCommonPrefix(strs) -> str:
    length = len(strs)
    min_len = float("inf")
    for word in strs:
        min_len = min(min_len, len(word))
    res = ""
    for i in range(min_len):
        ch = strs[0][i]
        common = True
        for j in range(1, length):
            if strs[j][i] != ch:
                common = False
        if common:
            res += ch
        else:
            return res
    return res

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))