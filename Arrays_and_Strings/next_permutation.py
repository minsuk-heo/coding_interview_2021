"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Examples
Input: nums = [1,2,3]
Output: [1,3,2]

Input: nums = [3,2,1]
Output: [1,2,3]

Input: nums = [1,1,5]
Output: [1,5,1]

Input: nums = [1]
Output: [1]

check from last index.
if list is desc order, just reverse it.
if you find asc ordered index(t), swap it with smallest but greater than t.
reverse items from t+1 to last index
"""


def nextPermutation(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 1
    while i > 0:
        if nums[i] > nums[i - 1]:
            t = i - 1
            j = len(nums) - 1
            while j > t:
                if nums[j] > nums[t]:
                    nums[j], nums[t] = nums[t], nums[j]
                    break
                else:
                    j -= 1
            l, r = t + 1, len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return nums
        else:
            i -= 1
    return nums.reverse()

nums = [1,1,5]
nextPermutation(nums)
print(nums)