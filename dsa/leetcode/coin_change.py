##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 322. Coin Change
# Problem link: https://leetcode.com/problems/coin-change/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = 1000000000
        dp = [inf]*(amount+1)
        dp[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if (i - coin) >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        ans = -1
        if dp[amount] < inf:
            ans = dp[amount]

        return ans