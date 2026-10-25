class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        for index, letters_tuple in enumerate(zip(*strs)): #Respective letters of al; strings
            reference_char = letters_tuple[0]
            if all(letter == reference_char for letter in letters_tuple):
                output+= f"{reference_char}"
            else:
                break
        return output