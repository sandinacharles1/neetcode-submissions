class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = 0
        total_sum = sum(nums)
        
        for index, value in enumerate(nums):
            postfix_sum = total_sum - prefix_sum - value
            if prefix_sum == postfix_sum:
                return index
            prefix_sum += value
        
        return -1