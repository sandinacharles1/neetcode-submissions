class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''(1) check for every instance of a letter beginning with something in s1
        (2) Maintain a length, the goal is to break when length == len(s1)
        (3) Use right pointer to keep moving while the letter is in words (DOESN"T WORK. DUPLICATE 
        LETTERS)        
        
        SECOND OPTION:
        (1) Sliding window length s1
        (2) See if the window equals s1 '''
        
        #0. Edge case, where s1 cannot fit into s2
        if len(s1) > len(s2):
            return False
        
        #1. Create Window Variables
        s1_size = len(s1) #no minus one, exclusive
        left_ptr, right_ptr = 0, s1_size
        
        while right_ptr <= len(s2):
            window = s2[left_ptr: right_ptr]

            #2. SOLVING ANAGRAMS! Add lettters in s1, subtract in s2
            '''Anagram Explanation
            We make an array with 26  spots for all 26 letters
            
            We add a frequency of a letter INTO that spot. WE calculate the spot using Ord() which is 
            unicode. HOWEVER, a starts at 97, so to have the leeters in their respective places, we 
            subtract by 97 to start from 0 - 26 letters

            For the first letter, we build the table, for the second, we subtract to see if its all
            0, which implies that they're all equal amounts of the same letters
            '''
            freq = [0] * 26
            for char1, char2 in zip(s1, window): 
                freq[ord(char1) - ord('a')] += 1
                freq[ord(char2) - ord('a')] -= 1
            if all(num == 0 for num in freq):
                return True

            #3. Slide the window
            left_ptr += 1
            right_ptr += 1
        return False
        