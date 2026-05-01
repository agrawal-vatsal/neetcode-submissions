class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        count = {}
        ans, max_freq = 0, 0

        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1

            max_freq = max(max_freq, count[s[j]])

            invalid_char_count = j - i + 1 - max_freq

            if invalid_char_count > k:
                count[s[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)

        return ans
