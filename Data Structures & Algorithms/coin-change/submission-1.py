class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None] * (amount + 1)
        dp[0] = 0

        coins = list(filter(lambda x: x <= amount, coins))

        for coin in coins:
            dp[coin] = 1

        if amount == 0:
            return 0

        if amount > 0 and dp[amount] == 1:
            return 1

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] is not None:
                    dp[i] = min(dp[i - coin] + 1, dp[i]) if dp[i] is not None else dp[i - coin] + 1

        return dp[amount] if dp[amount] is not None else -1