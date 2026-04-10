class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, -stone)
        while len(pq) > 1:
            r1 = -heapq.heappop(pq)
            r2 = -heapq.heappop(pq)
            if r1 > r2:
                heapq.heappush(pq, -(r1 - r2))
            elif r2 > r1:
                heapq.heappush(pq, -(r2 - r1))
        return 0 if len(pq) == 0 else -heapq.heappop(pq)
        