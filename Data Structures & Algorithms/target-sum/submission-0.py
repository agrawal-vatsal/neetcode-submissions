from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            temp_dp = defaultdict(int)
            for total, count in dp.items():
                temp_dp[total + num] += count
                temp_dp[total - num] += count
            dp = temp_dp

        return dp[target]
