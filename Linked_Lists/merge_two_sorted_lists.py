"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []

Input: l1 = [], l2 = [0]
Output: [0]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    # maintain an unchanging reference to node ahead of the return node.
    prehead = ListNode(-1)

    prev = prehead
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    # At least one of l1 and l2 can still have nodes at this point, so connect
    # the non-null list to the end of the merged list.
    prev.next = l1 if l1 is not None else l2

    return prehead.next

l1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(3)
l1_2.next = l1_3
l1.next = l1_2

l2 = ListNode(2)
l2_2 = ListNode(3)
l2_3 = ListNode(4)
l2_2.next = l2_3
l2.next = l2_2

result = mergeTwoLists(l1, l2)
result