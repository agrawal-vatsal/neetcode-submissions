class Solution:
    def dp(self, i, j, matrix, dp_matrix):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            return -1

        if dp_matrix[i][j] is not None:
            return dp_matrix[i][j]
        
        up = matrix[i - 1][j] if i > 0 else -1
        down = matrix[i + 1][j] if i < len(matrix) - 1 else -1
        left = matrix[i][j - 1] if j > 0 else -1
        right = matrix[i][j + 1] if j < len(matrix[0]) - 1 else -1
        
        score = 1
        
        if matrix[i][j] < up:
            score = max(score, self.dp(i - 1, j, matrix, dp_matrix) + 1)

        if matrix[i][j] < down:
            score = max(score, self.dp(i + 1, j, matrix, dp_matrix) + 1)

        if matrix[i][j] < left:
            score = max(score, self.dp(i, j - 1, matrix, dp_matrix) + 1)

        if matrix[i][j] < right:
            score = max(score, self.dp(i, j + 1, matrix, dp_matrix) + 1)

        dp_matrix[i][j] = score
        return score


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:        
        r, c = len(matrix), len(matrix[0])
        dp_matrix = [[None for _ in range(c)] for _ in range(r)]

        for i in range(r):
            for j in range(c):
                self.dp(i, j, matrix, dp_matrix)

        print(dp_matrix)

        ans = 0
        for i in range(r):
            for j in range(c):
                ans = max(ans, dp_matrix[i][j])

        return ans
