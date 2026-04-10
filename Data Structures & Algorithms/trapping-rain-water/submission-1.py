class Solution:
    def trap(self, height: List[int]) -> int:
        m = 0
        left_highest = [0 for _ in range(len(height))]
        right_highest = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            left_highest[i] = max(left_highest[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            right_highest[i] = max(right_highest[i + 1], height[i + 1])

        for i in range(len(height)):
            m += max(0, min(left_highest[i], right_highest[i]) - height[i])

        return m
        