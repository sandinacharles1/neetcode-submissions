class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_to_index = {}
        
        for index,num in enumerate(nums):
            complement = target - num
            
            if complement in number_to_index.keys():
                return [number_to_index[complement], index]
            
            number_to_index[num] = index