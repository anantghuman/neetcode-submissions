class Solution:
    def solve(self, board: List[List[str]]) -> None:
        not_trapped = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return
            if board[r][c] == 'X':
                return
            if board[r][c] == 'O':
                board[r][c] = 'T'
            else:
                return
            not_trapped.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        
        for i in range(len(board)):
            dfs(i, 0)
        for i in range(len(board[0])):
            dfs(0, i)
        for i in range(len(board)):
            dfs(i, len(board[0]) - 1)
        for i in range(len(board[0])):
            dfs(len(board) - 1, i)


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'