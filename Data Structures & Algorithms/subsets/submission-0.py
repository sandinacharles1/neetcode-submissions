class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #We have to go through EACH option (consider it as a first option). Append after every step
        #WE can either INCLUDE or exclude a numbber. we can see all the options including it then backtrack to all the options excuding it. with backtracjking, you always turn it into differnet decisions
        subsets, current_subset = [], []
        def backtrack(index):
            if index == len(nums): 
                subsets.append(current_subset.copy()) #After a full decision tree we append. Including & Excluding so we can know we have ALL then we also have none
                return
            
            #Including The Value
            current_subset.append(nums[index])
            backtrack(index + 1)
            current_subset.pop()
            
            #Excluding the Value
            backtrack(index + 1)
            return
        
        backtrack(0)
        return subsets
