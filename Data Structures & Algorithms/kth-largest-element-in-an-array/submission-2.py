import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''Priority Queue: So we can heapify the array, and keep popping in K times and return that value'''
        nums_max_heap = [-num for num in nums]
        heapq.heapify(nums_max_heap)
        largest_num = 0
        
        for count in range(k): largest_num = heapq.heappop(nums_max_heap)
        return -largest_num