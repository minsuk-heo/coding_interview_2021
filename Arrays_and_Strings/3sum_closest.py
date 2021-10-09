"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Initialize the minimum difference diff with a large value.
Sort the input array nums.
Iterate through the array:
For the current position i, set lo to i + 1, and hi to the last index.
While the lo pointer is smaller than hi:
Set sum to nums[i] + nums[lo] + nums[hi].
If the absolute difference between sum and target is smaller than the absolute value of diff:
Set diff to target - sum.
If sum is less than target, increment lo.
Else, decrement hi.
If diff is zero, break from the loop.
Return the value of the closest triplet, which is target - diff.
"""


def threeSumClosest(nums, target) -> int:
    ans = float("inf")
    nums = sorted(nums)
    for i in range(len(nums)):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if abs(target - ans) > abs(target - s):
                ans = s
            if s < target:
                lo += 1
            else:
                hi -= 1
    return ans

print(threeSumClosest([-1,2,1,-4], 1))