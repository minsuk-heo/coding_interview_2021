"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


l = TreeNode(3)
r = TreeNode(1)
l1 = TreeNode(-5, l, r)
r1 = TreeNode(7)
root = TreeNode(5, l1, r1)

diameter = 0

def longest_path(node):
    if not node:
        return 0
    global diameter
    # recursively find the longest path in
    # both left child and right child
    left_path = longest_path(node.left)
    right_path = longest_path(node.right)

    # update the diameter if left_path plus right_path is larger
    diameter = max(diameter, left_path + right_path)

    # return the longest one between left_path and right_path;
    # remember to add 1 for the path connecting the node and its parent
    return max(left_path, right_path) + 1



print(longest_path(root))