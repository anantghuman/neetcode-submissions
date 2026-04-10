class Solution:
    def countSubstrings(self, s: str) -> str:
        l = 0
        def check(i, j):
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                count += 1
            return count

        for i in range(len(s)):
            l += check(i, i) + check(i, i + 1)
    
        return l