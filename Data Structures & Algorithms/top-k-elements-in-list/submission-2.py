class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = {}
        freq_to_num = {}
        output = []
        
        #1. Do a Number to Frequency Hashtable to get the connection going since you need to find frequency in this additive way
        for i in range(len(nums)):
            num_to_frequency[nums[i]] = num_to_frequency.get(nums[i], 0) + 1
        
        #2. Reverse the hashtable to get Frequency to Values (list) Hashtable to then quick lookup based on frequency
        for value,frequency in num_to_frequency.items():
            if frequency in freq_to_num.keys():
                freq_to_num[frequency].append(value)
            else:
                freq_to_num[frequency] = [value]
        
        #3. Read values from max possibility frequency going down  until we have the amount of numbers we need, and if the frequency we are looking at is there, add the values if theres 1 or more associated with that frequency
        for i in range(len(nums),0,-1):
            if len(output) == k:
                return output
            else: 
                if i in freq_to_num.keys():
                    for value in freq_to_num[i]: #If multiple values have same frequency
                        output.append(value)
        return output 


                
           
        
       
        
        