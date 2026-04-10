class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        s = nums[0]
        for n in nums[1:]:
            s = max(s + n, n)
            m = max(m, s)
        return m