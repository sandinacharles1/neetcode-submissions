class Solution:
    def isPalindrome(self, s: str) -> bool:
        #same forward and backward
        newS = "".join(char.lower() for char in s if char.isalnum()) #check if its a letter or number, alphanumeric, not periods or stuff
        left, right = 0, len(newS) - 1
        
        while left < right: #whilst theyre not the same letter
            if newS[left] != newS[right]:
                return False
            else:
                left += 1
                right -= 1
        return True