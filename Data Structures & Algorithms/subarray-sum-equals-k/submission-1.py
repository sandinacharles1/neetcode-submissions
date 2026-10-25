class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1} #Incase theres an instance of a value that equals k
        subarrays_equaling_k = 0
        prefix = 0

        for index, num in enumerate(nums):
            prefix += num
            prefix_sums[prefix] = prefix_sums.get(prefix, 0) + 1
            complement_prefix = prefix - k
            
            if complement_prefix in prefix_sums:
                exclude_self = 1 if complement_prefix == prefix else 0
                subarrays_equaling_k += prefix_sums[complement_prefix] - exclude_self
        return subarrays_equaling_k