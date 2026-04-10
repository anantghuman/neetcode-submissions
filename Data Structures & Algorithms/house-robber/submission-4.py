class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []
        if len(nums) <= 2:
            return max(nums)
        for i in range(len(nums)):
            if i < 2:
                dp.append(nums[i])
            elif i == 2:
                dp.append(max(nums[i - 1], nums[i - 2] + nums[i]))
            else:
                dp.append(max(dp[i - 1], dp[i - 2] + nums[i], dp[i - 3] + nums[i]))
        return dp[-1]
        
            
            
        