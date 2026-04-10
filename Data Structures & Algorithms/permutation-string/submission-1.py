class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1 = [0 for _ in range(26)]
        arr2 = [0 for _ in range(26)]

        for ch in s1:
            arr1[ord(ch) - ord('a')] += 1
        
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            arr2[ord(s2[i]) - ord('a')] += 1
        if arr1 == arr2:
            return True
        
        for i in range(len(s1), len(s2)):
            arr2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            arr2[ord(s2[i]) - ord('a')] += 1
            if arr1 == arr2:
                return True
        return False

        