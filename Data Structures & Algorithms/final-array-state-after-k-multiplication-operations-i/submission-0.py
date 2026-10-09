class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
       #Create min-heap to get minimum. Create shallow copy of nums to perform multiplication with preservation
        min_heap = [(num,index) for index,num in enumerate(nums)] #O(n)
        heapq.heapify(min_heap) #O(logn)
        result = nums[:] #copy
        #Loop through the heap, pop the smallest (it's tupled with index as a second criteria), and for the value at that index, multiply it. Then you add the bigger number to the min-heap that'll be addressed later with the multiplier, but we replace the value with its new multiplier value so it updates.
        for _ in range(k):
            value,index = heapq.heappop(min_heap) #O(1)
            result[index] *= multiplier
            heapq.heappush(min_heap, (result[index],index)) #Not Sorted O(1)
        
        ''' Issue: This doesn't perserve the heaps' order. It's right but unordered
        for _ in range(k):
            value,index = heapq.heappop(min_heap) #O(1)
            heapq.heappush(min_heap, (value * multiplier, len(min_heap))) #Not Sorted O(1)
        '''
        return result 