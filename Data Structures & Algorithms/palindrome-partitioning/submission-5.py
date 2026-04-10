class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        def palindrome(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                dp[i][j] = True
                i -= 1
                j += 1


        for start in range(len(s)):
            palindrome(start, start)
            palindrome(start, start + 1)


        ret = []
        def p(start_index, arr):
            if start_index == len(s):
                ret.append([k for k in arr])
                return
            for i in range(start_index, len(s)):
                if dp[start_index][i]:
                    arr.append(s[start_index:i + 1])
                    p(i + 1, arr)
                    arr.pop()
            
            
        print(dp)

        p(0, [])
        return ret

        


        