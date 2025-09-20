# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            current_group_start = prev_group_end.next
            end_of_group = current_group_start
            for _ in range(k):
                if not end_of_group:
                    return dummy.next
                end_of_group = end_of_group.next
            
            prev_node = end_of_group
            curr_node = current_group_start
            for _ in range(k):
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node

            prev_group_end.next = prev_node
            prev_group_end = current_group_start