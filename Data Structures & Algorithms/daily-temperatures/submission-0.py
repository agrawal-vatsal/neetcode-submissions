class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans_array = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                top_item, idx = stack.pop()
                ans_array[idx] = i - idx

            stack.append((temperatures[i], i))

        return ans_array

