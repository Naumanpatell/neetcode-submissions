# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy # WE USE ANOTHER VARIBLE BECAUSE WE WANT TO KEEP THE DUMMY AS IT IS AND NOT MOVE IT.
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next #JUST A FANCY WAY TO MOVE THE POINTER
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2 #ONE LIST GOES NONE JUST ADD THE OTHE LIST AFTER THE TAIL
        return dummy.next


#Revised today (24 July 2026) Did not mark tail worked directly with dummy forgot to to actually move the tail pointer and line after it as well.(edit wrote this 10 times after that)