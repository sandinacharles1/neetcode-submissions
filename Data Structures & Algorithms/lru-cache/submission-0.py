class Node:
    def __init__(self,val=0, key=None, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        #Head -> MRU -> LRU -> Tail
        self.capacity = capacity 
        self.LRU_Keys = dict()
        self.head, self.tail = Node(), Node() #Head has most recently used, tail has least recently used
        self.head.next, self.tail.prev = self.tail, self.head #Connect them before making the list   

    def addNode(self, node):
        self.node = node
        self.MRU_Node = self.head.next
        self.MRU_Node.prev, self.node.next = self.node, self.MRU_Node
        self.head.next, self.node.prev = self.node, self.head
        self.LRU_Keys[node.key] = node

    def removeNode(self, node):
        self.node = node
        self.node.prev.next, self.node.next.prev = self.node.next, self.node.prev
        del self.LRU_Keys[node.key]
    
    def get(self, key: int) -> int:
        if key not in self.LRU_Keys:
            return -1
        node = self.LRU_Keys[key]
        self.removeNode(node)
        self.addNode(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        #If its already in: (1)Remove the Node, then add the new one to the head
        #IF its not in: Add key-value pair if greater than capacity, then remove LRU
        
        if key in self.LRU_Keys: #Update the value of the key if the key exists. 
            Original_Node = self.LRU_Keys[key]
            self.removeNode(Original_Node)
        
        New_Node = Node(value,key)
        self.addNode(New_Node)
        
        if len(self.LRU_Keys) > self.capacity:
            LRU = self.tail.prev
            self.removeNode(LRU)