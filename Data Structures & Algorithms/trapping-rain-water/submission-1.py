class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [height[0]]

        for i in range(1, len(height)):
            left_max.append(max(height[i], left_max[-1]))

        right_max = [height[-1]]

        for i in range(len(height) - 2, -1, -1):
            right_max.append(max(height[i], right_max[-1]))

        right_max = right_max[::-1]

        ans = 0
        for i in range(len(height)):
            ans += min(right_max[i], left_max[i]) - height[i]

        return ans