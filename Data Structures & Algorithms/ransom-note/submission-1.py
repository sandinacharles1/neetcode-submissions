class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letter_frequencies = [0] * 26
        for letter in magazine: magazine_letter_frequencies[ord('a') - ord(letter)] += 1

        for letter in ransomNote: 
            alphabet_index = ord('a') - ord(letter)
            if magazine_letter_frequencies[alphabet_index] < 1:
                return False
            magazine_letter_frequencies[ord('a') - ord(letter)] -= 1 
        return True