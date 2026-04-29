class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        
        row_0 = False
        col_0 = False

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    if r == 0:
                        row_0 = True
                    else:
                        matrix[0][c] = 0
                    if c == 0:
                        col_0 = True
                    else:
                        matrix[r][0] = 0

        for r in range(1, n):
            for c in range(1, m):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if col_0:
            for r in range(n):
                matrix[r][0] = 0

        if row_0:
            for c in range(m):
                matrix[0][c] = 0