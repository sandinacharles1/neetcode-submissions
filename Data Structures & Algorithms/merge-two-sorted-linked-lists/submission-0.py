# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #1. Have a node stay at the beginning. Maintain a moving node throughout your  list for comparisons. 
        first_node = node = ListNode()
        #2. Compare the two linked lists until we run out of one
        while list1 and list2:
            #compare the values for the list nodes from the original lists
            if list1.val < list2.val:
                #update our next node to be the beginning hence the entirety of list1
                node.next = list1
                #update for new comparisons right after the updated node
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            #keep incrementing to the NEWLY updaed and find its new next
            node = node.next
        #Update the rest of the linked list after one of them ended
        node.next = list1 or list2
        return first_node.next
