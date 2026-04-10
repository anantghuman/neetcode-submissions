class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in s:
            if n - 1 in s:
                continue
            i = 1
            while n + i in s:
                i += 1
            longest = max(longest, i)
        return longest

        