"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""


def searchRange(nums, target: int):
    def find_first(start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] != target:
                return mid
            return find_first(start, mid - 1)
        else:
            return find_first(mid + 1, end)

    def find_last(start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                return mid
            return find_last(mid + 1, end)
        else:
            return find_last(start, mid - 1)

    def find_target(start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return find_target(mid + 1, end)
        else:
            return find_target(start, mid - 1)

    if len(nums) == 0:
        return [-1, -1]

    idx = find_target(0, len(nums) - 1)
    if idx == -1:
        return [-1, -1]
    f = find_first(0, idx)
    l = find_last(idx, len(nums) - 1)
    return [f, l]

print(searchRange([5,7,7,8,8,10], 8))