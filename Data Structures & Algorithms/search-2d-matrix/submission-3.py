class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        (1) Loop through the first values of every list matrix[i][0]
        THIS WOULD BE AT MOST LOG(N). NOT log m*n

        (0) Start at the middle len(matrix) / 2. Get the first number num[mid][0]
        (1) CHECK the beginning and end if the number is in that row. If it is, 
        BREAK out of the loop of checking if its in another row
        (2) If the number is less than [0], recalculate the middle from the left
        (3) If the number is greater than [-1], recalculate the middle from the 
        right
        
        (4) Do binary search in the row itself and return true when its found
        (5) If it is false, then return false at the end
        '''
        left_ptr, right_ptr = 0, len(matrix) - 1
        #Edge case for empty matrix:
        if not matrix or not matrix[0]:
            return False
        #1. Loop through the LISTS
        while left_ptr <= right_ptr:
            #Find the middle row 
            middle_ptr  = int((right_ptr + left_ptr) / 2)
            
            #Find the first and last values
            middle_row = matrix[middle_ptr]
            first_number, last_number = middle_row[0], middle_row[-1]
            
            if target in range(first_number, last_number + 1):
                break #break the nearest loop
            elif target > last_number:
                left_ptr = middle_ptr + 1
            else:
                right_ptr = middle_ptr - 1

        #2. Loop inside the list
        left_ptr, right_ptr = 0, len(middle_row) - 1
        while left_ptr <= right_ptr:
            middle = int((right_ptr + left_ptr) / 2)
            middle_value = middle_row[middle]
            
            if target == middle_value:
                return True
            elif target > middle_value:
                left_ptr = middle + 1
            else:
                right_ptr = middle - 1
        
        return False

        