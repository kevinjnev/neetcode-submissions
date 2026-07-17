class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #have sets for each row, column, and 3x3 grid square to check for duplicates
        rowsets = defaultdict(set)
        colsets = defaultdict(set)
        gridsets = defaultdict(set)

        #iterate through every square, checking the row, column, and 3x3 grid that it is in.
        #if it is already there it is a duplicate and returns false.
        #otherwise it keeps going and if it is a number it adds itself to the sets of the
        #column, row, and grid it is in.

        #The grids are 3x3 and there are 9 on the board, so if you divide the row and column
        #of a square by 3 you will get either 0, 1, or 2 (int. division). You can use this as
        #the key for the hashset that holds the grid duplicates so you can access the correct
        #set.
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowsets[r]
                    or board[r][c] in colsets[c]
                    or board[r][c] in gridsets[(r // 3, c // 3)]):
                    return False

                colsets[c].add(board[r][c])
                rowsets[r].add(board[r][c])
                gridsets[(r // 3, c // 3)].add(board[r][c])

        return True
