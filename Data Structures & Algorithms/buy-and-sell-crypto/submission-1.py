class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_till_now = 101

        for price in prices:
            if min_till_now < price:
                ans = max(ans, price - min_till_now)
            else:
                min_till_now = price

        return ans