"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = []
Output: []

Input: nums = [0]
Output: []
"""


def threeSum(nums):
    res = []
    nums = sorted(nums)
    for i in range(len(nums)):
        t = 0 - nums[i]
        d = {}
        for j in range(i + 1, len(nums)):
            if nums[j] in d:
                item = [nums[i], d[nums[j]], nums[j]]
                if item not in res:
                    res.append(item)
            else:
                d[t - nums[j]] = nums[j]
    return res

print(threeSum([-1,0,1,2,-1,-4]))