"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
"""


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_cur = l1
        l2_cur = l2
        dummy = ListNode(0)
        d_cur = dummy
        while l1_cur and l2_cur:
            if l1_cur.val < l2_cur.val:
                d_cur.next = l1_cur
                d_cur = d_cur.next
                l1_cur = l1_cur.next
            else:
                d_cur.next = l2_cur
                d_cur = d_cur.next
                l2_cur = l2_cur.next
        while l1_cur:
            d_cur.next = l1_cur
            d_cur = d_cur.next
            l1_cur = l1_cur.next
        while l2_cur:
            d_cur.next = l2_cur
            d_cur = d_cur.next
            l2_cur = l2_cur.next

        return dummy.next
