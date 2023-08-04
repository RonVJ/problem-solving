class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    if ((j == 0) or ((j > 0) and (board[i][j-1] == "."))) and ((i == 0) or ((i > 0) and (board[i-1][j] == "."))):
                        count = count + 1
        return count