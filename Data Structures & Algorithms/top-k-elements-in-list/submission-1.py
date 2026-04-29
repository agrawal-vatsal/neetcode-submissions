from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        h = []
        for t, v in c.items():
            h.append((-v, t))

        heapq.heapify(h)
        ans = []

        while len(ans) < k:
            ans.append(heapq.heappop(h)[1])

        return ans

