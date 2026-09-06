class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #1. Sort because it's difficult to get numerical order when adding stuff with two pointers
        nums.sort()
        result = []

        #2. Loop through the entire array to get a third const value, and use pointers to see what two values add to it. If we have already passed throughh values we have to check if it equals  the previous one to minimize duplicates
        for i in range(len(nums)): #shouldve used enumerate for cleanlieness.
            val = i
            if val > 0 and nums[val] == nums[val - 1]:
                continue #stop the loop and restart from step 2 where wew increrment since we dont have to do a while since num happened yeg
           
           #3. Use two-pointer to see if it adds to 0
            left, right = val + 1, len(nums) - 1
            while left < right: 
                nums3 = nums[left]  + nums[right] + nums[val]
                
                if nums3 > 0:
                    right -= 1
                elif nums3 < 0:
                    left += 1
                else: 
                    result.append([nums[val],nums[left],nums[right]])
                    #We still have to update a poointer or else its kind of going to be studck in this while left < right loop forever. it ALWAYS needs to end up incrementing. we can increment any side randomly because our two poiunter will automaticlly adapt so lets do the left. make sure the left doesnt have repeated sorted values
                    left += 1
                    while nums[left] == nums[left -1 ] and left < right:
                        left +=1
                    
                    

        return result

