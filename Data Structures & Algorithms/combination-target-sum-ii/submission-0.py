class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = set()
        t = [0] * 51

        def backtrack(s, i):
            if s == target:
                combs.add(tuple(t))
                return
            if s > target or i >= len(candidates):
                return
            
            backtrack(s, i + 1)
            t[candidates[i]] += 1
            backtrack(s + candidates[i], i + 1)
            t[candidates[i]] -= 1

        for i in range(len(candidates)):
            t[candidates[i]] += 1
            backtrack(candidates[i], i + 1)
            t[candidates[i]] -= 1

        arr = []
        print(len(combs))
        for comb in combs:
            t = []
            for i in range(len(comb)):
                for c in range(comb[i]):
                    t.append(i)

            arr.append(t)
                    
        return arr