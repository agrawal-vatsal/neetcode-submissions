class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = 0

        i = 0
        while i <= len(nums):
            total_sum += i
            i += 1

        return total_sum - sum(nums)