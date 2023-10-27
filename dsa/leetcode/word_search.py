##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 79. Word Search
# Problem link: https://leetcode.com/problems/word-search/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def dfs(self, board, r, c, visited, word, ind):
        m = len(board)
        n = len(board[0])
        if visited[r][c]:
            return False
        if board[r][c] != word[ind]:
            return False
        elif ind == len(word) - 1:
            return True
        visited[r][c] = True
        directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        directions_len = len(directions)
        for i in range(directions_len):
            new_r = r + directions[i][0]
            new_c = c + directions[i][1]
            if (new_r >= 0 and new_r < m) and (new_c >= 0 and new_c < n) and not visited[new_r][new_c] :
                if self.dfs(board, new_r, new_c, visited, word, ind+1):
                    return True
        visited[r][c] = False
        return False



    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                visited = [[False] * n for k in range(m)]
                if self.dfs(board, i, j, visited, word, 0):
                    return True
        return False