# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1. Find the middle. That'll be the last value (the value where the reversing starts). This is found by slow and fast pointer where the slow pointer = middle when fast = null.
        fast_pointer, slow_pointer = head, head
        while fast_pointer and fast_pointer.next: #wont increment if its a 1 or 2 value linkedlist
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        
        #2. While at the middle, that's when we start reversing the lsit (because the last nodes go togehter in reversed order). You do this by incrementing then getting the next, saving it, pointing back to previous and updating to the next node until done at the new head.
        previous = None #not the middle, thats first half
        reversed_list = slow_pointer.next
        slow_pointer.next = None #detach from the  next one because we we skip it to save as previous
        while reversed_list:
            next_node = reversed_list.next
            reversed_list.next = previous
            #Store current as previous
            previous = reversed_list
            #incrmenet
            reversed_list = next_node
        #3 Now we whave a list that looks like first half -> mid <- last half. So now to re-order, we have opointers at the old head and the new head.  and we point old to new and save the next, then new to old, etc etc
        first_half_node, last_half_node = head, previous
        while last_half_node: #while they dont point to 3
            #store nexes 
            next_first_half_node = first_half_node.next
            next_last_half_node = last_half_node.next
            
            
            #point second half back to first
            first_half_node.next = last_half_node
            last_half_node.next = next_first_half_node
            
            #increment 
            first_half_node, last_half_node = next_first_half_node, next_last_half_node
