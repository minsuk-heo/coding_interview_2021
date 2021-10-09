"""
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Now one could write down the algortihm.

Return 0 if the string is empty or k is equal to zero.
Set both set pointers in the beginning of the string left = 0 and right = 0 and init max substring length max_len = 1.
While right pointer is less than N:
Add the current character s[right] in the hashmap and move right pointer to the right.
If hashmap contains k + 1 distinct characters, remove the leftmost character from the hashmap and move the left pointer so that sliding window contains again k distinct characters only.
Update max_len.
"""

from collections import defaultdict


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    n = len(s)
    if n * k == 0:
        return 0

    # sliding window left and right pointers
    left, right = 0, 0
    # hashmap character -> its rightmost position
    # in the sliding window
    hashmap = defaultdict()

    max_len = 1

    while right < n:
        # add new character and move right pointer
        hashmap[s[right]] = right
        right += 1

        if len(hashmap) == k + 1:
            # delete the leftmost character
            del_idx = min(hashmap.values())
            del hashmap[s[del_idx]]
            # move left pointer of the slidewindow
            left = del_idx + 1

        max_len = max(max_len, right - left)

    return max_len

s = "eceba"
k = 2
print(lengthOfLongestSubstringKDistinct(s, k))