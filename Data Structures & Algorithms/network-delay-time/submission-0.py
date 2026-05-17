import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for s, d, w in times:
            edges[s].append((d, w))

        visited = set()
        cost = [(0, k)]
        ans = 0
        
        while cost:
            w1, n1 = heapq.heappop(cost)

            if n1 in visited:
                continue

            visited.add(n1)

            for n2, w2 in edges[n1]:
                heapq.heappush(cost, (w2 + w1, n2))

            ans = max(ans, w1)

        return ans if len(visited) == n else -1
            
