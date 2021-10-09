# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        f, s = dummy, dummy
        # starting from dummy
        for i in range(n + 1):
            f = f.next

        while f is not None:
            f = f.next
            s = s.next

        s.next = s.next.next
        return dummy.next