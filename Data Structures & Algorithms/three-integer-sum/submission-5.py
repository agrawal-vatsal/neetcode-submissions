class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum > 0:
                    k -= 1
                elif curr_sum < 0:
                    j += 1
                else:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1

        return list(ans)
