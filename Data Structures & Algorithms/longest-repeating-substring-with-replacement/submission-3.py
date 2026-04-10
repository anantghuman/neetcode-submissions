from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        left = 0
        max_count = 0
        longest = 0
        
        for right in range(len(s)):
            hm[s[right]] += 1
            max_count = max(max_count, hm[s[right]])
            
            while (right - left + 1) - max_count > k:
                hm[s[left]] -= 1
                left += 1
                
            longest = max(longest, right - left + 1)
            
        return longest
