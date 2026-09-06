class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #1. Start from beginning and end indices
        left = 0
        right = len(numbers) - 1

        #2. Move pointers in on eachother respectively, if the number is too big, decrease the value of the bigger (right) pointer, if its too small then increase the smaller (left pointer) then retrun the indices with 1-index
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1 
            elif numbers[left] + numbers[right] < target:
                left += 1
            else: 
                return [left + 1,right + 1]
        return []
                



        