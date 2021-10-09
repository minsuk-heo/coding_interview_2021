"""
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
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


def lowestCommonAncestor(root, p, q):
    ans = None

    def recurse_tree(current_node):
        nonlocal ans

        # If reached the end of a branch, return False.
        if not current_node:
            return False

        # Left Recursion
        left = recurse_tree(current_node.left)

        # Right Recursion
        right = recurse_tree(current_node.right)

        # If the current node is one of p or q
        mid = current_node == p or current_node == q

        # If any two of the three flags left, right or mid become True.
        if mid + left + right >= 2:
            ans = current_node

        # Return True if either of the three bool values is True.
        return mid or left or right

    # Traverse the tree
    recurse_tree(root)
    return ans

print(lowestCommonAncestor(root, l, r).val)