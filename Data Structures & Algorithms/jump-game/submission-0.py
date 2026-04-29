class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        curr = 0

        while curr <= max_reachable and curr < len(nums):
            new_reachable = curr + nums[curr]
            max_reachable = max(max_reachable, new_reachable)
            curr += 1

        print(max_reachable)
        return max_reachable >= (len(nums) - 1)
            