import math

class Solution:

    def isSolutionValid(self, piles: List[int], h: int, speed: int) -> bool:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)

        return h >= hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximumPile = max(piles)
        if h == len(piles):
            return maximumPile

        if h >= sum(piles):
            return 1

        l, r = 1, maximumPile

        while l <= r:
            if l == r:
                return l
            mid = (l + r) // 2
            if self.isSolutionValid(piles, h, mid):
                r = mid
            else:
                l = mid + 1

        return -1
