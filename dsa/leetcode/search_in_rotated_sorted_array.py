##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 33. Search in Rotated Sorted Array
# Problem link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def binary_search(self, nums, l, r, target):
        while l <= r:
            m = (l + (r - l)//2)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if nums[0] <= nums[n-1]:
            pivot = 0
        else:
            l = 0
            r = n - 1
            while l <= r:
                m = (l + r)//2
                if ((m > 0) and (nums[m] < nums[m - 1])) and ((m < (n - 1)) and (nums[m] < nums[m + 1])):
                    break
                else:
                    if nums[m] >= nums[0]:
                        l = m + 1
                    else:
                        r = m - 1
                print (str(m) + " " + str(nums[m]))
            pivot = m

        if target <= nums[n - 1]:
            return self.binary_search(nums, pivot, n - 1, target)
        return self.binary_search(nums, 0, pivot - 1, target)
