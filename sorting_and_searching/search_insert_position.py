"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
"""


def searchInsert(nums, target: int) -> int:
    if len(nums) == 0:
        return 0
    s, e = 0, len(nums) - 1
    while s <= e:
        m = (s + e) // 2
        if nums[m] == target:
            return m
        else:
            if nums[m] > target:
                e = m - 1
            else:
                s = m + 1
    if target < nums[m]:
        if m == 0:
            return 0
        else:
            return m
    else:
        if m == len(nums) - 1:
            return len(nums)
        else:
            return m + 1

print(searchInsert([1,3,5,6], 5))