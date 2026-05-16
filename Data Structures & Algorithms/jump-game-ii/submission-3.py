class Solution:
    def jumpable(self, nums: List[int], start_idx: int, end_idx: int) -> int:
        ans = start_idx + nums[start_idx]
        end_idx = min(end_idx, len(nums) - 1)
        for i in range(start_idx, end_idx + 1):
            ans = max(ans, i + nums[i])

        return ans

    def jump(self, nums: List[int]) -> int:
        count = 1
        i = 0
        max_reachable = nums[0]

        if len(nums) == 1:
            return 0

        if max_reachable >= (len(nums) - 1):
            return 1

        while True:
            new_max_reachable = self.jumpable(nums, i + 1, max_reachable)
            count += 1
            if new_max_reachable >= (len(nums) - 1):
                return count

            i = max_reachable
            max_reachable = new_max_reachable

        return -1
