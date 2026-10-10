class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix,postfix = 1,1 #initialie

        for index,value in enumerate(nums):
            output[index] = prefix #the prefix is multiplied by numbers before
            prefix *= value

        for index in range(len(nums)-1, -1, -1): #-1 stop because stop is exclusive
            output[index] *= postfix
            postfix *= nums[index]
        
        return output