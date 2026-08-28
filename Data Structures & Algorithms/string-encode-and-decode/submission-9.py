class Solution:
#ORIGINAL SOLUTION: Add a delimeter. Then slice based on delimiter. DOESNT WORK if delimeter is in solution. WE want to JUMP from word to word to not even risk that

#NEW SOLUTION: If you want to jump from words, then you need the length of the word then slice from it. We might need to decode with two pointer method, a pointer that finds the # and another pointer at start (beginning char length) and jump it to the next beginning char length
    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(i)) + "#" + i for i in strs)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0 #start at first letter
        
        while i < len(s): #NOT <= since we dont want it to do that near the end
            j = i #Start second pointer at first
            while s[j] != "#":
                j += 1
            #Once it reaches the hashtag, read the length of number
            length = int(s[i:j])
            strng = s[j+1: j+1+length] #read after hashtag and up to new letter. stop is exclusive so we add 1
            output.append(strng)
            i = j+1+length
        
        return output
