class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        How to find pivot point: We can use binary search, except binary search only works when its sorted.We can binary search fornthe minimum as long as we know the pivot point and check the right half and left half of the pivot point respectively. 
        We can find the pivot point by finding which numbers' next is less thanit. We can keep a number pivot = index and NONE otherwise and if its none we get nums[0]
        however, looping through is o(n)'''
        #1. Find pivot point. If the middle between the numbers are grater than the last, then the pivot point is after the number. r becmes mile. IF less than then its to the right
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l+r)//2
            nums_mid = nums[mid]

            if nums_mid  > nums[mid + 1]:
                return nums[mid + 1]
            if nums_mid  > nums[r]:
                l = mid + 1
            elif nums_mid  < nums[r]:
                r = mid 
        return nums[0]
        
        
            
