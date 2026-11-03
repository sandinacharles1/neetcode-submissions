# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        '''Why this works. For every node, we have to abide by rules.
        If you go right, you MUST be greater than your parent. It CANNOT be less than. So whenever we get a new node after that, unless its invalid, it will fit within that range, hence it is grater (if we go right) than that node we evaluated that was  greater than the parent root. So that is ouur new minimum. Same with the left. root becomes maximum, then the next smaller one before it must be less than then its children will haave a max of that parent'''
        def validate(root, min_val, max_val):
            if not root: return True
            if not (min_val < root.val < max_val): return False
            return validate(root.left, min_val, root.val) and validate(root.right, root.val, max_val)
        
        return validate(root,float('-inf'), float('inf'))

        '''
        "This works because a valid BST requires subtrees to respect constraints from all ancestors, not just immediate parents. Every time we make a decision to move down the tree, we narrow our valid window (min, max):

• Going Right: The current node establishes a strict new minimum (floor) for everything below it. The maximum remains inherited from above.

• Going Left: The current node establishes a strict new maximum (ceiling) for everything below it. The minimum remains inherited from above.

By passing this window down recursively, every node checks if it fits within the historical boundaries established by its path from the root."'''