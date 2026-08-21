class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #1. Create dict to carry letters and their frequencies 
        hashmap_S, hashmap_T = {}, {} 

        #2. For the amount of letters in each string (both equal since we filtered out), we use .get to assign the letter at each strings' index to a key in the hashmap, then increase the frequency by one.
        for i in range(len(s)):
            hashmap_S[s[i]] = hashmap_S.get(s[i],0) + 1 
            hashmap_T[t[i]] = hashmap_T.get(t[i],0) + 1
        
        return hashmap_T == hashmap_S