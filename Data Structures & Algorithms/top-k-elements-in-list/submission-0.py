class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        freq = [[i, []] for i in range(len(nums) + 1)]

        for i in count.keys():
            f = count[i]
            freq[f][1].append(i)

        arr = []
        for i in range(len(nums), 0, -1):
            t = freq[i][1]
            for elem in t:
                arr.append(elem)
                k-= 1
                if k == 0:
                    return arr
        return arr
        