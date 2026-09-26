# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Recursive Approach: Base case, node is null, we stop. Else print, do same for child
        output = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            output.append(root.val)
            inorder(root.right)
        inorder(root)
        return output
