class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''Logic: 
        (1) We find the maximum of the window by getting max on the sliced portion O(k) time.
        (2) Then, when we shrink and we need to identify a new maximum.
        (2a) We know if the next value is greater than the maximum, thats the value.
        (2b) If its less than the maximum PLUS if the max is on the edge, there's extra things to know
        (2b.a) If the maximum was on the edge, we'd need to recalculate the new maximum, but how would 
        we know the maximum is on the edge? We could check the left_boundary - 1 to see if it equals the item we just ignored  Maybe we could keep a heap of values in the window. (-val). We first check to see if the max got removed, then add the new item to the heap and peek the maximum there. However, if a number is so low it never gets removed, we can make it (val, index) and we check the index to see if its in the range, if it isnt then we pop it anyway (save space) but ignore it '''
        
        window = [(-nums[i],i) for i in range(k)]
        heapq.heapify(window)
        
        sliding_window_max = []
        
        for left_index in range(len(nums) - k + 1):
            right_index = left_index + k - 1
            
            heapq.heappush(window,(-nums[right_index], right_index))
            while window[0][1] < left_index: 
                heapq.heappop(window)
            
            sliding_window_max.append(window[0][0] * -1)
        return sliding_window_max

                
