class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        pq = []
        for i, f in enumerate(freq):
            if f != 0:
                pq.append((-f, chr(i + ord('A'))))
        print(pq)
        heapq.heapify(pq)
        current_not_allowed = set()
        not_allowed_order = deque()
        cycles = 0
        while pq:
            t = []
            while (len(t) == 0 or t[-1][1] in current_not_allowed) and len(pq) > 0 :
                t.append(heapq.heappop(pq))
            if len(not_allowed_order) < n and t[-1][1] not in current_not_allowed:
                #print(cycles, t[-1], 'less than n')
                current_not_allowed.add(t[-1][1])
                not_allowed_order.append(t[-1][1])
                temp = (t[-1][0] + 1, t.pop()[-1])
                if temp[0] != 0:
                    heapq.heappush(pq, temp)
            elif t[-1][1] not in current_not_allowed:
                #print(cycles, t[-1], 'prev kicked out')
                current_not_allowed.add(t[-1][1])
                not_allowed_order.append(t[-1][1])
                if len(not_allowed_order) > n:
                    r = not_allowed_order.popleft()
                    if r != '0':
                        current_not_allowed.remove(r)
                
                temp = (t[-1][0] + 1, t.pop()[-1])
                if temp[0] != 0:
                    heapq.heappush(pq, temp)
            else:
                #print('not allowed')
                not_allowed_order.append('0')
                if len(not_allowed_order) > n:
                    r = not_allowed_order.popleft()
                    if r != '0':
                        current_not_allowed.remove(r)
            while t:
                heapq.heappush(pq, t.pop())
            print(cycles)
            print(not_allowed_order)
            print(current_not_allowed)
            cycles += 1
        return cycles
            


        
        