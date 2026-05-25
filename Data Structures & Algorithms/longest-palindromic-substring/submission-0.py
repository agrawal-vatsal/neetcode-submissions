class Solution:
    def maxOddCharPalindrome(self, s):
        maxSize = 0
        maxLenIdx = -1

        for i in range(len(s)):
            for j in range(len(s) // 2):
                if i - j < 0 or i + j >= len(s):
                    break
                if s[i - j] != s[i + j]:
                    break

                if maxSize <= j:
                    maxSize = j
                    maxLenIdx = i

        return s[maxLenIdx - maxSize:maxLenIdx + maxSize + 1]

    def maxEvenCharPalindrome(self, s):
        maxSize = 0
        maxLenIdx = 0

        for k in range(len(s) - 1):
            i = k + 0.5
            for l in range(len(s) // 2):
                j = l + 0.5
                if i - j < 0 or i + j >= len(s):
                    break
                if s[int(i - j)] != s[int(i + j)]:
                    break
                if maxSize <= j:
                    maxSize = j
                    maxLenIdx = i

        return s[int(maxLenIdx - maxSize):int(maxLenIdx + maxSize) + 1]

    def longestPalindrome(self, s: str) -> str:
        oddLength = self.maxOddCharPalindrome(s)
        evenLength = self.maxEvenCharPalindrome(s)
        if len(oddLength) > len(evenLength):
            return oddLength

        return evenLength

        