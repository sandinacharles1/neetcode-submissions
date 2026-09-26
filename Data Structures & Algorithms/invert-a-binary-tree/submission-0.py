# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #Edge Case
        if not root:
            return None

        #BFS. Use a queue. FIFO. It wantss us to return the root, so lets swap in place
        #1. Initialize a queue with the root
        queue = deque([root])
        #2. While we keep adding items to the queue (meaning there are no children left)
        while queue:
            #3. Get the item from the top
            current = queue.popleft()

            #Edge(?) If that child node is Null, ignore the rest and go to the next item
            if not current: 
                continue
            #4. Swap them in place
            current.right, current.left = current.left, current.right
            #5 Append them to the queue so we can pop them in a later iteration and get their
            #Children and add them to the end after the next. Order of appending communitative
            #Since it just means it gets processed in a different order, not like we're 
            #printing them
            queue.append(current.right)
            queue.append(current.left)
            
        return root
        '''
        Put into a new ooutput
        if root is None:
            return []
        invertedTree = []

        #BFS. Use a queue. FIFO. 
        queue = deque()
        queue.append(root)
        
        def invert(queue):
            while queue:
                current = queue.popleft()
                invertedTree.append(current.val)
                
                queue.append(current.right)
                queue.append(current.left)
        
        invert(queue)
        return invertedTree
        '''
