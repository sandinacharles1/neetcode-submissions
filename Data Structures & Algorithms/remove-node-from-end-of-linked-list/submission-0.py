# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # So, to know if it's nth from end, we'd need to either (A) know the length of the list, then subtract (length - n) to get it relative to the head.(B) Or we can reverse the list and start from the end. (A) sounds more efficient, especially since we need to output in order too.

        # (A) find length of list. When we know what n is we have to subtract (length - n) 0-indexing
        linked_list_length = 0
        current_node = head

        # Count items
        while current_node:
            linked_list_length += 1
            current_node = current_node.next

        # Calculate index of nth-node
        node_to_remove_index = linked_list_length - n
        node_to_reassign = new_head = ListNode() 
        node_to_reassign.next = head

        # Get to the node before it
        for index in range(
            node_to_remove_index
        ):  # Since we put NEXT, we have to stop before the actual node to reassign  + the exclusivity of the range function
            node_to_reassign = node_to_reassign.next
        
        # Delete the nth node
        node_to_remove = node_to_reassign.next
        node_to_reassign.next = node_to_reassign.next.next
        node_to_remove.next = None
        return new_head.next
