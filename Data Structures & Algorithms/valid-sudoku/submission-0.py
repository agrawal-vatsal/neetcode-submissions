class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_data = [set() for _ in range(9)]
        grid_data = [set() for _ in range(9)]
        for i in range(9):
            row_data = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_data:
                    return False
                if board[i][j] in col_data[j]:
                    return False
                grid_i = i // 3
                grid_j = j // 3
                grid_no = grid_i * 3 + grid_j
                if board[i][j] in grid_data[grid_no]:
                    return False
                row_data.add(board[i][j])
                col_data[j].add(board[i][j])
                grid_data[grid_no].add(board[i][j])
        return True

                
                