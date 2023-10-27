##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 452. Minimum Number of Arrows to Burst Balloons
# Problem link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: (x[1], x[0]))

        i = 0
        num_arrows_required = 1
        last_arrow_shot_at = points[0][1]

        while i < n:
            if (points[i][0] <= last_arrow_shot_at) and (points[i][1] >= last_arrow_shot_at):
                i = i + 1
            else:
                num_arrows_required = num_arrows_required + 1
                last_arrow_shot_at = points[i][1]
        return num_arrows_required