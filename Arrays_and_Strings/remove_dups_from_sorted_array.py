"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example
Input: nums = [1,1,2]
Output: 2, nums = [1,2]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
"""

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return
    prev = nums[0]
    idx = 1
    while idx < len(nums):
        if prev == nums[idx]:
            del nums[idx]
        else:
            prev = nums[idx]
            idx += 1

    return len(nums)

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))