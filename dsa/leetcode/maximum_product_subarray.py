##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 152. Maximum Product Subarray
# Problem link: https://leetcode.com/problems/maximum-product-subarray/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = nums[0]
        min_product = nums[0]
        ans = nums[0]
        i = 1
        while i < n:
            if nums[i] > 0:
                max_product = max(1, max_product) * nums[i]
                min_product = min(1, min_product) * nums[i]
            elif nums[i] < 0:
                old_min_product = min_product
                min_product = max(1, max_product) * nums[i]
                max_product = min(1, old_min_product) * nums[i]
            else:
                ans = max(ans, 0)
                if i < (n - 1):
                    max_product = nums[i + 1]
                    min_product = nums[i + 1]
                    i = i + 1
            i = i + 1
            ans = max(ans, max_product)
        return ans