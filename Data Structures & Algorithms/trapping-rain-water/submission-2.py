class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        s = 0
        for i in range(1, n):
            left[i] = max(height[i - 1], left[i - 1])
            right[n - i - 1] = max(height[n - i], right[n - i])
            
        for i in range(n):
            s += max(0, min(left[i], right[i]) - height[i])

        return s
        