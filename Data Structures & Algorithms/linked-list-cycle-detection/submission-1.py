# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Use cycle detection. One pointer moves slow and the other moves fast!
        slow_ptr, fast_ptr = head, head

        #Process: In a loop (so it doesn't return false after one  pass)
        while fast_ptr and fast_ptr.next: #while we haven't reached the end, Since the fast skips twice, it will eventually make the fast_ptr go to none, which is what we want to end the loop. So we check that it isnt none AND it has a next coming incase we have none and try none.next. we only want valid.nextifyk
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next 

            #Stop: when they equal Eachother
            if slow_ptr == fast_ptr:
                return True
        
        return False 