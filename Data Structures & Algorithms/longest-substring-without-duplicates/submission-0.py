class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0

        max_len = 0
        chars = set()

        while i < len(s):
            while s[i] in chars:
                chars.remove(s[j])
                j += 1

            chars.add(s[i])

            max_len = max(max_len, len(chars))
            i += 1

        return max_len
                