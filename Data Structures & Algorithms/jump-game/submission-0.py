class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        for i in range(len(nums)):
            jump = max(jump - 1, nums[i])
            if jump == 0 and len(nums) - 1 != i:
                return False
        return True
