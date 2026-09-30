class KthLargest:
    '''
    Method:
    We only care about the k largest element -> Heap. Single element needed. If it was a row,
    then I'd sort.
    
    Since we only know k largest, so working from largest to k-largest. (Not smallest to k
    smallest. thats why im not using max-heap). I'll pop all the minimums until we have a
    heap size k, and whenever we add, we add the value, pop the minimum after the value waws 
    added, and and the minimum will be the k-th
    
    Edge Cases: Empty OR less than k nums even after adding. just return minimum

    '''
    def __init__(self, k: int, nums: List[int]):
        #Initialize Variables
        self.nums_min_heap, self.k_largest_element = nums, k
        #Turn nums into a heap we can work with
        heapq.heapify(self.nums_min_heap)
        #Make it only the 3 largest elements, so pop the smaller ones
        while len(self.nums_min_heap) > self.k_largest_element:
            heapq.heappop(self.nums_min_heap)

    def add(self, val: int) -> int:
        #Add the value
        heapq.heappush(self.nums_min_heap, val)
        #Pop the smallest if its greater than the amount(we dont want to have it pop even when 
        #its smaller, yk), its out the k-largest running
        if len(self.nums_min_heap) > self.k_largest_element:
            heapq.heappop(self.nums_min_heap)
        #Return the smallest (k-th largest, not the actual largest). 
        return self.nums_min_heap[0]
