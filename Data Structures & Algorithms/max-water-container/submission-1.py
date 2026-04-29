class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        curr_vol = 0

        while i < j:
            new_vol = (j - i) * min(heights[i], heights[j])
            curr_vol = max(curr_vol, new_vol)

            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1

        return curr_vol