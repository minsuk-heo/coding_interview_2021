"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1

The algorithm is quite straightforward :

Find a rotation index rotation_index, i.e. index of the smallest element in the array. Binary search works just perfect here.

rotation_index splits array in two parts. Compare nums[0] and target to identify in which part one has to look for target.

Perform a binary search in the chosen part of the array.


"""


def search(nums, target: int) -> int:
    def find_pivot(l, r):
        if l > r:
            return -1

        m = (l + r) // 2
        if m > 0 and nums[m] < nums[m - 1]:
            return m - 1
        if m < len(nums) - 1 and nums[m] > nums[m + 1]:
            return m
        else:
            if nums[m] < nums[r]:
                return find_pivot(l, m - 1)

            else:
                return find_pivot(m + 1, r)

    def find_target(l, r):
        if l > r:
            return -1
        m = (l + r) // 2
        if nums[m] == target:
            return m
        else:
            if nums[m] < target:
                return find_target(m + 1, r)
            else:
                return find_target(l, m - 1)

    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    pivot = find_pivot(0, len(nums) - 1)

    if pivot == -1:
        idx = find_target(0, len(nums) - 1)
    else:
        if target == nums[pivot]:
            return pivot

        if target < nums[0]:
            idx = find_target(pivot + 1, len(nums) - 1)
        else:
            idx = find_target(0, pivot - 1)
    return idx

print(search([4,5,6,7,0,1,2], 0))