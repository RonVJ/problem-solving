##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 70. Climbing Stairs
# Problem link: https://leetcode.com/problems/climbing-stairs/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        last_step_ways = 2
        second_last_step_ways = 1
        for i in range(3, n + 1):
            cur_step_ways = last_step_ways + second_last_step_ways
            second_last_step_ways = last_step_ways
            last_step_ways = cur_step_ways

        return cur_step_ways