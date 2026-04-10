class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = defaultdict(list)
        arr = []

        ch = 0
        for i in range(2, 10):
            j = 4 if i == 7 or i == 9 else 3
            for _ in range(0, j):
                hm[chr(i + ord('0'))].append(chr(ord('a') + ch))
                ch += 1

        def dfs(i, curr):
            if i == len(digits):
                arr.append(''.join(curr))
                return
            for n in hm[digits[i]]:
                curr.append(n)
                dfs(i + 1, curr)
                curr.pop()

            print(curr)

        if len(digits) != 0:
            dfs(0, [])
        return arr