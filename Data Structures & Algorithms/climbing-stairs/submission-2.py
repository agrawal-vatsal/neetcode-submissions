from collections import deque
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        q = deque([1, 2])

        for i in range(3, n + 1):
            q.append(q[0] + q[1])
            q.popleft()

        return q[1]