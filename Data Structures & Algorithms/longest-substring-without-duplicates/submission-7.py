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
            
            #If the letter is in the sliding window (greater than l), update the hashmap so the leftmost part of the sliding window becomes the letter after the duplicate
            if char in char_index.keys() and char_index[char] >= l: 
                l = char_index[char] + 1
                
            char_index[char] = r #Update index of the rightmost character, it wont be a duplicate since we removed it in the if statement. 
            r += 1
            count = max(count, r - l)
    
        return count
        
        '''
        Explanation:
        We have a right and a left pointer. We want to REMEMBER (hashmap) if a letter is within our sliding window. So, to manage that, we make a char to index hashmap.
        Next, we want to keep auto-incrementing our right, to elongate as much as possible. And we always update our hashmap by adding / updating this character to show its index
        However, we want to cut off the left side and increment if our right comes across a duplicate letter. How do we do this? We see if our current r character is in the hashmap, and if it is WITHIN the current sliding window where l is our minimum, since our hashmap also includes previous letters that may not be in our window no more. Then, we update our left pointer to go to the index associated with that value  + 1 to get rid of that letter so we can make our right pointer equal it. 
        Always increment our right after we perform actions so we're  not doing actions 1 step ahead.
        '''
        
        
        
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
            