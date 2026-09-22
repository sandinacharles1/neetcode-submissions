
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        We have to remember previous numbers BEFORE. so we loop through the array, list numbers against (WHAT ORDER OF NUMBERS IT IS) and check every time for if n - 1 is already in the hashmap.
        '''

        #1. Create the set
        nums_set = set(nums)
        max_sequence = 0
        
        #2. If it is a FIRST value, we calulcate the length by looping through until we reach 
        #the last value of the sequence. 
        for val in nums:
            if (val - 1) not in nums_set: 
                length = 1
                #3. Doesn't count as O(n2) because this only happens for specific values
                while (val + length) in nums_set: 
                    length += 1
                
                max_sequence = max(max_sequence, length)
        return max_sequence

        
        









        '''
        Only works for finding the longest sequence. I misunderstood the question.
        Let's use sliding window. 
       Elongates: when it notices the the next value is one more than the next
        Puts its new starting value at the next number if it is NOT consecutive
        #1. Variable Initialization
        longest_sequence = 0
        max_idx = 1
        min_idx = 0
        
        #2. Loop through until the second maximum value reaches the end. Not the maximum, 
        #since we check if the next value (which if it was the end, would be out of range)
        while max_idx < (len(nums) - 1):
            next_val = nums[max_idx + 1]
            
            if (nums[max_idx] + 1) == next_val:
                max_idx += 1
            else:
                min_idx = next_val
                max_idx = next_val + 1
            
            longest_sequence = max(longest_sequence, max_idx - min_idx)
        
        #return
        return longest_sequence
        '''
