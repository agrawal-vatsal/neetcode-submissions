class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_left = [1] * len(nums)
        arr_right = [1] * len(nums)

        for i in range(1, len(nums)):
            arr_left[i] = arr_left[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            arr_right[i] = arr_right[i + 1] * nums[i + 1]

        ans = [0] * len(nums)

        ans[0] = arr_right[0]
        ans[len(nums) - 1] = arr_left[len(nums) - 1]

        for i in range(1, len(nums) - 1):
            ans[i] = arr_left[i] * arr_right[i]

        return ans