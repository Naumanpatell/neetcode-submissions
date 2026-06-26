# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Method 2 --> Claude ans

        dummy = ListNode(0,head)
        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
        # Method 1 (Reverse, find, remove, Re-reverse) --> My first thought

        # prev = None
        # curr = head
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # new_head = prev

        # dummy = ListNode(0,new_head)
        # pointer = dummy
        # for _ in range(n-1):
        #     pointer = pointer.next
        # pointer.next = pointer.next.next

        # prev = None
        # curr = dummy.next
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev

