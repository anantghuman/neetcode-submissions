class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0] + nums[2], nums[1])
        
        arr = []
        arr.append(nums[0])
        arr.append(nums[1])
        arr.append(max(nums[0] + nums[2], nums[1]))
        for i in range (3, n):
            arr.append(max(arr[i - 2] + nums[i], max(arr[i-1], arr[i-3] + nums[i])))
       
        return arr[n - 1]