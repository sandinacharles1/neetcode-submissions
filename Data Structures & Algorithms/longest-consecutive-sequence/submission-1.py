class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        To find sequences
        (0) Hashset all the numbers for easy memory and access in O(1) time
        (1) Get the initalizing number
        (2) Find out if values after it exist. Keep looping until we end and find 
        that final number
        (3) Keep track of a count for each iteration of going through consecutive 
        numbers
        Constraints: Skip duplicates
        '''
        count = 0
        nums_set = {num for num in nums} #0. Make a hashmap for easy access
        
        for num in nums_set:
            if (num - 1) in nums_set: #1. If it's a number mid-sequence, ignore
                continue
            else: #2. Keep incrementing the length until it isn't in the set
                length = 1
                while (num + length) in nums_set: 
                    length += 1
                count = max(count, length) #Find if this sequence is bigger than 
                #the next
        return count