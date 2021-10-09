"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Input: root = [1]
Output: ["1"]
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


def construct_paths(node, path):
    if node:
        path += str(node.val)
        if not node.left and not node.right:  # if reach a leaf
            paths.append(path)  # update paths
        else:
            path += '->'  # extend the current path
            construct_paths(node.left, path)
            construct_paths(node.right, path)

paths = []
construct_paths(root, '')
print(paths)