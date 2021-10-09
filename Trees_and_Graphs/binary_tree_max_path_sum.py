"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
l = TreeNode(2)
r = TreeNode(3)
t = TreeNode(1, l, r)
"""
l = TreeNode(3)
r = TreeNode(1)
l1 = TreeNode(-5, l, r)
r1 = TreeNode(7)
t = TreeNode(5, l1, r1)

max_sum = float('-inf')


def max_path(root):
    max_gain(root)


def max_gain(node):
    if not node:
        return 0
    left_gain = max(max_gain(node.left), 0)
    right_gain = max(max_gain(node.right), 0)
    cur = node.val + left_gain + right_gain
    global max_sum
    max_sum = max(max_sum, cur)
    return node.val + max(left_gain, right_gain)

max_path(t)
print(max_sum)
