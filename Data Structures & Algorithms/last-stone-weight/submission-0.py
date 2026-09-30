class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        While heap > 1:
        GET two heaviest. Max-heap. Pop the maximums
        Run a if-else. Then heappush the new weight
        '''
        stones_max_heap = [-stone for stone in stones]
        heapq.heapify(stones_max_heap) 
        
        while len(stones_max_heap) > 1:
            heaviest = -heapq.heappop(stones_max_heap)
            second_heaviest = -heapq.heappop(stones_max_heap)

            if heaviest == second_heaviest:
                continue
            else:
                heapq.heappush(stones_max_heap, -(heaviest - second_heaviest))
        
        if not stones_max_heap:
            return 0
        
        return -stones_max_heap[0]