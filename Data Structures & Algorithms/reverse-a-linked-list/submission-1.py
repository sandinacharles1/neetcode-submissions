# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #0. Store the variables for holding the previous and current node
        previous_node, current_node = None, head
        #1. Storage the node.next value to a temporary 
        while current_node:
            next_node = current_node.next
        #2. Point the node.next to the previous (maintain a value for previous)
            current_node.next = previous_node
        #3. Increment the current node to become previous
            previous_node = current_node
        #4. Update the current to be the stored node.next value
            current_node = next_node
        #5. Return the head (the new head is the last value. Before next_node is null So, the last previous)
        return previous_node 