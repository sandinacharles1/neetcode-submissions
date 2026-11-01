# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #Goal: (1) FIND both p and q (2) Find the ancestor node
        #One way: We can find p and q using DFS while noting their individual ancestors, then check for any matching values since each value is unique.
        #Way 2: Since its a BST, we can look at the neighboring nodes. If p or q is greater than the node then we know the ancestor is that node (because thats where they separate). we keep doing that for each
        if not root:
            return
        
        #If it meets the criteria, we return it
        if p.val <= root.val and root.val <= q.val:
            return root
        if q.val <= root.val and root.val <= p.val:
            return root
        
        #Continuation if it doesnt. We search based on the value's relationship so we dont search       
        #unnecessarily. WE return because
        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        