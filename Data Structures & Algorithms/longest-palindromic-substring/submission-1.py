class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 0
        start = 0
        def check(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - i - 1

        for i in range(len(s)):
            temp_start, temp_length = check(i, i)
            if temp_length > l:
                start = temp_start
                l = temp_length
            
            temp_start, temp_length = check(i, i + 1)
            if temp_length > l:
                start = temp_start
                l = temp_length

        return s[start: start + l]