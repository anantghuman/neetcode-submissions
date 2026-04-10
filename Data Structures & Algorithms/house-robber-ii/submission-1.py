class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(nums):
            rob1, rob2 = 0, 0
            for i in range(len(nums)):
                t = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = t

            return rob2
        return max(nums[0], rob_helper(nums[1:]), rob_helper(nums[:-1]))