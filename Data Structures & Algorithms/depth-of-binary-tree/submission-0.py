# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''WE write our nodes, but after each row of nodes, we add its level DFS
        1) Initalize our stack. We add right and left children & analyze the left
        We will keep adding left children to the end so when we pop
        we pop from the bottom to its parent and that parent's siblings etc. 
        2) While our stack isn't complete (like we havent exhausted all the items), 
        we check for if that child ended up null, if it isnt, then we move on
        3) We pair together values and their numebrs, so each child will get their parents'
        level and increment on that
        4) If we end up going back in time (from popping children back to the higher levels)
        we have to use max() instead of incrementing each time
        '''
        if not root:
            return 0
        
        stack = [[root,1]]
        output = 0

        while stack:
            #spread number and level
            node, level = stack.pop()
            if node: #if it isnt one of the nulls
                output = max(output, level)
                
                next_level = level + 1
                stack.append([node.right, next_level])
                stack.append([node.left, next_level])
                
        return output