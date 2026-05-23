class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        i, maxFreq, ans = 0, 0, 0

        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1

            maxFreq = max(maxFreq, count[s[j]])

            invalidCharCount = j - i + 1 - maxFreq

            if invalidCharCount > k:
                count[s[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)

        return ans