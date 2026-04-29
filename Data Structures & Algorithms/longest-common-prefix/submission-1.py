class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]
            common_till = min(len(ans), len(word))

            for j in range(common_till):
                if word[j] != ans[j]:
                    common_till = j
                    break

            ans = ans[:common_till]

        return ans
