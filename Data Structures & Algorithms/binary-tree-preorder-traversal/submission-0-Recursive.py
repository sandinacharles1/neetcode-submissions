# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Depth-First search Logic :
        For each parent, we check the left-most value down. Then go up and check right,
        move up levels

        Pre-Order:
        This means we check left-most child first. We cann do this by checking the value, then
        the left child, then thhe right

        How to implement:
        METHOD 1: Recursion:
        We keep a base case of if the root is null so we stop that one recursive iteration
        but otherwise we run the function on the function's children. First the left, it will
        runn all its lefties first before left reaches null and we move onto the right. 
        We make sure to include the work of appending to the output 

        METHOD 2: ITERATIVE:
        We maintain a stack. Its LIFO structure is helpful because we need to get deep into 
        the most recently checked node. VISUALIZE THIS: We start the stack at the root. We
        pop the root then append the right -> left. The left is the most recent in the stack,
        now we pop the left and add its children right-> left. We stop and pop once left 
        reaches null. Now, we go to the most recent right. Then the most recent right up

        Edge case: Empty tree
        '''
        
        result = [] 
        '''! PROBLEM: List resets every time because its apart of the entire class 
        children and it doesn't work well when children are traversed. 
        NEW THING LEARNED: Helper functions. We can define a function in our algorithm to 
        consolidate the functions we always want it to re-run'''
        def traverse(root):
            #Edge case / base case
            if not root:
                return 
            #Work
            result.append(root.val)    
            #recursion functions
            if root.left:
                traverse(root.left)
            
            if root.right:
                traverse(root.right)
        
        traverse(root)
        return result
