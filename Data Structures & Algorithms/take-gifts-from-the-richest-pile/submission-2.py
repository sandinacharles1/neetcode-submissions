class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts_max_heap = [-num for num in gifts]
        heapq.heapify(gifts_max_heap)

        for _ in range(k):
            value = -heapq.heappop(gifts_max_heap)
            heapq.heappush(gifts_max_heap, -int((value**(1/2))))
        
        return -sum(gifts_max_heap)