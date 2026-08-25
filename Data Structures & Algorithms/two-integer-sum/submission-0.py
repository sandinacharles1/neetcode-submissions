class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {} #Value, Index. Index lookup
        for index, value in enumerate(nums): #1. Go through  list items & find complement
            complement = target - value
            
            if complement not in nums_hash.keys(): #2. if complement unpassed, continue
                nums_hash[value] = index
            else: #2. If complement in dictionary, look for its index
                index2 = nums_hash[complement]
                
                if index <= index2: #3. Put index in order
                    return [index, index2]
                else:
                    return [index2, index]
#HOW I SOLVED IT: Use a index lookup for values. This is because we will always be looking back to find the needed value and its index