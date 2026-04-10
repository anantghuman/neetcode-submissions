class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    dp[row][col] = 1
                elif row == 0:
                    dp[row][col] = dp[row][col - 1]
                elif col == 0:
                    dp[row][col] = dp[row - 1][col]
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[m - 1][n - 1]
        