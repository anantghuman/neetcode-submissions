class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = 0

        def dfs(x, y):
            if x < 0 or x > len(grid) - 1:
                return 0
            if y < 0 or y > len(grid[x]) - 1:
                return 0
            if grid[x][y] == 0:
                return 0
            if grid[x][y] == 1:
                grid[x][y] = 0
            return 1 + dfs(x+1, y) + dfs(x-1, y) + dfs(x, y+1) + dfs(x, y-1)

    
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    m = max(m, dfs(x, y))
        return m
                
        