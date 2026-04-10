class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        valid_combos = set()



        def backtracking(index, s, freq):
            if s > target or index >= len(nums):
                return
            if s == target:
                valid_combos.add(tuple(freq))
            backtracking(index + 1, s, freq)
            freq[nums[index]] += 1
            backtracking(index, s + nums[index], freq)
            freq[nums[index]] -= 1

        
        for i in range(len(nums)):
            arr = [nums[i]]
            freq = [0] * 31
            freq[nums[i]] += 1
            backtracking(i, nums[i], freq)

        temp = []
        if target == 0:
            temp.append([])

        for combo in valid_combos:
            t = []
            for i, elem in enumerate(combo):
                for r in range(elem):
                    t.append(i)
            temp.append(t)
        
        return temp