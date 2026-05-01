from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        ans = 0
        handled_set = set()

        while j < len(s):
            if s[j] not in handled_set:
                ans = max(ans, j - i + 1)
                handled_set.add(s[j])
                j += 1
                continue
        
            while s[j] in handled_set:
                handled_set.discard(s[i])
                i += 1

        return ans

        