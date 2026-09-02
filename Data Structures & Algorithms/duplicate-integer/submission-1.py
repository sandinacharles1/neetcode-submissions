class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: #The -> is a return type hint
        nums_hash = set(nums)
        return not (len(nums_hash) == len(nums))
    
        #set is less than array because duplicates removed

        