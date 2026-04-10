class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        m = 0
        found = set()
        for ch in s:
            while ch in found:
                found.remove(s[left])
                left += 1
            found.add(ch)
            m = max(m, len(found))
        return m

        