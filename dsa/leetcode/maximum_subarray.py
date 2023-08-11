##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 53. Maximum Subarray
# Problem link: https://leetcode.com/problems/maximum-subarray/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        total = nums[0]

        for i in range(1, n):
            total = max(0, total) + nums[i]
            if total > ans:
                ans = total
        return ans