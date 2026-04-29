class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_idx = 0
        num_moves = 0

        while curr_idx < len(nums) - 1:
            l = curr_idx + 1
            r = min(curr_idx + nums[curr_idx], len(nums) - 1)
            if r >= len(nums) - 1:
                return num_moves + 1
            curr_max = r
            curr_max_index = curr_idx
            for i in range(l, r + 1):
                if i + nums[i] > curr_max:
                    curr_max = i + nums[i]
                    curr_max_index = i

            curr_idx = curr_max_index
            num_moves += 1

        return num_moves
