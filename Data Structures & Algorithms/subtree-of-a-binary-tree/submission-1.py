# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #2.Base Case: Check if either tree exists. 
        if not subRoot: return True
        if not root: return False
        
        #3. Work: Check if the trees are the same 
        def isSameTree(root, subRoot):
            if not root and not subRoot: return True #We reached the end!!
            if root and subRoot and root.val == subRoot.val:
                return (isSameTree(root.left,subRoot.left) and isSameTree(root.right,subRoot.right))
            return False #We reached an inconsistency
        if isSameTree(root, subRoot): return True 
        
        #4. If they aren't the same, check the subtrees for if theyre the same tree
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        