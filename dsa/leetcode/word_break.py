##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 139. Word Break
# Problem link: https://leetcode.com/problems/word-break/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:

    def check_if_possible(self, s, ind, trie, temp, dp, word_start_ind):
        if (ind == len(s)):
            return temp[1]
        if dp[ind][word_start_ind] != -1:
            return dp[ind][word_start_ind]
        char = s[ind]
        if char not in temp[0]:
            dp[ind][word_start_ind] = 0
            return dp[ind][word_start_ind]
        if temp[0][char][1]:
            dp[ind+1][ind+1] = self.check_if_possible(s, ind+1, trie, trie, dp, ind+1)
        dp[ind+1][word_start_ind] = self.check_if_possible(s, ind+1, trie, temp[0][char], dp, word_start_ind)

        dp[ind][word_start_ind] = 0
        if (dp[ind+1][word_start_ind] == 1) or (dp[ind+1][ind+1] == 1):
            dp[ind][word_start_ind] = 1
        return dp[ind][word_start_ind]


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        m = len(wordDict)

        trie = [{}, False]
        dp = [[-1] * (n+1) for i in range(n+1)]

        for i in range(m):
            word = wordDict[i]
            l = len(word)
            temp = trie
            for char in word:
                if char not in temp[0]:
                    temp[0][char] = [{}, False]
                temp = temp[0][char]
            temp[1] = True

        return self.check_if_possible(s, 0, trie, trie, dp, 0)




