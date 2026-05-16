[1, 2, 3, 4]
[2, 2, 4, 1]
[-1, 0, -1,3]

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            if gas[i] - cost[i] > 0:
                return i

        return -1