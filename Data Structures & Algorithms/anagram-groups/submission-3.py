class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_letter_frequency_to_words= {}
        
        for word in strs:
            '''26 element freqeuncy array. Each unicdode value is an index'''
            letter_frequency = [0] * 26
            for char in word:
                letter_frequency[ord(char) - ord("a")] += 1
            key = tuple(letter_frequency)

            if key not in anagram_letter_frequency_to_words.keys():
                anagram_letter_frequency_to_words[key] = [word]
            else:
                anagram_letter_frequency_to_words[key].append(word)
        
        return list(anagram_letter_frequency_to_words.values())
            
