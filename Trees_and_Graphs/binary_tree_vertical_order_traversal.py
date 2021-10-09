"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque

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


def verticalOrder(root):
    if root is None:
        return []

    columnTable = defaultdict(list)
    min_column = max_column = 0
    queue = deque([(root, 0)])

    while queue:
        node, column = queue.popleft()

        if node is not None:
            columnTable[column].append(node.val)
            min_column = min(min_column, column)
            max_column = max(max_column, column)

            queue.append((node.left, column - 1))
            queue.append((node.right, column + 1))

    return [columnTable[x] for x in range(min_column, max_column + 1)]

print(verticalOrder(root))