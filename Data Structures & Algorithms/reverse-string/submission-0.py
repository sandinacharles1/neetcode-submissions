class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead. Swap front and back
        """
        left_ptr, right_ptr = 0, len(s) - 1
        
        while left_ptr < right_ptr:
            right_value = s[right_ptr] #Stores the value
            left_value = s[left_ptr]

            s[right_ptr] = left_value #Replace the value using its actual index
            s[left_ptr] = right_value

            left_ptr += 1
            right_ptr -= 1