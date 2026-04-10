class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []
        for s in strs:
            arr.append(str(len(s)) + '#')
            arr.append(s)
        return ''.join(arr)

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        print(s)
        while i < len(s):
            val = 0
            while s[i] != '#':
                val *= 10
                val += ord(s[i]) - ord('0')
                i += 1
            i += 1
            arr.append(s[i : i + val])
            i += val
        return arr
        
