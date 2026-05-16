class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        high = ans

        for i in range(1, len(nums)):
            if high < 0:
                high = 0

            high += nums[i]
            ans = max(ans, high)

        return ans