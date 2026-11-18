class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #We don't want to know while we're in the middle-- We want to know before we start. So we can keep track of rows and columns. Doing that in separate hashsets is O(m*n) space though. We could possibly use the pre-existing matrix as a way to store the info. Like temporary markers on the first column for each column, and on the first row for each row. So we use the first row as reference on where to put 0s.

        #Issue. If theres a 3 in column 1 and we replace that (0,0) cell with 0, it might inappropriately think its refrencing the row when we pass later. Same for the opposite. Since we are using the first rows and the first columns as information storage, we lose information about the actual rows itself since it gets overridden. So, how will we make sure that first cell is defined as EITHER row storage, or column storage? And how will we remember which its for? to get rid of this issue, we could just keep note about if first row had a zero, or if the first column had a 0 so we dont have to worry about interpreting the 0 cell. Plus, the other cells only care about cells + 1
        first_row_zero = False
        first_col_zero = False
        
        #First pass, mark the zeros. 
        for row_num, row in enumerate(matrix):
            for col_num, value in enumerate(row):
                if value == 0: 
                    if row_num == 0: first_row_zero = True
                    if col_num == 0: first_col_zero = True
                    matrix[row_num][0] = 0
                    matrix[0][col_num] = 0

        #Second pass, read the zeros. AFTER THAT(bcz we dont wnana lose info) update based  first_row & first_col. We HAVE to skip the first row/column though, because it might read from the top left cell, since it might be ambigiouso
        for row_num in range(1, len(matrix)):
            row = matrix[row_num]
            for col_num in range(1,len(row)):
                value = row[col_num]
                if matrix[row_num][0] == 0 or matrix[0][col_num] == 0:
                     matrix[row_num][col_num] = 0
        
        #Third pass... (this may be a lot, it can be optimized. Technically (O(n*m) time though))
        if first_row_zero == True: matrix[0] = [0] * len(matrix[0])
        if first_col_zero == True:
            for row in matrix:
                row[0] = 0