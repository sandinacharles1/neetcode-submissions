class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Edge Case:
        if len(s2) < len(s1): return False

        #Update Frequency tables
        s1_frequencies = [0] * 26
        s2_frequencies = [0] * 26
        for index in range(len(s1)): 
            s1_frequencies[ord(s1[index]) - ord('a')] += 1
            s2_frequencies[ord(s2[index]) - ord('a')] += 1 #initialize first sliding window
        
        #Dynamically update s2
        left_bound = 0
        right_bound = len(s1) - 1

        while right_bound < len(s2) - 1: 
            if s1_frequencies == s2_frequencies:
                return True
            
            #Increment -- HOWEVER if we are at the last window we CANNOT increment but we cant hceck since we already checked so we check at the return
            s2_frequencies[ord(s2[left_bound]) - ord('a')] -= 1
            left_bound += 1
            right_bound += 1
            s2_frequencies[ord(s2[right_bound]) - ord('a')] += 1 
            
        # Check the final window position after the loop finishes
        return s1_frequencies == s2_frequencies
