class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        max_i = -1
        max_val = 0
        for i in range(len(gas)):
            if gas[i] - cost[i] > max_val:
                max_val = gas[i] - cost[i]
                max_i = i

        return max_i