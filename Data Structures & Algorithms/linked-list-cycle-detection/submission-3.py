# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = dummy_node = ListNode()
        dummy_node.next = head
        fast_pointer = head

        while fast_pointer and fast_pointer.next and slow_pointer != fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return False if slow_pointer != fast_pointer else True