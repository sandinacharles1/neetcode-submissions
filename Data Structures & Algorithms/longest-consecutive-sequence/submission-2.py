class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Clarifications: Number that CAN be in order
        #What matters: 
            #Remembering numbers (hashmap). We do hashmap first, since numbers wont be in order so we cant check  chronologically. Since we dont have to store any key-value pair, it can be a set
            
            #Hypothetically: We could start with the smallest number, have a increment value, and an output where we perform max() after we reach the end of an increment, and bring increment down to 0
            
            #Concerns: How will we get the next value? if we remove the values from our previous checks, we could use min() on the set, but using min() during a loop is going to be O(n^2)
            nums_set = set(nums)
            consecutive_values_max_length = 0
            #We get the set, then we loop again, and for every value where n-1 isnt in the set, we add it to maybe a increment and keep removing the things from set until we have only something where n-1 isnt in set then we keep going until the set is gone?
            for num in nums:
                if num-1 not in nums_set:
                    
                    next_value = num + 1
                    while next_value in nums_set:
                        next_value += 1
                    consecutive_values_max_length = max(consecutive_values_max_length, next_value - num)
            return consecutive_values_max_length