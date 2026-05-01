from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        ans = 0
        data = defaultdict(int)

        for j in range(len(s)):
            while data[s[j]] == 1:
                data[s[i]] -= 1
                i += 1

            data[s[j]] += 1
            ans = max(ans, j - i + 1)

        return ans

        