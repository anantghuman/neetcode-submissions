class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hm = defaultdict(list)

        for source, dest, time in times:
            hm[source].append((dest, time))

        times = [float('inf')] * (n + 1)

        q = deque()
        q.append((k, 0))

        times[k] = 0
        times[0] = 0

        while q:
            for _ in range(len(q)):
                curr, time = q.popleft()
                for v, t in hm[curr]:
                    print(v)
                    if time + t < times[v]:
                        times[v] = time + t
                        q.append((v, times[v]))
                

        t = max(times) 
        if math.isinf(t):
            return -1
        else:
            return t