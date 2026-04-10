class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        q = deque()
        visited = set()
        count = [0]
        def rot(grid, x, y):
            if x < 0 or x >= r or y < 0 or y >= c:
                return
            if (x,y) in visited:
                return
            visited.add((x, y))
            if grid[x][y] == 0:
                return
            if grid[x][y] == 1:
                count[0] -= 1
                q.append([x,y])






        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    visited.add((i, j))
                    q.append([i,j])
                elif grid[i][j] == 1:
                    count[0] += 1
        minutes = 0
        while q:
            if count[0] == 0:
                return minutes
            for i in range(len(q)):
                x, y = q.popleft()
                rot(grid, x + 1, y)
                rot(grid, x - 1, y)
                rot(grid, x, y - 1)
                rot(grid, x, y + 1)
            minutes += 1

        return -1 if count[0] != 0 else 0