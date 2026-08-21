class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: #The -> is a return type hint
        nums_hash = set(nums)
        if len(nums_hash) == len(nums):
            return False
        else: #set is less than array because duplicates removed
            return True
        