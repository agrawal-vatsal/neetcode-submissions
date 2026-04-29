import math

class Solution:

    def is_speed_valid(self, piles, h, speed):
        ans = 0
        for pile in piles:
            ans += math.ceil(pile / speed)

        return ans <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        result = None
        while l <= r:
            mid = (l + r) // 2

            is_speed_valid = self.is_speed_valid(piles, h, mid)

            if is_speed_valid:
                result = min(result, mid) if result is not None else mid
                r = mid - 1
            else:
                l = mid + 1

        return result
