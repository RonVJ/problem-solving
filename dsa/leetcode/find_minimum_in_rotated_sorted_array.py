##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 153. Find Minimum in Rotated Sorted Array
# Problem link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        if nums[0] <= nums[n - 1]:
            pivot = 0
        else:
            l = 0
            r = n - 1

            while l <= r:
                m = (l + r)//2
                if ((m > 0) and (nums[m] < nums[m - 1])) and ((m < n-1) and (nums[m] < nums[m + 1])) :
                    break
                if nums[m] >= nums[0]:
                    l = m + 1
                else:
                    r = m - 1
            pivot = m

        return nums[pivot]