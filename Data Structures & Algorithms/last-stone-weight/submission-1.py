import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 != stone2:
                heapq.heappush(stones, stone1 - stone2)

        return stones[0] * -1 if len(stones) > 0 else 0
