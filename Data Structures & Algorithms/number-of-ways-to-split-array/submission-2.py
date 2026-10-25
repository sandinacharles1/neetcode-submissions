class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
    #The first half must be >= second half. WE can do this by maintaining a list prefixes and suffixes so we can compare across a line . We loop through and check if Check if suffix[n] = prefix[n] + nums[n] (we have to include the number in only one group). 
        arr_length = len(nums)
        prefixes = [0] * arr_length
        suffixes = [0] * arr_length
        output = 0

        for index,num in enumerate(nums):
            if index == 0:
                prefixes[index] = num
                continue
            curr_prefix = prefixes[index - 1] + num
            prefixes[index] = curr_prefix
        
        for index in range(arr_length - 1, -1,-1):
            num = nums[index]
            add_suffix = suffixes[index + 1] if (index != arr_length - 1) else 0
            curr_suffix = num + add_suffix
            suffixes[index] = curr_suffix

            #Check for corresponding prefixes 
            if prefixes[index - 1] >= curr_suffix and index > 0:
                output += 1
        
        return output
