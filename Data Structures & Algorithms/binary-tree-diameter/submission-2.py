# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        I'm thinking we can do depth-first search, 
        
        0) For this question, we have to get the diameter. The diameter = left + right heigths
        
        1) To get the heights, we can use recursion where we add 1 (increment) to the dfs of 
        the right and left subtree, where we get their individual children, add one for the
        row the children is on, and check their individual childrenn to get the number of
        extra rows the childrenn has until there are no more rows left

        2) However, the function cant and shouldn't be run at root because sometimees it
        isnt at the root. That means we have to continuously run it for each child node.
        We can incorporate it in our dfs calculation that already goes through each child node
        and the work where we calculate diameter and maximize our result output to see if 
        diameter isi greater if the child node is treated as the current "root"
        '''
         #member variable, makes it accessibble in the nested function
        self.result = 0
        
        def dfs(root):
            #base case
            if not root:
                return 0
            
            #WORK: Get the depth of each node's subtrees. keep recalculating result for sub-
            #trees until the recursive output adds it all up
            leftDepth = dfs(root.left)
            rightDepth = dfs(root.right)
            self.result = max(self.result, leftDepth + rightDepth)
            
            #Recursive output for sub-functions
            return 1 + max(leftDepth ,rightDepth)

        

        dfs(root)
        return self.result
        
