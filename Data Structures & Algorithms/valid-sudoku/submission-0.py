class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Row is ONE input
        #Column is the [row][i]
        #a nine by nine box is  CHECK if not isinstance(int)
        seen_row = defaultdict(set) #row number -> values
        seen_col = defaultdict(set) #column number -> values
        seen_square = defaultdict(set)
        
        for row_idx, row in enumerate(board):
            for col_idx, num in enumerate(row):
                if num.isdigit():
                    #Check for rows by seeing if  the ROW index has the same value
                    if num in seen_row[row_idx]: 
                        return False
                    seen_row[row_idx].add(num) 
                    
                    #Check for columns by seeing if the COLUMN value hasthe same value
                    if num in seen_col[col_idx]: 
                        return False
                    seen_col[col_idx].add(num)

                    #Check for squares
                    square = ((row_idx // 3) * 3 + (col_idx // 3))
                    if num in seen_square[square]: 
                        return False
                    seen_square[square].add(num)
        return True


            