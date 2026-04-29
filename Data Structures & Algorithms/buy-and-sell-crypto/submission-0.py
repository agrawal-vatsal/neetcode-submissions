class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_till_now = [0] * len(prices)

        max_item = 0
        for i in range(len(prices) - 1, -1, -1):
            max_till_now [i] = max_item
            max_item = max(prices[i], max_item)

        max_item = 0

        for a, b in zip(prices, max_till_now):
            max_item = max(b - a, max_item)

        return max_item