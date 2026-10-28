class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Get Heaviest Stones (priority)
        #Comparison logic
        stones_max_heap = [-stone for stone in stones]
        heapq.heapify(stones_max_heap)
        print(stones_max_heap)
        while len(stones_max_heap) > 1:
            y,x = heapq.heappop(stones_max_heap), heapq.heappop(stones_max_heap)
            
            if -y > -x:
                heapq.heappush(stones_max_heap, (y-x))
            print(y,x, stones_max_heap)
        return -stones_max_heap[0] if stones_max_heap else 0