##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 1143. Longest Common Subsequence
# Problem link: https://leetcode.com/problems/longest-common-subsequence/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0] * n2 for i in range(n1)]

        if text1[0] == text2[0]:
            dp[0][0] = 1

        for i in range(1, n1):
            dp[i][0] = max(dp[i - 1][0], (1 if (text1[i] == text2[0]) else 0))

        for j in range(1, n2):
            dp[0][j] = max(dp[0][j - 1], (1 if (text1[0] == text2[j]) else 0))

        for i in range(1, n1):
            for j in range(1, n2):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n1-1][n2-1]