from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 1
        count = defaultdict(int)
        count[s[i]] = 1
        ans = 1
        sum_counts = sum(count.values())
        max_count = max(count.values())

        while j < len(s):
            diff = sum_counts - max_count
            if diff <= k:
                ans = max(sum_counts, ans)
                count[s[j]] += 1
                j += 1
            else:
                count[s[i]] -= 1
                i += 1
            sum_counts = sum(count.values())
            max_count = max(count.values())

        sum_counts = sum(count.values())
        max_count = max(count.values())
        if sum_counts - max_count <= k:
            ans = max(ans, sum_counts)

        return ans
