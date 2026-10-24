class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ''' How this works:
        We binary search through the list. We simeultaneously check for the target while taking note of the pivot point. We do that by checking to see which half is sorted. If our target may be in the sorted half, we restrict our search to the sorted half. If it isn't, then we at least remove our sortedd half to keep binary searching fofr a sorted-ish half where the number may lie
        '''
        start_idx, end_idx = 0, len(nums) - 1
        while start_idx <= end_idx:
            mid_idx = (start_idx + end_idx) // 2
            mid_val = nums[mid_idx]
            start_val, end_val = nums[start_idx], nums[end_idx]
            
            if mid_val == target:
                return mid_idx
            
            if mid_val >= start_val: #Left is sorted. Pivot right, nums greater than targ, less than [0]
                if target > mid_val or target < start_val: #remove left half
                    start_idx = mid_idx + 1
                else: #the target is IN the sorted range
                    end_idx = mid_idx
            
            elif mid_val < start_val: #The pivot point is before the mid_val, right is sorted
                if target < mid_val or target > end_val: #Remove the left half
                    end_idx = mid_idx 
                else: #the target is IN the sorted range
                    start_idx = mid_idx + 1
        return -1