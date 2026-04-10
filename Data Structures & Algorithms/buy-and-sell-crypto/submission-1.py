class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_min = int(1e5)
        m = 0
        for n in prices:
            running_min = min(running_min, n)
            m = max(m, n - running_min)
        return m