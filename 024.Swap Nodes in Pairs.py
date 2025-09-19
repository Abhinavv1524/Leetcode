# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            # Nodes to be swapped
            first = head
            second = head.next
            
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move pointers
            prev = first
            head = first.next
        
        return dummy.next