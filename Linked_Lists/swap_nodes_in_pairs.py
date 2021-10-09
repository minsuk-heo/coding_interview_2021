"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        cur = dummy.next
        nxt = dummy.next.next

        while cur and nxt:
            prev.next = nxt
            cur.next = nxt.next
            nxt.next = cur
            prev = cur
            if prev.next:
                cur = prev.next
                if prev.next.next:
                    nxt = prev.next.next
                else:
                    break
            else:
                break
        return dummy.next