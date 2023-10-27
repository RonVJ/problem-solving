##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 55. Jump Game
# Problem link: https://leetcode.com/problems/jump-game/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        reachable = 0
        for i in range(n):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
        return True