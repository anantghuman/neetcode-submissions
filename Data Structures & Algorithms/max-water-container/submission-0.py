class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        m = 0
        while left < right:
            minimum = min(heights[left], heights[right])
            m = max(m, (right - left) * minimum)
            if heights[left] == minimum == heights[right]:
                left += 1
                right -= 1
            elif heights[left] == minimum:
                left += 1
            else:
                right -= 1

        return m