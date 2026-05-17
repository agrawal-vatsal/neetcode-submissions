class Island:
    def __init__(self):
        self.area = 0

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        length = len(grid)
        breadth = len(grid[0])

        def explore_island(grid, i, j, island):
            if i < 0 or j < 0 or i >= length or j >= breadth or grid[i][j] == 0:
                return

            grid[i][j] = 0
            island.area += 1
            explore_island(grid, i + 1, j, island)
            explore_island(grid, i, j + 1, island)
            explore_island(grid, i, j - 1, island)
            explore_island(grid, i - 1, j, island)

        max_area = 0

        for i in range(length):
            for j in range(breadth):
                if grid[i][j] == 1:
                    island = Island()
                    explore_island(grid, i, j, island)
                    max_area = max(max_area, island.area)

        return max_area