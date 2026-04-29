from collections import deque
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        q = deque([cost[0], cost[1]])
        for i in range(2, len(cost)):
            new_cost = cost[i] + min(q[0], q[1])
            q.append(new_cost)
            q.popleft()
        return min(q)

        