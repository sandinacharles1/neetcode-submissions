# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Iterative approach. Stack for LIFO structure. For the most recent node checked
        #check its children (left first), then we checkc its right child (last appended)
        '''
        if root is None:
            return []
        
        stack = [root]
        output = []
        while stack:
            currentNode = stack.pop()
            if currentNode.right is not None:
                stack.append(currentNode.right)
            if currentNode.left is not None:
                stack.append(currentNode.left)
            output.append(currentNode.val)
        return output
        '''
        #Recursive Approach
        #Base case, we read a child thats null n we backtrack
        output = []
        def postorder(root):
            if not root:
                return []
            
            postorder(root.left)
            postorder(root.right)
            output.append(root.val)
        postorder(root)
        return output
