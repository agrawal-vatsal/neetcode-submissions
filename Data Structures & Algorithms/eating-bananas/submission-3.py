class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def valid_pile(arr, k, h):
            total = 0
            for item in arr:
                time_taken = math.ceil(item / k)
                total += time_taken

            return total <= h

        lo, hi = 0, max(piles)

        while lo <= hi:
            if lo == hi:
                return lo

            mid = (lo + hi) // 2
            if valid_pile(piles, mid, h):
                hi = mid
            else:
                lo = mid + 1

        return -1
            
        