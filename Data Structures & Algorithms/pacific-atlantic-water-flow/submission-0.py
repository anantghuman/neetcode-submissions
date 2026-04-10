class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(r, c, ocean, prevHeight):
            if (r, c) in ocean or r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]) or heights[r][c] < prevHeight:
                return
            ocean.add((r, c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        atl = set()
        pac = set()

        for i in range(len(heights)):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, len(heights[i]) - 1, atl, heights[i][len(heights[i]) - 1])

        for i in range(len(heights[0])):
            dfs(0, i, pac, heights[0][i])
            dfs(len(heights) - 1, i, atl, heights[len(heights) - 1][i])
        
        arr = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in pac and (r, c) in atl:
                    arr.append([r,c])
        return arr


        
        