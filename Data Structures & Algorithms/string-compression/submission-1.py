class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed_string = ""
        index, count, length = 0, 0, len(chars) - 1
        
        while index <= length:
            count += 1
            
            if index == length or chars[index] != chars[index + 1]:
                if count == 1: compressed_string += f"{chars[index]}"
                else: compressed_string += f"{chars[index]}{count}"
                
                count = 0                
            
            index += 1
        
        for index, item in enumerate(compressed_string): chars[index] = item
        return len(compressed_string)
