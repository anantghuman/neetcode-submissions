class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        indegree = [0] * n
        hm = defaultdict(set)
        for edge in edges:
            if edge[0] == edge[1]:
                return False
            hm[edge[0]].add(edge[1])
            hm[edge[1]].add(edge[0])


        queue = deque()
        queue.append((0,0))
        visited = set()
        visited.add(0)

        while queue:
            for i in range(len(queue)):
                parent, child = queue.popleft()
                for v in hm[child]:
                    if v not in visited:
                        queue.append((child, v))
                        visited.add(v)
                    elif v in visited and v != parent:
                        return False

        return len(visited) == n

        