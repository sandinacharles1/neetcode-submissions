class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        num_to_idx = dict() 
        for l in range(len(nums)):
            if nums[l] in num_to_idx and (l - num_to_idx[nums[l]]) <= k:
                return True
 
            num_to_idx[nums[l]] = l

        return False
    '''
        num_to_idx = dict()
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
  '''         