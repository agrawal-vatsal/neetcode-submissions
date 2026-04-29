import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin_value in coins:
                if coin_value > i:
                    continue
                coins_needed = 1 + dp[i - coin_value]
                dp[i] = min(dp[i], coins_needed)

        return dp[amount] if dp[amount] != math.inf else -1