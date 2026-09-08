class MinStack:
#1. Logic for minimum time. As we append to our main list, we keep a current list of minimums. So we make it the same length as the stack, and show relative minimums to each point in the stack. So, when we remove the most recent item, if it was also a minimum, it goes bacck to the minimum before it.
    def __init__(self):
        self.stack = []
        self.minStack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            self.last = self.stack[-1]
        return self.last

    def getMin(self) -> int:
        #self.minimum = min(self.stack). Doesn't work. time complexity O(n)
        if self.stack:
            return self.minStack[-1]