##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 11. Container With Most Water
# Problem link: https://leetcode.com/problems/container-with-most-water/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_volume = 0
        while l < r:
            volume = (r - l) * min(height[l], height[r])
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
            max_volume = max(max_volume, volume)
        return max_volume