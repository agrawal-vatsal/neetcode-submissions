class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data_set = set(nums)

        ans = 0

        for item in nums:
            if item - 1 in data_set:
                continue

            size = 1
            a = item

            while a + 1 in data_set:
                a = a + 1
                size += 1

            ans = max(ans, size)

        return ans