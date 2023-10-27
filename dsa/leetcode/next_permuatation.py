##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 31. Next Permutation
# Problem link: https://leetcode.com/problems/next-permutation/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def reverse_array_in_range(self, nums, ind):
        n = len(nums)
        i = ind
        j = n-1

        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i = i + 1
            j = j - 1

    def get_ind_of_just_greater_than(self, nums, ind, target):
        n = len(nums)
        l = ind
        r = n - 1

        while l <= r:
            m = (l + r)//2
            if nums[m] > target:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        i = n-1
        while i > 0:
            if nums[i] > nums[i-1]:
                self.reverse_array_in_range(nums, i)
                ind = self.get_ind_of_just_greater_than(nums, i, nums[i-1])
                temp = nums[i-1]
                nums[i-1] = nums[ind]
                nums[ind] = temp
                break
            i = i - 1
        if i == 0:
            self.reverse_array_in_range(nums, 0)