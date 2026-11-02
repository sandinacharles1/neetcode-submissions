# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        bfs_queue = deque([[root]])
        level_order_traversal = []
        
        while bfs_queue:
            #1. Get the list of current nodes
            curr_nodes = bfs_queue.popleft()
            
            #3. Make a new temporary list for the children of the listers
            next_level_nodes = []
            
            #4. For each item in the queue list, append their children to the temp list l -> r
            for node in curr_nodes:
                if node.left: next_level_nodes.append(node.left)
                if node.right: next_level_nodes.append(node.right)
            
            #2. Append the list (l->r) to our output
            level_order_traversal.append([node.val for node in curr_nodes])
            #append temp list to the queue
            if next_level_nodes: bfs_queue.append(next_level_nodes)
            
            
        
        return level_order_traversal