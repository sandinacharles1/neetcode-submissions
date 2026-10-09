class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        self.min_heap = nums[:]
        heapq.heapify(self.min_heap) #O(logn)

        while len(nums) > k: #O(non-k)
            heapq.heappop(nums) #O(logk)
            

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val) #O(logk)
        
        while len(self.min_heap) > self.k: #O(non-k)
            heapq.heappop(self.min_heap) #O(logk)
        
        return self.min_heap[0] #O(1)
    #Space Complexity: O(k) sice the hep store max
    #Tiem complexity: O(logk) per call