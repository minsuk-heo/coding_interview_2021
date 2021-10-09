"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


def perm(input, i):
    if i == len(input) - 1:
        print(input)
    else:
        for j in range(i, len(input)):
            input[i], input[j] = input[j], input[i]
            perm(input, i + 1)
            input[i], input[j] = input[j], input[i]  # swap back, for the next loop


perm([1, 2, 3], 0)