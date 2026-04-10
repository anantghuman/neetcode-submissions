class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []

        def dfs(i, curr):
            if i == len(nums):
                arr.append([k for k in curr])
                return 
            if not (len(curr) != 0 and curr[-1] == nums[i]):
                dfs(i + 1, curr)
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
   
        dfs(0, [])
        return arr