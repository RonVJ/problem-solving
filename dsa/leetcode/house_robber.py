##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 198. House Robber
# Problem link: https://leetcode.com/problems/house-robber/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1, n):
            dp[i] = nums[i]
            for j in range(i-1):
                dp[i] = max(dp[i], dp[j] + nums[i])
            ans = max(ans, dp[i])
        return ans
