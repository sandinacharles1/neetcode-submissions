# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #initalize variables. Nothing for previous since there's nothing before the head And the current is the head (it starts at the first value automatically ig despite head being a full list)
        previous, current = None, head #head is a single object


        while current: #loops through linked list until the 
        #Switch the direction of linked list. keep temporary storee of following numebrs
            temporary = current.next
            current.next = previous #Make the previous be the next in the current. I did this first then realized now we lost the other variables after current.next becasue we are not pointing towards them so i added the ones above

            #move up our previous and and our current. the current is the temporary we saved before we switched to reverse
            previous = current
            current = temporary

        return previous #Return previous because previous is now the new START aka head of the linked list. When your return the head, it then points to the next, then the next, and returns the list
