"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Initialize two empty arrays, L and R where for a given index i, L[i] would contain the product of all the numbers to the left of i and R[i] would contain the product of all the numbers to the right of i.
We would need two different loops to fill in values for the two arrays. For the array L, L[0]L[0] would be 1 since there are no elements to the left of the first element. For the rest of the elements, we simply use L[i] = L[i - 1] * nums[i - 1]L[i]=L[i−1]∗nums[i−1]. Remember that L[i] represents product of all the elements to the left of element at index i.
For the other array, we do the same thing but in reverse i.e. we start with the initial value of 1 in R[length - 1]R[length−1] where lengthlength is the number of elements in the array, and keep updating R[i] in reverse. Essentially, R[i] = R[i + 1] * nums[i + 1]R[i]=R[i+1]∗nums[i+1]. Remember that R[i] represents product of all the elements to the right of element at index i.
Once we have the two arrays set up properly, we simply iterate over the input array one element at a time, and for each element at index i, we find the product except self as L[i] * R[i]L[i]∗R[i].

"""
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    # The length of the input array
    length = len(nums)

    # The left and right arrays as described in the algorithm
    L, R, answer = [0] * length, [0] * length, [0] * length

    # L[i] contains the product of all the elements to the left
    # Note: for the element at index '0', there are no elements to the left,
    # so the L[0] would be 1
    L[0] = 1
    for i in range(1, length):
        # L[i - 1] already contains the product of elements to the left of 'i - 1'
        # Simply multiplying it with nums[i - 1] would give the product of all
        # elements to the left of index 'i'
        L[i] = nums[i - 1] * L[i - 1]

    # R[i] contains the product of all the elements to the right
    # Note: for the element at index 'length - 1', there are no elements to the right,
    # so the R[length - 1] would be 1
    R[length - 1] = 1
    for i in reversed(range(length - 1)):
        # R[i + 1] already contains the product of elements to the right of 'i + 1'
        # Simply multiplying it with nums[i + 1] would give the product of all
        # elements to the right of index 'i'
        R[i] = nums[i + 1] * R[i + 1]

    # Constructing the answer array
    for i in range(length):
        # For the first element, R[i] would be product except self
        # For the last element of the array, product except self would be L[i]
        # Else, multiple product of all elements to the left and to the right
        answer[i] = L[i] * R[i]

    return answer

nums = [1,2,3,4]
print(productExceptSelf(nums))