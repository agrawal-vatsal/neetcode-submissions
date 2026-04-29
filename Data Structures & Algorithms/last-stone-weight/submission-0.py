import heapq
class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            t = heapq.heappop(stones)
            st = heapq.heappop(stones)

            if t != st:
                diff = t - st if t < st else st - t
                heapq.heappush(stones, diff)

        if len(stones) == 1:
            return -stones[0]

        return 0

