class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_hash  = {} #ALPHABETICAL, ANAGRAMS LOOKUP
        
        #1. Get the keys by alphabetically sorting the words
        for index, value in enumerate(strs):
            sorted_value = "".join(sorted(value)).lower()
        #2. Make the anagrams lookup values a list
            if sorted_value not in strs_hash.keys():
                strs_hash[sorted_value] = [value]
            else:
                strs_hash[sorted_value].append(value)
        
        return list(strs_hash.values())

#Time Complexity: O(n) * the sorting O(l*log(l)) (length of string) 

        