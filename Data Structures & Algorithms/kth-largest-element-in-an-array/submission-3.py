from _heapq import heappushpop
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''Priority Queue: So we can heapify the array, and keep popping in K times and return that value'''
        nums_max_heap = [-num for num in nums]  #O(n) time O(n) space
        heapq.heapify(nums_max_heap) #O(n) time O(1) space
        largest_num = 0
        
        for count in range(k): largest_num = heapq.heappop(nums_max_heap) #O(k*log(n))
        return -largest_num
        #Overall: O(n + k*log(n)) time and O(n) space
        #We can maybeb reduce the O(n) to O(k) by keeping a FIXED size k instead of making ti big then reducing. THen we keep heappoping for 

        nums_size_k_heap = [-num for num in nums[:k]] #O(k) time and space
        heapq.heapify(nums_size_k_heap) #O(n) time O(1) space
        
        for index, num in nums[k:]: #O((n-k))
            if -num < nums_size_k_heap[0]: 
                heapq.heappushpop(nums_size_k_heap, -num) #O(logn)
        return numss_size_k_heap[0]
