class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        heap = [(grid[0][0], 0, 0)]
        visited = set((0, 0))

        while heap:
            t, r, c = heapq.heappop(heap)

            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if newR < 0 or newC < 0 or newR == N or newC == N or (newR, newC) in visited:
                    continue

                heapq.heappush(heap, (max(t, grid[newR][newC]), newR, newC))
                visited.add((newR, newC))
        