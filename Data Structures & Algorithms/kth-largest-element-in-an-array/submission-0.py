class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            pq.append(-n)
        heapq.heapify(pq)
        for _ in range(k - 1):
            heapq.heappop(pq)
        return -heapq.heappop(pq)

        