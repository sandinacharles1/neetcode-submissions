class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #What I know: We will always want to keep moving right to  test
        '''
        My idea:
        (1) We keep elongating a string until it reaches a duplicate. That was our max for the area.
        (2) THen we keep cutting it until the duplciate is gone, and keep elongating it until it reaches a new dupliciate. 
        (3) Wait, if we keep cutting it until the duplicate is gone, then that's useless, since we also need to cuut AND elongate. Just elongate WHILE cutting
        '''
        count = 0
        char_index = {}
        l, r  = 0,0 #manual incrementing left pointer & right pointer

        while r < len(s):
            char = s[r]
            if char in char_index.keys() and char_index[char] >= l: #If the letter is in the sliding window (greater than l), update the hashmap so the l in the sliding window becomes the letter before the duplicate
                l = char_index[char] + 1
                
            char_index[char] = r #Update frequency of a NEW character to be right side
            r += 1
            count = max(count, r - l)
    
        return count
        '''
        THE FOLLOWING DOESN'T WORK BECAUSE IT WILL KEEP LOOKING UP STUFF OUTSIIDE THE SLIDING WINDOW
        if len(s) == 1:
            return 1

        for r, char in enumerate(s): #r is our auto-incrementing right pointer in the for-loop

            if char not in char_index.keys():
                char_index[char] = r
                
            else: #If it's already there, move the left pointer to where it was and update the hashmap to show its new location
                l = char_index[char] + 1
                char_index[char] = r
            '''
            