class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #ROW
        for row in board:
            seen = set()
            for cell in row:
                if cell != '.' and cell in seen:
                    return False
                seen.add(cell)
        
        #COl
        for i in range(9):
            seen = set()
            for j in range(9):
                cell = board[j][i]
                if cell != '.' and cell in seen:
                    return False
                seen.add(cell)
        
        #3*3

        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for i in range(box_row*3, box_row*3+3):
                    for j in range(box_col*3, box_col*3+3):
                        cell = board[i][j]
                        if cell != '.' and cell in seen:
                            return False
                        seen.add(cell)
        
        return True







