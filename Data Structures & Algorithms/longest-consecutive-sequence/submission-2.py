class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        ans = 1
        curr = 0

        for num in num_set:
            if num - 1 in num_set:
                continue
            curr = 1
            num_in_ques = num + 1
            while num_in_ques in num_set:
                curr += 1
                ans = max(curr, ans)
                num_in_ques += 1
        return ans
