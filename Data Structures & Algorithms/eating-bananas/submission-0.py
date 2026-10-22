class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        output = float('inf')
        min_k, max_k = 1, max(piles) 
        
        #Upper bound. When time is limited and equals number of  piles. The minimum integer is the max 
        #value since you need to get through that first pile.
        while min_k <= max_k:
            k = (min_k + max_k) // 2
            hours = 0
            
            #Calculate hours needed
            for pile in piles:
                extra = (pile % k)
                if extra != 0:
                    extra = 1
                else:
                    extra = 0
                hours += (pile // k) + extra

            #If h is greater than what we want (increase k)
            if hours > h:
                min_k = k + 1
            else:
                output = min(output, k) #not necessary since we keep decreasing but helps understanding
                max_k = k - 1
        return output