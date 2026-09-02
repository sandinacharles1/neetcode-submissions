class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #1. Mark the indices from start to end
        left = 0
        right = len(nums) - 1
        #2. While there are numbers inside to split, split down middle. left and right can be equal & it'll just test itself as a number.
        while left <= right:
            mid = (left + right) // 2 #floor division
            result = nums[mid]
            
            if result == target:
                return mid
            elif result > target:
                right = mid - 1
            elif result < target:
                left = mid + 1
        
        return -1
