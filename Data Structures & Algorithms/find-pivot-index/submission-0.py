class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #calulate all the valueus to the left and to thhe right of EACH number
        #Do this by 
        length = len(nums)
        nums_prefix_sum = [0] * length
        nums_postfix_sum = [0] * length
        
        for index in range(1,length):
            nums_prefix_sum[index] += nums[index - 1] + nums_prefix_sum[index - 1]
       
        for index in range(length -2, -1, -1):
            nums_postfix_sum[index] += nums[index + 1] + nums_postfix_sum[index + 1]
        
        for index,(prefix,postfix) in enumerate(zip(nums_prefix_sum, nums_postfix_sum)):
            if prefix == postfix:
                return index
        return -1
