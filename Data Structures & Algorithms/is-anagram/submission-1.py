class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hm = defaultdict(int)
        hm2 = defaultdict(int)
        for ch1, ch2 in zip(s, t):
            hm[ch1] += 1
            hm2[ch2] += 1

        return hm == hm2
