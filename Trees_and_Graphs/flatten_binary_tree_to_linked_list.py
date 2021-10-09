"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]


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



def flattenTree(node):
    # Handle the null scenario
    if not node:
        return None

    # For a leaf node, we simply return the
    # node as is.
    if not node.left and not node.right:
        return node

    # Recursively flatten the left subtree
    leftTail = flattenTree(node.left)

    # Recursively flatten the right subtree
    rightTail = flattenTree(node.right)

    # If there was a left subtree, we shuffle the connections
    # around so that there is nothing on the left side
    # anymore.
    if leftTail:
        leftTail.right = node.right
        node.right = node.left
        node.left = None

    # We need to return the "rightmost" node after we are
    # done wiring the new connections.
    return rightTail if rightTail else leftTail


flattenTree(root)
print(root)