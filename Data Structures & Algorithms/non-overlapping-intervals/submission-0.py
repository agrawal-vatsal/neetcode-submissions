class Solution:
    def __init__(self, start: int=None, end: int=None):
        self.start = start
        self.end = end

    def __gt__(self, another) -> bool:
        if self.start != another.start:
            return self.start > another.start

        return self.end > another.end

    def overlap(self, another) -> bool:
        return self.end > another.start

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = [Solution(a[0], a[1]) for a in intervals]
        intervals.sort()

        n = 0

        curr = intervals[0]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if not curr.overlap(interval):
                curr = interval
            else:
                n += 1
                curr = curr if curr.end < interval.end else interval

        return n
            