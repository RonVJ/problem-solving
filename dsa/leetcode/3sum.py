##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 15. 3Sum
# Problem link: https://leetcode.com/problems/3sum/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        ans = set()
        for i in range(n):
            l = i+1
            r = n-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    ans.add((nums[i], nums[l], nums[r]))
                    l = l+1
                    r = r-1
                elif sum < 0:
                    l = l+1
                else:
                    r = r-1
        return list(ans)