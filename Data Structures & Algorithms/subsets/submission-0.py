class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        
        def backtrack(temp, index):
            if index == len(nums):
                arr.append([t for t in temp])
                return
            backtrack(temp, index + 1)
            temp.append(nums[index])
            backtrack(temp, index + 1)
            temp.pop()
            
        for i in range(len(nums)):
            temp = [nums[i]]
            backtrack(temp, i + 1)


        return arr    