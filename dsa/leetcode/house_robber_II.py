##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 213. House Robber II
# Problem link: https://leetcode.com/problems/house-robber-ii/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for i in range(n)]
        dp[0][0] = nums[0]
        dp[0][1] = 0
        ans = dp[0][0]

        for i in range(1,n):
            dp[i][0] = nums[i]
            dp[i][1] = nums[i]
            for j in range(i-1):
                dp[i][1] = max(dp[i][1], nums[i] + dp[j][1])
                dp[i][0] = max(dp[i][0], nums[i] + dp[j][0])
            ans = max(ans, dp[i][1])
            if i < (n - 1):
                ans = max(ans, dp[i][0])
        return ans