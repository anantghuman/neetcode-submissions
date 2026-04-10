class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_eating_speed = r
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(float(p) / mid)
            if time <= h:
                min_eating_speed = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_eating_speed
        


        