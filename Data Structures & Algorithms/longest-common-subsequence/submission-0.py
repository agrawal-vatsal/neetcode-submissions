class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        arr = []

        for i in range(n):
            arr.append([])
            for j in range(m):
                arr[i].append(0)

        arr[0][0] = 1 if text1[0] == text2[0] else 0
        for j in range(1, m):
            match_score = 1 if text1[0] == text2[j] else 0
            arr[0][j] = max(arr[0][j - 1], match_score)

        for i in range(1, n):
            match_score = 1 if text1[i] == text2[0] else 0
            arr[i][0] = max(arr[i - 1][0], match_score)

        for i in range(1, n):
            for j in range(1, m):
                match_score = 1 if text1[i] == text2[j] else 0
                arr[i][j] = max(arr[i - 1][j - 1] + match_score, arr[i - 1][j], arr[i][j - 1])

        return arr[-1][-1]