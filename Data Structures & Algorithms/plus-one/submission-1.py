class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        print(str(digits))
        value = int("".join(map(str,digits)))
        return [digit for digit in str(value + 1)]