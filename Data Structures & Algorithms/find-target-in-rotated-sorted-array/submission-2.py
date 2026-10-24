from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''1: #Logic: We check the middle and the end. If the middle is greater than the end, that means the pivot point is after the middle. If it's less than the end, that means the pivot point is in the beginning. The WHILE LOOP  is Less than since if the array is just one item, 0 < 1-0 will fail.  #2. Split array across pivot point. We know the first and last values and where the pivot point stops. WE know which array to search in. Then perform binary search. If it's the first half, the index is itself. if its in the second half, its pivot + itself'''


        #1. Find Pivot Point
        start_idx, end_idx = 0, len(nums) - 1
        pivot_idx = -1
        
        while start_idx < end_idx: 
            middle_idx = (start_idx + end_idx) // 2
            middle_value, end_value = nums[middle_idx], nums[end_idx]
            
            if middle_value > nums[middle_idx + 1]:
                pivot_idx = middle_idx
                break
            
            if middle_value > end_value:
                start_idx = middle_idx + 1
            elif middle_value <= end_value:
                end_idx = middle_idx  #i dont udnerstand why not -1
        
        target_index = -1 
        #EDGE CASE: NO ROTATION
        if pivot_idx == -1:
            target_index = bisect_left(nums, target)
            if len(nums) -1  < target_index:
                return -1
            return target_index if (nums[target_index] == target and target_index < len(nums)) else -1
        
        #ARRAY SLICING IN ROTATED SLICES
        first_num, last_num = nums[0],  nums[-1]
        greatest_num, smallest_num = nums[pivot_idx], nums[pivot_idx + 1]
            #First Slice Check
        if first_num <= target <= greatest_num:
            target_index  = bisect_left(nums, target, lo=0, hi=pivot_idx + 1)
            #Second Slice Check
        elif smallest_num <= target <= last_num:
            target_index  = bisect_left(nums, target, lo=pivot_idx + 1, hi=len(nums))
       
        return target_index if (nums[target_index] == target and target_index < len(nums)) else -1
        

       
