class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = [set() for i in range(9)]
        col_seen = [set() for i in range(9)]
        square_seen = [set() for i in range(9)]

        for row in range(9):
            for col in range(9):
                square_index = row // 3 * 3 + col//3
                value = board[row][col]

                if value != "." and value in row_seen[row]:
                    return False 
                if value != "." and value in col_seen[col]:
                    return False
                if value != "." and value in square_seen[square_index]:
                    return False

                col_seen[col].add(value)
                row_seen[row].add(value)
                square_seen[row //3 * 3 + col//3].add(value)

        return True