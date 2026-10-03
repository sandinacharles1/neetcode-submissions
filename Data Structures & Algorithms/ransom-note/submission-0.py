class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        magazine_letter_frequency = Counter(magazine)
        
        for letter in ransomNote:
            if letter in magazine_letter_frequency.keys() and magazine_letter_frequency[letter] > 0:
                magazine_letter_frequency[letter] -= 1
            else:
                return False
        return True