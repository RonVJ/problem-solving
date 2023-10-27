##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 212. Word Search II
# Problem link: https://leetcode.com/problems/word-search-ii/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def dfs(self, board, visited, r, c, trie, ans):
        m = len(board)
        n = len(board[0])

        if (r < 0) or (r >= m) or (c < 0) or (c >= n) or visited[r][c] or (not trie) or (board[r][c] not in trie[0]):
            return
        char = board[r][c]
        if trie[0][char][1]:
            ans.add(trie[0][char][2])


        visited[r][c] = True
        temp = trie[0][char]
        self.dfs(board, visited, r-1, c, temp, ans)
        self.dfs(board, visited, r+1, c, temp, ans)
        self.dfs(board, visited, r, c-1, temp, ans)
        self.dfs(board, visited, r, c+1, temp, ans)
        visited[r][c] = False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        num_words = len(words)

        trie = [{}, False, ""]

        for i in range(num_words):
            word_len = len(words[i])
            temp = trie
            for j in range(word_len):
                c = words[i][j]
                if c not in temp[0]:
                    temp[0][c] = [{}, False, ""]
                temp = temp[0][c]
            temp[1] = True
            temp[2] = words[i]

        ans = set()
        for i in range(m):
            for j in range(n):
                visited = [[False]*n for k in range(m)]
                self.dfs(board, visited, i, j, trie, ans)
        return ans