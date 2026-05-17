"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [x.start for x in intervals]
        end = [x.end for x in intervals]

        start.sort()
        end.sort()

        count, max_count = 0, 0
        i, j = 0, 0

        while j < len(start):
            if i < len(start) and start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            
            max_count = max(max_count, count)

        return max_count

        
        


