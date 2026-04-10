class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        hm = defaultdict(int)
        for s in strs:
            c = [0] * 26
            for ch in s:
                c[ord(ch) - ord('a')] += 1
            t = tuple(c)
            if t in hm:
                arr[hm[t]].append(s)
            else:
                hm[t] = len(arr)
                arr.append([s])
        return arr