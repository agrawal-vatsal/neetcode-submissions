from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = defaultdict(list)

        for i in range(len(nums)):
            data[nums[i]].append(i)

        for i in range(len(nums)):
            current_num = nums[i]
            remaining_sum = target - current_num

            if remaining_sum in data:
                if current_num == remaining_sum and len(data[current_num]) == 1:
                    continue

                return [i, data[remaining_sum][-1]]
        return None
        
