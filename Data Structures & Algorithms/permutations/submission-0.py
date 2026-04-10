class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        visited = [-11] * len(nums)
        def dfs(nums, temp):
            if len(temp) == len(nums):
                t = []
                for elem in temp:
                    t.append(elem)
                arr.append(t)
                return
            for i in range(len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    dfs(nums, temp)
                    temp.pop()
        dfs(nums, [])
        return arr