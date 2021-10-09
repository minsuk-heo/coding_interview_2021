"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container,
such that the container contains the most water.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Algorithm:
Keep two index, first = 0 and last = n-1 and a value max_area that stores the maximum area.
Run a loop until first is less than the last.
Update the max_area with maximum of max_area and min(array[first] , array[last])*(last-first)
if the value at array[first] is greater the array[last] then update last as last – 1 else update first as first + 1
Print the maximum area.

"""


def maxArea(height) -> int:
    l, r = 0, len(height) - 1
    max_width = 0
    while l < r:
        max_width = max(max_width, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_width

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))