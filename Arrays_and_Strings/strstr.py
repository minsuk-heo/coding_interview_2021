"""
Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
"""
def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    return haystack.find(needle)

print(strStr("hello", "ll"))