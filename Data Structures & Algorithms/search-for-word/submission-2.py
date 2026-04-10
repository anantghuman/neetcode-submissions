class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, s, i):
            if (r, c) in s:
                return False
            if i >= len(word):
                return True
            if c < 0 or r < 0 or r >= len(board) or c >= len(board[0]):
                return False
            
            if board[r][c] == word[i]:
                print(r, c)
                s.add((r, c))
                if dfs(r + 1, c, s, i + 1) or dfs(r, c + 1, s, i + 1) or dfs(r - 1, c, s, i + 1) or dfs(r, c - 1, s, i + 1):
                    return True
                s.remove((r, c))
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, set(), 0):
                        return True
        return False


        