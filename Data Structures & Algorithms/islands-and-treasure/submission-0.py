class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        queue = deque()

        def dist(grid, x, y):
            if 0 > x or x >= len(grid) or y < 0 or y >= len(grid[x]) or (x,y) in visited or grid[x][y] == -1:
                return 
            queue.append([x,y])
            visited.add((x,y))
            
            
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 0:
                    visited.add((x,y))
                    queue.append((x,y))
        
        d = 0
        while queue:
            for i in range(len(queue)):
                x,y = queue.popleft()
                grid[x][y] = d
                dist(grid, x + 1, y)
                dist(grid, x - 1, y)
                dist(grid, x, y - 1)
                dist(grid, x, y + 1)
            d += 1