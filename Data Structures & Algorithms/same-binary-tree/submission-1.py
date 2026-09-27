# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Base cases, when to stop instead of keep on going with their children
        if not p and not q: #If both nodes are nonexistent then we stop cuz no children
            return True

        if not p or not q: #if only one is done (since we already checked for if both)
            return False

        if p.val != q.val: #if they both exist but dont have the same value
            return False

        #Keep going with the children, right and left, and recurse
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

    
        