# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''Method 1: making the queue/stack without popping and compare the lists.
        Issues: Takes O(2n) space and time, can we maximimize the space?
        Method 2: While doing dfs, we can have a work function that sees if the val equals
        the other val. No, the issue with that is, when we run recursively, it isnt 
        concurrent'''

        def dfs(root, array):
            #base case 
            if root is None:
                array.append("Null")
                return 
            
            #Work
            array.append(root.val)
            
            #Recursive
            dfs(root.right, array)
            dfs(root.left, array)

        p_array = []
        q_array = []
        dfs(p,p_array)
        dfs(q,q_array)
        
        if p_array == q_array :
            return True
        
        return False