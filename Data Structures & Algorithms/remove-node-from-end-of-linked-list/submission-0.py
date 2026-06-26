# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Method 1 (Reverse, find, remove, Re-reverse)
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        new_head = prev

        dummy = ListNode(0,new_head)
        pointer = dummy
        for _ in range(n-1):
            pointer = pointer.next
        pointer.next = pointer.next.next

        prev = None
        curr = dummy.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

