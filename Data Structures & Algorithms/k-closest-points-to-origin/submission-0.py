class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x, y in points:
            heapq.heappush(pq, (((x**2)+(y**2)) ** .5, x, y))
        arr = []
        for _ in range(k):
            t, x, y = heapq.heappop(pq)
            arr.append([x, y])
        return arr
        