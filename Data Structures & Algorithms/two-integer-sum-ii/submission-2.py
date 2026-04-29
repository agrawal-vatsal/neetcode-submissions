class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            current_sum = numbers[i] + numbers[j]
            if target == current_sum:
                return [i + 1, j + 1]
            if target > current_sum:
                i += 1
            else:
                j -= 1
        return [None, None]