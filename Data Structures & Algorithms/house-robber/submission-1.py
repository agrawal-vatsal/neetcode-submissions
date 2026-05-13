[6, 2, 2, 5, 2, 5, 5]
6, 2, 8, 11, 10, 16, 15

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        helper_arr = [nums[0], nums[1]]
        max_till_now = nums[0]

        for i in range(2, len(nums)):
            helper_arr.append(max_till_now + nums[i])
            max_till_now = max(max_till_now, helper_arr[-2])

        return max(helper_arr[-1], helper_arr[-2])