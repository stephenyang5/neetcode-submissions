class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for row in range(9):
            col_seen = set()
            for col in range(9):
                value = board[row][col]
                if value in col_seen and value != ".":
                    return False
                col_seen.add(value)
        
        for col in range(9):
            col_seen = set()
            for row in range(9):
                value = board[row][col]
                if value in col_seen and value != ".":
                    return False
                col_seen.add(value)

        for square in range(9):
            square_seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    value = board[row][col]
                    if value in square_seen and value != ".":
                        return False
                    square_seen.add(value)
        return True