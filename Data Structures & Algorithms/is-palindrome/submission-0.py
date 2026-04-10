class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = []
        for ch in s:
            if ch.isalnum():
                arr.append(ch)
        s = ''.join(arr)
        start = 0
        end = len(s) - 1
        print(s)
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True  