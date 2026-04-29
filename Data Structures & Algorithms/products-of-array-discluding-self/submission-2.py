class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        prod = 1
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod *= num
        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_count: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res

        