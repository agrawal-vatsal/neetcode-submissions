from collections import deque
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        q = deque([1, 2])

        for i in range(3, n + 1):
            front = q[0]
            back = q[1]
            new_ele = q.append(q[0] + q[1])
            q.popleft()

        return q[1]
