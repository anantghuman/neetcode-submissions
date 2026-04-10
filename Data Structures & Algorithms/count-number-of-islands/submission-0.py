class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x < 0 or x > len(grid) - 1:
                return
            if y < 0 or y > len(grid[x]) - 1:
                return
            if grid[x][y] == '0':
                return
            if grid[x][y] == '1':
                grid[x][y] = '0'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == '1':
                    dfs(x, y)
                    count += 1
        return count

        