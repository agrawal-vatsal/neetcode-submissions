class Solution:
    def markIsland(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return

        if grid[i][j] == "1":
            grid[i][j] = "0"
            self.markIsland(grid, i + 1, j)
            self.markIsland(grid, i, j + 1)
            self.markIsland(grid, i - 1, j)
            self.markIsland(grid, i, j - 1)


    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    self.markIsland(grid, i, j)
        
        return ans